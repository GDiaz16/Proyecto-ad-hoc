class Graph:

    def __init__(self):
        self.node_list=[]

    def add_node(self, node):
        self.node_list.append(node)

    def remove_node(self,node):
        self.node_list.remove(node)

    def path_A_B(self):
        pass

    def get_node_list(self):
        return self.node_list

    def get_edges_list(self):
        neighbors_list =[]
        for node in self.node_list:
            for neighbor in node.get_neighbors_list():
                neighbors_list.append([node.get_id(),neighbor])
        return neighbors_list
