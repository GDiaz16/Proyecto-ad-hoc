# Generated from E:/Universidad/Materias/Lenguajes de Programación/Proyecto/Compiler\brownie_grammar.g4 by ANTLR 4.7.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\5")
        buf.write("\t\4\2\t\2\3\2\3\2\3\2\3\2\3\2\2\2\3\2\2\2\2\7\2\4\3\2")
        buf.write("\2\2\4\5\7\4\2\2\5\6\7\3\2\2\6\7\7\4\2\2\7\3\3\2\2\2\2")
        return buf.getvalue()


class brownie_grammarParser ( Parser ):

    grammarFileName = "brownie_grammar.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'+'", "<INVALID>", "' '" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "NUMBER", "WHITESPACE" ]

    RULE_operation = 0

    ruleNames =  [ "operation" ]

    EOF = Token.EOF
    T__0=1
    NUMBER=2
    WHITESPACE=3

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class OperationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self, i:int=None):
            if i is None:
                return self.getTokens(brownie_grammarParser.NUMBER)
            else:
                return self.getToken(brownie_grammarParser.NUMBER, i)

        def getRuleIndex(self):
            return brownie_grammarParser.RULE_operation

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOperation" ):
                listener.enterOperation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOperation" ):
                listener.exitOperation(self)




    def operation(self):

        localctx = brownie_grammarParser.OperationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_operation)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2
            self.match(brownie_grammarParser.NUMBER)
            self.state = 3
            self.match(brownie_grammarParser.T__0)
            self.state = 4
            self.match(brownie_grammarParser.NUMBER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





