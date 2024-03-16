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

    def
