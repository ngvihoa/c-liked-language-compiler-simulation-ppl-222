# Generated from main/mt22/parser/MT22.g4 by ANTLR 4.9.2
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2;")
        buf.write("\u01c1\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\3\2\3\2\3\3\3\3\3\4\3\4\3\5\3\5\3\6\3\6\3\7\3\7\3\b")
        buf.write("\3\b\3\b\3\t\3\t\3\t\3\n\3\n\3\n\3\13\3\13\3\13\3\f\3")
        buf.write("\f\3\r\3\r\3\r\3\16\3\16\3\17\3\17\3\17\3\20\3\20\3\20")
        buf.write("\3\21\3\21\3\22\3\22\3\23\3\23\3\24\3\24\3\25\3\25\3\26")
        buf.write("\3\26\3\27\3\27\3\30\3\30\3\31\3\31\3\32\3\32\3\33\3\33")
        buf.write("\3\34\3\34\3\35\3\35\3\35\3\35\3\35\3\35\3\36\3\36\3\36")
        buf.write("\3\36\3\36\3\37\3\37\3\37\3\37\3\37\3\37\3 \3 \3 \3 \3")
        buf.write(" \3 \3 \3 \3!\3!\3!\3\"\3\"\3\"\3\"\3\"\3#\3#\3#\3#\3")
        buf.write("#\3#\3$\3$\3$\3$\3$\3$\3%\3%\3%\3%\3&\3&\3&\3&\3&\3&\3")
        buf.write("&\3&\3&\3\'\3\'\3\'\3(\3(\3(\3(\3(\3(\3(\3(\3)\3)\3)\3")
        buf.write(")\3)\3)\3)\3*\3*\3*\3*\3*\3*\3*\3+\3+\3+\3+\3+\3,\3,\3")
        buf.write(",\3,\3,\3-\3-\3-\3-\3-\3-\3.\3.\3.\3.\3/\3/\3/\3/\3/\3")
        buf.write("/\3/\3/\3/\3\60\3\60\3\60\3\61\3\61\3\61\3\61\3\61\3\61")
        buf.write("\3\61\3\61\3\62\3\62\7\62\u0142\n\62\f\62\16\62\u0145")
        buf.write("\13\62\3\63\3\63\3\63\3\64\3\64\3\64\3\64\3\64\3\64\5")
        buf.write("\64\u0150\n\64\3\64\3\64\3\64\3\64\5\64\u0156\n\64\3\64")
        buf.write("\3\64\3\64\3\64\5\64\u015c\n\64\3\65\3\65\3\66\3\66\3")
        buf.write("\67\3\67\3\67\5\67\u0165\n\67\3\67\7\67\u0168\n\67\f\67")
        buf.write("\16\67\u016b\13\67\5\67\u016d\n\67\38\38\78\u0171\n8\f")
        buf.write("8\168\u0174\138\39\39\59\u0178\n9\39\69\u017b\n9\r9\16")
        buf.write("9\u017c\3:\3:\5:\u0181\n:\3:\3:\3:\3;\3;\6;\u0188\n;\r")
        buf.write(";\16;\u0189\3<\3<\3<\3=\3=\3=\3>\3>\3>\3>\7>\u0196\n>")
        buf.write("\f>\16>\u0199\13>\3>\3>\3>\3>\3>\3?\3?\3?\3?\7?\u01a4")
        buf.write("\n?\f?\16?\u01a7\13?\3?\3?\3@\6@\u01ac\n@\r@\16@\u01ad")
        buf.write("\3@\3@\3A\3A\3A\3B\3B\5B\u01b7\nB\3B\3B\3C\3C\5C\u01bd")
        buf.write("\nC\3C\3C\3C\3\u0197\2D\3\3\5\4\7\5\t\6\13\7\r\b\17\t")
        buf.write("\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21!\2#\22%")
        buf.write("\23\'\24)\25+\26-\27/\30\61\31\63\32\65\33\67\349\35;")
        buf.write("\36=\37? A!C\"E#G$I%K&M\'O(Q)S*U+W,Y-[.]/_\60a\61c\62")
        buf.write("e\63g\64i\2k\2m\2o\2q\2s\65u\2w\2y\2{\66}\67\1778\u0081")
        buf.write("9\u0083:\u0085;\3\2\f\5\2C\\aac|\6\2\62;C\\aac|\3\2\62")
        buf.write(";\3\2\63;\4\2GGgg\4\2--//\6\2\f\f\17\17$$^^\n\2$$))^^")
        buf.write("ddhhppttvv\4\2\f\f\17\17\5\2\13\f\17\17\"\"\2\u01ca\2")
        buf.write("\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3")
        buf.write("\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2")
        buf.write("\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2")
        buf.write("\2\2\35\3\2\2\2\2\37\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'")
        buf.write("\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2")
        buf.write("\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29")
        buf.write("\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2")
        buf.write("C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2")
        buf.write("\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2")
        buf.write("\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2")
        buf.write("\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2s\3")
        buf.write("\2\2\2\2{\3\2\2\2\2}\3\2\2\2\2\177\3\2\2\2\2\u0081\3\2")
        buf.write("\2\2\2\u0083\3\2\2\2\2\u0085\3\2\2\2\3\u0087\3\2\2\2\5")
        buf.write("\u0089\3\2\2\2\7\u008b\3\2\2\2\t\u008d\3\2\2\2\13\u008f")
        buf.write("\3\2\2\2\r\u0091\3\2\2\2\17\u0093\3\2\2\2\21\u0096\3\2")
        buf.write("\2\2\23\u0099\3\2\2\2\25\u009c\3\2\2\2\27\u009f\3\2\2")
        buf.write("\2\31\u00a1\3\2\2\2\33\u00a4\3\2\2\2\35\u00a6\3\2\2\2")
        buf.write("\37\u00a9\3\2\2\2!\u00ac\3\2\2\2#\u00ae\3\2\2\2%\u00b0")
        buf.write("\3\2\2\2\'\u00b2\3\2\2\2)\u00b4\3\2\2\2+\u00b6\3\2\2\2")
        buf.write("-\u00b8\3\2\2\2/\u00ba\3\2\2\2\61\u00bc\3\2\2\2\63\u00be")
        buf.write("\3\2\2\2\65\u00c0\3\2\2\2\67\u00c2\3\2\2\29\u00c4\3\2")
        buf.write("\2\2;\u00ca\3\2\2\2=\u00cf\3\2\2\2?\u00d5\3\2\2\2A\u00dd")
        buf.write("\3\2\2\2C\u00e0\3\2\2\2E\u00e5\3\2\2\2G\u00eb\3\2\2\2")
        buf.write("I\u00f1\3\2\2\2K\u00f5\3\2\2\2M\u00fe\3\2\2\2O\u0101\3")
        buf.write("\2\2\2Q\u0109\3\2\2\2S\u0110\3\2\2\2U\u0117\3\2\2\2W\u011c")
        buf.write("\3\2\2\2Y\u0121\3\2\2\2[\u0127\3\2\2\2]\u012b\3\2\2\2")
        buf.write("_\u0134\3\2\2\2a\u0137\3\2\2\2c\u013f\3\2\2\2e\u0146\3")
        buf.write("\2\2\2g\u015b\3\2\2\2i\u015d\3\2\2\2k\u015f\3\2\2\2m\u016c")
        buf.write("\3\2\2\2o\u016e\3\2\2\2q\u0175\3\2\2\2s\u017e\3\2\2\2")
        buf.write("u\u0187\3\2\2\2w\u018b\3\2\2\2y\u018e\3\2\2\2{\u0191\3")
        buf.write("\2\2\2}\u019f\3\2\2\2\177\u01ab\3\2\2\2\u0081\u01b1\3")
        buf.write("\2\2\2\u0083\u01b4\3\2\2\2\u0085\u01ba\3\2\2\2\u0087\u0088")
        buf.write("\7-\2\2\u0088\4\3\2\2\2\u0089\u008a\7/\2\2\u008a\6\3\2")
        buf.write("\2\2\u008b\u008c\7,\2\2\u008c\b\3\2\2\2\u008d\u008e\7")
        buf.write("\61\2\2\u008e\n\3\2\2\2\u008f\u0090\7\'\2\2\u0090\f\3")
        buf.write("\2\2\2\u0091\u0092\7#\2\2\u0092\16\3\2\2\2\u0093\u0094")
        buf.write("\7(\2\2\u0094\u0095\7(\2\2\u0095\20\3\2\2\2\u0096\u0097")
        buf.write("\7~\2\2\u0097\u0098\7~\2\2\u0098\22\3\2\2\2\u0099\u009a")
        buf.write("\7?\2\2\u009a\u009b\7?\2\2\u009b\24\3\2\2\2\u009c\u009d")
        buf.write("\7#\2\2\u009d\u009e\7?\2\2\u009e\26\3\2\2\2\u009f\u00a0")
        buf.write("\7>\2\2\u00a0\30\3\2\2\2\u00a1\u00a2\7>\2\2\u00a2\u00a3")
        buf.write("\7?\2\2\u00a3\32\3\2\2\2\u00a4\u00a5\7@\2\2\u00a5\34\3")
        buf.write("\2\2\2\u00a6\u00a7\7@\2\2\u00a7\u00a8\7?\2\2\u00a8\36")
        buf.write("\3\2\2\2\u00a9\u00aa\7<\2\2\u00aa\u00ab\7<\2\2\u00ab ")
        buf.write("\3\2\2\2\u00ac\u00ad\7a\2\2\u00ad\"\3\2\2\2\u00ae\u00af")
        buf.write("\7*\2\2\u00af$\3\2\2\2\u00b0\u00b1\7+\2\2\u00b1&\3\2\2")
        buf.write("\2\u00b2\u00b3\7]\2\2\u00b3(\3\2\2\2\u00b4\u00b5\7_\2")
        buf.write("\2\u00b5*\3\2\2\2\u00b6\u00b7\7}\2\2\u00b7,\3\2\2\2\u00b8")
        buf.write("\u00b9\7\177\2\2\u00b9.\3\2\2\2\u00ba\u00bb\7\60\2\2\u00bb")
        buf.write("\60\3\2\2\2\u00bc\u00bd\7.\2\2\u00bd\62\3\2\2\2\u00be")
        buf.write("\u00bf\7<\2\2\u00bf\64\3\2\2\2\u00c0\u00c1\7=\2\2\u00c1")
        buf.write("\66\3\2\2\2\u00c2\u00c3\7?\2\2\u00c38\3\2\2\2\u00c4\u00c5")
        buf.write("\7c\2\2\u00c5\u00c6\7t\2\2\u00c6\u00c7\7t\2\2\u00c7\u00c8")
        buf.write("\7c\2\2\u00c8\u00c9\7{\2\2\u00c9:\3\2\2\2\u00ca\u00cb")
        buf.write("\7c\2\2\u00cb\u00cc\7w\2\2\u00cc\u00cd\7v\2\2\u00cd\u00ce")
        buf.write("\7q\2\2\u00ce<\3\2\2\2\u00cf\u00d0\7d\2\2\u00d0\u00d1")
        buf.write("\7t\2\2\u00d1\u00d2\7g\2\2\u00d2\u00d3\7c\2\2\u00d3\u00d4")
        buf.write("\7m\2\2\u00d4>\3\2\2\2\u00d5\u00d6\7d\2\2\u00d6\u00d7")
        buf.write("\7q\2\2\u00d7\u00d8\7q\2\2\u00d8\u00d9\7n\2\2\u00d9\u00da")
        buf.write("\7g\2\2\u00da\u00db\7c\2\2\u00db\u00dc\7p\2\2\u00dc@\3")
        buf.write("\2\2\2\u00dd\u00de\7f\2\2\u00de\u00df\7q\2\2\u00dfB\3")
        buf.write("\2\2\2\u00e0\u00e1\7g\2\2\u00e1\u00e2\7n\2\2\u00e2\u00e3")
        buf.write("\7u\2\2\u00e3\u00e4\7g\2\2\u00e4D\3\2\2\2\u00e5\u00e6")
        buf.write("\7h\2\2\u00e6\u00e7\7c\2\2\u00e7\u00e8\7n\2\2\u00e8\u00e9")
        buf.write("\7u\2\2\u00e9\u00ea\7g\2\2\u00eaF\3\2\2\2\u00eb\u00ec")
        buf.write("\7h\2\2\u00ec\u00ed\7n\2\2\u00ed\u00ee\7q\2\2\u00ee\u00ef")
        buf.write("\7c\2\2\u00ef\u00f0\7v\2\2\u00f0H\3\2\2\2\u00f1\u00f2")
        buf.write("\7h\2\2\u00f2\u00f3\7q\2\2\u00f3\u00f4\7t\2\2\u00f4J\3")
        buf.write("\2\2\2\u00f5\u00f6\7h\2\2\u00f6\u00f7\7w\2\2\u00f7\u00f8")
        buf.write("\7p\2\2\u00f8\u00f9\7e\2\2\u00f9\u00fa\7v\2\2\u00fa\u00fb")
        buf.write("\7k\2\2\u00fb\u00fc\7q\2\2\u00fc\u00fd\7p\2\2\u00fdL\3")
        buf.write("\2\2\2\u00fe\u00ff\7k\2\2\u00ff\u0100\7h\2\2\u0100N\3")
        buf.write("\2\2\2\u0101\u0102\7k\2\2\u0102\u0103\7p\2\2\u0103\u0104")
        buf.write("\7v\2\2\u0104\u0105\7g\2\2\u0105\u0106\7i\2\2\u0106\u0107")
        buf.write("\7g\2\2\u0107\u0108\7t\2\2\u0108P\3\2\2\2\u0109\u010a")
        buf.write("\7t\2\2\u010a\u010b\7g\2\2\u010b\u010c\7v\2\2\u010c\u010d")
        buf.write("\7w\2\2\u010d\u010e\7t\2\2\u010e\u010f\7p\2\2\u010fR\3")
        buf.write("\2\2\2\u0110\u0111\7u\2\2\u0111\u0112\7v\2\2\u0112\u0113")
        buf.write("\7t\2\2\u0113\u0114\7k\2\2\u0114\u0115\7p\2\2\u0115\u0116")
        buf.write("\7i\2\2\u0116T\3\2\2\2\u0117\u0118\7v\2\2\u0118\u0119")
        buf.write("\7t\2\2\u0119\u011a\7w\2\2\u011a\u011b\7g\2\2\u011bV\3")
        buf.write("\2\2\2\u011c\u011d\7x\2\2\u011d\u011e\7q\2\2\u011e\u011f")
        buf.write("\7k\2\2\u011f\u0120\7f\2\2\u0120X\3\2\2\2\u0121\u0122")
        buf.write("\7y\2\2\u0122\u0123\7j\2\2\u0123\u0124\7k\2\2\u0124\u0125")
        buf.write("\7n\2\2\u0125\u0126\7g\2\2\u0126Z\3\2\2\2\u0127\u0128")
        buf.write("\7q\2\2\u0128\u0129\7w\2\2\u0129\u012a\7v\2\2\u012a\\")
        buf.write("\3\2\2\2\u012b\u012c\7e\2\2\u012c\u012d\7q\2\2\u012d\u012e")
        buf.write("\7p\2\2\u012e\u012f\7v\2\2\u012f\u0130\7k\2\2\u0130\u0131")
        buf.write("\7p\2\2\u0131\u0132\7w\2\2\u0132\u0133\7g\2\2\u0133^\3")
        buf.write("\2\2\2\u0134\u0135\7q\2\2\u0135\u0136\7h\2\2\u0136`\3")
        buf.write("\2\2\2\u0137\u0138\7k\2\2\u0138\u0139\7p\2\2\u0139\u013a")
        buf.write("\7j\2\2\u013a\u013b\7g\2\2\u013b\u013c\7t\2\2\u013c\u013d")
        buf.write("\7k\2\2\u013d\u013e\7v\2\2\u013eb\3\2\2\2\u013f\u0143")
        buf.write("\t\2\2\2\u0140\u0142\t\3\2\2\u0141\u0140\3\2\2\2\u0142")
        buf.write("\u0145\3\2\2\2\u0143\u0141\3\2\2\2\u0143\u0144\3\2\2\2")
        buf.write("\u0144d\3\2\2\2\u0145\u0143\3\2\2\2\u0146\u0147\5m\67")
        buf.write("\2\u0147\u0148\b\63\2\2\u0148f\3\2\2\2\u0149\u014a\5m")
        buf.write("\67\2\u014a\u014b\5o8\2\u014b\u014c\b\64\3\2\u014c\u015c")
        buf.write("\3\2\2\2\u014d\u014f\5m\67\2\u014e\u0150\5o8\2\u014f\u014e")
        buf.write("\3\2\2\2\u014f\u0150\3\2\2\2\u0150\u0151\3\2\2\2\u0151")
        buf.write("\u0152\5q9\2\u0152\u0153\b\64\4\2\u0153\u015c\3\2\2\2")
        buf.write("\u0154\u0156\5m\67\2\u0155\u0154\3\2\2\2\u0155\u0156\3")
        buf.write("\2\2\2\u0156\u0157\3\2\2\2\u0157\u0158\5o8\2\u0158\u0159")
        buf.write("\5q9\2\u0159\u015a\b\64\5\2\u015a\u015c\3\2\2\2\u015b")
        buf.write("\u0149\3\2\2\2\u015b\u014d\3\2\2\2\u015b\u0155\3\2\2\2")
        buf.write("\u015ch\3\2\2\2\u015d\u015e\t\4\2\2\u015ej\3\2\2\2\u015f")
        buf.write("\u0160\t\5\2\2\u0160l\3\2\2\2\u0161\u016d\7\62\2\2\u0162")
        buf.write("\u0169\5k\66\2\u0163\u0165\5!\21\2\u0164\u0163\3\2\2\2")
        buf.write("\u0164\u0165\3\2\2\2\u0165\u0166\3\2\2\2\u0166\u0168\5")
        buf.write("i\65\2\u0167\u0164\3\2\2\2\u0168\u016b\3\2\2\2\u0169\u0167")
        buf.write("\3\2\2\2\u0169\u016a\3\2\2\2\u016a\u016d\3\2\2\2\u016b")
        buf.write("\u0169\3\2\2\2\u016c\u0161\3\2\2\2\u016c\u0162\3\2\2\2")
        buf.write("\u016dn\3\2\2\2\u016e\u0172\5/\30\2\u016f\u0171\5i\65")
        buf.write("\2\u0170\u016f\3\2\2\2\u0171\u0174\3\2\2\2\u0172\u0170")
        buf.write("\3\2\2\2\u0172\u0173\3\2\2\2\u0173p\3\2\2\2\u0174\u0172")
        buf.write("\3\2\2\2\u0175\u0177\t\6\2\2\u0176\u0178\t\7\2\2\u0177")
        buf.write("\u0176\3\2\2\2\u0177\u0178\3\2\2\2\u0178\u017a\3\2\2\2")
        buf.write("\u0179\u017b\5i\65\2\u017a\u0179\3\2\2\2\u017b\u017c\3")
        buf.write("\2\2\2\u017c\u017a\3\2\2\2\u017c\u017d\3\2\2\2\u017dr")
        buf.write("\3\2\2\2\u017e\u0180\7$\2\2\u017f\u0181\5u;\2\u0180\u017f")
        buf.write("\3\2\2\2\u0180\u0181\3\2\2\2\u0181\u0182\3\2\2\2\u0182")
        buf.write("\u0183\7$\2\2\u0183\u0184\b:\6\2\u0184t\3\2\2\2\u0185")
        buf.write("\u0188\n\b\2\2\u0186\u0188\5w<\2\u0187\u0185\3\2\2\2\u0187")
        buf.write("\u0186\3\2\2\2\u0188\u0189\3\2\2\2\u0189\u0187\3\2\2\2")
        buf.write("\u0189\u018a\3\2\2\2\u018av\3\2\2\2\u018b\u018c\7^\2\2")
        buf.write("\u018c\u018d\t\t\2\2\u018dx\3\2\2\2\u018e\u018f\7^\2\2")
        buf.write("\u018f\u0190\n\t\2\2\u0190z\3\2\2\2\u0191\u0192\7\61\2")
        buf.write("\2\u0192\u0193\7,\2\2\u0193\u0197\3\2\2\2\u0194\u0196")
        buf.write("\13\2\2\2\u0195\u0194\3\2\2\2\u0196\u0199\3\2\2\2\u0197")
        buf.write("\u0198\3\2\2\2\u0197\u0195\3\2\2\2\u0198\u019a\3\2\2\2")
        buf.write("\u0199\u0197\3\2\2\2\u019a\u019b\7,\2\2\u019b\u019c\7")
        buf.write("\61\2\2\u019c\u019d\3\2\2\2\u019d\u019e\b>\7\2\u019e|")
        buf.write("\3\2\2\2\u019f\u01a0\7\61\2\2\u01a0\u01a1\7\61\2\2\u01a1")
        buf.write("\u01a5\3\2\2\2\u01a2\u01a4\n\n\2\2\u01a3\u01a2\3\2\2\2")
        buf.write("\u01a4\u01a7\3\2\2\2\u01a5\u01a3\3\2\2\2\u01a5\u01a6\3")
        buf.write("\2\2\2\u01a6\u01a8\3\2\2\2\u01a7\u01a5\3\2\2\2\u01a8\u01a9")
        buf.write("\b?\7\2\u01a9~\3\2\2\2\u01aa\u01ac\t\13\2\2\u01ab\u01aa")
        buf.write("\3\2\2\2\u01ac\u01ad\3\2\2\2\u01ad\u01ab\3\2\2\2\u01ad")
        buf.write("\u01ae\3\2\2\2\u01ae\u01af\3\2\2\2\u01af\u01b0\b@\7\2")
        buf.write("\u01b0\u0080\3\2\2\2\u01b1\u01b2\13\2\2\2\u01b2\u01b3")
        buf.write("\bA\b\2\u01b3\u0082\3\2\2\2\u01b4\u01b6\7$\2\2\u01b5\u01b7")
        buf.write("\5u;\2\u01b6\u01b5\3\2\2\2\u01b6\u01b7\3\2\2\2\u01b7\u01b8")
        buf.write("\3\2\2\2\u01b8\u01b9\bB\t\2\u01b9\u0084\3\2\2\2\u01ba")
        buf.write("\u01bc\7$\2\2\u01bb\u01bd\5u;\2\u01bc\u01bb\3\2\2\2\u01bc")
        buf.write("\u01bd\3\2\2\2\u01bd\u01be\3\2\2\2\u01be\u01bf\5y=\2\u01bf")
        buf.write("\u01c0\bC\n\2\u01c0\u0086\3\2\2\2\25\2\u0143\u014f\u0155")
        buf.write("\u015b\u0164\u0169\u016c\u0172\u0177\u017c\u0180\u0187")
        buf.write("\u0189\u0197\u01a5\u01ad\u01b6\u01bc\13\3\63\2\3\64\3")
        buf.write("\3\64\4\3\64\5\3:\6\b\2\2\3A\7\3B\b\3C\t")
        return buf.getvalue()


