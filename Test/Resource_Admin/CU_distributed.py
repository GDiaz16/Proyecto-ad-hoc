import copy


class CU_distributed:
    def __init__(self, DS, ALU):
        # Registos
        self.ax = [0]
        self.bx = [0]
        self.cx = [0]
        self.dx = [0]
        self.sp = [0]
        self.ALU = ALU
        self.DS = DS

    # Instrucciones assembler
    def LOAD(self, rx, address):
        rx[0] = self.DS.load(address)[0]

    def SAVE(self, int, address):
        self.DS.save(int, address)

    def ADD(self, rx, sx):
        rx[0] = self.ALU.add(rx[0], sx[0])

    def DEC(self, rx, sx):
        rx[0] = self.ALU.substract(rx[0], sx[0])

    def MUL(self, rx, sx):
        rx[0] = self.ALU.multiply(rx[0], sx[0])

    def DIV(self, rx, sx):
        rx[0] = self.ALU.divide(rx[0], sx[0])

    def MOV(self, rx, sx):
        register = [0]
        address = 0
        if type(rx) == type(register):
            #registro <-- registro
            if type(sx) == type(register):
                rx[0] = sx[0]
            #registro <-- entero
            elif type(sx) == type(address):
                rx[0] = sx
        elif type(rx) == type(address):
            # memoria <-- registro
            if type(sx) == type(register):
                self.SAVE(sx[0],rx)
            # memoria <-- entero
            elif type(sx) == type(address):
                self.SAVE(sx,rx)

    def LESS(self, rx, sx, label):
        if self.ALU.NOT(self.ALU.substract(rx[0], sx[0]) < 0):
            self.GOTO(label)

    def LEQ(self, rx, sx, label):
        if self.ALU.NOT(self.ALU.substract(sx[0], rx[0]) <= 0):
            self.GOTO(label)

    def GREATER(self, rx, sx, label):
        if self.ALU.NOT(self.ALU.substract(rx[0], sx[0]) > 0):
            self.GOTO(label)

    def GEQ(self, rx, sx, label):
        if self.ALU.NOT(self.ALU.substract(rx[0], sx[0]) >= 0):
            self.GOTO(label)

    def EQ(self, rx, sx, label):
        if self.ALU.NOT(self.ALU.substract(rx[0], sx[0]) == 0):
            self.GOTO(label)

    def END(self, sp=0, address=0):
        return "end"

    def GOTO(self, label, rx=0):
        for i in range(len(self.buffer)):
            if self.buffer[i][1] == label:
                self.sp[0] = i

    def AND(self, rx, sx, label):
        if self.ALU.AND(rx[0], sx[0]):
            self.GOTO(label)

    def OR(self, rx, sx, label):
        if self.ALU.OR(rx[0], sx[0]):
            self.GOTO(label)

    def PRINT(self, rx, sx=0):
        print(f"{self.DS.device.name} {rx[0]}")

    def INPUT(self, rx, sx=0):
        rx[0] = input("RX-->")

    def SLICE(self, rx, sx, label, buffer):
        thread = buffer[rx : sx + 1]
        self.DS.thread(thread)
        self.GOTO(label)

    def translate(self, buffer):
        buffer_copy = copy.deepcopy(buffer)
        for instruction in buffer_copy:
            if instruction[0] == "LOAD":
                instruction[0] = self.LOAD
            elif instruction[0] == "SAVE":
                instruction[0] = self.SAVE
            elif instruction[0] == "ADD":
                instruction[0] = self.ADD
            elif instruction[0] == "DEC":
                instruction[0] = self.DEC
            elif instruction[0] == "MUL":
                instruction[0] = self.MUL
            elif instruction[0] == "DIV":
                instruction[0] = self.DIV
            elif instruction[0] == "MOV":
                instruction[0] = self.MOV
            elif instruction[0] == "LESS":
                instruction[0] = self.LESS
            elif instruction[0] == "LEQ":
                instruction[0] = self.LEQ
            elif instruction[0] == "GREATER":
                instruction[0] = self.GREATER
            elif instruction[0] == "GEQ":
                instruction[0] = self.GEQ
            elif instruction[0] == "EQ":
                instruction[0] = self.EQ
            elif instruction[0] == "END":
                instruction[0] = self.END
            elif instruction[0] == "GOTO":
                instruction[0] = self.GOTO
            elif instruction[0] == "AND":
                instruction[0] = self.AND
            elif instruction[0] == "OR":
                instruction[0] = self.OR
            elif instruction[0] == "PRINT":
                instruction[0] = self.PRINT
            elif instruction[0] == "INPUT":
                instruction[0] = self.INPUT
            elif instruction[0] == "SLICE":
                instruction[0] = self.SLICE
        for instruction in buffer_copy:
            for i in range(1, 3):
                if instruction[i] == "ax":
                    instruction[i] = self.ax
                elif instruction[i] == "bx":
                    instruction[i] = self.bx
                elif instruction[i] == "cx":
                    instruction[i] = self.cx
                elif instruction[i] == "dx":
                    instruction[i] = self.dx
        return buffer_copy

    def execute(self, buffer_org):
        #Buffer en formato de instrucciones
        self.buffer = self.translate(buffer_org)
        buffer = self.buffer
        end = True
        # Ejecucion del programa.br
        try:
            while end != "end":
                # Si el programa.br tiene sentencias de control, salta a la posicion que indica la etiqueta en la tercera posicion
                if buffer[self.sp[0]][0] == self.LESS or \
                        buffer[self.sp[0]][0] == self.LEQ or \
                        buffer[self.sp[0]][0] == self.GREATER or \
                        buffer[self.sp[0]][0] == self.GEQ or \
                        buffer[self.sp[0]][0] == self.EQ or \
                        buffer[self.sp[0]][0] == self.AND or \
                        buffer[self.sp[0]][0] == self.OR:

                    instruction = buffer[self.sp[0]][0]
                    rx = buffer[self.sp[0]][1]
                    sx = buffer[self.sp[0]][2]
                    label = buffer[self.sp[0]][3]
                    end = instruction(rx, sx, label)
                # instruccion especial para threading
                elif buffer[self.sp[0]][0] == self.SLICE:
                    instruction = buffer[self.sp[0]][0]
                    rx = buffer[self.sp[0]][1]
                    sx = buffer[self.sp[0]][2]
                    label = buffer[self.sp[0]][3]
                    end = instruction(rx, sx, label, buffer_org)
                elif buffer[self.sp[0]][0] == "LABEL":
                    pass
                else:
                    # Si no es una sentencia de control, solo ejecuta la instruccion
                    instruction = buffer[self.sp[0]][0]
                    rx = buffer[self.sp[0]][1]
                    sx = buffer[self.sp[0]][2]
                    end = instruction(rx, sx)
                # Hacer correr el puntero una posicion hacia adelante
                self.sp[0] = self.sp[0] + 1
        except:
            print(f"Error de ejecucion en {self.DS.device.name}")

# CU().execution()

