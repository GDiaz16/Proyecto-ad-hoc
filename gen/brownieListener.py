# Generated from E:/Universidad/Materias/Lenguajes de Programación/Proyecto/Compiler\brownie.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .brownieParser import brownieParser
else:
    from brownieParser import brownieParser

# This class defines a complete listener for a parse tree produced by brownieParser.
class brownieListener(ParseTreeListener):

    # Enter a parse tree produced by brownieParser#start.
    def enterStart(self, ctx:brownieParser.StartContext):
        pass

    # Exit a parse tree produced by brownieParser#start.
    def exitStart(self, ctx:brownieParser.StartContext):
        pass


    # Enter a parse tree produced by brownieParser#structure.
    def enterStructure(self, ctx:brownieParser.StructureContext):
        pass

    # Exit a parse tree produced by brownieParser#structure.
    def exitStructure(self, ctx:brownieParser.StructureContext):
        pass


    # Enter a parse tree produced by brownieParser#sentence.
    def enterSentence(self, ctx:brownieParser.SentenceContext):
        pass

    # Exit a parse tree produced by brownieParser#sentence.
    def exitSentence(self, ctx:brownieParser.SentenceContext):
        pass


    # Enter a parse tree produced by brownieParser#function.
    def enterFunction(self, ctx:brownieParser.FunctionContext):
        pass

    # Exit a parse tree produced by brownieParser#function.
    def exitFunction(self, ctx:brownieParser.FunctionContext):
        pass


    # Enter a parse tree produced by brownieParser#call.
    def enterCall(self, ctx:brownieParser.CallContext):
        pass

    # Exit a parse tree produced by brownieParser#call.
    def exitCall(self, ctx:brownieParser.CallContext):
        pass


    # Enter a parse tree produced by brownieParser#call_sentence.
    def enterCall_sentence(self, ctx:brownieParser.Call_sentenceContext):
        pass

    # Exit a parse tree produced by brownieParser#call_sentence.
    def exitCall_sentence(self, ctx:brownieParser.Call_sentenceContext):
        pass


    # Enter a parse tree produced by brownieParser#parameter.
    def enterParameter(self, ctx:brownieParser.ParameterContext):
        pass

    # Exit a parse tree produced by brownieParser#parameter.
    def exitParameter(self, ctx:brownieParser.ParameterContext):
        pass


    # Enter a parse tree produced by brownieParser#parameter_call.
    def enterParameter_call(self, ctx:brownieParser.Parameter_callContext):
        pass

    # Exit a parse tree produced by brownieParser#parameter_call.
    def exitParameter_call(self, ctx:brownieParser.Parameter_callContext):
        pass


    # Enter a parse tree produced by brownieParser#definition.
    def enterDefinition(self, ctx:brownieParser.DefinitionContext):
        pass

    # Exit a parse tree produced by brownieParser#definition.
    def exitDefinition(self, ctx:brownieParser.DefinitionContext):
        pass


    # Enter a parse tree produced by brownieParser#assign.
    def enterAssign(self, ctx:brownieParser.AssignContext):
        pass

    # Exit a parse tree produced by brownieParser#assign.
    def exitAssign(self, ctx:brownieParser.AssignContext):
        pass


    # Enter a parse tree produced by brownieParser#exp.
    def enterExp(self, ctx:brownieParser.ExpContext):
        pass

    # Exit a parse tree produced by brownieParser#exp.
    def exitExp(self, ctx:brownieParser.ExpContext):
        pass


    # Enter a parse tree produced by brownieParser#term.
    def enterTerm(self, ctx:brownieParser.TermContext):
        pass

    # Exit a parse tree produced by brownieParser#term.
    def exitTerm(self, ctx:brownieParser.TermContext):
        pass


    # Enter a parse tree produced by brownieParser#ar_value.
    def enterAr_value(self, ctx:brownieParser.Ar_valueContext):
        pass

    # Exit a parse tree produced by brownieParser#ar_value.
    def exitAr_value(self, ctx:brownieParser.Ar_valueContext):
        pass


    # Enter a parse tree produced by brownieParser#ar_operator.
    def enterAr_operator(self, ctx:brownieParser.Ar_operatorContext):
        pass

    # Exit a parse tree produced by brownieParser#ar_operator.
    def exitAr_operator(self, ctx:brownieParser.Ar_operatorContext):
        pass


    # Enter a parse tree produced by brownieParser#prior_operator.
    def enterPrior_operator(self, ctx:brownieParser.Prior_operatorContext):
        pass

    # Exit a parse tree produced by brownieParser#prior_operator.
    def exitPrior_operator(self, ctx:brownieParser.Prior_operatorContext):
        pass


    # Enter a parse tree produced by brownieParser#conditional.
    def enterConditional(self, ctx:brownieParser.ConditionalContext):
        pass

    # Exit a parse tree produced by brownieParser#conditional.
    def exitConditional(self, ctx:brownieParser.ConditionalContext):
        pass


    # Enter a parse tree produced by brownieParser#otherwise.
    def enterOtherwise(self, ctx:brownieParser.OtherwiseContext):
        pass

    # Exit a parse tree produced by brownieParser#otherwise.
    def exitOtherwise(self, ctx:brownieParser.OtherwiseContext):
        pass


    # Enter a parse tree produced by brownieParser#condition.
    def enterCondition(self, ctx:brownieParser.ConditionContext):
        pass

    # Exit a parse tree produced by brownieParser#condition.
    def exitCondition(self, ctx:brownieParser.ConditionContext):
        pass


    # Enter a parse tree produced by brownieParser#com_value.
    def enterCom_value(self, ctx:brownieParser.Com_valueContext):
        pass

    # Exit a parse tree produced by brownieParser#com_value.
    def exitCom_value(self, ctx:brownieParser.Com_valueContext):
        pass


    # Enter a parse tree produced by brownieParser#comparator.
    def enterComparator(self, ctx:brownieParser.ComparatorContext):
        pass

    # Exit a parse tree produced by brownieParser#comparator.
    def exitComparator(self, ctx:brownieParser.ComparatorContext):
        pass


    # Enter a parse tree produced by brownieParser#cycle.
    def enterCycle(self, ctx:brownieParser.CycleContext):
        pass

    # Exit a parse tree produced by brownieParser#cycle.
    def exitCycle(self, ctx:brownieParser.CycleContext):
        pass


    # Enter a parse tree produced by brownieParser#while_.
    def enterWhile_(self, ctx:brownieParser.While_Context):
        pass

    # Exit a parse tree produced by brownieParser#while_.
    def exitWhile_(self, ctx:brownieParser.While_Context):
        pass


    # Enter a parse tree produced by brownieParser#for_.
    def enterFor_(self, ctx:brownieParser.For_Context):
        pass

    # Exit a parse tree produced by brownieParser#for_.
    def exitFor_(self, ctx:brownieParser.For_Context):
        pass


    # Enter a parse tree produced by brownieParser#for_condition.
    def enterFor_condition(self, ctx:brownieParser.For_conditionContext):
        pass

    # Exit a parse tree produced by brownieParser#for_condition.
    def exitFor_condition(self, ctx:brownieParser.For_conditionContext):
        pass


    # Enter a parse tree produced by brownieParser#for_definition.
    def enterFor_definition(self, ctx:brownieParser.For_definitionContext):
        pass

    # Exit a parse tree produced by brownieParser#for_definition.
    def exitFor_definition(self, ctx:brownieParser.For_definitionContext):
        pass


    # Enter a parse tree produced by brownieParser#for_iterator.
    def enterFor_iterator(self, ctx:brownieParser.For_iteratorContext):
        pass

    # Exit a parse tree produced by brownieParser#for_iterator.
    def exitFor_iterator(self, ctx:brownieParser.For_iteratorContext):
        pass


    # Enter a parse tree produced by brownieParser#body.
    def enterBody(self, ctx:brownieParser.BodyContext):
        pass

    # Exit a parse tree produced by brownieParser#body.
    def exitBody(self, ctx:brownieParser.BodyContext):
        pass


    # Enter a parse tree produced by brownieParser#fun_body.
    def enterFun_body(self, ctx:brownieParser.Fun_bodyContext):
        pass

    # Exit a parse tree produced by brownieParser#fun_body.
    def exitFun_body(self, ctx:brownieParser.Fun_bodyContext):
        pass


    # Enter a parse tree produced by brownieParser#fun_sentence.
    def enterFun_sentence(self, ctx:brownieParser.Fun_sentenceContext):
        pass

    # Exit a parse tree produced by brownieParser#fun_sentence.
    def exitFun_sentence(self, ctx:brownieParser.Fun_sentenceContext):
        pass


    # Enter a parse tree produced by brownieParser#process.
    def enterProcess(self, ctx:brownieParser.ProcessContext):
        pass

    # Exit a parse tree produced by brownieParser#process.
    def exitProcess(self, ctx:brownieParser.ProcessContext):
        pass


    # Enter a parse tree produced by brownieParser#concurrency.
    def enterConcurrency(self, ctx:brownieParser.ConcurrencyContext):
        pass

    # Exit a parse tree produced by brownieParser#concurrency.
    def exitConcurrency(self, ctx:brownieParser.ConcurrencyContext):
        pass


    # Enter a parse tree produced by brownieParser#loop.
    def enterLoop(self, ctx:brownieParser.LoopContext):
        pass

    # Exit a parse tree produced by brownieParser#loop.
    def exitLoop(self, ctx:brownieParser.LoopContext):
        pass


    # Enter a parse tree produced by brownieParser#exec.
    def enterExec(self, ctx:brownieParser.ExecContext):
        pass

    # Exit a parse tree produced by brownieParser#exec.
    def exitExec(self, ctx:brownieParser.ExecContext):
        pass


    # Enter a parse tree produced by brownieParser#start_process.
    def enterStart_process(self, ctx:brownieParser.Start_processContext):
        pass

    # Exit a parse tree produced by brownieParser#start_process.
    def exitStart_process(self, ctx:brownieParser.Start_processContext):
        pass


    # Enter a parse tree produced by brownieParser#stop.
    def enterStop(self, ctx:brownieParser.StopContext):
        pass

    # Exit a parse tree produced by brownieParser#stop.
    def exitStop(self, ctx:brownieParser.StopContext):
        pass


    # Enter a parse tree produced by brownieParser#message.
    def enterMessage(self, ctx:brownieParser.MessageContext):
        pass

    # Exit a parse tree produced by brownieParser#message.
    def exitMessage(self, ctx:brownieParser.MessageContext):
        pass


    # Enter a parse tree produced by brownieParser#dictionary.
    def enterDictionary(self, ctx:brownieParser.DictionaryContext):
        pass

    # Exit a parse tree produced by brownieParser#dictionary.
    def exitDictionary(self, ctx:brownieParser.DictionaryContext):
        pass


    # Enter a parse tree produced by brownieParser#dict_element.
    def enterDict_element(self, ctx:brownieParser.Dict_elementContext):
        pass

    # Exit a parse tree produced by brownieParser#dict_element.
    def exitDict_element(self, ctx:brownieParser.Dict_elementContext):
        pass


    # Enter a parse tree produced by brownieParser#dict_value.
    def enterDict_value(self, ctx:brownieParser.Dict_valueContext):
        pass

    # Exit a parse tree produced by brownieParser#dict_value.
    def exitDict_value(self, ctx:brownieParser.Dict_valueContext):
        pass


    # Enter a parse tree produced by brownieParser#switch_.
    def enterSwitch_(self, ctx:brownieParser.Switch_Context):
        pass

    # Exit a parse tree produced by brownieParser#switch_.
    def exitSwitch_(self, ctx:brownieParser.Switch_Context):
        pass


    # Enter a parse tree produced by brownieParser#switch_body.
    def enterSwitch_body(self, ctx:brownieParser.Switch_bodyContext):
        pass

    # Exit a parse tree produced by brownieParser#switch_body.
    def exitSwitch_body(self, ctx:brownieParser.Switch_bodyContext):
        pass


    # Enter a parse tree produced by brownieParser#case_.
    def enterCase_(self, ctx:brownieParser.Case_Context):
        pass

    # Exit a parse tree produced by brownieParser#case_.
    def exitCase_(self, ctx:brownieParser.Case_Context):
        pass


    # Enter a parse tree produced by brownieParser#default_.
    def enterDefault_(self, ctx:brownieParser.Default_Context):
        pass

    # Exit a parse tree produced by brownieParser#default_.
    def exitDefault_(self, ctx:brownieParser.Default_Context):
        pass


    # Enter a parse tree produced by brownieParser#case_value.
    def enterCase_value(self, ctx:brownieParser.Case_valueContext):
        pass

    # Exit a parse tree produced by brownieParser#case_value.
    def exitCase_value(self, ctx:brownieParser.Case_valueContext):
        pass


    # Enter a parse tree produced by brownieParser#break_.
    def enterBreak_(self, ctx:brownieParser.Break_Context):
        pass

    # Exit a parse tree produced by brownieParser#break_.
    def exitBreak_(self, ctx:brownieParser.Break_Context):
        pass


    # Enter a parse tree produced by brownieParser#element.
    def enterElement(self, ctx:brownieParser.ElementContext):
        pass

    # Exit a parse tree produced by brownieParser#element.
    def exitElement(self, ctx:brownieParser.ElementContext):
        pass


    # Enter a parse tree produced by brownieParser#list_elements.
    def enterList_elements(self, ctx:brownieParser.List_elementsContext):
        pass

    # Exit a parse tree produced by brownieParser#list_elements.
    def exitList_elements(self, ctx:brownieParser.List_elementsContext):
        pass


    # Enter a parse tree produced by brownieParser#logic.
    def enterLogic(self, ctx:brownieParser.LogicContext):
        pass

    # Exit a parse tree produced by brownieParser#logic.
    def exitLogic(self, ctx:brownieParser.LogicContext):
        pass


