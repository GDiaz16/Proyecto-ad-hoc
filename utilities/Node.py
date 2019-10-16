class Node:
    def __init__(self,id,value):
        self.id=id
        self.value=value
        self.neighbors =[]

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