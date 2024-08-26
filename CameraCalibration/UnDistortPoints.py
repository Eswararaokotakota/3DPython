# import cv2 as cv
# import pickle
# import numpy as np

# # Load calibration parameters
# calibration_params = pickle.load(open(r"E:\Coding\Python\DepthAnything\CameraCalibration\results\calibration_params.pkl", "rb"))

# cameraMatrix = calibration_params['cameraMatrix']
# dist = calibration_params['dist']
# newCameraMatrix = calibration_params['newCameraMatrix']
# roi = calibration_params['roi']

# # Load the image to undistort
# img = cv.imread(r"E:\Coding\Python\DepthAnything\CameraCalibration\images\2.png")

# # Get image size
# h, w = img.shape[:2]

# # Generate a grid of points (pixel coordinates)
# grid_x, grid_y = np.meshgrid(np.arange(w), np.arange(h))
# points = np.vstack((grid_x.ravel(), grid_y.ravel())).T.astype(np.float32)

# # Undistort the points using cv.undistortPoints
# undistorted_points = cv.undistortPoints(points, cameraMatrix, dist, None, newCameraMatrix)

# # Reshape the undistorted points to match the image
# undistorted_points = undistorted_points.reshape(h, w, 2)

# # Remap the image using the undistorted points
# map_x, map_y = cv.convertMaps(undistorted_points[..., 0], undistorted_points[..., 1], cv.CV_32FC1)
# dst = cv.remap(img, map_x, map_y, interpolation=cv.INTER_LINEAR)

# # Crop the image using the ROI
# x, y, w, h = roi
# dst = dst[y:y+h, x:x+w]

# # Save the undistorted and cropped image
# cv.imwrite(r'E:\Coding\Python\DepthAnything\CameraCalibration\images\caliResult_frame_2_undistort_points.png', dst)
import cv2 as cv
import pickle
import numpy as np

# Load calibration parameters
calibration_params = pickle.load(open(r"E:\Coding\Python\DepthAnything\CameraCalibration\results\calibration_params.pkl", "rb"))

cameraMatrix = calibration_params['cameraMatrix']
dist = calibration_params['dist']
newCameraMatrix = calibration_params['newCameraMatrix']
roi = calibration_params['roi']

# Load the image to undistort
img = cv.imread(r"E:\Coding\Python\DepthAnything\CameraCalibration\images\2.png")

# Get image size
h, w = img.shape[:2]

# Generate the undistortion and rectification maps
map1, map2 = cv.initUndistortRectifyMap(cameraMatrix, dist, None, newCameraMatrix, (w, h), cv.CV_32FC1)

# Remap the image using the generated maps
dst = cv.remap(img, map1, map2, interpolation=cv.INTER_LINEAR)

# Crop the image using the ROI
x, y, w, h = roi
dst = dst[y:y+h, x:x+w]

# Save the undistorted and cropped image
cv.imwrite(r'E:\Coding\Python\DepthAnything\CameraCalibration\images\caliResult_frame_2_undistort_rectifymap_uncropped.png', dst)
