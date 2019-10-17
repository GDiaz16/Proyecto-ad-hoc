class Node:
    def __init__(self,id,value=""):
        self.id=id
        self.value=value
        self.neighbors =[]
        self.graphic_position_circle=None
        self.graphic_position_title = None

    def get_id(self):
        return self.id

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