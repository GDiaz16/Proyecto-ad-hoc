import socket
import threading
import pickle

from utilities.Graph import Graph
from utilities.Node import Node


class IO:

    def __init__(self,machine_address,server_port, node_id,GUI=None):
        # Nodo como servidor-----
        self.machine_address = machine_address
        self.server_port = server_port
        self.machine_id = node_id
        self.socket_as_server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.socket_as_server.bind(("localhost",self.machine_address))
        self.socket_as_server.listen(10)
        self.connected = False
        self.GUI = GUI
        self.processes()
        self.tabla = []
        self.graph = Graph()
        if GUI != None:
            self.my_graph()
        #Encabezado para cada tipo de mensaje
        self.HEADERS = ["<MPR?>--------------",
                        "<MPR=>--------------",
                        "<MSG=>--------------",
                        "<ID?>---------------",
                        "<ID=>---------------"]

    def my_graph(self):
        self.graph.add_node(Node(id="N1"))
        self.graph.add_node(Node(id="N2"))
        self.graph.add_node(Node(id="N3"))
        self.graph.add_node(Node(id="N4"))
        self.graph.add_node(Node(id="N5"))
        nodes = self.graph.get_node_list()
        nodes[0].add_neighbor("N2")
        nodes[1].add_neighbor("N3")
        nodes[2].add_neighbor("N4")
        nodes[3].add_neighbor("N1")
        #for node in nodes:
        print(self.graph.get_edges_list())
        print(nodes[0].get_id())

        self.GUI.create_graph(nodes,"")

    def get_id(self):
        return self.machine_id

    def connect_node(self):
        # Nodo como cliente------
        while not self.connected:
            try:
                self.socket_as_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                self.socket_as_client.connect(("localhost",self.server_port ))
                t2 = threading.Thread(target=self.receive, args=(self.socket_as_client,))
                t2.start()
                self.connected = True
            except:
                pass

    def update_MPR(self):
        for client in self.clients:
            #Pedir la MPR a los nodos hijo
            self.send(client,self.fit_data(0,""))

    def processes(self):
        self.clients=[]
        threads = list()
        t1 = threading.Thread(target=self.connections_as_server)
        t2 = threading.Thread(target=self.connect_node)
        t3 = threading.Thread(target=self.command)
        t1.start()
        t2.start()
        t3.start()

    def connections_as_server(self):
        while True:
            #Aceptar una conexion y asignarle un hilo
            client_socket, address = self.socket_as_server.accept()
            self.clients.append(client_socket)
            t1 = threading.Thread(target=self.receive,args=(client_socket,))
            t1.start()
            print(len(self.clients))
            print(f"Connection from: {address}")
            #Pedir a la nueva conexion su identificacion
            self.request_id(client_socket)

    def receive(self, socket_c):
        while True:
            data = socket_c.recv(1024)
            if data != '':
                #Separar el header de los datos
                header = data[0:20]
                data = data[20:]
                self.protocols(header,data,socket_c)

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
            self.tabla.append(data)

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
                    self.send(self.clients[i],self.fit_data(2,com))

            elif com == "update":
                self.update_MPR()


