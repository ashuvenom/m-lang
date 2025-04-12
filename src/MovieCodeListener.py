# Generated from MovieCode.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .MovieCodeParser import MovieCodeParser
else:
    from MovieCodeParser import MovieCodeParser

# This class defines a complete listener for a parse tree produced by MovieCodeParser.
class MovieCodeListener(ParseTreeListener):

    # Enter a parse tree produced by MovieCodeParser#program.
    def enterProgram(self, ctx:MovieCodeParser.ProgramContext):
        pass

    # Exit a parse tree produced by MovieCodeParser#program.
    def exitProgram(self, ctx:MovieCodeParser.ProgramContext):
        pass


    # Enter a parse tree produced by MovieCodeParser#statement.
    def enterStatement(self, ctx:MovieCodeParser.StatementContext):
        pass

    # Exit a parse tree produced by MovieCodeParser#statement.
    def exitStatement(self, ctx:MovieCodeParser.StatementContext):
        pass


    # Enter a parse tree produced by MovieCodeParser#variableDecl.
    def enterVariableDecl(self, ctx:MovieCodeParser.VariableDeclContext):
        pass

    # Exit a parse tree produced by MovieCodeParser#variableDecl.
    def exitVariableDecl(self, ctx:MovieCodeParser.VariableDeclContext):
        pass


    # Enter a parse tree produced by MovieCodeParser#assignStmt.
    def enterAssignStmt(self, ctx:MovieCodeParser.AssignStmtContext):
        pass

    # Exit a parse tree produced by MovieCodeParser#assignStmt.
    def exitAssignStmt(self, ctx:MovieCodeParser.AssignStmtContext):
        pass


    # Enter a parse tree produced by MovieCodeParser#printStmt.
    def enterPrintStmt(self, ctx:MovieCodeParser.PrintStmtContext):
        pass

    # Exit a parse tree produced by MovieCodeParser#printStmt.
    def exitPrintStmt(self, ctx:MovieCodeParser.PrintStmtContext):
        pass


    # Enter a parse tree produced by MovieCodeParser#expr.
    def enterExpr(self, ctx:MovieCodeParser.ExprContext):
        pass

    # Exit a parse tree produced by MovieCodeParser#expr.
    def exitExpr(self, ctx:MovieCodeParser.ExprContext):
        pass



del MovieCodeParser