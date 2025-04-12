# Generated from MovieCode.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .MovieCodeParser import MovieCodeParser
else:
    from MovieCodeParser import MovieCodeParser

# This class defines a complete generic visitor for a parse tree produced by MovieCodeParser.

class MovieCodeVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MovieCodeParser#program.
    def visitProgram(self, ctx:MovieCodeParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MovieCodeParser#statement.
    def visitStatement(self, ctx:MovieCodeParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MovieCodeParser#variableDecl.
    def visitVariableDecl(self, ctx:MovieCodeParser.VariableDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MovieCodeParser#assignStmt.
    def visitAssignStmt(self, ctx:MovieCodeParser.AssignStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MovieCodeParser#printStmt.
    def visitPrintStmt(self, ctx:MovieCodeParser.PrintStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MovieCodeParser#expr.
    def visitExpr(self, ctx:MovieCodeParser.ExprContext):
        return self.visitChildren(ctx)



del MovieCodeParser