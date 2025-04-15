from mlangVisitor import mlangVisitor

class BreakSignal(Exception): pass
class ContinueSignal(Exception): pass

class mlangInterpreter(mlangVisitor):
    def __init__(self):
        self.memory = {}
        self.functions = {}
        self.return_value = None

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

    def visitFunctionDecl(self, ctx):
        name = ctx.ID().getText()
        params = [p.getText() for p in ctx.paramList().ID()] if ctx.paramList() else []
        body = ctx.statement()
        self.functions[name] = (params, body)

    def visitFunctionCall(self, ctx):
        return self.visitFunctionCallExpr(ctx.functionCallExpr())

    def visitFunctionCallExpr(self, ctx):
        name = ctx.ID().getText()
        if name not in self.functions:
            raise Exception(f"Function '{name}' not defined.")

        params, body = self.functions[name]
        args = [self.visit(arg) for arg in ctx.argList().expr()] if ctx.argList() else []

        if len(params) != len(args):
            raise Exception(f"Function '{name}' expects {len(params)} args, got {len(args)}.")

        outer_memory = self.memory.copy()
        self.memory = dict(zip(params, args))

        self.return_value = None
        for stmt in body:
            self.visit(stmt)
            if self.return_value is not None:
                break

        result = self.return_value
        self.memory = outer_memory
        self.return_value = None
        return result

    def visitReturnStmt(self, ctx):
        self.return_value = self.visit(ctx.expr())

    def visitExpr(self, ctx):
        if ctx.functionCallExpr():
            return self.visitFunctionCallExpr(ctx.functionCallExpr())

        if ctx.INT():
            return int(ctx.INT().getText())
        elif ctx.BOOL():
            return ctx.BOOL().getText() == 'truth'
        elif ctx.STRING():
            return ctx.STRING().getText()[1:-1]
        elif ctx.ID():
            return self.memory.get(ctx.ID().getText(), 0)
        elif ctx.op:
            left = self.visit(ctx.expr(0))
            right = self.visit(ctx.expr(1)) if ctx.expr(1) else None

            if ctx.op.text == '+':
             # String concatenation if either operand is a string
                if isinstance(left, str) or isinstance(right, str):
                    return str(left) + str(right)
                return left + right
            
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
        elif ctx.getChildCount() == 5 and ctx.getChild(1).getText() == 'cut?':
            condition = self.visit(ctx.expr(0))
            true_expr = self.visit(ctx.expr(1))
            false_expr = self.visit(ctx.expr(2))
            # print(f"DEBUG: condition={condition}, true_expr={true_expr}, false_expr={false_expr}")  
            if bool(condition):  
                return true_expr
            else:
                return false_expr
        elif ctx.getChild(0).getText() == 'not':
            return not self.visit(ctx.expr(0))
        return 0