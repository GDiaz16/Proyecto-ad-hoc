class instruction:
    def __init__(self):
        self.pos = 0
        self.i1 = ""
        self.i2 = ""
        self.op = ""
        self.i3 = ""


    def __str__(self):
        if self.i1 == "PUSH" or self.i1 == "CALL" or self.i1 == "POP":
            inst = str(self.pos) + "\t: " + str(self.i1) + "  " + str(self.i2) + \
                   " " + str(self.op) + " " + str(self.i3)
            return inst

        inst = str(self.pos) + "\t: " + str(self.i1) + " = " + str(self.i2) +\
               " "+ str(self.op) + " "+ str(self.i3)
        return inst
