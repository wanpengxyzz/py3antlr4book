import sys
from antlr4 import *
from antlr4.InputStream import InputStream
from antlr4.TokenStreamRewriter import TokenStreamRewriter

from PropertyFileLexer import PropertyFileLexer
from PropertyFileParser import PropertyFileParser
from PropertyFileVisitor import PropertyFileVisitor


class PropertyFileLoader(PropertyFileVisitor):
    def __init__(self,rewriter):
        super().__init__()
        self.props = {}
        self.rewriter=rewriter

    def visitProp(self, ctx):
        print("visitProp:")
        ctx.businessnode=1
        rewriter.replace("top", ctx.stop.tokenIndex-1, ctx.stop.tokenIndex-1, "helo")
        #rewriter.insertBeforeToken(ctx.stop,"text to put after t| ","top"); 
        print(dir(ctx))
        self.props[ctx.ID().getText()] = ctx.STRING().getText()
    
    def visitTop(self, ctx):
        print("visitTop")
        self.visitChildren(ctx)

    def show(self):
        print(rewriter.getText("top",0,100))
        for (key, value) in self.props.items():
            print(key, '=>', value)

if __name__ == '__main__':
    if len(sys.argv) > 1:
        input_stream = FileStream(sys.argv[1])
    else:
        input_stream = InputStream(sys.stdin.read())
    lexer = PropertyFileLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    rewriter = TokenStreamRewriter(token_stream)
    parser = PropertyFileParser(token_stream)
    tree = parser.top()

    visitor = PropertyFileLoader(rewriter)
    visitor.visit(tree)
    print("HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH")
    #visitor.visit(tree) #已经被visit遍历过，且已经改变了原始的token_stream的，不能继续visit，否则会出错
    visitor.show()
    print("rewriter HHHHHHHHHHHHHHHHHH")
