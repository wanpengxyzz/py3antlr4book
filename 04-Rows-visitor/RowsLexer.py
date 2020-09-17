# Generated from Rows.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\5")
        buf.write("\27\b\1\4\2\t\2\4\3\t\3\4\4\t\4\3\2\3\2\3\2\3\2\3\3\5")
        buf.write("\3\17\n\3\3\3\3\3\3\4\6\4\24\n\4\r\4\16\4\25\2\2\5\3\3")
        buf.write("\5\4\7\5\3\2\3\4\2\13\f\17\17\2\30\2\3\3\2\2\2\2\5\3\2")
        buf.write("\2\2\2\7\3\2\2\2\3\t\3\2\2\2\5\16\3\2\2\2\7\23\3\2\2\2")
        buf.write("\t\n\7\13\2\2\n\13\3\2\2\2\13\f\b\2\2\2\f\4\3\2\2\2\r")
        buf.write("\17\7\17\2\2\16\r\3\2\2\2\16\17\3\2\2\2\17\20\3\2\2\2")
        buf.write("\20\21\7\f\2\2\21\6\3\2\2\2\22\24\n\2\2\2\23\22\3\2\2")
        buf.write("\2\24\25\3\2\2\2\25\23\3\2\2\2\25\26\3\2\2\2\26\b\3\2")
        buf.write("\2\2\5\2\16\25\3\b\2\2")
        return buf.getvalue()


class RowsLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    TAB = 1
    NL = 2
    STUFF = 3

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'\t'" ]

    symbolicNames = [ "<INVALID>",
            "TAB", "NL", "STUFF" ]

    ruleNames = [ "TAB", "NL", "STUFF" ]

    grammarFileName = "Rows.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


