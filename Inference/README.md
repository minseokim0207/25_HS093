# Inference on Hailo-8
### 실시간 추론 코드는 Hailo RPi5 Basic Pipelines의 예제를 참고하였습니다.
---
## 🚀 Step 1. Installation
### 1) Installing AI HAT Software and Python Pipelines
```bash
git clone https://github.com/hailo-ai/hailo-rpi5-examples.git
```
```bash
cd hailo-rpi5-examples
```
```bash
./install.sh
```
### 2) Installing the HAT Firmware with
```bash
sudo apt install hailo-all
```
```bash
sudo reboot
```
### 3) Set PCIe to Gen3
성능 최적화를 위해 PCle 전송 속도를 Gen3로 설정합니다.
```bash
sudo raspi-config
```
**"6 Advanced Options"** -> **"A8 PCIe Speed"** -> **"Yes" to enable PCIe Gen 3 mode**
```bash
sudo reboot
```
---
## 🚀 Step2. Runing real-time inference example
label.json 파일을 생성합니다.
```json
[
   {
    "detection_threshold": 0.1,
    "max_boxes": 10,
    "labels": 
    [
        " ",
        "fall",
        "normal",
        "bed"
    ]
    }
  ]
```
```bash
.source setup_env.sh
```
**변환 파일(CareBuddy.hef)**, **추론 코드(CareBuddy.py)** 및 **label 파일(label.json)** 을 지정해 줍니다.
```bash
python basic_pipelines/CareBuddy.py --labels-json ./label.json --hef-path ./CareBuddy.hef  --input rpi
```
---
---
## 🚀 Step3. Source Code Analysis
본 코드는 Hailo RPi5 Basic Pipelines 예제를 기반으로 수정 및 확장하여,
실시간 낙상 감지 및 알림 기능을 구현한 예제입니다.
GStreamer 기반 추론 파이프라인에서 객체 감지 결과를 받아
오디오 알람 재생 및 TCP 메시지 전송을 수행합니다.
### 1) 라이브러리 및 환경 설정
```python
import os, socket, time, threading, subprocess
from collections import deque
from pathlib import Path
import gi
gi.require_version('Gst', '1.0')
from gi.repository import Gst
import hailo
from hailo_apps.hailo_app_python.core.gstreamer.gstreamer_app import app_callback_class
from hailo_apps.hailo_app_python.apps.detection_simple.detection_pipeline_simple import GStreamerDetectionApp
```
### 2)파라미터 정의
```python
LABELS_AND_AUDIO = {"fall": "/home/user/CareBuddy.mp3"}
CONF_THRESH = 0.70
BED_CONF_THRESH = 0.30
AUDIO_PLAY_DELAY = 2.0
HOST = "0.0.0.0"
PORT = 12345
SMOOTHING_WINDOW = 5  
```
### 3) 앱연동을 위한 TCP서버 클래스 정의
```python
class TCPServer:
    def __init__(self, host, port):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind((host, port))
        self.sock.listen()
        print("[TCP] Server start, waiting for client...")
        self.conn, self.addr = self.sock.accept()
        print(f"[TCP] Client connected: {self.addr}")

    def send(self, message: str):
        try:
            self.conn.sendall(message.encode())
            print(f"[TCP] send: {message}")
        except Exception as e:
            print(f"[TCP] Error: {e}")
```
### 4) 알림 출력을 위한 사운드 재생 클래스 정의
```python
class SoundPlayer:
    def __init__(self, audio_path: Path):
        self.audio_path = Path(audio_path).resolve()
        if not self.audio_path.exists():
            raise FileNotFoundError(f"Audio file not found: {self.audio_path}")
        self._lock = threading.Lock()

    def _play_gstreamer(self):
        pipeline = Gst.parse_launch(f'playbin uri=file://{self.audio_path}')
        pipeline.set_state(Gst.State.PLAYING)
        bus = pipeline.get_bus()
        bus.timed_pop_filtered(10*Gst.SECOND, Gst.MessageType.EOS|Gst.MessageType.ERROR)
        pipeline.set_state(Gst.State.NULL)
        del pipeline

    def play(self):
        def worker():
            try: self._play_gstreamer()
            except: subprocess.run(["aplay","-q",str(self.audio_path)],check=False)
        with self._lock:
            threading.Thread(target=worker,daemon=True).start()
```            
### 5) Center Suppression 함수 정의
낙상으로 감지된 객체의 중심점이 침대 영역 안에 있을 경우 낙상으로 처리하지 않도록 필터링 처리합니다.
```python
def is_center_inside(fall_box, bed_box):
    fx, fy, fw, fh = fall_box.xmin(), fall_box.ymin(), fall_box.width(), fall_box.height()
    bx, by, bw, bh = bed_box.xmin(), bed_box.ymin(), bed_box.width(), bed_box.height()
    cx, cy = fx + fw/2, fy + fh/2
    return (bx <= cx <= bx + bw) and (by <= cy <= by + bh)
```
### 6) 사용자 콜백 클래스 정의
```python
class user_app_callback_class(app_callback_class):
    def __init__(self, players=None, tcp_server=None):
        super().__init__()
        self.players=players
        self.tcp_server=tcp_server
        self.last_global_play_ts=0.0
        self.fall_history = deque(maxlen=SMOOTHING_WINDOW)
```
### 7) 추론 콜백 함수 정의
```python
def app_callback(pad, info, user_data: user_app_callback_class):
    buffer=info.get_buffer()
    if buffer is None: return Gst.PadProbeReturn.OK
    roi=hailo.get_roi_from_buffer(buffer)
    detections=roi.get_objects_typed(hailo.HAILO_DETECTION)
    now=time.time()
```
#### - "bed" class의 바운딩 박스만 필터링
```python
    fall_detected=False
    bed_boxes=[d.get_bbox() for d in detections if d.get_label()=="bed" and d.get_confidence()>=BED_CONF_THRESH]
```
#### - “fall” class만 선별, 신뢰도 기준(0.7 이상)
```python
    for det in detections:
        if det.get_label()!="fall" or det.get_confidence()<CONF_THRESH: 
            continue
        fall_box=det.get_bbox()
````
#### - "fall"의 중심점이 "bed"안에 있으면 무시
```python
        if any(is_center_inside(fall_box,b) for b in bed_boxes):
            print("[INFO] Fall ignored (center suppression).")
            continue

        fall_detected=True
```
#### - 최근 5프레임(SMOOTHING_WINDOW) 중 과반 이상 낙상 감지 시 → 실제 낙상으로 판단
```python
    user_data.fall_history.append(fall_detected)

    smoothed_fall = sum(user_data.fall_history) > (len(user_data.fall_history)//2)
```
#### - 모든 조건 충족시 오디오 알림 재생 및 TCP 메시지 전송
```python
    if smoothed_fall:
        if (now-user_data.last_global_play_ts)>=AUDIO_PLAY_DELAY:
            user_data.players["fall"].play()
            if user_data.tcp_server: user_data.tcp_server.send("Fall")
            user_data.last_global_play_ts=now
    return Gst.PadProbeReturn.OK
```
#### - 메인 실행부
```python
if __name__=="__main__":
    Gst.init(None)
    tcp_server=TCPServer(HOST,PORT)
    players={"fall":SoundPlayer(Path(LABELS_AND_AUDIO["fall"]))}
    user_data=user_app_callback_class(players,tcp_server)
    app=GStreamerDetectionApp(app_callback,user_data)
    app.run()
```
---



