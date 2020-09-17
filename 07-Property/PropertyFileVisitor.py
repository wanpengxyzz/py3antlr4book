# Generated from PropertyFile.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .PropertyFileParser import PropertyFileParser
else:
    from PropertyFileParser import PropertyFileParser

# This class defines a complete generic visitor for a parse tree produced by PropertyFileParser.

class PropertyFileVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by PropertyFileParser#top.
    def visitTop(self, ctx:PropertyFileParser.TopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PropertyFileParser#prop.
    def visitProp(self, ctx:PropertyFileParser.PropContext):
        return self.visitChildren(ctx)



del PropertyFileParser