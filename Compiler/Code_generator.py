class Code_generator:
    def __init__(self, instructions, symbols):
        self.instructions = instructions
        self.assembly = []
        self.symbols = symbols
        self.count_variables = 0
        self.global_variables()
        self.translate()
        self.print_codes()

    def print_codes(self):
        print(self.symbols)

        for ins in self.instructions:
            print(ins)
        print("\n")
        for asse in self.assembly:
            print(asse)

    def translate(self):
        for inst in self.instructions:
            self.operations(inst)

        self.assembly.append(["END", '', ''])

    def global_variables(self):
        i = 0
        for key in self.symbols.keys():
            self.symbols[key] = i
            i = i + 1

    def operations(self, inst):
        s = ["+", "-", "*", "/", "^", "%", ]
        # En el caso en el que hayan variables
        if inst.i1 in self.symbols:
            # Caso a = 1
            try:
                n1 = float(inst.i2)
                self.assembly.append(["MOV", self.symbols[inst.i1], n1])

            # Caso a = <tx> | a = "string" | a++ | a--
            except ValueError:
                if inst.i2 in self.symbols:
                    # Caso a++  --->  a = a + 1
                    if inst.op == s[0]:
                        asse = ["ADD", inst.i1, float(inst.i3)]
                    # Caso a--  --->  a = a - 1
                    elif inst.op == s[1]:
                        asse = ["DEC", inst.i1, float(inst.i3)]

                    # Cargar la variable
                    self.assembly.append(["LOAD", "dx", self.symbols[asse[1]]])
                    # Poner el 1 en un registro
                    n1 = float(inst.i3)
                    self.assembly.append(["MOV", "cx", n1])
                    # Reemplazar en la instruccion de suma
                    asse[1] = "dx"
                    asse[2] = "cx"
                    self.assembly.append(asse)
                    # Mover el resultado a memoria de nuevo
                    self.assembly.append(["MOV", self.symbols[inst.i1], "dx"])

                else:
                    # Caso a = <tx> o a = "string"
                    self.assembly.append(["MOV", self.symbols[inst.i1], self.register(inst.i2)])

        else:  # elif inst.op in s:
            # Caso <tn> = numero op numero
            try:
                n1 = float(inst.i2)
                n2 = float(inst.i3)

                # Operaciones aritmeticas
                if inst.op == s[0]:
                    self.assembly.append(["MOV", self.register(inst.i1), n1 + n2])
                elif inst.op == s[1]:
                    self.assembly.append(["MOV", self.register(inst.i1), n1 - n2])
                elif inst.op == s[2]:
                    self.assembly.append(["MOV", self.register(inst.i1), n1 * n2])
                elif inst.op == s[3]:
                    self.assembly.append(["MOV", self.register(inst.i1), n1 / n2])
                elif inst.op == s[4]:
                    self.assembly.append(["MOV", self.register(inst.i1), n1 ** n2])
                elif inst.op == s[5]:
                    self.assembly.append(["MOV", self.register(inst.i1), n1 % n2])

                # Operaciones de comparacion
                elif inst.op == "==":
                    self.assembly.append(["MOV", self.register(inst.i1), n1 == n2])
                elif inst.op == "!=":
                    self.assembly.append(["MOV", self.register(inst.i1), n1 != n2])
                elif inst.op == ">":
                    self.assembly.append(["MOV", self.register(inst.i1), n1 > n2])
                elif inst.op == "<":
                    self.assembly.append(["MOV", self.register(inst.i1), n1 < n2])
                elif inst.op == ">=":
                    self.assembly.append(["MOV", self.register(inst.i1), n1 >= n2])
                elif inst.op == "<=":
                    self.assembly.append(["MOV", self.register(inst.i1), n1 <= n2])

            except ValueError:
                # Caso <tn> = numero op <tx>
                try:
                    # Ya que el resultado se guarda en el primer registro no es necesario colocar un move
                    # al final
                    n1 = float(inst.i2)
                    self.assembly.append(["MOV", self.register(inst.i1), n1])
                    # Se especifica el LOAD para evitar que las direcciones siendo enteros se malinterpreten
                    if inst.i1 != "LOAD":
                        # Instrucciones aritmeticas
                        if inst.op == s[0]:
                            self.assembly.append(["ADD", self.register(inst.i1), self.register(inst.i3)])
                        elif inst.op == s[1]:
                            self.assembly.append(["DEC", self.register(inst.i1), self.register(inst.i3)])
                        elif inst.op == s[2]:
                            self.assembly.append(["MUL", self.register(inst.i1), self.register(inst.i3)])
                        elif inst.op == s[3]:
                            self.assembly.append(["DIV", self.register(inst.i1), self.register(inst.i3)])
                        elif inst.op == s[4]:
                            self.assembly.append(["POW", self.register(inst.i1), self.register(inst.i3)])
                        elif inst.op == s[5]:
                            self.assembly.append(["MOD", self.register(inst.i1), self.register(inst.i3)])

                        # Instrucciones de comparacion
                        elif inst.op == "==":
                            self.assembly.append(["EQ", self.register(inst.i1), self.register(inst.i3)])
                        elif inst.op == "!=":
                            self.assembly.append(["NEQ", self.register(inst.i1), self.register(inst.i3)])
                        elif inst.op == ">":
                            self.assembly.append(["GREATER", self.register(inst.i1), self.register(inst.i3)])
                        elif inst.op == "<":
                            self.assembly.append(["LESS", self.register(inst.i1), self.register(inst.i3)])
                        elif inst.op == ">=":
                            self.assembly.append(["GEQ", self.register(inst.i1), self.register(inst.i3)])
                        elif inst.op == "<=":
                            self.assembly.append(["LEQ", self.register(inst.i1), self.register(inst.i3)])

                    # En caso de que <tx> resulte ser una variable
                    asse = self.assembly[len(self.assembly) - 1]
                    if asse[2] in self.symbols:
                        self.assembly.pop()
                        self.assembly.append(["LOAD", "dx", self.symbols[asse[2]]])
                        asse[2] = "dx"
                        self.assembly.append(asse)
                except:
                    # Caso <tn> = <tx> op numero
                    try:
                        n1 = float(inst.i3)
                        self.assembly.append(["MOV", self.register(inst.i1), n1])

                        # Instrucciones aritmeticas
                        if inst.op == s[0]:
                            self.assembly.append(["ADD", self.register(inst.i2), self.register(inst.i1)])
                        elif inst.op == s[1]:
                            self.assembly.append(["DEC", self.register(inst.i2), self.register(inst.i1)])
                        elif inst.op == s[2]:
                            self.assembly.append(["MUL", self.register(inst.i2), self.register(inst.i1)])
                        elif inst.op == s[3]:
                            self.assembly.append(["DIV", self.register(inst.i2), self.register(inst.i1)])
                        elif inst.op == s[4]:
                            self.assembly.append(["POW", self.register(inst.i2), self.register(inst.i1)])
                        elif inst.op == s[5]:
                            self.assembly.append(["MOD", self.register(inst.i2), self.register(inst.i1)])

                        # Instrucciones de comparacion
                        elif inst.op == "==":
                            self.assembly.append(["EQ", self.register(inst.i2), self.register(inst.i1)])
                        elif inst.op == "!=":
                            self.assembly.append(["NEQ", self.register(inst.i2), self.register(inst.i1)])
                        elif inst.op == ">":
                            self.assembly.append(["GREATER", self.register(inst.i2), self.register(inst.i1)])
                        elif inst.op == "<":
                            self.assembly.append(["LESS", self.register(inst.i2), self.register(inst.i1)])
                        elif inst.op == ">=":
                            self.assembly.append(["GEQ", self.register(inst.i2), self.register(inst.i1)])
                        elif inst.op == "<=":
                            self.assembly.append(["LEQ", self.register(inst.i2), self.register(inst.i1)])

                        # En caso de que <tx> resulte ser una variable
                        asse = self.assembly[len(self.assembly) - 1]
                        if asse[1] in self.symbols:
                            self.assembly.pop()
                            self.assembly.append(["LOAD", "dx", self.symbols[asse[1]]])
                            asse[1] = "dx"
                            self.assembly.append(asse)

                        # Mover el resultado al registro correspondiente
                        self.assembly.append(["MOV", self.register(inst.i1), "dx"])

                    # Caso <tn> = <tx> op <ty>
                    except:
                        # Caso <tn> = "string" + <tx>
                        if inst.i2[0] == '"' and inst.i3[0:2] == "<t":
                            # Quitar las comillas del texto
                            inst.i2 = inst.i2[1:-1]
                            #Pasar a un registro y luego concatenar las cadenas
                            self.assembly.append(["MOV", self.register(inst.i1), inst.i2])
                            self.assembly.append(["ADD", self.register(inst.i1), self.register(inst.i3)])

                        # Caso <tn> = <tx> + "string"
                        elif inst.i2[0:2] == "<t" and inst.i3[0] == '"':
                            # Quitar las comillas del texto
                            inst.i2 = inst.i2[1:-1]
                            # Pasar a un registro y luego concatenar las cadenas
                            self.assembly.append(["MOV", self.register(inst.i1), inst.i3])
                            self.assembly.append(["ADD", self.register(inst.i2), self.register(inst.i1)])

                        # Caso <tn> = "string" + var
                        elif inst.i2[0] == '"' and inst.i3 in self.symbols:
                            # Quitar las comillas del texto
                            inst.i2 = inst.i2[1:-1]
                            #Pasar a un registro y luego concatenar las cadenas
                            self.assembly.append(["MOV", self.register(inst.i1), inst.i2])
                            self.assembly.append(["ADD", self.register(inst.i1), self.register(inst.i3)])

                        # Caso <tn> = var + "string"
                        elif inst.i2 in self.symbols and inst.i3[0] == '"':
                            # Quitar las comillas del texto
                            inst.i2 = inst.i2[1:-1]
                            # Pasar a un registro y luego concatenar las cadenas
                            self.assembly.append(["MOV", self.register(inst.i1), inst.i3])
                            self.assembly.append(["ADD", self.register(inst.i2), self.register(inst.i1)])

                        # Caso <tn> = "string" + "string"
                        elif inst.i2[0] == '"' and inst.i3[0] == '"':
                            inst.i2 = inst.i2[1:-1]
                            inst.i3 = inst.i3[1:-1]
                            self.assembly.append(["MOV", self.register(inst.i1), inst.i2 + inst.i3])

                        # Operaciones aritmeticas
                        elif inst.op == s[0]:
                            self.assembly.append(["ADD", self.register(inst.i2), self.register(inst.i3)])
                        elif inst.op == s[1]:
                            self.assembly.append(["DEC", self.register(inst.i2), self.register(inst.i3)])
                        elif inst.op == s[2]:
                            self.assembly.append(["MUL", self.register(inst.i2), self.register(inst.i3)])
                        elif inst.op == s[3]:
                            self.assembly.append(["DIV", self.register(inst.i2), self.register(inst.i3)])
                        elif inst.op == s[4]:
                            self.assembly.append(["POW", self.register(inst.i2), self.register(inst.i3)])
                        elif inst.op == s[5]:
                            self.assembly.append(["MOD", self.register(inst.i2), self.register(inst.i3)])

                        # Operaciones logicas
                        elif inst.op == "&&":
                            self.assembly.append(["AND", self.register(inst.i2), self.register(inst.i3)])
                        elif inst.op == "||":
                            self.assembly.append(["OR", self.register(inst.i2), self.register(inst.i3)])

                        # Operaciones de comparacion
                        elif inst.op == "==":
                            self.assembly.append(["EQ", self.register(inst.i2), self.register(inst.i3)])
                        elif inst.op == "!=":
                            self.assembly.append(["NEQ", self.register(inst.i2), self.register(inst.i3)])
                        elif inst.op == ">":
                            self.assembly.append(["GREATER", self.register(inst.i2), self.register(inst.i3)])
                        elif inst.op == "<":
                            self.assembly.append(["LESS", self.register(inst.i2), self.register(inst.i3)])
                        elif inst.op == ">=":
                            self.assembly.append(["GEQ", self.register(inst.i2), self.register(inst.i3)])
                        elif inst.op == "<=":
                            self.assembly.append(["LEQ", self.register(inst.i2), self.register(inst.i3)])

                        # En caso de que <tx> o <ty> sean variables
                        asse = self.assembly[len(self.assembly) - 1]
                        # Leer la primera variable
                        if asse[1] in self.symbols:
                            self.assembly.pop()
                            self.assembly.append(["LOAD", "cx", self.symbols[asse[1]]])
                            asse[1] = "cx"
                            self.assembly.append(asse)
                        # Leer la segunda variable
                        asse = self.assembly[len(self.assembly) - 1]
                        if asse[2] in self.symbols:
                            self.assembly.pop()
                            self.assembly.append(["LOAD", "dx", self.symbols[asse[2]]])
                            asse[2] = "dx"
                            self.assembly.append(asse)
                        # En caso de tener un if
                        if inst.i1 == "if":
                            self.assembly.append(["IF", asse[1], inst.i3])

                        # En caso de tener un goto
                        elif inst.i1 == "goto":
                            self.assembly.append(["GOTO", inst.i2, ""])

                        # En caso de tener un label
                        elif inst.i1 == "LABEL":
                            self.assembly.append(["LABEL", inst.i2, ""])

                        else:
                            # Mover por defecto el resultado al registro correspondiente
                            r1 = self.register(inst.i1)
                            r2 = asse[1]
                            #Mover si los registros son diferentes
                            if r1 != r2:
                                self.assembly.append(["MOV", r1, r2])

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
