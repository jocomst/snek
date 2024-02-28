# cube_data.py

# Define the eight vertices of the cube
vertices = [
    [-0.5, -0.5, -0.5],  # Vertex 0
    [0.5, -0.5, -0.5],   # Vertex 1
    [0.5, 0.5, -0.5],    # Vertex 2
    [-0.5, 0.5, -0.5],   # Vertex 3
    [-0.5, -0.5, 0.5],   # Vertex 4
    [0.5, -0.5, 0.5],    # Vertex 5
    [0.5, 0.5, 0.5],     # Vertex 6
    [-0.5, 0.5, 0.5]     # Vertex 7
]

# Define the six faces of the cube, each face is a list of four vertices
faces = [
    [0, 1, 2, 3],  # Front face
    [4, 5, 6, 7],  # Back face
    [0, 1, 5, 4],  # Bottom face
    [3, 2, 6, 7],  # Top face
    [0, 3, 7, 4],  # Left face
    [1, 2, 6, 5]   # Right face
]
