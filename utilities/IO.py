import socket
import threading
import pickle

from utilities.Graph import Graph
from utilities.Node import Node


class IO:

    def __init__(self,machine_address,server_port, node_id):
        self.machine_address = machine_address
        self.server_port = server_port
        self.machine_id = node_id
        # Nodo como servidor-----
        self.socket_as_server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.socket_as_server.bind(("localhost",self.machine_address))
        self.socket_as_server.listen(10)

        self.clients=[] #[socket, id]
        self.connected = False
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
                        "<U-GRAFO=>----------",
                        "<REP=>--------------"]


    def connect_node(self, port = None):
        if port == None:
            port = self.server_port
        # Nodo como cliente------
        connected = False
        while not connected:
            try:
                socket_as_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                socket_as_client.connect(("localhost",port ))
                t2 = threading.Thread(target=self.receive, args=(socket_as_client,))
                t2.start()
                self.clients.append([socket_as_client,""])
                self.request_id(socket_as_client)
                print(f"Connected to {socket_as_client}")
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
            self.clients.append([client_socket, ""])
            #Pedir a la nueva conexion su identificacion
            self.request_id(client_socket)

    #Desconectar un nodo dado su id
    def disconnect_node(self,node_id):
        for client in self.clients:
            if client[1]==node_id:
                client[0].close()
                self.clients.remove(client)
                break

    def update_MPR(self):
        for client in self.clients:
            #Pedir la MPR a los nodos hijo
            self.send(client[0],self.fit_data(0,""))

    #Procesos corriendo continuamente
    def processes(self):
        t1 = threading.Thread(target=self.connections_as_server)
        t3 = threading.Thread(target=self.command)
        t1.start()
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
            #Manejar el error en caso de desconexion o cierre de la conexion
            except (ConnectionResetError,  ConnectionAbortedError):
                for client in self.clients:
                    if client[0] == socket_c:
                        print(f"Se ha cortado la comunicacion con {client[1]}")
                        self.clients.remove(client)
                        #Intentar reconectar nuevamente con el nodo que se desconecto sin previo aviso
                        for node in self.graph.get_node_list():
                            if node.get_id() == client[1]:
                                t = threading.Thread(target=self.connect_node,
                                                     args=(node.get_id(), node.get_machine_address(),))
                                t.start()
                                break
                        return

    #Enviar un mensaje previamente empaquetado a traves del socket especificado
    def send(self,socket,message):
        try:
            socket.send(message.encode('utf-8'))
        except:
            socket.send(message)

    #Instrucciones a realizar dependiendo del tipo de mensaje
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
        elif header == self.HEADERS[6]:
            self.disconnect_node(data)
        elif header == self.HEADERS[7]:
            self.graph = data
            self.graph.print_connections()

    #Asignarle un identificador a un socket
    def assign_id(self,socket,id):
        for client in self.clients:
            if client[0] == socket:
                client[1]=id
                break

    #Funciones de identificacion
    def request_id(self,socket):
        self.send(socket,self.fit_data(3,""))

    def send_id(self,socket):
        self.send(socket,self.fit_data(4,self.machine_id))

    def get_id(self):
        return self.machine_id

    def send_MPR(self,socket):
        #Enviar tabla MPR
        msg = self.fit_data(1,self.tabla)
        self.send(socket, msg)

    #empaquetar datos para enviarlos a traves del socket
    def fit_data(self, header, data):
        msg = self.HEADERS[header].encode('utf-8')+pickle.dumps(data)
        return msg

    #Replicar un mensaje hasta que llegue a su destinatario
    def replicate(self, data):
        path = data.get_path()
        path.reverse()
        next_node = path.pop()
        for client in self.clients:
            if client[1]== next_node:
                self.send(client[0], self.fit_data(9, data))

    #consola de comandos
    def command(self):
        while True:
            com = input(">")
            if com == "broadcast":
                com = input(">>")
                for i in range(len(self.clients)):
                    self.send(self.clients[i][0],self.fit_data(2,com))

            elif com == "update":
                self.update_MPR()

            elif com == "send":
                target = input("target>>")
                message = input("message>>")




