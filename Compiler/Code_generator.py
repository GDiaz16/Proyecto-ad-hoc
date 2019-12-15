from copy import copy

from Compiler.Instruction import instruction as Ins


class Code_generator:
    def __init__(self, instructions, symbols):
        self.instructions = instructions
        self.assembly = []
        self.symbols = symbols
        self.count_variables = 0
        self.global_variables()
        self.print_codes()
        self.translate()
        self.format()
        #self.print_codes()

    def print_codes(self):
        print(self.symbols)

        for ins in self.instructions:
            print(ins)
        print("\n")

    def translate(self):
        self.i = 0
        while self.i < len(self.instructions):
            self.transform(self.instructions[self.i], self.i)
            self.i = self.i + 1
        inst = Ins()
        inst.i1 = "END"
        inst.assembly = True
        self.instructions.append(inst)

    def format(self):
        for inst in self.instructions:
            self.assembly.append([inst.i1, inst.i2, inst.i3])
        #
        # for asse in self.assembly:
        #    print(asse)

    def global_variables(self):
        i = 0
        for key in self.symbols.keys():
            self.symbols[key] = i
            i = i + 1

    def transform(self, inst, pos):
        """
        -Verificar que i1 no sea instruccion especial
            i1 = [if, goto, LABEL, print, PUSH, CALL, POP, LIST]

        -Cambiar los <tx> por registros nx
        -Si la instruccion es numero op numero, enviar el resultado directo
        -Si es numero op [registro/var], hacer un [mov nx numero] antes, pero no hacer un mov despues de
            la operacion ya que no es necesario
        -Si es [registro/var] op numero, hacer un [mov nx numero] antes y otro despues de la operacion
        -Si es [registro/var] op [registro/var] se debe mover i2 al valor correspondiente i1 siempre que no
            sea el mismo
        -Si uno de los valores es una variable se debe anteponer la instruccion load
        -Hacer asignaciones de registros a variables
        -Si es un string se pasa a un registro, similar que con los numeros, pero no se procesa,
            la unidad de control procesa y guarda la cadena sin las comillas
        """
        # i1 = [if, goto, LABEL, print, PUSH, CALL, POP, LIST]++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        # print(f"i = {self.i}")
        # self.print_codes()
        inst.result = self.register(inst.i1)
        # En caso de tener un if
        if inst.i1 == "if":
            inst.assembly = True
            inst.i1 = "IF"
            inst.i2 = self.register(inst.i2)

        # En caso de tener un goto
        elif inst.i1 == "goto":
            inst.assembly = True
            inst.i1 = "GOTO"
            inst.i2 = inst.i2

        # En caso de tener un label
        elif inst.i1 == "LABEL":
            inst.assembly = True
            inst.i1 = "LABEL"
            inst.i2 = inst.i2

        # En caso de tener un SLICE
        elif inst.i1 == "SLICE":
            inst.assembly = True

        # En caso de tener un print
        elif inst.i1 == "print":
            # Pasar a un registro y luego imprimir la cadena
            inst2 = Ins()
            inst2.i1 = "MOV"
            inst2.i2 = "cx"
            inst2.i3 = inst.i2
            inst2.assembly = True
            self.instructions.insert(self.i, inst2)

            if inst2.i3 in self.symbols :
                load = Ins()
                load.i1 = "LOAD"
                load.i2 = "dx"
                load.i3 = self.symbols[inst2.i3]
                load.assembly = True
                self.instructions.insert(self.i, load)
                inst2.i3 = load.i2
                self.i = self.i + 1

            inst.assembly = True
            inst.i1 = "PRINT"
            inst.i2 = inst2.i2

        # i1 = [var, <tx>]
        inst.i1 = self.register(inst.i1)

        # i2 = [var, number, "string", <tx>, L1]++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        inst.i2 = self.register(inst.i2)
        # i3 = [var, number, "string", <tx>]++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        inst.i3 = self.register(inst.i3)

        # op = [+, -, *, /, ^, %, <, >, <=, >=, ==, !=, &&, ||]+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        flag = False
        n1_flag = False
        n2_flag = False
        try:
            n1 = float(inst.i2)
            n2 = float(inst.i3)
            inst.i2 = self.register(inst.i1)
            flag = True
        except:
            try:
                if inst.op != "":
                    n1 = float(inst.i2)
                    inst2 = Ins()
                    inst2.i1 = "MOV"
                    inst2.i2 = inst.result
                    inst2.i3 = n1
                    inst2.assembly = True
                    self.instructions.insert(self.i, inst2)
                    inst.i2 = inst2.i2
                    self.i = self.i + 1
                    n1_flag = True
                elif inst.op == "":
                    n1 = float(inst.i2)
                    inst.assembly = True
                    inst.i2 = inst.i1
                    inst.i1 = "MOV"
                    inst.i3 = n1
                    #print(inst)

            except:
                try:
                    n2 = float(inst.i3)
                    inst3 = Ins()
                    inst3.i1 = "MOV"
                    inst3.i2 = "dx"
                    inst3.i3 = n2
                    inst3.assembly = True
                    self.instructions.insert(self.i, inst3)
                    inst.i3 = inst3.i2
                    self.i = self.i + 1
                    n2_flag = True
                except:
                    pass

        # Si los dos valores son numeros
        if flag:
            # Operaciones aritmeticas
            if inst.op == "+":
                inst.assembly = True
                inst.i1 = "MOV"
                inst.i3 = n1 + n2
            elif inst.op == "-":
                inst.assembly = True
                inst.i1 = "MOV"
                inst.i3 = n1 - n2
            elif inst.op == "*":
                inst.assembly = True
                inst.i1 = "MOV"
                inst.i3 = n1 * n2
            elif inst.op == "/":
                inst.assembly = True
                inst.i1 = "MOV"
                inst.i3 = n1 / n2
            elif inst.op == "^":
                inst.assembly = True
                inst.i1 = "MOV"
                inst.i3 = n1 ** n2
            elif inst.op == "%":
                inst.assembly = True
                inst.i1 = "MOV"
                inst.i3 = n1 % n2

            # Operaciones de comparacion
            elif inst.op == "==":
                inst.assembly = True
                inst.i1 = "MOV"
                inst.i3 = n1 == n2
            elif inst.op == "!=":
                inst.assembly = True
                inst.i1 = "MOV"
                inst.i3 = n1 != n2
            elif inst.op == ">":
                inst.assembly = True
                inst.i1 = "MOV"
                inst.i3 = n1 > n2
            elif inst.op == "<":
                inst.assembly = True
                inst.i1 = "MOV"
                inst.i3 = n1 < n2
            elif inst.op == ">=":
                inst.assembly = True
                inst.i1 = "MOV"
                inst.i3 = n1 >= n2
            elif inst.op == "<=":
                inst.assembly = True
                inst.i1 = "MOV"
                inst.i3 = n1 <= n2


        # Si uno o ninguno de los dos valores no es un numero
        else:
            # Operaciones aritmeticas
            if inst.op == "+":
                inst.assembly = True
                inst.i1 = "ADD"

            elif inst.op == "-":
                inst.assembly = True
                inst.i1 = "DEC"

            elif inst.op == "*":
                inst.assembly = True
                inst.i1 = "MUL"

            elif inst.op == "/":
                inst.assembly = True
                inst.i1 = "DIV"

            elif inst.op == "^":
                inst.assembly = True
                inst.i1 = "POW"

            elif inst.op == "%":
                inst.assembly = True
                inst.i1 = "MOD"


            # Operaciones logicas
            elif inst.op == "&&":
                inst.assembly = True
                inst.i1 = "AND"

            elif inst.op == "||":
                inst.assembly = True
                inst.i1 = "OR"


            # Operaciones de comparacion
            elif inst.op == "==":
                inst.assembly = True
                inst.i1 = "EQ"

            elif inst.op == "!=":
                inst.assembly = True
                inst.i1 = "NEQ"

            elif inst.op == ">":
                inst.assembly = True
                inst.i1 = "GREATER"

            elif inst.op == "<":
                inst.assembly = True
                inst.i1 = "LESS"

            elif inst.op == ">=":
                inst.assembly = True
                inst.i1 = "GEQ"

            elif inst.op == "<=":
                inst.assembly = True
                inst.i1 = "LEQ"

        special = ["if", "IF", "GOTO", "SLICE","PRINT", "goto", "LABEL", "print", "PUSH", "CALL", "POP", "LIST"]

        # Si hay una asignacion de registro a variable
        if inst.op == "" and inst.i1 not in special and type(inst.i3) != type(0.0):
            inst.i1 = "MOV"
            inst.i3 = inst.i2
            inst.i2 = inst.result
            inst.assembly = True
            #print(inst)

        if type(inst.i2) == type("") and type(inst.i3) == type(""):
            # Si el primer operando es un string
            if inst.i2[0] == '"':
                inst3 = Ins()
                inst3.i1 = "MOV"
                inst3.i2 = "cx"
                inst3.i3 = inst.i2
                inst3.assembly = True
                self.instructions.insert(self.i, inst3)
                inst.i2 = inst3.i2
                self.i = self.i + 1
            # Si el segundo operando es un string
            if inst.i3[0] == '"':
                inst3 = Ins()
                inst3.i1 = "MOV"
                inst3.i2 = "dx"
                inst3.i3 = inst.i3
                inst3.assembly = True
                self.instructions.insert(self.i, inst3)
                inst.i3 = inst3.i2
                self.i = self.i + 1
        # Si el primer operando es una variable, leerla de memoria
        if inst.i1 != "MOV" and inst.i2 in self.symbols:
            load = Ins()
            load.i1 = "LOAD"
            load.i2 = "cx"
            load.i3 = self.symbols[inst.i2]
            load.assembly = True
            self.instructions.insert(self.i, load)
            inst.i2 = load.i2
            self.i = self.i + 1

        # Si el segundo operando es una variable, leerla de memoria
        if  inst.i3 in self.symbols:
            load = Ins()
            load.i1 = "LOAD"
            load.i2 = "dx"
            load.i3 = self.symbols[inst.i3]
            load.assembly = True
            self.instructions.insert(self.i, load)
            inst.i3 = load.i2
            self.i = self.i + 1

        # Si es asignacion de variable a varible directamente
        if inst.i1 == "MOV" and inst.i3 in self.symbols:
            load = Ins()
            load.i1 = "LOAD"
            load.i2 = "dx"
            load.i3 = self.symbols[inst.i3]
            load.assembly = True
            self.instructions.insert(self.i, load)
            inst.i3 = load.i2
            self.i = self.i + 1

        # Si es un asignacion de memoria
        if inst.i1 == "MOV" and inst.i2 in self.symbols:
            inst.i2 = self.symbols[inst.i2]

        mov = Ins()
        # Mover el resultado al registro correspondiente
        if n2_flag or inst.op != "" and inst.result != inst.i2 and inst.i1 not in special:
            mov.i1 = "MOV"
            mov.i2 = inst.result
            mov.i3 = inst.i2
            mov.assembly = True
            self.instructions.insert(self.i + 1, mov)
            self.i = self.i + 1

            if mov.i2 in self.symbols :
                mov.i2 = self.symbols[mov.i2]


    def register(self, tx):
        if tx == "<t0>":
            return "ax"
        if tx == "<t1>":
            return "bx"
        if tx == "<t2>":
            return "cx"
        if tx == "<t3>":
            return "dx"
        return tx
