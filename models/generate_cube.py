import sys

EDGE_DISTANCE = 10
quads_per_edge = int(sys.argv[1])

with open(f"cube_{quads_per_edge}.obj", "w") as file:
    file.write(f"o Cube_{quads_per_edge}\n")
    # Vertices
    # Up face
    for x in range(quads_per_edge + 1):
        for z in range(quads_per_edge + 1):
            file.write(f"v {-EDGE_DISTANCE/2 + EDGE_DISTANCE/quads_per_edge * x} {EDGE_DISTANCE/2} {-EDGE_DISTANCE/2 + EDGE_DISTANCE/quads_per_edge * z}\n")
    # Down face
    for x in range(quads_per_edge + 1):
        for z in range(quads_per_edge + 1):
            file.write(f"v {-EDGE_DISTANCE/2 + EDGE_DISTANCE/quads_per_edge * x} {-EDGE_DISTANCE/2} {-EDGE_DISTANCE/2 + EDGE_DISTANCE/quads_per_edge * z}\n")
    # Left face
    for z in range(quads_per_edge + 1):
        for y in range(quads_per_edge + 1):
            file.write(f"v {-EDGE_DISTANCE/2} {-EDGE_DISTANCE/2 + EDGE_DISTANCE/quads_per_edge * y} {-EDGE_DISTANCE/2 + EDGE_DISTANCE/quads_per_edge * z}\n")
    # Right face
    for z in range(quads_per_edge + 1):
        for y in range(quads_per_edge + 1):
            file.write(f"v {EDGE_DISTANCE/2} {-EDGE_DISTANCE/2 + EDGE_DISTANCE/quads_per_edge * y} {-EDGE_DISTANCE/2 + EDGE_DISTANCE/quads_per_edge * z}\n")
    # Back face
    for x in range(quads_per_edge + 1):
        for y in range(quads_per_edge + 1):
            file.write(f"v {-EDGE_DISTANCE/2 + EDGE_DISTANCE/quads_per_edge * x} {-EDGE_DISTANCE/2 + EDGE_DISTANCE/quads_per_edge * y} {-EDGE_DISTANCE/2}\n")
    # Front face
    for x in range(quads_per_edge + 1):
        for y in range(quads_per_edge + 1):
            file.write(f"v {-EDGE_DISTANCE/2 + EDGE_DISTANCE/quads_per_edge * x} {-EDGE_DISTANCE/2 + EDGE_DISTANCE/quads_per_edge * y} {EDGE_DISTANCE/2}\n")

    # Normals
    file.write("vn 1 0 0\n")
    file.write("vn -1 0 0\n")
    file.write("vn 0 1 0\n")
    file.write("vn 0 -1 0\n")
    file.write("vn 0 0 1\n")
    file.write("vn 0 0 -1\n")

    # Placeholder tex coord
    file.write("vt 0 0\n")

    # Something
    file.write("s off\n")

    # Faces
    # Up face
    for x in range(quads_per_edge):
        for z in range(quads_per_edge):
            A = 1 + x * (quads_per_edge + 1) + z
            B = A + quads_per_edge + 1
            C = A + 1
            D = B + 1
            file.write(f"f {A}/1/3 {C}/1/3 {B}/1/3\n")
            file.write(f"f {C}/1/3 {D}/1/3 {B}/1/3\n")
    # Down face
    for x in range(quads_per_edge):
        for z in range(quads_per_edge):
            A = 1 + x * (quads_per_edge + 1) + z + pow(quads_per_edge + 1, 2)
            B = A + quads_per_edge + 1
            C = A + 1
            D = B + 1
            file.write(f"f {A}/1/4 {B}/1/4 {C}/1/4\n")
            file.write(f"f {C}/1/4 {B}/1/4 {D}/1/4\n")
    # Left face
    for z in range(quads_per_edge):
        for y in range(quads_per_edge):
            A = 1 + z * (quads_per_edge + 1) + y + pow(quads_per_edge + 1, 2)*2
            B = A + quads_per_edge + 1
            C = A + 1
            D = B + 1
            file.write(f"f {A}/1/3 {B}/1/3 {C}/1/3\n")
            file.write(f"f {B}/1/3 {D}/1/3 {C}/1/3\n")
    # Right face
    for z in range(quads_per_edge):
        for y in range(quads_per_edge):
            A = 1 + z * (quads_per_edge + 1) + y+ pow(quads_per_edge + 1, 2)*3
            B = A + quads_per_edge + 1
            C = A + 1
            D = B + 1
            file.write(f"f {A}/1/3 {C}/1/3 {B}/1/3\n")
            file.write(f"f {B}/1/3 {C}/1/3 {D}/1/3\n")
    # Back face
    for x in range(quads_per_edge):
        for y in range(quads_per_edge):
            A = 1 + x * (quads_per_edge + 1) + y+ pow(quads_per_edge + 1, 2)*4
            B = A + quads_per_edge + 1
            C = A + 1
            D = B + 1
            file.write(f"f {A}/1/3 {C}/1/3 {B}/1/3\n")
            file.write(f"f {B}/1/3 {C}/1/3 {D}/1/3\n")
    # Front face
    for x in range(quads_per_edge):
        for y in range(quads_per_edge):
            A = 1 + x * (quads_per_edge + 1) + y+ pow(quads_per_edge + 1, 2)*5
            B = A + quads_per_edge + 1
            C = A + 1
            D = B + 1
            file.write(f"f {A}/1/3 {B}/1/3 {C}/1/3\n")
            file.write(f"f {B}/1/3 {D}/1/3 {C}/1/3\n")