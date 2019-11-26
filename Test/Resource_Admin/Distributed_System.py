import random
import threading
import time

import math

from Test.Utilities.Pack import Pack
from Test.Resource_Admin.CU_distributed import CU_distributed
from Trash.Machine.Resource_Admin.RAM_distributed import RAM_distributed


class Distributed_System:
    def __init__(self, device):
        self.RAM = device.RAM
        self.CU = device.CU
        self.ALU = device.ALU
        self.CU_distributed = CU_distributed(self, self.ALU)
        self.device_id = device.name
        self.device = device
        self.memory = {}
        self.threads = [False,False,False,False,False,False]

    #Obtener la memoria del dispositivo
    def get_ram(self):
        self.pos_ini = 10
        self.pos_fin = 500
        ram = {"pos_ini": self.pos_ini, "pos_fin": self.pos_fin, "device": self.device.name}
        return ram

    #Establecer la memoria del resto de dispositivos
    def set_ram(self, ram):
        self.memory[ram["device"]] = [ram["pos_ini"], ram["pos_fin"]]

    #Guardar datos en otros dispositivos
    def save(self, rx, address):
        #Buscar la posicion que se deduce de dividir la posicion original en seis
        n = address % 6 + 1
        target = "D" + str(n)
        pos = math.ceil(address / 6)
        register = {"pos": pos, "data": rx}
        pack = Pack(self.device.headers[5], register, target)
        self.device.reach_point(pack)

    #Pedir datos a otro dispositivo
    def load(self, address):
        #Buscar la posicion que se deduce de dividir la posicion original en seis
        n = address % 6 + 1
        target = "D" + str(n)
        pos = math.ceil(address / 6)
        pack = Pack(self.device.headers[6], pos, target, origin=self.device.name)
        self.device.reach_point(pack)
        #Esperar hasta que se reciba respuesta del valor que se pidio
        while True:
            try:
                pack1 = self.device.stack[pack.check]
                del self.device.stack[pack.check]
                return pack1.data
            except KeyError:
                pass
            time.sleep(0.01)

    #Guardar datos en el dispositivo
    def save_local(self, register):
        self.CU.SAVE(register["data"], self.pos_ini + register["pos"])

    #Leer datos en el dispositivo
    def load_local(self, address):
        rx = [0]
        self.CU.LOAD(rx, self.pos_ini + address)
        return rx
    #Ejecutar un codigo assembly
    def execute(self, buffer):
        t1 = threading.Thread(target=self.CU_distributed.execute, args=(buffer,))
        t1.start()

    def thread(self, buffer):
        #Escoger un dispositivo aleatoriamente
        flag = True
        r = -1
        while flag:
            r = random.randrange(1,7)
            flag = self.threads[r-1]
        #Si todos estan ocupados reiniciamos la cuenta
        if r == -1:
            for i in range(len(self.threads)):
                self.threads[i] = False
            #Y escogemos un dispositivo al azar
            r = random.randrange(1,7)
            self.threads[r - 1] = True
        target = "D" + str(r)
        pack = Pack(self.device.headers[8], buffer, target, origin=self.device.name)
        self.device.reach_point(pack)
