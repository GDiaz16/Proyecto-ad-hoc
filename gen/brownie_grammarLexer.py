# Generated from E:/Universidad/Materias/Lenguajes de Programaci�n/Proyecto/Compiler\brownie_grammar.g4 by ANTLR 4.7.2
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\60")
        buf.write("\u0114\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4")
        buf.write("\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3")
        buf.write("\6\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\t\3\t\3\t")
        buf.write("\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3\13\3\f")
        buf.write("\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3")
        buf.write("\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\17\3\17")
        buf.write("\3\20\5\20\u00aa\n\20\3\20\6\20\u00ad\n\20\r\20\16\20")
        buf.write("\u00ae\3\20\5\20\u00b2\n\20\3\20\6\20\u00b5\n\20\r\20")
        buf.write("\16\20\u00b6\3\20\3\20\6\20\u00bb\n\20\r\20\16\20\u00bc")
        buf.write("\5\20\u00bf\n\20\3\21\3\21\7\21\u00c3\n\21\f\21\16\21")
        buf.write("\u00c6\13\21\3\21\3\21\3\22\3\22\7\22\u00cc\n\22\f\22")
        buf.write("\16\22\u00cf\13\22\3\23\3\23\3\24\3\24\3\25\3\25\3\26")
        buf.write("\3\26\3\27\3\27\3\30\3\30\3\31\3\31\3\32\3\32\3\33\3\33")
        buf.write("\3\34\3\34\3\35\3\35\3\36\3\36\3\37\3\37\3 \3 \3!\3!\3")
        buf.write("\"\3\"\3\"\3#\3#\3#\3$\3$\3%\3%\3%\3&\3&\3&\3\'\3\'\3")
        buf.write("(\3(\3)\3)\3)\3*\3*\3*\3+\3+\3,\3,\3-\3-\3-\3.\3.\3.\3")
        buf.write("/\3/\3/\3/\3\u00c4\2\60\3\3\5\4\7\5\t\6\13\7\r\b\17\t")
        buf.write("\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23")
        buf.write("%\24\'\25)\26+\27-\30/\31\61\32\63\33\65\34\67\359\36")
        buf.write(";\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[/]\60\3\2\7\3\2/")
        buf.write("/\3\2\62;\4\2C\\c|\6\2\62;C\\aac|\4\2\13\f\"\"\2\u011b")
        buf.write("\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13")
        buf.write("\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3")
        buf.write("\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2")
        buf.write("\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2")
        buf.write("%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2")
        buf.write("\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67")
        buf.write("\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2")
        buf.write("A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2")
        buf.write("\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2")
        buf.write("\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2")
        buf.write("\2\2\3_\3\2\2\2\5b\3\2\2\2\7g\3\2\2\2\tl\3\2\2\2\13s\3")
        buf.write("\2\2\2\rx\3\2\2\2\17~\3\2\2\2\21\u0082\3\2\2\2\23\u0085")
        buf.write("\3\2\2\2\25\u008a\3\2\2\2\27\u0090\3\2\2\2\31\u0096\3")
        buf.write("\2\2\2\33\u009a\3\2\2\2\35\u00a1\3\2\2\2\37\u00be\3\2")
        buf.write("\2\2!\u00c0\3\2\2\2#\u00c9\3\2\2\2%\u00d0\3\2\2\2\'\u00d2")
        buf.write("\3\2\2\2)\u00d4\3\2\2\2+\u00d6\3\2\2\2-\u00d8\3\2\2\2")
        buf.write("/\u00da\3\2\2\2\61\u00dc\3\2\2\2\63\u00de\3\2\2\2\65\u00e0")
        buf.write("\3\2\2\2\67\u00e2\3\2\2\29\u00e4\3\2\2\2;\u00e6\3\2\2")
        buf.write("\2=\u00e8\3\2\2\2?\u00ea\3\2\2\2A\u00ec\3\2\2\2C\u00ee")
        buf.write("\3\2\2\2E\u00f1\3\2\2\2G\u00f4\3\2\2\2I\u00f6\3\2\2\2")
        buf.write("K\u00f9\3\2\2\2M\u00fc\3\2\2\2O\u00fe\3\2\2\2Q\u0100\3")
        buf.write("\2\2\2S\u0103\3\2\2\2U\u0106\3\2\2\2W\u0108\3\2\2\2Y\u010a")
        buf.write("\3\2\2\2[\u010d\3\2\2\2]\u0110\3\2\2\2_`\7k\2\2`a\7h\2")
        buf.write("\2a\4\3\2\2\2bc\7g\2\2cd\7n\2\2de\7k\2\2ef\7h\2\2f\6\3")
        buf.write("\2\2\2gh\7g\2\2hi\7n\2\2ij\7u\2\2jk\7g\2\2k\b\3\2\2\2")
        buf.write("lm\7u\2\2mn\7y\2\2no\7k\2\2op\7v\2\2pq\7e\2\2qr\7j\2\2")
        buf.write("r\n\3\2\2\2st\7e\2\2tu\7c\2\2uv\7u\2\2vw\7g\2\2w\f\3\2")
        buf.write("\2\2xy\7y\2\2yz\7j\2\2z{\7k\2\2{|\7n\2\2|}\7g\2\2}\16")
        buf.write("\3\2\2\2~\177\7h\2\2\177\u0080\7q\2\2\u0080\u0081\7t\2")
        buf.write("\2\u0081\20\3\2\2\2\u0082\u0083\7f\2\2\u0083\u0084\7q")
        buf.write("\2\2\u0084\22\3\2\2\2\u0085\u0086\7V\2\2\u0086\u0087\7")
        buf.write("t\2\2\u0087\u0088\7w\2\2\u0088\u0089\7g\2\2\u0089\24\3")
        buf.write("\2\2\2\u008a\u008b\7H\2\2\u008b\u008c\7c\2\2\u008c\u008d")
        buf.write("\7n\2\2\u008d\u008e\7u\2\2\u008e\u008f\7g\2\2\u008f\26")
        buf.write("\3\2\2\2\u0090\u0091\7d\2\2\u0091\u0092\7t\2\2\u0092\u0093")
        buf.write("\7g\2\2\u0093\u0094\7c\2\2\u0094\u0095\7m\2\2\u0095\30")
        buf.write("\3\2\2\2\u0096\u0097\7h\2\2\u0097\u0098\7w\2\2\u0098\u0099")
        buf.write("\7p\2\2\u0099\32\3\2\2\2\u009a\u009b\7t\2\2\u009b\u009c")
        buf.write("\7g\2\2\u009c\u009d\7v\2\2\u009d\u009e\7w\2\2\u009e\u009f")
        buf.write("\7t\2\2\u009f\u00a0\7p\2\2\u00a0\34\3\2\2\2\u00a1\u00a2")
        buf.write("\7v\2\2\u00a2\u00a3\7j\2\2\u00a3\u00a4\7t\2\2\u00a4\u00a5")
        buf.write("\7g\2\2\u00a5\u00a6\7c\2\2\u00a6\u00a7\7f\2\2\u00a7\36")
        buf.write("\3\2\2\2\u00a8\u00aa\t\2\2\2\u00a9\u00a8\3\2\2\2\u00a9")
        buf.write("\u00aa\3\2\2\2\u00aa\u00ac\3\2\2\2\u00ab\u00ad\t\3\2\2")
        buf.write("\u00ac\u00ab\3\2\2\2\u00ad\u00ae\3\2\2\2\u00ae\u00ac\3")
        buf.write("\2\2\2\u00ae\u00af\3\2\2\2\u00af\u00bf\3\2\2\2\u00b0\u00b2")
        buf.write("\t\2\2\2\u00b1\u00b0\3\2\2\2\u00b1\u00b2\3\2\2\2\u00b2")
        buf.write("\u00b4\3\2\2\2\u00b3\u00b5\t\3\2\2\u00b4\u00b3\3\2\2\2")
        buf.write("\u00b5\u00b6\3\2\2\2\u00b6\u00b4\3\2\2\2\u00b6\u00b7\3")
        buf.write("\2\2\2\u00b7\u00b8\3\2\2\2\u00b8\u00ba\7\60\2\2\u00b9")
        buf.write("\u00bb\t\3\2\2\u00ba\u00b9\3\2\2\2\u00bb\u00bc\3\2\2\2")
        buf.write("\u00bc\u00ba\3\2\2\2\u00bc\u00bd\3\2\2\2\u00bd\u00bf\3")
        buf.write("\2\2\2\u00be\u00a9\3\2\2\2\u00be\u00b1\3\2\2\2\u00bf ")
        buf.write("\3\2\2\2\u00c0\u00c4\7$\2\2\u00c1\u00c3\13\2\2\2\u00c2")
        buf.write("\u00c1\3\2\2\2\u00c3\u00c6\3\2\2\2\u00c4\u00c5\3\2\2\2")
        buf.write("\u00c4\u00c2\3\2\2\2\u00c5\u00c7\3\2\2\2\u00c6\u00c4\3")
        buf.write("\2\2\2\u00c7\u00c8\7$\2\2\u00c8\"\3\2\2\2\u00c9\u00cd")
        buf.write("\t\4\2\2\u00ca\u00cc\t\5\2\2\u00cb\u00ca\3\2\2\2\u00cc")
        buf.write("\u00cf\3\2\2\2\u00cd\u00cb\3\2\2\2\u00cd\u00ce\3\2\2\2")
        buf.write("\u00ce$\3\2\2\2\u00cf\u00cd\3\2\2\2\u00d0\u00d1\7]\2\2")
        buf.write("\u00d1&\3\2\2\2\u00d2\u00d3\7}\2\2\u00d3(\3\2\2\2\u00d4")
        buf.write("\u00d5\7*\2\2\u00d5*\3\2\2\2\u00d6\u00d7\7_\2\2\u00d7")
        buf.write(",\3\2\2\2\u00d8\u00d9\7\177\2\2\u00d9.\3\2\2\2\u00da\u00db")
        buf.write("\7+\2\2\u00db\60\3\2\2\2\u00dc\u00dd\7.\2\2\u00dd\62\3")
        buf.write("\2\2\2\u00de\u00df\7\60\2\2\u00df\64\3\2\2\2\u00e0\u00e1")
        buf.write("\7<\2\2\u00e1\66\3\2\2\2\u00e2\u00e3\7=\2\2\u00e38\3\2")
        buf.write("\2\2\u00e4\u00e5\7-\2\2\u00e5:\3\2\2\2\u00e6\u00e7\7/")
        buf.write("\2\2\u00e7<\3\2\2\2\u00e8\u00e9\7,\2\2\u00e9>\3\2\2\2")
        buf.write("\u00ea\u00eb\7\61\2\2\u00eb@\3\2\2\2\u00ec\u00ed\7`\2")
        buf.write("\2\u00edB\3\2\2\2\u00ee\u00ef\7(\2\2\u00ef\u00f0\7(\2")
        buf.write("\2\u00f0D\3\2\2\2\u00f1\u00f2\7~\2\2\u00f2\u00f3\7~\2")
        buf.write("\2\u00f3F\3\2\2\2\u00f4\u00f5\7#\2\2\u00f5H\3\2\2\2\u00f6")
        buf.write("\u00f7\7?\2\2\u00f7\u00f8\7?\2\2\u00f8J\3\2\2\2\u00f9")
        buf.write("\u00fa\7#\2\2\u00fa\u00fb\7?\2\2\u00fbL\3\2\2\2\u00fc")
        buf.write("\u00fd\7@\2\2\u00fdN\3\2\2\2\u00fe\u00ff\7>\2\2\u00ff")
        buf.write("P\3\2\2\2\u0100\u0101\7@\2\2\u0101\u0102\7?\2\2\u0102")
        buf.write("R\3\2\2\2\u0103\u0104\7>\2\2\u0104\u0105\7?\2\2\u0105")
        buf.write("T\3\2\2\2\u0106\u0107\7?\2\2\u0107V\3\2\2\2\u0108\u0109")
        buf.write("\7%\2\2\u0109X\3\2\2\2\u010a\u010b\7\61\2\2\u010b\u010c")
        buf.write("\7,\2\2\u010cZ\3\2\2\2\u010d\u010e\7,\2\2\u010e\u010f")
        buf.write("\7\61\2\2\u010f\\\3\2\2\2\u0110\u0111\t\6\2\2\u0111\u0112")
        buf.write("\3\2\2\2\u0112\u0113\b/\2\2\u0113^\3\2\2\2\13\2\u00a9")
        buf.write("\u00ae\u00b1\u00b6\u00bc\u00be\u00c4\u00cd\3\b\2\2")
        return buf.getvalue()


