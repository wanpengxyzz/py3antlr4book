# Generated from Rows.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .RowsParser import RowsParser
else:
    from RowsParser import RowsParser

# This class defines a complete generic visitor for a parse tree produced by RowsParser.

class RowsVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by RowsParser#rows.
    def visitRows(self, ctx:RowsParser.RowsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RowsParser#row.
    def visitRow(self, ctx:RowsParser.RowContext):
        return self.visitChildren(ctx)



del RowsParser