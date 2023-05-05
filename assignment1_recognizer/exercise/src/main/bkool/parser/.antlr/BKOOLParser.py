# Generated from c:\Users\Admin\Desktop\222_PPL\assignment1_recognizer\exercise\src\main\bkool\parser\BKOOL.g4 by ANTLR 4.9.2
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\27")
        buf.write("\u00da\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\5\3E\n\3\3\4\3\4\5\4")
        buf.write("I\n\4\3\5\3\5\3\5\3\5\3\6\3\6\3\6\5\6R\n\6\3\7\3\7\3\7")
        buf.write("\3\7\5\7X\n\7\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\n")
        buf.write("\3\n\3\n\3\n\5\ng\n\n\3\13\3\13\3\13\3\13\3\13\5\13n\n")
        buf.write("\13\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\5")
        buf.write("\16{\n\16\3\17\3\17\3\17\3\17\5\17\u0081\n\17\3\20\3\20")
        buf.write("\5\20\u0085\n\20\3\21\3\21\3\21\3\22\3\22\3\22\5\22\u008d")
        buf.write("\n\22\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\24\3\25")
        buf.write("\3\25\3\25\3\26\3\26\3\26\3\26\5\26\u009f\n\26\3\27\3")
        buf.write("\27\3\27\3\27\3\27\5\27\u00a6\n\27\3\30\3\30\3\31\3\31")
        buf.write("\3\31\3\31\3\31\5\31\u00af\n\31\3\32\3\32\3\32\3\32\3")
        buf.write("\32\5\32\u00b6\n\32\3\33\3\33\3\33\3\33\3\33\3\33\7\33")
        buf.write("\u00be\n\33\f\33\16\33\u00c1\13\33\3\34\3\34\3\34\3\34")
        buf.write("\3\34\3\34\7\34\u00c9\n\34\f\34\16\34\u00cc\13\34\3\35")
        buf.write("\3\35\3\35\3\35\3\35\3\35\3\35\3\35\5\35\u00d6\n\35\3")
        buf.write("\36\3\36\3\36\2\4\64\66\37\2\4\6\b\n\f\16\20\22\24\26")
        buf.write("\30\32\34\36 \"$&(*,.\60\62\64\668:\2\3\3\2\3\4\2\u00d1")
        buf.write("\2<\3\2\2\2\4D\3\2\2\2\6H\3\2\2\2\bJ\3\2\2\2\nQ\3\2\2")
        buf.write("\2\fW\3\2\2\2\16Y\3\2\2\2\20^\3\2\2\2\22f\3\2\2\2\24m")
        buf.write("\3\2\2\2\26o\3\2\2\2\30r\3\2\2\2\32z\3\2\2\2\34\u0080")
        buf.write("\3\2\2\2\36\u0084\3\2\2\2 \u0086\3\2\2\2\"\u008c\3\2\2")
        buf.write("\2$\u008e\3\2\2\2&\u0092\3\2\2\2(\u0097\3\2\2\2*\u009e")
        buf.write("\3\2\2\2,\u00a5\3\2\2\2.\u00a7\3\2\2\2\60\u00ae\3\2\2")
        buf.write("\2\62\u00b5\3\2\2\2\64\u00b7\3\2\2\2\66\u00c2\3\2\2\2")
        buf.write("8\u00d5\3\2\2\2:\u00d7\3\2\2\2<=\5\6\4\2=>\5\4\3\2>?\7")
        buf.write("\2\2\3?\3\3\2\2\2@A\5\6\4\2AB\5\4\3\2BE\3\2\2\2CE\3\2")
        buf.write("\2\2D@\3\2\2\2DC\3\2\2\2E\5\3\2\2\2FI\5\b\5\2GI\5\16\b")
        buf.write("\2HF\3\2\2\2HG\3\2\2\2I\7\3\2\2\2JK\5:\36\2KL\5\n\6\2")
        buf.write("LM\7\5\2\2M\t\3\2\2\2NO\7\23\2\2OR\5\f\7\2PR\7\23\2\2")
        buf.write("QN\3\2\2\2QP\3\2\2\2R\13\3\2\2\2ST\7\6\2\2TU\7\23\2\2")
        buf.write("UX\5\f\7\2VX\3\2\2\2WS\3\2\2\2WV\3\2\2\2X\r\3\2\2\2YZ")
        buf.write("\5:\36\2Z[\7\23\2\2[\\\5\20\t\2\\]\5\30\r\2]\17\3\2\2")
        buf.write("\2^_\7\7\2\2_`\5\22\n\2`a\7\b\2\2a\21\3\2\2\2bc\5\26\f")
        buf.write("\2cd\5\24\13\2dg\3\2\2\2eg\3\2\2\2fb\3\2\2\2fe\3\2\2\2")
        buf.write("g\23\3\2\2\2hi\7\5\2\2ij\5\26\f\2jk\5\24\13\2kn\3\2\2")
        buf.write("\2ln\3\2\2\2mh\3\2\2\2ml\3\2\2\2n\25\3\2\2\2op\5:\36\2")
        buf.write("pq\5\n\6\2q\27\3\2\2\2rs\7\t\2\2st\5\32\16\2tu\7\n\2\2")
        buf.write("u\31\3\2\2\2vw\5\36\20\2wx\5\34\17\2x{\3\2\2\2y{\3\2\2")
        buf.write("\2zv\3\2\2\2zy\3\2\2\2{\33\3\2\2\2|}\5\36\20\2}~\5\34")
        buf.write("\17\2~\u0081\3\2\2\2\177\u0081\3\2\2\2\u0080|\3\2\2\2")
        buf.write("\u0080\177\3\2\2\2\u0081\35\3\2\2\2\u0082\u0085\5\b\5")
        buf.write("\2\u0083\u0085\5 \21\2\u0084\u0082\3\2\2\2\u0084\u0083")
        buf.write("\3\2\2\2\u0085\37\3\2\2\2\u0086\u0087\5\"\22\2\u0087\u0088")
        buf.write("\7\5\2\2\u0088!\3\2\2\2\u0089\u008d\5$\23\2\u008a\u008d")
        buf.write("\5&\24\2\u008b\u008d\5(\25\2\u008c\u0089\3\2\2\2\u008c")
        buf.write("\u008a\3\2\2\2\u008c\u008b\3\2\2\2\u008d#\3\2\2\2\u008e")
        buf.write("\u008f\7\23\2\2\u008f\u0090\7\13\2\2\u0090\u0091\5.\30")
        buf.write("\2\u0091%\3\2\2\2\u0092\u0093\7\23\2\2\u0093\u0094\7\7")
        buf.write("\2\2\u0094\u0095\5*\26\2\u0095\u0096\7\b\2\2\u0096\'\3")
        buf.write("\2\2\2\u0097\u0098\7\20\2\2\u0098\u0099\5.\30\2\u0099")
        buf.write(")\3\2\2\2\u009a\u009b\5.\30\2\u009b\u009c\5,\27\2\u009c")
        buf.write("\u009f\3\2\2\2\u009d\u009f\3\2\2\2\u009e\u009a\3\2\2\2")
        buf.write("\u009e\u009d\3\2\2\2\u009f+\3\2\2\2\u00a0\u00a1\7\6\2")
        buf.write("\2\u00a1\u00a2\5.\30\2\u00a2\u00a3\5,\27\2\u00a3\u00a6")
        buf.write("\3\2\2\2\u00a4\u00a6\3\2\2\2\u00a5\u00a0\3\2\2\2\u00a5")
        buf.write("\u00a4\3\2\2\2\u00a6-\3\2\2\2\u00a7\u00a8\5\60\31\2\u00a8")
        buf.write("/\3\2\2\2\u00a9\u00aa\5\62\32\2\u00aa\u00ab\7\f\2\2\u00ab")
        buf.write("\u00ac\5\60\31\2\u00ac\u00af\3\2\2\2\u00ad\u00af\5\62")
        buf.write("\32\2\u00ae\u00a9\3\2\2\2\u00ae\u00ad\3\2\2\2\u00af\61")
        buf.write("\3\2\2\2\u00b0\u00b1\5\64\33\2\u00b1\u00b2\7\r\2\2\u00b2")
        buf.write("\u00b3\5\64\33\2\u00b3\u00b6\3\2\2\2\u00b4\u00b6\5\64")
        buf.write("\33\2\u00b5\u00b0\3\2\2\2\u00b5\u00b4\3\2\2\2\u00b6\63")
        buf.write("\3\2\2\2\u00b7\u00b8\b\33\1\2\u00b8\u00b9\5\66\34\2\u00b9")
        buf.write("\u00bf\3\2\2\2\u00ba\u00bb\f\4\2\2\u00bb\u00bc\7\16\2")
        buf.write("\2\u00bc\u00be\5\66\34\2\u00bd\u00ba\3\2\2\2\u00be\u00c1")
        buf.write("\3\2\2\2\u00bf\u00bd\3\2\2\2\u00bf\u00c0\3\2\2\2\u00c0")
        buf.write("\65\3\2\2\2\u00c1\u00bf\3\2\2\2\u00c2\u00c3\b\34\1\2\u00c3")
        buf.write("\u00c4\58\35\2\u00c4\u00ca\3\2\2\2\u00c5\u00c6\f\4\2\2")
        buf.write("\u00c6\u00c7\7\17\2\2\u00c7\u00c9\58\35\2\u00c8\u00c5")
        buf.write("\3\2\2\2\u00c9\u00cc\3\2\2\2\u00ca\u00c8\3\2\2\2\u00ca")
        buf.write("\u00cb\3\2\2\2\u00cb\67\3\2\2\2\u00cc\u00ca\3\2\2\2\u00cd")
        buf.write("\u00d6\7\21\2\2\u00ce\u00d6\7\22\2\2\u00cf\u00d6\7\23")
        buf.write("\2\2\u00d0\u00d6\5&\24\2\u00d1\u00d2\7\7\2\2\u00d2\u00d3")
        buf.write("\5\62\32\2\u00d3\u00d4\7\b\2\2\u00d4\u00d6\3\2\2\2\u00d5")
        buf.write("\u00cd\3\2\2\2\u00d5\u00ce\3\2\2\2\u00d5\u00cf\3\2\2\2")
        buf.write("\u00d5\u00d0\3\2\2\2\u00d5\u00d1\3\2\2\2\u00d69\3\2\2")
        buf.write("\2\u00d7\u00d8\t\2\2\2\u00d8;\3\2\2\2\23DHQWfmz\u0080")
        buf.write("\u0084\u008c\u009e\u00a5\u00ae\u00b5\u00bf\u00ca\u00d5")
        return buf.getvalue()


