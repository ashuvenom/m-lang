from MarathiCodeVisitor import MarathiCodeVisitor

class MarathiInterpreter(MarathiCodeVisitor):
    def __init__(self):
        self.memory = {}

    def visitProgram(self, ctx):
        for stmt in ctx.statement():
            self.visit(stmt)

    def visitVariableDecl(self, ctx):
        var = ctx.ID().getText()
        value = self.visit(ctx.expr())
        self.memory[var] = value

    def visitAssignStmt(self, ctx):
        var = ctx.ID().getText()
        value = self.visit(ctx.expr())
        self.memory[var] = value

    def visitPrintStmt(self, ctx):
        value = self.visit(ctx.expr())
        print(value)

    def visitExpr(self, ctx):
        if ctx.INT():
            return int(ctx.INT().getText())
        elif ctx.ID():
            return self.memory.get(ctx.ID().getText(), 0)
        elif ctx.op:
            left = self.visit(ctx.expr(0))
            right = self.visit(ctx.expr(1))
            if ctx.op.text == '+': return left + right
            if ctx.op.text == '-': return left - right
            if ctx.op.text == '*': return left * right
            if ctx.op.text == '/': return left // right
        return 0
