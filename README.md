## **💡1. 프로젝트 개요**

**1-1. 프로젝트 소개**
- 프로젝트 명 : **CareBuddy** (케어버디)
- 프로젝트 정의 : 고령자 및 돌봄 대상자의 안전을 지키고 돌봄 부담을 완화하는 **레일 주행형 AI 모바일 로봇**
  
   <img width="650" height="300" alt="image" src="https://github.com/minseokim0207/assets/blob/master/img/mainImage.jpg?raw=true" /></br>

**1-2. 개발 배경 및 필요성**
 
  1) 초고령화 사회 대응과 돌봄 인력 부족 해결 필요

 - 통계청의 ‘2024 고령자 통계’ 에 따르면, 2025년 65세 이상 고령 인구 전체 인구의 20% 이상 약 1,051만 명 예상
   
   <img width="650" height="300" alt="image" src="https://github.com/minseokim0207/assets/blob/master/img/populationExpectation.png?raw=true" /></br>
   
  - 현재 1명의 요양보호사가 5.3~8.8명의 대상자를 담당하는 등 과중한 업무 현실
  - 요양보호사 수요 급증에도 불구하고, 2028년까지 약 11만 명 부족 예상
    
    <img width="650" height="300" alt="image" src="https://github.com/minseokim0207/assets/blob/master/img/ShortageOfNursingStaff.png?raw=true" /></br>
  
  2) 스마트 케어 시스템을 통해 효율적이고 지속 가능한 돌봄 환경 마련 필요


**1-3. 프로젝트 특장점**
- 기존 돌봄 장비 대비 실시간성과 정밀성이 향상된 스마트 시스템
  
  <img width="650" height="250" alt="image" src="https://github.com/minseokim0207/assets/blob/master/img/chart1.png?raw=true" /></br> 
- 기존 CCTV 기반 모니터링 대비 개선 효과
  
  <img width="650" height="300" alt="image" src="https://github.com/minseokim0207/assets/blob/master/img/chart2.png?raw=true" /></br>
 
**1-4. 주요 기능**
- **On Device AI**: Hailo-8 기반 로컬 AI 추론으로 네트워크 없이 저지연·고속 연산 가능
- **실시간 이동형 관측 시스템**: 레일형 로봇이 천장 구조를 따라 이동하여 사각지대 문제 해소
- **NOIR 카메라 기반 야간 인식 기능**: 주.야간환경에서 24시간 실시간 감지 가능
- **모바일 실시간 알림 연동**: 이상행동 발생 시 보호자 앱으로 즉시 알림 전송
- **음성 인터페이스**: 이상행동 발생 시 블루투스 스피커를 통해 실내 경고 알림 제공


**1-5. 기대 효과 및 활용 분야**
1) 기대 효과 
- **즉각 대응**: 이상행동(낙상) 실시간 감지 → 음성/앱 알림으로 보호자 및 의료진의 신속한 대응 가능
- **사각지대 최소화**: 이동형 레일 로봇 + NOIR 카메라로 주야간 감시 및 사각지대 해소
- **통행 방해 해소**: 천장 설치 구조로 바닥 공간 점유 없이 설치 가능.

2) 활용 분야 
- **의료·돌봄**: 요양병원, 요양원, 장애인 시설 등에서 낙상·실신 등 이상행동 실시간 감지 및 알림
- **보육시설**: 유아의 위험 행동·쓰러짐 등 시야 밖 상황 자동 인식
- **산업 현장**: 작업자의 이상 동작·재해 상황 조기 감지로 안전사고 예방
- **스마트 홈**: 1인 가구·고위험군의 돌발 행동 감지 및 비상 대응 지원


**1-6. 기술 스택**
- 프론트엔드 : MIT App Inventor
- Edge Device : Raspberry Pi 5, Hailo-8 AI HAT+, Arduino Nano RP2040, TCP/IP
- AI/ML : YOLOv8, PyTorch, Hailo SDK
- 배포 및 관리 : Docker, GitHub Actions

---

