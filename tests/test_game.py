import pytest
import pygame
import os
import sys

# Calculate the absolute path to the src directory and append it to sys.path
current_dir = os.path.dirname(__file__)
parent_dir = os.path.join(current_dir, os.pardir)
src_path = os.path.abspath(os.path.join(parent_dir, 'src'))
sys.path.insert(0, src_path)

import snake
import food
from game import SnakeGame  # Assuming your game class is in a file named game.py

@pytest.fixture
def game():
    """Fixture to create a game instance for each test."""
    game_instance = SnakeGame()
    yield game_instance
    # Teardown code here if necessary, e.g., closing the Pygame window
    pygame.quit()

def test_initialization(game):
    """Test game initializes with correct default values."""
    assert game.width == 600
    assert game.height == 400
    assert not game.game_over
    assert not game.game_close

def test_game_initialization_with_renderer(game):
    """Test if the SnakeGame is initialized with a renderer property."""
    assert hasattr(game, 'renderer'), "SnakeGame instance should have a 'renderer' property"
    assert game.renderer is not None, "'renderer' property should not be None"

# Test to ensure the grass texture loads correctly
def test_grass_texture_loading():
    game = SnakeGame()

    try:
        # Attempt to load the grass texture
        grass_texture = pygame.image.load('./models/fakeModel.png')
        grass_texture = pygame.transform.scale(grass_texture, (game.width, game.height))
        assert game.grass_texture is not None
        assert grass_texture.get_width() == game.width
        assert grass_texture.get_height() == game.height
    except pygame.error:
        # If the texture loading fails, check if the game uses the white background
        assert game.grass_texture is None
        assert game.game_display.get_at((0, 0)) == game.white
