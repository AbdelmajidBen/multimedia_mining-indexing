def decode_obj_file(file_path):
    model_data = {
        'vertices': [],
        'texture_coords': [],
        'normals': [],
        'faces': []
    }

    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()

            if not line or line.startswith('#'):
                continue

            if line.startswith('v '):
                coords = tuple(map(float, line.split()[1:]))
                model_data['vertices'].append(coords)

            elif line.startswith('vt '):
                coords = tuple(map(float, line.split()[1:]))
                model_data['texture_coords'].append(coords)

            elif line.startswith('vn '):
                coords = tuple(map(float, line.split()[1:]))
                model_data['normals'].append(coords)

            elif line.startswith('f '):
                face = []
                elements = line.split()[1:]

                for element in elements:
                    vertex_data = element.split('/')

                    if len(vertex_data) == 1:
                        vertex_index = int(vertex_data[0])
                        texture_index = None
                        normal_index = None
                    elif len(vertex_data) == 2:
                        vertex_index = int(vertex_data[0])
                        texture_index = None
                        normal_index = int(vertex_data[1])
                    elif len(vertex_data) == 3:
                        vertex_index = int(vertex_data[0])
                        texture_index = int(vertex_data[1]) if vertex_data[1] else None
                        normal_index = int(vertex_data[2]) if vertex_data[2] else None
                    else:
                        continue

                    face.append((vertex_index, texture_index, normal_index))

                if face:
                    model_data['faces'].append(face)

    return model_data
