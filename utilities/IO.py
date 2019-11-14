import socket
import threading
import pickle

from utilities.Graph import Graph
from utilities.Node import Node
from utilities.Pack import Pack


class IO:

    def __init__(self,machine_address, node_id,screen=None):
        self.machine_address = machine_address
        self.machine_id = node_id
        self.screen = screen
        # Nodo como servidor-----
        self.socket_as_server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.socket_as_server.bind(("localhost",self.machine_address))
        self.socket_as_server.listen(10)

        self.clients=[] #[socket, id]
        self.connected = False

        self.tabla = []
        self.graph = None


        #Encabezado para cada tipo de mensaje
        self.HEADERS = ["<MPR?>--------------",
                        "<MPR=>--------------",
                        "<MSG=>--------------",
                        "<ID?>---------------",
                        "<ID=>---------------",
                        "<CONNECT-TO=>-------",
                        "<DISCONNECT-OF=>----",
                        "<U-GRAFO=>----------",
                        "<REP=>--------------",
                        "<IMAGE=>------------",
                        "<STREAM=>-----------"]

        self.processes()

    def set_connections(self):
        while True:
            if self.graph != None:
                for node in self.graph.get_connections_by_nodes():
                    if node[0].get_id() == self.machine_id:
                        t = threading.Thread(target=self.connect_node,args=(node[1].get_id(), node[1].get_machine_address(),))
                        t.start()
                break


    #!Bloqueante--Redefinir!
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
                self.clients.append([socket_as_client,node_id])
                print(len(self.clients))
                print(f"Connected to: {node_id}")
                connected = True
            except:
                pass

    def connections_as_server(self):
        while True:
            #Aceptar una conexion y asignarle un hilo
            client_socket, address = self.socket_as_server.accept()
            t1 = threading.Thread(target=self.receive,args=(client_socket,))
            t1.start()
            self.clients.append([client_socket,""])
            print(f"Server: {len(self.clients)}")
            #Pedir a la nueva conexion su identificacion
            self.request_id(client_socket)

    #Desconectar un nodo dado su id
    # def disconnect_node(self,node_id):
    #     for client in self.clients:
    #         if client[1]==node_id:
    #             client[0].close()
    #             self.clients.remove(client)
    #             print("Disconnect")
    #             break

    # def update_MPR(self):
    #     for client in self.clients:
    #         #Pedir la MPR a los nodos hijo
    #         self.send(client[0],self.fit_data(0,""))

    #Procesos corriendo continuamente
    def processes(self):
        t1 = threading.Thread(target=self.connections_as_server)
        t2 = threading.Thread(target=self.set_connections)
        t3 = threading.Thread(target=self.command)
        t1.start()
        t2.start()
        t3.start()

    def receive(self, socket_c):
        while True:
            try:
                data = b''
                socket_c.setblocking(True)
                #recibir datos mientras sigan llegando al buffer
                while True:
                    packet = socket_c.recv(1024)
                    data = data+packet
                    socket_c.setblocking(False)
            #Manejar el error en caso de desconexion o cierre de la conexion
            except (ConnectionResetError,  ConnectionAbortedError, EOFError) :
                    self.disconnect(socket_c)
                    return

            except BlockingIOError:
                if data != '':
                    # Separar el header de los datos
                    header = data[0:20]
                    data = data[20:]
                    self.protocols(header, data, socket_c)
            # except OSError:
            #     print("-------Not a socket!-------")
            #     break

    def disconnect(self,socket):
        for client in self.clients:
            if client[0] == socket:
                print(f"Se ha cortado la comunicacion con {client[1]}")
                self.clients.remove(client)
                # for node in self.graph.get_node_list():
                #     if node.get_id()==client[1]:
                #         t = threading.Thread(target=self.connect_node, args=(node.get_id(), node.get_machine_address(),))
                #         t.start()
                #         break
                for conn in self.graph.get_connections_by_nodes():
                    if conn[0].get_id() == self.machine_id and conn[1].get_id() == client[1]:
                        t = threading.Thread(target=self.connect_node,
                                             args=(conn[1].get_id(), conn[1].get_machine_address(),))
                        t.start()
                break

    #Enviar un mensaje previamente empaquetado a traves del socket especificado
    def send(self,socket,message):
        try:
            socket.send(message)
        except ConnectionResetError:
            self.disconnect(socket)

    #Instrucciones a realizar dependiendo del tipo de mensaje
    def protocols(self, header,data,socket=socket.socket()):
        header = header.decode('utf-8')
        data = pickle.loads(data)
        if header == self.HEADERS[0]:
            pass#self.send_MPR(socket)
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
        # elif header == self.HEADERS[6]:
        #     self.disconnect_node(data)
        elif header == self.HEADERS[7]:
            self.graph = data
            print("grafo recibido")
        elif header == self.HEADERS[8]:
            self.replicate(data)
        elif header == self.HEADERS[9]:
            self.screen.Show_Image(data)
        elif header == self.HEADERS[10]:
            self.screen.draw_stream(data)

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

    #empaquetar datos para enviarlos a traves del socket
    def fit_data(self, header, data):
        msg = self.HEADERS[header].encode('utf-8')+pickle.dumps(data)
        return msg

    #Replicar un mensaje hasta que llegue a su destinatario
    def replicate(self, data):
        path = data.get_path()
        current_node = path.pop()
        #si el camino es mayor o igual a 1 seguimos buscando
        if len(path) >= 1:
            next_node = path[len(path)-1]
        else:
            next_node = None
        data.set_path(path)
        #si llegamos al destino ejecutamos la instruccion del header
        if len(path)==0 and current_node == self.machine_id:
            self.protocols(data.get_header(),data.get_data())
        #si no es el destino mostramos el error
        elif len(path)==0 and next_node != self.machine_id:
            print("Error de direccionamiento")
        #si aun no hemos llegado, continuamos replicando el mensaje
        else:
            for client in self.clients:
                if client[1] == next_node:
                    self.send(client[0], self.fit_data(8, data))
                    #print("retransmiting...")

    #Alcanzar un nodo dentro de la red y enviarle un mensaje
    def reach_point(self, target, message, instruction):
        path = self.graph.path_A_B(self.machine_id,target)
        #dar la vuelta a la lista
        path.reverse()
        pack = Pack(path, instruction, message)
        self.replicate(pack)

    #Hacer streaming de figuras geometricas
    def stream(self,graphics_list):
        names = ["N1","N2", "N3", "N4", "N5", "N6"]
        for name in names:
            if name != self.machine_id:
                # arreglar los datos para que se envien codificados
                msg = self.fit_data(10, graphics_list)
                header = msg[0:20]
                data = msg[20:]
                self.reach_point(name, data, header)

    #consola de comandos
    def command(self):
        while True:
            com = input(">")
            if com == "broadcast":
                com = input(">>")
                for i in range(len(self.clients)):
                    self.send(self.clients[i][0],self.fit_data(2,com))

            # elif com == "update":
            #     self.update_MPR()

            elif com == "send":
                target = input("target>>")
                message = input("message>>")

                msg = self.fit_data(2, message)
                header = msg[0:20]
                data = msg[20:]
                self.reach_point(target,data,header)

            elif com == "conns":
                print(len(self.clients))
                for client in self.clients:
                    print(client[1])

            elif com == "hello":
                names = ["N1","N2","N3","N4","N5","N6"]
                for i in range(20):
                    for name in names:
                        msg = self.fit_data(2, f"hello {i} from {self.machine_id}")
                        header = msg[0:20]
                        data = msg[20:]
                        self.reach_point(name, data, header)

            elif com == "mosaico":
                names = ["N1","N2","N3","N4","N5","N6"]
                parts = self.screen.Split_Image("")
                i=0
                for name in names:
                    #arreglar los datos para que se envien codificados
                    msg = self.fit_data(9,parts[i])
                    header = msg[0:20]
                    data = msg[20:]
                    self.reach_point(name, data,header)
                    i=i+1




