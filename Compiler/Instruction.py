from copy import copy


class instruction:
    def __init__(self):
        self.pos = 0
        self.label = ""
        self.i1 = ""
        self.i2 = ""
        self.op = ""
        self.i3 = "  "
        self.result = ""

        self.array1 = False
        self.array2 = False
        self.assembly = False

    def __str__(self):
        #PUSH t1
        #CALL t1
        #POP t1
        #LIST a
        #print a

        if self.assembly:
            inst = str(self.i1) + " " + str(self.i2) + " "  + str(self.i3)
            return inst

        special =["PUSH", "START", "CALL", "POP", "LIST", "print", "SLICE", "<fun>", "<EndFun>"]
        if self.i1 in special:
            inst = str(self.pos) + "\t: "+str(self.label)+"\t " + str(self.i1) + "  " + str(self.i2) + \
                   " " + str(self.op) + " " + str(self.i3)
            return inst

        # a[x] = b
        if self.array1:
            inst = str(self.pos) + "\t: "+str(self.label)+"\t " + str(self.i1) + "[" + str(self.i2) + \
                   "]" + " = " + str(self.i3)
            return inst

        # a = b[x]
        if self.array2:
            inst = str(self.pos) + "\t: "+str(self.label)+"\t " + str(self.i1) + " = " + str(self.i2) + \
                   "[" + str(self.i3) + "]"
            return inst

        # GOTO L1
        if self.i1 == "goto":
            inst = str(self.pos) + "\t: " + str(self.label) + "\t " + str(self.i1) + "  " + str(self.i2)
            return inst

        # if <tx> goto y
        # elif z goto w
        if self.i1 == "if" or self.i1 == "elif":
            inst = str(self.pos) + "\t: " + str(self.label) + "\t " + str(self.i1) + "  " + str(self.i2) \
                    + "  "+ str(self.op)+ "  "+ str(self.i3) #+ "  "+ str(self.i4)
            return inst

        # LABEL L1
        if self.i1 == "LABEL" :
            inst = str(self.pos) + "\t: " + str(self.label) + "\t " + str(self.i1) + "  " + str(self.i2) \
                   + "  " + str(self.op) + "  " + str(self.i3)  # + "  "+ str(self.i4)
            return inst

        # ifFalse x < y goto z
        # if self.i1 == "ifFalse" and self.op != "":
        #     inst = str(self.pos) + "\t: " + str(self.label) + "\t " + str(self.i1) + "  " + str(self.i2) \
        #             + "  "+ str(self.op)+"  "+ str(self.i3)+ "  "+ str(self.i4) + "  "+ str(self.i5)
        #     return inst

        # t1 = t2 + t3
        inst = str(self.pos) + "\t: " +str(self.label)+"\t "+ str(self.i1) + " = " + str(self.i2) +\
               " "+ str(self.op) + " "+ str(self.i3)
        return inst
