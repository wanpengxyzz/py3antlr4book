# Generated from Expr.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .ExprParser import ExprParser
else:
    from ExprParser import ExprParser

# This class defines a complete listener for a parse tree produced by ExprParser.
class ExprListener(ParseTreeListener):

    # Enter a parse tree produced by ExprParser#prog.
    def enterProg(self, ctx:ExprParser.ProgContext):
        pass

    # Exit a parse tree produced by ExprParser#prog.
    def exitProg(self, ctx:ExprParser.ProgContext):
        pass


    # Enter a parse tree produced by ExprParser#STATE_EXPR.
    def enterSTATE_EXPR(self, ctx:ExprParser.STATE_EXPRContext):
        pass

    # Exit a parse tree produced by ExprParser#STATE_EXPR.
    def exitSTATE_EXPR(self, ctx:ExprParser.STATE_EXPRContext):
        pass


    # Enter a parse tree produced by ExprParser#STATE_ID.
    def enterSTATE_ID(self, ctx:ExprParser.STATE_IDContext):
        pass

    # Exit a parse tree produced by ExprParser#STATE_ID.
    def exitSTATE_ID(self, ctx:ExprParser.STATE_IDContext):
        pass


    # Enter a parse tree produced by ExprParser#STATE_NEWLINE.
    def enterSTATE_NEWLINE(self, ctx:ExprParser.STATE_NEWLINEContext):
        pass

    # Exit a parse tree produced by ExprParser#STATE_NEWLINE.
    def exitSTATE_NEWLINE(self, ctx:ExprParser.STATE_NEWLINEContext):
        pass


    # Enter a parse tree produced by ExprParser#EXPR_AM.
    def enterEXPR_AM(self, ctx:ExprParser.EXPR_AMContext):
        pass

    # Exit a parse tree produced by ExprParser#EXPR_AM.
    def exitEXPR_AM(self, ctx:ExprParser.EXPR_AMContext):
        pass


    # Enter a parse tree produced by ExprParser#EXPR_ID.
    def enterEXPR_ID(self, ctx:ExprParser.EXPR_IDContext):
        pass

    # Exit a parse tree produced by ExprParser#EXPR_ID.
    def exitEXPR_ID(self, ctx:ExprParser.EXPR_IDContext):
        pass


    # Enter a parse tree produced by ExprParser#EXPR_C.
    def enterEXPR_C(self, ctx:ExprParser.EXPR_CContext):
        pass

    # Exit a parse tree produced by ExprParser#EXPR_C.
    def exitEXPR_C(self, ctx:ExprParser.EXPR_CContext):
        pass


    # Enter a parse tree produced by ExprParser#EXPR_MD.
    def enterEXPR_MD(self, ctx:ExprParser.EXPR_MDContext):
        pass

    # Exit a parse tree produced by ExprParser#EXPR_MD.
    def exitEXPR_MD(self, ctx:ExprParser.EXPR_MDContext):
        pass


    # Enter a parse tree produced by ExprParser#EXPR_INT.
    def enterEXPR_INT(self, ctx:ExprParser.EXPR_INTContext):
        pass

    # Exit a parse tree produced by ExprParser#EXPR_INT.
    def exitEXPR_INT(self, ctx:ExprParser.EXPR_INTContext):
        pass



del ExprParser