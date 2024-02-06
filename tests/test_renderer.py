import pytest
import os
import sys
from OpenGL.GL import *
from unittest.mock import patch

# Calculate the absolute path to the src directory and append it to sys.path
current_dir = os.path.dirname(__file__)
parent_dir = os.path.join(current_dir, os.pardir)
src_path = os.path.abspath(os.path.join(parent_dir, 'src'))
sys.path.insert(0, src_path)

from renderer import Renderer

@pytest.fixture
def renderer():
    return Renderer()

# Use context managers to patch each OpenGL function used in the Renderer methods
def test_renderer_initializes_with_expected_background_color(renderer):
    with patch('renderer.glClearColor') as mock_clear_color:
        renderer.initialize_scene()
        mock_clear_color.assert_called_once_with(0.5, 0.5, 0.5, 1.0)

def test_camera_setup_with_expected_parameters(renderer):
    with patch('renderer.glMatrixMode') as mock_glMatrixMode, \
         patch('renderer.glLoadIdentity'), \
         patch('renderer.gluPerspective') as mock_gluPerspective:
        renderer.setup_camera()
        # Check if glMatrixMode was called with GL_PROJECTION at any point
        mock_glMatrixMode.assert_any_call(GL_PROJECTION)
        # Also, verify the aspect ratio passed to gluPerspective
        mock_gluPerspective.assert_called_with(45.0, 800/600, 0.1, 50.0)
        # Ensure glMatrixMode was called with GL_MODELVIEW as well
        mock_glMatrixMode.assert_any_call(GL_MODELVIEW)


def test_overhead_lighting_setup(renderer):
    with patch('renderer.glEnable') as mock_glEnable, \
         patch('renderer.glLightfv') as mock_glLightfv:
        renderer.setup_lighting()
        mock_glEnable.assert_any_call(GL_LIGHTING)
        mock_glEnable.assert_any_call(GL_LIGHT0)
        mock_glLightfv.assert_called_with(GL_LIGHT0, GL_POSITION, [0.0, 1.0, 1.0, 1.0])