import cv2 as cv
import pickle
import numpy as np

# Load calibration parameters
calibration_params = pickle.load(open(r"E:\Coding\Python\DepthAnything\CameraCalibration\results\calibration_params_50imgs.pkl", "rb"))

cameraMatrix = calibration_params['cameraMatrix']
dist = calibration_params['dist']
newCameraMatrix = calibration_params['newCameraMatrix']
roi = calibration_params['roi']

# Load the image to undistort
img = cv.imread(r"E:\Coding\Python\DepthAnything\CameraCalibration\images\frame36.png")

# Undistort
dst = cv.undistort(img, cameraMatrix, dist, None, newCameraMatrix)



# Crop the image
x, y, w, h = roi
dst = dst[y:y+h, x:x+w]


# Pad the undistorted image to the original size
# Resize the undistorted image to match the ROI size
# x, y, w, h = roi
# resized_dst = cv.resize(dst, (w, h), interpolation=cv.INTER_LINEAR)
# # Get original image size
# original_h, original_w = img.shape[:2]
# # Pad the undistorted image to the original size
# padded_dst = np.zeros((original_h, original_w, 3), dtype=np.uint8)
# padded_dst[y:y+h, x:x+w] = resized_dst
cv.imwrite(r'E:\Coding\Python\DepthAnything\CameraCalibration\images\caliResult_frame36_50imgs.png', dst)
