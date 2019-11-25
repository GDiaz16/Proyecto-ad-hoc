import copy
import random
import socket
import threading
import pickle
import time

from utilities.Graph import Graph
from utilities.Node import Node
from utilities.Pack import Pack


class IO:

    def __init__(self,machine_address, node_id,screen=None,DS=None):
        self.DS = DS
        self.DS.IO = self

        self.machine_address = machine_address
        self.machine_id = node_id
        self.screen = screen
        # Nodo como servidor-----
        self.socket_as_server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.socket_as_server.bind(("localhost",self.machine_address))
        self.socket_as_server.listen(10)

        self.clients=[] #[socket, id]
        self.connected = False
        self.names = ["N1", "N2", "N3", "N4", "N5", "N6"]


        self.tabla = []
        self.graph = None
        self.message_queues={"N1":[],"N2":[],"N3":[],"N4":[],"N5":[],"N6":[]}
        self.checks = {"N1":100,"N2":100,"N3":100,"N4":100,"N5":100,"N6":100}
        self.current_messages = {"N1":100,"N2":100,"N3":100,"N4":100,"N5":100,"N6":100}


        #Encabezado para cada tipo de mensaje
        self.HEADERS = ["<MPR?>--------------",#0
                        "<MPR=>--------------",#1
                        "<MSG=>--------------",#2
                        "<ID?>---------------",#3
                        "<ID=>---------------",#4
                        "<CONNECT-TO=>-------",#5
                        "<DISCONNECT-OF=>----",#6
                        "<U-GRAFO=>----------",#7
                        "<REP=>--------------",#8
                        "<IMAGE=>------------",#9
                        "<STREAM=>-----------",#10
                        "<MEMORY?>-----------",#11
                        "<MEMORY=>-----------",#12
                        "<SAVE>--------------",#13
                        "<OK>----------------" #14
                        ]

        self.processes()

    def processes(self):
        t1 = threading.Thread(target=self.connections_as_server)
        t2 = threading.Thread(target=self.set_connections)
        t3 = threading.Thread(target=self.command)
        t4 = threading.Thread(target=self.queue)
        t1.start()
        t2.start()
        t3.start()
        t4.start()


    def set_connections(self):
        while True:
            if self.graph != None:
                for node in self.graph.get_connections_by_nodes():
                    if node[0].get_id() == self.machine_id:
                        t = threading.Thread(target=self.connect_node,args=(node[1].get_id(), node[1].get_machine_address(),))
                        t.start()
                break

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

    #Recibir datos de un socket especifico
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

    #Enviar un mensaje previamente empaquetado a traves del socket especificado
    def send(self,socket,message):
        try:
            socket.send(message)
        except ConnectionResetError:
            self.disconnect(socket)

    #Instrucciones a realizar dependiendo del tipo de mensaje
    def protocols(self, header,data,socket=socket.socket(), origin = ""):
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
        elif header == self.HEADERS[11]:
            print("Memory------------------")
            ram = self.DS.get_ram()
            #self.broadcast(12,ram)

            msg = self.fit_data(12, ram)
            header2 = msg[0:20]
            pack = msg[20:]
            self.reach_point(origin, pack, header2)

        elif header == self.HEADERS[12]:
            self.DS.set_ram(data)
            print("get memory--")
        elif header == self.HEADERS[13]:
            self.DS.save_local(data["data"],data["pos"])
        elif header == self.HEADERS[14]:
            self.checks[origin] = data
            #print("ok")

    #Funciones de identificacion------------------------------------>
    #Asignarle un identificador a un socket
    def assign_id(self,socket,id):
        for client in self.clients:
            if client[0] == socket:
                client[1]=id
                break

    #Pedir el id de un socket
    def request_id(self,socket):
        self.send(socket,self.fit_data(3,""))

    #Enviar el id del socket
    def send_id(self,socket):
        self.send(socket,self.fit_data(4,self.machine_id))

    #Pedir id local
    def get_id(self):
        return self.machine_id

    #empaquetar datos para enviarlos a traves del socket
    def fit_data(self, header, data):
        msg = self.HEADERS[header].encode('utf-8')+pickle.dumps(data)
        return msg

    #Replicar un mensaje hasta que llegue a su destinatario
    def replicate(self, pack):
        path = pack.get_path()
        current_node = path.pop()
        #si el camino es mayor o igual a 1 seguimos buscando
        if len(path) >= 1:
            next_node = path[len(path)-1]
        else:
            next_node = None
        pack.set_path(path)
        #si llegamos al destino ejecutamos la instruccion del header
        if len(path) == 0 and current_node == self.machine_id:
            #si se recibe el mismo mensaje varias veces, usarlo solo una vez y
            #esperar a que cambie para volver a procesarlo
            if pack.check != self.current_messages[pack.get_origin()]:
                #Retornar la confirmacion de que se recibio el mensaje
                #siempre que no sea un OK ya que se vuelve recursivo
                if pack.get_header().decode('utf-8') != self.HEADERS[14]:
                    self.confirm(pack)

                self.protocols(pack.get_header(),pack.get_data(),origin=pack.get_origin())
                self.current_messages[pack.get_origin()] = pack.check
                if pack.get_origin() == self.machine_id:
                    self.checks[pack.get_origin()] = pack.check
                    return


        #si no es el destino mostramos el error
        elif len(path)==0 and next_node != self.machine_id:
            print("Error de direccionamiento")
        #si aun no hemos llegado, continuamos replicando el mensaje
        else:
            for client in self.clients:
                if client[1] == next_node:
                    self.send(client[0], self.fit_data(8, pack))
                    break
                    #print("retransmiting...")

    #Alcanzar un nodo dentro de la red y enviarle un mensaje
    #----------------Parametros en formato de bytes
    def reach_point(self, target, message, instruction):
        path = self.graph.path_A_B(self.machine_id,target)
        #dar la vuelta a la lista
        path.reverse()
        check = random.uniform(0,10)
        #-----------------instruction y message en formato de bytes
        pack = Pack(path, instruction, message, check)
        #Poner el mensaje en la cola de envios
        self.message_queues[target].append(pack)

    # def queue(self):
    #     while True:
    #         #Enviar todos los mensajes que esten en la cola
    #         while len(self.message_queue)>0:
    #             pack = self.message_queue.pop(0)
    #             #si es un ok, enviarlo solo una vez
    #             if pack.get_header().decode('utf-8') == self.HEADERS[14]:
    #                 self.replicate(pack)
    #             #si no, enviarlo hasta que sea recibido
    #             else:
    #                 while self.check != pack.check:
    #                     #crear copia para evitar errores
    #                     aux = copy.deepcopy(pack)
    #                     self.replicate(aux)
    #                     time.sleep(0.001)
    #         time.sleep(0.05)

    def queue(self):
        while True:
            #Enviar todos los mensajes que esten en las colas
            for name in self.names:
                if len(self.message_queues[name]) > 0:
                    queue = self.message_queues[name]
                    pack = queue[0]
                    #si es un ok, enviarlo solo una vez
                    if pack.get_header().decode('utf-8') == self.HEADERS[14]:
                        self.replicate(pack)
                    #Si se confirma el envio se elimina de la cola
                    elif self.checks[name] == pack.check:
                        queue.pop(0)
                    #si no, enviarlo hasta que sea recibido
                    elif self.checks[name] != pack.check:
                        #crear copia para evitar errores
                        aux = copy.deepcopy(pack)
                        self.replicate(aux)
                        time.sleep(0.001)
            time.sleep(0.05)
            #
            # #Enviar todos los mensajes que esten en la cola
            # while len(self.message_queue)>0:
            #     pack = self.message_queue.pop(0)
            #     #si es un ok, enviarlo solo una vez
            #     if pack.get_header().decode('utf-8') == self.HEADERS[14]:
            #         self.replicate(pack)
            #     #si no, enviarlo hasta que sea recibido
            #     else:
            #         while self.check != pack.check:
            #             #crear copia para evitar errores
            #             aux = copy.deepcopy(pack)
            #             self.replicate(aux)
            #             time.sleep(0.001)
            # time.sleep(0.05)

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

    #Parametros sin formato
    def broadcast(self,header,data):
        names = ["N1", "N2", "N3", "N4", "N5", "N6"]
        msg = self.fit_data(header, data)
        header = msg[0:20]
        data = msg[20:]
        for name in names:
            if name != self.machine_id:
                self.reach_point(name, data, header)

    def confirm(self,data):
        msg = self.fit_data(14, data.check)
        header = msg[0:20]
        check = msg[20:]
        self.reach_point(data.get_origin(), check, header)

    #consola de comandos
    def command(self):
        while True:
            com = input(">")
            if com == "broadcast":
                com = input(">>")
                for i in range(len(self.clients)):
                    self.send(self.clients[i][0],self.fit_data(2,com))

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
                for i in range(20):
                    self.broadcast(2, f"hello {i} from {self.machine_id}")
                    # for name in names:
                    #     msg = self.fit_data(2, f"hello {i} from {self.machine_id}")
                    #     header = msg[0:20]
                    #     data = msg[20:]
                    #     self.reach_point(name, data, header)
                    #

            elif com == "RAM":
                self.broadcast(11,"")

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

            elif com == "memory":
                print(self.DS.memory)

            elif com == "test":
                target = input("target>>")
                message = input("message>>")

                for i in range(50):
                    msg = self.fit_data(2, message+f"   {i}")
                    header = msg[0:20]
                    data = msg[20:]
                    self.reach_point(target, data, header)

            elif com == "cola":
                pass
                # for queue in self.message_queues:
                #     for msg in queue:
                #         print(f"cola: {msg.get_header()}")
                # if len(self.message_queue) == 0:
                #     print("Empty")



