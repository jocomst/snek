# test_food.py

import os
import sys
import pytest
from unittest.mock import MagicMock

# Calculate the absolute path to the src directory and append it to sys.path
current_dir = os.path.dirname(__file__)
parent_dir = os.path.join(current_dir, os.pardir)
src_path = os.path.abspath(os.path.join(parent_dir, 'src'))
sys.path.insert(0, src_path)

from food import Food  # Import the Food class

# MockRenderer is a mock of the Renderer class
class MockRenderer:
    def draw_cube(self, position, size, color):
        pass  # The mock doesn't actually do anything

@pytest.fixture
def mock_renderer():
    return MockRenderer()

@pytest.fixture
def food(mock_renderer):
    block_size = 20
    width, height, depth = 800, 600, 100
    return Food(mock_renderer, block_size, width, height, depth)

def test_food_initial_position(food):
    assert 0 <= food.x < food.width and food.x % food.block_size == 0
    assert 0 <= food.y < food.height and food.y % food.block_size == 0
    assert food.z == food.block_size  # Assuming the food is placed one block above the ground

def test_food_draw(food, mock_renderer):
    mock_renderer.draw_cube = MagicMock()
    food.draw()
    mock_renderer.draw_cube.assert_called_once_with([food.x, food.y, food.z], food.block_size, food.color)

def test_food_relocate(food):
    initial_position = (food.x, food.y)
    food.relocate()
    new_position = (food.x, food.y)
    assert new_position != initial_position
    assert 0 <= food.x < food.width and food.x % food.block_size == 0
    assert 0 <= food.y < food.height and food.y % food.block_size == 0
    # Optionally, assert that the food's z-coordinate has not changed if it should remain constant