
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
