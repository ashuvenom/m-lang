import sys
from antlr4 import *
from MarathiCodeLexer import MarathiCodeLexer
from MarathiCodeParser import MarathiCodeParser
from MarathiInterpreter import MarathiInterpreter

def main():
    input_stream = FileStream(sys.argv[1])
    lexer = MarathiCodeLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = MarathiCodeParser(stream)
    tree = parser.program()

    print(tree.toStringTree(recog=parser))  # Optional: see the parse tree

    interpreter = MarathiInterpreter()
    interpreter.visit(tree)

if __name__ == '__main__':
    main()
