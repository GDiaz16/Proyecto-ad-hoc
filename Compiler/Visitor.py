from gen import brownieParser
from gen.brownieVisitor import brownieVisitor
from gen.brownieParser import brownieParser
from Compiler.Instruction import instruction as ins


class Visitor(brownieVisitor):
    def __init__(self):
        self.count = 0
        self.instructions = []

    # Visit a parse tree produced by brownieParser#start.
    def visitStart(self, ctx: brownieParser.StartContext):
        self.visitChildren(ctx)
        for ins in self.instructions:
            print(ins)

    def visitDefinition(self, ctx: brownieParser.DefinitionContext):
        self.visit(ctx.assign())

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
    def visitAr_operator1(self, ctx: brownieParser.Ar_operator1Context):
        return ctx.getText()

    # Visit a parse tree produced by brownieParser#ar_operator2.
    def visitAr_operator2(self, ctx: brownieParser.Ar_operator2Context):
        return ctx.getText()

    # Visit a parse tree produced by brownieParser#prior_operator1.
    def visitPrior_operator1(self, ctx: brownieParser.Prior_operator1Context):
        return ctx.getText()

    # Visit a parse tree produced by brownieParser#prior_operator2.
    def visitPrior_operator2(self, ctx: brownieParser.Prior_operator2Context):
        return ctx.getText()

    # Visit a parse tree produced by brownieParser#prior_operator3.
    def visitPrior_operator3(self, ctx: brownieParser.Prior_operator3Context):
        return ctx.getText()

    # Visit a parse tree produced by brownieParser#prior_operator4.
    def visitPrior_operator4(self, ctx: brownieParser.Prior_operator4Context):
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
        #self.count = self.count + 1
        pop_.i1 = f"POP"
        pop_.i2 = f"t{self.count}"

        #Auxiliar de retorno
        aux = ins()
        aux.i1 = f"t{self.count}"
        return aux

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
