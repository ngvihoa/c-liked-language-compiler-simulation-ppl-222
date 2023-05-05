import unittest
from TestUtils import TestChecker
from AST import *

class CheckerSuite(unittest.TestCase):
    def test_checker1(self):
        input = """x: integer;"""
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input, expect, 401))
    
    def test_checker2(self):
        input = """x: integer;
        main: function void(){}"""
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 402))

    def test_checker3(self):
        input = """foo: function auto(){}
        main: function void(){
            foo: integer = 3;
            a: integer;
            a = foo();
        }"""
        expect = "Type mismatch in expression: FuncCall(foo, [])"
        self.assertTrue(TestChecker.test(input, expect, 403))

    def test_checker4(self):
        input = """foo: function array [2,3] of integer(out inherit a: boolean){}"""
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input, expect, 404))

#########################################################################

    def test_checker5(self):
        input = """x: integer;
        main: function void(){
            while(x < 10){
                i: integer;
                for(i = 0, i < x, i + 1){
                    break;
                }
            }
        }"""
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 405))
    
    def test_checker6(self):
        input = """main: function integer(){}
        main: function void(){}"""
        expect = "Redeclared Function: main"
        self.assertTrue(TestChecker.test(input, expect, 406))

    def test_checker7(self):
        input = """x: integer;
        ta: function auto(out a: boolean) inherit foo{
            return true;
        }
        main: function void(){}
        
        foo: function void(inherit k: integer){}"""
        expect = "Invalid statement in function: ta"
        self.assertTrue(TestChecker.test(input, expect, 407))

    def test_checker8(self):
        input = """x: integer;
        ta: function auto(out a: boolean) inherit foo{
            super(1);
            return true;
        }
        main: function void(){}
        
        foo: function void(inherit k: integer){}
        foo: function string(b: string, c: string){}"""
        expect = "Redeclared Function: foo"
        self.assertTrue(TestChecker.test(input, expect, 408))

    def test_checker9(self):
        input = """
        a: auto = a + 1;
        b: string = a::"InnerAnt";
        main: function void(){}
        """
        expect = "Type mismatch in expression: BinExpr(::, Id(a), StringLit(InnerAnt))"
        self.assertTrue(TestChecker.test(input, expect, 409))

    def test_checker10(self):
        input = """a: auto = "aaaaa";
        b: string = a::"InnerAnt";
        main: function void(){}
        """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 410))

    def test_checker11(self):
        input = """fun: function void(){}
        x: integer = fun();"""
        expect = "Type mismatch in expression: FuncCall(fun, [])"
        self.assertTrue(TestChecker.test(input, expect, 411))
    
    def test_checker12(self):
        input = """fun: function auto(a: integer){
            return a;
        }
        x: integer = fun();"""
        expect = "Type mismatch in expression: FuncCall(fun, [])"
        self.assertTrue(TestChecker.test(input, expect, 412))

    def test_checker13(self):
        input = """fun: function auto(a: integer){
            return a;
        }
        x: integer = fun(2, 4);"""
        expect = "Type mismatch in expression: FuncCall(fun, [IntegerLit(2), IntegerLit(4)])"
        self.assertTrue(TestChecker.test(input, expect, 413))

    def test_checker14(self):
        input = """fun: function auto(a: integer, b: integer){
            return a;
        }
        x: integer = fun(2, 4);"""
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input, expect, 414))

    def test_checker15(self):
        input = """fun: function auto(a: integer, b: float){return 1;}
        x: integer = fun(2, 4);
        main: function void(){}"""
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 415))
    
    def test_checker16(self):
        input = """
        main: function integer(){}"""
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input, expect, 416))

    def test_checker17(self):
        input = """x: auto = {2, 3, 4, {2}};
        main: function void(){}"""
        expect = "Illegal array literal: ArrayLit([IntegerLit(2), IntegerLit(3), IntegerLit(4), ArrayLit([IntegerLit(2)])])"
        self.assertTrue(TestChecker.test(input, expect, 417))

    def test_checker18(self):
        input = """j: array [4,2] of string = {{"a", "b"}, {"a", "b"}, {"a", "b"}, {"a", "b"}};"""
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input, expect, 418))

    def test_checker19(self):
        input = """j: array [4,2] of string = {{"a", "b"}, {"a"}, {"a", "b"}, {"a", "b"}};
        main: function void(){}"""
        expect = "Illegal array literal: ArrayLit([ArrayLit([StringLit(a), StringLit(b)]), ArrayLit([StringLit(a)]), ArrayLit([StringLit(a), StringLit(b)]), ArrayLit([StringLit(a), StringLit(b)])])"
        self.assertTrue(TestChecker.test(input, expect, 419))

    def test_checker20(self):
        input = """j: array [4,2] of string = {{"a", "b"}, {"a", true}, {"a", "b"}, {"a", "b"}};
        main: function void(){}"""
        expect = "Illegal array literal: ArrayLit([StringLit(a), BooleanLit(True)])"
        self.assertTrue(TestChecker.test(input, expect, 420))

    def test_checker21(self):
        input = """
        k: function auto(){
            return "string"
        }
        main:function void(){
            k();
            return;
        }
        """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 421))
    
    def test_checker22(self):
        input = """
        k: function auto() inherit m{
            
        }
        main:function void(){
            k();
            return;
        }
        m: function boolean(inherit a: string, inherit b: integer){}
        """
        expect = "Invalid statement in function: k"
        self.assertTrue(TestChecker.test(input, expect, 422))

    def test_checker23(self):
        input = """k: function auto() inherit m{
            super();
        }
        main:function void(){
            k();
            return;
        }
        m: function boolean(inherit a: string, inherit b: integer){}"""
        expect = "Type mismatch in expression: "
        self.assertTrue(TestChecker.test(input, expect, 423))

    def test_checker24(self):
        input = """k: function auto() inherit m{
            super("kkk", 333);
        }
        main:function void(){
            k();
            return;
        }
        m: function boolean(inherit a: string, inherit b: integer){}"""
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 424))

    def test_checker25(self):
        input = """k: function auto(a: integer) inherit m{
            super("kkk", 333);
        }
        main:function void(){
            k();
            return;
        }
        m: function boolean(inherit a: string, inherit b: integer){}"""
        expect = "Invalid Parameter: a"
        self.assertTrue(TestChecker.test(input, expect, 425))
    
    def test_checker26(self):
        input = """k: function auto(a: integer) inherit m{
            preventDefault();
            return a + 1;
        }
        main:function void(){
            k();
            return;
        }
        m: function boolean(inherit a: string, inherit b: integer){}"""
        expect = "Type mismatch in statement: CallStmt(k, )"
        self.assertTrue(TestChecker.test(input, expect, 426))

    def test_checker27(self):
        input = """
        k: function auto(a: integer, b: string) inherit m {
            preventDefault();
            return a + b;
        }

        main:function void(){
            k(1, "s");
            return;
        }
        m: function boolean(inherit a: string, inherit b: integer){}"""
        expect = "Type mismatch in expression: BinExpr(+, Id(a), Id(b))"
        self.assertTrue(TestChecker.test(input, expect, 427))

    def test_checker28(self):
        input = """k: function auto(c: integer, b: string) inherit m{
            super("s", 1);
            return -a;
        }
        main:function void(){
            k(22, "ssa");
            return;
        }
        m: function boolean(inherit a: string, inherit a: integer){}"""
        expect = "Redeclared Parameter: a"
        self.assertTrue(TestChecker.test(input, expect, 428))

    def test_checker29(self):
        input = """k: function auto(a: integer, b: string) inherit m{
            preventDefault();
            return b;
        }
        main:function void(){
            a: integer = k(1, "s");
            return;
        }
        m: function boolean(inherit a: string, inherit b: integer){}"""
        expect = "Type mismatch in Variable Declaration: VarDecl(a, IntegerType, FuncCall(k, [IntegerLit(1), StringLit(s)]))"
        self.assertTrue(TestChecker.test(input, expect, 429))

    def test_checker30(self):
        input = """k: function auto(c: integer, b: string) inherit m{
            super(b, c);
            return b;
        }
        main:function void(){
            a: auto = k(1, "d");
            return;
        }
        m: function boolean(inherit a: string, b: integer){}"""
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 430))

