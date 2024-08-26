import open3d as o3d

# Load the PLY file as a point cloud
ply_file_path = r"e:\Coding\Python\DepthAnything\2d_images\calib_imgs\depthanything\2.ply"
point_cloud = o3d.io.read_point_cloud(ply_file_path)

# Visualize the entire point cloud to inspect it
o3d.visualization.draw_geometries([point_cloud], window_name="Original Point Cloud")

# Get the minimum and maximum bounds of the point cloud
min_bound = point_cloud.get_min_bound()
max_bound = point_cloud.get_max_bound()

print(f"Minimum bounds: {min_bound}")
print(f"Maximum bounds: {max_bound}")

# Define a bounding box based on the min and max bounds
# You can manually adjust these to focus on your region of interest
bbox = o3d.geometry.AxisAlignedBoundingBox(min_bound, max_bound)

# Optionally, you can shrink the bounding box to focus on the area of interest
# For example, tighten the bounds by a fixed margin:
margin = 0.1  # Adjust this margin as needed
bbox = o3d.geometry.AxisAlignedBoundingBox(
    min_bound + margin,
    max_bound - margin
)

# Crop the point cloud using the bounding box
cropped_point_cloud = point_cloud.crop(bbox)

# Visualize the cropped point cloud to see the result
o3d.visualization.draw_geometries([cropped_point_cloud], window_name="Cropped Point Cloud")

# Proceed with further processing on the cropped point cloud
