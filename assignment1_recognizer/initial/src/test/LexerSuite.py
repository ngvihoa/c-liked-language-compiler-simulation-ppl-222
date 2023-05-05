import unittest
from TestUtils import TestLexer


class LexerSuite(unittest.TestCase):

    def test_lowercase_identifier_0(self):
        input = """antiVirus004"""
        output = "antiVirus004,<EOF>"
        self.assertTrue(TestLexer.test(input, output, 101))

    def test_lowercase_identifier_1(self):
        input = """2401intern"""
        output = "2401,intern,<EOF>"
        self.assertTrue(TestLexer.test(input, output, 102))
    
    def test_lowercase_identifier_2(self):
        input = """102_33"""
        output = "10233,<EOF>"
        self.assertTrue(TestLexer.test(input, output, 103))
    
    def test_lowercase_identifier_3(self): 
        input = """102_33.222"""
        output = "10233.222,<EOF>"
        self.assertTrue(TestLexer.test(input, output, 104))

    def test_lowercase_identifier_4(self):
        input = """ C\si chay """
        output = """C,Error Token \\"""
        self.assertTrue(TestLexer.test(input, output, 105))

    def test_lowercase_identifier_5(self):
        input = """// Hello World!!"""
        output = "<EOF>"
        self.assertTrue(TestLexer.test(input, output, 106))

    def test_lowercase_identifier_6(self):
        input = """/*alibaba*/"""
        output = "<EOF>"
        self.assertTrue(TestLexer.test(input, output, 107))

    def test_lowercase_identifier_7(self):
        input = """/*alibaba*/ */"""
        output = "*,/,<EOF>"
        self.assertTrue(TestLexer.test(input, output, 108))

    def test_lowercase_identifier_8(self):
        input = """ "This is \\"PPL\\" course!" """
        output = """This is \\"PPL\\" course!,<EOF>"""
        self.assertTrue(TestLexer.test(input, output, 109))

    def test_lowercase_identifier_9(self):
        input = """"This is PPL course!"""
        output = "Unclosed String: This is PPL course!"
        self.assertTrue(TestLexer.test(input, output, 110))
        
    def test_lowercase_identifier_10(self):
        input = """~ahbovru"""
        output = "Error Token ~"
        self.assertTrue(TestLexer.test(input, output, 111))
        
    def test_lowercase_identifier_11(self):
        input = """x = 3 + 2 * sum;"""
        output = "x,=,3,+,2,*,sum,;,<EOF>"
        self.assertTrue(TestLexer.test(input, output, 112))
        
    def test_lowercase_identifier_12(self):
        input = """if(true || isEven){x = 5;}"""
        output = "if,(,true,||,isEven,),{,x,=,5,;,},<EOF>"
        self.assertTrue(TestLexer.test(input, output, 113))
        
    def test_lowercase_identifier_13(self): 
        input = """ "test illegal escape \\z" """
        output = "Illegal Escape In String: test illegal escape \\z" 
        self.assertTrue(TestLexer.test(input, output, 114))
        
    def test_lowercase_identifier_14(self):
        input = """ "Johnny: \\"How are you?\\"" """
        output = """Johnny: \\"How are you?\\",<EOF>"""
        self.assertTrue(TestLexer.test(input, output, 115))
        
    def test_lowercase_identifier_15(self):
        input = """/* ahbauvebboubace 
                    cahbjua veoub */ """
        output = "<EOF>"
        self.assertTrue(TestLexer.test(input, output, 116))
        
    def test_lowercase_identifier_16(self):
        input = """/* ahbauvebboubace 
                    cahbjua veoub """
        output = "/,*,ahbauvebboubace,cahbjua,veoub,<EOF>"
        self.assertTrue(TestLexer.test(input, output, 117))
        
    def test_lowercase_identifier_17(self):
        input = """A____bsjhf__091"""
        output = "A____bsjhf__091,<EOF>"
        self.assertTrue(TestLexer.test(input, output, 118))
        
    def test_lowercase_identifier_18(self):
        input = """hoaNguyeN2907inttt"""
        output = "hoaNguyeN2907inttt,<EOF>"
        self.assertTrue(TestLexer.test(input, output, 119))
        
    def test_lowercase_identifier_19(self):
        input = """a,b,c,d : integer;"""
        output = "a,,,b,,,c,,,d,:,integer,;,<EOF>"
        self.assertTrue(TestLexer.test(input, output, 120))
        
    def test_lowercase_identifier_20(self):
        input = """a,b,c,d : integer = 3,5,"a",true;"""
        output = "a,,,b,,,c,,,d,:,integer,=,3,,,5,,,a,,,true,;,<EOF>"
        self.assertTrue(TestLexer.test(input, output, 121))
                
    def test_lowercase_identifier_21(self):
        input = """isOdd: function bool(out number: integer, key: string){}"""
        output = "isOdd,:,function,bool,(,out,number,:,integer,,,key,:,string,),{,},<EOF>"
        self.assertTrue(TestLexer.test(input, output, 122))
                
    def test_lowercase_identifier_22(self):
        input = """isOdd: function bool(out number: integer, key: string) inherit ClassifiedNumber {}"""
        output = "isOdd,:,function,bool,(,out,number,:,integer,,,key,:,string,),inherit,ClassifiedNumber,{,},<EOF>"
        self.assertTrue(TestLexer.test(input, output, 123))
                
    def test_lowercase_identifier_23(self):
        input = """void auto"""
        output = "void,auto,<EOF>"
        self.assertTrue(TestLexer.test(input, output, 124))
                
    def test_lowercase_identifier_24(self):
        input = """while(2+3 == 5){}"""
        output = "while,(,2,+,3,==,5,),{,},<EOF>"
        self.assertTrue(TestLexer.test(input, output, 125))
                
    def test_lowercase_identifier_25(self):
        input = """truefalse"""
        output = "truefalse,<EOF>"
        self.assertTrue(TestLexer.test(input, output, 126))
                
    def test_lowercase_identifier_26(self):
        input = """____1044__23.13e-23"""
        output = "____1044__23,.,13e-23,<EOF>"
        self.assertTrue(TestLexer.test(input, output, 127))
                
    def test_lowercase_identifier_27(self): 
        input = """10_24___34.2e34"""
        output = "1024,___34,.,2e34,<EOF>"
        self.assertTrue(TestLexer.test(input, output, 128))
                
    def test_lowercase_identifier_28(self):
        input = """i == -2"""
        output = "i,==,-,2,<EOF>"
        self.assertTrue(TestLexer.test(input, output, 129))
                
    def test_lowercase_identifier_29(self):
        input = """1131\\212"""
        output = "1131,Error Token \\"
        self.assertTrue(TestLexer.test(input, output, 130))
                
    def test_lowercase_identifier_30(self):
        input = """ "good job \\t high 5" """
        output = "good job \\t high 5,<EOF>"
        self.assertTrue(TestLexer.test(input, output, 131))
                        
    def test_lowercase_identifier_31(self):
        input = """ "good job \\x high 5" """
        output = "Illegal Escape In String: good job \\x"
        self.assertTrue(TestLexer.test(input, output, 132))
                                
    def test_lowercase_identifier_32(self):
        input = """arr : array [3,4] of float;"""
        output = "arr,:,array,[,3,,,4,],of,float,;,<EOF>"
        self.assertTrue(TestLexer.test(input, output, 133))
                                
    def test_lowercase_identifier_33(self):
        input = """12_+_11a"""
        output = "12,_,+,_11a,<EOF>"
        self.assertTrue(TestLexer.test(input, output, 134))
                                
    def test_lowercase_identifier_34(self):
        input = """ "I'm a \\'hero\\'" """
        output = "I'm a \\'hero\\',<EOF>"
        self.assertTrue(TestLexer.test(input, output, 135))
                                
    def test_lowercase_identifier_35(self):
        input = """a = "international";"""
        output = "a,=,international,;,<EOF>"
        self.assertTrue(TestLexer.test(input, output, 136))
                                
    def test_lowercase_identifier_36(self):
        input = """a = "international a;"""
        output = """a,=,Unclosed String: international a;"""
        self.assertTrue(TestLexer.test(input, output, 137))
                                
    def test_lowercase_identifier_37(self):
        input = """a = "international /*aa*/ a;" """
        output = "a,=,international /*aa*/ a;,<EOF>"
        self.assertTrue(TestLexer.test(input, output, 138))
                                
    def test_lowercase_identifier_38(self):
        input = """:::"""
        output = "::,:,<EOF>"
        self.assertTrue(TestLexer.test(input, output, 139))
                                
    def test_lowercase_identifier_39(self):
        input = """ "He tips me 5"$ lastnight!" """
        output = "He tips me 5,Error Token $"
        self.assertTrue(TestLexer.test(input, output, 140))
                                
    def test_lowercase_identifier_40(self):
        input = """01648"""
        output = "0,1648,<EOF>"
        self.assertTrue(TestLexer.test(input, output, 141))
    
    def test_lowercase_identifier_41(self): 
        input = """ "Now u see me \n\\ a" """
        output = "Unclosed String: Now u see me "
        self.assertTrue(TestLexer.test(input, output, 142))
                                
    def test_lowercase_identifier_42(self):
        input = """0___1245"""
        output = "0,___1245,<EOF>"
        self.assertTrue(TestLexer.test(input, output, 143))
                                
    def test_lowercase_identifier_43(self):
        input = """43_56E50"""
        output = "4356E50,<EOF>"
        self.assertTrue(TestLexer.test(input, output, 144))
                                
    def test_lowercase_identifier_44(self):
        input = """ "Check illegal esc \\m tffff" """
        output = "Illegal Escape In String: Check illegal esc \\m"
        self.assertTrue(TestLexer.test(input, output, 145))
                                
    def test_lowercase_identifier_45(self):
        input = """()()()()"""
        output = "(,),(,),(,),(,),<EOF>"
        self.assertTrue(TestLexer.test(input, output, 146))
                                
    def test_lowercase_identifier_46(self):
        input = """[{]}(||)"""
        output = "[,{,],},(,||,),<EOF>"
        self.assertTrue(TestLexer.test(input, output, 147))
                                
    def test_lowercase_identifier_47(self):
        input = """if(any || group && trything){}"""
        output = "if,(,any,||,group,&&,trything,),{,},<EOF>"
        self.assertTrue(TestLexer.test(input, output, 148))
                                
    def test_lowercase_identifier_48(self):
        input = """ "Try something new \\\\ like swimming \\\\" """
        output = "Try something new \\\\ like swimming \\\\,<EOF>"
        self.assertTrue(TestLexer.test(input, output, 149))
                                
    def test_lowercase_identifier_49(self):
        input = """2+34|5"""
        output = "2,+,34,Error Token |"
        self.assertTrue(TestLexer.test(input, output, 150))
                                        
    def test_lowercase_identifier_50(self):
        input = """ "Test escape character \\b \\t \\f" """
        output = "Test escape character \\b \\t \\f,<EOF>"
        self.assertTrue(TestLexer.test(input, output, 151))
    
    def test_lowercase_identifier_51(self):
        input = """O_________Wsome______thing"""
        output = "O_________Wsome______thing,<EOF>"
        self.assertTrue(TestLexer.test(input, output, 152))
                                
    def test_lowercase_identifier_52(self): 
        input = """ "Test unclosing string \n\";" """
        output = "Unclosed String: Test unclosing string "
        self.assertTrue(TestLexer.test(input, output, 153))
                                
    def test_lowercase_identifier_53(self):
        input = """auto void ."""
        output = "auto,void,.,<EOF>"
        self.assertTrue(TestLexer.test(input, output, 154))
                                
    def test_lowercase_identifier_54(self):
        input = """void_____"""
        output = "void_____,<EOF>"
        self.assertTrue(TestLexer.test(input, output, 155))
                                
    def test_lowercase_identifier_55(self):
        input = """m = 2 "+" 3 ;"""
        output = "m,=,2,+,3,;,<EOF>"
        self.assertTrue(TestLexer.test(input, output, 156))
                                
    def test_lowercase_identifier_56(self):
        input = """/*i do not know */ /~/~"""
        output = "/,Error Token ~"
        self.assertTrue(TestLexer.test(input, output, 157))
                                
    def test_lowercase_identifier_57(self):
        input = """string tmp[2] = {"House", "Family"};"""
        output = "string,tmp,[,2,],=,{,House,,,Family,},;,<EOF>"
        self.assertTrue(TestLexer.test(input, output, 158))
                                
    def test_lowercase_identifier_58(self):
        input = """ "\\\ " """
        output = "\\\ ,<EOF>"
        self.assertTrue(TestLexer.test(input, output, 159))
                                
    def test_lowercase_identifier_59(self):
        input = """ for i in range(2,3): sum++ """
        output = "for,i,in,range,(,2,,,3,),:,sum,+,+,<EOF>"
        self.assertTrue(TestLexer.test(input, output, 160))
                                        
    def test_lowercase_identifier_60(self):
        input = """ "\\\" """
        output = "Unclosed String: \\\" "
        self.assertTrue(TestLexer.test(input, output, 161))
    
    def test_lowercase_identifier_61(self):
        input = """========="""
        output = "==,==,==,==,=,<EOF>"
        self.assertTrue(TestLexer.test(input, output, 162))
                                
    def test_lowercase_identifier_62(self):
        input = """ "Hi there! \" What u r doing \"" """
        output = "Hi there! ,What,u,r,doing,,<EOF>"
        self.assertTrue(TestLexer.test(input, output, 163))
                                
    def test_lowercase_identifier_63(self):
        input = """|&||"""
        output = "Error Token |"
        self.assertTrue(TestLexer.test(input, output, 164))
                                
    def test_lowercase_identifier_64(self):
        input = """=&%|"""
        output = "=,Error Token &"
        self.assertTrue(TestLexer.test(input, output, 165))
                                
    def test_lowercase_identifier_65(self):
        input = """ "\\l so bad!" """
        output = "Illegal Escape In String: \\l"
        self.assertTrue(TestLexer.test(input, output, 166))
                                
    def test_lowercase_identifier_66(self):
        input = """!!=====!"""
        output = "!,!=,==,==,!,<EOF>"
        self.assertTrue(TestLexer.test(input, output, 167))
                                
    def test_lowercase_identifier_67(self):
        input = """123_+900_00"""
        output = "123,_,+,90000,<EOF>"
        self.assertTrue(TestLexer.test(input, output, 168))
                                
    def test_lowercase_identifier_68(self):
        input = """5 >= 3"""
        output = "5,>=,3,<EOF>"
        self.assertTrue(TestLexer.test(input, output, 169))
                                
    def test_lowercase_identifier_69(self):
        input = """>==<==>>"""
        output = ">=,=,<=,=,>,>,<EOF>"
        self.assertTrue(TestLexer.test(input, output, 170))
                                        
    def test_lowercase_identifier_70(self):
        input = """<>!<===="""
        output = "<,>,!,<=,==,=,<EOF>"
        self.assertTrue(TestLexer.test(input, output, 171))
    
    def test_lowercase_identifier_71(self):
        input = """foo(1,2,2,2::"concat");"""
        output = "foo,(,1,,,2,,,2,,,2,::,concat,),;,<EOF>"
        self.assertTrue(TestLexer.test(input, output, 172))
                                
    def test_lowercase_identifier_72(self):
        input = """summerAndFall = 2; fall--"""
        output = "summerAndFall,=,2,;,fall,-,-,<EOF>"
        self.assertTrue(TestLexer.test(input, output, 173))
                                
    def test_lowercase_identifier_73(self):
        input = """_______________name_______trtr____1213"""
        output = "_______________name_______trtr____1213,<EOF>"
        self.assertTrue(TestLexer.test(input, output, 174))
                                
    def test_lowercase_identifier_74(self):
        input = """cin >> string >> a;"""
        output = "cin,>,>,string,>,>,a,;,<EOF>"
        self.assertTrue(TestLexer.test(input, output, 175))
                                
    def test_lowercase_identifier_75(self):
        input = """ "Draw the \\"Spider-man\\" in 30s"? """
        output = """Draw the \\"Spider-man\\" in 30s,Error Token ?"""
        self.assertTrue(TestLexer.test(input, output, 176))
                                
    def test_lowercase_identifier_76(self):
        input = """\"Catching the escapse \y hhh\""""
        output = "Illegal Escape In String: Catching the escapse \\y"
        self.assertTrue(TestLexer.test(input, output, 177))
                                
    def test_lowercase_identifier_77(self):
        input = """748563_367e-12"""
        output = "748563367e-12,<EOF>"
        self.assertTrue(TestLexer.test(input, output, 178))
                                
    def test_lowercase_identifier_78(self):
        input = """\"Just gonna stand there \\t\""""
        output = "Just gonna stand there \\t,<EOF>"
        self.assertTrue(TestLexer.test(input, output, 179))
                                
    def test_lowercase_identifier_79(self):
        input = """\"if(a==1) a=2 else a=5"""
        output = "Unclosed String: if(a==1) a=2 else a=5"
        self.assertTrue(TestLexer.test(input, output, 180))
                                        
    def test_lowercase_identifier_80(self):
        input = """if(a==1) a=2 else a=5"""
        output = "if,(,a,==,1,),a,=,2,else,a,=,5,<EOF>"
        self.assertTrue(TestLexer.test(input, output, 181))
    
    def test_lowercase_identifier_81(self):
        input = """return tmp,sum"""
        output = "return,tmp,,,sum,<EOF>"
        self.assertTrue(TestLexer.test(input, output, 182))
                                
    def test_lowercase_identifier_82(self):
        input = """ "" """
        output = ",<EOF>"
        self.assertTrue(TestLexer.test(input, output, 183))
                                
    def test_lowercase_identifier_83(self):
        input = """0.23e-23"""
        output = "0.23e-23,<EOF>"
        self.assertTrue(TestLexer.test(input, output, 184))
                                
    def test_lowercase_identifier_84(self):
        input = """rem : string = "King Kong";"""
        output = "rem,:,string,=,King Kong,;,<EOF>"
        self.assertTrue(TestLexer.test(input, output, 185))
                    
    def test_lowercase_identifier_85(self):
        input = """rem : string = \"King Kong;"""
        output = "rem,:,string,=,Unclosed String: King Kong;"
        self.assertTrue(TestLexer.test(input, output, 186))
                                
    def test_lowercase_identifier_86(self):
        input = """for(;;n/2){}"""
        output = "for,(,;,;,n,/,2,),{,},<EOF>"
        self.assertTrue(TestLexer.test(input, output, 187))
                                
    def test_lowercase_identifier_87(self):
        input = """for(;;n/2){\"\"}"""
        output = "for,(,;,;,n,/,2,),{,,},<EOF>"
        self.assertTrue(TestLexer.test(input, output, 188))
                                
    def test_lowercase_identifier_88(self):
        input = """\"I'm Batman!\\'"""
        output = "Unclosed String: I'm Batman!\\'"
        self.assertTrue(TestLexer.test(input, output, 189))
                                
    def test_lowercase_identifier_89(self):
        input = """awhile 23__ under"""
        output = "awhile,23,__,under,<EOF>"
        self.assertTrue(TestLexer.test(input, output, 190))
                                        
    def test_lowercase_identifier_90(self):
        input = """---/---*/*-*/"""
        output = "-,-,-,/,-,-,-,*,<EOF>"
        self.assertTrue(TestLexer.test(input, output, 191))
    
    def test_lowercase_identifier_91(self):
        input = """000372826"""
        output = "0,0,0,372826,<EOF>"
        self.assertTrue(TestLexer.test(input, output, 192))
                                
    def test_lowercase_identifier_92(self):
        input = """2_758_637_27787"""
        output = "275863727787,<EOF>"
        self.assertTrue(TestLexer.test(input, output, 193))
                                
    def test_lowercase_identifier_93(self):
        input = """clinstar^"""
        output = "clinstar,Error Token ^"
        self.assertTrue(TestLexer.test(input, output, 194))
                                
    def test_lowercase_identifier_94(self):
        input = """Oh my god`````"""
        output = "Oh,my,god,Error Token `"
        self.assertTrue(TestLexer.test(input, output, 195))
                                
    def test_lowercase_identifier_95(self):
        input = """tmp-intt-=2;"""
        output = "tmp,-,intt,-,=,2,;,<EOF>"
        self.assertTrue(TestLexer.test(input, output, 196))
                                
    def test_lowercase_identifier_96(self):
        input = """\"\\'\\'\""""
        output = "\\'\\',<EOF>"
        self.assertTrue(TestLexer.test(input, output, 197))
                                
    def test_lowercase_identifier_97(self):
        input = """ \"Blue or Red?!?!?! """
        output = "Unclosed String: Blue or Red?!?!?! "
        self.assertTrue(TestLexer.test(input, output, 198))
                                
    def test_lowercase_identifier_98(self):
        input = """ Mrs.tam: "do not use ice!" """
        output = "Mrs,.,tam,:,do not use ice!,<EOF>"
        self.assertTrue(TestLexer.test(input, output, 199))
                                
    def test_lowercase_identifier_99(self):
        input = """c = 675 // wow"""
        output = "c,=,675,<EOF>"
        self.assertTrue(TestLexer.test(input, output, 200))
 
    