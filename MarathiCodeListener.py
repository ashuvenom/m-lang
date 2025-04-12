# Generated from MarathiCode.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .MarathiCodeParser import MarathiCodeParser
else:
    from MarathiCodeParser import MarathiCodeParser

# This class defines a complete listener for a parse tree produced by MarathiCodeParser.
class MarathiCodeListener(ParseTreeListener):

    # Enter a parse tree produced by MarathiCodeParser#program.
    def enterProgram(self, ctx:MarathiCodeParser.ProgramContext):
        pass

    # Exit a parse tree produced by MarathiCodeParser#program.
    def exitProgram(self, ctx:MarathiCodeParser.ProgramContext):
        pass


    # Enter a parse tree produced by MarathiCodeParser#statement.
    def enterStatement(self, ctx:MarathiCodeParser.StatementContext):
        pass

    # Exit a parse tree produced by MarathiCodeParser#statement.
    def exitStatement(self, ctx:MarathiCodeParser.StatementContext):
        pass


    # Enter a parse tree produced by MarathiCodeParser#variableDecl.
    def enterVariableDecl(self, ctx:MarathiCodeParser.VariableDeclContext):
        pass

    # Exit a parse tree produced by MarathiCodeParser#variableDecl.
    def exitVariableDecl(self, ctx:MarathiCodeParser.VariableDeclContext):
        pass


    # Enter a parse tree produced by MarathiCodeParser#assignStmt.
    def enterAssignStmt(self, ctx:MarathiCodeParser.AssignStmtContext):
        pass

    # Exit a parse tree produced by MarathiCodeParser#assignStmt.
    def exitAssignStmt(self, ctx:MarathiCodeParser.AssignStmtContext):
        pass


    # Enter a parse tree produced by MarathiCodeParser#printStmt.
    def enterPrintStmt(self, ctx:MarathiCodeParser.PrintStmtContext):
        pass

    # Exit a parse tree produced by MarathiCodeParser#printStmt.
    def exitPrintStmt(self, ctx:MarathiCodeParser.PrintStmtContext):
        pass


    # Enter a parse tree produced by MarathiCodeParser#expr.
    def enterExpr(self, ctx:MarathiCodeParser.ExprContext):
        pass

    # Exit a parse tree produced by MarathiCodeParser#expr.
    def exitExpr(self, ctx:MarathiCodeParser.ExprContext):
        pass



del MarathiCodeParser