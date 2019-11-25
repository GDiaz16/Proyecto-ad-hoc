import math

from Machine.Resource_Admin.CU_distributed import CU_distributed
from Machine.Resource_Admin.RAM_distributed import RAM_distributed


class Distributed_System:
    def __init__(self,RAM,CU,ALU,device_id):
        self.RAM = RAM
        self.CU = CU
        self.ALU = ALU
        self.RAM_distributed = RAM_distributed()
        self.CU_distributed = CU_distributed(self,self.ALU)
        self.device_id = device_id
        self.IO = None
        self.memory = {}

    def get_ram(self):
        self.pos_ini = 10
        self.pos_fin = 500
        ram = {"pos_ini":self.pos_ini,"pos_fin":self.pos_fin,"device":self.device_id}
        return ram

    def set_ram(self,ram):
        self.memory[ram["device"]] = [ram["pos_ini"], ram["pos_fin"]]


    def save(self, rx, address):
        n = address % 6 + 1
        device = "N"+ str(n)
        pos = math.ceil(address/6)
        message = {"pos":pos,"data":rx}

        #Editar para enviar-----!
        msg = self.IO.fit_data(13,message)
        header = msg[0:20]
        data = msg[20:]
        self.IO.reach_point(device, data, header)

    def save_local(self,rx,address):
        self.CU.save(rx,self.pos_fin + address)


