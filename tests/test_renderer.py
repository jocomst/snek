import pytest
import os
import sys
from OpenGL.GL import *
from OpenGL.GLU import *

# Calculate the absolute path to the src directory and append it to sys.path
current_dir = os.path.dirname(__file__)
parent_dir = os.path.join(current_dir, os.pardir)
src_path = os.path.abspath(os.path.join(parent_dir, 'src'))
sys.path.insert(0, src_path)

from renderer import Renderer

# Define a fixture for creating a Renderer instance
@pytest.fixture
def renderer():
    return Renderer()

def test_renderer_initializes_with_expected_background_color(mocker, renderer):
    glClearColor_mock = mocker.patch('OpenGL.GL.glClearColor')
    renderer.initialize_scene()
    glClearColor_mock.assert_called_with(0.5, 0.5, 0.5, 1.0)  # Assuming a grey background

def test_camera_setup_with_expected_parameters(mocker, renderer):
    gluPerspective_mock = mocker.patch('OpenGL.GLU.gluPerspective')
    renderer.setup_camera()
    gluPerspective_mock.assert_called_with(45.0, pytest.approx(1.33), 0.1, 50.0)  # Use `pytest.approx` for floating-point comparison

def test_overhead_lighting_setup(mocker, renderer):
    glEnable_mock = mocker.patch('OpenGL.GL.glEnable')
    glLightfv_mock = mocker.patch('OpenGL.GL.glLightfv')
    renderer.setup_lighting()
    glEnable_mock.assert_called_with(OpenGL.GL.GL_LIGHT0)  # Check if lighting was enabled
    # Further assertions can be added to check glLightfv calls