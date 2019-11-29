# Generated from E:/Universidad/Materias/Lenguajes de Programación/Proyecto/Compiler\brownie_grammar.g4 by ANTLR 4.7.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\60")
        buf.write("\u00f9\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\3\2\6\2")
        buf.write("<\n\2\r\2\16\2=\3\2\3\2\3\3\3\3\3\3\5\3E\n\3\3\4\3\4\3")
        buf.write("\4\3\4\5\4K\n\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3")
        buf.write("\6\3\6\3\6\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\7\bb\n")
        buf.write("\b\f\b\16\be\13\b\3\t\7\th\n\t\f\t\16\tk\13\t\3\t\3\t")
        buf.write("\3\t\3\t\3\t\3\t\3\t\5\tt\n\t\3\n\3\n\3\n\3\n\3\n\3\13")
        buf.write("\3\13\3\13\3\13\3\13\5\13\u0080\n\13\3\f\3\f\3\f\5\f\u0085")
        buf.write("\n\f\3\r\3\r\3\16\3\16\3\16\3\16\3\16\7\16\u008e\n\16")
        buf.write("\f\16\16\16\u0091\13\16\3\17\3\17\3\17\3\17\3\17\3\17")
        buf.write("\3\17\5\17\u009a\n\17\3\20\3\20\3\20\3\20\3\20\3\20\7")
        buf.write("\20\u00a2\n\20\f\20\16\20\u00a5\13\20\3\20\3\20\5\20\u00a9")
        buf.write("\n\20\3\21\3\21\3\21\3\21\3\21\3\21\3\21\5\21\u00b2\n")
        buf.write("\21\3\22\3\22\3\23\3\23\3\24\3\24\5\24\u00ba\n\24\3\24")
        buf.write("\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\27")
        buf.write("\3\27\3\27\3\27\3\30\3\30\7\30\u00cd\n\30\f\30\16\30\u00d0")
        buf.write("\13\30\3\30\3\30\3\31\3\31\7\31\u00d6\n\31\f\31\16\31")
        buf.write("\u00d9\13\31\3\31\3\31\3\32\3\32\3\32\3\32\3\32\5\32\u00e2")
        buf.write("\n\32\3\33\3\33\3\33\5\33\u00e7\n\33\3\33\3\33\3\33\7")
        buf.write("\33\u00ec\n\33\f\33\16\33\u00ef\13\33\3\34\3\34\5\34\u00f3")
        buf.write("\n\34\3\34\3\34\3\35\3\35\3\35\2\4\16\64\36\2\4\6\b\n")
        buf.write("\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64\668\2")
        buf.write("\5\3\2\36\"\3\2&+\3\2#$\2\u00fd\2;\3\2\2\2\4D\3\2\2\2")
        buf.write("\6J\3\2\2\2\bL\3\2\2\2\nS\3\2\2\2\fX\3\2\2\2\16[\3\2\2")
        buf.write("\2\20s\3\2\2\2\22u\3\2\2\2\24\177\3\2\2\2\26\u0084\3\2")
        buf.write("\2\2\30\u0086\3\2\2\2\32\u0088\3\2\2\2\34\u0099\3\2\2")
        buf.write("\2\36\u00a8\3\2\2\2 \u00b1\3\2\2\2\"\u00b3\3\2\2\2$\u00b5")
        buf.write("\3\2\2\2&\u00b9\3\2\2\2(\u00bf\3\2\2\2*\u00c3\3\2\2\2")
        buf.write(",\u00c6\3\2\2\2.\u00ca\3\2\2\2\60\u00d3\3\2\2\2\62\u00e1")
        buf.write("\3\2\2\2\64\u00e6\3\2\2\2\66\u00f0\3\2\2\28\u00f6\3\2")
        buf.write("\2\2:<\5\4\3\2;:\3\2\2\2<=\3\2\2\2=;\3\2\2\2=>\3\2\2\2")
        buf.write(">?\3\2\2\2?@\7\2\2\3@\3\3\2\2\2AE\5\b\5\2BE\5\6\4\2CE")
        buf.write("\5\n\6\2DA\3\2\2\2DB\3\2\2\2DC\3\2\2\2E\5\3\2\2\2FK\5")
        buf.write("\22\n\2GK\5\32\16\2HK\5\f\7\2IK\5$\23\2JF\3\2\2\2JG\3")
        buf.write("\2\2\2JH\3\2\2\2JI\3\2\2\2K\7\3\2\2\2LM\7\16\2\2MN\7\23")
        buf.write("\2\2NO\7\26\2\2OP\5\16\b\2PQ\7\31\2\2QR\5\60\31\2R\t\3")
        buf.write("\2\2\2ST\7\23\2\2TU\7\26\2\2UV\5\20\t\2VW\7\31\2\2W\13")
        buf.write("\3\2\2\2XY\5\n\6\2YZ\7\35\2\2Z\r\3\2\2\2[\\\b\b\1\2\\")
        buf.write("]\7\23\2\2]c\3\2\2\2^_\f\3\2\2_`\7\32\2\2`b\5\16\b\4a")
        buf.write("^\3\2\2\2be\3\2\2\2ca\3\2\2\2cd\3\2\2\2d\17\3\2\2\2ec")
        buf.write("\3\2\2\2fh\7\23\2\2gf\3\2\2\2hk\3\2\2\2ig\3\2\2\2ij\3")
        buf.write("\2\2\2jt\3\2\2\2ki\3\2\2\2lt\7\21\2\2mt\7\22\2\2nt\5\n")
        buf.write("\6\2op\5\16\b\2pq\7\32\2\2qr\5\16\b\2rt\3\2\2\2si\3\2")
        buf.write("\2\2sl\3\2\2\2sm\3\2\2\2sn\3\2\2\2so\3\2\2\2t\21\3\2\2")
        buf.write("\2uv\7\23\2\2vw\7,\2\2wx\5\24\13\2xy\7\35\2\2y\23\3\2")
        buf.write("\2\2z{\5\26\f\2{|\5\30\r\2|}\5\24\13\2}\u0080\3\2\2\2")
        buf.write("~\u0080\5\26\f\2\177z\3\2\2\2\177~\3\2\2\2\u0080\25\3")
        buf.write("\2\2\2\u0081\u0085\7\21\2\2\u0082\u0085\7\23\2\2\u0083")
        buf.write("\u0085\5\n\6\2\u0084\u0081\3\2\2\2\u0084\u0082\3\2\2\2")
        buf.write("\u0084\u0083\3\2\2\2\u0085\27\3\2\2\2\u0086\u0087\t\2")
        buf.write("\2\2\u0087\31\3\2\2\2\u0088\u0089\7\3\2\2\u0089\u008a")
        buf.write("\5\36\20\2\u008a\u008b\7\34\2\2\u008b\u008f\5.\30\2\u008c")
        buf.write("\u008e\5\34\17\2\u008d\u008c\3\2\2\2\u008e\u0091\3\2\2")
        buf.write("\2\u008f\u008d\3\2\2\2\u008f\u0090\3\2\2\2\u0090\33\3")
        buf.write("\2\2\2\u0091\u008f\3\2\2\2\u0092\u0093\7\4\2\2\u0093\u0094")
        buf.write("\5\36\20\2\u0094\u0095\7\34\2\2\u0095\u0096\5.\30\2\u0096")
        buf.write("\u009a\3\2\2\2\u0097\u0098\7\5\2\2\u0098\u009a\5.\30\2")
        buf.write("\u0099\u0092\3\2\2\2\u0099\u0097\3\2\2\2\u009a\35\3\2")
        buf.write("\2\2\u009b\u009c\5 \21\2\u009c\u009d\5\"\22\2\u009d\u00a3")
        buf.write("\5 \21\2\u009e\u009f\58\35\2\u009f\u00a0\5\36\20\2\u00a0")
        buf.write("\u00a2\3\2\2\2\u00a1\u009e\3\2\2\2\u00a2\u00a5\3\2\2\2")
        buf.write("\u00a3\u00a1\3\2\2\2\u00a3\u00a4\3\2\2\2\u00a4\u00a9\3")
        buf.write("\2\2\2\u00a5\u00a3\3\2\2\2\u00a6\u00a9\7\13\2\2\u00a7")
        buf.write("\u00a9\7\f\2\2\u00a8\u009b\3\2\2\2\u00a8\u00a6\3\2\2\2")
        buf.write("\u00a8\u00a7\3\2\2\2\u00a9\37\3\2\2\2\u00aa\u00b2\7\21")
        buf.write("\2\2\u00ab\u00b2\7\23\2\2\u00ac\u00b2\7\22\2\2\u00ad\u00b2")
        buf.write("\3\2\2\2\u00ae\u00b2\7\13\2\2\u00af\u00b2\7\f\2\2\u00b0")
        buf.write("\u00b2\5\n\6\2\u00b1\u00aa\3\2\2\2\u00b1\u00ab\3\2\2\2")
        buf.write("\u00b1\u00ac\3\2\2\2\u00b1\u00ad\3\2\2\2\u00b1\u00ae\3")
        buf.write("\2\2\2\u00b1\u00af\3\2\2\2\u00b1\u00b0\3\2\2\2\u00b2!")
        buf.write("\3\2\2\2\u00b3\u00b4\t\3\2\2\u00b4#\3\2\2\2\u00b5\u00b6")
        buf.write("\5&\24\2\u00b6%\3\2\2\2\u00b7\u00b8\7\n\2\2\u00b8\u00ba")
        buf.write("\5.\30\2\u00b9\u00b7\3\2\2\2\u00b9\u00ba\3\2\2\2\u00ba")
        buf.write("\u00bb\3\2\2\2\u00bb\u00bc\7\b\2\2\u00bc\u00bd\5\36\20")
        buf.write("\2\u00bd\u00be\5.\30\2\u00be\'\3\2\2\2\u00bf\u00c0\7\t")
        buf.write("\2\2\u00c0\u00c1\5*\26\2\u00c1\u00c2\5.\30\2\u00c2)\3")
        buf.write("\2\2\2\u00c3\u00c4\5,\27\2\u00c4\u00c5\7\35\2\2\u00c5")
        buf.write("+\3\2\2\2\u00c6\u00c7\7\23\2\2\u00c7\u00c8\7,\2\2\u00c8")
        buf.write("\u00c9\5\24\13\2\u00c9-\3\2\2\2\u00ca\u00ce\7\25\2\2\u00cb")
        buf.write("\u00cd\5\6\4\2\u00cc\u00cb\3\2\2\2\u00cd\u00d0\3\2\2\2")
        buf.write("\u00ce\u00cc\3\2\2\2\u00ce\u00cf\3\2\2\2\u00cf\u00d1\3")
        buf.write("\2\2\2\u00d0\u00ce\3\2\2\2\u00d1\u00d2\7\30\2\2\u00d2")
        buf.write("/\3\2\2\2\u00d3\u00d7\7\25\2\2\u00d4\u00d6\5\62\32\2\u00d5")
        buf.write("\u00d4\3\2\2\2\u00d6\u00d9\3\2\2\2\u00d7\u00d5\3\2\2\2")
        buf.write("\u00d7\u00d8\3\2\2\2\u00d8\u00da\3\2\2\2\u00d9\u00d7\3")
        buf.write("\2\2\2\u00da\u00db\7\30\2\2\u00db\61\3\2\2\2\u00dc\u00e2")
        buf.write("\5\6\4\2\u00dd\u00de\7\17\2\2\u00de\u00df\5\24\13\2\u00df")
        buf.write("\u00e0\7\35\2\2\u00e0\u00e2\3\2\2\2\u00e1\u00dc\3\2\2")
        buf.write("\2\u00e1\u00dd\3\2\2\2\u00e2\63\3\2\2\2\u00e3\u00e4\b")
        buf.write("\33\1\2\u00e4\u00e7\7\21\2\2\u00e5\u00e7\7\22\2\2\u00e6")
        buf.write("\u00e3\3\2\2\2\u00e6\u00e5\3\2\2\2\u00e7\u00ed\3\2\2\2")
        buf.write("\u00e8\u00e9\f\3\2\2\u00e9\u00ea\7\32\2\2\u00ea\u00ec")
        buf.write("\5\64\33\4\u00eb\u00e8\3\2\2\2\u00ec\u00ef\3\2\2\2\u00ed")
        buf.write("\u00eb\3\2\2\2\u00ed\u00ee\3\2\2\2\u00ee\65\3\2\2\2\u00ef")
        buf.write("\u00ed\3\2\2\2\u00f0\u00f2\7\24\2\2\u00f1\u00f3\5\64\33")
        buf.write("\2\u00f2\u00f1\3\2\2\2\u00f2\u00f3\3\2\2\2\u00f3\u00f4")
        buf.write("\3\2\2\2\u00f4\u00f5\7\27\2\2\u00f5\67\3\2\2\2\u00f6\u00f7")
        buf.write("\t\4\2\2\u00f79\3\2\2\2\26=DJcis\177\u0084\u008f\u0099")
        buf.write("\u00a3\u00a8\u00b1\u00b9\u00ce\u00d7\u00e1\u00e6\u00ed")
        buf.write("\u00f2")
        return buf.getvalue()