## **💡2. 팀원 소개**
| <img width="80" height="100" src="https://github.com/minseokim0207/assets/blob/master/img/mentee1.jpg?raw=true" > | <img width="80" height="100" alt="image" src="https://github.com/minseokim0207/assets/blob/master/img/mentee2.jpg?raw=true" > | <img width="80" height="100" alt="image" src="https://github.com/minseokim0207/assets/blob/master/img/mentee3.jpg?raw=true" > | <img width="80" height="100" alt="image" src="https://github.com/minseokim0207/assets/blob/master/img/mentee4.jpg?raw=true" > | 
|:---:|:---:|:---:|:---:|
| **김민서** | **박건희** | **라영웅** | **김효주** |
| • 개발총괄 <br> • 데이터 분석 | • UI/UX 기획 <br> • 문서 작성 | • 하드웨어 제작 <br> • 프론트엔드 |• 하드웨어 설계 <br> • 임베디드 제어| 



---
## **💡3. 시스템 구성도**
- 서비스 흐름도
  
<img width="600" height="300" alt="image" src="https://github.com/minseokim0207/assets/blob/master/img/ServiceFlowChart1.png?raw=true" />

- S/W 구성도
  
<img width="600" height="550" alt="image" src="https://github.com/minseokim0207/assets/blob/master/img/softwareConfigurationDiagram1.png?raw=true" />  

- H/W 구성도
  
<img width="1200" height="700" alt="image" src="https://github.com/minseokim0207/assets/blob/master/img/HardwareConfigurationDiagram.png?raw=true" />  


<!-- 엔티티 관계도
  
<img width="500" height="500" alt="image" src="https://github.com/user-attachments/assets/76e3347b-6d94-491e-8aeb-a7b4601c54d5" /> -->


---
## **💡4. 작품 소개영상**

[![한이음 드림업 프로젝트 소개](https://github.com/minseokim0207/assets/blob/master/img/youtubeImage.png?raw=true)](https://youtu.be/md-1Mj3nchI?si=9WYguuIe8CvcwUC6)


---
## **💡5. 핵심 소스코드**
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

LABELS_AND_AUDIO = {"fall": "/home/user/CareBuddy.mp3"}
CONF_THRESH = 0.70
BED_CONF_THRESH = 0.30
AUDIO_PLAY_DELAY = 2.0
HOST = "0.0.0.0"
PORT = 12345
SMOOTHING_WINDOW = 5   

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

def is_center_inside(fall_box, bed_box):
    fx, fy, fw, fh = fall_box.xmin(), fall_box.ymin(), fall_box.width(), fall_box.height()
    bx, by, bw, bh = bed_box.xmin(), bed_box.ymin(), bed_box.width(), bed_box.height()
    cx, cy = fx + fw/2, fy + fh/2
    return (bx <= cx <= bx + bw) and (by <= cy <= by + bh)

class user_app_callback_class(app_callback_class):
    def __init__(self, players=None, tcp_server=None):
        super().__init__()
        self.players=players
        self.tcp_server=tcp_server
        self.last_global_play_ts=0.0
        self.fall_history = deque(maxlen=SMOOTHING_WINDOW)

def app_callback(pad, info, user_data: user_app_callback_class):
    buffer=info.get_buffer()
    if buffer is None: return Gst.PadProbeReturn.OK
    roi=hailo.get_roi_from_buffer(buffer)
    detections=roi.get_objects_typed(hailo.HAILO_DETECTION)
    now=time.time()

    fall_detected=False
    bed_boxes=[d.get_bbox() for d in detections if d.get_label()=="bed" and d.get_confidence()>=BED_CONF_THRESH]

    for det in detections:
        if det.get_label()!="fall" or det.get_confidence()<CONF_THRESH: 
            continue
        fall_box=det.get_bbox()

        if any(is_center_inside(fall_box,b) for b in bed_boxes):
            print("[INFO] Fall ignored (center suppression).")
            continue

        fall_detected=True

    user_data.fall_history.append(fall_detected)

    smoothed_fall = sum(user_data.fall_history) > (len(user_data.fall_history)//2)

    if smoothed_fall:
        if (now-user_data.last_global_play_ts)>=AUDIO_PLAY_DELAY:
            user_data.players["fall"].play()
            if user_data.tcp_server: user_data.tcp_server.send("Fall")
            user_data.last_global_play_ts=now
    return Gst.PadProbeReturn.OK

if __name__=="__main__":
    Gst.init(None)
    tcp_server=TCPServer(HOST,PORT)
    players={"fall":SoundPlayer(Path(LABELS_AND_AUDIO["fall"]))}
    user_data=user_app_callback_class(players,tcp_server)
    app=GStreamerDetectionApp(app_callback,user_data)
    app.run()

```
