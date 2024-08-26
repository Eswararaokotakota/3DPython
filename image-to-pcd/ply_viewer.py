import open3d as o3d

# Load the .ply file
pcd = o3d.io.read_point_cloud(r"E:\Coding\Python\DepthAnything\2d_3d\cityhawkdata\left_cam\depthanything\frame_0034_filtered_mesh.ply")

# Visualize the point cloud
o3d.visualization.draw_geometries([pcd])
