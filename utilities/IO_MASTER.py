import socket
import threading
import pickle

from utilities.Graph import Graph
from utilities.Node import Node


class IO:

    def __init__(self,machine_address,server_port, node_id,GUI=None):
        self.machine_address = machine_address
        self.server_port = server_port
        self.machine_id = node_id
        # Nodo como servidor-----
        self.socket_as_server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.socket_as_server.bind(("localhost",self.machine_address))
        self.socket_as_server.listen(10)

        self.clients=[]
        self.connected = False
        self.GUI = GUI
        self.processes()
        self.tabla = []
        self.graph = Graph()

        #Crear entorno grafico solo si se instancia
        if GUI != None:
            self.my_graph()
        #Encabezado para cada tipo de mensaje
        self.HEADERS = ["<MPR?>--------------",
                        "<MPR=>--------------",
                        "<MSG=>--------------",
                        "<ID?>---------------",
                        "<ID=>---------------",
                        "<CONNECT-TO=>-------"]

    def my_graph(self):


        self.graph.add_node(Node(id="MASTER", machine_address=10000))
        self.graph.add_node(Node(id="N2", machine_address=10001))
        self.graph.add_node(Node(id="N3", machine_address=10002))
        self.graph.add_node(Node(id="N4", machine_address=10003))
        self.graph.add_node(Node(id="N5", machine_address=10004))
        self.graph.add_node(Node(id="N6", machine_address=10005))

        for node in self.graph.get_node_list():
            t = threading.Thread(target=self.connect_node, args=(node.get_machine_address(),))
            t.start()

        self.graph.insert_edge([1, "N1", "N2"])
        self.graph.insert_edge([2, "N3", "N2"])
        self.graph.insert_edge([3, "N4", "N1"])
        self.graph.insert_edge([4, "N4", "N5"])
        self.graph.insert_edge([5, "N3", "N1"])

        nodes = self.graph.get_node_list()
        nodes[0].add_neighbor("N2")
        nodes[1].add_neighbor("N3")
        nodes[2].add_neighbor("N4")
        nodes[3].add_neighbor("N1")
        #for node in nodes:
        list = []
        for edge in self.graph.get_edges_list():
            list.append(edge[1:])

        self.GUI.create_graph(nodes,list)

    def get_id(self):
        return self.machine_id

    def connect_node(self, port = None):
        if port == None:
            port = self.server_port
        # Nodo como cliente------
        connected = False
        while not connected:
            try:
                self.socket_as_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                self.socket_as_client.connect(("localhost",port ))
                t2 = threading.Thread(target=self.receive, args=(self.socket_as_client,))
                t2.start()
                self.clients.append([self.socket_as_client,""])
                self.request_id(self.socket_as_client)
                connected = True
            except:
                pass

    def connections_as_server(self):
        while True:
            #Aceptar una conexion y asignarle un hilo
            client_socket, address = self.socket_as_server.accept()
            self.clients.append([client_socket,""])
            t1 = threading.Thread(target=self.receive,args=(client_socket,))
            t1.start()
            print(len(self.clients))
            print(f"Connection from: {address}")
            #Pedir a la nueva conexion su identificacion
            self.request_id(client_socket)

    def disconnect(self,socket):
        socket.close()

    def connect_to(self,address, node_address):

        self.send(self.connect_node(socket),self.fit_data(5, node_address))

    def update_MPR(self):
        for client in self.clients:
            #Pedir la MPR a los nodos hijo
            self.send(client[0],self.fit_data(0,""))

    def processes(self):
        threads = list()
        t1 = threading.Thread(target=self.connections_as_server)
        t2 = threading.Thread(target=self.connect_node)
        t3 = threading.Thread(target=self.command)
        t1.start()
        t2.start()
        t3.start()

    def receive(self, socket_c):
        while True:
            try:
                data = socket_c.recv(1024)
                if data != '':
                    #Separar el header de los datos
                    header = data[0:20]
                    data = data[20:]
                    self.protocols(header,data,socket_c)
            except ConnectionResetError:
                if socket_c == self.socket_as_client:
                    print("Se ha cortado la comunicacion con el servidor")
                    self.connected = False
                    t = threading.Thread(target=self.connect_node)
                    t.start()
                    return
                else:
                    print(f"Se ha cortado la comunicacion con el cliente:{socket_c}")
                    for client in self.clients:
                        if client[0]==socket_c:
                            self.clients.remove(client)
                            break
                    return

    def send(self,socket,message):
        try:
            socket.send(message.encode('utf-8'))
        except:
            socket.send(message)

    def protocols(self, header,data,socket):
        header = header.decode('utf-8')
        data = pickle.loads(data)
        if header == self.HEADERS[0]:
            self.send_MPR(socket)
        elif header == self.HEADERS[1]:
            self.tabla.append(data)
            print(data)
        elif header == self.HEADERS[2]:
            print(data)
        elif header == self.HEADERS[3]:
            self.send_id(socket)
        elif header == self.HEADERS[4]:
            self.assign_id(socket,data)
        elif header == self.HEADERS[5]:
            self.connect_node(data)

    def assign_id(self,socket,id):
        for client in self.clients:
            if client[0] == socket:
                client[1]=id
                break


    def request_id(self,socket):
        self.send(socket,self.fit_data(3,""))

    def send_id(self,socket):
        self.send(socket,self.fit_data(4,self.machine_id))

    def send_MPR(self,socket):
        #Enviar tabla MPR
        msg = self.fit_data(1,self.tabla)
        self.send(socket, msg)

    def fit_data(self, header, data):
        msg = self.HEADERS[header].encode('utf-8')+pickle.dumps(data)
        return msg

    def command(self):
        while True:
            com = input(">")
            if com == "send":
                com = input(">>")
                for i in range(len(self.clients)):
                    self.send(self.clients[i][0],self.fit_data(2,com))

            elif com == "update":
                self.update_MPR()