class brownie_grammarParser ( Parser ):

    grammarFileName = "brownie_grammar.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'if'", "'elif'", "'else'", "'switch'", 
                     "'case'", "'while'", "'for'", "'do'", "'True'", "'False'", 
                     "'break'", "'fun'", "'return'", "'thread'", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'['", "'{'", "'('", "']'", 
                     "'}'", "')'", "','", "'.'", "':'", "';'", "'+'", "'-'", 
                     "'*'", "'/'", "'^'", "'&&'", "'||'", "'!'", "'=='", 
                     "'!='", "'>'", "'<'", "'>='", "'<='", "'='", "'#'", 
                     "'/*'", "'*/'" ]

    symbolicNames = [ "<INVALID>", "IF", "ELIF", "ELSE", "SWITCH", "CASE", 
                      "WHILE", "FOR", "DO", "TRUE", "FALSE", "BREAK", "FUNCTION", 
                      "RETURN", "THREAD", "NUMBER", "STRING", "VARIABLE", 
                      "OP_SQUARE", "OP_BRACE", "OP_PARENTHESIS", "CL_SQUARE", 
                      "CL_BRACE", "CL_PARENTHESIS", "COMMA", "DOT", "COLON", 
                      "SEMICOLON", "PLUS", "MINUS", "MUL", "DIV", "POW", 
                      "AND", "OR", "NOT", "EQ", "DIF", "GREATER", "LESS", 
                      "GEQ", "LEQ", "ASSIGN", "COMMENT_LINE", "COMM_OPEN", 
                      "COMM_CLOSE", "WHITESPACE" ]

    RULE_start = 0
    RULE_structure = 1
    RULE_sentence = 2
    RULE_function = 3
    RULE_call = 4
    RULE_call_sentence = 5
    RULE_parameter = 6
    RULE_parameter_call = 7
    RULE_definition = 8
    RULE_exp = 9
    RULE_ar_value = 10
    RULE_ar_operator = 11
    RULE_conditional = 12
    RULE_otherwise = 13
    RULE_condition = 14
    RULE_com_value = 15
    RULE_comparator = 16
    RULE_loop = 17
    RULE_while_ = 18
    RULE_for_ = 19
    RULE_for_condition = 20
    RULE_for_def = 21
    RULE_body = 22
    RULE_fun_body = 23
    RULE_fun_sentence = 24
    RULE_element = 25
    RULE_list_elements = 26
    RULE_logic = 27

    ruleNames =  [ "start", "structure", "sentence", "function", "call", 
                   "call_sentence", "parameter", "parameter_call", "definition", 
                   "exp", "ar_value", "ar_operator", "conditional", "otherwise", 
                   "condition", "com_value", "comparator", "loop", "while_", 
                   "for_", "for_condition", "for_def", "body", "fun_body", 
                   "fun_sentence", "element", "list_elements", "logic" ]

    EOF = Token.EOF
    IF=1
    ELIF=2
    ELSE=3
    SWITCH=4
    CASE=5
    WHILE=6
    FOR=7
    DO=8
    TRUE=9
    FALSE=10
    BREAK=11
    FUNCTION=12
    RETURN=13
    THREAD=14
    NUMBER=15
    STRING=16
    VARIABLE=17
    OP_SQUARE=18
    OP_BRACE=19
    OP_PARENTHESIS=20
    CL_SQUARE=21
    CL_BRACE=22
    CL_PARENTHESIS=23
    COMMA=24
    DOT=25
    COLON=26
    SEMICOLON=27
    PLUS=28
    MINUS=29
    MUL=30
    DIV=31
    POW=32
    AND=33
    OR=34
    NOT=35
    EQ=36
    DIF=37
    GREATER=38
    LESS=39
    GEQ=40
    LEQ=41
    ASSIGN=42
    COMMENT_LINE=43
    COMM_OPEN=44
    COMM_CLOSE=45
    WHITESPACE=46

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class StartContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(brownie_grammarParser.EOF, 0)

        def structure(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(brownie_grammarParser.StructureContext)
            else:
                return self.getTypedRuleContext(brownie_grammarParser.StructureContext,i)


        def getRuleIndex(self):
            return brownie_grammarParser.RULE_start

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStart" ):
                listener.enterStart(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStart" ):
                listener.exitStart(self)




    def start(self):

        localctx = brownie_grammarParser.StartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_start)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 57 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 56
                self.structure()
                self.state = 59 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << brownie_grammarParser.IF) | (1 << brownie_grammarParser.WHILE) | (1 << brownie_grammarParser.DO) | (1 << brownie_grammarParser.FUNCTION) | (1 << brownie_grammarParser.VARIABLE))) != 0)):
                    break

            self.state = 61
            self.match(brownie_grammarParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StructureContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def function(self):
            return self.getTypedRuleContext(brownie_grammarParser.FunctionContext,0)


        def sentence(self):
            return self.getTypedRuleContext(brownie_grammarParser.SentenceContext,0)


        def call(self):
            return self.getTypedRuleContext(brownie_grammarParser.CallContext,0)


        def getRuleIndex(self):
            return brownie_grammarParser.RULE_structure

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStructure" ):
                listener.enterStructure(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStructure" ):
                listener.exitStructure(self)




    def structure(self):

        localctx = brownie_grammarParser.StructureContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_structure)
        try:
            self.state = 66
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 63
                self.function()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 64
                self.sentence()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 65
                self.call()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SentenceContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def definition(self):
            return self.getTypedRuleContext(brownie_grammarParser.DefinitionContext,0)


        def conditional(self):
            return self.getTypedRuleContext(brownie_grammarParser.ConditionalContext,0)


        def call_sentence(self):
            return self.getTypedRuleContext(brownie_grammarParser.Call_sentenceContext,0)


        def loop(self):
            return self.getTypedRuleContext(brownie_grammarParser.LoopContext,0)


        def getRuleIndex(self):
            return brownie_grammarParser.RULE_sentence

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSentence" ):
                listener.enterSentence(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSentence" ):
                listener.exitSentence(self)




    def sentence(self):

        localctx = brownie_grammarParser.SentenceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_sentence)
        try:
            self.state = 72
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 68
                self.definition()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 69
                self.conditional()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 70
                self.call_sentence()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 71
                self.loop()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNCTION(self):
            return self.getToken(brownie_grammarParser.FUNCTION, 0)

        def VARIABLE(self):
            return self.getToken(brownie_grammarParser.VARIABLE, 0)

        def OP_PARENTHESIS(self):
            return self.getToken(brownie_grammarParser.OP_PARENTHESIS, 0)

        def parameter(self):
            return self.getTypedRuleContext(brownie_grammarParser.ParameterContext,0)


        def CL_PARENTHESIS(self):
            return self.getToken(brownie_grammarParser.CL_PARENTHESIS, 0)

        def fun_body(self):
            return self.getTypedRuleContext(brownie_grammarParser.Fun_bodyContext,0)


        def getRuleIndex(self):
            return brownie_grammarParser.RULE_function

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunction" ):
                listener.enterFunction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunction" ):
                listener.exitFunction(self)




    def function(self):

        localctx = brownie_grammarParser.FunctionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_function)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 74
            self.match(brownie_grammarParser.FUNCTION)
            self.state = 75
            self.match(brownie_grammarParser.VARIABLE)
            self.state = 76
            self.match(brownie_grammarParser.OP_PARENTHESIS)
            self.state = 77
            self.parameter(0)
            self.state = 78
            self.match(brownie_grammarParser.CL_PARENTHESIS)
            self.state = 79
            self.fun_body()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CallContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VARIABLE(self):
            return self.getToken(brownie_grammarParser.VARIABLE, 0)

        def OP_PARENTHESIS(self):
            return self.getToken(brownie_grammarParser.OP_PARENTHESIS, 0)

        def parameter_call(self):
            return self.getTypedRuleContext(brownie_grammarParser.Parameter_callContext,0)


        def CL_PARENTHESIS(self):
            return self.getToken(brownie_grammarParser.CL_PARENTHESIS, 0)

        def getRuleIndex(self):
            return brownie_grammarParser.RULE_call

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCall" ):
                listener.enterCall(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCall" ):
                listener.exitCall(self)




    def call(self):

        localctx = brownie_grammarParser.CallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_call)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 81
            self.match(brownie_grammarParser.VARIABLE)
            self.state = 82
            self.match(brownie_grammarParser.OP_PARENTHESIS)
            self.state = 83
            self.parameter_call()
            self.state = 84
            self.match(brownie_grammarParser.CL_PARENTHESIS)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Call_sentenceContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def call(self):
            return self.getTypedRuleContext(brownie_grammarParser.CallContext,0)


        def SEMICOLON(self):
            return self.getToken(brownie_grammarParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return brownie_grammarParser.RULE_call_sentence

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCall_sentence" ):
                listener.enterCall_sentence(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCall_sentence" ):
                listener.exitCall_sentence(self)




    def call_sentence(self):

        localctx = brownie_grammarParser.Call_sentenceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_call_sentence)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 86
            self.call()
            self.state = 87
            self.match(brownie_grammarParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParameterContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VARIABLE(self):
            return self.getToken(brownie_grammarParser.VARIABLE, 0)

        def parameter(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(brownie_grammarParser.ParameterContext)
            else:
                return self.getTypedRuleContext(brownie_grammarParser.ParameterContext,i)


        def COMMA(self):
            return self.getToken(brownie_grammarParser.COMMA, 0)

        def getRuleIndex(self):
            return brownie_grammarParser.RULE_parameter

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParameter" ):
                listener.enterParameter(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParameter" ):
                listener.exitParameter(self)



    def parameter(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = brownie_grammarParser.ParameterContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 12
        self.enterRecursionRule(localctx, 12, self.RULE_parameter, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 90
            self.match(brownie_grammarParser.VARIABLE)
            self._ctx.stop = self._input.LT(-1)
            self.state = 97
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = brownie_grammarParser.ParameterContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_parameter)
                    self.state = 92
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 93
                    self.match(brownie_grammarParser.COMMA)
                    self.state = 94
                    self.parameter(2) 
                self.state = 99
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Parameter_callContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VARIABLE(self, i:int=None):
            if i is None:
                return self.getTokens(brownie_grammarParser.VARIABLE)
            else:
                return self.getToken(brownie_grammarParser.VARIABLE, i)

        def NUMBER(self):
            return self.getToken(brownie_grammarParser.NUMBER, 0)

        def STRING(self):
            return self.getToken(brownie_grammarParser.STRING, 0)

        def call(self):
            return self.getTypedRuleContext(brownie_grammarParser.CallContext,0)


        def parameter(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(brownie_grammarParser.ParameterContext)
            else:
                return self.getTypedRuleContext(brownie_grammarParser.ParameterContext,i)


        def COMMA(self):
            return self.getToken(brownie_grammarParser.COMMA, 0)

        def getRuleIndex(self):
            return brownie_grammarParser.RULE_parameter_call

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParameter_call" ):
                listener.enterParameter_call(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParameter_call" ):
                listener.exitParameter_call(self)




    def parameter_call(self):

        localctx = brownie_grammarParser.Parameter_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_parameter_call)
        self._la = 0 # Token type
        try:
            self.state = 113
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 103
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==brownie_grammarParser.VARIABLE:
                    self.state = 100
                    self.match(brownie_grammarParser.VARIABLE)
                    self.state = 105
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 106
                self.match(brownie_grammarParser.NUMBER)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 107
                self.match(brownie_grammarParser.STRING)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 108
                self.call()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 109
                self.parameter(0)
                self.state = 110
                self.match(brownie_grammarParser.COMMA)
                self.state = 111
                self.parameter(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DefinitionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VARIABLE(self):
            return self.getToken(brownie_grammarParser.VARIABLE, 0)

        def ASSIGN(self):
            return self.getToken(brownie_grammarParser.ASSIGN, 0)

        def exp(self):
            return self.getTypedRuleContext(brownie_grammarParser.ExpContext,0)


        def SEMICOLON(self):
            return self.getToken(brownie_grammarParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return brownie_grammarParser.RULE_definition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDefinition" ):
                listener.enterDefinition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDefinition" ):
                listener.exitDefinition(self)




    def definition(self):

        localctx = brownie_grammarParser.DefinitionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_definition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 115
            self.match(brownie_grammarParser.VARIABLE)
            self.state = 116
            self.match(brownie_grammarParser.ASSIGN)
            self.state = 117
            self.exp()
            self.state = 118
            self.match(brownie_grammarParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ar_value(self):
            return self.getTypedRuleContext(brownie_grammarParser.Ar_valueContext,0)


        def ar_operator(self):
            return self.getTypedRuleContext(brownie_grammarParser.Ar_operatorContext,0)


        def exp(self):
            return self.getTypedRuleContext(brownie_grammarParser.ExpContext,0)


        def getRuleIndex(self):
            return brownie_grammarParser.RULE_exp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExp" ):
                listener.enterExp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExp" ):
                listener.exitExp(self)




    def exp(self):

        localctx = brownie_grammarParser.ExpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_exp)
        try:
            self.state = 125
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 120
                self.ar_value()
                self.state = 121
                self.ar_operator()
                self.state = 122
                self.exp()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 124
                self.ar_value()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Ar_valueContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(brownie_grammarParser.NUMBER, 0)

        def VARIABLE(self):
            return self.getToken(brownie_grammarParser.VARIABLE, 0)

        def call(self):
            return self.getTypedRuleContext(brownie_grammarParser.CallContext,0)


        def getRuleIndex(self):
            return brownie_grammarParser.RULE_ar_value

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAr_value" ):
                listener.enterAr_value(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAr_value" ):
                listener.exitAr_value(self)




    def ar_value(self):

        localctx = brownie_grammarParser.Ar_valueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_ar_value)
        try:
            self.state = 130
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 127
                self.match(brownie_grammarParser.NUMBER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 128
                self.match(brownie_grammarParser.VARIABLE)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 129
                self.call()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Ar_operatorContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PLUS(self):
            return self.getToken(brownie_grammarParser.PLUS, 0)

        def MINUS(self):
            return self.getToken(brownie_grammarParser.MINUS, 0)

        def MUL(self):
            return self.getToken(brownie_grammarParser.MUL, 0)

        def DIV(self):
            return self.getToken(brownie_grammarParser.DIV, 0)

        def POW(self):
            return self.getToken(brownie_grammarParser.POW, 0)

        def getRuleIndex(self):
            return brownie_grammarParser.RULE_ar_operator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAr_operator" ):
                listener.enterAr_operator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAr_operator" ):
                listener.exitAr_operator(self)




    def ar_operator(self):

        localctx = brownie_grammarParser.Ar_operatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_ar_operator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 132
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << brownie_grammarParser.PLUS) | (1 << brownie_grammarParser.MINUS) | (1 << brownie_grammarParser.MUL) | (1 << brownie_grammarParser.DIV) | (1 << brownie_grammarParser.POW))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConditionalContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(brownie_grammarParser.IF, 0)

        def condition(self):
            return self.getTypedRuleContext(brownie_grammarParser.ConditionContext,0)


        def COLON(self):
            return self.getToken(brownie_grammarParser.COLON, 0)

        def body(self):
            return self.getTypedRuleContext(brownie_grammarParser.BodyContext,0)


        def otherwise(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(brownie_grammarParser.OtherwiseContext)
            else:
                return self.getTypedRuleContext(brownie_grammarParser.OtherwiseContext,i)


        def getRuleIndex(self):
            return brownie_grammarParser.RULE_conditional

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConditional" ):
                listener.enterConditional(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConditional" ):
                listener.exitConditional(self)




    def conditional(self):

        localctx = brownie_grammarParser.ConditionalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_conditional)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 134
            self.match(brownie_grammarParser.IF)
            self.state = 135
            self.condition()
            self.state = 136
            self.match(brownie_grammarParser.COLON)
            self.state = 137
            self.body()
            self.state = 141
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==brownie_grammarParser.ELIF or _la==brownie_grammarParser.ELSE:
                self.state = 138
                self.otherwise()
                self.state = 143
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OtherwiseContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELIF(self):
            return self.getToken(brownie_grammarParser.ELIF, 0)

        def condition(self):
            return self.getTypedRuleContext(brownie_grammarParser.ConditionContext,0)


        def COLON(self):
            return self.getToken(brownie_grammarParser.COLON, 0)

        def body(self):
            return self.getTypedRuleContext(brownie_grammarParser.BodyContext,0)


        def ELSE(self):
            return self.getToken(brownie_grammarParser.ELSE, 0)

        def getRuleIndex(self):
            return brownie_grammarParser.RULE_otherwise

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOtherwise" ):
                listener.enterOtherwise(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOtherwise" ):
                listener.exitOtherwise(self)




    def otherwise(self):

        localctx = brownie_grammarParser.OtherwiseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_otherwise)
        try:
            self.state = 151
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [brownie_grammarParser.ELIF]:
                self.enterOuterAlt(localctx, 1)
                self.state = 144
                self.match(brownie_grammarParser.ELIF)
                self.state = 145
                self.condition()
                self.state = 146
                self.match(brownie_grammarParser.COLON)
                self.state = 147
                self.body()
                pass
            elif token in [brownie_grammarParser.ELSE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 149
                self.match(brownie_grammarParser.ELSE)
                self.state = 150
                self.body()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConditionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def com_value(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(brownie_grammarParser.Com_valueContext)
            else:
                return self.getTypedRuleContext(brownie_grammarParser.Com_valueContext,i)


        def comparator(self):
            return self.getTypedRuleContext(brownie_grammarParser.ComparatorContext,0)


        def logic(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(brownie_grammarParser.LogicContext)
            else:
                return self.getTypedRuleContext(brownie_grammarParser.LogicContext,i)


        def condition(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(brownie_grammarParser.ConditionContext)
            else:
                return self.getTypedRuleContext(brownie_grammarParser.ConditionContext,i)


        def TRUE(self):
            return self.getToken(brownie_grammarParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(brownie_grammarParser.FALSE, 0)

        def getRuleIndex(self):
            return brownie_grammarParser.RULE_condition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondition" ):
                listener.enterCondition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondition" ):
                listener.exitCondition(self)




    def condition(self):

        localctx = brownie_grammarParser.ConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_condition)
        try:
            self.state = 166
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 153
                self.com_value()
                self.state = 154
                self.comparator()
                self.state = 155
                self.com_value()
                self.state = 161
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,10,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 156
                        self.logic()
                        self.state = 157
                        self.condition() 
                    self.state = 163
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,10,self._ctx)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 164
                self.match(brownie_grammarParser.TRUE)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 165
                self.match(brownie_grammarParser.FALSE)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Com_valueContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(brownie_grammarParser.NUMBER, 0)

        def VARIABLE(self):
            return self.getToken(brownie_grammarParser.VARIABLE, 0)

        def STRING(self):
            return self.getToken(brownie_grammarParser.STRING, 0)

        def TRUE(self):
            return self.getToken(brownie_grammarParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(brownie_grammarParser.FALSE, 0)

        def call(self):
            return self.getTypedRuleContext(brownie_grammarParser.CallContext,0)


        def getRuleIndex(self):
            return brownie_grammarParser.RULE_com_value

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCom_value" ):
                listener.enterCom_value(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCom_value" ):
                listener.exitCom_value(self)




    def com_value(self):

        localctx = brownie_grammarParser.Com_valueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_com_value)
        try:
            self.state = 175
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 168
                self.match(brownie_grammarParser.NUMBER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 169
                self.match(brownie_grammarParser.VARIABLE)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 170
                self.match(brownie_grammarParser.STRING)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)

                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 172
                self.match(brownie_grammarParser.TRUE)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 173
                self.match(brownie_grammarParser.FALSE)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 174
                self.call()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ComparatorContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EQ(self):
            return self.getToken(brownie_grammarParser.EQ, 0)

        def DIF(self):
            return self.getToken(brownie_grammarParser.DIF, 0)

        def GREATER(self):
            return self.getToken(brownie_grammarParser.GREATER, 0)

        def LESS(self):
            return self.getToken(brownie_grammarParser.LESS, 0)

        def GEQ(self):
            return self.getToken(brownie_grammarParser.GEQ, 0)

        def LEQ(self):
            return self.getToken(brownie_grammarParser.LEQ, 0)

        def getRuleIndex(self):
            return brownie_grammarParser.RULE_comparator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComparator" ):
                listener.enterComparator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComparator" ):
                listener.exitComparator(self)




    def comparator(self):

        localctx = brownie_grammarParser.ComparatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_comparator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 177
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << brownie_grammarParser.EQ) | (1 << brownie_grammarParser.DIF) | (1 << brownie_grammarParser.GREATER) | (1 << brownie_grammarParser.LESS) | (1 << brownie_grammarParser.GEQ) | (1 << brownie_grammarParser.LEQ))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LoopContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def while_(self):
            return self.getTypedRuleContext(brownie_grammarParser.While_Context,0)


        def getRuleIndex(self):
            return brownie_grammarParser.RULE_loop

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLoop" ):
                listener.enterLoop(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLoop" ):
                listener.exitLoop(self)




    def loop(self):

        localctx = brownie_grammarParser.LoopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_loop)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 179
            self.while_()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class While_Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(brownie_grammarParser.WHILE, 0)

        def condition(self):
            return self.getTypedRuleContext(brownie_grammarParser.ConditionContext,0)


        def body(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(brownie_grammarParser.BodyContext)
            else:
                return self.getTypedRuleContext(brownie_grammarParser.BodyContext,i)


        def DO(self):
            return self.getToken(brownie_grammarParser.DO, 0)

        def getRuleIndex(self):
            return brownie_grammarParser.RULE_while_

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhile_" ):
                listener.enterWhile_(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhile_" ):
                listener.exitWhile_(self)




    def while_(self):

        localctx = brownie_grammarParser.While_Context(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_while_)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 183
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==brownie_grammarParser.DO:
                self.state = 181
                self.match(brownie_grammarParser.DO)
                self.state = 182
                self.body()


            self.state = 185
            self.match(brownie_grammarParser.WHILE)
            self.state = 186
            self.condition()
            self.state = 187
            self.body()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(brownie_grammarParser.FOR, 0)

        def for_condition(self):
            return self.getTypedRuleContext(brownie_grammarParser.For_conditionContext,0)


        def body(self):
            return self.getTypedRuleContext(brownie_grammarParser.BodyContext,0)


        def getRuleIndex(self):
            return brownie_grammarParser.RULE_for_

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFor_" ):
                listener.enterFor_(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFor_" ):
                listener.exitFor_(self)




    def for_(self):

        localctx = brownie_grammarParser.For_Context(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_for_)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 189
            self.match(brownie_grammarParser.FOR)
            self.state = 190
            self.for_condition()
            self.state = 191
            self.body()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_conditionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def for_def(self):
            return self.getTypedRuleContext(brownie_grammarParser.For_defContext,0)


        def SEMICOLON(self):
            return self.getToken(brownie_grammarParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return brownie_grammarParser.RULE_for_condition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFor_condition" ):
                listener.enterFor_condition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFor_condition" ):
                listener.exitFor_condition(self)




    def for_condition(self):

        localctx = brownie_grammarParser.For_conditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_for_condition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 193
            self.for_def()
            self.state = 194
            self.match(brownie_grammarParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_defContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VARIABLE(self):
            return self.getToken(brownie_grammarParser.VARIABLE, 0)

        def ASSIGN(self):
            return self.getToken(brownie_grammarParser.ASSIGN, 0)

        def exp(self):
            return self.getTypedRuleContext(brownie_grammarParser.ExpContext,0)


        def getRuleIndex(self):
            return brownie_grammarParser.RULE_for_def

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFor_def" ):
                listener.enterFor_def(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFor_def" ):
                listener.exitFor_def(self)




    def for_def(self):

        localctx = brownie_grammarParser.For_defContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_for_def)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 196
            self.match(brownie_grammarParser.VARIABLE)
            self.state = 197
            self.match(brownie_grammarParser.ASSIGN)
            self.state = 198
            self.exp()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BodyContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OP_BRACE(self):
            return self.getToken(brownie_grammarParser.OP_BRACE, 0)

        def CL_BRACE(self):
            return self.getToken(brownie_grammarParser.CL_BRACE, 0)

        def sentence(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(brownie_grammarParser.SentenceContext)
            else:
                return self.getTypedRuleContext(brownie_grammarParser.SentenceContext,i)


        def getRuleIndex(self):
            return brownie_grammarParser.RULE_body

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBody" ):
                listener.enterBody(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBody" ):
                listener.exitBody(self)




    def body(self):

        localctx = brownie_grammarParser.BodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_body)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 200
            self.match(brownie_grammarParser.OP_BRACE)
            self.state = 204
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << brownie_grammarParser.IF) | (1 << brownie_grammarParser.WHILE) | (1 << brownie_grammarParser.DO) | (1 << brownie_grammarParser.VARIABLE))) != 0):
                self.state = 201
                self.sentence()
                self.state = 206
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 207
            self.match(brownie_grammarParser.CL_BRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Fun_bodyContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OP_BRACE(self):
            return self.getToken(brownie_grammarParser.OP_BRACE, 0)

        def CL_BRACE(self):
            return self.getToken(brownie_grammarParser.CL_BRACE, 0)

        def fun_sentence(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(brownie_grammarParser.Fun_sentenceContext)
            else:
                return self.getTypedRuleContext(brownie_grammarParser.Fun_sentenceContext,i)


        def getRuleIndex(self):
            return brownie_grammarParser.RULE_fun_body

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFun_body" ):
                listener.enterFun_body(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFun_body" ):
                listener.exitFun_body(self)




    def fun_body(self):

        localctx = brownie_grammarParser.Fun_bodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_fun_body)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 209
            self.match(brownie_grammarParser.OP_BRACE)
            self.state = 213
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << brownie_grammarParser.IF) | (1 << brownie_grammarParser.WHILE) | (1 << brownie_grammarParser.DO) | (1 << brownie_grammarParser.RETURN) | (1 << brownie_grammarParser.VARIABLE))) != 0):
                self.state = 210
                self.fun_sentence()
                self.state = 215
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 216
            self.match(brownie_grammarParser.CL_BRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Fun_sentenceContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def sentence(self):
            return self.getTypedRuleContext(brownie_grammarParser.SentenceContext,0)


        def RETURN(self):
            return self.getToken(brownie_grammarParser.RETURN, 0)

        def exp(self):
            return self.getTypedRuleContext(brownie_grammarParser.ExpContext,0)


        def SEMICOLON(self):
            return self.getToken(brownie_grammarParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return brownie_grammarParser.RULE_fun_sentence

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFun_sentence" ):
                listener.enterFun_sentence(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFun_sentence" ):
                listener.exitFun_sentence(self)




    def fun_sentence(self):

        localctx = brownie_grammarParser.Fun_sentenceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_fun_sentence)
        try:
            self.state = 223
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [brownie_grammarParser.IF, brownie_grammarParser.WHILE, brownie_grammarParser.DO, brownie_grammarParser.VARIABLE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 218
                self.sentence()
                pass
            elif token in [brownie_grammarParser.RETURN]:
                self.enterOuterAlt(localctx, 2)
                self.state = 219
                self.match(brownie_grammarParser.RETURN)
                self.state = 220
                self.exp()
                self.state = 221
                self.match(brownie_grammarParser.SEMICOLON)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(brownie_grammarParser.NUMBER, 0)

        def STRING(self):
            return self.getToken(brownie_grammarParser.STRING, 0)

        def element(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(brownie_grammarParser.ElementContext)
            else:
                return self.getTypedRuleContext(brownie_grammarParser.ElementContext,i)


        def COMMA(self):
            return self.getToken(brownie_grammarParser.COMMA, 0)

        def getRuleIndex(self):
            return brownie_grammarParser.RULE_element

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElement" ):
                listener.enterElement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElement" ):
                listener.exitElement(self)



    def element(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = brownie_grammarParser.ElementContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 50
        self.enterRecursionRule(localctx, 50, self.RULE_element, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 228
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [brownie_grammarParser.NUMBER]:
                self.state = 226
                self.match(brownie_grammarParser.NUMBER)
                pass
            elif token in [brownie_grammarParser.STRING]:
                self.state = 227
                self.match(brownie_grammarParser.STRING)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 235
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,18,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = brownie_grammarParser.ElementContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_element)
                    self.state = 230
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 231
                    self.match(brownie_grammarParser.COMMA)
                    self.state = 232
                    self.element(2) 
                self.state = 237
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,18,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class List_elementsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OP_SQUARE(self):
            return self.getToken(brownie_grammarParser.OP_SQUARE, 0)

        def CL_SQUARE(self):
            return self.getToken(brownie_grammarParser.CL_SQUARE, 0)

        def element(self):
            return self.getTypedRuleContext(brownie_grammarParser.ElementContext,0)


        def getRuleIndex(self):
            return brownie_grammarParser.RULE_list_elements

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterList_elements" ):
                listener.enterList_elements(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitList_elements" ):
                listener.exitList_elements(self)




    def list_elements(self):

        localctx = brownie_grammarParser.List_elementsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_list_elements)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 238
            self.match(brownie_grammarParser.OP_SQUARE)
            self.state = 240
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==brownie_grammarParser.NUMBER or _la==brownie_grammarParser.STRING:
                self.state = 239
                self.element(0)


            self.state = 242
            self.match(brownie_grammarParser.CL_SQUARE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LogicContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AND(self):
            return self.getToken(brownie_grammarParser.AND, 0)

        def OR(self):
            return self.getToken(brownie_grammarParser.OR, 0)

        def getRuleIndex(self):
            return brownie_grammarParser.RULE_logic

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogic" ):
                listener.enterLogic(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogic" ):
                listener.exitLogic(self)




    def logic(self):

        localctx = brownie_grammarParser.LogicContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_logic)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 244
            _la = self._input.LA(1)
            if not(_la==brownie_grammarParser.AND or _la==brownie_grammarParser.OR):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[6] = self.parameter_sempred
        self._predicates[25] = self.element_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def parameter_sempred(self, localctx:ParameterContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 1)
         

    def element_sempred(self, localctx:ElementContext, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 1)
         




