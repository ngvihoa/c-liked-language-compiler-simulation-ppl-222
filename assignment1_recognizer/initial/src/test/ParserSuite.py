import unittest
from TestUtils import TestParser


class ParserSuite(unittest.TestCase):
    def test_simple_program(self):
        input = """isEven: function boolean(a: boolean) {}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 201))
    
    def test_simple_program_1(self):
        input = """
        for (i=1, i<10,i+1) {
            for( k = 0, k<-2, k*1) {
                a: integer;
            }
            b: string = "hello/";
        }
        }"""
        expect = "Error on line 2 col 8: for"
        self.assertTrue(TestParser.test(input, expect, 202))

    def test_simple_program_2(self):
        input = """a_: float = 1.22;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 203))
        
    def test_simple_program_3(self):
        input = """a_: float = 1.22"""
        expect = "Error on line 1 col 16: <EOF>"
        self.assertTrue(TestParser.test(input, expect, 204))
                
    def test_simple_program_4(self):
        input = """a_: float = 1.22
        a = 5;"""
        expect = "Error on line 2 col 8: a"
        self.assertTrue(TestParser.test(input, expect, 205))
                        
    def test_simple_program_5(self):
        input = """a_: float = 1.22,3.33;"""
        expect = "Error on line 1 col 16: ,"
        self.assertTrue(TestParser.test(input, expect, 206)) 

    def test_simple_program_6(self):
        input = """a_,_b,__C: float = 1.22,3.33;"""
        expect = "Error on line 1 col 28: ;"
        self.assertTrue(TestParser.test(input, expect, 207)) 

    def test_simple_program_7(self):
        input = """
        foo: function integer (n: integer) {
            if (n == 0) return 1;
            else return n * fact(n - 1);
        }
        main: function void() {
            del: integer = foo(3);
            printInteger(del);
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 208)) 

    def test_simple_program_8(self):
        input = """
        foo: function integer (n: integer) {
            if (n == 0) return 1;
            else return n * fact(n - 1);
        }
        main: function void() {
            del: integer = foo(3);
            printInteger(del)
        }"""
        expect = "Error on line 9 col 8: }"
        self.assertTrue(TestParser.test(input, expect, 209)) 

    def test_simple_program_9(self):
        input = """
        foo: function integer (n: integer) {
            if (n == 0 return 1;
            else return n * fact(n - 1);
        }
        main: function void() {
            del: integer = foo(3);
            printInteger(del);
        }"""
        expect = "Error on line 3 col 23: return"
        self.assertTrue(TestParser.test(input, expect, 210))
                               
    def test_simple_program_10(self):
        input = """
        foo: function integer (n: integer) {
            if (n == 0) return 1;
            else return n fact(n - 1);
        }
        main: function void() {
            del: integer = foo(3);
            printInteger(del)
        }"""
        expect = "Error on line 4 col 26: fact"
        self.assertTrue(TestParser.test(input, expect, 211))
                               
    def test_simple_program_11(self):
        input = """
        foo: function integer (n: integer) {
            if (n == 0) return 1;
            else return n * fact(n - 1);
        }
        main function void() {
            del: integer = foo(3);
            printInteger(del)
        }"""
        expect = "Error on line 6 col 13: function"
        self.assertTrue(TestParser.test(input, expect, 212))
                               
    def test_simple_program_12(self):
        input = """if(i == (2-1) + 3) sum = foo(inte,21);"""
        expect = "Error on line 1 col 0: if"
        self.assertTrue(TestParser.test(input, expect, 213))
                               
    def test_simple_program_13(self):
        input = """
        comp: function boolean(a: integer, b: integer){
            return a > b;
        }
        main: function void(){
            a: array [6] of integer = {0, 1, 2, 3, 4, 5};
            sort(a, a + 6, comp); // we get 5 4 3 2 1 0
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 214))
                               
    def test_simple_program_14(self):
        input = """
        comp: function boolean(a, b: integer){
            return a > b;
        }
        main: function void(){
            a: array [6] of integer = {0, 1, 2, 3, 4, 5};
            sort(a, a + 6, comp); // we get 5 4 3 2 1 0
        }"""
        expect = "Error on line 2 col 32: ,"
        self.assertTrue(TestParser.test(input, expect, 215))
                               
    def test_simple_program_15(self):
        input = """
        comp: function int(a: integer, b: integer){
            return a > b;
        }
        main: function void(){
            a: array [6] of integer = {0, 1, 2, 3, 4, 5};
            sort(a, a + 6, comp); // we get 5 4 3 2 1 0
        }"""
        expect = "Error on line 2 col 23: int"
        self.assertTrue(TestParser.test(input, expect, 216))
                               
    def test_simple_program_16(self):
        input = """
        comp: function boolean(a: integer, b: integer){
            return a > b;
        }
        main: funion void(){
            a: array [6] of integer = {0, 1, 2, 3, 4, 5};
            sort(a, a + 6, comp); // we get 5 4 3 2 1 0
        }"""
        expect = "Error on line 5 col 14: funion"
        self.assertTrue(TestParser.test(input, expect, 217))
                               
    def test_simple_program_17(self):
        input = """
        comp: function boolean(a: integer, b: integer){
            return a > b;
        
        main: function void(){
            a: array [6] of integer = {0, 1, 2, 3, 4, 5};
            sort(a, a + 6, comp); // we get 5 4 3 2 1 0
        }"""
        expect = "Error on line 5 col 14: function"
        self.assertTrue(TestParser.test(input, expect, 218))
                               
    def test_simple_program_18(self):
        input = """
        comp: function boolean(a: integer, b: integer){
            return a <== b;
        }
        main: function void(){
            a: array [6] of integer = {0, 1, 2, 3, 4, 5};
            sort(a, a + 6, comp); // we get 5 4 3 2 1 0
        }"""
        expect = "Error on line 3 col 23: ="
        self.assertTrue(TestParser.test(input, expect, 219))
                               
    def test_simple_program_19(self):
        input = """
        comp: function boolean(a: integer, b: integer){
            return a > b;
        }
        main: function void(){
            a: array [6 of integer = {0, 1, 2, 3, 4, 5};
            sort(a, a + 6, comp); // we get 5 4 3 2 1 0
        }"""
        expect = "Error on line 6 col 24: of"
        self.assertTrue(TestParser.test(input, expect, 220))
                               
    def test_simple_program_20(self):
        input = """
        comp: function boolean(a: integer, b: integer){
            return a > b;
        }
        main: function void(){
            a: array [6] of integer = {0, 1, 2, 3, 4, 5};
            sort(a, a + 6, comp); / we get 5 4 3 2 1 0
        }"""
        expect = "Error on line 7 col 34: /"
        self.assertTrue(TestParser.test(input, expect, 221))
                                       
    def test_simple_program_21(self):
        input = """/* This is multiple comment line 
        ~~*/"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 222))
                               
    def test_simple_program_22(self):
        input = """a,b,c: array [3] of boolean = {true, true, false},{false, false, false},{false, true, false};"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 223))
                               
    def test_simple_program_23(self):
        input = """a,b,c: array [3] of = {true, true, false},{false, false, false},{false, true, false};"""
        expect = "Error on line 1 col 20: ="
        self.assertTrue(TestParser.test(input, expect, 224))
                               
    def test_simple_program_24(self):
        input = """a,b,c: array [3] of void = {true, true, false},{false, false, false},{false, true, false};"""
        expect = "Error on line 1 col 20: void"
        self.assertTrue(TestParser.test(input, expect, 225))
                               
    def test_simple_program_25(self):
        input = """a,b,c: array [3] of auto = {true, true, false},{false, false, false},{false, true, false};"""
        expect = "Error on line 1 col 20: auto"
        self.assertTrue(TestParser.test(input, expect, 226))
                               
    def test_simple_program_26(self):
        input = """index, undex, odex: string;;
        /* Please do not care this /**/
        */"""
        expect = "Error on line 1 col 27: ;"
        self.assertTrue(TestParser.test(input, expect, 227))
                               
    def test_simple_program_27(self):
        input = """time: array [] of string;"""
        expect = "Error on line 1 col 13: ]"
        self.assertTrue(TestParser.test(input, expect, 228))
                               
    def test_simple_program_28(self):
        input = """time: array [,,] of string;"""
        expect = "Error on line 1 col 13: ,"
        self.assertTrue(TestParser.test(input, expect, 229))
                               
    def test_simple_program_29(self):
        input = """time: array [2] of stringIntFLoat__;"""
        expect = "Error on line 1 col 19: stringIntFLoat__"
        self.assertTrue(TestParser.test(input, expect, 230))
                               
    def test_simple_program_30(self):
        input = """time:: array [] of string;"""
        expect = "Error on line 1 col 4: ::"
        self.assertTrue(TestParser.test(input, expect, 231))
                                       
    def test_simple_program_31(self):
        input = """exp: string = tmp1::tmp2;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 232))
                               
    def test_simple_program_32(self):
        input = """exp: string = tmp1::(tmp2 + 3);"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 233))
                               
    def test_simple_program_33(self):
        input = """
        isEven: function boolean(a: integer) inherit isCNUmber {
            if(a % 2 == 0) return true;
            return false;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 234))
                               
    def test_simple_program_34(self):
        input = """
        isEven: function boolean(a: integer) inherit {
            if(a % 2 == 0) return true;
            return false;
        }
        """
        expect = "Error on line 2 col 53: {"
        self.assertTrue(TestParser.test(input, expect, 235))
                               
    def test_simple_program_35(self):
        input = """
        isEven: function boolean(a: integer)  isCNUmber {
            if(a % 2 == 0) return true;
            return false;
        }
        """
        expect = "Error on line 2 col 46: isCNUmber"
        self.assertTrue(TestParser.test(input, expect, 236))
                               
    def test_simple_program_36(self):
        input = """
        isEven: function boolean(a: integer) {
            if(a % 2 == 0) return true;
            false;
        }
        """
        expect = "Error on line 4 col 17: ;"
        self.assertTrue(TestParser.test(input, expect, 237))
                               
    def test_simple_program_37(self):
        input = """
        isEven: function boolean(a: integer) {
            if(a % 2 == ) return true;
            return false;
        }
        """
        expect = "Error on line 3 col 24: )"
        self.assertTrue(TestParser.test(input, expect, 238))
                               
    def test_simple_program_38(self):
        input = """cppBubbleSort: function void(A: array [10] of integer, n: integer) {
        for (i = 0, i < n - 1, i+1)
            for (j = 0, j < n - i - 1, j+1)
                if (A[j] > A[j + 1])
                    swap(A[j], A[j + 1]);
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 239))
                               
    def test_simple_program_39(self):
        input = """cppBubbleSort: function void(A: array [10] of integer, n: integer) {
        for (i = 0; i < n - 1, i+1)
            for (j = 0, j < n - i - 1, j+1)
                if (A[j] > A[j + 1])
                    swap(A[j], A[j + 1]);
        }"""
        expect = "Error on line 2 col 18: ;"
        self.assertTrue(TestParser.test(input, expect, 240))
                               
    def test_simple_program_40(self):
        input = """cppBubbleSort: function auto(A: array [10] of integer, n: integer) {
        for (i = 0, i < n - 1, i+1)
            for (j = 0, j < n - i - 1, j+1)
                if (A[j] > A[j + 1])
                    swap(A[j], A[j + 1]);
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 241))
                                       
    def test_simple_program_41(self):
        input = """cppBubbleSort: function void(A: array [10] of integer, n: integer) {
        for (i = 0, i < n - 1, i+1)
            for (j = 0, j < n - i - 1, j+ 1)
                if (&&(A[j] > A[j + 1]))
                    swap(A[j], A[j + 1]);
        }"""
        expect = "Error on line 4 col 20: &&"
        self.assertTrue(TestParser.test(input, expect, 242))
                               
    def test_simple_program_42(self):
        input = """simple: function array [13,2] of float(n: integer) {}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 243))
                               
    def test_simple_program_43(self):
        input = """simple: function array [13,2] of float(n: integer) {};;"""
        expect = "Error on line 1 col 53: ;"
        self.assertTrue(TestParser.test(input, expect, 244))
                               
    def test_simple_program_44(self):
        input = """simple: function array [13.2e23] of float(n: integer) {}"""
        expect = "Error on line 1 col 24: 13.2e23"
        self.assertTrue(TestParser.test(input, expect, 245))
                               
    def test_simple_program_45(self):
        input = """simple: function array [0254] of float(n: integer) {}"""
        expect = "Error on line 1 col 25: 254"
        self.assertTrue(TestParser.test(input, expect, 246))
                               
    def test_simple_program_46(self):
        input = """simple: function array [13_2] of float(n: integer) {}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 247))
                               
    def test_simple_program_47(self):
        input = """simple: function (n: integer) {}"""
        expect = "Error on line 1 col 17: ("
        self.assertTrue(TestParser.test(input, expect, 248))
                               
    def test_simple_program_48(self):
        input = """simple: function {}"""
        expect = "Error on line 1 col 17: {"
        self.assertTrue(TestParser.test(input, expect, 249))
                               
    def test_simple_program_49(self):
        input = """simple: function [13,2] of float(n: integer) {}"""
        expect = "Error on line 1 col 17: ["
        self.assertTrue(TestParser.test(input, expect, 250))
                            
    def test_simple_program_50(self):
        input = """simple: function array [13,2] of float(n: integer) {
            goo();
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 251))
                                       
    def test_simple_program_51(self):
        input = """simple: function array [13,2] of float(n: integer) {
            x::a = inte(x);
        }"""
        expect = "Error on line 2 col 13: ::"
        self.assertTrue(TestParser.test(input, expect, 252))
                               
    def test_simple_program_52(self):
        input = """i: integer = 10;
        i++;"""
        expect = "Error on line 2 col 9: +"
        self.assertTrue(TestParser.test(input, expect, 253))
                               
    def test_simple_program_53(self):
        input = """i: string = "Hello there \\x";"""
        expect = "Hello there \\x"
        self.assertTrue(TestParser.test(input, expect, 254))
                               
    def test_simple_program_54(self):
        input = """i: integer = 10-23*23/47+1;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 255))
                               
    def test_simple_program_55(self):
        input = """i: integer = 10-23*23/47-1+;""" 
        expect = "Error on line 1 col 27: ;"
        self.assertTrue(TestParser.test(input, expect, 256))
                               
    def test_simple_program_56(self):
        input = """main: function void(){
        n: integer = 12;
        while{!n){
            printLn(n);
            n = n-1;
        }
        }"""
        expect = "Error on line 3 col 13: {"
        self.assertTrue(TestParser.test(input, expect, 257))
                               
    def test_simple_program_57(self):
        input = """main: function void(){
        n: integer = 12;
        while(!n){
            printLn(n);
            n = n-1;
            if(n == 3) break;
        }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 258))
                               
    def test_simple_program_58(self):
        input = """main: function void(){
        n: integer = 12;
        while(!n){
            printLn(n);
            n = n--1;
            if(n == 3) break;
        }
        }"""        
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 259))
                               
    def test_simple_program_59(self):
        input = """main: function void(){
        n: integer = 12;
        while(-!n){
            printLn(n);
            n = n-1;
            if(n == 3) continue;
        }
        }"""        
        expect = "Error on line 3 col 15: !"
        self.assertTrue(TestParser.test(input, expect, 260))
                               
    def test_simple_program_60(self):
        input = """main: function void(){
        n: integer = 12;
        while(!-n){
            printLn(n);
            n = n-1;
            if(n == 3) break;
        }
        }"""        
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 261))
                                       
    def test_simple_program_61(self):
        input = """main: function void(){
        n: integer = 12;
        while(!n){
            printLn(n);
            n = n-1;
            if(n == 3) break;
            else b = a || false || true;
        }
        }"""        
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 262))
                               
    def test_simple_program_62(self):
        input = """main: function void(){
        n: integer = 12;
        while(!n){
            printLn(n);
            n = n-1;
            if(n == 3) break;
            else b = a || false || true;
        }
        }"""        
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 263))
                               
    def test_simple_program_63(self):
        input = """main: function void(){
        n: integer = 12;
        while(!n){
            printLn(n);
            n = n-1;
            if(n == 3) break;
            else b = a || false || true;
        }
        """        
        expect = "Error on line 9 col 8: <EOF>"
        self.assertTrue(TestParser.test(input, expect, 264))
                               
    def test_simple_program_64(self):
        input = """main: function void(){
        n: integer = 12;
        while(if(true) a = 5)){
            printLn(n);
            n = n-1;
            if(n == 3) break;
            else b = a || false || true;
        }
        }"""        
        expect = "Error on line 3 col 14: if"
        self.assertTrue(TestParser.test(input, expect, 265))
                               
    def test_simple_program_65(self):
        input = """main: function void(){
        n: integer = 12;
        for(i = 3, a[n], n - 1){
            generateNumber(mm);
            setString("incarese");
            a[n] = 1 + a[n-1];
        }   
        }"""        
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 266))
                               
    def test_simple_program_66(self):
        input = """main: function void(){
        n: integer = 12;
        for(i = 3, a[n], n - 1){
            generateNumber(mm);
            setString("incarese");
            a[n] = 1 + an-1];
        }   
        }"""        
        expect = "Error on line 6 col 27: ]"
        self.assertTrue(TestParser.test(input, expect, 267))
                               
    def test_simple_program_67(self):
        input = """main: function void(){
        n: integer = 12;
        for(i = 3, a[n],, n - 1){
            generateNumber(mm);
            setString("incarese");
            a[n] = 1 + a[n-1];
        }   
        }"""        
        expect = "Error on line 3 col 24: ,"
        self.assertTrue(TestParser.test(input, expect, 268))
                               
    def test_simple_program_68(self):
        input = """main: function void(){
        n: integer = 12;
        for(i, a[n], n - 1){
            generateNumber(mm);
            setString("incarese");
            a[n] = 1 + a[n-1];
        }   
        }"""        
        expect = "Error on line 3 col 13: ,"
        self.assertTrue(TestParser.test(input, expect, 269))
                               
    def test_simple_program_69(self):
        input = """main: function void(){
        n: integer = 12;
        for(i = 3, a[n], n - 1){
            generateNumber(mm);
            setString("incarese");
            a[n] = 1 + a[n-1];
        }   
        }"""        
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 270))
                               
    def test_simple_program_70(self):
        input = """main: function void(){
        n: integer == 12;
        for(i = 3, a[n], n - 1){
            generateNumber(mm);
            setString("incarese");
            a[n] = 1 + a[n-1];
        }   
        }"""        
        expect = "Error on line 2 col 19: =="
        self.assertTrue(TestParser.test(input, expect, 271))
                                       
    def test_simple_program_71(self):
        input = """main: Function void(){
        n: integer = 12;
        for(i = 3, a[n], n - 1){
            generateNumber(mm);
            setString("incarese");
            a[n] = 1 + a[n-1];
        }   
        }"""        
        expect = "Error on line 1 col 6: Function"
        self.assertTrue(TestParser.test(input, expect, 272))
                               
    def test_simple_program_72(self):
        input = """main: function void(){
        do:
        foo(iii, 3.6, 3e-23);
        while (a > 100);
        }"""        
        expect = "Error on line 2 col 10: :"
        self.assertTrue(TestParser.test(input, expect, 273))
                               
    def test_simple_program_73(self):
        input = """main: function void(){
        do{
        foo(iii, 3.6, 3e-23);
        } while (a > 100);
        }"""        
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 274))
                               
    def test_simple_program_74(self):
        input = """main: function void(){
        do{
        foo(iii, 3.6, 3e-23);
        } while (a > 100)
        }"""        
        expect = "Error on line 5 col 8: }"
        self.assertTrue(TestParser.test(input, expect, 275))
                               
    def test_simple_program_75(self):
        input = """main: function void(){
        do{
        foo(iii, 3.6, 3e-23);
        } while float(a > 100);
        }"""        
        expect = "Error on line 4 col 16: float"
        self.assertTrue(TestParser.test(input, expect, 276))
                               
    def test_simple_program_76(self):
        input = """main: function void(inherit out m: integer){
        do {
        a+1;
        foo(iii, 3.6, 3e-23);
        } while (a > 100);
        m = a;
        }"""        
        expect = "Error on line 3 col 9: +"
        self.assertTrue(TestParser.test(input, expect, 277))
                               
    def test_simple_program_77(self):
        input = """main: function void(){
        do // Something wrong
        a+1;
        foo(iii, 3.6, 3e-23);
        } while float(a > 100);
        }"""        
        expect = "Error on line 3 col 8: a"
        self.assertTrue(TestParser.test(input, expect, 278))
                               
    def test_simple_program_78(self):
        input = """main: function void(){
        do{
        a++;
        foo(iii, 3.6, 3e-23);
        } while float(a > 100);
        }"""        
        expect = "Error on line 3 col 9: +"
        self.assertTrue(TestParser.test(input, expect, 279))
                               
    def test_simple_program_79(self):
        input = """main: function void(){
        do{
        a[for] = a+1;
        foo(iii, 3.6, 3e-23);
        } while float(a > 100);
        }"""        
        expect = "Error on line 3 col 10: for"
        self.assertTrue(TestParser.test(input, expect, 280))
                               
    def test_simple_program_80(self):
        input = """randomFunction: function void(){
            tmp = stringInt :: "concate \\f" :: _34;
        }"""
        expect = "Error on line 2 col 44: ::"
        self.assertTrue(TestParser.test(input, expect, 281))
                                       
    def test_simple_program_81(self):
        input = """randomFunction: function void(){
            tmp = stringInt == "concate \\f" == _34;
        }"""
        expect = "Error on line 2 col 44: =="
        self.assertTrue(TestParser.test(input, expect, 282))
                               
    def test_simple_program_82(self):
        input = """randomFunction: function void(){
            tmp = stringInt >= "concate \\f" < _34;
        }"""
        expect = "Error on line 2 col 44: <"
        self.assertTrue(TestParser.test(input, expect, 283))
                               
    def test_simple_program_83(self):
        input = """randomFunction: function void(){
            tmp[(foo(23) - innerNum + 34) == "hfjgj \\b"] = stringInt + "concate \\f" + _34;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 284))
                               
    def test_simple_program_84(self):
        input = """randomFunction: function void(){
            tmp[5] = a + 2 * b && b % 5.0 + "daaaaaaaaa";
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 285))
                               
    def test_simple_program_85(self):
        input = """randomFunction: function void(){
            tmp[2,3] = tmp[f23()];
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 286))
                               
    def test_simple_program_86(self):
        input = """randomFunction: function void(){
            tmp: array [10] of integer;
            tmp[m] = {2,3,4,5};
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 287))
                               
    def test_simple_program_87(self):
        input = """randomFunction: function integer("__2": string){
            return 2;
        }"""
        expect = "Error on line 1 col 33: __2"
        self.assertTrue(TestParser.test(input, expect, 288))
                               
    def test_simple_program_88(self):
        input = """randomFunction: function integer("5"b[3]: boolean){
            return 2;
        }"""
        expect = "Error on line 1 col 33: 5"
        self.assertTrue(TestParser.test(input, expect, 289))
                               
    def test_simple_program_89(self):
        input = """randomFunction: function integer"dd"(out b[3]: boolean){
            return 2;
        }"""
        expect = "Error on line 1 col 32: dd"
        self.assertTrue(TestParser.test(input, expect, 290))
                               
    def test_simple_program_90(self):
        input = """randomFunction: function integer(b: boolean, tmp: void){
            return 2;
        }"""
        expect = "Error on line 1 col 50: void"
        self.assertTrue(TestParser.test(input, expect, 291))
                                       
    def test_simple_program_91(self):
        input = """main: function void(){
            print("King Kong will come to YNC next month!!");
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 292))
                               
    def test_simple_program_92(self):
        input = """main: function void(){
            // Comment
            num :: integer = 23;
        }"""
        expect = "Error on line 3 col 16: ::"
        self.assertTrue(TestParser.test(input, expect, 293))
                               
    def test_simple_program_93(self):
        input = """main: function void(){
            // Comment
            num: array [4,7,5] of integer = {2.5,"hdjsh",timr + 2};
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 294))
                               
    def test_simple_program_94(self):
        input = """main: function void(){
            a,b: float;
            a = 3.5;
            b = 7.6;
            printLn(a, b::"+");
            printLn(a, b, "-");
            printLn(a, b, "/");
            printLn(a, b, "<");
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 295))
                               
    def test_simple_program_95(self):
        input = """main: function void(){
            a,b: float;
            a = 3.5;
            b = 7.6;
            printLn(a, b, "+");
            printLn(a, b, "-");
            printLn(a, b, "/");
            printLn(a, b, "<");
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 296))
                               
    def test_simple_program_96(self):
        input = """main: function void(){
            n: integer = 23;
            sum: integer;
            for(k = 1, k <= n, k +1 ) {
                sum = sum + k;
            }
            print("The sum from 1 to n: \\t", sum);
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 297))
                               
    def test_simple_program_97(self):
        input = """
        calling: string = "\\t Welcome to NYC:\\t";
        main: function void(){
            n: integer = 100;
            while(n % (n - 3)){
                printLn(calling, n);
                n = n - 1;
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 298))
                               
    def test_simple_program_98(self):
        input = """main: function void() {
        while(i <= 3 && true) 
            foo("calling the number", i);
            i = i - 1;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 299))
                               
    def test_simple_program_99(self):
        input = """varr: float = 0.3e+7;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 300))
                               
    