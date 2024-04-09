import random

class Food:
    def __init__(self, renderer, block_size, width, height, depth, model_path=None):
        self.renderer = renderer
        self.color = (0, 255, 0)  # Green color for the food
        self.block_size = block_size
        self.width = width
        self.height = height
        self.depth = depth
        self.model_loaded = False

        # Adjusted initial position for the food within a 0 to 0.5 range
        self.x = (round(random.randrange(0, self.width - self.block_size) / self.block_size) * self.block_size) / self.width
        self.y = (round(random.randrange(0, self.height - self.block_size) / self.block_size) * self.block_size) / self.height
        self.z = 0.01  # Slightly above the ground to ensure visibility

        # If a model_path is provided, try to load a 3D model, otherwise use the default cube representation
        if model_path:
            try:
                self.model = self.load_model(model_path)
                self.model_loaded = True
            except Exception as e:
                print(f"Could not load the model at {model_path}: {e}")
                self.model = None

    def load_model(self, model_path):
        # Implement model loading logic here, for now, let's just return None as a placeholder
        return None

    def draw(self):
        if self.model_loaded:
            # Draw the loaded model, you will need a method in the renderer for this
            pass
        else:
            # Use the renderer's draw_cube method to draw the food as a cube
            self.renderer.draw_cube([self.x, self.y, self.z], self.block_size, self.color)

    def relocate(self):
        self.x = round(random.randrange(0, self.width - self.block_size) / self.block_size) * self.block_size
        self.y = round(random.randrange(0, self.height - self.block_size) / self.block_size) * self.block_size
        # Optionally, you may also want to randomize the z-axis if you have a 3D field with varying elevation
