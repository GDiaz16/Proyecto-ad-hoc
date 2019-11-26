class GraphicObject:
    def __init__(self, type="",coords="",color="red",canvas_position=""):
        self.canvas_position=canvas_position
        self.type = type
        self.coords= coords
        self.color = color

    def get_type(self):
        return self.type

    def get_coords(self):
        return self.coords

    def get_color(self):
        return self.color

    def get_canvas_position(self):
        return self.canvas_position

    def set_coords(self,coords):
        self.coords = coords