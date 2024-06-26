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

        # Initialize x and y within the range and as multiples of block_size
        self.x = random.randrange(0, self.width, self.block_size)
        self.y = random.randrange(0, self.height, self.block_size)
        self.z = self.block_size  # Set z to block_size, assuming the food is one block_size above the ground

        # If a model_path is provided, try to load a 3D model
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

    def draw(self, x=None, y=None, z=None):
            # Use provided coordinates if available, otherwise use the food's current position
            draw_x = x if x is not None else self.x
            draw_y = y if y is not None else self.y
            draw_z = z if z is not None else self.z

            if self.model_loaded:
                # Draw the loaded model, you will need a method in the renderer for this
                # This is a placeholder for drawing a 3D model, replace it with the actual model rendering logic
                pass
            else:
                # Use the renderer's draw_cube method to draw the food as a cube
                self.renderer.draw_cube([draw_x, draw_y, draw_z], self.block_size, self.color)

    def relocate(self):
        self.x = round(random.randrange(0, self.width - self.block_size) / self.block_size) * self.block_size
        self.y = round(random.randrange(0, self.height - self.block_size) / self.block_size) * self.block_size
        # Optionally, you may also want to randomize the z-axis if you have a 3D field with varying elevation
