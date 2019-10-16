class Graph:

    def __init__(self):
        self.node_list=[]

    def add_node(self, node):
        self.node_list.append(node)

    def remove_node(self,node):
        self.node_list.remove(node)

    def path_A_B(self):
        pass