class MT22Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    ADD = 1
    SUB = 2
    MUL = 3
    DIV = 4
    MOD = 5
    NOT = 6
    AND = 7
    OR = 8
    EQUAL = 9
    UNEQUAL = 10
    LT = 11
    LTE = 12
    GT = 13
    GTE = 14
    DCOLON = 15
    LB = 16
    RB = 17
    LSB = 18
    RSB = 19
    LCB = 20
    RCB = 21
    DOT = 22
    COMMA = 23
    COLON = 24
    SMCOLON = 25
    ASSIGN = 26
    ARRAY = 27
    AUTO = 28
    BREAK = 29
    BOOLEAN = 30
    DO = 31
    ELSE = 32
    FALSE = 33
    FLOAT = 34
    FOR = 35
    FUNCTION = 36
    IF = 37
    INTEGER = 38
    RETURN = 39
    STRING = 40
    TRUE = 41
    VOID = 42
    WHILE = 43
    OUT = 44
    CONTINUE = 45
    OF = 46
    INHERIT = 47
    ID = 48
    INT_LIT = 49
    FLOAT_LIT = 50
    STRING_LIT = 51
    BLOCK_COMMENT = 52
    INLINE_COMMENT = 53
    WS = 54
    ERROR_CHAR = 55
    UNCLOSE_STRING = 56
    ILLEGAL_ESCAPE = 57

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'+'", "'-'", "'*'", "'/'", "'%'", "'!'", "'&&'", "'||'", "'=='", 
            "'!='", "'<'", "'<='", "'>'", "'>='", "'::'", "'('", "')'", 
            "'['", "']'", "'{'", "'}'", "'.'", "','", "':'", "';'", "'='", 
            "'array'", "'auto'", "'break'", "'boolean'", "'do'", "'else'", 
            "'false'", "'float'", "'for'", "'function'", "'if'", "'integer'", 
            "'return'", "'string'", "'true'", "'void'", "'while'", "'out'", 
            "'continue'", "'of'", "'inherit'" ]

    symbolicNames = [ "<INVALID>",
            "ADD", "SUB", "MUL", "DIV", "MOD", "NOT", "AND", "OR", "EQUAL", 
            "UNEQUAL", "LT", "LTE", "GT", "GTE", "DCOLON", "LB", "RB", "LSB", 
            "RSB", "LCB", "RCB", "DOT", "COMMA", "COLON", "SMCOLON", "ASSIGN", 
            "ARRAY", "AUTO", "BREAK", "BOOLEAN", "DO", "ELSE", "FALSE", 
            "FLOAT", "FOR", "FUNCTION", "IF", "INTEGER", "RETURN", "STRING", 
            "TRUE", "VOID", "WHILE", "OUT", "CONTINUE", "OF", "INHERIT", 
            "ID", "INT_LIT", "FLOAT_LIT", "STRING_LIT", "BLOCK_COMMENT", 
            "INLINE_COMMENT", "WS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    ruleNames = [ "ADD", "SUB", "MUL", "DIV", "MOD", "NOT", "AND", "OR", 
                  "EQUAL", "UNEQUAL", "LT", "LTE", "GT", "GTE", "DCOLON", 
                  "UNDERSCORE", "LB", "RB", "LSB", "RSB", "LCB", "RCB", 
                  "DOT", "COMMA", "COLON", "SMCOLON", "ASSIGN", "ARRAY", 
                  "AUTO", "BREAK", "BOOLEAN", "DO", "ELSE", "FALSE", "FLOAT", 
                  "FOR", "FUNCTION", "IF", "INTEGER", "RETURN", "STRING", 
                  "TRUE", "VOID", "WHILE", "OUT", "CONTINUE", "OF", "INHERIT", 
                  "ID", "INT_LIT", "FLOAT_LIT", "DIGIT_Z", "DIGIT_N", "INT_PART", 
                  "DECPART", "EXP", "STRING_LIT", "STRING_SEQUENCE", "ESCAPE_C", 
                  "ILLEGAL_C", "BLOCK_COMMENT", "INLINE_COMMENT", "WS", 
                  "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    grammarFileName = "MT22.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[49] = self.INT_LIT_action 
            actions[50] = self.FLOAT_LIT_action 
            actions[56] = self.STRING_LIT_action 
            actions[63] = self.ERROR_CHAR_action 
            actions[64] = self.UNCLOSE_STRING_action 
            actions[65] = self.ILLEGAL_ESCAPE_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def INT_LIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:

            		self.text = self.text.replace('_','')
            	
     

    def FLOAT_LIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:

            		self.text = self.text.replace('_','')
            	
     

        if actionIndex == 2:

            		self.text = self.text.replace('_','')
            	
     

        if actionIndex == 3:

            		self.text = self.text.replace('_','')
            	
     

    def STRING_LIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 4:

            		self.text = self.text[1:-1]
            	
     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 5:
            raise ErrorToken(self.text)
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 6:

            		self.text = self.text[1:]
            		raise UncloseString(self.text)
            	
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 7:

            		self.text = self.text[1:]
            		raise IllegalEscape(self.text)
            	
     


