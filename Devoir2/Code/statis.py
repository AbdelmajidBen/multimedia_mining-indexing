import os

# Path to your folder containing the .obj files
folder_path = 'Devoir2/DVI2'

# Iterate through all .obj files in the folder
for filename in os.listdir(folder_path):
    if filename.endswith('.obj'):
        file_path = os.path.join(folder_path, filename)

        # Initialize counters for each file
        v_count = 0
        vn_count = 0
        vt_count = 0
        f_count = 0

        # Read the file and count the components
        with open(file_path, 'r') as file:
            for line in file:
                if line.startswith('v '):  # vertex
                    v_count += 1
                elif line.startswith('vn '):  # vertex normal
                    vn_count += 1
                elif line.startswith('vt '):  # texture coordinate
                    vt_count += 1
                elif line.startswith('f '):  # face
                    f_count += 1

        # Print the statistics for the current file
        print(f"File: {filename}")
        print(f"  Vertices (v): {v_count}")
        print(f"  Vertex Normals (vn): {vn_count}")
        print(f"  Texture Coordinates (vt): {vt_count}")
        print(f"  Faces (f): {f_count}")
        print("-" * 40)  # Separator for better readability
