# Generated from mlang.g4 by ANTLR 4.13.0
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,15,63,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,1,0,5,
        0,14,8,0,10,0,12,0,17,9,0,1,0,1,0,1,1,1,1,1,1,3,1,24,8,1,1,2,1,2,
        1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,3,1,4,1,4,1,4,1,4,1,5,1,5,1,5,
        1,5,1,5,1,5,3,5,47,8,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,5,5,58,
        8,5,10,5,12,5,61,9,5,1,5,0,1,10,6,0,2,4,6,8,10,0,3,1,0,5,6,1,0,7,
        8,1,0,9,10,65,0,15,1,0,0,0,2,23,1,0,0,0,4,25,1,0,0,0,6,31,1,0,0,
        0,8,36,1,0,0,0,10,46,1,0,0,0,12,14,3,2,1,0,13,12,1,0,0,0,14,17,1,
        0,0,0,15,13,1,0,0,0,15,16,1,0,0,0,16,18,1,0,0,0,17,15,1,0,0,0,18,
        19,5,0,0,1,19,1,1,0,0,0,20,24,3,4,2,0,21,24,3,6,3,0,22,24,3,8,4,
        0,23,20,1,0,0,0,23,21,1,0,0,0,23,22,1,0,0,0,24,3,1,0,0,0,25,26,5,
        1,0,0,26,27,5,13,0,0,27,28,5,2,0,0,28,29,3,10,5,0,29,30,5,3,0,0,
        30,5,1,0,0,0,31,32,5,13,0,0,32,33,5,2,0,0,33,34,3,10,5,0,34,35,5,
        3,0,0,35,7,1,0,0,0,36,37,5,4,0,0,37,38,3,10,5,0,38,39,5,3,0,0,39,
        9,1,0,0,0,40,41,6,5,-1,0,41,42,5,11,0,0,42,47,3,10,5,4,43,47,5,12,
        0,0,44,47,5,14,0,0,45,47,5,13,0,0,46,40,1,0,0,0,46,43,1,0,0,0,46,
        44,1,0,0,0,46,45,1,0,0,0,47,59,1,0,0,0,48,49,10,7,0,0,49,50,7,0,
        0,0,50,58,3,10,5,8,51,52,10,6,0,0,52,53,7,1,0,0,53,58,3,10,5,7,54,
        55,10,5,0,0,55,56,7,2,0,0,56,58,3,10,5,6,57,48,1,0,0,0,57,51,1,0,
        0,0,57,54,1,0,0,0,58,61,1,0,0,0,59,57,1,0,0,0,59,60,1,0,0,0,60,11,
        1,0,0,0,61,59,1,0,0,0,5,15,23,46,57,59
    ]

