import pygame

class Snake:
    def __init__(self, display, block_size, model_path=None):
        self.display = display
        self.color = (0, 0, 0)  # Black
        self.block_size = block_size
        self.positions = [[display.get_width() / 2, display.get_height() / 2]]
        self.model_loaded = False
        
        if model_path:
            try:
                self.model = self.load_model(model_path)
                self.model_loaded = True
            except Exception as e:
                print(f"Could not load the model at {model_path}: {e}")
                self.model = None
    
    def load_model(self, model_path):
        # Replace this with actual model loading logic.
        # For now, let's assume it's a pygame Surface object.
        return pygame.image.load(model_path)

    def move(self, x_change, y_change):
        self.x_change = x_change
        self.y_change = y_change

    def update(self):
        head_x, head_y = self.positions[-1]
        new_head = [head_x + self.x_change, head_y + self.y_change]
        self.positions.append(new_head)
        self.positions.pop(0)

    def grow(self):
        head_x, head_y = self.positions[-1]
        new_head = [head_x + self.x_change, head_y + self.y_change]
        self.positions.append(new_head)

    def draw(self):
        for segment in self.positions:
            pygame.draw.rect(self.display, self.color, [segment[0], segment[1], self.block_size, self.block_size])
