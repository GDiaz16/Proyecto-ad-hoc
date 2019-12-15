import threading
import time

from Compiler.compiler import compiler
from Test.ALU import ALU
from Test.CU import CU
from Test.RAM import RAM
from Test.Resource_Admin.Distributed_System import Distributed_System
from Test.Utilities.Node import Node
from Test.Utilities.Pack import Pack


class Device:

    def __init__(self, name, graph):
        self.name = name
        self.node = Node(self.name)
        self.buffers_output = {}
        self.buffers_input = {}
        self.stack = {}
        self.headers = ["message---->",  # 0
                        "replicate-->",  # 1
                        "stream----->",  # 2
                        "ram?------->",  # 3
                        "ram=------->",  # 4
                        "save------->",  # 5
                        "load(get)-->",  # 6
                        "load(send)->",  # 7
                        "thread----->"  # 8
                        ]
        self.graph = graph

        self.screen = None
        self.processes()
        self.RAM = RAM()
        self.ALU = ALU()
        self.CU = CU(self.RAM, self.ALU)
        self.Distributed_System = Distributed_System(self)
        self.compiler = compiler()

    def processes(self):
        t1 = threading.Thread(target=self.input)
        t1.start()

    def input(self):
        while True:
            for device in self.buffers_input.keys():
                if len(self.buffers_input[device]) > 0:
                    self.protocols(self.buffers_input[device].pop(0))
            time.sleep(0.01)

    def send(self, pack):
        self.buffers_output[pack.target].append(pack)

    def connect_to(self):
        pass

    def protocols(self, pack):
        header = pack.header
        data = pack.data
        target = pack.target
        origin = pack.origin
        check = pack.check

        if header == self.headers[0]:
            print("")
            print(self.name + ":  " + data)
        elif header == self.headers[1]:
            self.replicate(pack)
        elif header == self.headers[2]:
            if self.screen != None:
                self.screen.draw_stream(pack.data)
            else:
                print("Pantalla no asignada")
        elif header == self.headers[3]:
            self.stream(self.Distributed_System.get_ram(), 4)
        elif header == self.headers[4]:
            self.Distributed_System.set_ram(data)
        elif header == self.headers[5]:
            self.Distributed_System.save_local(data)
        elif header == self.headers[6]:
            rx = self.Distributed_System.load_local(data)
            pack1 = Pack(self.headers[7], rx, origin, check=check)
            self.reach_point(pack1)
        elif header == self.headers[7]:
            self.stack[check] = pack
        elif header == self.headers[8]:
            self.Distributed_System.execute(data)

    def command(self, **kwargs):
        if kwargs["com"] == "send":
            pack = Pack(header=self.headers[0], data=kwargs["message"], target=kwargs["target"])
            self.reach_point(pack)

        elif kwargs["com"] == "ram":
            self.stream("", 3)

        elif kwargs["com"] == "memory":
            print(self.Distributed_System.memory)
            print(self.RAM.memory)

        elif kwargs["com"] == "execute":
            buffer = self.compiler.compile()
            self.Distributed_System.execute(buffer)

    # Replicar un mensaje hasta que llegue a su destinatario
    def replicate(self, pack):
        path = pack.path
        sub_pack = pack.data

        # si llegamos al destino ejecutamos la instruccion del header
        if sub_pack.target == self.name:
            self.protocols(sub_pack)

        # si no es el destino mostramos el error
        elif len(path) == 0 and sub_pack.target != self.name:
            print("Error de direccionamiento")
        # si aun no hemos llegado, continuamos replicando el mensaje
        else:
            target = path.pop()
            pack1 = Pack(self.headers[1], sub_pack, target, path=path)

            # Poner el mensaje en la cola de envios
            self.send(pack1)

    # Alcanzar un nodo dentro de la red y enviarle un mensaje
    def reach_point(self, pack):
        path = self.graph.path_A_B(self.name, pack.target)
        # dar la vuelta a la lista
        path.reverse()
        target = path.pop()
        # Si es a un nodo diferente del propio
        if len(path) == 0 and target == self.name:
            self.protocols(pack)
        # De lo contrario procesarlo aqui mismo
        else:
            target = path.pop()
            pack1 = Pack(self.headers[1], pack, target, path=path)
            # Poner el mensaje en la cola de envios
            self.send(pack1)

    def stream(self, data, header):
        devs = self.graph.node_list
        for dev in devs:
            pack1 = Pack(self.headers[header], data, dev.name)
            self.reach_point(pack1)
