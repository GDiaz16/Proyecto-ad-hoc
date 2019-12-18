# Generated from E:/Universidad/Materias/Lenguajes de Programación/Proyecto/Compiler\brownie.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .brownieParser import brownieParser
else:
    from brownieParser import brownieParser

# This class defines a complete generic visitor for a parse tree produced by brownieParser.

class brownieVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by brownieParser#start.
    def visitStart(self, ctx:brownieParser.StartContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by brownieParser#structure.
    def visitStructure(self, ctx:brownieParser.StructureContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by brownieParser#sentence.
    def visitSentence(self, ctx:brownieParser.SentenceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by brownieParser#parameter2.
    def visitParameter2(self, ctx:brownieParser.Parameter2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by brownieParser#parameter1.
    def visitParameter1(self, ctx:brownieParser.Parameter1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by brownieParser#parameter_call6.
    def visitParameter_call6(self, ctx:brownieParser.Parameter_call6Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by brownieParser#parameter_call5.
    def visitParameter_call5(self, ctx:brownieParser.Parameter_call5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by brownieParser#parameter_call2.
    def visitParameter_call2(self, ctx:brownieParser.Parameter_call2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by brownieParser#parameter_call3.
    def visitParameter_call3(self, ctx:brownieParser.Parameter_call3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by brownieParser#parameter_call1.
    def visitParameter_call1(self, ctx:brownieParser.Parameter_call1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by brownieParser#definition.
    def visitDefinition(self, ctx:brownieParser.DefinitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by brownieParser#assign1.
    def visitAssign1(self, ctx:brownieParser.Assign1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by brownieParser#assign2.
    def visitAssign2(self, ctx:brownieParser.Assign2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by brownieParser#assign3.
    def visitAssign3(self, ctx:brownieParser.Assign3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by brownieParser#assign4.
    def visitAssign4(self, ctx:brownieParser.Assign4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by brownieParser#assign5.
    def visitAssign5(self, ctx:brownieParser.Assign5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by brownieParser#assign6.
    def visitAssign6(self, ctx:brownieParser.Assign6Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by brownieParser#text3.
    def visitText3(self, ctx:brownieParser.Text3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by brownieParser#text1.
    def visitText1(self, ctx:brownieParser.Text1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by brownieParser#text2.
    def visitText2(self, ctx:brownieParser.Text2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by brownieParser#element1.
    def visitElement1(self, ctx:brownieParser.Element1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by brownieParser#element2.
    def visitElement2(self, ctx:brownieParser.Element2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by brownieParser#element3.
    def visitElement3(self, ctx:brownieParser.Element3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by brownieParser#element4.
    def visitElement4(self, ctx:brownieParser.Element4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by brownieParser#list_elements.
    def visitList_elements(self, ctx:brownieParser.List_elementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by brownieParser#exp2.
    def visitExp2(self, ctx:brownieParser.Exp2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by brownieParser#exp1.
    def visitExp1(self, ctx:brownieParser.Exp1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by brownieParser#term1.
    def visitTerm1(self, ctx:brownieParser.Term1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by brownieParser#term2.
    def visitTerm2(self, ctx:brownieParser.Term2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by brownieParser#ar_value1.
    def visitAr_value1(self, ctx:brownieParser.Ar_value1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by brownieParser#ar_value2.
    def visitAr_value2(self, ctx:brownieParser.Ar_value2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by brownieParser#ar_value4.
    def visitAr_value4(self, ctx:brownieParser.Ar_value4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by brownieParser#ar_value5.
    def visitAr_value5(self, ctx:brownieParser.Ar_value5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by brownieParser#array_call.
    def visitArray_call(self, ctx:brownieParser.Array_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by brownieParser#ar_operator.
    def visitAr_operator(self, ctx:brownieParser.Ar_operatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by brownieParser#prior_operator.
    def visitPrior_operator(self, ctx:brownieParser.Prior_operatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by brownieParser#conditional.
    def visitConditional(self, ctx:brownieParser.ConditionalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by brownieParser#otherwise1.
    def visitOtherwise1(self, ctx:brownieParser.Otherwise1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by brownieParser#otherwise2.
    def visitOtherwise2(self, ctx:brownieParser.Otherwise2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by brownieParser#condition1.
    def visitCondition1(self, ctx:brownieParser.Condition1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by brownieParser#condition2.
    def visitCondition2(self, ctx:brownieParser.Condition2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by brownieParser#other_cond.
    def visitOther_cond(self, ctx:brownieParser.Other_condContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by brownieParser#other_condition1.
    def visitOther_condition1(self, ctx:brownieParser.Other_condition1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by brownieParser#other_condition2.
    def visitOther_condition2(self, ctx:brownieParser.Other_condition2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by brownieParser#com_value.
    def visitCom_value(self, ctx:brownieParser.Com_valueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by brownieParser#comparator.
    def visitComparator(self, ctx:brownieParser.ComparatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by brownieParser#logic.
    def visitLogic(self, ctx:brownieParser.LogicContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by brownieParser#cycle.
    def visitCycle(self, ctx:brownieParser.CycleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by brownieParser#do_while.
    def visitDo_while(self, ctx:brownieParser.Do_whileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by brownieParser#while_.
    def visitWhile_(self, ctx:brownieParser.While_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by brownieParser#for_.
    def visitFor_(self, ctx:brownieParser.For_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by brownieParser#for_condition1.
    def visitFor_condition1(self, ctx:brownieParser.For_condition1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by brownieParser#for_condition2.
    def visitFor_condition2(self, ctx:brownieParser.For_condition2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by brownieParser#for_definition.
    def visitFor_definition(self, ctx:brownieParser.For_definitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by brownieParser#for_iterator.
    def visitFor_iterator(self, ctx:brownieParser.For_iteratorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by brownieParser#body.
    def visitBody(self, ctx:brownieParser.BodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by brownieParser#procedure.
    def visitProcedure(self, ctx:brownieParser.ProcedureContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by brownieParser#concurrency.
    def visitConcurrency(self, ctx:brownieParser.ConcurrencyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by brownieParser#start_process.
    def visitStart_process(self, ctx:brownieParser.Start_processContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by brownieParser#print_.
    def visitPrint_(self, ctx:brownieParser.Print_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by brownieParser#print_value.
    def visitPrint_value(self, ctx:brownieParser.Print_valueContext):
        return self.visitChildren(ctx)



del brownieParser