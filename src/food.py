import pygame
import random

class Food:
    def __init__(self, display, block_size, width, height):
        self.display = display
        self.color = (0, 255, 0)  # Green
        self.block_size = block_size
        self.x = round(random.randrange(0, width - block_size) / block_size) * block_size
        self.y = round(random.randrange(0, height - block_size) / block_size) * block_size

    def draw(self):
        pygame.draw.rect(self.display, self.color, [self.x, self.y, self.block_size, self.block_size])

    def relocate(self, width, height):
        self.x = round(random.randrange(0, width - self.block_size) / self.block_size) * self.block_size
        self.y = round(random.randrange(0, height - self.block_size) / self.block_size) * self.block_size
