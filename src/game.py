import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from renderer import Renderer
from snake import Snake3D

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
        movement_increment = 0.1  # Set a small value for movement

        while not self.game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_over = True
                elif event.type == pygame.KEYDOWN:
                    # Reset movement to zero each time to avoid continuous movement
                    x_change = y_change = 0
                    
                    # Update the direction based on the key press
                    if event.key == pygame.K_UP:
                        y_change = movement_increment  # Move up
                    elif event.key == pygame.K_DOWN:
                        y_change = -movement_increment  # Move down
                    elif event.key == pygame.K_LEFT:
                        x_change = -movement_increment  # Move left
                    elif event.key == pygame.K_RIGHT:
                        x_change = movement_increment  # Move right

                    # Update the snake's position based on the key press
                    self.snake.x += x_change
                    self.snake.y += y_change
                    self.snake.positions[-1] = [self.snake.x, self.snake.y, self.snake.z]

            # Clear the screen and depth buffer
            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

            # Draw the grass texture
            self.renderer.draw_square(self.grass_texture_id)

            # Draw the snake in its new position
            self.snake.draw()

            # Swap buffers to display the scene
            pygame.display.flip()

            # Cap the frame rate
            self.clock.tick(60)

        # Clean up and close the game properly
        pygame.quit()


# To run the game
if __name__ == "__main__":
    game = SnakeGame()
    game.run_game()
