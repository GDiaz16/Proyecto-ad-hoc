import io
import antlr4

from Compiler.Visitor import Visitor
from Compiler.Code_generator import Code_generator as Generator
from gen.brownieLexer import brownieLexer
from gen.brownieParser import brownieParser

class compiler:
    def __init__(self):
        stream = antlr4.InputStream(io.open("tests.br").read())
        lexer = brownieLexer(stream)
        tok_stream = antlr4.CommonTokenStream(lexer)
        parser = brownieParser(tok_stream)

        parserTree = parser.start()
        visitor = Visitor()
        visitor.visit(parserTree)
        instructions = visitor.instructions
        symbols = visitor.symbols_table
        generator = Generator(instructions,symbols)
        self.code = generator.assembly

compiler = compiler()





