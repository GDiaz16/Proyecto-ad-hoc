from Test.Node import Node


class Connection:

    def __init__(self, device1, device2):
        self.device1 = device1
        self.device2 = device2
        self.node1 = device1.node
        self.node2 = device2.node
        self.connection_graphic = ""
        self.buffer1 = []
        self.buffer2 = []
        self.connect()

    def connect(self):
        #1 --> 2 buffer1
        self.device1.buffers_output[self.device2.name] = self.buffer1
        #1 <-- 2 buffer2
        self.device1.buffers_input[self.device2.name] = self.buffer2
        #2 --> 1 buffer2
        self.device2.buffers_output[self.device1.name] = self.buffer2
        #2 <-- 1 buffer1
        self.device2.buffers_input[self.device1.name] = self.buffer1


