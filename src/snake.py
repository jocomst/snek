import renderer

class Snake3D:
    def __init__(self, block_size, model_path=None):
        self.renderer = renderer
        self.color = (0, 0, 0)  # Black, though this may not be used in 3D
        self.block_size = block_size
        # Initialize with a position in 3D space, with z being up
        self.positions = [[0, 0, 0]]  
        self.model_loaded = False
        # Initialize x_change, y_change, and z_change to zero
        self.x_change = 0
        self.y_change = 0
        self.z_change = 0
        
        if model_path:
            try:
                self.model = self.load_model(model_path)
                self.model_loaded = True
            except Exception as e:
                print(f"Could not load the model at {model_path}: {e}")
                self.model = None

    # Model loading should be done using OpenGL if you have a 3D model
    def load_model(self, model_path):
        # OpenGL model loading logic goes here
        pass

    def move(self, x_change, y_change, z_change):
        self.x_change = x_change
        self.y_change = y_change
        self.z_change = z_change

    def update(self):
        head_x, head_y, head_z = self.positions[-1]
        new_head = [head_x + self.x_change, head_y + self.y_change, head_z + self.z_change]
        self.positions.append(new_head)
        self.positions.pop(0)

    def grow(self):
        head_x, head_y, head_z = self.positions[-1]
        new_head = [head_x + self.x_change, head_y + self.y_change, head_z + self.z_change]
        self.positions.append(new_head)

    def draw(self, renderer):
        for segment in self.positions:
            # In the 3D version, we don't just draw a rectangle, but rather a 3D cube or the loaded model
            renderer.draw_segment(segment, size=self.block_size)
