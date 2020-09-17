# Generated from PropertyFile.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\7")
        buf.write(",\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\3\2\3\2")
        buf.write("\3\3\3\3\3\4\3\4\3\4\3\4\7\4\26\n\4\f\4\16\4\31\13\4\3")
        buf.write("\4\3\4\3\4\3\4\3\5\6\5 \n\5\r\5\16\5!\3\6\3\6\7\6&\n\6")
        buf.write("\f\6\16\6)\13\6\3\6\3\6\4\27\'\2\7\3\3\5\4\7\5\t\6\13")
        buf.write("\7\3\2\3\3\2c|\2.\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2")
        buf.write("\2\t\3\2\2\2\2\13\3\2\2\2\3\r\3\2\2\2\5\17\3\2\2\2\7\21")
        buf.write("\3\2\2\2\t\37\3\2\2\2\13#\3\2\2\2\r\16\7?\2\2\16\4\3\2")
        buf.write("\2\2\17\20\7\f\2\2\20\6\3\2\2\2\21\22\7\61\2\2\22\23\7")
        buf.write("\61\2\2\23\27\3\2\2\2\24\26\13\2\2\2\25\24\3\2\2\2\26")
        buf.write("\31\3\2\2\2\27\30\3\2\2\2\27\25\3\2\2\2\30\32\3\2\2\2")
        buf.write("\31\27\3\2\2\2\32\33\7\f\2\2\33\34\3\2\2\2\34\35\b\4\2")
        buf.write("\2\35\b\3\2\2\2\36 \t\2\2\2\37\36\3\2\2\2 !\3\2\2\2!\37")
        buf.write("\3\2\2\2!\"\3\2\2\2\"\n\3\2\2\2#\'\7$\2\2$&\13\2\2\2%")
        buf.write("$\3\2\2\2&)\3\2\2\2\'(\3\2\2\2\'%\3\2\2\2(*\3\2\2\2)\'")
        buf.write("\3\2\2\2*+\7$\2\2+\f\3\2\2\2\6\2\27!\'\3\2\4\2")
        return buf.getvalue()


class PropertyFileLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    SL_COMMENT = 3
    ID = 4
    STRING = 5

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'='", "'\n'" ]

    symbolicNames = [ "<INVALID>",
            "SL_COMMENT", "ID", "STRING" ]

    ruleNames = [ "T__0", "T__1", "SL_COMMENT", "ID", "STRING" ]

    grammarFileName = "PropertyFile.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def startFile(self):
        pass
    def finishFile(self):
        pass
    def defineProperty(self, name, value):
        pass


