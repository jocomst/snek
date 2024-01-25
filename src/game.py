import pygame
import snake
import food

# Initialize Pygame
pygame.init()

# Colors
white = (255, 255, 255)
red = (255, 0, 0)

# Game Display Setup
width, height = 600, 400
game_display = pygame.display.set_mode((width, height))
pygame.display.set_caption('Snake Game')

# Game Clock
clock = pygame.time.Clock()

# Game Variables
snake_block = 10
snake_speed = 15
font_style = pygame.font.SysFont(None, 50)

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    game_display.blit(mesg, [width / 6, height / 3])

def run_game():
    player_snake = snake.Snake(game_display, snake_block)
    apple = food.Food(game_display, snake_block, width, height)
    game_over = False
    game_close = False

    while not game_over:
        while game_close:
            game_display.fill(white)
            message("You Lost! Press C-Play Again or Q-Quit", red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        run_game()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player_snake.move(-snake_block, 0)
                elif event.key == pygame.K_RIGHT:
                    player_snake.move(snake_block, 0)
                elif event.key == pygame.K_UP:
                    player_snake.move(0, -snake_block)
                elif event.key == pygame.K_DOWN:
                    player_snake.move(0, snake_block)

        if player_snake.positions[-1][0] >= width or player_snake.positions[-1][0] < 0 or player_snake.positions[-1][1] >= height or player_snake.positions[-1][1] < 0:
            game_close = True

        player_snake.update()
        game_display.fill(white)
        apple.draw()
        player_snake.draw()

        if player_snake.positions[-1][0] == apple.x and player_snake.positions[-1][1] == apple.y:
            apple.relocate(width, height)
            player_snake.grow()

        pygame.display.update()
        clock.tick(snake_speed)

    pygame.quit()
    quit()