class brownie_grammarLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    IF = 1
    ELIF = 2
    ELSE = 3
    SWITCH = 4
    CASE = 5
    WHILE = 6
    FOR = 7
    DO = 8
    TRUE = 9
    FALSE = 10
    BREAK = 11
    FUNCTION = 12
    RETURN = 13
    THREAD = 14
    NUMBER = 15
    STRING = 16
    VARIABLE = 17
    OP_SQUARE = 18
    OP_BRACE = 19
    OP_PARENTHESIS = 20
    CL_SQUARE = 21
    CL_BRACE = 22
    CL_PARENTHESIS = 23
    COMMA = 24
    DOT = 25
    COLON = 26
    SEMICOLON = 27
    PLUS = 28
    MINUS = 29
    MUL = 30
    DIV = 31
    POW = 32
    AND = 33
    OR = 34
    NOT = 35
    EQ = 36
    DIF = 37
    GREATER = 38
    LESS = 39
    GEQ = 40
    LEQ = 41
    ASSIGN = 42
    COMMENT_LINE = 43
    COMM_OPEN = 44
    COMM_CLOSE = 45
    WHITESPACE = 46

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'if'", "'elif'", "'else'", "'switch'", "'case'", "'while'", 
            "'for'", "'do'", "'True'", "'False'", "'break'", "'fun'", "'return'", 
            "'thread'", "'['", "'{'", "'('", "']'", "'}'", "')'", "','", 
            "'.'", "':'", "';'", "'+'", "'-'", "'*'", "'/'", "'^'", "'&&'", 
            "'||'", "'!'", "'=='", "'!='", "'>'", "'<'", "'>='", "'<='", 
            "'='", "'#'", "'/*'", "'*/'" ]

    symbolicNames = [ "<INVALID>",
            "IF", "ELIF", "ELSE", "SWITCH", "CASE", "WHILE", "FOR", "DO", 
            "TRUE", "FALSE", "BREAK", "FUNCTION", "RETURN", "THREAD", "NUMBER", 
            "STRING", "VARIABLE", "OP_SQUARE", "OP_BRACE", "OP_PARENTHESIS", 
            "CL_SQUARE", "CL_BRACE", "CL_PARENTHESIS", "COMMA", "DOT", "COLON", 
            "SEMICOLON", "PLUS", "MINUS", "MUL", "DIV", "POW", "AND", "OR", 
            "NOT", "EQ", "DIF", "GREATER", "LESS", "GEQ", "LEQ", "ASSIGN", 
            "COMMENT_LINE", "COMM_OPEN", "COMM_CLOSE", "WHITESPACE" ]

    ruleNames = [ "IF", "ELIF", "ELSE", "SWITCH", "CASE", "WHILE", "FOR", 
                  "DO", "TRUE", "FALSE", "BREAK", "FUNCTION", "RETURN", 
                  "THREAD", "NUMBER", "STRING", "VARIABLE", "OP_SQUARE", 
                  "OP_BRACE", "OP_PARENTHESIS", "CL_SQUARE", "CL_BRACE", 
                  "CL_PARENTHESIS", "COMMA", "DOT", "COLON", "SEMICOLON", 
                  "PLUS", "MINUS", "MUL", "DIV", "POW", "AND", "OR", "NOT", 
                  "EQ", "DIF", "GREATER", "LESS", "GEQ", "LEQ", "ASSIGN", 
                  "COMMENT_LINE", "COMM_OPEN", "COMM_CLOSE", "WHITESPACE" ]

    grammarFileName = "brownie_grammar.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None

