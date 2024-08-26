import open3d as o3d

# Load the PLY file as a point cloud
ply_file_path = r"c:\Users\oculo\Desktop\Eswar\DepthAnything\2d_images\depthanything\frame36_mesh.ply"

# Load the PLY file as a point cloud
pc = o3d.io.read_point_cloud(ply_file_path)
point_cloud = o3d.io.read_point_cloud(ply_file_path)

# Estimate normals for the point cloud
point_cloud.estimate_normals(search_param=o3d.geometry.KDTreeSearchParamHybrid(radius=0.1, max_nn=30))

# Optionally, orient the normals consistently
point_cloud.orient_normals_consistent_tangent_plane(k=30)

# Display the point cloud with estimated normals
# o3d.visualization.draw_geometries([point_cloud], point_show_normal=True)
o3d.visualization.draw_geometries([point_cloud])
o3d.visualization.draw_geometries([pc])