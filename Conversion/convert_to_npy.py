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
