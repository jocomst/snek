import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from renderer import Renderer

class SnakeGame:
    def __init__(self):
        pygame.init()

        # Game Configuration
        self.width, self.height = 800, 600  # Updated for consistency with OpenGL window

        # Game Initialization
        self.game_display = pygame.display.set_mode((self.width, self.height), pygame.DOUBLEBUF | pygame.OPENGL)
        pygame.display.set_caption('Snake Game')
        self.clock = pygame.time.Clock()

        # Initialize Renderer
        self.renderer = Renderer()  # This line initializes the renderer property

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

            # Clear the screen and depth buffer
            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

            # Draw the grass texture
            self.renderer.draw_square(self.grass_texture_id)

            # Swap buffers to display the scene
            pygame.display.flip()

            # Cap the frame rate
            self.clock.tick(60)  # Set to 60 or any other appropriate framerate

        # Clean up and close the game properly
        pygame.quit()

# To run the game
if __name__ == "__main__":
    game = SnakeGame()
    game.run_game()
