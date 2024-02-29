import os
import sys
import pytest
from unittest.mock import Mock, patch

# Calculate the absolute path to the src directory and append it to sys.path
current_dir = os.path.dirname(__file__)
parent_dir = os.path.join(current_dir, os.pardir)
src_path = os.path.abspath(os.path.join(parent_dir, 'src'))
sys.path.insert(0, src_path)


from snake import Snake3D

@pytest.fixture
def snake():
    block_size = 1  # Easier to work with unit size for testing
    return Snake3D(block_size)

def test_snake_initialization(snake):
    # Snake should start at the origin in 3D space
    assert snake.positions == [[0, 0, 0]]

def test_snake_movement(snake):
    # Move the snake along x-axis
    snake.move(1, 0, 0)
    snake.update()
    # The head should now be at (1, 0, 0)
    assert snake.positions[-1] == [1, 0, 0]

def test_snake_growth(snake):
    initial_length = len(snake.positions)
    snake.grow()
    # Snake should have one more segment after growing
    assert len(snake.positions) == initial_length + 1
    # The new head should be at the same position as the old head
    assert snake.positions[-1] == snake.positions[-2]

def test_snake_direction_change(snake):
    # Move the snake along y-axis
    snake.move(0, 1, 0)
    snake.update()
    # The head should now be at (0, 1, 0)
    assert snake.positions[-1] == [0, 1, 0]

    # Change direction along z-axis
    snake.move(0, 0, 1)
    snake.update()
    # The head should now be at (0, 1, 1)
    assert snake.positions[-1] == [0, 1, 1]

# Tests for model loading can be omitted if you're handling this entirely within OpenGL and not using pygame