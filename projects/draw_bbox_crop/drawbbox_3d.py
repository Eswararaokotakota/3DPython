import open3d as o3d
import numpy as np
import cv2 as cv

def draw_bbox(event, x, y, flags, param):
    global bbox, drawing, img_resized

    if event == cv.EVENT_LBUTTONDOWN:
        drawing = True
        bbox = [(x, y)]

    elif event == cv.EVENT_MOUSEMOVE:
        if drawing:
            img_copy = img_resized.copy()
            cv.rectangle(img_copy, bbox[0], (x, y), (0, 255, 0), 2)
            cv.imshow("Draw Bounding Box", img_copy)

    elif event == cv.EVENT_LBUTTONUP:
        drawing = False
        bbox.append((x, y))
        cv.rectangle(img_resized, bbox[0], bbox[1], (0, 255, 0), 2)
        cv.imshow("Draw Bounding Box", img_resized)

def crop_point_cloud(point_cloud, bbox, img_width, img_height):
    # Scale bbox back to original size
    bbox = [(int(x / 2), int(y / 2)) for x, y in bbox]

    x1, y1 = bbox[0]
    x2, y2 = bbox[1]
    x_min = min(x1, x2) / img_width
    x_max = max(x1, x2) / img_width
    y_min = min(y1, y2) / img_height
    y_max = max(y1, y2) / img_height

    # Crop the 3D point cloud based on the normalized bbox
    points = np.asarray(point_cloud.points)
    colors = np.asarray(point_cloud.colors)
    mask = (
        (points[:, 0] >= x_min) & (points[:, 0] <= x_max) &
        (points[:, 1] >= y_min) & (points[:, 1] <= y_max)
    )
    cropped_points = points[mask]
    cropped_colors = colors[mask]

    cropped_point_cloud = o3d.geometry.PointCloud()
    cropped_point_cloud.points = o3d.utility.Vector3dVector(cropped_points)
    cropped_point_cloud.colors = o3d.utility.Vector3dVector(cropped_colors)
    return cropped_point_cloud

# Load the 2D image
img_path = r"E:\Coding\Python\DepthAnything\2d_3d\cityhawkdata\right_cam\frame_0030.png"
img = cv.imread(img_path)
img_height, img_width = img.shape[:2]

# Resize the image 2x for easier bbox drawing
img_resized = img#cv.resize(img, (img_width * 2, img_height * 2))

# Initialize variables
bbox = []
drawing = False

# Show the resized image and set up the mouse callback to draw the bounding box
cv.imshow("Draw Bounding Box", img_resized)
cv.setMouseCallback("Draw Bounding Box", draw_bbox)
cv.waitKey(0)
cv.destroyAllWindows()

# Ensure a bounding box was drawn
if len(bbox) == 2:
    # Load the corresponding point cloud
    ply_file_path = r"E:\Coding\Python\DepthAnything\2d_3d\cityhawkdata\right_cam\frame_0030.ply"
    point_cloud = o3d.io.read_point_cloud(ply_file_path)

    # Crop the point cloud using the bounding box
    cropped_point_cloud = crop_point_cloud(point_cloud, bbox, img_width, img_height)

    # Save and display the cropped point cloud
    cropped_ply_file_path = "cropped_point_cloud.ply"
    o3d.io.write_point_cloud(cropped_ply_file_path, cropped_point_cloud)
    o3d.visualization.draw_geometries([cropped_point_cloud])
    print(f"Cropped point cloud saved to: {cropped_ply_file_path}")
else:
    print("No bounding box drawn.")
