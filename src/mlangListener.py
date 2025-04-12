# Generated from mlang.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .mlangParser import mlangParser
else:
    from mlangParser import mlangParser

# This class defines a complete listener for a parse tree produced by mlangParser.
class mlangListener(ParseTreeListener):

    # Enter a parse tree produced by mlangParser#program.
    def enterProgram(self, ctx:mlangParser.ProgramContext):
        pass

    # Exit a parse tree produced by mlangParser#program.
    def exitProgram(self, ctx:mlangParser.ProgramContext):
        pass


    # Enter a parse tree produced by mlangParser#statement.
    def enterStatement(self, ctx:mlangParser.StatementContext):
        pass

    # Exit a parse tree produced by mlangParser#statement.
    def exitStatement(self, ctx:mlangParser.StatementContext):
        pass


    # Enter a parse tree produced by mlangParser#variableDecl.
    def enterVariableDecl(self, ctx:mlangParser.VariableDeclContext):
        pass

    # Exit a parse tree produced by mlangParser#variableDecl.
    def exitVariableDecl(self, ctx:mlangParser.VariableDeclContext):
        pass


    # Enter a parse tree produced by mlangParser#assignStmt.
    def enterAssignStmt(self, ctx:mlangParser.AssignStmtContext):
        pass

    # Exit a parse tree produced by mlangParser#assignStmt.
    def exitAssignStmt(self, ctx:mlangParser.AssignStmtContext):
        pass


    # Enter a parse tree produced by mlangParser#printStmt.
    def enterPrintStmt(self, ctx:mlangParser.PrintStmtContext):
        pass

    # Exit a parse tree produced by mlangParser#printStmt.
    def exitPrintStmt(self, ctx:mlangParser.PrintStmtContext):
        pass


    # Enter a parse tree produced by mlangParser#expr.
    def enterExpr(self, ctx:mlangParser.ExprContext):
        pass

    # Exit a parse tree produced by mlangParser#expr.
    def exitExpr(self, ctx:mlangParser.ExprContext):
        pass



del mlangParser