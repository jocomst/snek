import os
import sys
import pytest
from unittest.mock import Mock, patch

# Calculate the absolute path to the src directory and append it to sys.path
current_dir = os.path.dirname(__file__)
parent_dir = os.path.join(current_dir, os.pardir)
src_path = os.path.abspath(os.path.join(parent_dir, 'src'))
sys.path.insert(0, src_path)


from snake import Snake

class MockDisplay:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height

@pytest.fixture
def mock_display():
    return MockDisplay(600, 400)

@pytest.fixture
def snake(mock_display):
    block_size = 20
    return Snake(mock_display, block_size)

def test_snake_initialization(snake, mock_display):
    assert snake.positions == [[mock_display.get_width() / 2, mock_display.get_height() / 2]]

def test_snake_movement(snake):
    # Get the initial head position
    initial_head = snake.positions[-1].copy()
    # Assume snake moves right by block_size
    snake.move(snake.block_size, 0)
    snake.update()
    # Check if the new head is correctly placed based on the initial head position
    assert snake.positions[-1][0] == initial_head[0] + snake.block_size
    assert snake.positions[-1][1] == initial_head[1]

def test_snake_growth(snake):
    initial_length = len(snake.positions)
    # Get the initial head position
    initial_head = snake.positions[-1].copy()
    snake.grow()
    # After growing, the snake should have one more segment, and the new head should be in the same position
    assert len(snake.positions) == initial_length + 1
    assert snake.positions[-1] == initial_head

def test_snake_direction_change(snake):
    # Get the initial head position
    initial_head = snake.positions[-1].copy()
    # Change direction to down
    snake.move(0, snake.block_size)
    snake.update()
    # Check if the new head's y position has changed based on the initial head position
    assert snake.positions[-1][0] == initial_head[0]
    assert snake.positions[-1][1] == initial_head[1] + snake.block_size

def test_snake_model_loading_success(mock_display):
    with patch('pygame.image.load') as mock_load:
        # Assuming 'valid_model_path.png' is a valid path for the model
        valid_model_path = './models/fakeModel.png'
        mock_load.return_value = Mock()  # Mock the pygame surface returned by image.load
        
        snake = Snake(mock_display, 20, valid_model_path)
        assert snake.model_loaded is True

def test_snake_model_loading_failure(mock_display):
    with patch('pygame.image.load', side_effect=Exception('Load failed')):
        # Assuming 'invalid_model_path.png' is an invalid path for the model
        invalid_model_path = 'path/to/invalid_model.png'
        
        snake = Snake(mock_display, 20, invalid_model_path)
        assert snake.model_loaded is False

# ... rest of the tests ...
