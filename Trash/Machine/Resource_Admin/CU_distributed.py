
class CU_distributed:
    def __init__(self,DS,ALU):
        #Registos
        self.ax = [0]
        self.bx = [0]
        self.cx= [0]
        self.dx = [0]
        self.sp = [0]

        self.ALU = ALU
        self.DS = DS

    #Instrucciones assembler
    def LOAD(self, rx , address):
        rx[0] =  self.ram.memory[address]

    def SAVE(self,rx, address):
        self.DS.save(rx,address)

    def ADD(self,rx,sx):
        rx[0]= self.ALU.add(rx[0],sx[0])

    def DEC(self,rx,sx):
        rx[0]=self.ALU.substract(rx[0],sx[0])

    def MUL(self,rx,sx):
        rx[0]=self.ALU.multiply(rx[0],sx[0])

    def DIV(self,rx,sx):
        rx[0]=self.ALU.divide(rx[0],sx[0])

    def MOV(self,rx,int):
        rx[0]=int

    def LESS(self,rx,sx,label):
        if self.ALU.NOT(self.ALU.substract(rx[0],sx[0])<0):
            self.GOTO(label)

    def LEQ(self,rx,sx,label):
        if self.ALU.NOT(self.ALU.substract(rx[0],sx[0])<=0):
            self.GOTO(label)


    def GREATER(self,rx,sx,label):
        if self.ALU.NOT(  self.ALU.substract(rx[0],sx[0])>0):
            self.GOTO(label)

    def GEQ(self,rx,sx,label):
        if self.ALU.NOT(  self.ALU.substract(rx[0],sx[0])>=0):
            self.GOTO(label)

    def EQ(self,rx,sx,label):
        if self.ALU.NOT(self.ALU.substract(rx[0],sx[0])==0):
            self.GOTO(label)

    def END(self,sp = 0, address = 0):
        return "end"

    def GOTO(self,address, rx=0):
        self.sp[0]=address

    def AND(self, rx, sx, label):
        if self.ALU.AND(rx[0], sx[0]):
            self.GOTO(label)

    def OR(self, rx, sx, label):
        if self.ALU.OR(rx[0], sx[0]):
            self.GOTO(label)

    def execution(self):
        #Programa en secuencia de instrucciones
        buffer=[
                [self.MOV,self.ax,1],
                [self.MOV,self.bx,2],
                [self.ADD,self.ax,self.bx],
                [self.SAVE,self.ax,0],
                [self.GEQ, self.ax, self.bx,8],
                #[self.GOTO, 8, None],
                [self.MOV, self.ax, 1],
                [self.MOV, self.bx, 2],
                [self.ADD, self.ax, self.bx],
                [self.MOV, self.ax, 10],
                [self.SAVE, self.ax, 0],
                [self.END,0,0]
            ]
        end = True
        #Ejecucion del programa.br
        while end != "end":
            #Si el programa.br tiene sentencias de control, salta a la posicion que indica la etiqueta en la tercera posicion
            if buffer[self.sp[0]][0] == self.LESS or \
                    buffer[self.sp[0]][0] == self.LEQ or \
                    buffer[self.sp[0]][0] == self.GREATER or \
                    buffer[self.sp[0]][0] == self.GEQ or \
                    buffer[self.sp[0]][0] == self.EQ or \
                    buffer[self.sp[0]][0] == self.AND or \
                    buffer[self.sp[0]][0] == self.OR:
                end = buffer[self.sp[0]][0](buffer[self.sp[0]][1], buffer[self.sp[0]][2], buffer[self.sp[0]][3])
            else:
                #Si no es una sentencia de control, solo ejecuta la instruccion
                end=buffer[self.sp[0]][0](buffer[self.sp[0]][1],buffer[self.sp[0]][2])
            self.sp[0]=self.sp[0]+1
            #print(self.sp[0])


        print(self.ram.memory[0])


#CU().execution()
