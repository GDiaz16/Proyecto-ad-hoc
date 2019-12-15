from gen import brownieParser
from gen.brownieVisitor import brownieVisitor
from gen.brownieParser import brownieParser
from Compiler.Instruction import instruction as ins


class Visitor(brownieVisitor):
    def __init__(self):
        self.count = 0
        self.label_count = 1
        self.instructions = []
        self.loop_label = []
        self.symbols_table = {}  # {"name": address in memory}

    # Visit a parse tree produced by brownieParser#start.
    def visitStart(self, ctx: brownieParser.StartContext):
        self.visitChildren(ctx)

    def visitDefinition(self, ctx: brownieParser.DefinitionContext):
        return self.visit(ctx.assign())

    # Visit a parse tree produced by brownieParser#assign1.
    def visitAssign1(self, ctx: brownieParser.Assign1Context):
        inst = ins()
        self.add_count()  # self.count = self.count + 1
        inst.i1 = str(ctx.VARIABLE())
        inst.i2 = self.visit(ctx.exp()).i1
        self.instructions.append(inst)
        inst.pos = len(self.instructions) - 1

        # Asignar la variable a la tabla de simbolos
        self.symbols_table[inst.i1] = 0

        return inst

    # Visit a parse tree produced by brownieParser#assign2.
    def visitAssign2(self, ctx: brownieParser.Assign2Context):
        inst = ins()
        self.add_count()  # self.count = self.count + 1
        inst.i1 = str(ctx.VARIABLE())
        inst.i2 = str(ctx.VARIABLE())
        inst.op = '+'
        inst.i3 = 1
        self.instructions.append(inst)
        inst.pos = len(self.instructions) - 1
        return inst

    # Visit a parse tree produced by brownieParser#assign3.
    def visitAssign3(self, ctx: brownieParser.Assign3Context):
        inst = ins()
        self.add_count()  # self.count = self.count + 1
        inst.i1 = str(ctx.VARIABLE())
        inst.i2 = str(ctx.VARIABLE())
        inst.op = '-'
        inst.i3 = 1
        self.instructions.append(inst)
        inst.pos = len(self.instructions) - 1
        return inst

    # Visit a parse tree produced by brownieParser#assign4.
    def visitAssign4(self, ctx: brownieParser.Assign4Context):
        inst = ins()
        self.add_count()  # self.count = self.count + 1
        inst.i1 = "LIST"
        inst.i2 = str(ctx.VARIABLE())
        self.instructions.append(inst)
        inst.pos = len(self.instructions) - 1

        # Asignar la variable a la tabla de simbolos
        self.symbols_table[inst.i2] = 0

        # Llamar los elementos que se van a insertar en la lista
        self.visit(ctx.list_elements())

        # Actualizar los elementos que se insertaron en la lista
        pos = len(self.instructions)
        j = 0
        for i in range(inst.pos + 1, pos):
            aux = self.instructions[i]
            aux.i1 = inst.i2
            aux.i2 = j
            j = j + 1

    # Visit a parse tree produced by brownieParser#element1.
    def visitElement1(self, ctx: brownieParser.Element1Context):
        inst = ins()
        self.add_count()  # self.count = self.count + 1
        inst.array1 = True
        inst.i3 = str(ctx.NUMBER())
        self.instructions.append(inst)
        inst.pos = len(self.instructions) - 1

    # Visit a parse tree produced by brownieParser#element2.
    def visitElement2(self, ctx: brownieParser.Element2Context):
        inst = ins()
        self.add_count()  # self.count = self.count + 1
        inst.array1 = True
        inst.i3 = str(ctx.VARIABLE())
        self.instructions.append(inst)
        inst.pos = len(self.instructions) - 1

    # Visit a parse tree produced by brownieParser#element3.
    def visitElement3(self, ctx: brownieParser.Element3Context):
        inst = ins()
        self.add_count()  # self.count = self.count + 1
        inst.array1 = True
        inst.i3 = str(ctx.STRING())
        self.instructions.append(inst)
        inst.pos = len(self.instructions) - 1

    # Visit a parse tree produced by brownieParser#assign5.
    def visitAssign5(self, ctx: brownieParser.Assign5Context):
        aux = str(self.visit(ctx.exp()).i1)
        array = self.visit(ctx.array_call())
        array.i1 = array.i2
        array.i2 = array.i3
        array.i3 = aux
        array.array1 = True
        array.array2 = False
        return array

    # Visit a parse tree produced by brownieParser#exp1.
    def visitExp1(self, ctx: brownieParser.Exp1Context):
        inst = ins()
        self.add_count()  # self.count = self.count + 1
        inst.i1 = f"<t{self.count}>"
        inst.i2 = self.visit(ctx.exp()).i1
        inst.op = str(self.visit(ctx.ar_operator()))
        inst.i3 = self.visit(ctx.term()).i1
        self.instructions.append(inst)
        inst.pos = len(self.instructions) - 1
        return inst

    # Visit a parse tree produced by brownieParser#term1.
    def visitTerm1(self, ctx: brownieParser.Term1Context):
        inst = ins()
        self.add_count()  # self.count = self.count + 1
        inst.i1 = f"<t{self.count}>"
        inst.i2 = self.visit(ctx.ar_value()).i1
        inst.op = str(self.visit(ctx.prior_operator()))
        inst.i3 = self.visit(ctx.term()).i1
        self.instructions.append(inst)
        inst.pos = len(self.instructions) - 1
        return inst

    # Visit a parse tree produced by brownieParser#ar_value1.
    def visitAr_value1(self, ctx: brownieParser.Ar_value1Context):
        inst = ins()
        inst.pos = len(self.instructions) - 1
        inst.i1 = str(ctx.NUMBER())
        return inst

    # Visit a parse tree produced by brownieParser#ar_value2.
    def visitAr_value2(self, ctx: brownieParser.Ar_value2Context):
        inst = ins()
        inst.pos = len(self.instructions) - 1
        inst.i1 = str(ctx.VARIABLE())
        return inst

    # Visit a parse tree produced by brownieParser#ar_value4.
    def visitAr_value4(self, ctx: brownieParser.Ar_value4Context):
        return self.visit(ctx.exp())

    # Visit a parse tree produced by brownieParser#ar_operator1.
    def visitAr_operator(self, ctx: brownieParser.Ar_operatorContext):
        return str(ctx.getText())

    # Visit a parse tree produced by brownieParser#prior_operator1.
    def visitPrior_operator(self, ctx: brownieParser.Prior_operatorContext):
        return str(ctx.getText())

    # Visit a parse tree produced by brownieParser#assign6.
    def visitAssign6(self, ctx: brownieParser.Assign6Context):
        inst = ins()
        self.add_count()  # self.count = self.count + 1
        inst.i1 = str(ctx.VARIABLE())
        inst.i2 = self.visit(ctx.text()).i1
        self.instructions.append(inst)
        inst.pos = len(self.instructions) - 1

        # Asignar la variable a la tabla de simbolos
        self.symbols_table[inst.i1] = 0

        return inst

    # Visit a parse tree produced by brownieParser#text1.
    def visitText1(self, ctx: brownieParser.Text1Context):
        inst = ins()
        self.add_count()  # self.count = self.count + 1
        inst.i1 = f"<t{self.count}>"
        inst.i2 = self.visit(ctx.text(0)).i1
        inst.op = str(ctx.PLUS())
        inst.i3 = self.visit(ctx.text(1)).i1
        self.instructions.append(inst)
        inst.pos = len(self.instructions) - 1
        return inst

    # Visit a parse tree produced by brownieParser#text2.
    def visitText2(self, ctx: brownieParser.Text2Context):
        inst = ins()
        inst.pos = len(self.instructions) - 1
        inst.i1 = str(ctx.STRING())
        return inst

    # Visit a parse tree produced by brownieParser#text3.
    def visitText3(self, ctx: brownieParser.Text3Context):
        inst = ins()
        inst.pos = len(self.instructions) - 1
        inst.i1 = str(ctx.VARIABLE())
        return inst

    # Visit a parse tree produced by brownieParser#call.
    def visitCall(self, ctx: brownieParser.CallContext):
        ret = ins()
        inst = ins()
        call = ins()

        # Asignar direccion de retorno
        self.instructions.append(ret)
        ret.pos = len(self.instructions) - 1
        self.add_count()  # self.count = self.count + 1
        ret.i1 = f"<t{self.count}>"

        # Apilar la direccion de retorno
        self.instructions.append(inst)
        inst.pos = len(self.instructions) - 1
        self.add_count()  # #self.count = self.count + 1
        inst.i1 = f"PUSH"
        inst.i2 = ret.i1

        # Apilar parametros
        self.visitChildren(ctx)

        # Llamada a la funcion
        self.instructions.append(call)
        call.pos = len(self.instructions) - 1
        self.add_count()  # #self.count = self.count + 1
        call.i1 = f"CALL"
        call.i2 = str(ctx.VARIABLE())

        # Asignar direccion de retorno
        ret.i2 = call.pos + 1

        # Desapilar el valor que devuelve la funcion y devolverlo
        pop_ = ins()
        self.instructions.append(pop_)
        pop_.pos = len(self.instructions) - 1
        self.add_count()  # self.count = self.count + 1
        pop_.i1 = f"POP"
        pop_.i2 = f"<t{self.count}>"

        # Auxiliar de retorno
        aux = ins()
        aux.i1 = f"<t{self.count}>"
        return aux

    # Visit a parse tree produced by brownieParser#parameter_call3.
    def visitParameter_call4(self, ctx: brownieParser.Parameter_call4Context):
        inst = ins()
        inst.i1 = "PUSH"
        inst.i2 = self.visit(ctx.call()).i1
        self.instructions.append(inst)
        inst.pos = len(self.instructions) - 1
        return inst

    # Visit a parse tree produced by brownieParser#parameter_call3.
    def visitParameter_call3(self, ctx: brownieParser.Parameter_call3Context):
        inst = ins()
        inst.i1 = "PUSH"
        inst.i2 = str(ctx.STRING())
        self.instructions.append(inst)
        inst.pos = len(self.instructions) - 1
        return inst

    # Visit a parse tree produced by brownieParser#parameter_call2.
    def visitParameter_call2(self, ctx: brownieParser.Parameter_call2Context):
        inst = ins()
        inst.i1 = "PUSH"
        inst.i2 = str(ctx.NUMBER())
        self.instructions.append(inst)
        inst.pos = len(self.instructions) - 1
        return inst

    # Visit a parse tree produced by brownieParser#parameter_call1.
    def visitParameter_call1(self, ctx: brownieParser.Parameter_call1Context):
        inst = ins()
        inst.i1 = "PUSH"
        inst.i2 = str(ctx.VARIABLE())
        self.instructions.append(inst)
        inst.pos = len(self.instructions) - 1
        return inst

    # Visit a parse tree produced by brownieParser#array_call.
    def visitArray_call(self, ctx: brownieParser.Array_callContext):
        inst = ins()
        self.add_count()  # self.count = self.count + 1
        inst.i1 = f"<t{self.count}>"
        inst.i2 = str(ctx.VARIABLE())
        inst.i3 = str(self.visit(ctx.ar_value()).i1)
        inst.array2 = True
        self.instructions.append(inst)
        inst.pos = len(self.instructions) - 1
        return inst

    # Visit a parse tree produced by brownieParser#conditional.
    def visitConditional(self, ctx: brownieParser.ConditionalContext):
        # if (condicion) goto Lv;
        # goto Lf;
        # Lv:
        # < instrucciones >
        # goto Lsalida;
        # Lf:
        # < instrucciones >
        # Lsalida:

        # Insertar if
        if_ = ins()
        if_.i1 = "if"
        if_.i2 = self.visit(ctx.condition()).i1
        if_.op = "goto"
        self.instructions.append(if_)
        if_.pos = len(self.instructions) - 1

        # Insertar salto al else
        els = ins()
        els.i1 = "goto"
        self.instructions.append(els)
        els.pos = len(self.instructions) - 1

        # Asignar el body del if al goto
        L1, L2 = self.visit(ctx.body())
        if_.i3 = L1.i2

        # Asignar la posicion que sigue si no se cumple la condicion
        els.i2 = L2.i2

        # Else y demas condicionales
        try:
            K1 = self.visit(ctx.otherwise())
            els.i2 = K1.i2
        except:
            pass

    # Visit a parse tree produced by brownieParser#otherwise1.
    def visitOtherwise1(self, ctx: brownieParser.Otherwise1Context):
        # Salto para evitar este elif si ya fue cumplido previamente
        goto = self.goto("")
        K1 = self.label()

        # Insertar elif
        if_ = ins()
        if_.i1 = "elif"
        if_.i2 = self.visit(ctx.condition()).i1
        if_.op = "goto"
        self.instructions.append(if_)
        if_.pos = len(self.instructions) - 1

        # Insertar salto al else
        els = ins()
        els.i1 = "goto"
        self.instructions.append(els)
        els.pos = len(self.instructions) - 1

        # Asignar el body del if al goto
        L1, L2 = self.visit(ctx.body())
        if_.i3 = L1.i2
        goto.i2 = L2.i2
        # Asignar la posicion que sigue si no se cumple la condicion
        els.i2 = L2.i2

        # Else y demas condicionales
        try:
            L1 = self.visit(ctx.otherwise())
            els.i2 = L1.i2
        except:
            pass

        return K1

    # Visit a parse tree produced by brownieParser#otherwise2.
    def visitOtherwise2(self, ctx: brownieParser.Otherwise2Context):
        goto = self.goto("")
        L1, L2 = self.visit(ctx.body())
        goto.i2 = L2.i2
        return L1

    # Visit a parse tree produced by brownieParser#other_condition1.
    def visitOther_condition1(self, ctx: brownieParser.Other_condition1Context):
        inst = ins()
        self.add_count()  # self.count = self.count + 1
        inst.i1 = f"<t{self.count}>"
        inst.i2 = self.visit(ctx.com_value()).i1
        inst.op = str(self.visit(ctx.comparator()))
        inst.i3 = self.visit(ctx.other_condition()).i1
        self.instructions.append(inst)
        inst.pos = len(self.instructions) - 1
        return inst

    # Visit a parse tree produced by brownieParser#condition1.
    def visitCondition1(self, ctx: brownieParser.Condition1Context):
        inst = ins()
        self.add_count()  # self.count = self.count + 1
        inst.i1 = f"<t{self.count}>"
        inst.i2 = self.visit(ctx.condition()).i1
        inst.op = str(self.visit(ctx.logic()))

        inst.i3 = self.visit(ctx.other_cond()).i1
        self.instructions.append(inst)
        inst.pos = len(self.instructions) - 1
        return inst

    # Visit a parse tree produced by brownieParser#other_cond.
    def visitOther_cond(self, ctx: brownieParser.Other_condContext):
        inst = ins()
        # Si hay un not
        try:
            self.visit(ctx.NOT())
            self.add_count()  # self.count = self.count + 1
            inst.i1 = f"<t{self.count}>"
            inst.i2 = "NOT"
            inst.i3 = self.visit(ctx.other_condition()).i1
            self.instructions.append(inst)
            inst.pos = len(self.instructions) - 1
            return inst
        # Si no hay not
        except:
            return self.visit(ctx.other_condition())

    # Visit a parse tree produced by brownieParser#com_value.
    def visitCom_value(self, ctx: brownieParser.Com_valueContext):
        try:
            aux = self.visit(ctx.ar_value())
            return aux
        except AttributeError:
            pass
        # Auxiliar de retorno
        aux = ins()
        aux.i1 = str(ctx.getText())
        return aux

    # Visit a parse tree produced by brownieParser#comparator.
    def visitComparator(self, ctx: brownieParser.ComparatorContext):
        return str(ctx.getText())

    # Visit a parse tree produced by brownieParser#logic.
    def visitLogic(self, ctx: brownieParser.LogicContext):
        return str(ctx.getText())

    # Visit a parse tree produced by brownieParser#body.
    def visitBody(self, ctx: brownieParser.BodyContext):
        # Inicio de body
        l1 = self.label()

        # Contenido
        self.visitChildren(ctx)

        # Fin de body
        l2 = self.label()

        return l1, l2

    # Visit a parse tree produced by brownieParser#do_while.
    def visitDo_while(self, ctx: brownieParser.Do_whileContext):
        # Lregreso:
        # < instrucciones >
        # if (condicion) goto Lregreso;
        # < instrucciones >

        # Body del do
        L1, L2 = self.visit(ctx.body())

        # Insertar if
        if_ = ins()
        if_.i1 = "if"
        if_.i2 = self.visit(ctx.condition()).i1
        if_.op = "goto"
        self.instructions.append(if_)
        if_.pos = len(self.instructions) - 1
        # Asignar el body del while al goto
        if_.i3 = L1.i2

        # Label en caso de Break
        # self.loop_label.append(self.label())

    # Visit a parse tree produced by brownieParser#while_.
    def visitWhile_(self, ctx: brownieParser.While_Context):
        # Lregreso:
        # if (condicion) goto Lv;
        # goto Lf;
        # Lv:
        # < instrucciones >
        # goto Lregreso;
        # Lf:
        # < instrucciones >

        # Etiqueta de regreso
        K1 = self.label()

        # Insertar if
        if_ = ins()
        if_.i1 = "if"
        if_.i2 = self.visit(ctx.condition()).i1
        if_.op = "goto"
        self.instructions.append(if_)
        if_.pos = len(self.instructions) - 1

        # Insertar salto de salida del ciclo
        els = ins()
        els.i1 = "goto"
        self.instructions.append(els)
        els.pos = len(self.instructions) - 1

        # Asignar el body del while al goto
        L1, L2 = self.visit(ctx.body())
        if_.i3 = L1.i2

        # Salto al inicio para evaluar de nuevo la condicion
        self.goto(K1.i2)

        # Etiqueta para salir del bucle
        K2 = self.label()
        els.i2 = K2.i2
        # self.loop_label.append(K2)

    # Visit a parse tree produced by brownieParser#for_.
    def visitFor_(self, ctx: brownieParser.For_Context):
        # for (< asignacion >; < condicion >; < actualización >){ < cuerpo >}
        # < asignacion de variables >
        # Lback:
        # if (condicion) goto Lv;
        # goto Lf;
        # Lupdate:
        # < actualizacion >
        # goto Lregreso;
        # Lv:
        # < instrucciones >
        # goto Lupdate;
        # Lf:
        # < instrucciones >

        if_, els, Lupdate = self.visit(ctx.for_condition())
        Lv, L2 = self.visit(ctx.body())

        # Actualizar goto del if
        if_.i3 = Lv.i2

        # Salto a actualizacion de variables
        self.goto(Lupdate.i2)

        # Etiqueta para salir del for
        Lf = self.label()

        # Asignar etiqueta para salir del for
        els.i2 = Lf.i2

    # Visit a parse tree produced by brownieParser#for_condition.
    def visitFor_condition1(self, ctx: brownieParser.For_condition1Context):
        # definicion de variables
        self.visit(ctx.for_definition())

        # Etiqueta de regreso
        Lback = self.label()

        # Insertar if (la direccion del goto se asigna en el for)
        if_ = ins()
        if_.i1 = "if"
        if_.i2 = self.visit(ctx.condition()).i1
        if_.op = "goto"
        self.instructions.append(if_)
        if_.pos = len(self.instructions) - 1

        # Insertar salto al else (la direccion del goto se asigna en el for)
        els = ins()
        els.i1 = "goto"
        self.instructions.append(els)
        els.pos = len(self.instructions) - 1

        # Insertar etiqueta de actualizacion
        Lupdate = self.label()

        # Actualizar variables
        self.visit(ctx.assign())

        # Saltar al inicio
        self.goto(Lback.i2)

        return if_, els, Lupdate

    # Visit a parse tree produced by brownieParser#for_condition.
    def visitFor_condition2(self, ctx: brownieParser.For_condition2Context):
        pass

    # Visit a parse tree produced by brownieParser#for_definition.
    def visitFor_definition(self, ctx: brownieParser.For_definitionContext):
        inst = ins()
        self.add_count()  # self.count = self.count + 1
        inst.i1 = str(ctx.VARIABLE())
        inst.i2 = self.visit(ctx.exp()).i1
        self.instructions.append(inst)
        inst.pos = len(self.instructions) - 1

        self.symbols_table[inst.i1] = 0

        return inst

    # Visit a parse tree produced by brownieParser#for_iterator.
    def visitFor_iterator(self, ctx: brownieParser.For_iteratorContext):
        pass

    # Visit a parse tree produced by brownieParser#break_.
    def visitBreak_(self, ctx: brownieParser.Break_Context):
        try:
            label = self.loop_label.pop()
            self.goto(label.i2)
        except IndexError:
            raise Exception("Break out of loop")

    # Visit a parse tree produced by brownieParser#function.
    def visitFunction(self, ctx: brownieParser.FunctionContext):
        # Ignorar la funcion hasta que se haga el llamado
        #goto = self.goto("")

        #Asignar la funcion a la tabla de simbolos
        self.symbols_table[str(ctx.VARIABLE())] = 0

        # Etiqueta para saber que es una funcion
        start = self.label(label= str(ctx.VARIABLE()))
        start.i1 = "<fun>"
        # Parametros
        self.visit(ctx.parameter())

        # Body
        L2 = self.visit(ctx.fun_body())
        L2.i1 = "<EndFun>"
        L2.i2 =str(ctx.VARIABLE())
        # Actualizar goto
        #goto.i2 = L2.i2

    # Visit a parse tree produced by brownieParser#fun_sentence2.
    def visitFun_sentence2(self, ctx:brownieParser.Fun_sentence2Context):
        inst = ins()
        inst.i1 = f"PUSH"
        inst.i2 = self.visit(ctx.exp()).i1

        self.instructions.append(inst)
        inst.pos = len(self.instructions) - 1
        return  inst
    # Visit a parse tree produced by brownieParser#parameter2.
    def visitParameter2(self, ctx: brownieParser.Parameter2Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by brownieParser#parameter1.
    def visitParameter1(self, ctx: brownieParser.Parameter1Context):
        inst = ins()
        inst.i1 = f"POP"
        inst.i2 = str(ctx.VARIABLE())

        self.instructions.append(inst)
        inst.pos = len(self.instructions) - 1
        return  inst

    # Visit a parse tree produced by brownieParser#fun_body.
    def visitFun_body(self, ctx: brownieParser.Fun_bodyContext):
        # Inicio de body
        #l1 = self.label()

        # Contenido
        self.visitChildren(ctx)

        # Fin de body
        l2 = self.label()

        return l2

    # Visit a parse tree produced by brownieParser#fun_sentence.
    def visitFun_sentence(self, ctx: brownieParser.Fun_sentenceContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by brownieParser#print_.
    def visitPrint_(self, ctx: brownieParser.Print_Context):
        inst = ins()
        inst.i1 = f"print"
        inst.i2 = self.visit(ctx.print_value()).i1
        self.instructions.append(inst)
        inst.pos = len(self.instructions) - 1

    # Visit a parse tree produced by brownieParser#print_value.
    def visitPrint_value(self, ctx: brownieParser.Print_valueContext):
        try:
            aux = self.visit(ctx.list_elements())
            return aux
        except AttributeError:
            pass
        # Auxiliar de retorno
        aux = ins()
        aux.i1 = str(ctx.getText())
        return aux

    # Visit a parse tree produced by brownieParser#procedure.
    def visitProcedure(self, ctx: brownieParser.ProcedureContext):
        inst = ins()
        inst.i1 = "SLICE"
        self.instructions.append(inst)
        inst.pos = len(self.instructions) - 1

        L1, L2 = self.visit(ctx.body())

        inst.i2 = L1.i2
        inst.i3 = L2.i2

    def label(self, label=""):
        label1 = ins()
        self.add_count()  # self.count = self.count + 1
        label1.i1 = f"LABEL"
        if label != "":
            label1.i2 = label
        else:
            label1.i2 = f"<L{self.label_count}>"
            self.label_count = self.label_count + 1
        self.instructions.append(label1)
        label1.pos = len(self.instructions) - 1
        return label1

    def goto(self, label):
        goto = ins()
        self.add_count()  # self.count = self.count + 1
        goto.i1 = f"goto"
        goto.i2 = label
        self.instructions.append(goto)
        goto.pos = len(self.instructions) - 1
        return goto

    def add_count(self):
        if self.count < 1:
            self.count = self.count + 1
        else:
            self.count = 0
