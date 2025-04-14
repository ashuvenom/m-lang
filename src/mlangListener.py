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


    # Enter a parse tree produced by mlangParser#ifStmt.
    def enterIfStmt(self, ctx:mlangParser.IfStmtContext):
        pass

    # Exit a parse tree produced by mlangParser#ifStmt.
    def exitIfStmt(self, ctx:mlangParser.IfStmtContext):
        pass


    # Enter a parse tree produced by mlangParser#elifStmt.
    def enterElifStmt(self, ctx:mlangParser.ElifStmtContext):
        pass

    # Exit a parse tree produced by mlangParser#elifStmt.
    def exitElifStmt(self, ctx:mlangParser.ElifStmtContext):
        pass


    # Enter a parse tree produced by mlangParser#elseStmt.
    def enterElseStmt(self, ctx:mlangParser.ElseStmtContext):
        pass

    # Exit a parse tree produced by mlangParser#elseStmt.
    def exitElseStmt(self, ctx:mlangParser.ElseStmtContext):
        pass


    # Enter a parse tree produced by mlangParser#whileStmt.
    def enterWhileStmt(self, ctx:mlangParser.WhileStmtContext):
        pass

    # Exit a parse tree produced by mlangParser#whileStmt.
    def exitWhileStmt(self, ctx:mlangParser.WhileStmtContext):
        pass


    # Enter a parse tree produced by mlangParser#forStmt.
    def enterForStmt(self, ctx:mlangParser.ForStmtContext):
        pass

    # Exit a parse tree produced by mlangParser#forStmt.
    def exitForStmt(self, ctx:mlangParser.ForStmtContext):
        pass


    # Enter a parse tree produced by mlangParser#breakStmt.
    def enterBreakStmt(self, ctx:mlangParser.BreakStmtContext):
        pass

    # Exit a parse tree produced by mlangParser#breakStmt.
    def exitBreakStmt(self, ctx:mlangParser.BreakStmtContext):
        pass


    # Enter a parse tree produced by mlangParser#continueStmt.
    def enterContinueStmt(self, ctx:mlangParser.ContinueStmtContext):
        pass

    # Exit a parse tree produced by mlangParser#continueStmt.
    def exitContinueStmt(self, ctx:mlangParser.ContinueStmtContext):
        pass


    # Enter a parse tree produced by mlangParser#expr.
    def enterExpr(self, ctx:mlangParser.ExprContext):
        pass

    # Exit a parse tree produced by mlangParser#expr.
    def exitExpr(self, ctx:mlangParser.ExprContext):
        pass



del mlangParser