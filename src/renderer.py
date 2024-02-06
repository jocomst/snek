from OpenGL.GL import *
from OpenGL.GLU import *

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
