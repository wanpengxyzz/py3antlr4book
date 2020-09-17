__author__ = 'jszheng'

import sys
from antlr4 import *
from antlr4.InputStream import InputStream
from ExprLexer import ExprLexer
from ExprParser import ExprParser
defaultencoding = 'utf-8'
if sys.getdefaultencoding() != defaultencoding:
    reload(sys)
    sys.setdefaultencoding(defaultencoding)
if __name__ == '__main__':
    if len(sys.argv) > 1:
        input_stream = FileStream(sys.argv[1],encoding="utf-8")
    else:
        input_stream = InputStream(sys.stdin.readline())

    lexer = ExprLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = ExprParser(token_stream)
    tree = parser.prog()
    print(tree.getText())
    lisp_tree_str = tree.toStringTree(recog=parser)
    print(lisp_tree_str)

