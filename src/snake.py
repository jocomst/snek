class Snake3D:
    def __init__(self, renderer, block_size, model_path=None):
        self.renderer = renderer  # Assuming renderer is passed in as a parameter
        self.color = (1, 0, 0)  # Red color for the snake
        self.block_size = block_size
        self.positions = [[0, 0, 0]]  # Initialize with a position in 3D space, with z being up
        self.model_loaded = False

        self.x_change = self.block_size  # Initial movement direction along x-axis
        self.y_change = 0
        self.z_change = 0
        
        # If a model_path is provided, try to load a 3D model, otherwise the snake will be drawn with cubes
        if model_path:
            try:
                self.model = self.load_model(model_path)
                self.model_loaded = True
            except Exception as e:
                print(f"Could not load the model at {model_path}: {e}")
                self.model = None

    # ... rest of your class methods ...

    def draw(self):
        # Iterate through the snake's positions and draw each segment
        for position in self.positions:
            # Here the renderer's draw_cube method is used to draw each segment of the snake
            self.renderer.draw_cube(position, self.block_size, self.color)

    def move(self, x_change, y_change, z_change):
        # Update movement direction
        self.x_change = x_change
        self.y_change = y_change
        self.z_change = z_change

    def update(self):
        # Calculate new head position based on the current direction
        head_x, head_y, head_z = self.positions[-1]
        new_head = [head_x + self.x_change, head_y + self.y_change, head_z + self.z_change]
        
        # Add the new head to the snake's body
        self.positions.append(new_head)
        
        # Remove the last segment of the tail
        self.positions.pop(0)

    def grow(self):
        # When growing, we don't remove the tail segment
        head_x, head_y, head_z = self.positions[-1]
        new_head = [head_x + self.x_change, head_y + self.y_change, head_z + self.z_change]
        self.positions.append(new_head)

# Rest of your class methods remains unchanged
