# Generated from PropertyFile.g4 by ANTLR 4.8
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\7")
        buf.write("\25\4\2\t\2\4\3\t\3\3\2\3\2\6\2\t\n\2\r\2\16\2\n\3\2\3")
        buf.write("\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\2\2\4\2\4\2\2\2\23\2\6")
        buf.write("\3\2\2\2\4\16\3\2\2\2\6\b\b\2\1\2\7\t\5\4\3\2\b\7\3\2")
        buf.write("\2\2\t\n\3\2\2\2\n\b\3\2\2\2\n\13\3\2\2\2\13\f\3\2\2\2")
        buf.write("\f\r\b\2\1\2\r\3\3\2\2\2\16\17\7\6\2\2\17\20\7\3\2\2\20")
        buf.write("\21\7\7\2\2\21\22\7\4\2\2\22\23\b\3\1\2\23\5\3\2\2\2\3")
        buf.write("\n")
        return buf.getvalue()


class PropertyFileParser ( Parser ):

    grammarFileName = "PropertyFile.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'='", "'\n'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "SL_COMMENT", 
                      "ID", "STRING" ]

    RULE_top = 0
    RULE_prop = 1

    ruleNames =  [ "top", "prop" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    SL_COMMENT=3
    ID=4
    STRING=5

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    def startFile(self):
        pass
    def finishFile(self):
        pass
    def defineProperty(self, name, value):
        pass



    class TopContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def prop(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PropertyFileParser.PropContext)
            else:
                return self.getTypedRuleContext(PropertyFileParser.PropContext,i)


        def getRuleIndex(self):
            return PropertyFileParser.RULE_top

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTop" ):
                listener.enterTop(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTop" ):
                listener.exitTop(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTop" ):
                return visitor.visitTop(self)
            else:
                return visitor.visitChildren(self)




    def top(self):

        localctx = PropertyFileParser.TopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_top)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.startFile()
            self.state = 6 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 5
                self.prop()
                self.state = 8 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==PropertyFileParser.ID):
                    break

            self.finishFile()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PropContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._ID = None # Token
            self._STRING = None # Token

        def ID(self):
            return self.getToken(PropertyFileParser.ID, 0)

        def STRING(self):
            return self.getToken(PropertyFileParser.STRING, 0)

        def getRuleIndex(self):
            return PropertyFileParser.RULE_prop

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProp" ):
                listener.enterProp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProp" ):
                listener.exitProp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProp" ):
                return visitor.visitProp(self)
            else:
                return visitor.visitChildren(self)




    def prop(self):

        localctx = PropertyFileParser.PropContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_prop)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 12
            localctx._ID = self.match(PropertyFileParser.ID)
            self.state = 13
            self.match(PropertyFileParser.T__0)
            self.state = 14
            localctx._STRING = self.match(PropertyFileParser.STRING)
            self.state = 15
            self.match(PropertyFileParser.T__1)
            self.defineProperty(localctx._ID, localctx._STRING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





