# Generated from mlang.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .mlangParser import mlangParser
else:
    from mlangParser import mlangParser

# This class defines a complete generic visitor for a parse tree produced by mlangParser.

class mlangVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by mlangParser#program.
    def visitProgram(self, ctx:mlangParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mlangParser#statement.
    def visitStatement(self, ctx:mlangParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mlangParser#variableDecl.
    def visitVariableDecl(self, ctx:mlangParser.VariableDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mlangParser#assignStmt.
    def visitAssignStmt(self, ctx:mlangParser.AssignStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mlangParser#printStmt.
    def visitPrintStmt(self, ctx:mlangParser.PrintStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mlangParser#expr.
    def visitExpr(self, ctx:mlangParser.ExprContext):
        return self.visitChildren(ctx)



del mlangParser