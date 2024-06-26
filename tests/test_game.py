import pytest
import pygame
import os
import sys

# Adjust the path according to your project structure
current_dir = os.path.dirname(__file__)
parent_dir = os.path.join(current_dir, os.pardir)
src_path = os.path.abspath(os.path.join(parent_dir, 'src'))
sys.path.insert(0, src_path)

from game import SnakeGame  # Update the import statement as necessary
from food import Food

@pytest.fixture
def game():
    """Fixture to create a game instance for each test."""
    game_instance = SnakeGame()
    yield game_instance
    # Teardown code, if necessary
    pygame.quit()

def test_initialization(game):
    """Test game initializes with correct default values."""
    # Adjust these assertions based on your game's initialization logic
    assert game.width == 800  # Assuming you've updated the width
    assert game.height == 600  # Assuming you've updated the height
    assert not game.game_over

def test_renderer_initialization(game):
    """Test if the SnakeGame is initialized with a renderer."""
    # This test assumes your game class now holds a renderer instance
    assert hasattr(game, 'renderer')
    assert game.renderer is not None

def test_snake_initialization(game):
    """Test if the Snake3D object is initialized correctly within SnakeGame."""
    snake = game.snake  # Assuming SnakeGame initializes a Snake3D object as `self.snake`
    
    # Verify that the Snake3D object has been created
    assert snake is not None
    
    # Check initial color of the snake is red
    assert snake.color == (1, 0, 0), "Initial snake color should be red."
    
    # Check that the snake's initial position is at the origin
    assert snake.positions == [[0, 0, 0]], "Initial snake position should be at the origin."
    
    # Check that the snake's initial block size is set correctly
    expected_block_size = 1  # Update this value to match the initial block size you set in SnakeGame
    assert snake.block_size == expected_block_size, f"Initial snake block size should be {expected_block_size}."
    
    # Check that the snake's initial movement direction is along the positive x-axis
    assert snake.x_change == expected_block_size, "Initial snake x movement should equal the block size."
    assert snake.y_change == 0, "Initial snake y movement should be 0."
    assert snake.z_change == 0, "Initial snake z movement should be 0."

def test_score_update(game):
    """Test if the game score updates correctly."""
    initial_score = game.score  # Store the initial score
    game.update_score()  # Simulate an event that would increase the score
    assert game.score == initial_score + 1, "Score should increase by 1 after an increment"

    additional_points = 5
    for _ in range(additional_points):  # Simulate multiple events increasing the score
        game.update_score()
    
    assert game.score == initial_score + 1 + additional_points, f"Score should be {initial_score + 1 + additional_points} after multiple increments"

def test_food_position_is_invalid(game):
    # Set the snake's positions manually for testing
    game.snake.positions = [
        [0, 0, 0],  # Head of the snake
        [1, 0, 0],  # First segment of the snake
        [2, 0, 0],  # Second segment of the snake
        # ... additional segments as needed
    ]

    # Test case where food spawns in an empty spot
    game.food.x = 3
    game.food.y = 3
    assert not game.food_position_is_invalid(), "Food should be valid if it's not colliding with the snake."

    # Test case where food spawns where the snake is
    game.food.x = 1
    game.food.y = 0
    assert game.food_position_is_invalid(), "Food should be invalid if it's colliding with the snake."

def test_food_initial_position(game):
    # Check if food is within the boundaries
    assert 0 <= game.food.x < game.width
    assert 0 <= game.food.y < game.height

    # Check if food is not in the same position as the snake
    snake_positions = set((segment[0], segment[1]) for segment in game.snake.positions)
    assert (game.food.x, game.food.y) not in snake_positions