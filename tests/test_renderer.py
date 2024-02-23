import pytest
import os
import sys
from OpenGL.GL import *
from unittest.mock import mock_open, patch

# Calculate the absolute path to the src directory and append it to sys.path
current_dir = os.path.dirname(__file__)
parent_dir = os.path.join(current_dir, os.pardir)
src_path = os.path.abspath(os.path.join(parent_dir, 'src'))
sys.path.insert(0, src_path)

from renderer import Renderer
from game import SnakeGame

@pytest.fixture
def renderer():
    return Renderer()

@pytest.fixture
def game(mocker):
    # You might need to mock or adjust any initializations that require a display or input devices
    mocker.patch('pygame.time.Clock', autospec=True)
    game_instance = SnakeGame()
    return game_instance


def test_camera_setup_with_expected_parameters(renderer):
    with patch('renderer.glMatrixMode') as mock_glMatrixMode, \
         patch('renderer.glLoadIdentity'), \
         patch('renderer.gluPerspective') as mock_gluPerspective, \
         patch('renderer.glTranslatef') as mock_glTranslatef:
        renderer.setup_camera()
        # Check if glMatrixMode was called with GL_PROJECTION at any point
        mock_glMatrixMode.assert_any_call(GL_PROJECTION)
        # Also, verify the aspect ratio passed to gluPerspective
        mock_gluPerspective.assert_called_with(45.0, 800/600, 0.1, 50.0)
        # Ensure glMatrixMode was called with GL_MODELVIEW as well
        mock_glMatrixMode.assert_any_call(GL_MODELVIEW)
        # Verify glTranslatef was called correctly if you decide to test it
        mock_glTranslatef.assert_called_with(0.0, 0.0, -3.0)


def test_overhead_lighting_setup(renderer):
    with patch('renderer.glEnable') as mock_glEnable, \
         patch('renderer.glLightfv') as mock_glLightfv:
        renderer.setup_lighting()
        mock_glEnable.assert_any_call(GL_LIGHTING)
        mock_glEnable.assert_any_call(GL_LIGHT0)
        mock_glLightfv.assert_called_with(GL_LIGHT0, GL_POSITION, [0.0, 1.0, 1.0, 1.0])

from unittest.mock import patch, mock_open

def test_renderer_adds_model_from_obj_file(renderer):
    with patch('renderer.glGenLists', return_value=1) as mock_glGenLists, \
         patch('renderer.glNewList') as mock_glNewList, \
         patch('renderer.glEndList') as mock_glEndList, \
         patch('renderer.glBegin') as mock_glBegin, \
         patch('renderer.glVertex3fv') as mock_glVertex3fv, \
         patch('renderer.glEnd') as mock_glEnd, \
         patch('renderer.glFlush') as mock_glFlush:
        mock_obj_file_content = "v 0.0 0.0 0.0\nv 1.0 0.0 0.0\nv 1.0 1.0 0.0\nv 0.0 1.0 0.0\nf 1 2 3 4\n"
        obj_file_path = "path/to/model.obj"

        with patch('builtins.open', mock_open(read_data=mock_obj_file_content)):
            renderer.add_model(obj_file_path)

        # Check if OpenGL list functions were called
        mock_glGenLists.assert_called_once()
        mock_glNewList.assert_called_once_with(1, GL_COMPILE)
        mock_glEndList.assert_called_once()
        mock_glBegin.assert_called_once_with(GL_POLYGON)
        mock_glEnd.assert_called_once()
        assert mock_glVertex3fv.call_count == 4

def test_load_texture(renderer):
    test_texture_path = './models/grassTexture.jpg'
    
    # Mock glGenTextures to return a fake texture ID
    with patch('OpenGL.GL.glGenTextures', return_value=1) as mock_glGenTextures, \
         patch('OpenGL.GL.glBindTexture') as mock_glBindTexture, \
         patch('OpenGL.GL.glTexParameteri'), \
         patch('OpenGL.GL.glTexImage2D'), \
         patch('PIL.Image.open') as mock_open:
        
        # Mock the image object and its methods
        mock_image = mock_open.return_value
        mock_image.convert.return_value = mock_image
        mock_image.tobytes.return_value = b'test bytes'
        mock_image.width = 256
        mock_image.height = 256
        
        # Call the load_texture method
        texture_id = renderer.load_texture(test_texture_path)
        
        # Ensure a texture ID was generated
        assert texture_id == 1
        mock_glGenTextures.assert_called_once_with(1)
        
        # Check that glBindTexture was called to bind and unbind the texture
        assert mock_glBindTexture.call_count == 2
        
        # Ensure the texture parameters and image data were set correctly
        mock_glBindTexture.assert_any_call(GL_TEXTURE_2D, texture_id)

# Similar test can be created for 3DS files, with appropriate mock data and assertions
