import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from renderer import Renderer
from snake import Snake3D
from food import Food

class SnakeGame:
    def __init__(self):
        pygame.init()

        # Game Configuration
        self.width, self.height = 800, 600

        self.score = 0  # Initialize the score attribute

        # Game Initialization
        self.game_display = pygame.display.set_mode((self.width, self.height), pygame.DOUBLEBUF | pygame.OPENGL)
        pygame.display.set_caption('Snake Game')
        self.clock = pygame.time.Clock()

        # Initialize Renderer
        self.renderer = Renderer(self.width, self.height)  # Pass width and height to Renderer

        # Initialize Snake
        self.snake = Snake3D(self.renderer, block_size=1)  # Block size set to 1 for example

        # Initialize Food
        self.food = Food(self.renderer, block_size=1, width=self.width, height=self.height, depth=100)

        # Game State
        self.game_over = False

        # Game Score
        self.score = 0

        # Load Grass Texture
        self.grass_texture_id = self.renderer.load_texture('./models/grassTexture.jpg')

        # Initialize the scene, camera, and lighting
        self.renderer.initialize_scene()
        self.renderer.setup_camera()
        self.renderer.setup_lighting()

    def update_score(self):
        # Method to update the score
        self.score += 1

    def run_game(self):
        movement_increment = 0.1  # Movement increment

        while not self.game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_over = True
                elif event.type == pygame.KEYDOWN:
                    # Set the direction based on the key press
                    if event.key == pygame.K_UP:
                        self.snake.set_direction(0, movement_increment)
                    elif event.key == pygame.K_DOWN:
                        self.snake.set_direction(0, -movement_increment)
                    elif event.key == pygame.K_LEFT:
                        self.snake.set_direction(-movement_increment, 0)
                    elif event.key == pygame.K_RIGHT:
                        self.snake.set_direction(movement_increment, 0)

            # Update the snake's position
            self.snake.update()

            # Clear the screen and depth buffer
            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

            # Draw the grass texture and the snake
            self.renderer.draw_square(self.grass_texture_id)
            self.snake.draw()
            self.food.draw()  # Draw the food

            # Swap buffers to display the scene
            pygame.display.flip()

            # Cap the frame rate
            self.clock.tick(60)

        # Cleanup
        pygame.quit()

    def food_position_is_invalid(self):
        """Check if the current food position is within the snake's body."""
        return any(segment[:2] == [self.food.x, self.food.y] for segment in self.snake.positions)


# To run the game
if __name__ == "__main__":
    game = SnakeGame()
    game.run_game()
