import io
import antlr4

from Compiler.Visitor import Visitor
from gen.brownieLexer import brownieLexer
from gen.brownieParser import brownieParser

stream = antlr4.InputStream(io.open("tests.br").read())
lexer = brownieLexer(stream)
tok_stream = antlr4.CommonTokenStream(lexer)
parser = brownieParser(tok_stream)

parserTree = parser.start()
visitor = Visitor()
visitor.visit(parserTree)

