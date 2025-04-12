import sys
from antlr4 import *
from MovieCodeLexer import MovieCodeLexer
from MovieCodeParser import MovieCodeParser
from MovieInterpreter import MovieInterpreter

def main():
    input_stream = FileStream(sys.argv[1])
    lexer = MovieCodeLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = MovieCodeParser(stream)
    tree = parser.program()

    # print(tree.toStringTree(recog=parser)) 

    interpreter = MovieInterpreter()
    interpreter.visit(tree)

if __name__ == '__main__':
    main()
