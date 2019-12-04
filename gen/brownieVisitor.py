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


    # Visit a parse tree produced by brownieParser#function.
    def visitFunction(self, ctx:brownieParser.FunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by brownieParser#call.
    def visitCall(self, ctx:brownieParser.CallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by brownieParser#call_sentence.
    def visitCall_sentence(self, ctx:brownieParser.Call_sentenceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by brownieParser#parameter.
    def visitParameter(self, ctx:brownieParser.ParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by brownieParser#parameter_call6.
    def visitParameter_call6(self, ctx:brownieParser.Parameter_call6Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by brownieParser#parameter_call4.
    def visitParameter_call4(self, ctx:brownieParser.Parameter_call4Context):
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


    # Visit a parse tree produced by brownieParser#ar_value3.
    def visitAr_value3(self, ctx:brownieParser.Ar_value3Context):
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


    # Visit a parse tree produced by brownieParser#ar_operator1.
    def visitAr_operator1(self, ctx:brownieParser.Ar_operator1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by brownieParser#ar_operator2.
    def visitAr_operator2(self, ctx:brownieParser.Ar_operator2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by brownieParser#prior_operator1.
    def visitPrior_operator1(self, ctx:brownieParser.Prior_operator1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by brownieParser#prior_operator2.
    def visitPrior_operator2(self, ctx:brownieParser.Prior_operator2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by brownieParser#prior_operator3.
    def visitPrior_operator3(self, ctx:brownieParser.Prior_operator3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by brownieParser#prior_operator4.
    def visitPrior_operator4(self, ctx:brownieParser.Prior_operator4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by brownieParser#conditional.
    def visitConditional(self, ctx:brownieParser.ConditionalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by brownieParser#otherwise.
    def visitOtherwise(self, ctx:brownieParser.OtherwiseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by brownieParser#condition.
    def visitCondition(self, ctx:brownieParser.ConditionContext):
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


    # Visit a parse tree produced by brownieParser#while_.
    def visitWhile_(self, ctx:brownieParser.While_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by brownieParser#for_.
    def visitFor_(self, ctx:brownieParser.For_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by brownieParser#for_condition.
    def visitFor_condition(self, ctx:brownieParser.For_conditionContext):
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


    # Visit a parse tree produced by brownieParser#fun_body.
    def visitFun_body(self, ctx:brownieParser.Fun_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by brownieParser#fun_sentence.
    def visitFun_sentence(self, ctx:brownieParser.Fun_sentenceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by brownieParser#process.
    def visitProcess(self, ctx:brownieParser.ProcessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by brownieParser#concurrency.
    def visitConcurrency(self, ctx:brownieParser.ConcurrencyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by brownieParser#loop.
    def visitLoop(self, ctx:brownieParser.LoopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by brownieParser#exec.
    def visitExec(self, ctx:brownieParser.ExecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by brownieParser#start_process.
    def visitStart_process(self, ctx:brownieParser.Start_processContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by brownieParser#stop.
    def visitStop(self, ctx:brownieParser.StopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by brownieParser#message.
    def visitMessage(self, ctx:brownieParser.MessageContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by brownieParser#dictionary.
    def visitDictionary(self, ctx:brownieParser.DictionaryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by brownieParser#dict_element.
    def visitDict_element(self, ctx:brownieParser.Dict_elementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by brownieParser#dict_value.
    def visitDict_value(self, ctx:brownieParser.Dict_valueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by brownieParser#switch_.
    def visitSwitch_(self, ctx:brownieParser.Switch_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by brownieParser#switch_body.
    def visitSwitch_body(self, ctx:brownieParser.Switch_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by brownieParser#case_.
    def visitCase_(self, ctx:brownieParser.Case_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by brownieParser#default_.
    def visitDefault_(self, ctx:brownieParser.Default_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by brownieParser#case_value.
    def visitCase_value(self, ctx:brownieParser.Case_valueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by brownieParser#break_.
    def visitBreak_(self, ctx:brownieParser.Break_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by brownieParser#element.
    def visitElement(self, ctx:brownieParser.ElementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by brownieParser#list_elements.
    def visitList_elements(self, ctx:brownieParser.List_elementsContext):
        return self.visitChildren(ctx)



del brownieParser