class mlangParser ( Parser ):

    grammarFileName = "mlang.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'cast'", "'is'", "';'", "'say'", "'*'", 
                     "'/'", "'+'", "'-'", "'andAlso'", "'orElse'", "'not'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "BOOL", "ID", "INT", "WS" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_variableDecl = 2
    RULE_assignStmt = 3
    RULE_printStmt = 4
    RULE_expr = 5

    ruleNames =  [ "program", "statement", "variableDecl", "assignStmt", 
                   "printStmt", "expr" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    BOOL=12
    ID=13
    INT=14
    WS=15

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.0")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(mlangParser.EOF, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(mlangParser.StatementContext)
            else:
                return self.getTypedRuleContext(mlangParser.StatementContext,i)


        def getRuleIndex(self):
            return mlangParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = mlangParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 15
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 8210) != 0):
                self.state = 12
                self.statement()
                self.state = 17
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 18
            self.match(mlangParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variableDecl(self):
            return self.getTypedRuleContext(mlangParser.VariableDeclContext,0)


        def assignStmt(self):
            return self.getTypedRuleContext(mlangParser.AssignStmtContext,0)


        def printStmt(self):
            return self.getTypedRuleContext(mlangParser.PrintStmtContext,0)


        def getRuleIndex(self):
            return mlangParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = mlangParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.state = 23
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 20
                self.variableDecl()
                pass
            elif token in [13]:
                self.enterOuterAlt(localctx, 2)
                self.state = 21
                self.assignStmt()
                pass
            elif token in [4]:
                self.enterOuterAlt(localctx, 3)
                self.state = 22
                self.printStmt()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VariableDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(mlangParser.ID, 0)

        def expr(self):
            return self.getTypedRuleContext(mlangParser.ExprContext,0)


        def getRuleIndex(self):
            return mlangParser.RULE_variableDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariableDecl" ):
                listener.enterVariableDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariableDecl" ):
                listener.exitVariableDecl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariableDecl" ):
                return visitor.visitVariableDecl(self)
            else:
                return visitor.visitChildren(self)




    def variableDecl(self):

        localctx = mlangParser.VariableDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_variableDecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 25
            self.match(mlangParser.T__0)
            self.state = 26
            self.match(mlangParser.ID)
            self.state = 27
            self.match(mlangParser.T__1)
            self.state = 28
            self.expr(0)
            self.state = 29
            self.match(mlangParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(mlangParser.ID, 0)

        def expr(self):
            return self.getTypedRuleContext(mlangParser.ExprContext,0)


        def getRuleIndex(self):
            return mlangParser.RULE_assignStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignStmt" ):
                listener.enterAssignStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignStmt" ):
                listener.exitAssignStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignStmt" ):
                return visitor.visitAssignStmt(self)
            else:
                return visitor.visitChildren(self)




    def assignStmt(self):

        localctx = mlangParser.AssignStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_assignStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 31
            self.match(mlangParser.ID)
            self.state = 32
            self.match(mlangParser.T__1)
            self.state = 33
            self.expr(0)
            self.state = 34
            self.match(mlangParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrintStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(mlangParser.ExprContext,0)


        def getRuleIndex(self):
            return mlangParser.RULE_printStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrintStmt" ):
                listener.enterPrintStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrintStmt" ):
                listener.exitPrintStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrintStmt" ):
                return visitor.visitPrintStmt(self)
            else:
                return visitor.visitChildren(self)




    def printStmt(self):

        localctx = mlangParser.PrintStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_printStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 36
            self.match(mlangParser.T__3)
            self.state = 37
            self.expr(0)
            self.state = 38
            self.match(mlangParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.op = None # Token

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(mlangParser.ExprContext)
            else:
                return self.getTypedRuleContext(mlangParser.ExprContext,i)


        def BOOL(self):
            return self.getToken(mlangParser.BOOL, 0)

        def INT(self):
            return self.getToken(mlangParser.INT, 0)

        def ID(self):
            return self.getToken(mlangParser.ID, 0)

        def getRuleIndex(self):
            return mlangParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = mlangParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 10
        self.enterRecursionRule(localctx, 10, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 46
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [11]:
                self.state = 41
                self.match(mlangParser.T__10)
                self.state = 42
                self.expr(4)
                pass
            elif token in [12]:
                self.state = 43
                self.match(mlangParser.BOOL)
                pass
            elif token in [14]:
                self.state = 44
                self.match(mlangParser.INT)
                pass
            elif token in [13]:
                self.state = 45
                self.match(mlangParser.ID)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 59
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 57
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
                    if la_ == 1:
                        localctx = mlangParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 48
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 49
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==5 or _la==6):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 50
                        self.expr(8)
                        pass

                    elif la_ == 2:
                        localctx = mlangParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 51
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 52
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==7 or _la==8):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 53
                        self.expr(7)
                        pass

                    elif la_ == 3:
                        localctx = mlangParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 54
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 55
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==9 or _la==10):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 56
                        self.expr(6)
                        pass

             
                self.state = 61
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[5] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 5)
         




