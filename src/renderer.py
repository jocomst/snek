from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import os
from PIL import Image
from cube_data import vertices as cube_vertices, faces as cube_faces

class Renderer:
    def __init__(self, width, height):
        self.width = width
        self.height = height  # Set these to your desired window size
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
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(45.0, float(self.width) / self.height, 0.1, 100.0)  # Slightly wider field of view

        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()

        # Position the camera further away
        eyeX, eyeY, eyeZ = 1, 1, 1  # Adjust these values as needed
        centerX, centerY, centerZ = 0, 0, 0  # Looking at the origin
        upX, upY, upZ = 0, 0, 1  # Up is along the Z-axis

        gluLookAt(eyeX, eyeY, eyeZ, centerX, centerY, centerZ, upX, upY, upZ)

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
        """Draw a neon green wireframe triangle centered at the origin and above the square plane."""
        glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)  # Draw as wireframe
        glColor3f(0, 1, 0)  # Neon green color

        glBegin(GL_TRIANGLES)  # Start drawing a triangle

        # Define the 3 vertices of the triangle, half the previous size
        glVertex3f(-5, -5, 0.1)  # Bottom Left, half the size of the previous square
        glVertex3f(5, -5, 0.1)   # Bottom Right, half the size of the previous square
        glVertex3f(0, 5, 0.1)    # Top Middle, half the size of the previous square

        glEnd()  # End drawing the triangle

        glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)  # Revert to default polygon mode
    
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

    def draw_segment(self, position, size=0.5):
        """Draw a cube segment of the snake at the given position."""
        glPushMatrix()
        glTranslatef(position[0], position[1], position[2])
        glScalef(size, size, size)  # Scale cube to the size of the snake segment

        glBegin(GL_QUADS)
        for face in cube_faces:
            for vertex_index in face:
                glVertex3fv(cube_vertices[vertex_index])
        glEnd()

        glPopMatrix()

    def draw_cube(self, position, size, color):
        x, y, z = position

        # Define the vertices of the cube relative to the center position
        # Modify the size of the cube here
        new_size_factor = 0.05  # To make the cube a quarter of its current size
        half_size = (size * new_size_factor) / 2
        vertices = [
            [-half_size, -half_size, -half_size], [half_size, -half_size, -half_size],
            [half_size, half_size, -half_size], [-half_size, half_size, -half_size],
            [-half_size, -half_size, half_size], [half_size, -half_size, half_size],
            [half_size, half_size, half_size], [-half_size, half_size, half_size]
        ]

        # Define the 6 faces of the cube, each face has 4 vertices (quads)
        faces = [
            [0, 1, 2, 3],  # Bottom
            [4, 5, 6, 7],  # Top
            [0, 1, 5, 4],  # Front
            [2, 3, 7, 6],  # Back
            [0, 3, 7, 4],  # Left
            [1, 2, 6, 5],  # Right
        ]

        glPushMatrix()
        glColor3f(*color)  # Set the color
        glTranslate(x, y, z)  # Translate the cube to its position

        glBegin(GL_QUADS)
        for face in faces:
            for vertex in face:
                glVertex3fv(vertices[vertex])
        glEnd()

        glPopMatrix()
