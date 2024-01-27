# test_food.py
import pytest
from food import Food

# Mocking pygame display surface for tests
class MockDisplay:
    def get_width(self):
        return 800

    def get_height(self):
        return 600

@pytest.fixture
def mock_display():
    return MockDisplay()

@pytest.fixture
def food(mock_display):
    block_size = 20
    width = mock_display.get_width()
    height = mock_display.get_height()
    return Food(mock_display, block_size, width, height)

def test_food_initial_position_within_bounds(food, mock_display):
    width = mock_display.get_width()
    height = mock_display.get_height()
    block_size = food.block_size

    assert 0 <= food.x < width
    assert 0 <= food.y < height
    assert food.x % block_size == 0
    assert food.y % block_size == 0

def test_food_relocate_within_bounds(food, mock_display):
    width = mock_display.get_width()
    height = mock_display.get_height()
    block_size = food.block_size

    # Call relocate and check multiple times to ensure randomness doesn't place it out of bounds
    for _ in range(10):
        food.relocate(width, height)
        assert 0 <= food.x < width
        assert 0 <= food.y < height
        assert food.x % block_size == 0
        assert food.y % block_size == 0
