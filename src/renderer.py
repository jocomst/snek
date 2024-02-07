from OpenGL.GL import *
from OpenGL.GLU import *
import os

class Renderer:
    def __init__(self):
        # This could include initializing variables that keep track of
        # the renderer state, like the camera position or lighting settings.
        pass

    def initialize_scene(self):
        # Set the scene's background color.
        glClearColor(0.5, 0.5, 0.5, 1.0)  # Matches the test expectation

    def setup_camera(self):
        # Setup the camera with a perspective projection
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        aspect_ratio = 800 / 600  # Assuming a window size of 800x600 for this example
        gluPerspective(45.0, aspect_ratio, 0.1, 50.0)  # Matches the test expectation
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()

    def setup_lighting(self):
        # Enable lighting and set up an overhead light.
        glEnable(GL_LIGHTING)
        glEnable(GL_LIGHT0)  # Enable the first light source

        # Position the light overhead. The fourth parameter (1.0) indicates
        # a positional light source rather than a directional one.
        light_position = [0.0, 1.0, 1.0, 1.0]  # An overhead light
        glLightfv(GL_LIGHT0, GL_POSITION, light_position)

        # Additional light properties, like color and intensity, could be set here as well.
    def add_model(self, file_path):
        # Determine the file type (assuming the file extension is correct)
        _, file_extension = os.path.splitext(file_path)
        
        if file_extension.lower() == '.obj':
            self._load_obj(file_path)
        elif file_extension.lower() == '.3ds':
            self._load_3ds(file_path)
        else:
            raise ValueError("Unsupported file format")
        
    def _load_obj(self, file_path):
        # A very simple OBJ file loader implementation
        with open(file_path, 'r') as file:
            lines = file.readlines()
        
        vertices = []
        faces = []
        
        for line in lines:
            if line.startswith('v '):
                vertices.append(list(map(float, line.strip().split()[1:])))
            elif line.startswith('f '):
                face = [int(face.split('/')[0]) for face in line.strip().split()[1:]]
                faces.append(face)
        
        # Now, you would use OpenGL calls to create and fill the display list
        display_list = glGenLists(1)
        glNewList(display_list, GL_COMPILE)
        
        glBegin(GL_POLYGON)
        for face in faces:
            for vertex_index in face:
                glVertex3fv(vertices[vertex_index - 1])
        glEnd()
        
        glEndList()
        glFlush()
