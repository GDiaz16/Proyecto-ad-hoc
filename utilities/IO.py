import socket
import threading
import pickle

from utilities.Graph import Graph
from utilities.Node import Node
from utilities.Pack import Pack


class IO:

    def __init__(self,machine_address, node_id):
        self.machine_address = machine_address
        #self.server_port = server_port
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

    #!Bloqueante--Redefinir!
    def connect_node(self, port = None):
        if port == None:
            print("No port provided!")
            return
        # Nodo como cliente------

        x =0
        while True:
            try:
                socket_as_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                socket_as_client.connect(("localhost",port ))
                t2 = threading.Thread(target=self.receive, args=(socket_as_client,))
                t2.start()

                x = x+1
                #Agregar la nueva conexion sin id
                self.clients.append([socket_as_client,"Null"])
                #Pedir el id al socket que acaba de conectarse
                self.request_id(socket_as_client)
                #print(f"Connected to {socket_as_client}")
                print(f"Client: {len(self.clients)}")
                print(f"x: {x}")
                break
            except:
                pass

    def connections_as_server(self):
        x = 0
        while True:
            x = x+1
            #Aceptar una conexion y asignarle un hilo
            client_socket, address = self.socket_as_server.accept()
            t1 = threading.Thread(target=self.receive,args=(client_socket,))
            t1.start()
            self.clients.append([client_socket,""])
            print(f"Server: {len(self.clients)}")
            print(f"y: {x}")
            #print(f"Connection from: {address}")

            #Pedir a la nueva conexion su identificacion
            self.request_id(client_socket)

    #Desconectar un nodo dado su id
    def disconnect_node(self,node_id):
        for client in self.clients:
            if client[1]==node_id:
                client[0].close()
                self.clients.remove(client)
                print("Disconnect")
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
                        if self.clients.__contains__(client):
                            self.clients.remove(client)
                            print("Deleted")

                        return

            except OSError:
                print("-------Not a socket!-------")
                break

    #Enviar un mensaje previamente empaquetado a traves del socket especificado
    def send(self,socket,message):
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
            print("grafo recibido")
        elif header == self.HEADERS[8]:
            self.replicate(data)

    #Asignarle un identificador a un socket
    def assign_id(self,socket,id):
        #Si la conexion ya existia, eliminar la nueva conexion
        for client in self.clients:
            if client[1]==id:
                for client1 in self.clients:
                    if client1[0]== socket:
                        self.clients.remove(client1)
                        return
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
        current_node = path.pop()
        if len(path) >= 1:
            next_node = path[len(path)-1]
        else:
            next_node = None
        data.set_path(path)
        #print("------------------------------------")
        #print(f"Path {path}")
        #print(f"current {current_node}")
        #print(f"next {next_node}")
        #print("------------------------------------")

        #si llegamos al destino mostramos los datos
        if len(path)==0 and current_node == self.machine_id:
            print(data.get_data())
        #si no es el destino mostramos el error
        elif len(path)==0 and next_node != self.machine_id:
            print("Error de direccionamiento")
        #si aun no hemos llegado, continuamos replicando el mensaje
        else:
            for client in self.clients:
                if client[1] == next_node:
                    self.send(client[0], self.fit_data(8, data))
                    #print("retransmiting...")

    def reach_point(self, target, message):
        path = self.graph.path_A_B(self.machine_id,target)
        #quitar el primer nodo, que es en el que se comienza la busqueda
        path.reverse()
        #path.pop()
        #print(path)
        pack = Pack(path,self.HEADERS[8],message)
        #print("reach...")
        self.replicate(pack)


    #consola de comandos
    def command(self):
        while True:
            com = input(">")
            if com == "broadcast":
                print(self.clients)
                com = input(">>")
                for i in range(len(self.clients)):
                    self.send(self.clients[i][0],self.fit_data(2,com))

            elif com == "update":
                self.update_MPR()

            elif com == "send":
                target = input("target>>")
                message = input("message>>")
                self.reach_point(target,message)

            elif com == "conns":
                print(len(self.clients))
                for client in self.clients:
                    print(client[1])

            elif com == "hello":
                names = ["N1","N2","N3","N4","N5","N6"]
                for i in range(20):
                    for name in names:
                        self.reach_point(name, f"hello {i} from {self.machine_id}")




