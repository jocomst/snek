import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import snake  # You will need to update this for 3D
import food  # You will need to update this for 3D
from renderer import Renderer


class SnakeGame:
    def __init__(self):
        pygame.init()

        # Game Configuration
        self.width, self.height = 600, 400
        self.white = (255, 255, 255)
        self.red = (255, 0, 0)
        self.snake_block = 10
        self.snake_speed = 15

        # Game Initialization
        self.game_display = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption('Snake Game')
        self.clock = pygame.time.Clock()
        self.font_style = pygame.font.SysFont(None, 50)
        # Initialize Renderer
        self.renderer = Renderer()  # This line initializes the renderer property

        # Game State
        self.game_over = False
        self.game_close = False

        # Game Entities
        self.player_snake = snake.Snake(self.game_display, self.snake_block)
        self.apple = food.Food(self.game_display, self.snake_block, self.width, self.height)

        # Game Grass Texture
        try:
            self.grass_texture = pygame.image.load('./models/grassTexture.jpg')
            self.grass_texture = pygame.transform.scale(self.grass_texture, (self.width, self.height))
        except pygame.error:
            self.grass_texture = None

    def message(self, msg, color):
        mesg = self.font_style.render(msg, True, color)
        self.game_display.blit(mesg, [self.width / 6, self.height / 3])

    def run_game(self): 
        # Initialize OpenGL settings
        pygame.display.set_mode((800, 600), pygame.DOUBLEBUF | pygame.OPENGL)
        self.renderer.initialize_scene()

        while not self.game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_over = True
                if event.type == pygame.KEYDOWN:
                    # Handle snake movement here (adapted for 3D if necessary)

                        # Clear the screen and depth buffer
                    # glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

                        # Setup the camera for each frame
                    self.renderer.setup_camera()

                        # Render a 3D scene here
                        # For example, setup lighting (if you haven't already)
                    self.renderer.setup_lighting()

                        # Draw a flat plane (You'll need to implement this method)
                    self.renderer.draw_triangle()

                        # Swap buffers to display the scene
                    pygame.display.flip()
                    self.clock.tick(self.snake_speed)

                    pygame.quit()

    def handle_snake_movement(self, event):
        if event.key == pygame.K_LEFT:
            self.player_snake.move(-self.snake_block, 0)
        elif event.key == pygame.K_RIGHT:
            self.player_snake.move(self.snake_block, 0)
        elif event.key == pygame.K_UP:
            self.player_snake.move(0, -self.snake_block)
        elif event.key == pygame.K_DOWN:
            self.player_snake.move(0, self.snake_block)

    def update_game_state(self):
        if self.check_collision():
            self.game_close = True

        self.player_snake.update()
        
        # Draw the grass texture if it's loaded, otherwise fill with white.
        if self.grass_texture:
            self.game_display.blit(self.grass_texture, (0, 0))
        else:
            self.game_display.fill(self.white)
        
        self.apple.draw()
        self.player_snake.draw()

        # Check if the snake has eaten the apple
        if self.player_snake.positions[-1][0] == self.apple.x and self.player_snake.positions[-1][1] == self.apple.y:
            self.apple.relocate(self.width, self.height)
            self.player_snake.grow()
        
        # Update the display only after all drawing operations
        pygame.display.update()
    

    def check_collision(self):
        head = self.player_snake.positions[-1]
        return head[0] >= self.width or head[0] < 0 or head[1] >= self.height or head[1] < 0

# To run the game
if __name__ == "__main__":
    game = SnakeGame()
    game.run_game()
