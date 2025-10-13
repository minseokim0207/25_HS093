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