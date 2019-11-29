# Generated from E:/Universidad/Materias/Lenguajes de Programación/Proyecto/Compiler\brownie_grammar.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .brownie_grammarParser import brownie_grammarParser
else:
    from brownie_grammarParser import brownie_grammarParser

# This class defines a complete listener for a parse tree produced by brownie_grammarParser.
class brownie_grammarListener(ParseTreeListener):

    # Enter a parse tree produced by brownie_grammarParser#start.
    def enterStart(self, ctx:brownie_grammarParser.StartContext):
        pass

    # Exit a parse tree produced by brownie_grammarParser#start.
    def exitStart(self, ctx:brownie_grammarParser.StartContext):
        pass


    # Enter a parse tree produced by brownie_grammarParser#structure.
    def enterStructure(self, ctx:brownie_grammarParser.StructureContext):
        pass

    # Exit a parse tree produced by brownie_grammarParser#structure.
    def exitStructure(self, ctx:brownie_grammarParser.StructureContext):
        pass


    # Enter a parse tree produced by brownie_grammarParser#sentence.
    def enterSentence(self, ctx:brownie_grammarParser.SentenceContext):
        pass

    # Exit a parse tree produced by brownie_grammarParser#sentence.
    def exitSentence(self, ctx:brownie_grammarParser.SentenceContext):
        pass


    # Enter a parse tree produced by brownie_grammarParser#function.
    def enterFunction(self, ctx:brownie_grammarParser.FunctionContext):
        pass

    # Exit a parse tree produced by brownie_grammarParser#function.
    def exitFunction(self, ctx:brownie_grammarParser.FunctionContext):
        pass


    # Enter a parse tree produced by brownie_grammarParser#call.
    def enterCall(self, ctx:brownie_grammarParser.CallContext):
        pass

    # Exit a parse tree produced by brownie_grammarParser#call.
    def exitCall(self, ctx:brownie_grammarParser.CallContext):
        pass


    # Enter a parse tree produced by brownie_grammarParser#call_sentence.
    def enterCall_sentence(self, ctx:brownie_grammarParser.Call_sentenceContext):
        pass

    # Exit a parse tree produced by brownie_grammarParser#call_sentence.
    def exitCall_sentence(self, ctx:brownie_grammarParser.Call_sentenceContext):
        pass


    # Enter a parse tree produced by brownie_grammarParser#parameter.
    def enterParameter(self, ctx:brownie_grammarParser.ParameterContext):
        pass

    # Exit a parse tree produced by brownie_grammarParser#parameter.
    def exitParameter(self, ctx:brownie_grammarParser.ParameterContext):
        pass


    # Enter a parse tree produced by brownie_grammarParser#parameter_call.
    def enterParameter_call(self, ctx:brownie_grammarParser.Parameter_callContext):
        pass

    # Exit a parse tree produced by brownie_grammarParser#parameter_call.
    def exitParameter_call(self, ctx:brownie_grammarParser.Parameter_callContext):
        pass


    # Enter a parse tree produced by brownie_grammarParser#definition.
    def enterDefinition(self, ctx:brownie_grammarParser.DefinitionContext):
        pass

    # Exit a parse tree produced by brownie_grammarParser#definition.
    def exitDefinition(self, ctx:brownie_grammarParser.DefinitionContext):
        pass


    # Enter a parse tree produced by brownie_grammarParser#exp.
    def enterExp(self, ctx:brownie_grammarParser.ExpContext):
        pass

    # Exit a parse tree produced by brownie_grammarParser#exp.
    def exitExp(self, ctx:brownie_grammarParser.ExpContext):
        pass


    # Enter a parse tree produced by brownie_grammarParser#ar_value.
    def enterAr_value(self, ctx:brownie_grammarParser.Ar_valueContext):
        pass

    # Exit a parse tree produced by brownie_grammarParser#ar_value.
    def exitAr_value(self, ctx:brownie_grammarParser.Ar_valueContext):
        pass


    # Enter a parse tree produced by brownie_grammarParser#ar_operator.
    def enterAr_operator(self, ctx:brownie_grammarParser.Ar_operatorContext):
        pass

    # Exit a parse tree produced by brownie_grammarParser#ar_operator.
    def exitAr_operator(self, ctx:brownie_grammarParser.Ar_operatorContext):
        pass


    # Enter a parse tree produced by brownie_grammarParser#conditional.
    def enterConditional(self, ctx:brownie_grammarParser.ConditionalContext):
        pass

    # Exit a parse tree produced by brownie_grammarParser#conditional.
    def exitConditional(self, ctx:brownie_grammarParser.ConditionalContext):
        pass


    # Enter a parse tree produced by brownie_grammarParser#otherwise.
    def enterOtherwise(self, ctx:brownie_grammarParser.OtherwiseContext):
        pass

    # Exit a parse tree produced by brownie_grammarParser#otherwise.
    def exitOtherwise(self, ctx:brownie_grammarParser.OtherwiseContext):
        pass


    # Enter a parse tree produced by brownie_grammarParser#condition.
    def enterCondition(self, ctx:brownie_grammarParser.ConditionContext):
        pass

    # Exit a parse tree produced by brownie_grammarParser#condition.
    def exitCondition(self, ctx:brownie_grammarParser.ConditionContext):
        pass


    # Enter a parse tree produced by brownie_grammarParser#com_value.
    def enterCom_value(self, ctx:brownie_grammarParser.Com_valueContext):
        pass

    # Exit a parse tree produced by brownie_grammarParser#com_value.
    def exitCom_value(self, ctx:brownie_grammarParser.Com_valueContext):
        pass


    # Enter a parse tree produced by brownie_grammarParser#comparator.
    def enterComparator(self, ctx:brownie_grammarParser.ComparatorContext):
        pass

    # Exit a parse tree produced by brownie_grammarParser#comparator.
    def exitComparator(self, ctx:brownie_grammarParser.ComparatorContext):
        pass


    # Enter a parse tree produced by brownie_grammarParser#loop.
    def enterLoop(self, ctx:brownie_grammarParser.LoopContext):
        pass

    # Exit a parse tree produced by brownie_grammarParser#loop.
    def exitLoop(self, ctx:brownie_grammarParser.LoopContext):
        pass


    # Enter a parse tree produced by brownie_grammarParser#while_.
    def enterWhile_(self, ctx:brownie_grammarParser.While_Context):
        pass

    # Exit a parse tree produced by brownie_grammarParser#while_.
    def exitWhile_(self, ctx:brownie_grammarParser.While_Context):
        pass


    # Enter a parse tree produced by brownie_grammarParser#for_.
    def enterFor_(self, ctx:brownie_grammarParser.For_Context):
        pass

    # Exit a parse tree produced by brownie_grammarParser#for_.
    def exitFor_(self, ctx:brownie_grammarParser.For_Context):
        pass


    # Enter a parse tree produced by brownie_grammarParser#for_condition.
    def enterFor_condition(self, ctx:brownie_grammarParser.For_conditionContext):
        pass

    # Exit a parse tree produced by brownie_grammarParser#for_condition.
    def exitFor_condition(self, ctx:brownie_grammarParser.For_conditionContext):
        pass


    # Enter a parse tree produced by brownie_grammarParser#for_def.
    def enterFor_def(self, ctx:brownie_grammarParser.For_defContext):
        pass

    # Exit a parse tree produced by brownie_grammarParser#for_def.
    def exitFor_def(self, ctx:brownie_grammarParser.For_defContext):
        pass


    # Enter a parse tree produced by brownie_grammarParser#body.
    def enterBody(self, ctx:brownie_grammarParser.BodyContext):
        pass

    # Exit a parse tree produced by brownie_grammarParser#body.
    def exitBody(self, ctx:brownie_grammarParser.BodyContext):
        pass


    # Enter a parse tree produced by brownie_grammarParser#fun_body.
    def enterFun_body(self, ctx:brownie_grammarParser.Fun_bodyContext):
        pass

    # Exit a parse tree produced by brownie_grammarParser#fun_body.
    def exitFun_body(self, ctx:brownie_grammarParser.Fun_bodyContext):
        pass


    # Enter a parse tree produced by brownie_grammarParser#fun_sentence.
    def enterFun_sentence(self, ctx:brownie_grammarParser.Fun_sentenceContext):
        pass

    # Exit a parse tree produced by brownie_grammarParser#fun_sentence.
    def exitFun_sentence(self, ctx:brownie_grammarParser.Fun_sentenceContext):
        pass


    # Enter a parse tree produced by brownie_grammarParser#element.
    def enterElement(self, ctx:brownie_grammarParser.ElementContext):
        pass

    # Exit a parse tree produced by brownie_grammarParser#element.
    def exitElement(self, ctx:brownie_grammarParser.ElementContext):
        pass


    # Enter a parse tree produced by brownie_grammarParser#list_elements.
    def enterList_elements(self, ctx:brownie_grammarParser.List_elementsContext):
        pass

    # Exit a parse tree produced by brownie_grammarParser#list_elements.
    def exitList_elements(self, ctx:brownie_grammarParser.List_elementsContext):
        pass


    # Enter a parse tree produced by brownie_grammarParser#logic.
    def enterLogic(self, ctx:brownie_grammarParser.LogicContext):
        pass

    # Exit a parse tree produced by brownie_grammarParser#logic.
    def exitLogic(self, ctx:brownie_grammarParser.LogicContext):
        pass