########################################################################### 

    def test_checker31(self):
        input = """
        jj: function string(a: integer, b: float){
            a: auto = {1,2,3};
            return "bingo";
        }
        main: function void(){

        }
        """
        expect = "Redeclared Identifier: a"
        self.assertTrue(TestChecker.test(input, expect, 431))
    
    def test_checker32(self):
        input = """
        jj: function string(a: integer, b: float){
            c: auto = {1,2,3};
            c[1,2] = 12 + 4.56e-3;
            return "bingo";
        }
        main: function void(){

        }
        """
        expect = "Type mismatch in expression: ArrayCell(c, [IntegerLit(1), IntegerLit(2)])"
        self.assertTrue(TestChecker.test(input, expect, 432))

    def test_checker33(self):
        input = """
        jj: function string(a: integer, b: float){
            c: auto = {{1,2},{5,2},{6,6}};
            c[1,2] = 12 + 4.56e-3;
            return "bingo";
        }
        main: function void(){

        }
        """
        expect = "Type mismatch in statement: AssignStmt(ArrayCell(c, [IntegerLit(1), IntegerLit(2)]), BinExpr(+, IntegerLit(12), FloatLit(0.00456)))"
        self.assertTrue(TestChecker.test(input, expect, 433))

    def test_checker34(self):
        input = """
        jj: function string(a: integer, b: float){
            c: array [3,2] of float = {{1,2},{5,2},{6,6}};
            c[1,2] = 12 + 4;
            return "bingo";
        }
        main: function void(){

        }
        """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 434))

    def test_checker35(self):
        input = """
        jj: function string(a: integer, b: float){
            c: auto = {{1,2},{5,2},{6,6}};
            c[1] = 12 + 4.56e-3;
            return "bingo";
        }
        main: function void(){

        }
        """
        expect = "Type mismatch in statement: AssignStmt(ArrayCell(c, [IntegerLit(1)]), BinExpr(+, IntegerLit(12), FloatLit(0.00456)))"
        self.assertTrue(TestChecker.test(input, expect, 435))
    
    def test_checker36(self):
        input = """
        jj: function string(a: auto, b: float){
            c: auto = {{1,2},{5,2},{6,6}};
            c[1,5] = 12 + a;
            foo();
            return "bingo";
        }
        main: function void(){

        }
        """
        expect = "Undeclared Function: foo"
        self.assertTrue(TestChecker.test(input, expect, 436))

    def test_checker37(self):
        input = """
        jj: function string(a: auto, b: float){
            c: auto = {{1,2},{5,2},{6,6}};
            c[1,5] = 12 + a;
            return "bingo";
        }
        main: function void(){
            jj(1, 4.66);
        }
        """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 437))

    def test_checker38(self):
        input = """
        jj: function string(a: auto, b: float) inherit foo{
            super("sss", b);
            c: auto = {{1,2},{5,2},{6,6}};
            c[1,5] = 12 + a;
            return "bingo";
        }
        main: function void(){
            jj(1, 4.66);
            foo("jksbjvd", 3.3333);
        }
        foo: function void(c: string, inherit d: auto){}
        """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 438))

    def test_checker39(self):
        input = """
        foo: function void(c: string, inherit d: auto){}
        jj: function string(a: auto, b: float) inherit foo{
            super("sss", b);
            c: auto = {{1,2},{5,2},{6,6}};
            c[1,5] = 12 + a;
            return "bingo";
        }
        main: function void(){
            jj(1, 4.66);
            foo("jksbjvd", 3.3333);
        }
        """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 439))

    def test_checker40(self): # problem
        input = """
        jj: function string(a: auto, b: float) inherit foo{
            super("sss", b);
            c: auto = {{1,2},{5,2},{6,6}};
            c[1,5] = 12 + a;
            d = "jjjjj";
            return "bingo";
        }
        main: function void(){
            jj(1, 4.66);
            a: boolean = foo("jksbjvd", 3.3333);
        }
        foo: function boolean(c: string, inherit d: auto){}
        """
        expect = "Type mismatch in statement: AssignStmt(Id(d), StringLit(jjjjj))"
        self.assertTrue(TestChecker.test(input, expect, 440))

