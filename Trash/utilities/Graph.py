class Graph:

    def __init__(self):
        self.node_list=[]
        self.edges_list=[]
        self.connections_by_node=[]

    def add_node(self, node):
        self.node_list.append(node)

    def remove_node(self,node):
        self.node_list.remove(node)

    #Hallar la lista de nodos por la cual debe pasar el recorrido para llegar al nodo B
    def path_A_B(self, node1_id, node2_id):
        if node1_id == node2_id:
            return [node1_id]
        for node in self.node_list:
            if node.get_id() == node1_id:
                return self.find_target(node, node2_id)

    def find_target(self, node1, node2_id):
        for node in self.node_list:
            node.set_visited(False)
            node.add_path([])
        #Comenzar con el nodo de origen
        frontier = [node1]
        node1.add_path([node1.get_id()])

        while True:
            #colocar los nodos de la frontera como visitados
            for node in frontier:
                node.set_visited(True)

            frontier2 = []
            #visitar los nodos vecinos de cada nodo de la frontera
            for node in frontier:
                for neighbor in node.get_neighbors_list():
                    if not neighbor.is_visited():
                        #Agregar la ruta necesaria para llegar hasta el camino actual
                        neighbor.add_path(node.get_current_path()+[neighbor.get_id()])
                        neighbor.set_visited(True)
                        #colocar el nodo vecino en la nueva frontera
                        frontier2.append(neighbor)
                        #Devolver el camino cuando se halle el nodo objetivo
                    if neighbor.get_id()== node2_id:
                        #print(f"Path {neighbor.get_current_path()}")
                        return neighbor.get_current_path()
            #Actualizar la frontera con los hijos o nodos vecinos de la frontera anterior
            frontier = frontier2

    def get_node_list(self):
        return self.node_list

    def get_neighbors_list(self):
        neighbors_list =[]
        for node in self.node_list:
            for neighbor in node.get_neighbors_list():
                neighbors_list.append([node.get_id(),neighbor])
        return neighbors_list

    def insert_edge(self,connection_graphic,node1_id,node2_id):
        edge=[connection_graphic,node1_id,node2_id]
        self.edges_list.append(edge)
        node1 = None
        node2 = None

        for node in self.node_list:
            if node.get_id() == node1_id:
                node1 = node
            elif node.get_id() == node2_id:
                node2 = node
        #Hay una referencia de conexion de los nodos del uno al otro
        node1.add_neighbor(node2)
        node2.add_neighbor(node1)

    def delete_edge(self,edge):
        self.edges_list.remove(edge)

    def get_edges_list(self):
        return self.edges_list

    def add_connection_by_nodes(self, node1, node2):
        conn=[node1,node2]
        self.connections_by_node.append(conn)

    def get_connections_by_nodes(self):
        return self.connections_by_node

    def print_nodes(self):
        for node in self.node_list:
            print(node.get_id())

    def print_connections(self):
        for conn in self.edges_list:
            print(conn)

"""from utilities.Node import Node
graph = Graph()
graph.add_node(Node(id="N1", machine_address=10001))
graph.add_node(Node(id="N2", machine_address=10002))
graph.add_node(Node(id="N3", machine_address=10003))
graph.add_node(Node(id="N4", machine_address=10004))
graph.add_node(Node(id="N5", machine_address=10005))
graph.add_node(Node(id="N6", machine_address=10006))
graph.add_node(Node(id="N7", machine_address=10001))
graph.add_node(Node(id="N8", machine_address=10002))
graph.add_node(Node(id="N9", machine_address=10003))
graph.add_node(Node(id="N10", machine_address=10004))
graph.add_node(Node(id="N11", machine_address=10005))
graph.add_node(Node(id="N12", machine_address=10006))

graph.insert_edge(0,"N1","N4")
graph.insert_edge(0,"N1","N2")
graph.insert_edge(0,"N1","N3")
graph.insert_edge(0,"N4","N3")
graph.insert_edge(0,"N2","N3")
graph.insert_edge(0,"N3","N5")
graph.insert_edge(0,"N3","N6")
graph.insert_edge(0,"N4","N5")
graph.insert_edge(0,"N2","N8")
graph.insert_edge(0,"N3","N7")
graph.insert_edge(0,"N7","N8")
graph.insert_edge(0,"N7","N9")
graph.insert_edge(0,"N8","N10")
graph.insert_edge(0,"N10","N11")
graph.insert_edge(0,"N9","N11")
graph.insert_edge(0,"N9","N12")
graph.insert_edge(0,"N11","N12")

graph.path_A_B("N6","N10") """