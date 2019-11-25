import threading
import time

from Test.Node import Node
from Test.Pack import Pack

class Device:
    def __init__(self, name, graph):
        self.name = name
        self.node = Node(self.name)
        self.buffers_output = {}
        self.buffers_input = {}
        self.headers = ["message",
                        "replicate"
                        ]
        self.graph = graph
        self.processes()

    def processes(self):
        t1 = threading.Thread(target = self.input)
        t1.start()

    def input(self):
        while True:
            for device in self.buffers_input.keys():
                if len(self.buffers_input[device]) > 0:
                    self.protocols(self.buffers_input[device].pop(0))
            time.sleep(0.05)



    def send(self, pack):
        self.buffers_output[pack.target].append(pack)

    def connect_to(self):
        pass

    def protocols(self, pack):
        header = pack.header
        data = pack.data
        target = pack.target
        origin = pack.origin
        if header == self.headers[0]:
            print("")
            print(self.name+":  "+data)

        elif header == self.headers[1]:
            self.replicate(pack)

    def command(self,**kwargs):
        if kwargs["com"] == "send":
            pack = Pack(header=self.headers[0],data=kwargs["message"],target=kwargs["target"])
            self.reach_point(pack)

    #Replicar un mensaje hasta que llegue a su destinatario
    def replicate(self, pack):
        path = pack.path
        sub_pack = pack.data

        #si llegamos al destino ejecutamos la instruccion del header
        if sub_pack.target == self.name:
            self.protocols(sub_pack)

        #si no es el destino mostramos el error
        elif len(path)==0 and sub_pack.target != self.name:
            print("Error de direccionamiento")
        #si aun no hemos llegado, continuamos replicando el mensaje
        else:
            target = path.pop()
            pack1 = Pack(self.headers[1], sub_pack, target, path = path)

            # Poner el mensaje en la cola de envios
            self.send(pack1)

    #Alcanzar un nodo dentro de la red y enviarle un mensaje
    def reach_point(self, pack):
        path = self.graph.path_A_B(self.name, pack.target)
        #dar la vuelta a la lista
        path.reverse()
        path.pop()
        target = path.pop()
        pack1 = Pack(self.headers[1], pack, target, path=path)
        #Poner el mensaje en la cola de envios
        self.send(pack1)
