import pygame
import random

class Food:
    def __init__(self, display, block_size, width, height, model_path=None):
        self.display = display
        self.color = (0, 255, 0)  # Green
        self.block_size = block_size
        self.model_loaded = False
        self.x = round(random.randrange(0, width - block_size) / block_size) * block_size
        self.y = round(random.randrange(0, height - block_size) / block_size) * block_size

        # Try to load the model if a path is provided
        if model_path:
            try:
                self.model = self.load_model(model_path)
                self.model_loaded = True
            except IOError:
                print(f"Unable to load model from {model_path}. Falling back to default representation.")
                self.model = None

    def load_model(self, model_path):
        # This is a placeholder for the model loading logic
        # You'll need to use an appropriate method from your 3D library
        # For now, we'll just simulate it with a Pygame Surface
        return pygame.image.load(model_path)

    def draw(self):
        if self.model_loaded:
            # Draw the loaded model
            # Placeholder: blit the model image onto the display
            self.display.blit(self.model, (self.x, self.y))
        else:
            # Draw the default representation
            pygame.draw.rect(self.display, self.color, [self.x, self.y, self.block_size, self.block_size])

    def relocate(self, width, height):
        self.x = round(random.randrange(0, width - self.block_size) / self.block_size) * self.block_size
        self.y = round(random.randrange(0, height - self.block_size) / self.block_size) * self.block_size