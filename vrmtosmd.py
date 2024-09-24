import click, sys

verts = {}
faces = {}
materials = {}
uvs = {}
normals = {}
faceattribs = {}

vert_count = None
face_count = None
material_count = None
uv_count = None
normal_count = None

def handle_copy_list(command_index, lines):
    for line in lines[command_index:]:
        print(line, end='')
        if line.strip() == 'end':
            break

def handle_generic_list(command_index, lines, storage_dict):
    for line in lines[(command_index + 1):]:
        if line.strip() == 'end':
            break
        split_line = line.split()
        storage_dict[int(split_line[0])] = split_line[1:]

@click.command()
@click.argument('file', type=click.types.File('r'))
def main(file):
    '''Convert a VRM to an SMD.'''
    lines = file.readlines()
    for index, line in enumerate(lines):
        split_line = line.strip().split(maxsplit=2)
        match split_line[0]:
            case 'version':
                if int(split_line[1]) != 2:
                    raise ValueError('Version is not 2')
                else:
                    print('version 1')
            case 'name':
                print(f'Model name: "{split_line[1]}"', file=sys.stderr)
            case 'vertices':
                print(f'Vert count: {split_line[1]}', file=sys.stderr)
                vert_count = int(split_line[1])
            case 'materials':
                print(f'Material count: {split_line[1]}', file=sys.stderr)
                material_count = int(split_line[1])
            case 'texcoords':
                print(f'UV count: {split_line[1]}', file=sys.stderr)
                uv_count = int(split_line[1])
            case 'normals':
                print(f'Normal count: {split_line[1]}', file=sys.stderr)
                normal_count = int(split_line[1])
            case 'tristrips':
                print(f'Tristrip count: {split_line[1]}', file=sys.stderr)
            case 'nodes':
                handle_copy_list(index, lines)
            case 'skeleton':
                handle_copy_list(index, lines)
            case 'vertexlist':
                handle_generic_list(index, lines, verts)
            case 'facelist':
                handle_generic_list(index, lines, faces)
            case 'materiallist':
                handle_generic_list(index, lines, materials)
            case 'texcoordlist':
                handle_generic_list(index, lines, uvs)
            case 'normallist':
                handle_generic_list(index, lines, normals)
            case 'faceattriblist':
                handle_generic_list(index, lines, faceattribs)
            case 'MRM':
                print('FIXME: "MRM" not implemented.', file=sys.stderr)
            case 'MRMvertices':
                print('FIXME: "MRMvertices" not implemented.', file=sys.stderr)
            case 'MRMfaces':
                print('FIXME: "MRMfaces" not implemented.', file=sys.stderr)
            case 'MRMfaceupdates':
                print('FIXME: "MRMfaceupdates" not implemented.', file=sys.stderr)
    if len(verts) != vert_count:
        print('Warning: Vert count not matching up?', file=sys.stderr)
    if len(faces) != face_count:
        print('Warning: Face count not matching up?', file=sys.stderr)
    if len(materials) != material_count:
        print('Warning: Material count not matching up?', file=sys.stderr)
    if len(uvs) != uv_count:
        print('Warning: UV count not matching up?', file=sys.stderr)
    if len(normals) != normal_count:
        print('Warning: Normal count not matching up?', file=sys.stderr)
    print('triangles')
    for face_id in faces:
        face = faces[face_id]
        face_attrib = faceattribs[face_id]

        # Write the material name/path.
        mat_id = int(face_attrib[0])
        print(materials[mat_id][13].strip('"'))

        # Write the verts
        for vert_index in range(3):
            # FIXME: Add support for multiple weights.
            print(' '.join(verts[int(face[vert_index])]), end=' ')
            print(' '.join(normals[int(face_attrib[5 + vert_index])][1:]), end=' ')
            print(' '.join(uvs[int(face_attrib[2 + vert_index])]))
    print('end')

if __name__ == '__main__':
    main()
