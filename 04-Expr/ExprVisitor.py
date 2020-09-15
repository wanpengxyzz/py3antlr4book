# Generated from Expr.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .ExprParser import ExprParser
else:
    from ExprParser import ExprParser

# This class defines a complete generic visitor for a parse tree produced by ExprParser.

class ExprVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ExprParser#prog.
    def visitProg(self, ctx:ExprParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#STATE_EXPR.
    def visitSTATE_EXPR(self, ctx:ExprParser.STATE_EXPRContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#STATE_ID.
    def visitSTATE_ID(self, ctx:ExprParser.STATE_IDContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#STATE_NEWLINE.
    def visitSTATE_NEWLINE(self, ctx:ExprParser.STATE_NEWLINEContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#EXPR_AM.
    def visitEXPR_AM(self, ctx:ExprParser.EXPR_AMContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#EXPR_ID.
    def visitEXPR_ID(self, ctx:ExprParser.EXPR_IDContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#EXPR_C.
    def visitEXPR_C(self, ctx:ExprParser.EXPR_CContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#EXPR_MD.
    def visitEXPR_MD(self, ctx:ExprParser.EXPR_MDContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#EXPR_INT.
    def visitEXPR_INT(self, ctx:ExprParser.EXPR_INTContext):
        return self.visitChildren(ctx)



del ExprParser