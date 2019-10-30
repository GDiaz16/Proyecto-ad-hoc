import socket
import threading
import pickle

from utilities.Graph import Graph
from utilities.Node import Node


class IO_MASTER:

    def __init__(self,machine_address,server_port, node_id,GUI):
        self.machine_address = machine_address
        #self.server_port = server_port
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

        #Encabezado para cada tipo de mensaje
        self.HEADERS = ["<MPR?>--------------",
                        "<MPR=>--------------",
                        "<MSG=>--------------",
                        "<ID?>---------------",
                        "<ID=>---------------",
                        "<CONNECT-TO=>-------",
                        "<DISCONNECT-OF=>----",
                        "<U-GRAFO=>----------"]

        #Crear entorno grafico
        self.my_graph()


    def my_graph(self):

        self.graph.add_node(Node(id="N1", machine_address=10001))
        self.graph.add_node(Node(id="N2", machine_address=10002))
        self.graph.add_node(Node(id="N3", machine_address=10003))
        self.graph.add_node(Node(id="N4", machine_address=10004))
        self.graph.add_node(Node(id="N5", machine_address=10005))
        self.graph.add_node(Node(id="N6", machine_address=10006))
        for node in self.graph.get_node_list():
            t = threading.Thread(target=self.connect_node, args=(node.get_id(),node.get_machine_address(),))
            t.start()

        self.GUI.create_graph(self.graph)

    def get_id(self):
        return self.machine_id

    def connect_node(self, node_id, port=None):
        if port == None:
            print("No port provided!")
            return
        # Nodo como cliente------
        connected = False
        while not connected:
            try:
                socket_as_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                socket_as_client.connect(("localhost",port ))
                t2 = threading.Thread(target=self.receive, args=(socket_as_client,))
                t2.start()
                #self.send_graph()
                self.clients.append([socket_as_client,node_id])
                print(len(self.clients))
                print(f"Connected to: {node_id}")
                connected = True
            except:
                pass

    def disconnect(self,node_id_A, node_id_B):
        for client in self.clients:
            if client[1] == node_id_A:
                self.send(client[0],self.fit_data(6, node_id_B))
                self.send_graph()

    def connect_to(self,node_id_A, node_address_B):
        #Buscar el nodo A y enviarle la orden de que se conecte al nodo B
        for client in self.clients:
            if client[1] == node_id_A:
                self.send(client[0],self.fit_data(5, node_address_B))
                self.send_graph()
                break

    def update_MPR(self):
        for client in self.clients:
            #Pedir la MPR a los nodos hijo
            self.send(client[0],self.fit_data(0,""))

    def processes(self):
        t = threading.Thread(target=self.command)
        t.start()

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

                    for client in self.clients:
                        if client[0]==socket_c:
                            print(f"Se ha cortado la comunicacion con {client[1]}")
                            self.clients.remove(client)
                            for node in self.graph.get_node_list():
                                if node.get_id()==client[1]:
                                    t = threading.Thread(target=self.connect_node, args=(node.get_id(), node.get_machine_address(),))
                                    t.start()
                                    break
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

    def send_graph(self):
        for i in range(len(self.clients)):
            self.send(self.clients[i][0], self.fit_data(7, self.graph))

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

            elif com == "send-graph":
                self.send_graph()




