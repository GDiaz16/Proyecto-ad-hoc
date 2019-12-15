from Test.Device import Device
from Test.Connection import Connection
from Test.Utilities.Graph import Graph
from Test.Utilities.Node import Node
import threading

class Network:

    def __init__(self, graph):
        self.graph = graph
        self.device1 = Device("D1", self.graph)
        self.device2 = Device("D2", self.graph)
        self.device3 = Device("D3", self.graph)
        self.device4 = Device("D4", self.graph)
        self.device5 = Device("D5", self.graph)
        self.device6 = Device("D6", self.graph)

        self.devs ={"D1":self.device1, "D2":self.device2, "D3":self.device3,
                    "D4":self.device4, "D5":self.device5, "D6":self.device6}
        self.processes()
        self.my_graph()
        self.start()

    def start(self):
        self.devs["D1"].command(com="ram")


    def my_graph(self):
        c1 = Connection(self.device1,self.device2)
        c2 = Connection(self.device1, self.device3)
        c3 = Connection(self.device1, self.device4)
        c4 = Connection(self.device3, self.device5)
        c5 = Connection(self.device3, self.device6)
        c6 = Connection(self.device6, self.device4)
        c7 = Connection(self.device5, self.device4)

        self.graph.add_node(self.device1.node)
        self.graph.add_node(self.device2.node)
        self.graph.add_node(self.device3.node)
        self.graph.add_node(self.device4.node)
        self.graph.add_node(self.device5.node)
        self.graph.add_node(self.device6.node)

        self.graph.add_connection(c1)
        self.graph.add_connection(c2)
        self.graph.add_connection(c3)
        self.graph.add_connection(c4)
        self.graph.add_connection(c5)
        self.graph.add_connection(c6)
        self.graph.add_connection(c7)

    def processes(self):
        t1 = threading.Thread(target = self.commands)
        t1.start()

    def commands(self):
        comms = ["ram","memory","execute"]
        while True:
            dev = input("Device>")
            com = input("Command>")

            if com == "send":
                target = input("Target>>")
                message = input("Message>>")
                self.devs[dev].command(com = com, target = target, message = message)

            elif comms.__contains__(com):
                self.devs[dev].command(com = com)


