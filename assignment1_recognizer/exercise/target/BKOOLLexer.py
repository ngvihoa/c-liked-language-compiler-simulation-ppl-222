# Generated from main/bkool/parser/BKOOL.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\27")
        buf.write("\u0080\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\5\3")
        buf.write("\5\3\6\3\6\3\7\3\7\3\b\3\b\3\t\3\t\3\n\3\n\3\13\3\13\3")
        buf.write("\f\3\f\3\r\3\r\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\17")
        buf.write("\3\17\3\20\3\20\3\21\3\21\3\21\3\22\3\22\3\22\7\22a\n")
        buf.write("\22\f\22\16\22d\13\22\5\22f\n\22\3\23\3\23\6\23j\n\23")
        buf.write("\r\23\16\23k\3\24\6\24o\n\24\r\24\16\24p\3\25\6\25t\n")
        buf.write("\25\r\25\16\25u\3\25\3\25\3\26\3\26\3\26\3\27\3\27\3\30")
        buf.write("\3\30\2\2\31\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13")
        buf.write("\25\f\27\r\31\16\33\17\35\20\37\21!\22#\2%\2\'\23)\24")
        buf.write("+\25-\26/\27\3\2\6\3\2\63;\3\2\62;\4\2C\\c|\5\2\13\f\17")
        buf.write("\17\"\"\2\u0082\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2")
        buf.write("\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21")
        buf.write("\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3")
        buf.write("\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2")
        buf.write("\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2")
        buf.write("\2\2\3\61\3\2\2\2\5\65\3\2\2\2\7;\3\2\2\2\t=\3\2\2\2\13")
        buf.write("?\3\2\2\2\rA\3\2\2\2\17C\3\2\2\2\21E\3\2\2\2\23G\3\2\2")
        buf.write("\2\25I\3\2\2\2\27K\3\2\2\2\31M\3\2\2\2\33O\3\2\2\2\35")
        buf.write("Q\3\2\2\2\37X\3\2\2\2!Z\3\2\2\2#e\3\2\2\2%g\3\2\2\2\'")
        buf.write("n\3\2\2\2)s\3\2\2\2+y\3\2\2\2-|\3\2\2\2/~\3\2\2\2\61\62")
        buf.write("\7k\2\2\62\63\7p\2\2\63\64\7v\2\2\64\4\3\2\2\2\65\66\7")
        buf.write("h\2\2\66\67\7n\2\2\678\7q\2\289\7c\2\29:\7v\2\2:\6\3\2")
        buf.write("\2\2;<\7=\2\2<\b\3\2\2\2=>\7.\2\2>\n\3\2\2\2?@\7*\2\2")
        buf.write("@\f\3\2\2\2AB\7+\2\2B\16\3\2\2\2CD\7}\2\2D\20\3\2\2\2")
        buf.write("EF\7\177\2\2F\22\3\2\2\2GH\7?\2\2H\24\3\2\2\2IJ\7-\2\2")
        buf.write("J\26\3\2\2\2KL\7/\2\2L\30\3\2\2\2MN\7,\2\2N\32\3\2\2\2")
        buf.write("OP\7\61\2\2P\34\3\2\2\2QR\7t\2\2RS\7g\2\2ST\7v\2\2TU\7")
        buf.write("w\2\2UV\7t\2\2VW\7p\2\2W\36\3\2\2\2XY\5#\22\2Y \3\2\2")
        buf.write("\2Z[\5#\22\2[\\\5%\23\2\\\"\3\2\2\2]f\7\62\2\2^b\t\2\2")
        buf.write("\2_a\t\3\2\2`_\3\2\2\2ad\3\2\2\2b`\3\2\2\2bc\3\2\2\2c")
        buf.write("f\3\2\2\2db\3\2\2\2e]\3\2\2\2e^\3\2\2\2f$\3\2\2\2gi\7")
        buf.write("\60\2\2hj\t\3\2\2ih\3\2\2\2jk\3\2\2\2ki\3\2\2\2kl\3\2")
        buf.write("\2\2l&\3\2\2\2mo\t\4\2\2nm\3\2\2\2op\3\2\2\2pn\3\2\2\2")
        buf.write("pq\3\2\2\2q(\3\2\2\2rt\t\5\2\2sr\3\2\2\2tu\3\2\2\2us\3")
        buf.write("\2\2\2uv\3\2\2\2vw\3\2\2\2wx\b\25\2\2x*\3\2\2\2yz\13\2")
        buf.write("\2\2z{\b\26\3\2{,\3\2\2\2|}\13\2\2\2}.\3\2\2\2~\177\13")
        buf.write("\2\2\2\177\60\3\2\2\2\b\2bekpu\4\b\2\2\3\26\2")
        return buf.getvalue()


class BKOOLLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    INT = 1
    FLOAT = 2
    SEMI = 3
    COMMA = 4
    LRB = 5
    RRB = 6
    LCB = 7
    RCB = 8
    EQUAL = 9
    ADD = 10
    SUB = 11
    MUL = 12
    DIV = 13
    RETURN = 14
    INTLIT = 15
    FLOATLIT = 16
    ID = 17
    WS = 18
    ERROR_CHAR = 19
    UNCLOSE_STRING = 20
    ILLEGAL_ESCAPE = 21

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'int'", "'float'", "';'", "','", "'('", "')'", "'{'", "'}'", 
            "'='", "'+'", "'-'", "'*'", "'/'", "'return'" ]

    symbolicNames = [ "<INVALID>",
            "INT", "FLOAT", "SEMI", "COMMA", "LRB", "RRB", "LCB", "RCB", 
            "EQUAL", "ADD", "SUB", "MUL", "DIV", "RETURN", "INTLIT", "FLOATLIT", 
            "ID", "WS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    ruleNames = [ "INT", "FLOAT", "SEMI", "COMMA", "LRB", "RRB", "LCB", 
                  "RCB", "EQUAL", "ADD", "SUB", "MUL", "DIV", "RETURN", 
                  "INTLIT", "FLOATLIT", "INTPART", "DECPART", "ID", "WS", 
                  "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    grammarFileName = "BKOOL.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[20] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            raise ErrorToken(self.text)
     


