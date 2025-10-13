# Model Conversion: From YOLOv8.pt to Hailo-8.hef

이 문서는 CareBuddy 프로젝트에서 YOLOv8 학습 모델을 Hailo-8 AI 가속기에서 실행 가능한 **HEF 파일**로 변환하는 과정을 정리한 매뉴얼입니다. 

모든 과정은 **Docker 환경(Hailo-8 AI SW Suite)** 내부에서 실행됩니다.

---

## 📌 변환 전체 흐름
1. YOLOv8 모델(.pt) → ONNX 변환  
2. ONNX → HAR 변환  
3. Calibration 이미지 → NPY 변환 
4. CHW → NHWC 변환  
5. HAR 최적화  
6. HEF 최종 생성  

---

## 🚀 Step 1. Docker 컨테이너 접속
```bash
docker exec -it hailo_docker bash
```
---
## 🚀 Step 2. PT → ONNX(Open Neural Network Exchange) 변환
```bash
>>import torch 
from ultralytics import YOLO 
# Load a trained Pytorch model
model = YOLO("CareBuddy.pt") 
# ONNX conversion (with a 640x640 input) 
model.export(format="onnx", opset=13, imgsz=640, simplify=True) 
```
---
## 🚀 Step 3. ONNX → HAR(Hailo Archive) 변환
---
```bash
hailo parser onnx CareBuddy.onnx \
  --har-path CareBuddy.har \
  --hw-arch hailo8 \
  -y
```
---
## 🚀 Step 4. Calibration JPG → NPY 변환
-Calibration: 학습된 모델을 정수 연산(INT8) 으로 변환하기 위해 실제와 유사한 이미지 데이터를 사용하여 모델의 분포를 보정하는 과정입니다.

-NPY 변환: Calibration에 사용할 이미지를 모델 입력 형식에 맞게 전처리 후 NPY 파일로 변환해야 Hailo 툴에서 읽고 사용할 수 있습니다.
```python
import numpy as np
import cv2, glob, os

input_size = (640, 640)
image_dir = "calib"
output_dir = "calib_npy"
os.makedirs(output_dir, exist_ok=True)

for idx, img_path in enumerate(glob.glob(os.path.join(image_dir, "*.jpg"))):
    img = cv2.imread(img_path)
    img = cv2.resize(img, input_size)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = img.astype(np.float32) / 255.0
    img = np.transpose(img, (2, 0, 1))
    img = np.expand_dims(img, axis=0) 
    np.save(os.path.join(output_dir, f"calib_{idx}.npy"), img)

print("Conversion completed:", len(glob.glob(os.path.join(output_dir, '*.npy'))))

```
```bash
python3 convert_to_npy.py
```
---
## 🚀 Step 5. NPY → NHWC 변환
-Hailo 도구는 Calibration 데이터를 **NHWC(Height, Width, Channels)** 형식으로 요구하지만,
PyTorch/OpenCV는 기본적으로 **CHW(Channels, Height, Width)** 형식으로 저장합니다.
따라서 INT8 양자화를 올바르게 수행하려면 **CHW → NHWC 변환**이 필수적입니다.
```python
import numpy as np
import glob, os

# Input / Output directories
in_dir = "calib_npy"        # Folder containing NPY files
out_dir = "calib_nhwc"      # Folder to save NHWC files
os.makedirs(out_dir, exist_ok=True)

for f in glob.glob(os.path.join(in_dir, "*.npy")):
    arr = np.load(f)

    if arr.ndim == 4 and arr.shape[1] == 3:
        arr = np.squeeze(arr, axis=0)
        arr = np.transpose(arr, (1, 2, 0))

    elif arr.ndim == 3 and arr.shape[0] == 3:
        arr = np.transpose(arr, (1, 2, 0))

    else:
        print(f"Unexpected shape {arr.shape} in {f}, skipped")
        continue

    out_path = os.path.join(out_dir, os.path.basename(f))
    np.save(out_path, arr)
    print(f"{f} → {out_path}  {arr.shape}")

print("Conversion completed")
```
```bash
python3 calib_nhwc.py
```
---
## 🚀 Step 6. HAR Optimization
-Hailo-8 하드웨어에서 최대 성능을 내도록 연산 구조를 int8로 재배치하는 과정입니다.
```bash
hailo optimize CareBuddy.har \
  --hw-arch hailo8 \
  --calib-set-path ./calib_nhwc/ \
  --output-har-path CareBuddy_OPT.har
```
---
## 🚀Step 7. HEF(Hailo Execution File) 파일 생성
**CareBuddy.pt → CareBuddy.hef** 로 변환 완료됩니다. 
```bash
hailo compiler CareBuddy_OPT.har \
  --hw-arch hailo8 \
  --output-dir .
```
