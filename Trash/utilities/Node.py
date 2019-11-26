class Node:
    def __init__(self,id="",machine_address="",value=""):
        self.id=id
        self.machine_address = machine_address
        self.value=value
        self.neighbors =[]
        self.graphic_position_circle=None
        self.graphic_position_title = None
        self.visited = False
        self.path=[]
        self.distance = 0

    def get_id(self):
        return self.id

    def get_machine_address(self):
        return self.machine_address

    def add_neighbor(self,neighbor):
        self.neighbors.append(neighbor)

    def remove_neighbor(self,neighbor):
        self.neighbors.remove(neighbor)

    def set_value(self,value):
        self.value = value

    def get_value(self):
        return self.value

    def get_neighbors_list(self):
        return self.neighbors

    def set_graphic_position_circle(self,pos):
        self.graphic_position_circle = pos

    def get_graphic_position_circle(self):
        return self.graphic_position_circle

    def set_graphic_position_title(self,pos):
        self.graphic_position_title = pos

    def get_graphic_position_title(self):
        return self.graphic_position_title

    def set_visited(self,value):
        self.visited = value

    def is_visited(self):
        return self.visited

    def add_path(self, path):
        self.path = path

    def get_current_path(self):
        return self.path