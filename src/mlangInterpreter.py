from mlangVisitor import mlangVisitor

class BreakSignal(Exception): pass
class ContinueSignal(Exception): pass

class mlangInterpreter(mlangVisitor):
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

    def visitIfStmt(self, ctx):
        if self.visit(ctx.expr()):
            for stmt in ctx.statement():
                self.visit(stmt)
        else:
            for elif_ctx in ctx.elifStmt():
                if self.visit(elif_ctx.expr()):
                    for stmt in elif_ctx.statement():
                        self.visit(stmt)
                    return
            if ctx.elseStmt():
                for stmt in ctx.elseStmt().statement():
                    self.visit(stmt)

    def visitWhileStmt(self, ctx):
        try:
            while self.visit(ctx.expr()):
                try:
                    for stmt in ctx.statement():
                        self.visit(stmt)
                except ContinueSignal:
                    continue
        except BreakSignal:
            pass

    def visitForStmt(self, ctx):
        self.visit(ctx.variableDecl())
        try:
            while self.visit(ctx.expr()):
                try:
                    for stmt in ctx.statement():
                        self.visit(stmt)
                except ContinueSignal:
                    pass
                self.visit(ctx.assignStmt())
        except BreakSignal:
            pass

    def visitBreakStmt(self, ctx):
        raise BreakSignal()

    def visitContinueStmt(self, ctx):
        raise ContinueSignal()

    def visitExpr(self, ctx):
        if ctx.INT():
            return int(ctx.INT().getText())
        elif ctx.BOOL():
            return ctx.BOOL().getText() == 'truth'
        elif ctx.STRING():
            return ctx.STRING().getText()[1:-1]  # Remove the quotes
        elif ctx.ID():
            return self.memory.get(ctx.ID().getText(), 0)
        elif ctx.op:
            left = self.visit(ctx.expr(0))
            right = self.visit(ctx.expr(1)) if ctx.expr(1) else None

            if ctx.op.text == '+': return left + right
            if ctx.op.text == '-': return left - right
            if ctx.op.text == '*': return left * right
            if ctx.op.text == '/': return left // right
            if ctx.op.text == '%': return left % right
            if ctx.op.text == 'andAlso': return left and right
            if ctx.op.text == 'orElse': return left or right
            if ctx.op.text == 'sameAs': return left == right
            if ctx.op.text == 'notSame': return left != right
            if ctx.op.text == 'smallerThan': return left < right
            if ctx.op.text == 'biggerThan': return left > right
            if ctx.op.text == 'biggerOrEqual': return left >= right
            if ctx.op.text == 'smallerOrEqual': return left <= right    
        elif ctx.getChild(0).getText() == 'not':
            value = self.visit(ctx.expr(0))
            return not value
        return 0
