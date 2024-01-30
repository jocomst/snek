# test_food.py

import os
import sys
import pytest

# Calculate the absolute path to the src directory and append it to sys.path
current_dir = os.path.dirname(__file__)
parent_dir = os.path.join(current_dir, os.pardir)
src_path = os.path.abspath(os.path.join(parent_dir, 'src'))
sys.path.insert(0, src_path)

from food import Food  # Import the Food class

@pytest.fixture
def mock_display():
    class MockDisplay:
        def get_width(self):
            return 800

        def get_height(self):
            return 600
    return MockDisplay()

def test_food_model_loading_success(mock_display):
    # Assume 'valid_model_path.png' is a valid model file path
    valid_model_path = './models/fakeModel.png'
    food = Food(mock_display, 20, mock_display.get_width(), mock_display.get_height(), valid_model_path)
    assert food.model_loaded is True

def test_food_model_loading_failure(mock_display):
    # Assume 'invalid_model_path.png' is an invalid model file path
    invalid_model_path = 'path/to/invalid_model.png'
    food = Food(mock_display, 20, mock_display.get_width(), mock_display.get_height(), invalid_model_path)
    assert food.model_loaded is False