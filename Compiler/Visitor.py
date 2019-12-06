from gen import brownieParser
from gen.brownieVisitor import brownieVisitor
from gen.brownieParser import brownieParser
from Compiler.Instruction import instruction as ins


class Visitor(brownieVisitor):
    def __init__(self):
        self.count = 0
        self.label_count = 1
        self.instructions = []

    # Visit a parse tree produced by brownieParser#start.
    def visitStart(self, ctx: brownieParser.StartContext):
        self.visitChildren(ctx)
        # aux = ""
        # for ins in self.instructions:
        #     if ins.i1 == "LABEL":
        #         aux = ins.i2
        #         self.instructions.remove(ins)
        #
        for ins in self.instructions:
            print(ins)

    def visitDefinition(self, ctx: brownieParser.DefinitionContext):
        return self.visit(ctx.assign())

    # Visit a parse tree produced by brownieParser#assign1.
    def visitAssign1(self, ctx: brownieParser.Assign1Context):
        inst = ins()
        self.count = self.count + 1
        inst.i1 = str(ctx.VARIABLE())
        inst.i2 = self.visit(ctx.exp()).i1
        self.instructions.append(inst)
        inst.pos = len(self.instructions) - 1
        return inst

    # Visit a parse tree produced by brownieParser#assign2.
    def visitAssign2(self, ctx: brownieParser.Assign2Context):
        inst = ins()
        self.count = self.count + 1
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
        self.count = self.count + 1
        inst.i1 = str(ctx.VARIABLE())
        inst.i2 = str(ctx.VARIABLE())
        inst.op = '-'
        inst.i3 = 1
        self.instructions.append(inst)
        inst.pos = len(self.instructions) - 1
        return inst

    # Visit a parse tree produced by brownieParser#assign4.
    def visitAssign4(self, ctx:brownieParser.Assign4Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by brownieParser#assign5.
    def visitAssign5(self, ctx:brownieParser.Assign5Context):
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
        self.count = self.count + 1
        inst.i1 = f"t{self.count}"
        inst.i2 = self.visit(ctx.exp()).i1
        inst.op = str(self.visit(ctx.ar_operator()))
        inst.i3 = self.visit(ctx.term()).i1
        self.instructions.append(inst)
        inst.pos = len(self.instructions) - 1
        return inst

    # Visit a parse tree produced by brownieParser#term1.
    def visitTerm1(self, ctx: brownieParser.Term1Context):
        inst = ins()
        self.count = self.count + 1
        inst.i1 = f"t{self.count}"
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
        inst.i1 = ctx.NUMBER()
        return inst

    # Visit a parse tree produced by brownieParser#ar_value2.
    def visitAr_value2(self, ctx: brownieParser.Ar_value2Context):
        inst = ins()
        inst.pos = len(self.instructions) - 1
        inst.i1 = ctx.VARIABLE()
        return inst

    # Visit a parse tree produced by brownieParser#ar_value4.
    def visitAr_value4(self, ctx: brownieParser.Ar_value4Context):
        return self.visit(ctx.exp())

    # Visit a parse tree produced by brownieParser#ar_operator1.
    def visitAr_operator(self, ctx: brownieParser.Ar_operatorContext):
        return ctx.getText()

    # Visit a parse tree produced by brownieParser#prior_operator1.
    def visitPrior_operator(self, ctx: brownieParser.Prior_operatorContext):
        return ctx.getText()

    # Visit a parse tree produced by brownieParser#call.
    def visitCall(self, ctx: brownieParser.CallContext):
        ret = ins()
        inst = ins()
        call = ins()

        # Asignar direccion de retorno
        self.instructions.append(ret)
        ret.pos = len(self.instructions) - 1
        self.count = self.count + 1
        ret.i1 = f"t{self.count}"

        # Apilar la direccion de retorno
        self.instructions.append(inst)
        inst.pos = len(self.instructions) - 1
        #self.count = self.count + 1
        inst.i1 = f"PUSH"
        inst.i2 = ret.i1

        # Apilar parametros
        self.visitChildren(ctx)

        # Llamada a la funcion
        self.instructions.append(call)
        call.pos = len(self.instructions) - 1
        #self.count = self.count + 1
        call.i1 = f"CALL"
        call.i2 = ctx.VARIABLE()

        # Asignar direccion de retorno
        ret.i2 = call.pos + 1

        #Desapilar el valor que devuelve la funcion y devolverlo
        pop_ = ins()
        self.instructions.append(pop_)
        pop_.pos = len(self.instructions) - 1
        self.count = self.count + 1
        pop_.i1 = f"POP"
        pop_.i2 = f"t{self.count}"

        #Auxiliar de retorno
        aux = ins()
        aux.i1 = f"t{self.count}"
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
        inst.i2 = ctx.STRING()
        self.instructions.append(inst)
        inst.pos = len(self.instructions) - 1
        return inst

    # Visit a parse tree produced by brownieParser#parameter_call2.
    def visitParameter_call2(self, ctx: brownieParser.Parameter_call2Context):
        inst = ins()
        inst.i1 = "PUSH"
        inst.i2 = ctx.NUMBER()
        self.instructions.append(inst)
        inst.pos = len(self.instructions) - 1
        return inst

    # Visit a parse tree produced by brownieParser#parameter_call1.
    def visitParameter_call1(self, ctx: brownieParser.Parameter_call1Context):
        inst = ins()
        inst.i1 = "PUSH"
        inst.i2 = ctx.VARIABLE()
        self.instructions.append(inst)
        inst.pos = len(self.instructions) - 1
        return inst

    # Visit a parse tree produced by brownieParser#array_call.
    def visitArray_call(self, ctx:brownieParser.Array_callContext):
        inst = ins()
        self.count = self.count + 1
        inst.i1 = f"t{self.count}"
        inst.i2 = str(ctx.VARIABLE())
        inst.i3 = str(self.visit(ctx.ar_value()).i1)
        inst.array2 = True
        self.instructions.append(inst)
        inst.pos = len(self.instructions) - 1
        return inst

 # Visit a parse tree produced by brownieParser#conditional.
    def visitConditional(self, ctx:brownieParser.ConditionalContext):
        # if (condicion) goto Lv;
        # goto Lf;
        # Lv:
        # < instrucciones >
        # goto Lsalida;
        # Lf:
        # < instrucciones >
        # Lsalida:

        #Insertar if
        if_ = ins()
        if_.i1 = "if"
        if_.i2 = self.visit(ctx.condition()).i1
        if_.op = "goto"
        self.instructions.append(if_)
        if_.pos = len(self.instructions) - 1

        #Insertar salto al else
        els = ins()
        els.i1 = "goto"
        self.instructions.append(els)
        els.pos = len(self.instructions) - 1

        #Asignar el body del if al goto
        L1, L2 = self.visit(ctx.body())
        if_.i3 = L1.i2

        #Asignar la posicion que sigue si no se cumple la condicion
        els.i2 = L2.i2

        #Else y demas condicionales
        try:
            K1 = self.visit(ctx.otherwise())
            els.i2 = K1.i2
        except:
            pass


    # Visit a parse tree produced by brownieParser#otherwise1.
    def visitOtherwise1(self, ctx:brownieParser.Otherwise1Context):
        #Salto para evitar este elif si ya fue cumplido previamente
        goto = self.goto("")
        K1 = self.label()

        #Insertar elif
        if_ = ins()
        if_.i1 = "elif"
        if_.i2 = self.visit(ctx.condition()).i1
        if_.op = "goto"
        self.instructions.append(if_)
        if_.pos = len(self.instructions) - 1

        #Insertar salto al else
        els = ins()
        els.i1 = "goto"
        self.instructions.append(els)
        els.pos = len(self.instructions) - 1

        #Asignar el body del if al goto
        L1, L2 = self.visit(ctx.body())
        if_.i3 = L1.i2
        goto.i2 = L2.i2
        #Asignar la posicion que sigue si no se cumple la condicion
        els.i2 = L2.i2

        #Else y demas condicionales
        try:
            L1 = self.visit(ctx.otherwise())
            els.i2 = L1.i2
        except:
            pass

        return K1


    # Visit a parse tree produced by brownieParser#otherwise2.
    def visitOtherwise2(self, ctx:brownieParser.Otherwise2Context):

        goto = self.goto("")
        L1,L2 = self.visit(ctx.body())
        goto.i2 = L2.i2
        return L1


    # Visit a parse tree produced by brownieParser#other_condition1.
    def visitOther_condition1(self, ctx:brownieParser.Other_condition1Context):
        inst = ins()
        self.count = self.count + 1
        inst.i1 = f"t{self.count}"
        inst.i2 = self.visit(ctx.com_value()).i1
        inst.op = str(self.visit(ctx.comparator()))
        inst.i3 = self.visit(ctx.other_condition()).i1
        self.instructions.append(inst)
        inst.pos = len(self.instructions) - 1
        return inst

    # Visit a parse tree produced by brownieParser#condition1.
    def visitCondition1(self, ctx:brownieParser.Condition1Context):
        inst = ins()
        self.count = self.count + 1
        inst.i1 = f"t{self.count}"
        inst.i2 = self.visit(ctx.condition()).i1
        inst.op = str(self.visit(ctx.logic()))
        inst.i3 = self.visit(ctx.other_condition()).i1
        self.instructions.append(inst)
        inst.pos = len(self.instructions) - 1
        return inst

    # Visit a parse tree produced by brownieParser#com_value.
    def visitCom_value(self, ctx:brownieParser.Com_valueContext):
        try:
            aux = self.visit(ctx.ar_value())
            return aux
        except AttributeError:
            pass
        #Auxiliar de retorno
        aux = ins()
        aux.i1 = ctx.getText()
        return aux

    # Visit a parse tree produced by brownieParser#comparator.
    def visitComparator(self, ctx:brownieParser.ComparatorContext):
        return  ctx.getText()

    # Visit a parse tree produced by brownieParser#logic.
    def visitLogic(self, ctx:brownieParser.LogicContext):
        return ctx.getText()

    # Visit a parse tree produced by brownieParser#body.
    def visitBody(self, ctx:brownieParser.BodyContext):
        #Inicio de body
        l1 = self.label()

        #Contenido
        self.visitChildren(ctx)

        #Fin de body
        l2 = self.label()

        return l1,l2

    def label(self):
        label1 = ins()
        self.count = self.count + 1
        label1.i1 = f"LABEL"
        label1.i2 = f"L{self.label_count}"
        self.instructions.append(label1)
        label1.pos = len(self.instructions) - 1

        #self.instructions[len(self.instructions)-1].label = f"L{self.label_count}"
        self.label_count = self.label_count + 1
        return label1

    def goto(self, label):
        label1 = ins()
        self.count = self.count + 1
        label1.i1 = f"goto"
        label1.i2 = label
        self.instructions.append(label1)
        label1.pos = len(self.instructions) - 1
        return label1