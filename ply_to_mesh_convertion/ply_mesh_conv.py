# import open3d as o3d
# import numpy as np

# # Specify the input PLY file path
# ply_file_path = r"e:\Coding\Python\DepthAnything\2d_images\calib_imgs\depthanything\2.ply"


# # Load the PLY file as a point cloud
# point_cloud = o3d.io.read_point_cloud(ply_file_path)

# # Apply statistical outlier removal
# point_cloud, ind = point_cloud.remove_statistical_outlier(
#     nb_neighbors=20,  # Number of neighbors to analyze for each point
#     std_ratio=6.0     # Threshold, lower means more aggressive filtering
# )
# #estimate normals
# point_cloud.estimate_normals()
# point_cloud.orient_normals_to_align_with_direction()
# # o3d.visualization.draw_geometries([point_cloud])
# # Optionally, save the filtered point cloud
# # filtered_ply_file_path = "filtered_point_cloud.ply"
# # o3d.io.write_point_cloud(filtered_ply_file_path, point_cloud)

# # Estimate normals (required for mesh reconstruction)
# # point_cloud.estimate_normals()

# # Create a mesh using the Poisson surface reconstruction
# mesh = o3d.geometry.TriangleMesh.create_from_point_cloud_poisson(
#     point_cloud, depth=10, n_threads=4
# )[0]

# #rotate the mesh
# rotation = mesh.get_rotation_matrix_from_xyz((np.pi, 0, 0))
# mesh.rotate(rotation, center=(0,0,0))
# # # Display the filtered mesh
# o3d.visualization.draw_geometries([mesh], mesh_show_back_face=True)

# file_name = ply_file_path.split[:-1]
# # Save the filtered mesh to a file
# mesh_file_path = "filtered_mesh.ply"
# o3d.io.write_triangle_mesh(mesh_file_path, mesh)

# # print(f"Filtered mesh saved as: {mesh_file_path}")

import open3d as o3d
import numpy as np
import os

# Specify the input folder path
input_folder_path = r"E:\Coding\Python\DepthAnything\2d_3d\cityhawkdata\left_cam\depthanything"

# Iterate over all .ply files in the input folder
for file_name in os.listdir(input_folder_path):
    if file_name.endswith(".ply"):
        ply_file_path = os.path.join(input_folder_path, file_name)
        
        # Load the PLY file as a point cloud
        point_cloud = o3d.io.read_point_cloud(ply_file_path)

        # Apply statistical outlier removal
        point_cloud, ind = point_cloud.remove_statistical_outlier(
            nb_neighbors=20,  # Number of neighbors to analyze for each point
            std_ratio=1.0     # Threshold, lower means more aggressive filtering
        )

        # Estimate normals
        point_cloud.estimate_normals()
        point_cloud.orient_normals_to_align_with_direction()

        # Create a mesh using the Poisson surface reconstruction
        mesh, densities = o3d.geometry.TriangleMesh.create_from_point_cloud_poisson(
            point_cloud, depth=10, n_threads=4
        )

        # Rotate the mesh
        rotation = mesh.get_rotation_matrix_from_xyz((np.pi, 0, 0))
        mesh.rotate(rotation, center=(0, 0, 0))

        # Display the filtered mesh

        # Define the output mesh file path
        base_file_name, _ = os.path.splitext(file_name)
        mesh_file_name = f"{base_file_name}_filtered_mesh.ply"
        mesh_file_path = os.path.join(input_folder_path, mesh_file_name)

        # Save the filtered mesh to a file
        o3d.io.write_triangle_mesh(mesh_file_path, mesh)

        print(f"Filtered mesh saved to: {mesh_file_path}")

print("Processing completed.")
