class Graph:

    def __init__(self):
        self.node_list=[]
        self.connections=[]
        #self.connections_by_node=[]

    def add_node(self, node):
        self.node_list.append(node)

    def remove_node(self,node):
        self.node_list.remove(node)

    #Hallar la lista de nodos por la cual debe pasar el recorrido para llegar al nodo B
    def path_A_B(self, node1_id, node2_id):
        if node1_id == node2_id:
            return [node1_id]
        for node in self.node_list:
            if node.name == node1_id:
                return self.find_target(node, node2_id)

    def find_target(self, node1, node2_id):
        #Reiniciar los nodos
        for node in self.node_list:
            node.visited = False
            node.path = []
        #Comenzar con el nodo de origen
        frontier = [node1]
        node1.path = [node1.name]

        while True:
            #colocar los nodos de la frontera como visitados
            for node in frontier:
                node.visited = True

            frontier2 = []
            #visitar los nodos vecinos de cada nodo de la frontera
            for node in frontier:
                for neighbor in node.neighbors:
                    if not neighbor.visited:
                        #Agregar la ruta necesaria para llegar hasta el camino actual
                        neighbor.path = node.get_current_path()+[neighbor.get_id()]
                        neighbor.visited = True
                        #colocar el nodo vecino en la nueva frontera
                        frontier2.append(neighbor)
                        #Devolver el camino cuando se halle el nodo objetivo
                    if neighbor.name == node2_id:
                        #print(f"Path {neighbor.get_current_path()}")
                        return neighbor.path
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

    # def insert_edge(self,connection_graphic,node1_id,node2_id):
    #     edge=[connection_graphic,node1_id,node2_id]
    #     self.connections.append(edge)
        # node1 = None
        # node2 = None
        #
        # for node in self.node_list:
        #     if node.get_id() == node1_id:
        #         node1 = node
        #     elif node.get_id() == node2_id:
        #         node2 = node
        # #Hay una referencia de conexion de los nodos del uno al otro
        # self.add_connection_by_nodes(node1,node2)
        # node1.add_neighbor(node2)
        # node2.add_neighbor(node1)


    def add_connection(self, conn):
        self.connections.append(conn)
        node1 = None
        node2 = None
        for node in self.node_list:
            if node.name == conn.node1.name:
                node1 = node
            elif node.name == conn.node2.name:
                node2 = node
        # Hay una referencia de conexion de los nodos del uno al otro
        #self.add_connection_by_nodes(node1, node2)
        node1.add_neighbor(node2)
        node2.add_neighbor(node1)

        #self.insert_edge(0, conn.device1.name, conn.device2.name)


    # def add_connection_by_nodes(self, node1, node2):
    #     conn=[node1,node2]
    #     self.connections_by_node.append(conn)

    # def get_connections_by_nodes(self):
    #     return self.connections_by_node


