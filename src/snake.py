class Snake3D:
    def __init__(self, renderer, block_size, model_path=None):
        self.renderer = renderer  # Assuming renderer is passed in as a parameter
        self.color = (1, 0, 0)  # Red color for the snake
        self.block_size = block_size
        self.model_loaded = False

        self.x = 0
        self.y = 0
        self.z = 0
        self.x_change = block_size
        self.y_change = 0
        self.z_change = 0
        self.positions = [[self.x, self.y, self.z]]
        self.max_movements = 5
        self.initial_x = self.x
        self.initial_y = self.y
        self.direction = (0, 0)  # Direction represented as (x_change, y_change)


        
        # If a model_path is provided, try to load a 3D model, otherwise the snake will be drawn with cubes
        if model_path:
            try:
                self.model = self.load_model(model_path)
                self.model_loaded = True
            except Exception as e:
                print(f"Could not load the model at {model_path}: {e}")
                self.model = None

    # ... rest of your class methods ...

    def set_direction(self, x_change, y_change):
        self.direction = (x_change, y_change)

    def draw(self):
        # Iterate through the snake's positions and draw each segment
        for position in self.positions:
            # Here the renderer's draw_cube method is used to draw each segment of the snake
            self.renderer.draw_cube(position, self.block_size, self.color)

    def is_out_of_bounds(self):
        distance_x = abs(self.x - self.initial_x) / self.block_size
        distance_y = abs(self.y - self.initial_y) / self.block_size
        print(f"Distance X: {distance_x}, Distance Y: {distance_y}, Current X: {self.x}, Initial X: {self.initial_x}")
        return distance_x > self.max_movements or distance_y > self.max_movements

    def update(self):
        # Update the snake's position based on its direction
        x_change, y_change = self.direction
        self.x += x_change
        self.y += y_change
        # Update the position list to reflect the new head position
        self.positions.append([self.x, self.y, self.z])
        self.positions.pop(0)  # Remove the tail's last position to simulate movement

    def get_state(self):
        # This method provides the current state of the snake for rendering or other purposes
        return {
            'positions': self.positions,
            'block_size': self.block_size,
            'color': self.color
        }


# Rest of your class methods remains unchanged