class BKOOLParser ( Parser ):

    grammarFileName = "BKOOL.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'int'", "'float'", "';'", "','", "'('", 
                     "')'", "'{'", "'}'", "'='", "'+'", "'-'", "'*'", "'/'", 
                     "'return'" ]

    symbolicNames = [ "<INVALID>", "INT", "FLOAT", "SEMI", "COMMA", "LRB", 
                      "RRB", "LCB", "RCB", "EQUAL", "ADD", "SUB", "MUL", 
                      "DIV", "RETURN", "INTLIT", "FLOATLIT", "ID", "WS", 
                      "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    RULE_program = 0
    RULE_decls = 1
    RULE_decl = 2
    RULE_vardecl = 3
    RULE_idlist = 4
    RULE_idlist2 = 5
    RULE_funcdecl = 6
    RULE_paramdecl = 7
    RULE_paramlist = 8
    RULE_paramlist2 = 9
    RULE_param = 10
    RULE_body = 11
    RULE_body_ele_list = 12
    RULE_body_ele_list2 = 13
    RULE_body_ele = 14
    RULE_statement = 15
    RULE_statement_kind = 16
    RULE_assignSt = 17
    RULE_callSt = 18
    RULE_returnSt = 19
    RULE_exprlist = 20
    RULE_exprlist2 = 21
    RULE_expr = 22
    RULE_addexpr = 23
    RULE_subexpr = 24
    RULE_mulexpr = 25
    RULE_divexpr = 26
    RULE_numlit = 27
    RULE_var_type = 28

    ruleNames =  [ "program", "decls", "decl", "vardecl", "idlist", "idlist2", 
                   "funcdecl", "paramdecl", "paramlist", "paramlist2", "param", 
                   "body", "body_ele_list", "body_ele_list2", "body_ele", 
                   "statement", "statement_kind", "assignSt", "callSt", 
                   "returnSt", "exprlist", "exprlist2", "expr", "addexpr", 
                   "subexpr", "mulexpr", "divexpr", "numlit", "var_type" ]

    EOF = Token.EOF
    INT=1
    FLOAT=2
    SEMI=3
    COMMA=4
    LRB=5
    RRB=6
    LCB=7
    RCB=8
    EQUAL=9
    ADD=10
    SUB=11
    MUL=12
    DIV=13
    RETURN=14
    INTLIT=15
    FLOATLIT=16
    ID=17
    WS=18
    ERROR_CHAR=19
    UNCLOSE_STRING=20
    ILLEGAL_ESCAPE=21

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def decl(self):
            return self.getTypedRuleContext(BKOOLParser.DeclContext,0)


        def decls(self):
            return self.getTypedRuleContext(BKOOLParser.DeclsContext,0)


        def EOF(self):
            return self.getToken(BKOOLParser.EOF, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_program




    def program(self):

        localctx = BKOOLParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 58
            self.decl()
            self.state = 59
            self.decls()
            self.state = 60
            self.match(BKOOLParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def decl(self):
            return self.getTypedRuleContext(BKOOLParser.DeclContext,0)


        def decls(self):
            return self.getTypedRuleContext(BKOOLParser.DeclsContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_decls




    def decls(self):

        localctx = BKOOLParser.DeclsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_decls)
        try:
            self.state = 66
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.INT, BKOOLParser.FLOAT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 62
                self.decl()
                self.state = 63
                self.decls()
                pass
            elif token in [BKOOLParser.EOF]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def vardecl(self):
            return self.getTypedRuleContext(BKOOLParser.VardeclContext,0)


        def funcdecl(self):
            return self.getTypedRuleContext(BKOOLParser.FuncdeclContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_decl




    def decl(self):

        localctx = BKOOLParser.DeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_decl)
        try:
            self.state = 70
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 68
                self.vardecl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 69
                self.funcdecl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VardeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_type(self):
            return self.getTypedRuleContext(BKOOLParser.Var_typeContext,0)


        def idlist(self):
            return self.getTypedRuleContext(BKOOLParser.IdlistContext,0)


        def SEMI(self):
            return self.getToken(BKOOLParser.SEMI, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_vardecl




    def vardecl(self):

        localctx = BKOOLParser.VardeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_vardecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 72
            self.var_type()
            self.state = 73
            self.idlist()
            self.state = 74
            self.match(BKOOLParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def idlist2(self):
            return self.getTypedRuleContext(BKOOLParser.Idlist2Context,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_idlist




    def idlist(self):

        localctx = BKOOLParser.IdlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_idlist)
        try:
            self.state = 79
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 76
                self.match(BKOOLParser.ID)
                self.state = 77
                self.idlist2()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 78
                self.match(BKOOLParser.ID)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Idlist2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMA(self):
            return self.getToken(BKOOLParser.COMMA, 0)

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def idlist2(self):
            return self.getTypedRuleContext(BKOOLParser.Idlist2Context,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_idlist2




    def idlist2(self):

        localctx = BKOOLParser.Idlist2Context(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_idlist2)
        try:
            self.state = 85
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.COMMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 81
                self.match(BKOOLParser.COMMA)
                self.state = 82
                self.match(BKOOLParser.ID)
                self.state = 83
                self.idlist2()
                pass
            elif token in [BKOOLParser.SEMI, BKOOLParser.RRB]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncdeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_type(self):
            return self.getTypedRuleContext(BKOOLParser.Var_typeContext,0)


        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def paramdecl(self):
            return self.getTypedRuleContext(BKOOLParser.ParamdeclContext,0)


        def body(self):
            return self.getTypedRuleContext(BKOOLParser.BodyContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_funcdecl




    def funcdecl(self):

        localctx = BKOOLParser.FuncdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_funcdecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 87
            self.var_type()
            self.state = 88
            self.match(BKOOLParser.ID)
            self.state = 89
            self.paramdecl()
            self.state = 90
            self.body()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamdeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LRB(self):
            return self.getToken(BKOOLParser.LRB, 0)

        def paramlist(self):
            return self.getTypedRuleContext(BKOOLParser.ParamlistContext,0)


        def RRB(self):
            return self.getToken(BKOOLParser.RRB, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_paramdecl




    def paramdecl(self):

        localctx = BKOOLParser.ParamdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_paramdecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 92
            self.match(BKOOLParser.LRB)
            self.state = 93
            self.paramlist()
            self.state = 94
            self.match(BKOOLParser.RRB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def param(self):
            return self.getTypedRuleContext(BKOOLParser.ParamContext,0)


        def paramlist2(self):
            return self.getTypedRuleContext(BKOOLParser.Paramlist2Context,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_paramlist




    def paramlist(self):

        localctx = BKOOLParser.ParamlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_paramlist)
        try:
            self.state = 100
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.INT, BKOOLParser.FLOAT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 96
                self.param()
                self.state = 97
                self.paramlist2()
                pass
            elif token in [BKOOLParser.RRB]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Paramlist2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SEMI(self):
            return self.getToken(BKOOLParser.SEMI, 0)

        def param(self):
            return self.getTypedRuleContext(BKOOLParser.ParamContext,0)


        def paramlist2(self):
            return self.getTypedRuleContext(BKOOLParser.Paramlist2Context,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_paramlist2




    def paramlist2(self):

        localctx = BKOOLParser.Paramlist2Context(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_paramlist2)
        try:
            self.state = 107
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.SEMI]:
                self.enterOuterAlt(localctx, 1)
                self.state = 102
                self.match(BKOOLParser.SEMI)
                self.state = 103
                self.param()
                self.state = 104
                self.paramlist2()
                pass
            elif token in [BKOOLParser.RRB]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_type(self):
            return self.getTypedRuleContext(BKOOLParser.Var_typeContext,0)


        def idlist(self):
            return self.getTypedRuleContext(BKOOLParser.IdlistContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_param




    def param(self):

        localctx = BKOOLParser.ParamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_param)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 109
            self.var_type()
            self.state = 110
            self.idlist()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LCB(self):
            return self.getToken(BKOOLParser.LCB, 0)

        def body_ele_list(self):
            return self.getTypedRuleContext(BKOOLParser.Body_ele_listContext,0)


        def RCB(self):
            return self.getToken(BKOOLParser.RCB, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_body




    def body(self):

        localctx = BKOOLParser.BodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_body)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 112
            self.match(BKOOLParser.LCB)
            self.state = 113
            self.body_ele_list()
            self.state = 114
            self.match(BKOOLParser.RCB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Body_ele_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def body_ele(self):
            return self.getTypedRuleContext(BKOOLParser.Body_eleContext,0)


        def body_ele_list2(self):
            return self.getTypedRuleContext(BKOOLParser.Body_ele_list2Context,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_body_ele_list




    def body_ele_list(self):

        localctx = BKOOLParser.Body_ele_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_body_ele_list)
        try:
            self.state = 120
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.INT, BKOOLParser.FLOAT, BKOOLParser.RETURN, BKOOLParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 116
                self.body_ele()
                self.state = 117
                self.body_ele_list2()
                pass
            elif token in [BKOOLParser.RCB]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Body_ele_list2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def body_ele(self):
            return self.getTypedRuleContext(BKOOLParser.Body_eleContext,0)


        def body_ele_list2(self):
            return self.getTypedRuleContext(BKOOLParser.Body_ele_list2Context,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_body_ele_list2




    def body_ele_list2(self):

        localctx = BKOOLParser.Body_ele_list2Context(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_body_ele_list2)
        try:
            self.state = 126
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.INT, BKOOLParser.FLOAT, BKOOLParser.RETURN, BKOOLParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 122
                self.body_ele()
                self.state = 123
                self.body_ele_list2()
                pass
            elif token in [BKOOLParser.RCB]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Body_eleContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def vardecl(self):
            return self.getTypedRuleContext(BKOOLParser.VardeclContext,0)


        def statement(self):
            return self.getTypedRuleContext(BKOOLParser.StatementContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_body_ele




    def body_ele(self):

        localctx = BKOOLParser.Body_eleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_body_ele)
        try:
            self.state = 130
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.INT, BKOOLParser.FLOAT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 128
                self.vardecl()
                pass
            elif token in [BKOOLParser.RETURN, BKOOLParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 129
                self.statement()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement_kind(self):
            return self.getTypedRuleContext(BKOOLParser.Statement_kindContext,0)


        def SEMI(self):
            return self.getToken(BKOOLParser.SEMI, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_statement




    def statement(self):

        localctx = BKOOLParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 132
            self.statement_kind()
            self.state = 133
            self.match(BKOOLParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Statement_kindContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignSt(self):
            return self.getTypedRuleContext(BKOOLParser.AssignStContext,0)


        def callSt(self):
            return self.getTypedRuleContext(BKOOLParser.CallStContext,0)


        def returnSt(self):
            return self.getTypedRuleContext(BKOOLParser.ReturnStContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_statement_kind




    def statement_kind(self):

        localctx = BKOOLParser.Statement_kindContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_statement_kind)
        try:
            self.state = 138
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 135
                self.assignSt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 136
                self.callSt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 137
                self.returnSt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignStContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def EQUAL(self):
            return self.getToken(BKOOLParser.EQUAL, 0)

        def expr(self):
            return self.getTypedRuleContext(BKOOLParser.ExprContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_assignSt




    def assignSt(self):

        localctx = BKOOLParser.AssignStContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_assignSt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 140
            self.match(BKOOLParser.ID)
            self.state = 141
            self.match(BKOOLParser.EQUAL)
            self.state = 142
            self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CallStContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def LRB(self):
            return self.getToken(BKOOLParser.LRB, 0)

        def exprlist(self):
            return self.getTypedRuleContext(BKOOLParser.ExprlistContext,0)


        def RRB(self):
            return self.getToken(BKOOLParser.RRB, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_callSt




    def callSt(self):

        localctx = BKOOLParser.CallStContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_callSt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 144
            self.match(BKOOLParser.ID)
            self.state = 145
            self.match(BKOOLParser.LRB)
            self.state = 146
            self.exprlist()
            self.state = 147
            self.match(BKOOLParser.RRB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturnStContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(BKOOLParser.RETURN, 0)

        def expr(self):
            return self.getTypedRuleContext(BKOOLParser.ExprContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_returnSt




    def returnSt(self):

        localctx = BKOOLParser.ReturnStContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_returnSt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 149
            self.match(BKOOLParser.RETURN)
            self.state = 150
            self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(BKOOLParser.ExprContext,0)


        def exprlist2(self):
            return self.getTypedRuleContext(BKOOLParser.Exprlist2Context,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_exprlist




    def exprlist(self):

        localctx = BKOOLParser.ExprlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_exprlist)
        try:
            self.state = 156
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.LRB, BKOOLParser.INTLIT, BKOOLParser.FLOATLIT, BKOOLParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 152
                self.expr()
                self.state = 153
                self.exprlist2()
                pass
            elif token in [BKOOLParser.RRB]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exprlist2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMA(self):
            return self.getToken(BKOOLParser.COMMA, 0)

        def expr(self):
            return self.getTypedRuleContext(BKOOLParser.ExprContext,0)


        def exprlist2(self):
            return self.getTypedRuleContext(BKOOLParser.Exprlist2Context,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_exprlist2




    def exprlist2(self):

        localctx = BKOOLParser.Exprlist2Context(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_exprlist2)
        try:
            self.state = 163
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.COMMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 158
                self.match(BKOOLParser.COMMA)
                self.state = 159
                self.expr()
                self.state = 160
                self.exprlist2()
                pass
            elif token in [BKOOLParser.RRB]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def addexpr(self):
            return self.getTypedRuleContext(BKOOLParser.AddexprContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_expr




    def expr(self):

        localctx = BKOOLParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 165
            self.addexpr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AddexprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def subexpr(self):
            return self.getTypedRuleContext(BKOOLParser.SubexprContext,0)


        def ADD(self):
            return self.getToken(BKOOLParser.ADD, 0)

        def addexpr(self):
            return self.getTypedRuleContext(BKOOLParser.AddexprContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_addexpr




    def addexpr(self):

        localctx = BKOOLParser.AddexprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_addexpr)
        try:
            self.state = 172
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 167
                self.subexpr()
                self.state = 168
                self.match(BKOOLParser.ADD)
                self.state = 169
                self.addexpr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 171
                self.subexpr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SubexprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def mulexpr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.MulexprContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.MulexprContext,i)


        def SUB(self):
            return self.getToken(BKOOLParser.SUB, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_subexpr




    def subexpr(self):

        localctx = BKOOLParser.SubexprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_subexpr)
        try:
            self.state = 179
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 174
                self.mulexpr(0)
                self.state = 175
                self.match(BKOOLParser.SUB)
                self.state = 176
                self.mulexpr(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 178
                self.mulexpr(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MulexprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def divexpr(self):
            return self.getTypedRuleContext(BKOOLParser.DivexprContext,0)


        def mulexpr(self):
            return self.getTypedRuleContext(BKOOLParser.MulexprContext,0)


        def MUL(self):
            return self.getToken(BKOOLParser.MUL, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_mulexpr



    def mulexpr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKOOLParser.MulexprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 50
        self.enterRecursionRule(localctx, 50, self.RULE_mulexpr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 182
            self.divexpr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 189
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,14,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKOOLParser.MulexprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_mulexpr)
                    self.state = 184
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 185
                    self.match(BKOOLParser.MUL)
                    self.state = 186
                    self.divexpr(0) 
                self.state = 191
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,14,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class DivexprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def numlit(self):
            return self.getTypedRuleContext(BKOOLParser.NumlitContext,0)


        def divexpr(self):
            return self.getTypedRuleContext(BKOOLParser.DivexprContext,0)


        def DIV(self):
            return self.getToken(BKOOLParser.DIV, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_divexpr



    def divexpr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKOOLParser.DivexprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 52
        self.enterRecursionRule(localctx, 52, self.RULE_divexpr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 193
            self.numlit()
            self._ctx.stop = self._input.LT(-1)
            self.state = 200
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,15,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKOOLParser.DivexprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_divexpr)
                    self.state = 195
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 196
                    self.match(BKOOLParser.DIV)
                    self.state = 197
                    self.numlit() 
                self.state = 202
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,15,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class NumlitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTLIT(self):
            return self.getToken(BKOOLParser.INTLIT, 0)

        def FLOATLIT(self):
            return self.getToken(BKOOLParser.FLOATLIT, 0)

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def callSt(self):
            return self.getTypedRuleContext(BKOOLParser.CallStContext,0)


        def LRB(self):
            return self.getToken(BKOOLParser.LRB, 0)

        def subexpr(self):
            return self.getTypedRuleContext(BKOOLParser.SubexprContext,0)


        def RRB(self):
            return self.getToken(BKOOLParser.RRB, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_numlit




    def numlit(self):

        localctx = BKOOLParser.NumlitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_numlit)
        try:
            self.state = 211
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 203
                self.match(BKOOLParser.INTLIT)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 204
                self.match(BKOOLParser.FLOATLIT)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 205
                self.match(BKOOLParser.ID)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 206
                self.callSt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 207
                self.match(BKOOLParser.LRB)
                self.state = 208
                self.subexpr()
                self.state = 209
                self.match(BKOOLParser.RRB)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(BKOOLParser.INT, 0)

        def FLOAT(self):
            return self.getToken(BKOOLParser.FLOAT, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_var_type




    def var_type(self):

        localctx = BKOOLParser.Var_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_var_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 213
            _la = self._input.LA(1)
            if not(_la==BKOOLParser.INT or _la==BKOOLParser.FLOAT):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[25] = self.mulexpr_sempred
        self._predicates[26] = self.divexpr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def mulexpr_sempred(self, localctx:MulexprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def divexpr_sempred(self, localctx:DivexprContext, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         




