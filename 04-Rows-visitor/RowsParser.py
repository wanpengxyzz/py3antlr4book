# Generated from Rows.g4 by ANTLR 4.8
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\5")
        buf.write("\24\4\2\t\2\4\3\t\3\3\2\3\2\3\2\6\2\n\n\2\r\2\16\2\13")
        buf.write("\3\3\3\3\6\3\20\n\3\r\3\16\3\21\3\3\2\2\4\2\4\2\2\2\23")
        buf.write("\2\t\3\2\2\2\4\17\3\2\2\2\6\7\5\4\3\2\7\b\7\4\2\2\b\n")
        buf.write("\3\2\2\2\t\6\3\2\2\2\n\13\3\2\2\2\13\t\3\2\2\2\13\f\3")
        buf.write("\2\2\2\f\3\3\2\2\2\r\16\7\5\2\2\16\20\b\3\1\2\17\r\3\2")
        buf.write("\2\2\20\21\3\2\2\2\21\17\3\2\2\2\21\22\3\2\2\2\22\5\3")
        buf.write("\2\2\2\4\13\21")
        return buf.getvalue()


class RowsParser ( Parser ):

    grammarFileName = "Rows.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'\t'" ]

    symbolicNames = [ "<INVALID>", "TAB", "NL", "STUFF" ]

    RULE_rows = 0
    RULE_row = 1

    ruleNames =  [ "rows", "row" ]

    EOF = Token.EOF
    TAB=1
    NL=2
    STUFF=3

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    @property
    def column(self):
        return self._col

    @column.setter
    def column(self, value):
        self._col = value




    class RowsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def row(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RowsParser.RowContext)
            else:
                return self.getTypedRuleContext(RowsParser.RowContext,i)


        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(RowsParser.NL)
            else:
                return self.getToken(RowsParser.NL, i)

        def getRuleIndex(self):
            return RowsParser.RULE_rows

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRows" ):
                listener.enterRows(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRows" ):
                listener.exitRows(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRows" ):
                return visitor.visitRows(self)
            else:
                return visitor.visitChildren(self)




    def rows(self):

        localctx = RowsParser.RowsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_rows)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 7 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 4
                self.row()
                self.state = 5
                self.match(RowsParser.NL)
                self.state = 9 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==RowsParser.STUFF):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RowContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.i = 0
            self._STUFF = None # Token

        def STUFF(self, i:int=None):
            if i is None:
                return self.getTokens(RowsParser.STUFF)
            else:
                return self.getToken(RowsParser.STUFF, i)

        def getRuleIndex(self):
            return RowsParser.RULE_row

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRow" ):
                listener.enterRow(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRow" ):
                listener.exitRow(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRow" ):
                return visitor.visitRow(self)
            else:
                return visitor.visitChildren(self)




    def row(self):

        localctx = RowsParser.RowContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_row)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 13 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 11
                localctx._STUFF = self.match(RowsParser.STUFF)

                localctx.i = localctx.i + 1
                if localctx.i == self.column:
                    print((None if localctx._STUFF is None else localctx._STUFF.text))

                self.state = 15 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==RowsParser.STUFF):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





