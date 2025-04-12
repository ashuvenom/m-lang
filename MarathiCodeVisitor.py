# Generated from MarathiCode.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .MarathiCodeParser import MarathiCodeParser
else:
    from MarathiCodeParser import MarathiCodeParser

# This class defines a complete generic visitor for a parse tree produced by MarathiCodeParser.

class MarathiCodeVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MarathiCodeParser#program.
    def visitProgram(self, ctx:MarathiCodeParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MarathiCodeParser#statement.
    def visitStatement(self, ctx:MarathiCodeParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MarathiCodeParser#variableDecl.
    def visitVariableDecl(self, ctx:MarathiCodeParser.VariableDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MarathiCodeParser#assignStmt.
    def visitAssignStmt(self, ctx:MarathiCodeParser.AssignStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MarathiCodeParser#printStmt.
    def visitPrintStmt(self, ctx:MarathiCodeParser.PrintStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MarathiCodeParser#expr.
    def visitExpr(self, ctx:MarathiCodeParser.ExprContext):
        return self.visitChildren(ctx)



del MarathiCodeParser