import pygame
import snake
import food

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
        while not self.game_over:
            while self.game_close:
                self.game_display.fill(self.white)
                self.message("You Lost! Press C-Play Again or Q-Quit", self.red)
                pygame.display.update()

                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_q:
                            self.game_over = True
                            self.game_close = False
                        if event.key == pygame.K_c:
                            self.__init__()  # Reinitialize the game

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_over = True
                if event.type == pygame.KEYDOWN:
                    # Handle snake movement
                    self.handle_snake_movement(event)

            self.update_game_state()
            pygame.display.update()
            self.clock.tick(self.snake_speed)

        pygame.quit()
        quit()

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

        if self.player_snake.positions[-1][0] == self.apple.x and self.player_snake.positions[-1][1] == self.apple.y:
            self.apple.relocate(self.width, self.height)
            self.player_snake.grow()


            self.player_snake.update()
            self.game_display.fill(self.white)
            self.apple.draw()
            self.player_snake.draw()

            if self.player_snake.positions[-1][0] == self.apple.x and self.player_snake.positions[-1][1] == self.apple.y:
                self.apple.relocate(self.width, self.height)
                self.player_snake.grow()

    def check_collision(self):
        head = self.player_snake.positions[-1]
        return head[0] >= self.width or head[0] < 0 or head[1] >= self.height or head[1] < 0

# To run the game
if __name__ == "__main__":
    game = SnakeGame()
    game.run_game()
