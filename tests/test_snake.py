import os
import sys
import unittest
from unittest.mock import Mock, patch, MagicMock

# Calculate the absolute path to the src directory and append it to sys.path
current_dir = os.path.dirname(__file__)
parent_dir = os.path.join(current_dir, os.pardir)
src_path = os.path.abspath(os.path.join(parent_dir, 'src'))
sys.path.insert(0, src_path)


from snake import Snake3D

class MockRenderer:
    # A mock renderer class to mimic the real renderer
    def draw_cube(self, position, size, color):
        pass  # The mock doesn't actually do anything

class TestSnake3D(unittest.TestCase):

    def setUp(self):
        self.block_size = 1
        self.renderer = MockRenderer()
        self.snake = Snake3D(self.renderer, self.block_size)

    def test_initial_position(self):
        # Test that the snake starts at the correct position
        self.assertEqual(self.snake.positions, [[0, 0, 0]])

    def test_update_within_boundaries(self):
        # Test that the snake updates correctly within boundaries
        self.snake.positions = [[0, 0, 0]]
        self.snake.x_change = self.block_size
        self.snake.y_change = 0
        self.snake.z_change = 0
        self.snake.update()
        self.assertIn([self.block_size, 0, 0], self.snake.positions)

    def test_get_state(self):
        # Test get_state method
        state = self.snake.get_state()
        self.assertEqual(state['positions'], self.snake.positions)
        self.assertEqual(state['block_size'], self.snake.block_size)
        self.assertEqual(state['color'], self.snake.color)

    def test_draw(self):
        # Mock the draw_cube method to ensure it's called correctly
        self.renderer.draw_cube = MagicMock()

        # Simulate movement to generate more positions
        self.snake.x_change = self.block_size
        for _ in range(3):
            self.snake.update()

        # Now, call the draw method and check if draw_cube is called correctly
        self.snake.draw()

        # draw_cube should be called once for each position in the snake's body
        self.assertEqual(self.renderer.draw_cube.call_count, len(self.snake.positions))
        for position in self.snake.positions:
            self.renderer.draw_cube.assert_any_call(position, self.snake.block_size, self.snake.color)

# More tests can be added here to cover all aspects of the Snake3D class.

# Tests for model loading can be omitted if you're handling this entirely within OpenGL and not using pygame