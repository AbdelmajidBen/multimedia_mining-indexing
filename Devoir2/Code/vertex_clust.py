import numpy as np
import pyvista as pv
from test import decode_obj_file

def vertex_clustering(mesh_data, grid_size):
    vertices = np.array(mesh_data['vertices'])
    faces = mesh_data['faces']
    grid_positions = (vertices / grid_size).astype(int)
    grid_dict = {}

    for i, pos in enumerate(grid_positions):
        grid_key = tuple(pos)
        if grid_key not in grid_dict:
            grid_dict[grid_key] = []
        grid_dict[grid_key].append(i)

    new_vertices = []
    vertex_mapping = {}

    for grid_key, vertex_indices in grid_dict.items():
        cluster_vertices = vertices[vertex_indices]
        cluster_center = cluster_vertices.mean(axis=0)
        new_index = len(new_vertices)
        new_vertices.append(cluster_center)

        for old_index in vertex_indices:
            vertex_mapping[old_index] = new_index

    new_vertices = np.array(new_vertices)
    new_faces = []

    for face in faces:
        new_face = []
        for v, vt, vn in face:
            new_vertex_index = vertex_mapping[v - 1] + 1
            new_face.append((new_vertex_index, vt, vn))
        new_faces.append(new_face)

    reduced_mesh = {
        'vertices': new_vertices.tolist(),
        'texture_coords': mesh_data['texture_coords'],
        'normals': mesh_data['normals'],
        'faces': new_faces
    }

    return reduced_mesh

def save_obj_file(mesh_data, output_path):
    with open(output_path, 'w') as file:
        for vertex in mesh_data['vertices']:
            file.write(f"v {vertex[0]} {vertex[1]} {vertex[2]}\n")
        for tex_coord in mesh_data['texture_coords']:
            file.write(f"vt {tex_coord[0]} {tex_coord[1]}\n")
        for normal in mesh_data['normals']:
            file.write(f"vn {normal[0]} {normal[1]} {normal[2]}\n")
        for face in mesh_data['faces']:
            face_str = []
            for v, vt, vn in face:
                if vt is None and vn is None:
                    face_str.append(f"{v}")
                elif vt is None:
                    face_str.append(f"{v}//{vn}")
                elif vn is None:
                    face_str.append(f"{v}/{vt}")
                else:
                    face_str.append(f"{v}/{vt}/{vn}")
            file.write(f"f {' '.join(face_str)}\n")

def create_pyvista_mesh(mesh_data):
    vertices = np.array(mesh_data['vertices'])
    faces = []

    for face in mesh_data['faces']:
        face_vertices = [len(face)] + [v[0] - 1 for v in face]
        faces.extend(face_vertices)

    faces = np.array(faces)
    return pv.PolyData(vertices, faces)

input_path = 'Devoir2/DVI2/obj6.obj'
mesh_data = decode_obj_file(input_path)
grid_size = 0.003
reduced_mesh = vertex_clustering(mesh_data, grid_size)

original_vertex_count = len(mesh_data['vertices'])
reduced_vertex_count = len(reduced_mesh['vertices'])
reduction_percentage = 100 * (original_vertex_count - reduced_vertex_count) / original_vertex_count

print(f"Original vertices: {original_vertex_count}")
print(f"Reduced vertices: {reduced_vertex_count}")
print(f"Reduction: {reduction_percentage:.2f}%")

output_path = 'Devoir2/DVI2/obj6_reduced.obj'
save_obj_file(reduced_mesh, output_path)
print(f"Reduced .obj file saved to {output_path}")

original_mesh = create_pyvista_mesh(mesh_data)
reduced_mesh_pv = create_pyvista_mesh(reduced_mesh)

plotter = pv.Plotter(shape=(1, 2), title="Vertex Clustering - Mesh Reduction")
plotter.subplot(0, 0)
plotter.add_text("Original Mesh", font_size=10)
plotter.add_mesh(original_mesh, color="white", show_edges=True)
plotter.add_text(f"Vertices: {original_vertex_count}", position="lower_left", color="yellow")
plotter.subplot(0, 1)
plotter.add_text("Reduced Mesh", font_size=10)
plotter.add_mesh(reduced_mesh_pv, color="lightblue", show_edges=True)
plotter.add_text(f"Vertices: {reduced_vertex_count}\nReduction: {reduction_percentage:.2f}%", position="lower_left", color="green")
plotter.show()