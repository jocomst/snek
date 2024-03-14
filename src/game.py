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

        # Load Grass Texture
        self.grass_texture_id = self.renderer.load_texture('./models/grassTexture.jpg')

        # Initialize the scene, camera, and lighting
        self.renderer.initialize_scene()
        self.renderer.setup_camera()
        self.renderer.setup_lighting()

    def run_game(self):
        while not self.game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_over = True
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.snake.move(0, self.snake.block_size, 0)
                    elif event.key == pygame.K_DOWN:
                        self.snake.move(0, -self.snake.block_size, 0)
                    elif event.key == pygame.K_LEFT:
                        self.snake.move(-self.snake.block_size, 0, 0)
                    elif event.key == pygame.K_RIGHT:
                        self.snake.move(self.snake.block_size, 0, 0)

            # Clear the screen and depth buffer
            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

            # Draw the grass texture
            # self.renderer.draw_square(self.grass_texture_id)
            self.renderer.draw_triangle()

            # Update and draw the snake
            self.snake.update()
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