#################################################################

    def test_checker41(self):
        input = """
        main: function void(){
            a: integer = 10;
            i: string;
            for(i = 0, i < a, i+1){
                break;
            }
            continue;
        }
        """
        expect = "Type mismatch in statement: AssignStmt(Id(i), IntegerLit(0))"
        self.assertTrue(TestChecker.test(input, expect, 441))
    
    def test_checker42(self):
        input = """
        main: function void(){
            a: integer = 10;
            i: integer;
            for(i = 0, i < a, i+1){
                break;
            }
            continue;
        }
        """
        expect = "Must in loop: ContinueStmt()"
        self.assertTrue(TestChecker.test(input, expect, 442))

    def test_checker43(self):
        input = """
        main: function void(){
            a: integer = 10;
            i: integer;
            for(i = 0, i < a, i+1){
                if (true){
                    break;
                }
            }
        }"""
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 443))

    def test_checker44(self):
        input = """
        main: function void(){
            a: integer = 10;
            i: integer;
            do{
                k:string;
                k = "SSSSSSSSS"::("erdsf"::"rrrrrrr");
                if(1==3.2) break;
            }while(1);
        }"""
        expect = "Type mismatch in expression: BinExpr(==, IntegerLit(1), FloatLit(3.2))"
        self.assertTrue(TestChecker.test(input, expect, 444))

    def test_checker45(self):
        input = """
        main: function void(){
            a: integer = 10;
            i: integer;
            if(i == 5){
                break;
            }
        }
        """
        expect = "Must in loop: BreakStmt()"
        self.assertTrue(TestChecker.test(input, expect, 445))
    
    def test_checker46(self):
        input = """
        main: function void(){
            a: integer = 10;
            i: integer;
            while(a == 34){
                continue;
            }
        }
        """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 446))

    def test_checker47(self):
        input = """
        main: function void(){
            a: integer = 10;
            i: integer;
            if(i == 5){
                while(a){
                    a = a - 1;
                    if(a == 3) break;
                }
            }
            else{
                continue;
            }
        }
        """
        expect = "Type mismatch in statement: WhileStmt(Id(a), BlockStmt([AssignStmt(Id(a), BinExpr(-, Id(a), IntegerLit(1))), IfStmt(BinExpr(==, Id(a), IntegerLit(3)), BreakStmt())]))"
        self.assertTrue(TestChecker.test(input, expect, 447))

    def test_checker48(self):
        input = """
        main: function void(){
            a: integer = 10;
            i: integer;
            if(i == 5){
                while(a <= 2){
                    a = a - 1;
                    if(a == 3) break;
                }
            }
            else{
                continue;
            }
        }
        """
        expect = "Must in loop: ContinueStmt()"
        self.assertTrue(TestChecker.test(input, expect, 448))

    def test_checker49(self):
        input = """
        main: function void(){
            a: integer = 10;
            i: integer;
            a();
        }
        """
        expect = "Undeclared Function: a"
        self.assertTrue(TestChecker.test(input, expect, 449))

    def test_checker50(self):
        input = """
        b: function integer(){}
        main: function void(){
            a: integer = 10;
            i: integer;
            i = b + 10;
        }
        """
        expect = "Undeclared Identifier: b"
        self.assertTrue(TestChecker.test(input, expect, 450))

    def test_checker51(self):
        input = """
        b: function integer(){}
        main: function void(){
            a: integer;
            readInteger();
        }
        """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 451))
    
    def test_checker52(self):
        input = """
        b: function integer(){}
        main: function void(){
            a: integer;
            readInteger();
            printInteger(a);
        }
        """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 452))

    def test_checker53(self):
        input = """ 
        b: function integer(){}
        main: function void(){
            a: integer;
            readInteger();
            printString(a);
        }"""
        expect = "Type mismatch in statement: CallStmt(printString, Id(a))"
        self.assertTrue(TestChecker.test(input, expect, 453))

    def test_checker54(self):
        input = """
        main: function void(){
            a: integer;
            readInteger();
            printFloat(a);
        }
        """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 454))

    def test_checker55(self):
        input = """x: array [1] of integer = {{1,2},{2,3}};"""
        expect = "Type mismatch in Variable Declaration: VarDecl(x, ArrayType([1], IntegerType), ArrayLit([ArrayLit([IntegerLit(1), IntegerLit(2)]), ArrayLit([IntegerLit(2), IntegerLit(3)])]))"
        self.assertTrue(TestChecker.test(input, expect, 455))
    
    def test_checker56(self):
        input = """x: auto = {{1,2},{2,3}};
        main: function void(){}"""
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 456))

    def test_checker57(self):
        input = """x: auto = {{foo(),2},{2,3}};
        main: function void(){}
        foo: function integer(){}"""
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 457))

    def test_checker58(self):
        input = """x: auto = {{foo(),2},{2,3}};
        main: function void(){}
        foo: function auto(){}"""
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 458))

    def test_checker59(self):
        input = """x: auto = {{foo(),2},{"String","String"}};
        main: function void(){}
        foo: function auto(){}"""
        expect = "Illegal array literal: ArrayLit([ArrayLit([FuncCall(foo, []), IntegerLit(2)]), ArrayLit([StringLit(String), StringLit(String)])])"
        self.assertTrue(TestChecker.test(input, expect, 459))

    def test_checker60(self):
        input = """
        j:function auto(){return 33;}
        l:function float(){}
        x: float = k() + j() + l();
        main: function void(){}
        k:function integer(){}"""
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 460))

    def test_checker61(self):
        input = """x, f, jj: integer = 1, 2, 3;"""
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input, expect, 461))
    
    def test_checker62(self):
        input = """
        x: float;
        a: auto = x < 10"""
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input, expect, 462))

    def test_checker63(self):
        input = """x: float;
        a: auto = x < 10
        koo: function boolean(a: boolean){}
        main:function void(){
            if(a == koo(a)){
                printBoolean(a);
            }

        }"""
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 463))

    def test_checker64(self):
        input = """x: float;
        a: auto = x < 10
        koo: function boolean(a: boolean){}
        main:function void(){
            if(a == koo(a)){

                {
                    a: integer = 234;
                    printInteger(a);
                }
            }

        }"""
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 464))

    def test_checker65(self):
        input = """x: integer;
        main: function void(){
            x: float;
            {
                x: string;
                {
                    x: boolean;
                    {
                        a: boolean = x;
                    }
                }
            }
        }"""
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 465))
    
    def test_checker66(self):
        input = """
        main: function void(){
            c: array [2,3] of boolean;
            if(c[2,"string"]){
                printBoolean(c[1,2]);
            }
        }"""
        expect = "Type mismatch in expression: ArrayCell(c, [IntegerLit(2), StringLit(string)])"
        self.assertTrue(TestChecker.test(input, expect, 466))

    def test_checker67(self):
        input = """
        main: function void(){
            c:boolean;
            if(c[2,3]){
                printBoolean(c[1,2]);
            }
        }
        """
        expect = "Type mismatch in expression: ArrayCell(c, [IntegerLit(2), IntegerLit(3)])"
        self.assertTrue(TestChecker.test(input, expect, 467))

    def test_checker68(self):
        input = """b: auto = (2 >= 3) && (4 % 7);
        main: function void(){}"""
        expect = "Type mismatch in expression: BinExpr(&&, BinExpr(>=, IntegerLit(2), IntegerLit(3)), BinExpr(%, IntegerLit(4), IntegerLit(7)))"
        self.assertTrue(TestChecker.test(input, expect, 468))

    def test_checker69(self):
        input = """b: auto = (2 >= 3) && (4 != 7);
        main: function void(){}"""
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 469))

    def test_checker70(self):
        input = """x: integer;
        main: function void(){
            if ((x == 3) || (x == 5) || (x == -10)){
                printInteger(x);
            }
        }"""
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 470))

    def test_checker71(self):
        input = """
        x: integer;
        main: function void(){
            while(x < 10){
                i: boolean;
                for(i = 0, i < x, i + 1){
                    break;
                }
            }
        }
        """
        expect = "Type mismatch in statement: AssignStmt(Id(i), IntegerLit(0))"
        self.assertTrue(TestChecker.test(input, expect, 471))
    
    def test_checker72(self):
        input = """x: integer;
        main: function void(){
            while(x < 10){
                i: integer;
                for(i = 0, i % x, i + 1){
                    x = 23 + i;
                }
            }
        }"""
        expect = "Type mismatch in statement: ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(%, Id(i), Id(x)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([AssignStmt(Id(x), BinExpr(+, IntegerLit(23), Id(i)))]))"
        self.assertTrue(TestChecker.test(input, expect, 472))

    def test_checker73(self):
        input = """x: integer;
        main: function void(){
            while(x < 10){
                i: integer;
                for(i = 0, i <= x, fin(i)){
                    x = 23 + i;
                }
            }
        }
        fin:function boolean(a: integer){}
        """
        expect = "Type mismatch in statement: ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<=, Id(i), Id(x)), FuncCall(fin, [Id(i)]), BlockStmt([AssignStmt(Id(x), BinExpr(+, IntegerLit(23), Id(i)))]))"
        self.assertTrue(TestChecker.test(input, expect, 473))

    def test_checker74(self):
        input = """x: integer;
        main: function void(){
            while(x < 10){
                i: integer;
                for(i = 0, i <= x, fin(i)){
                    x = 23 + i;
                }
            }
        }
        fin:function auto(a: integer){}"""
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 474))

    def test_checker75(self):
        input = """x: integer;
        fin:function void(a: integer){}
        main: function void(){
            while(x < 10){
                i: integer;
                for(i = 0, i <= x, i + 1){
                    fin = 23 + i;
                }
            }
        }"""
        expect = "Undeclared Identifier: fin"
        self.assertTrue(TestChecker.test(input, expect, 475))
    
    def test_checker76(self):
        input = """x: array [22] of integer;
        fin:array [12] of integer;
        main: function void(){
            while(x < 10){
                i: integer;
                for(i = 0, i <= x, i + 1){
                    fin = x;
                }
            }
        }"""
        expect = "Type mismatch in expression: BinExpr(<, Id(x), IntegerLit(10))"
        self.assertTrue(TestChecker.test(input, expect, 476))

    def test_checker77(self):
        input = """k: array [22] of integer;
        x: integer;
        fin:array [12] of integer;
        main: function void(){
            while(x < 10){
                i: integer;
                for(i = 0, i <= x, i + 1){
                    fin = k;
                }
            }
        }"""
        expect = "Type mismatch in statement: AssignStmt(Id(fin), Id(k))"
        self.assertTrue(TestChecker.test(input, expect, 477))

    def test_checker78(self):
        input = """main: function void() {
                        a: auto = {1, 2};
                        a[f1(1,2,3)] = 2;
                        x: string = true;
                }
                f1: function auto(x: float, y: float, z: float) {
                        return x + y + z;
                }
                """
        expect = "Type mismatch in Variable Declaration: VarDecl(x, StringType, BooleanLit(True))"
        self.assertTrue(TestChecker.test(input, expect, 478))

    def test_checker79(self):
        input = """main: function void() {
                        a: auto = {1 + 33, 2};
                        a[f1(5,5,5)] = 2;
                        x: string = "ssssss";
                }
                f1: function auto(x: float, y: float, z: float) {
                        return x + y + z;
                }"""
        expect = "Type mismatch in statement: ReturnStmt(BinExpr(+, BinExpr(+, Id(x), Id(y)), Id(z)))"
        self.assertTrue(TestChecker.test(input, expect, 479))

    def test_checker80(self):
        input = """main: function void() {
                        a: auto = {1 + 33, 2};
                        a[f4(5,5,5)] = 2;
                        x: string = "ssssss";
                }
                f4: function float(x: float, y: float, z: float) {
                        return x + y + z;
                }"""
        expect = "Type mismatch in expression: ArrayCell(a, [FuncCall(f4, [IntegerLit(5), IntegerLit(5), IntegerLit(5)])])"
        self.assertTrue(TestChecker.test(input, expect, 480))

    def test_checker81(self):
        input = """
        dl:function auto(a:auto, b:integer){
            return a + b;
            return "fkjsnfvkjs";
        }
        main:function void(){}
        """
        expect = "Type mismatch in statement: ReturnStmt(StringLit(fkjsnfvkjs))"
        self.assertTrue(TestChecker.test(input, expect, 481))
    
    def test_checker82(self):
        input = """
        dl:function auto(a:auto, b:integer){
            return a + b;
            if (a == 3){
                return b;
            }
            else{
                return false;
            }
        }
        main: function void(){}"""
        expect = "Type mismatch in statement: ReturnStmt(BooleanLit(False))"
        self.assertTrue(TestChecker.test(input, expect, 482))

    def test_checker83(self):
        input = """
        dl:function auto(a:auto, b:integer){
            return a + b;
            if (a == 3){
                return b;
            }
            else{
                return a;
            }
        }
        main: function void(){}
        """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 483))

    def test_checker84(self):
        input = """s: auto;"""
        expect = "Invalid Variable: s"
        self.assertTrue(TestChecker.test(input, expect, 484))

    def test_checker85(self):
        input = """s: array [1,2,3] of boolean = {{true,false},{false,false}};"""
        expect = "Type mismatch in Variable Declaration: VarDecl(s, ArrayType([1, 2, 3], BooleanType), ArrayLit([ArrayLit([BooleanLit(True), BooleanLit(False)]), ArrayLit([BooleanLit(False), BooleanLit(False)])]))"
        self.assertTrue(TestChecker.test(input, expect, 485))

    def test_checker86(self):
        input = """s: array [1,2] of boolean = {{true,false}};
        main: function void(){}"""
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 486))

    def test_checker87(self):
        input = """s: array [1,2] of boolean = {{false,false}};"""
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input, expect, 487))

    def test_checker88(self):
        input = """s: array [2,2] of boolean = {{true,false},{2.0,false}};"""
        expect = "Illegal array literal: ArrayLit([FloatLit(2.0), BooleanLit(False)])"
        self.assertTrue(TestChecker.test(input, expect, 488))

    def test_checker89(self):
        input = """
        g: function integer() inherit f{}
        main: function void(){}"""
        expect = "Undeclared Function: f"
        self.assertTrue(TestChecker.test(input, expect, 489))

    def test_checker90(self):
        input = """
        f: function float(){}
        g: function integer() inherit f{}
        main: function void(){}"""
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 490))

    def test_checker91(self):
        input = """
        gin: function auto(inherit k: integer, inherit c: string){}
        hin: function auto(inherit b: float){
            super(1, "fksnl");
        }
        lin:function integer(k: boolean){
            super(true);
        }
        """
        expect = "Invalid statement in function: hin"
        self.assertTrue(TestChecker.test(input, expect, 491))
    
    def test_checker92(self):
        input = """
        gin: function auto(inherit k: integer, inherit c: string) {}

        hin: function auto(inherit b: float) inherit gin {
            super(1, "fksnl");
        }

        lin:function integer(k: boolean) {
            super(2.5);
        }
        """
        expect = "Invalid statement in function: lin"
        self.assertTrue(TestChecker.test(input, expect, 492))

    def test_checker93(self):
        input = """
        gin: function auto(inherit k: integer, inherit c: string){}
        hin: function auto(inherit b: float) inherit gin{
            super(1, "fksnl");
        }
        lin:function integer(k: boolean) inherit hin{
            super(2.5);
        }
        """
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input, expect, 493))

    def test_checker94(self):
        input = """gin: function auto(inherit k: integer, inherit c: string){}
        hin: function auto(inherit b: float) inherit gin{
            super(1, "fksnl");
        }
        lin:function integer(b: boolean) inherit hin{
            super(2.5);
        }"""
        expect = "Invalid Parameter: b"
        self.assertTrue(TestChecker.test(input, expect, 494))

    def test_checker95(self):
        input = """gin: function auto(inherit k: integer, inherit c: string){}
        hin: function auto(inherit b: float) inherit lin{
            super(true, 3);
        }
        lin:function integer(k: boolean, k: integer){
        }"""
        expect = "Redeclared Parameter: k"
        self.assertTrue(TestChecker.test(input, expect, 495))
    
    def test_checker96(self):
        input = """gin: function auto(inherit k: integer, inherit c: string){}
        hin: function auto(inherit b: float) inherit lin{
            super(true, 3);
        }
        lin:function integer(k: boolean, d: integer){
        }"""
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input, expect, 496))

    def test_checker97(self):
        input = """
        c: auto = 122e-2 + 23;
        d: float = c;"""
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input, expect, 497))

    def test_checker98(self):
        input = """
        c: auto = 122e-2 + 23;
        d: integer = c;
        """
        expect = "Type mismatch in Variable Declaration: VarDecl(d, IntegerType, Id(c))"
        self.assertTrue(TestChecker.test(input, expect, 498))

    def test_checker99(self):
        input = """
        gin: function auto(inherit k: integer, inherit c: string){}
        hin: function auto(inherit b: auto) inherit lin{
            super(true, 3);
            b = "nljdvnal";
            return b
        }
        lin:function integer(k: boolean, d: integer){
        }
        """
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input, expect, 499))

    def test_checke100(self):
        input = """
        fin: function integer(a: integer, b: float, c: auto){}
        d: array [3] of integer = {fin(23, 3.3, foo()), 3, 6};
        foo:function string(){}
        main: function void(){}"""
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 500))

