from OpenGL.GL import *
from OpenGL.GLU import *
import os
from PIL import Image

class Renderer:
    def __init__(self):
        # This could include initializing variables that keep track of
        # the renderer state, like the camera position or lighting settings.
        pass

    def initialize_scene(self):
    # Initialize other aspects of the scene that do not involve direct OpenGL calls
    # For example, setting up initial positions of objects, initializing game state, etc.
    
    # Note: Since we're not using glClearColor, consider alternatives for background color
    # This could involve drawing a full-screen quad as the first step in your rendering loop
    # or adjusting the render logic to include a background texture or color in another way.

    # Setup initial OpenGL settings that don't cause issues
        glEnable(GL_DEPTH_TEST)  # Example of enabling depth testing if needed for 3D rendering
        

    # Other OpenGL initialization code that's safe to run can go here

    def setup_camera(self):
        # Setup the camera with a perspective projection
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        aspect_ratio = 800 / 600  # Assuming a window size of 800x600 for this example
        gluPerspective(45.0, aspect_ratio, 0.1, 50.0)  # Field of view, aspect ratio, near clip, far clip

        # Switch to modelview matrix to set camera position and orientation
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        # Move the camera back so the objects can be seen
        glTranslatef(0.0, 0.0, -3.0)

        
    def draw_plane(self, width=20, length=20, color=(0.5, 0.75, 0.5)):
        """Draw a flat plane centered at the origin with specified width and length."""
        half_width = width / 2
        half_length = length / 2

        glBegin(GL_QUADS)  # Start drawing a flat plane
        glColor3fv(color)  # Set the color of the plane

        # Define the 4 vertices of the plane
        glVertex3f(-half_width, -half_length, 0)  # Bottom Left
        glVertex3f(half_width, -half_length, 0)   # Bottom Right
        glVertex3f(half_width, half_length, 0)    # Top Right
        glVertex3f(-half_width, half_length, 0)   # Top Left

        glEnd()  # End drawing the plane

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
        
    def draw_triangle(self):
        """Draw a green triangle centered at the origin."""
        glBegin(GL_TRIANGLES)  # Start drawing a triangle
        glColor3f(0.0, 1.0, 0.0)  # Set the color to green
        
        # Define the 3 vertices of the triangle
        glVertex3f(-0.5, -0.5, 0)  # Bottom Left
        glVertex3f(0.5, -0.5, 0)   # Bottom Right
        glVertex3f(0.0, 0.5, 0)    # Top Middle

        glEnd()  # End drawing the triangle
    
    def draw_square(self, texture_id=None):
        """Draw a flat square centered at the origin. Apply a texture if texture_id is provided."""
        if texture_id is not None:
            glEnable(GL_TEXTURE_2D)
            glBindTexture(GL_TEXTURE_2D, texture_id)
        
        glBegin(GL_QUADS)
        
        if texture_id is not None:
            # Define texture coordinates along with each vertex
            glTexCoord2f(0.0, 0.0)
        glVertex3f(-0.5, -0.5, 0)  # Bottom Left
        
        if texture_id is not None:
            glTexCoord2f(1.0, 0.0)
        glVertex3f(0.5, -0.5, 0)   # Bottom Right
        
        if texture_id is not None:
            glTexCoord2f(1.0, 1.0)
        glVertex3f(0.5, 0.5, 0)    # Top Right
        
        if texture_id is not None:
            glTexCoord2f(0.0, 1.0)
        glVertex3f(-0.5, 0.5, 0)   # Top Left

        glEnd()

        if texture_id is not None:
            glBindTexture(GL_TEXTURE_2D, 0)
            glDisable(GL_TEXTURE_2D)
        
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

    def load_texture(self, file_path):
            """Load a texture from a file and return the OpenGL texture ID."""
            # Load the image with PIL
            img = Image.open(file_path)
            img = img.convert("RGB")  # Ensure it's in the correct format
            img_data = img.tobytes("raw", "RGB", 0, -1)
            
            # Generate a texture ID
            texture_id = glGenTextures(1)
            glBindTexture(GL_TEXTURE_2D, texture_id)
            glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
            glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
            glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP_TO_EDGE)
            glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP_TO_EDGE)
            
            # Upload the texture data
            glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, img.width, img.height, 0, GL_RGB, GL_UNSIGNED_BYTE, img_data)
            
            # Unbind the texture
            glBindTexture(GL_TEXTURE_2D, 0)
            
            return texture_id