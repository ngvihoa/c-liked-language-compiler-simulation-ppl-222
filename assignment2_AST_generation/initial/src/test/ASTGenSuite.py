import unittest
from TestUtils import TestAST
from AST import *


class ASTGenSuite(unittest.TestCase):
    def test_short_vardecl(self):
        input = """x:integer;
        """
        expect = str(Program([VarDecl("x", IntegerType())]))
        self.assertTrue(TestAST.test(input, expect, 300))

    def test_full_vardecl(self):
        input = """x, y, z: integer = 1, 2, 3;"""
        expect = """Program([
	VarDecl(x, IntegerType, IntegerLit(1))
	VarDecl(y, IntegerType, IntegerLit(2))
	VarDecl(z, IntegerType, IntegerLit(3))
])"""
        self.assertTrue(TestAST.test(input, expect, 301))

    def test_vardecls(self):
        input = """x, y, z: integer = 1, 2, 3;
        a, b: float;"""
        expect = """Program([
	VarDecl(x, IntegerType, IntegerLit(1))
	VarDecl(y, IntegerType, IntegerLit(2))
	VarDecl(z, IntegerType, IntegerLit(3))
	VarDecl(a, FloatType)
	VarDecl(b, FloatType)
])"""
        self.assertTrue(TestAST.test(input, expect, 302))

    def test_simple_program(self):
        """Simple program"""
        input = """simpleFunc: function void () {
        }"""
        expect = """Program([
	FuncDecl(simpleFunc, VoidType, [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 303))

    def test_more_complex_program(self):
        """More complex program"""
        input = """simpleFunc: function void () {
            printInteger(4);
        }"""
        expect = """Program([
	FuncDecl(simpleFunc, VoidType, [], None, BlockStmt([CallStmt(printInteger, IntegerLit(4))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 304))

####################################################################################################

    def test_more_complex_program1(self):
        """More complex program"""
        input = """a: string  = "aaaaaaa";
b: integer = 2834;
c: auto = 2-3-3;"""
        expect = """Program([
	VarDecl(a, StringType, StringLit(aaaaaaa))
	VarDecl(b, IntegerType, IntegerLit(2834))
	VarDecl(c, AutoType, BinExpr(-, BinExpr(-, IntegerLit(2), IntegerLit(3)), IntegerLit(3)))
])"""
        self.assertTrue(TestAST.test(input, expect, 305))

    def test_more_complex_program2(self):
        """More complex program"""
        input = """simpleFunc: function void () {
            n: integer = 5;
            for(i = 0, i < n, i + 1){
                printOut(i);
            }
        }"""
        expect = """Program([
	FuncDecl(simpleFunc, VoidType, [], None, BlockStmt([VarDecl(n, IntegerType, IntegerLit(5)), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), Id(n)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([CallStmt(printOut, Id(i))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 306))

    def test_more_complex_program3(self):
        """More complex program"""
        input = """pi: float = 3.14;
        simpleFunc: function void () {
            tmp: float = pi * 2 * 5;
            printInteger(tmp);
            return;
        }"""
        expect = """Program([
	VarDecl(pi, FloatType, FloatLit(3.14))
	FuncDecl(simpleFunc, VoidType, [], None, BlockStmt([VarDecl(tmp, FloatType, BinExpr(*, BinExpr(*, Id(pi), IntegerLit(2)), IntegerLit(5))), CallStmt(printInteger, Id(tmp)), ReturnStmt()]))
])"""
        self.assertTrue(TestAST.test(input, expect, 307))

    def test_more_complex_program4(self):
        """More complex program"""
        input = """simpleFunc: function void () {
            n:integer = 12;
            for(i = 1, i <= n, i+1){
                if(i % 2 == 0){
                    printout(i);
                }
            }
            return;
        }"""
        expect = """Program([
	FuncDecl(simpleFunc, VoidType, [], None, BlockStmt([VarDecl(n, IntegerType, IntegerLit(12)), ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<=, Id(i), Id(n)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(==, BinExpr(%, Id(i), IntegerLit(2)), IntegerLit(0)), BlockStmt([CallStmt(printout, Id(i))]))])), ReturnStmt()]))
])"""
        self.assertTrue(TestAST.test(input, expect, 308))

    def test_more_complex_program5(self):
        """More complex program"""
        input = """simpleFunc: function void () {
            a,b:string = "Cindy", "Adam";
            printout(a, b);
            c:string;
            c = a;
            a = b;
            b = c;
            printout(a, b);
        }"""
        expect = """Program([
	FuncDecl(simpleFunc, VoidType, [], None, BlockStmt([VarDecl(a, StringType, StringLit(Cindy)), VarDecl(b, StringType, StringLit(Adam)), CallStmt(printout, Id(a), Id(b)), VarDecl(c, StringType), AssignStmt(Id(c), Id(a)), AssignStmt(Id(a), Id(b)), AssignStmt(Id(b), Id(c)), CallStmt(printout, Id(a), Id(b))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 309))

    def test_more_complex_program6(self):
        """More complex program"""
        input = """
        isEven: function boolean(n: integer){
            if(n%2==0){
                return true;
            }
            return false;
        }
        simpleFunc: function void () {
            n:integer = 7;
            printout(isEven(n));
        }"""
        expect = """Program([
	FuncDecl(isEven, BooleanType, [Param(n, IntegerType)], None, BlockStmt([IfStmt(BinExpr(==, BinExpr(%, Id(n), IntegerLit(2)), IntegerLit(0)), BlockStmt([ReturnStmt(BooleanLit(True))])), ReturnStmt(BooleanLit(False))]))
	FuncDecl(simpleFunc, VoidType, [], None, BlockStmt([VarDecl(n, IntegerType, IntegerLit(7)), CallStmt(printout, FuncCall(isEven, [Id(n)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 310))

    def test_more_complex_program7(self):
        """More complex program"""
        input = """
        factor: function integer(n: integer){
            if(n == 1) return 1;
            return n * factor(n-1);
        }
        simpleFunc: function void () {
            printout(factor(3));
        }"""
        expect = """Program([
	FuncDecl(factor, IntegerType, [Param(n, IntegerType)], None, BlockStmt([IfStmt(BinExpr(==, Id(n), IntegerLit(1)), ReturnStmt(IntegerLit(1))), ReturnStmt(BinExpr(*, Id(n), FuncCall(factor, [BinExpr(-, Id(n), IntegerLit(1))])))]))
	FuncDecl(simpleFunc, VoidType, [], None, BlockStmt([CallStmt(printout, FuncCall(factor, [IntegerLit(3)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 311))

    def test_more_complex_program8(self):
        """More complex program"""
        input = """simpleFunc: function void () {
            arr: array [3] of integer;
            arr = {2,4,8};
        }"""
        expect = """Program([
	FuncDecl(simpleFunc, VoidType, [], None, BlockStmt([VarDecl(arr, ArrayType([3], IntegerType)), AssignStmt(Id(arr), ArrayLit([IntegerLit(2), IntegerLit(4), IntegerLit(8)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 312))

    def test_more_complex_program9(self):
        """More complex program"""
        input = """simpleFunc: function void () {
            tmp = "1234"::"I love u";
            print(tmp);
        }"""
        expect = """Program([
	FuncDecl(simpleFunc, VoidType, [], None, BlockStmt([AssignStmt(Id(tmp), BinExpr(::, StringLit(1234), StringLit(I love u))), CallStmt(print, Id(tmp))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 313))

    def test_more_complex_program10(self):
        """More complex program"""
        input = """
        sort: function array [10] of integer(out n: array [10] of integer){
            sort(n);
            return n;
        }
        simpleFunc: function void () {
            printout({1,5,2,8,5,0,6,3,9,7});
        }"""
        expect = """Program([
	FuncDecl(sort, ArrayType([10], IntegerType), [OutParam(n, ArrayType([10], IntegerType))], None, BlockStmt([CallStmt(sort, Id(n)), ReturnStmt(Id(n))]))
	FuncDecl(simpleFunc, VoidType, [], None, BlockStmt([CallStmt(printout, ArrayLit([IntegerLit(1), IntegerLit(5), IntegerLit(2), IntegerLit(8), IntegerLit(5), IntegerLit(0), IntegerLit(6), IntegerLit(3), IntegerLit(9), IntegerLit(7)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 314))

    def test_more_complex_program11(self):
        """More complex program"""
        input = """
        b, c, d, e: boolean = true, false, false, true;
        simpleFunc: function void () {
        }"""
        expect = """Program([
	VarDecl(b, BooleanType, BooleanLit(True))
	VarDecl(c, BooleanType, BooleanLit(False))
	VarDecl(d, BooleanType, BooleanLit(False))
	VarDecl(e, BooleanType, BooleanLit(True))
	FuncDecl(simpleFunc, VoidType, [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 315))

    def test_more_complex_program12(self):
        """More complex program"""
        input = """simpleFunc: function void () {
            e,f,g:auto = 3, 5.6, "intint";
        }"""
        expect = """Program([
	FuncDecl(simpleFunc, VoidType, [], None, BlockStmt([VarDecl(e, AutoType, IntegerLit(3)), VarDecl(f, AutoType, FloatLit(5.6)), VarDecl(g, AutoType, StringLit(intint))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 316))

    def test_more_complex_program13(self):
        """More complex program"""
        input = """
        f1: function auto(inherit out n: integer){
            return 3;
        }
        simpleFunc: function void () {
            
        }"""
        expect = """Program([
	FuncDecl(f1, AutoType, [InheritOutParam(n, IntegerType)], None, BlockStmt([ReturnStmt(IntegerLit(3))]))
	FuncDecl(simpleFunc, VoidType, [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 317))

    def test_more_complex_program14(self):
        """More complex program"""
        input = """simpleFunc: function void () {
            for(i = 0, i < n, i+1){
                for(j = i+1, j < n, j+1){
                    if(i < j) swap(i,j);
                }
                continue;
            }
        }"""
        expect = """Program([
	FuncDecl(simpleFunc, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), Id(n)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([ForStmt(AssignStmt(Id(j), BinExpr(+, Id(i), IntegerLit(1))), BinExpr(<, Id(j), Id(n)), BinExpr(+, Id(j), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(<, Id(i), Id(j)), CallStmt(swap, Id(i), Id(j)))])), ContinueStmt()]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 318))

    def test_more_complex_program15(self):
        """More complex program"""
        input = """simpleFunc: function void () {
            while(true){
                print(i);
                i=i+1;
                if(i==100)
                    break;
            }
        }"""
        expect = """Program([
	FuncDecl(simpleFunc, VoidType, [], None, BlockStmt([WhileStmt(BooleanLit(True), BlockStmt([CallStmt(print, Id(i)), AssignStmt(Id(i), BinExpr(+, Id(i), IntegerLit(1))), IfStmt(BinExpr(==, Id(i), IntegerLit(100)), BreakStmt())]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 319))

    def test_more_complex_program16(self):
        """More complex program"""
        input = """simpleFunc: function void () {
            n[12] = "2345 I love cake";
        }"""
        expect = """Program([
	FuncDecl(simpleFunc, VoidType, [], None, BlockStmt([AssignStmt(ArrayCell(n, [IntegerLit(12)]), StringLit(2345 I love cake))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 320))

    def test_more_complex_program17(self):
        """More complex program"""
        input = """simpleFunc: function void () {
            {
                a = "something";
            }
        }"""
        expect = """Program([
	FuncDecl(simpleFunc, VoidType, [], None, BlockStmt([BlockStmt([AssignStmt(Id(a), StringLit(something))])]))
])"""
        self.assertTrue(TestAST.test(input, expect, 321))

    def test_more_complex_program18(self):
        """More complex program"""
        input = """simpleFunc: function void () {
            if(1){
                print(true);
            }
            else {
                if(3){
                    print(false);
                }
                else print("hhhhh");
            }
        }"""
        expect = """Program([
	FuncDecl(simpleFunc, VoidType, [], None, BlockStmt([IfStmt(IntegerLit(1), BlockStmt([CallStmt(print, BooleanLit(True))]), BlockStmt([IfStmt(IntegerLit(3), BlockStmt([CallStmt(print, BooleanLit(False))]), CallStmt(print, StringLit(hhhhh)))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 322))

    def test_more_complex_program19(self):
        """More complex program"""
        input = """simpleFunc: function void () {
            do{
                printout("Do something fun");
            }while(a==1);
        }"""
        expect = """Program([
	FuncDecl(simpleFunc, VoidType, [], None, BlockStmt([DoWhileStmt(BinExpr(==, Id(a), IntegerLit(1)), BlockStmt([CallStmt(printout, StringLit(Do something fun))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 323))

    def test_more_complex_program20(self):
        """More complex program"""
        input = """simpleFunc: function void () {
            n : integer = (2+3+4*5/7-2)/2;
        }"""
        expect = """Program([
	FuncDecl(simpleFunc, VoidType, [], None, BlockStmt([VarDecl(n, IntegerType, BinExpr(/, BinExpr(-, BinExpr(+, BinExpr(+, IntegerLit(2), IntegerLit(3)), BinExpr(/, BinExpr(*, IntegerLit(4), IntegerLit(5)), IntegerLit(7))), IntegerLit(2)), IntegerLit(2)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 324))

    def test_more_complex_program21(self):
        """More complex program"""
        input = """simpleFunc: function void () {
            a[1,2,4] = tmp :: tmp2;
        }"""
        expect = """Program([
	FuncDecl(simpleFunc, VoidType, [], None, BlockStmt([AssignStmt(ArrayCell(a, [IntegerLit(1), IntegerLit(2), IntegerLit(4)]), BinExpr(::, Id(tmp), Id(tmp2)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 325))

    def test_more_complex_program22(self):
        """More complex program"""
        input = """simpleFunc: function void () {
            a,b,c: float = d,e,(21==2);
        }"""
        expect = """Program([
	FuncDecl(simpleFunc, VoidType, [], None, BlockStmt([VarDecl(a, FloatType, Id(d)), VarDecl(b, FloatType, Id(e)), VarDecl(c, FloatType, BinExpr(==, IntegerLit(21), IntegerLit(2)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 326))

    def test_more_complex_program23(self):
        """More complex program"""
        input = """simpleFunc: function void () {
            if (!isEven(3)){
                i = i - (2+3);
            }
            else{
                while(n){
                    print(n);
                    n = n - 1;
                    if (n == 10) break;
                }
            }
        }"""
        expect = """Program([
	FuncDecl(simpleFunc, VoidType, [], None, BlockStmt([IfStmt(UnExpr(!, FuncCall(isEven, [IntegerLit(3)])), BlockStmt([AssignStmt(Id(i), BinExpr(-, Id(i), BinExpr(+, IntegerLit(2), IntegerLit(3))))]), BlockStmt([WhileStmt(Id(n), BlockStmt([CallStmt(print, Id(n)), AssignStmt(Id(n), BinExpr(-, Id(n), IntegerLit(1))), IfStmt(BinExpr(==, Id(n), IntegerLit(10)), BreakStmt())]))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 327))

    def test_more_complex_program24(self):
        """More complex program"""
        input = """
        intern: function float(a:integer, b:float) inherit ite{
            return a*b+5;
        }
        simpleFunc: function void () {
            intern(a, b);
        }"""
        expect = """Program([
	FuncDecl(intern, FloatType, [Param(a, IntegerType), Param(b, FloatType)], ite, BlockStmt([ReturnStmt(BinExpr(+, BinExpr(*, Id(a), Id(b)), IntegerLit(5)))]))
	FuncDecl(simpleFunc, VoidType, [], None, BlockStmt([CallStmt(intern, Id(a), Id(b))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 328))

    def test_more_complex_program25(self):
        """More complex program"""
        input = """
        print: function void (a:string) {
            return a::"String";
        }
        cal: function boolean (isT: boolean) {
            return !isT;
        }
        simpleFunc: function void () {
            print("Automata");
            cal(true);
        }"""
        expect = """Program([
	FuncDecl(print, VoidType, [Param(a, StringType)], None, BlockStmt([ReturnStmt(BinExpr(::, Id(a), StringLit(String)))]))
	FuncDecl(cal, BooleanType, [Param(isT, BooleanType)], None, BlockStmt([ReturnStmt(UnExpr(!, Id(isT)))]))
	FuncDecl(simpleFunc, VoidType, [], None, BlockStmt([CallStmt(print, StringLit(Automata)), CallStmt(cal, BooleanLit(True))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 329))

    def test_more_complex_program26(self):
        """More complex program"""
        input = """simpleFunc: function void () {
            m = a[1];
        }"""
        expect = """Program([
	FuncDecl(simpleFunc, VoidType, [], None, BlockStmt([AssignStmt(Id(m), ArrayCell(a, [IntegerLit(1)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 330))

    def test_more_complex_program27(self):
        """More complex program"""
        input = """f, h, s: string = "Baby Shark", "LOving you \\n", "nonstop \\t music"; 
        """
        expect = """Program([
	VarDecl(f, StringType, StringLit(Baby Shark))
	VarDecl(h, StringType, StringLit(LOving you \\n))
	VarDecl(s, StringType, StringLit(nonstop \\t music))
])"""
        self.assertTrue(TestAST.test(input, expect, 331))

    def test_more_complex_program28(self):
        """More complex program"""
        input = """t, x: float = 1_2020.0e4, 36_4.002;"""
        expect = """Program([
	VarDecl(t, FloatType, FloatLit(120200000.0))
	VarDecl(x, FloatType, FloatLit(364.002))
])"""
        self.assertTrue(TestAST.test(input, expect, 332))

    def test_more_complex_program29(self):
        """More complex program"""
        input = """t, x: float = 3_7720.3E+444, 0.022;"""
        expect = """Program([
	VarDecl(t, FloatType, FloatLit(inf))
	VarDecl(x, FloatType, FloatLit(0.022))
])"""
        self.assertTrue(TestAST.test(input, expect, 333))

    def test_more_complex_program30(self):
        """More complex program"""
        input = """simpleFunc: function void () {
            if ( a+b >= 3 || (tymp == "Superman")) {
                a =b;
                c = b;
            }
            else print();
        }"""
        expect = """Program([
	FuncDecl(simpleFunc, VoidType, [], None, BlockStmt([IfStmt(BinExpr(>=, BinExpr(+, Id(a), Id(b)), BinExpr(||, IntegerLit(3), BinExpr(==, Id(tymp), StringLit(Superman)))), BlockStmt([AssignStmt(Id(a), Id(b)), AssignStmt(Id(c), Id(b))]), CallStmt(print, ))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 334))

    def test_more_complex_program31(self):
        """More complex program"""
        input = """simpleFunc: function void () {
            a: boolean = true || a < 3;
        }"""
        expect = """Program([
	FuncDecl(simpleFunc, VoidType, [], None, BlockStmt([VarDecl(a, BooleanType, BinExpr(<, BinExpr(||, BooleanLit(True), Id(a)), IntegerLit(3)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 335))

    def test_more_complex_program32(self):
        """More complex program"""
        input = """simpleFunc: function void () {
            a: integer = b + fact(50) * 1204;
            b : boolean = c || (50 == 3) && 23;
        }"""
        expect = """Program([
	FuncDecl(simpleFunc, VoidType, [], None, BlockStmt([VarDecl(a, IntegerType, BinExpr(+, Id(b), BinExpr(*, FuncCall(fact, [IntegerLit(50)]), IntegerLit(1204)))), VarDecl(b, BooleanType, BinExpr(&&, BinExpr(||, Id(c), BinExpr(==, IntegerLit(50), IntegerLit(3))), IntegerLit(23)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 336))

    def test_more_complex_program33(self):
        """More complex program"""
        input = """simpleFunc: function void () {
            // Something u cant see
            for(a[3] = b(jdbao), a[3] > 4, a[3]+1){

            }
        }"""
        expect = """Program([
	FuncDecl(simpleFunc, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(ArrayCell(a, [IntegerLit(3)]), FuncCall(b, [Id(jdbao)])), BinExpr(>, ArrayCell(a, [IntegerLit(3)]), IntegerLit(4)), BinExpr(+, ArrayCell(a, [IntegerLit(3)]), IntegerLit(1)), BlockStmt([]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 337))

    def test_more_complex_program34(self):
        """More complex program"""
        input = """simpleFunc: function void () {
            do {print(c); }while(c>5);
        }"""
        expect = """Program([
	FuncDecl(simpleFunc, VoidType, [], None, BlockStmt([DoWhileStmt(BinExpr(>, Id(c), IntegerLit(5)), BlockStmt([CallStmt(print, Id(c))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 338))

    def test_more_complex_program35(self):
        """More complex program"""
        input = """
        a: array [2,3] of string = {{"a", "b", "c"}, {"d", "e", "f"}};
        simpleFunc: function void () {
            print(a);
        }"""
        expect = """Program([
	VarDecl(a, ArrayType([2, 3], StringType), ArrayLit([ArrayLit([StringLit(a), StringLit(b), StringLit(c)]), ArrayLit([StringLit(d), StringLit(e), StringLit(f)])]))
	FuncDecl(simpleFunc, VoidType, [], None, BlockStmt([CallStmt(print, Id(a))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 339))

    def test_more_complex_program36(self):
        """More complex program"""
        input = """simpleFunc: function void () {
            do{
                do{
                    do{
                        b = c
                    }while(a == 1);
                }while(call());
            }while(a==b);
        }"""
        expect = """Program([
	FuncDecl(simpleFunc, VoidType, [], None, BlockStmt([DoWhileStmt(BinExpr(==, Id(a), Id(b)), BlockStmt([DoWhileStmt(FuncCall(call, []), BlockStmt([DoWhileStmt(BinExpr(==, Id(a), IntegerLit(1)), BlockStmt([AssignStmt(Id(b), Id(c))]))]))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 340))

    def test_more_complex_program37(self):
        """More complex program"""
        input = """simpleFunc: function void () {
            a:array [10] of integer;
            m: integer = 0;
            for(i = 1, i < n * 2, i * 3){
                a[m] = i;
                m = m + 1;
            }
            return;
        }"""
        expect = """Program([
	FuncDecl(simpleFunc, VoidType, [], None, BlockStmt([VarDecl(a, ArrayType([10], IntegerType)), VarDecl(m, IntegerType, IntegerLit(0)), ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<, Id(i), BinExpr(*, Id(n), IntegerLit(2))), BinExpr(*, Id(i), IntegerLit(3)), BlockStmt([AssignStmt(ArrayCell(a, [Id(m)]), Id(i)), AssignStmt(Id(m), BinExpr(+, Id(m), IntegerLit(1)))])), ReturnStmt()]))
])"""
        self.assertTrue(TestAST.test(input, expect, 341))

    def test_more_complex_program38(self):
        """More complex program"""
        input = """simpleFunc: function void () {
            m: array [3] of float = {1.111E-23, .002E24, 2.0e4};
            n: array [2] of float = {23.5, 77.7};
            m = m + n;
            printArray(m);
        }"""
        expect = """Program([
	FuncDecl(simpleFunc, VoidType, [], None, BlockStmt([VarDecl(m, ArrayType([3], FloatType), ArrayLit([FloatLit(1.111e-23), FloatLit(2e+21), FloatLit(20000.0)])), VarDecl(n, ArrayType([2], FloatType), ArrayLit([FloatLit(23.5), FloatLit(77.7)])), AssignStmt(Id(m), BinExpr(+, Id(m), Id(n))), CallStmt(printArray, Id(m))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 342))

    def test_more_complex_program39(self):
        """More complex program"""
        input = """simpleFunc: function void () {
            printString(tmp::(tmp1::tmp2));
        }"""
        expect = """Program([
	FuncDecl(simpleFunc, VoidType, [], None, BlockStmt([CallStmt(printString, BinExpr(::, Id(tmp), BinExpr(::, Id(tmp1), Id(tmp2))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 343))

    def test_more_complex_program40(self):
        """More complex program"""
        input = """
        simpleFunc: function void () {
            foo(1);
            fun(2.333);
            stringg("jbvjabue \\b");
            ttt(!true);
        }"""
        expect = """Program([
	FuncDecl(simpleFunc, VoidType, [], None, BlockStmt([CallStmt(foo, IntegerLit(1)), CallStmt(fun, FloatLit(2.333)), CallStmt(stringg, StringLit(jbvjabue \\b)), CallStmt(ttt, UnExpr(!, BooleanLit(True)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 344))

    def test_more_complex_program41(self):
        """More complex program"""
        input = """
        string1: string = "random string \\f random string";
        string2: string = "I'm \\\"Batman\\\"";
        simpleFunc: function void () {
            print(string1::string2);
        }"""
        expect = """Program([
	VarDecl(string1, StringType, StringLit(random string \\f random string))
	VarDecl(string2, StringType, StringLit(I'm \\\"Batman\\\"))
	FuncDecl(simpleFunc, VoidType, [], None, BlockStmt([CallStmt(print, BinExpr(::, Id(string1), Id(string2)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 345))

    def test_more_complex_program42(self):
        """More complex program"""
        input = """simpleFunc: function void () {
            f[12-3, "stringstring", true] = 1_200_000;
        }"""
        expect = """Program([
	FuncDecl(simpleFunc, VoidType, [], None, BlockStmt([AssignStmt(ArrayCell(f, [BinExpr(-, IntegerLit(12), IntegerLit(3)), StringLit(stringstring), BooleanLit(True)]), IntegerLit(1200000))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 346))

    def test_more_complex_program43(self):
        """More complex program"""
        input = """
        a_ejbcau237: boolean;
        ____22421ekvoib: integer;
        Adbo________kvasubeu83649: string;"""
        expect = """Program([
	VarDecl(a_ejbcau237, BooleanType)
	VarDecl(____22421ekvoib, IntegerType)
	VarDecl(Adbo________kvasubeu83649, StringType)
])"""
        self.assertTrue(TestAST.test(input, expect, 347))

    def test_more_complex_program44(self):
        """More complex program"""
        input = """
        Double: function integer(out n: integer){
            n = n * 2;
        }
        simpleFunc: function void () {
            print(Double(5));
        }"""
        expect = """Program([
	FuncDecl(Double, IntegerType, [OutParam(n, IntegerType)], None, BlockStmt([AssignStmt(Id(n), BinExpr(*, Id(n), IntegerLit(2)))]))
	FuncDecl(simpleFunc, VoidType, [], None, BlockStmt([CallStmt(print, FuncCall(Double, [IntegerLit(5)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 348))

    def test_more_complex_program45(self):
        """More complex program"""
        input = """
        high: function void(a: string){
            print(a);
        }
        inner: function auto(bb: boolean){ return bb==true;}
        simpleFunc: function void () {}"""
        expect = """Program([
	FuncDecl(high, VoidType, [Param(a, StringType)], None, BlockStmt([CallStmt(print, Id(a))]))
	FuncDecl(inner, AutoType, [Param(bb, BooleanType)], None, BlockStmt([ReturnStmt(BinExpr(==, Id(bb), BooleanLit(True)))]))
	FuncDecl(simpleFunc, VoidType, [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 349))

    def test_more_complex_program46(self):
        """More complex program"""
        input = """simpleFunc: function void () {
            i:integer = 5;
            do{
                i = i / 2;
                if(i == 2) break;
            }while(1);
            print(i);
        }"""
        expect = """Program([
	FuncDecl(simpleFunc, VoidType, [], None, BlockStmt([VarDecl(i, IntegerType, IntegerLit(5)), DoWhileStmt(IntegerLit(1), BlockStmt([AssignStmt(Id(i), BinExpr(/, Id(i), IntegerLit(2))), IfStmt(BinExpr(==, Id(i), IntegerLit(2)), BreakStmt())])), CallStmt(print, Id(i))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 350))

    def test_more_complex_program47(self):
        """More complex program"""
        input = """simpleFunc: function void () {
            sum: integer = 0;
            for(i = 1,check(i),i+1){
                if(i != 5) sum = sum + i;
                continue;
            }
            print(sum);
        }"""
        expect = """Program([
	FuncDecl(simpleFunc, VoidType, [], None, BlockStmt([VarDecl(sum, IntegerType, IntegerLit(0)), ForStmt(AssignStmt(Id(i), IntegerLit(1)), FuncCall(check, [Id(i)]), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(!=, Id(i), IntegerLit(5)), AssignStmt(Id(sum), BinExpr(+, Id(sum), Id(i)))), ContinueStmt()])), CallStmt(print, Id(sum))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 351))

    def test_more_complex_program48(self):
        """More complex program"""
        input = """simpleFunc: function void () {
            if(1){if(2){if(3){}}}
            else{}
        }"""
        expect = """Program([
	FuncDecl(simpleFunc, VoidType, [], None, BlockStmt([IfStmt(IntegerLit(1), BlockStmt([IfStmt(IntegerLit(2), BlockStmt([IfStmt(IntegerLit(3), BlockStmt([]))]))]), BlockStmt([]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 352))

    def test_more_complex_program49(self):
        """More complex program"""
        input = """simpleFunc: function void () {
            i[2,4+4,"string\\t"] = tmp <= tmp2; 
        }"""
        expect = """Program([
	FuncDecl(simpleFunc, VoidType, [], None, BlockStmt([AssignStmt(ArrayCell(i, [IntegerLit(2), BinExpr(+, IntegerLit(4), IntegerLit(4)), StringLit(string\\t)]), BinExpr(<=, Id(tmp), Id(tmp2)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 353))

    def test_more_complex_program50(self):
        """More complex program"""
        input = """simpleFunc: function void () {
            toArray("Hello! can u speak \\\'vietnamese\\\'");
        }"""
        expect = """Program([
	FuncDecl(simpleFunc, VoidType, [], None, BlockStmt([CallStmt(toArray, StringLit(Hello! can u speak \\\'vietnamese\\\'))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 354))

    def test_more_complex_program51(self):
        """More complex program"""
        input = """
        esc, esc2, esc3__ : string = "\\r ayyyo", "come on \\f \\n", "2/3\\\ ";
        simpleFunc: function void () {
        }"""
        expect = """Program([
	VarDecl(esc, StringType, StringLit(\\r ayyyo))
	VarDecl(esc2, StringType, StringLit(come on \\f \\n))
	VarDecl(esc3__, StringType, StringLit(2/3\\\ ))
	FuncDecl(simpleFunc, VoidType, [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 355))

    def test_more_complex_program52(self):
        """More complex program"""
        input = """
        ar: array [3] of boolean = {true, a[10], false == true};
        """
        expect = """Program([
	VarDecl(ar, ArrayType([3], BooleanType), ArrayLit([BooleanLit(True), ArrayCell(a, [IntegerLit(10)]), BinExpr(==, BooleanLit(False), BooleanLit(True))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 356))

    def test_more_complex_program53(self):
        """More complex program"""
        input = """
        testType: function auto(inherit out m: integer, out k: boolean, null: string) {
            return;
        }
        """
        expect = """Program([
	FuncDecl(testType, AutoType, [InheritOutParam(m, IntegerType), OutParam(k, BooleanType), Param(null, StringType)], None, BlockStmt([ReturnStmt()]))
])"""
        self.assertTrue(TestAST.test(input, expect, 357))

    def test_more_complex_program54(self):
        """More complex program"""
        input = """simpleFunc: function void () {
            print("=================");
            print("Cause I dont care!");
            print("Who you love oh oh ~");
            print("=================");
        }"""
        expect = """Program([
	FuncDecl(simpleFunc, VoidType, [], None, BlockStmt([CallStmt(print, StringLit(=================)), CallStmt(print, StringLit(Cause I dont care!)), CallStmt(print, StringLit(Who you love oh oh ~)), CallStmt(print, StringLit(=================))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 358))

    def test_more_complex_program55(self):
        """More complex program"""
        input = """simpleFunc: function void () {
            num: integer = 4;
            for(i=1,i<=num,i+1){
                for(j=1,j<=i,j+1){
                    print("*");
                }
            }
        }"""
        expect = """Program([
	FuncDecl(simpleFunc, VoidType, [], None, BlockStmt([VarDecl(num, IntegerType, IntegerLit(4)), ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<=, Id(i), Id(num)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([ForStmt(AssignStmt(Id(j), IntegerLit(1)), BinExpr(<=, Id(j), Id(i)), BinExpr(+, Id(j), IntegerLit(1)), BlockStmt([CallStmt(print, StringLit(*))]))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 359))

    def test_more_complex_program56(self):
        """More complex program"""
        input = """simpleFunc: function void () {
            d,r: integer = 5,4;
            for(i=1,i<=r,i+1){
                if((i==1) || (i==r)){
                    for(j=1,j<=r,j+1){
                        print("*");
                    }
                }
                else{
                    tmp: string = "*";
                    for(j=2,j<=r-1,j+1){
                        tmp = tmp::" ";
                    }
                    tmp = tmp::"*";
                    printLn(tmp);
                }
            }
        }"""
        expect = """Program([
	FuncDecl(simpleFunc, VoidType, [], None, BlockStmt([VarDecl(d, IntegerType, IntegerLit(5)), VarDecl(r, IntegerType, IntegerLit(4)), ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<=, Id(i), Id(r)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(||, BinExpr(==, Id(i), IntegerLit(1)), BinExpr(==, Id(i), Id(r))), BlockStmt([ForStmt(AssignStmt(Id(j), IntegerLit(1)), BinExpr(<=, Id(j), Id(r)), BinExpr(+, Id(j), IntegerLit(1)), BlockStmt([CallStmt(print, StringLit(*))]))]), BlockStmt([VarDecl(tmp, StringType, StringLit(*)), ForStmt(AssignStmt(Id(j), IntegerLit(2)), BinExpr(<=, Id(j), BinExpr(-, Id(r), IntegerLit(1))), BinExpr(+, Id(j), IntegerLit(1)), BlockStmt([AssignStmt(Id(tmp), BinExpr(::, Id(tmp), StringLit( )))])), AssignStmt(Id(tmp), BinExpr(::, Id(tmp), StringLit(*))), CallStmt(printLn, Id(tmp))]))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 360))

    def test_more_complex_program57(self):
        """More complex program"""
        input = """simpleFunc: function void () {
            d,r: integer = 5,4;
            /*print to screen the rectangle*/
            for(i=1,i<=r,i+1){
                printLn("*", d);
            }
        }"""
        expect = """Program([
	FuncDecl(simpleFunc, VoidType, [], None, BlockStmt([VarDecl(d, IntegerType, IntegerLit(5)), VarDecl(r, IntegerType, IntegerLit(4)), ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<=, Id(i), Id(r)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([CallStmt(printLn, StringLit(*), Id(d))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 361))

    def test_more_complex_program58(self):
        """More complex program"""
        input = """simpleFunc: function void () {
            k: integer = 12345;
            l:integer = 0;
            // reverse the number
            while(k){
                r = k % 10;
                k = k / 10;
                l = l * 10 + r;
            }
            print(l);
        }"""
        expect = """Program([
	FuncDecl(simpleFunc, VoidType, [], None, BlockStmt([VarDecl(k, IntegerType, IntegerLit(12345)), VarDecl(l, IntegerType, IntegerLit(0)), WhileStmt(Id(k), BlockStmt([AssignStmt(Id(r), BinExpr(%, Id(k), IntegerLit(10))), AssignStmt(Id(k), BinExpr(/, Id(k), IntegerLit(10))), AssignStmt(Id(l), BinExpr(+, BinExpr(*, Id(l), IntegerLit(10)), Id(r)))])), CallStmt(print, Id(l))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 362))

    def test_more_complex_program59(self):
        """More complex program"""
        input = """simpleFunc: function void () {
            d: integer = 100;
            n: integer = 0;
            while(d){
                r = k % 2;
                k = k / 2;
                n = n * 10 + r;
            }
            print(reverse(n));
        }"""
        expect = """Program([
	FuncDecl(simpleFunc, VoidType, [], None, BlockStmt([VarDecl(d, IntegerType, IntegerLit(100)), VarDecl(n, IntegerType, IntegerLit(0)), WhileStmt(Id(d), BlockStmt([AssignStmt(Id(r), BinExpr(%, Id(k), IntegerLit(2))), AssignStmt(Id(k), BinExpr(/, Id(k), IntegerLit(2))), AssignStmt(Id(n), BinExpr(+, BinExpr(*, Id(n), IntegerLit(10)), Id(r)))])), CallStmt(print, FuncCall(reverse, [Id(n)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 363))

    def test_more_complex_program60(self):
        """More complex program"""
        input = """simpleFunc: function void () inherit main {
            return;
        }"""
        expect = """Program([
	FuncDecl(simpleFunc, VoidType, [], main, BlockStmt([ReturnStmt()]))
])"""
        self.assertTrue(TestAST.test(input, expect, 364))

    def test_more_complex_program61(self):
        """More complex program"""
        input = """simpleFunc: function void () {
            m: string = "Nguyen viet hoa";
            n: string = "";
            for(i=0,i<len(m),i+1){
                n = m[i]::n;
            }
            print(n);
        }"""
        expect = """Program([
	FuncDecl(simpleFunc, VoidType, [], None, BlockStmt([VarDecl(m, StringType, StringLit(Nguyen viet hoa)), VarDecl(n, StringType, StringLit()), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), FuncCall(len, [Id(m)])), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([AssignStmt(Id(n), BinExpr(::, ArrayCell(m, [Id(i)]), Id(n)))])), CallStmt(print, Id(n))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 365))

    def test_more_complex_program62(self):
        """More complex program"""
        input = """
        reverseString: function string(m: string){
            n: string = "";
            for(i=0,i<len(m),i+1){
                n = m[i]::n;
            }
            return n;
        }
        simpleFunc: function void () {
            m: string = "Nguyen viet hoa";
            m = reverseString(m);
            print(m);
        }"""
        expect = """Program([
	FuncDecl(reverseString, StringType, [Param(m, StringType)], None, BlockStmt([VarDecl(n, StringType, StringLit()), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), FuncCall(len, [Id(m)])), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([AssignStmt(Id(n), BinExpr(::, ArrayCell(m, [Id(i)]), Id(n)))])), ReturnStmt(Id(n))]))
	FuncDecl(simpleFunc, VoidType, [], None, BlockStmt([VarDecl(m, StringType, StringLit(Nguyen viet hoa)), AssignStmt(Id(m), FuncCall(reverseString, [Id(m)])), CallStmt(print, Id(m))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 366))

    def test_more_complex_program63(self):
        """More complex program"""
        input = """simpleFunc: function void () {
            a1, a2: string = "Love u to the moon and back, I cant let u know this fact", "moon";
            a1 = toArrayString(a1);
            print(isSubString(a1, a2));
        }"""
        expect = """Program([
	FuncDecl(simpleFunc, VoidType, [], None, BlockStmt([VarDecl(a1, StringType, StringLit(Love u to the moon and back, I cant let u know this fact)), VarDecl(a2, StringType, StringLit(moon)), AssignStmt(Id(a1), FuncCall(toArrayString, [Id(a1)])), CallStmt(print, FuncCall(isSubString, [Id(a1), Id(a2)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 367))

    def test_more_complex_program64(self):
        """More complex program"""
        input = """simpleFunc: function void () {
            m = a + x % 2 / 23 - .9e-23;
            print(m);
        }"""
        expect = """Program([
	FuncDecl(simpleFunc, VoidType, [], None, BlockStmt([AssignStmt(Id(m), BinExpr(-, BinExpr(+, Id(a), BinExpr(/, BinExpr(%, Id(x), IntegerLit(2)), IntegerLit(23))), FloatLit(9e-24))), CallStmt(print, Id(m))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 368))

    def test_more_complex_program65(self):
        """More complex program"""
        input = """simpleFunc: function void () {
            cap["name"] = e[33] + "aa";
        }"""
        expect = """Program([
	FuncDecl(simpleFunc, VoidType, [], None, BlockStmt([AssignStmt(ArrayCell(cap, [StringLit(name)]), BinExpr(+, ArrayCell(e, [IntegerLit(33)]), StringLit(aa)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 369))

    def test_more_complex_program66(self):
        """More complex program"""
        input = """simpleFunc: function void () {
            bool: boolean = (23 == 4) % 120 >= "theheh";
        }"""
        expect = """Program([
	FuncDecl(simpleFunc, VoidType, [], None, BlockStmt([VarDecl(bool, BooleanType, BinExpr(>=, BinExpr(%, BinExpr(==, IntegerLit(23), IntegerLit(4)), IntegerLit(120)), StringLit(theheh)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 370))

    def test_more_complex_program67(self):
        """More complex program"""
        input = """simpleFunc: function void () {
            da: array [3] of string = {"I'm happy u never saw me in college",
                                        "Blood on my hands I refuse to ignore it",
                                        "I got my light headed..."};
            tmp: string = "";
            n: integer = 0;
            while(n<3){
                tmp = tmp::da[n];
                n = n + 1;
            }
            print(tmp);
        }"""
        expect = """Program([
	FuncDecl(simpleFunc, VoidType, [], None, BlockStmt([VarDecl(da, ArrayType([3], StringType), ArrayLit([StringLit(I'm happy u never saw me in college), StringLit(Blood on my hands I refuse to ignore it), StringLit(I got my light headed...)])), VarDecl(tmp, StringType, StringLit()), VarDecl(n, IntegerType, IntegerLit(0)), WhileStmt(BinExpr(<, Id(n), IntegerLit(3)), BlockStmt([AssignStmt(Id(tmp), BinExpr(::, Id(tmp), ArrayCell(da, [Id(n)]))), AssignStmt(Id(n), BinExpr(+, Id(n), IntegerLit(1)))])), CallStmt(print, Id(tmp))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 371))

    def test_more_complex_program68(self):
        """More complex program"""
        input = """simpleFunc: function void () {
            a: string = "Nguyen van Tu";
            b: string = "Nguyen Thi Buoi";
            if (a == b) print(a, b, " vs ");
            else break;
        }"""
        expect = """Program([
	FuncDecl(simpleFunc, VoidType, [], None, BlockStmt([VarDecl(a, StringType, StringLit(Nguyen van Tu)), VarDecl(b, StringType, StringLit(Nguyen Thi Buoi)), IfStmt(BinExpr(==, Id(a), Id(b)), CallStmt(print, Id(a), Id(b), StringLit( vs )), BreakStmt())]))
])"""
        self.assertTrue(TestAST.test(input, expect, 372))

    def test_more_complex_program69(self):
        """More complex program"""
        input = """
        average: function auto(a: auto, b: auto){
            return (a+b)/2;
        }
        simpleFunc: function void () {
            average(3, 4);
        }"""
        expect = """Program([
	FuncDecl(average, AutoType, [Param(a, AutoType), Param(b, AutoType)], None, BlockStmt([ReturnStmt(BinExpr(/, BinExpr(+, Id(a), Id(b)), IntegerLit(2)))]))
	FuncDecl(simpleFunc, VoidType, [], None, BlockStmt([CallStmt(average, IntegerLit(3), IntegerLit(4))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 373))

    def test_more_complex_program70(self):
        """More complex program"""
        input = """
        gcd: function integer(a: integer, b: integer) inherit GCD__A {
            if(a == b) return a;
            if(a>b){
                return gcd(b, a-b);
            }
            return gcd(a, b-a);
        }
        simpleFunc: function void () {
            print(gcd(5, 10));
        }"""
        expect = """Program([
	FuncDecl(gcd, IntegerType, [Param(a, IntegerType), Param(b, IntegerType)], GCD__A, BlockStmt([IfStmt(BinExpr(==, Id(a), Id(b)), ReturnStmt(Id(a))), IfStmt(BinExpr(>, Id(a), Id(b)), BlockStmt([ReturnStmt(FuncCall(gcd, [Id(b), BinExpr(-, Id(a), Id(b))]))])), ReturnStmt(FuncCall(gcd, [Id(a), BinExpr(-, Id(b), Id(a))]))]))
	FuncDecl(simpleFunc, VoidType, [], None, BlockStmt([CallStmt(print, FuncCall(gcd, [IntegerLit(5), IntegerLit(10)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 374))

    def test_more_complex_program71(self):
        """More complex program"""
        input = """
        fibonacci: function integer(n: integer) {
            f0,f1,fn: integer = 0,1,1;
            i:integer;
            if (n < 0) {
                return -1;
            } 
            if ((n == 0) || (n == 1)) {
                return n;
            } else {
                for (i = 2, i < n, i+1) {
                    f0 = f1;
                    f1 = fn;
                    fn = f0 + f1;
                }
            }
            return fn;
        }
        simpleFunc: function void () {
            print(fibonacci(10));
        }"""
        expect = """Program([
	FuncDecl(fibonacci, IntegerType, [Param(n, IntegerType)], None, BlockStmt([VarDecl(f0, IntegerType, IntegerLit(0)), VarDecl(f1, IntegerType, IntegerLit(1)), VarDecl(fn, IntegerType, IntegerLit(1)), VarDecl(i, IntegerType), IfStmt(BinExpr(<, Id(n), IntegerLit(0)), BlockStmt([ReturnStmt(UnExpr(-, IntegerLit(1)))])), IfStmt(BinExpr(||, BinExpr(==, Id(n), IntegerLit(0)), BinExpr(==, Id(n), IntegerLit(1))), BlockStmt([ReturnStmt(Id(n))]), BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(2)), BinExpr(<, Id(i), Id(n)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([AssignStmt(Id(f0), Id(f1)), AssignStmt(Id(f1), Id(fn)), AssignStmt(Id(fn), BinExpr(+, Id(f0), Id(f1)))]))])), ReturnStmt(Id(fn))]))
	FuncDecl(simpleFunc, VoidType, [], None, BlockStmt([CallStmt(print, FuncCall(fibonacci, [IntegerLit(10)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 375))

    def test_more_complex_program72(self):
        """More complex program"""
        input = """a,b: float = 0.E-3, 1e-3;"""
        expect = """Program([
	VarDecl(a, FloatType, FloatLit(0.0))
	VarDecl(b, FloatType, FloatLit(0.001))
])"""
        self.assertTrue(TestAST.test(input, expect, 376))

    def test_more_complex_program73(self):
        """More complex program"""
        input = """
        isPrimeNumber: function integer(n: integer) {
            // so nguyen n < 2 khong phai la so nguyen to
            if (n < 2) {
                return 0;
            }
            // check so nguyen to khi n >= 2
            squareRoot: integer = sqrt(n);
            for (i = 2, i <= squareRoot, i+1) {
                if (n % i == 0) {
                    return 0;
                }
            }
            return 1;
        }
        simpleFunc: function void () {
            for (i = 0, i < 100, i+1) {
                if (isPrimeNumber(i)) {
                    print(i + " ");
                }
            }
        }"""
        expect = """Program([
	FuncDecl(isPrimeNumber, IntegerType, [Param(n, IntegerType)], None, BlockStmt([IfStmt(BinExpr(<, Id(n), IntegerLit(2)), BlockStmt([ReturnStmt(IntegerLit(0))])), VarDecl(squareRoot, IntegerType, FuncCall(sqrt, [Id(n)])), ForStmt(AssignStmt(Id(i), IntegerLit(2)), BinExpr(<=, Id(i), Id(squareRoot)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(==, BinExpr(%, Id(n), Id(i)), IntegerLit(0)), BlockStmt([ReturnStmt(IntegerLit(0))]))])), ReturnStmt(IntegerLit(1))]))
	FuncDecl(simpleFunc, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(100)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([IfStmt(FuncCall(isPrimeNumber, [Id(i)]), BlockStmt([CallStmt(print, BinExpr(+, Id(i), StringLit( )))]))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 377))

    def test_more_complex_program74(self):
        """More complex program"""
        input = """
        USCLN: function integer(a: integer, b: integer) {
            if (b == 0) return a;
            return USCLN(b, a % b);
        }
        simpleFunc: function void () {
            a,b: integer;
            getInput(a, b);
            print("USCLN cua %d va %d la: %d, ", a, b, USCLN(a, b));
        }"""
        expect = """Program([
	FuncDecl(USCLN, IntegerType, [Param(a, IntegerType), Param(b, IntegerType)], None, BlockStmt([IfStmt(BinExpr(==, Id(b), IntegerLit(0)), ReturnStmt(Id(a))), ReturnStmt(FuncCall(USCLN, [Id(b), BinExpr(%, Id(a), Id(b))]))]))
	FuncDecl(simpleFunc, VoidType, [], None, BlockStmt([VarDecl(a, IntegerType), VarDecl(b, IntegerType), CallStmt(getInput, Id(a), Id(b)), CallStmt(print, StringLit(USCLN cua %d va %d la: %d, ), Id(a), Id(b), FuncCall(USCLN, [Id(a), Id(b)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 378))

    def test_more_complex_program75(self):
        """More complex program"""
        input = """
        USCLN: function integer(a: integer, b: integer) {
            if (b == 0) return a;
            return USCLN(b, a % b);
        }
        BSCNN: function integer(a: integer, b: integer) {
            return (a * b) / USCLN(a, b);
        }
        simpleFunc: function void () {
            a,b: integer;
            getInput(a, b);
            print("BSCNN cua %d va %d la: %d", a, b, BSCNN(a, b));
        }"""
        expect = """Program([
	FuncDecl(USCLN, IntegerType, [Param(a, IntegerType), Param(b, IntegerType)], None, BlockStmt([IfStmt(BinExpr(==, Id(b), IntegerLit(0)), ReturnStmt(Id(a))), ReturnStmt(FuncCall(USCLN, [Id(b), BinExpr(%, Id(a), Id(b))]))]))
	FuncDecl(BSCNN, IntegerType, [Param(a, IntegerType), Param(b, IntegerType)], None, BlockStmt([ReturnStmt(BinExpr(/, BinExpr(*, Id(a), Id(b)), FuncCall(USCLN, [Id(a), Id(b)])))]))
	FuncDecl(simpleFunc, VoidType, [], None, BlockStmt([VarDecl(a, IntegerType), VarDecl(b, IntegerType), CallStmt(getInput, Id(a), Id(b)), CallStmt(print, StringLit(BSCNN cua %d va %d la: %d), Id(a), Id(b), FuncCall(BSCNN, [Id(a), Id(b)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 379))

    def test_more_complex_program76(self):
        """More complex program"""
        input = """
        Analyse_Integer: function void(n: integer) {
            i, dem : integer = 2, 0;
            a: array [100] of integer;
            while (n > 1) {
                if (n % i == 0) {
                    n = n / i;
                    a[dem] = i;
                    dem = dem + 1;
                } else {
                    i =  i + 1;
                }
            }

            if (dem == 0) {
                a[dem] = n;
                dem = dem + 1;
            }

            for (i = 0, i < dem - 1, i+1) {
                print(a[i] + " x ");
            }
            print(a[dem - 1]);
        }

        simpleFunc: function void () {
            n: integer;
            getinput(n);
            Analyse_Integer(n);
        }"""
        expect = """Program([
	FuncDecl(Analyse_Integer, VoidType, [Param(n, IntegerType)], None, BlockStmt([VarDecl(i, IntegerType, IntegerLit(2)), VarDecl(dem, IntegerType, IntegerLit(0)), VarDecl(a, ArrayType([100], IntegerType)), WhileStmt(BinExpr(>, Id(n), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(==, BinExpr(%, Id(n), Id(i)), IntegerLit(0)), BlockStmt([AssignStmt(Id(n), BinExpr(/, Id(n), Id(i))), AssignStmt(ArrayCell(a, [Id(dem)]), Id(i)), AssignStmt(Id(dem), BinExpr(+, Id(dem), IntegerLit(1)))]), BlockStmt([AssignStmt(Id(i), BinExpr(+, Id(i), IntegerLit(1)))]))])), IfStmt(BinExpr(==, Id(dem), IntegerLit(0)), BlockStmt([AssignStmt(ArrayCell(a, [Id(dem)]), Id(n)), AssignStmt(Id(dem), BinExpr(+, Id(dem), IntegerLit(1)))])), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), BinExpr(-, Id(dem), IntegerLit(1))), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([CallStmt(print, BinExpr(+, ArrayCell(a, [Id(i)]), StringLit( x )))])), CallStmt(print, ArrayCell(a, [BinExpr(-, Id(dem), IntegerLit(1))]))]))
	FuncDecl(simpleFunc, VoidType, [], None, BlockStmt([VarDecl(n, IntegerType), CallStmt(getinput, Id(n)), CallStmt(Analyse_Integer, Id(n))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 380))

    def test_more_complex_program77(self):
        """More complex program"""
        input = """
        dec: integer = 10;
        sum_digit_number: function integer(n: integer) {
            total: integer = 0;
            do {
                total = total + n % dec;
                n = n / dec;
            } while (n > 0);
            return total;
        }
        simpleFunc: function void () {
            print("The sum of all digit in a number is: " + sum_digit_number(163846));
        }"""
        expect = """Program([
	VarDecl(dec, IntegerType, IntegerLit(10))
	FuncDecl(sum_digit_number, IntegerType, [Param(n, IntegerType)], None, BlockStmt([VarDecl(total, IntegerType, IntegerLit(0)), DoWhileStmt(BinExpr(>, Id(n), IntegerLit(0)), BlockStmt([AssignStmt(Id(total), BinExpr(+, Id(total), BinExpr(%, Id(n), Id(dec)))), AssignStmt(Id(n), BinExpr(/, Id(n), Id(dec)))])), ReturnStmt(Id(total))]))
	FuncDecl(simpleFunc, VoidType, [], None, BlockStmt([CallStmt(print, BinExpr(+, StringLit(The sum of all digit in a number is: ), FuncCall(sum_digit_number, [IntegerLit(163846)])))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 381))

    def test_more_complex_program78(self):
        """More complex program"""
        input = """
        PerfectNum: function boolean(n: integer) {
            a: array [20] of integer;
            dem: integer = 0;
            do {
                a[dem] = (n % 10);
                n = n / 10;
                dem = dem + 1;
            } while (n > 0);

            for (i = 0, i < (dem/2), i+1) {
                if (a[i] != a[dem - i - 1]) {
                    return true;
                }
            }
            return false;
        }
        simpleFunc: function void () {
            n: integer;
            getInput(n);
            print(PerfectNum(n));
        }"""
        expect = """Program([
	FuncDecl(PerfectNum, BooleanType, [Param(n, IntegerType)], None, BlockStmt([VarDecl(a, ArrayType([20], IntegerType)), VarDecl(dem, IntegerType, IntegerLit(0)), DoWhileStmt(BinExpr(>, Id(n), IntegerLit(0)), BlockStmt([AssignStmt(ArrayCell(a, [Id(dem)]), BinExpr(%, Id(n), IntegerLit(10))), AssignStmt(Id(n), BinExpr(/, Id(n), IntegerLit(10))), AssignStmt(Id(dem), BinExpr(+, Id(dem), IntegerLit(1)))])), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), BinExpr(/, Id(dem), IntegerLit(2))), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(!=, ArrayCell(a, [Id(i)]), ArrayCell(a, [BinExpr(-, BinExpr(-, Id(dem), Id(i)), IntegerLit(1))])), BlockStmt([ReturnStmt(BooleanLit(True))]))])), ReturnStmt(BooleanLit(False))]))
	FuncDecl(simpleFunc, VoidType, [], None, BlockStmt([VarDecl(n, IntegerType), CallStmt(getInput, Id(n)), CallStmt(print, FuncCall(PerfectNum, [Id(n)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 382))

    def test_more_complex_program79(self):
        """More complex program"""
        input = """
        fibonacci: function integer(n: integer) {
            f0,f1,fn: integer = 0,1,1;
            i:integer;
            if (n < 0) {
                return -1;
            } 
            if ((n == 0) || (n == 1)) {
                return n;
            } else {
                for (i = 2, i < n, i+1) {
                    f0 = f1;
                    f1 = fn;
                    fn = f0 + f1;
                }
            }
            return fn;
        }

        isPrimeNumber: function integer(n: integer) {
            if (n < 2) {
                return 0;
            }
            squareRoot: integer = sqrt(n);
            for (i = 2, i <= squareRoot, i+1) {
                if (n % i == 0) {
                    return 0;
                }
            }
            return 1;
        }
        simpleFunc: function void () {
            n: integer;
            getInput(n);
            i: integer = 0;
            print("All fiibinacci numbers < n and are prime number: ");
            while(fibonacci(i) < n){
                fi: integer = fibonacci(i);
                if (isPrimeNumber(fi)){
                    print(fi + " ");
                }
                i = i + 1;
            }   
        }"""
        expect = """Program([
	FuncDecl(fibonacci, IntegerType, [Param(n, IntegerType)], None, BlockStmt([VarDecl(f0, IntegerType, IntegerLit(0)), VarDecl(f1, IntegerType, IntegerLit(1)), VarDecl(fn, IntegerType, IntegerLit(1)), VarDecl(i, IntegerType), IfStmt(BinExpr(<, Id(n), IntegerLit(0)), BlockStmt([ReturnStmt(UnExpr(-, IntegerLit(1)))])), IfStmt(BinExpr(||, BinExpr(==, Id(n), IntegerLit(0)), BinExpr(==, Id(n), IntegerLit(1))), BlockStmt([ReturnStmt(Id(n))]), BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(2)), BinExpr(<, Id(i), Id(n)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([AssignStmt(Id(f0), Id(f1)), AssignStmt(Id(f1), Id(fn)), AssignStmt(Id(fn), BinExpr(+, Id(f0), Id(f1)))]))])), ReturnStmt(Id(fn))]))
	FuncDecl(isPrimeNumber, IntegerType, [Param(n, IntegerType)], None, BlockStmt([IfStmt(BinExpr(<, Id(n), IntegerLit(2)), BlockStmt([ReturnStmt(IntegerLit(0))])), VarDecl(squareRoot, IntegerType, FuncCall(sqrt, [Id(n)])), ForStmt(AssignStmt(Id(i), IntegerLit(2)), BinExpr(<=, Id(i), Id(squareRoot)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(==, BinExpr(%, Id(n), Id(i)), IntegerLit(0)), BlockStmt([ReturnStmt(IntegerLit(0))]))])), ReturnStmt(IntegerLit(1))]))
	FuncDecl(simpleFunc, VoidType, [], None, BlockStmt([VarDecl(n, IntegerType), CallStmt(getInput, Id(n)), VarDecl(i, IntegerType, IntegerLit(0)), CallStmt(print, StringLit(All fiibinacci numbers < n and are prime number: )), WhileStmt(BinExpr(<, FuncCall(fibonacci, [Id(i)]), Id(n)), BlockStmt([VarDecl(fi, IntegerType, FuncCall(fibonacci, [Id(i)])), IfStmt(FuncCall(isPrimeNumber, [Id(fi)]), BlockStmt([CallStmt(print, BinExpr(+, Id(fi), StringLit( )))])), AssignStmt(Id(i), BinExpr(+, Id(i), IntegerLit(1)))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 383))

    def test_more_complex_program80(self):
        """More complex program"""
        input = """simpleFunc: function void () {
        n: integer = 6;  
        for(i = 1, i <= n, i+1) {
            for(j = 1, j <= n-i, j+1)
                print(" ");
        
            for(j = 1, j <= i, j+1)
                print("* ");
        
            printf("\\n");
        }
        return 1;
        }"""
        expect = """Program([
	FuncDecl(simpleFunc, VoidType, [], None, BlockStmt([VarDecl(n, IntegerType, IntegerLit(6)), ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<=, Id(i), Id(n)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([ForStmt(AssignStmt(Id(j), IntegerLit(1)), BinExpr(<=, Id(j), BinExpr(-, Id(n), Id(i))), BinExpr(+, Id(j), IntegerLit(1)), CallStmt(print, StringLit( ))), ForStmt(AssignStmt(Id(j), IntegerLit(1)), BinExpr(<=, Id(j), Id(i)), BinExpr(+, Id(j), IntegerLit(1)), CallStmt(print, StringLit(* ))), CallStmt(printf, StringLit(\\n))])), ReturnStmt(IntegerLit(1))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 384))

    def test_more_complex_program81(self):
        """More complex program"""
        input = """simpleFunc: function void () {
            a, b, c: array [2,3] of integer;
            getInputArray(a);
            getInputArray(b);
            for (i = 0, i < 2, i+1)
                for (j = 0, j < 3, j+1) {
                    c[i,j] = a[i,j] + b[i,j];
                }
            for (i = 0, i < 2, i+1) {
                for (j = 0, j < 3, j+1) {
                    print(c[i,j] + " ");
                }
                print("\\n");
            }
 
        }"""
        expect = """Program([
	FuncDecl(simpleFunc, VoidType, [], None, BlockStmt([VarDecl(a, ArrayType([2, 3], IntegerType)), VarDecl(b, ArrayType([2, 3], IntegerType)), VarDecl(c, ArrayType([2, 3], IntegerType)), CallStmt(getInputArray, Id(a)), CallStmt(getInputArray, Id(b)), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(2)), BinExpr(+, Id(i), IntegerLit(1)), ForStmt(AssignStmt(Id(j), IntegerLit(0)), BinExpr(<, Id(j), IntegerLit(3)), BinExpr(+, Id(j), IntegerLit(1)), BlockStmt([AssignStmt(ArrayCell(c, [Id(i), Id(j)]), BinExpr(+, ArrayCell(a, [Id(i), Id(j)]), ArrayCell(b, [Id(i), Id(j)])))]))), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(2)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([ForStmt(AssignStmt(Id(j), IntegerLit(0)), BinExpr(<, Id(j), IntegerLit(3)), BinExpr(+, Id(j), IntegerLit(1)), BlockStmt([CallStmt(print, BinExpr(+, ArrayCell(c, [Id(i), Id(j)]), StringLit( )))])), CallStmt(print, StringLit(\\n))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 385))

    def test_more_complex_program82(self):
        """More complex program"""
        input = """simpleFunc: function void () {
            a: array [2,3] of integer;
            getInputArray(a);
            sum: integer = 0;
            for (i = 0, i < 2, i+1)
                for (j = 0, j < 3, j+1) {
                    sum = sum + a[i,j];
                }
            print("Sum of all elements in array: " + sum);
        }"""
        expect = """Program([
	FuncDecl(simpleFunc, VoidType, [], None, BlockStmt([VarDecl(a, ArrayType([2, 3], IntegerType)), CallStmt(getInputArray, Id(a)), VarDecl(sum, IntegerType, IntegerLit(0)), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(2)), BinExpr(+, Id(i), IntegerLit(1)), ForStmt(AssignStmt(Id(j), IntegerLit(0)), BinExpr(<, Id(j), IntegerLit(3)), BinExpr(+, Id(j), IntegerLit(1)), BlockStmt([AssignStmt(Id(sum), BinExpr(+, Id(sum), ArrayCell(a, [Id(i), Id(j)])))]))), CallStmt(print, BinExpr(+, StringLit(Sum of all elements in array: ), Id(sum)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 386))

    def test_more_complex_program83(self):
        """More complex program"""
        input = """simpleFunc: function void () {
            n: integer;
            k: integer = 1;
            getInput(n);
            for(i = 1, i <= n, i+1) {
                for(j=1, j <= i, j+1){
                    print(k + " ");
                    k = k + 1;
                }   
                print("\\n");
            }
        }"""
        expect = """Program([
	FuncDecl(simpleFunc, VoidType, [], None, BlockStmt([VarDecl(n, IntegerType), VarDecl(k, IntegerType, IntegerLit(1)), CallStmt(getInput, Id(n)), ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<=, Id(i), Id(n)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([ForStmt(AssignStmt(Id(j), IntegerLit(1)), BinExpr(<=, Id(j), Id(i)), BinExpr(+, Id(j), IntegerLit(1)), BlockStmt([CallStmt(print, BinExpr(+, Id(k), StringLit( ))), AssignStmt(Id(k), BinExpr(+, Id(k), IntegerLit(1)))])), CallStmt(print, StringLit(\\n))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 387))

    def test_more_complex_program84(self):
        """More complex program"""
        input = """
        isLeafYear: function boolean (n: integer) {
            if ((n%4==0)||(n%400==0)) return true;
            return false;
        }"""
        expect = """Program([
	FuncDecl(isLeafYear, BooleanType, [Param(n, IntegerType)], None, BlockStmt([IfStmt(BinExpr(||, BinExpr(==, BinExpr(%, Id(n), IntegerLit(4)), IntegerLit(0)), BinExpr(==, BinExpr(%, Id(n), IntegerLit(400)), IntegerLit(0))), ReturnStmt(BooleanLit(True))), ReturnStmt(BooleanLit(False))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 388))

    def test_more_complex_program85(self):
        """More complex program"""
        input = """
        CanChi: function string (n:integer) {
            r: integer = n%12;
            if(r==0) return "Than";
            if(r==1) return "Dau";
            if(r==2) return "Tuat";
            if(r==3) return "Hoi";
            if(r==4) return "Ti";
            if(r==5) return "Suu";
            if(r==6) return "Dan";
            if(r==7) return "Mao";
            if(r==8) return "Thin";
            if(r==9) return "Ty";
            if(r==10) return "Ngo";
            else return "Mui";
        }"""
        expect = """Program([
	FuncDecl(CanChi, StringType, [Param(n, IntegerType)], None, BlockStmt([VarDecl(r, IntegerType, BinExpr(%, Id(n), IntegerLit(12))), IfStmt(BinExpr(==, Id(r), IntegerLit(0)), ReturnStmt(StringLit(Than))), IfStmt(BinExpr(==, Id(r), IntegerLit(1)), ReturnStmt(StringLit(Dau))), IfStmt(BinExpr(==, Id(r), IntegerLit(2)), ReturnStmt(StringLit(Tuat))), IfStmt(BinExpr(==, Id(r), IntegerLit(3)), ReturnStmt(StringLit(Hoi))), IfStmt(BinExpr(==, Id(r), IntegerLit(4)), ReturnStmt(StringLit(Ti))), IfStmt(BinExpr(==, Id(r), IntegerLit(5)), ReturnStmt(StringLit(Suu))), IfStmt(BinExpr(==, Id(r), IntegerLit(6)), ReturnStmt(StringLit(Dan))), IfStmt(BinExpr(==, Id(r), IntegerLit(7)), ReturnStmt(StringLit(Mao))), IfStmt(BinExpr(==, Id(r), IntegerLit(8)), ReturnStmt(StringLit(Thin))), IfStmt(BinExpr(==, Id(r), IntegerLit(9)), ReturnStmt(StringLit(Ty))), IfStmt(BinExpr(==, Id(r), IntegerLit(10)), ReturnStmt(StringLit(Ngo)), ReturnStmt(StringLit(Mui)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 389))

    def test_more_complex_program86(self):
        """More complex program"""
        input = """
        HToS: function void(n: float){
            m: float = n * 3600;
            print(n + " hours is equal to " + m + " seconds");
        }"""
        expect = """Program([
	FuncDecl(HToS, VoidType, [Param(n, FloatType)], None, BlockStmt([VarDecl(m, FloatType, BinExpr(*, Id(n), IntegerLit(3600))), CallStmt(print, BinExpr(+, BinExpr(+, BinExpr(+, Id(n), StringLit( hours is equal to )), Id(m)), StringLit( seconds)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 390))

    def test_more_complex_program87(self):
        """More complex program"""
        input = """SToH: function void(n: float){
            m: float = n / 3600;
            print(n + " seconds is equal to " + m + " hours");
        }"""
        expect = """Program([
	FuncDecl(SToH, VoidType, [Param(n, FloatType)], None, BlockStmt([VarDecl(m, FloatType, BinExpr(/, Id(n), IntegerLit(3600))), CallStmt(print, BinExpr(+, BinExpr(+, BinExpr(+, Id(n), StringLit( seconds is equal to )), Id(m)), StringLit( hours)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 391))

    def test_more_complex_program88(self):
        """More complex program"""
        input = """simpleFunc: function void () {
            d, m, y: integer;
            getInput(d, m, y);
            a,b,D: integer;
            D = y - 1 ;
            K: integer = 365 * D;
            D = y % 4;
            day_num: integer;
            kq: integer = 0;
            for (a = 1, a <= y - 1, a+1) {
                if (a % 100 == 0) {
                    if (a % 400 == 0) K = K + 1 ;
                }
                else if (a % 4 == 0) K = K + 1 ;
            }
            if (nam % 100 == 0) {
                    if (nam % 400 == 0) kq = 1 ;
                    else kq = 0 ;
            }
            else {
                if (nam % 4 == 0) kq = 1 ;
                else kq = 0 ;
            }
            ds: integer = 0;
            for (a = 1, a <= m, a+1) {
                
                if ((a==1) || (a==3) || (a==5) || (a==7) || (a==8) || (a==10) || (a==12)) day_num = 31;
                if ((a==4) ||(a==6)|| (a==9 )|| (a==11)) day_num = 30 ;
                if (a==2) {
                    if (kq==1) day_num = 29 ;
                    else day_num = 28 ;
                }
                for (b = 1, b <= day_num, b+1) {
                    K = K + 1 ;
                    if ((b == d) && (a == m)) {
                        ds = 1 ;
                        break;
                    }
                }
                if (ds == 1) break ;
            }
            K = K % 7 ;
            if(K==0) print("Chu nhat");
            if(K==1) print("Thu Hai");
            if(K==2) print("Thu Ba");
            if(K==3) print("Thu Tu");
            if(K==4) print("Thu Nam");
            if(K==5) print("Thu Sau");
            else print("Thu Bay");
        }"""
        expect = """Program([
	FuncDecl(simpleFunc, VoidType, [], None, BlockStmt([VarDecl(d, IntegerType), VarDecl(m, IntegerType), VarDecl(y, IntegerType), CallStmt(getInput, Id(d), Id(m), Id(y)), VarDecl(a, IntegerType), VarDecl(b, IntegerType), VarDecl(D, IntegerType), AssignStmt(Id(D), BinExpr(-, Id(y), IntegerLit(1))), VarDecl(K, IntegerType, BinExpr(*, IntegerLit(365), Id(D))), AssignStmt(Id(D), BinExpr(%, Id(y), IntegerLit(4))), VarDecl(day_num, IntegerType), VarDecl(kq, IntegerType, IntegerLit(0)), ForStmt(AssignStmt(Id(a), IntegerLit(1)), BinExpr(<=, Id(a), BinExpr(-, Id(y), IntegerLit(1))), BinExpr(+, Id(a), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(==, BinExpr(%, Id(a), IntegerLit(100)), IntegerLit(0)), BlockStmt([IfStmt(BinExpr(==, BinExpr(%, Id(a), IntegerLit(400)), IntegerLit(0)), AssignStmt(Id(K), BinExpr(+, Id(K), IntegerLit(1))))]), IfStmt(BinExpr(==, BinExpr(%, Id(a), IntegerLit(4)), IntegerLit(0)), AssignStmt(Id(K), BinExpr(+, Id(K), IntegerLit(1)))))])), IfStmt(BinExpr(==, BinExpr(%, Id(nam), IntegerLit(100)), IntegerLit(0)), BlockStmt([IfStmt(BinExpr(==, BinExpr(%, Id(nam), IntegerLit(400)), IntegerLit(0)), AssignStmt(Id(kq), IntegerLit(1)), AssignStmt(Id(kq), IntegerLit(0)))]), BlockStmt([IfStmt(BinExpr(==, BinExpr(%, Id(nam), IntegerLit(4)), IntegerLit(0)), AssignStmt(Id(kq), IntegerLit(1)), AssignStmt(Id(kq), IntegerLit(0)))])), VarDecl(ds, IntegerType, IntegerLit(0)), ForStmt(AssignStmt(Id(a), IntegerLit(1)), BinExpr(<=, Id(a), Id(m)), BinExpr(+, Id(a), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(||, BinExpr(||, BinExpr(||, BinExpr(||, BinExpr(||, BinExpr(||, BinExpr(==, Id(a), IntegerLit(1)), BinExpr(==, Id(a), IntegerLit(3))), BinExpr(==, Id(a), IntegerLit(5))), BinExpr(==, Id(a), IntegerLit(7))), BinExpr(==, Id(a), IntegerLit(8))), BinExpr(==, Id(a), IntegerLit(10))), BinExpr(==, Id(a), IntegerLit(12))), AssignStmt(Id(day_num), IntegerLit(31))), IfStmt(BinExpr(||, BinExpr(||, BinExpr(||, BinExpr(==, Id(a), IntegerLit(4)), BinExpr(==, Id(a), IntegerLit(6))), BinExpr(==, Id(a), IntegerLit(9))), BinExpr(==, Id(a), IntegerLit(11))), AssignStmt(Id(day_num), IntegerLit(30))), IfStmt(BinExpr(==, Id(a), IntegerLit(2)), BlockStmt([IfStmt(BinExpr(==, Id(kq), IntegerLit(1)), AssignStmt(Id(day_num), IntegerLit(29)), AssignStmt(Id(day_num), IntegerLit(28)))])), ForStmt(AssignStmt(Id(b), IntegerLit(1)), BinExpr(<=, Id(b), Id(day_num)), BinExpr(+, Id(b), IntegerLit(1)), BlockStmt([AssignStmt(Id(K), BinExpr(+, Id(K), IntegerLit(1))), IfStmt(BinExpr(&&, BinExpr(==, Id(b), Id(d)), BinExpr(==, Id(a), Id(m))), BlockStmt([AssignStmt(Id(ds), IntegerLit(1)), BreakStmt()]))])), IfStmt(BinExpr(==, Id(ds), IntegerLit(1)), BreakStmt())])), AssignStmt(Id(K), BinExpr(%, Id(K), IntegerLit(7))), IfStmt(BinExpr(==, Id(K), IntegerLit(0)), CallStmt(print, StringLit(Chu nhat))), IfStmt(BinExpr(==, Id(K), IntegerLit(1)), CallStmt(print, StringLit(Thu Hai))), IfStmt(BinExpr(==, Id(K), IntegerLit(2)), CallStmt(print, StringLit(Thu Ba))), IfStmt(BinExpr(==, Id(K), IntegerLit(3)), CallStmt(print, StringLit(Thu Tu))), IfStmt(BinExpr(==, Id(K), IntegerLit(4)), CallStmt(print, StringLit(Thu Nam))), IfStmt(BinExpr(==, Id(K), IntegerLit(5)), CallStmt(print, StringLit(Thu Sau)), CallStmt(print, StringLit(Thu Bay)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 392))

    def test_more_complex_program89(self):
        """More complex program"""
        input = """
        pi: float = 3.14159265359;
        simpleFunc: function void () {
            r: integer;
            getInput(r);
            S: float = pow(r, 2) * pi;
            print("Dien tich hinh tron la:\\t");
        }"""
        expect = """Program([
	VarDecl(pi, FloatType, FloatLit(3.14159265359))
	FuncDecl(simpleFunc, VoidType, [], None, BlockStmt([VarDecl(r, IntegerType), CallStmt(getInput, Id(r)), VarDecl(S, FloatType, BinExpr(*, FuncCall(pow, [Id(r), IntegerLit(2)]), Id(pi))), CallStmt(print, StringLit(Dien tich hinh tron la:\\t))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 393))

    def test_more_complex_program90(self):
        """More complex program"""
        input = """simpleFunc: function void () {
            fahrenheit, celsius: float = 0.0, 0.0;

            print("Please input the Celsius degree(s): ");
            getInput(celcius);
            print("=> The Fahrenheit is: " + (celsius * 1.8 + 32.0) + " degree(s)\\n");

            print("Please input the Fahrenheit degree(s): ");
            getInput(fahrenheit);
            print("=> The Celsius is: " + ((fahrenheit - 32.0) / 1.8) + " degree(s)\\n");
        }"""
        expect = """Program([
	FuncDecl(simpleFunc, VoidType, [], None, BlockStmt([VarDecl(fahrenheit, FloatType, FloatLit(0.0)), VarDecl(celsius, FloatType, FloatLit(0.0)), CallStmt(print, StringLit(Please input the Celsius degree(s): )), CallStmt(getInput, Id(celcius)), CallStmt(print, BinExpr(+, BinExpr(+, StringLit(=> The Fahrenheit is: ), BinExpr(+, BinExpr(*, Id(celsius), FloatLit(1.8)), FloatLit(32.0))), StringLit( degree(s)\\n))), CallStmt(print, StringLit(Please input the Fahrenheit degree(s): )), CallStmt(getInput, Id(fahrenheit)), CallStmt(print, BinExpr(+, BinExpr(+, StringLit(=> The Celsius is: ), BinExpr(/, BinExpr(-, Id(fahrenheit), FloatLit(32.0)), FloatLit(1.8))), StringLit( degree(s)\\n)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 394))

    def test_more_complex_program91(self):
        """More complex program"""
        input = """simpleFunc: function void () {
            i, n: integer;
            print("Nhap so n: ");
            getInput(n);
            print("In bang nhan tu 1 den 20 voi " + n + " :\\n");
                
            for(i = 1, i <= 20, i+1) {
                print(n + "\\t x\\t" + i + "\\t =\\t" + (n*i) + "\\n");
            }
        }"""
        expect = """Program([
	FuncDecl(simpleFunc, VoidType, [], None, BlockStmt([VarDecl(i, IntegerType), VarDecl(n, IntegerType), CallStmt(print, StringLit(Nhap so n: )), CallStmt(getInput, Id(n)), CallStmt(print, BinExpr(+, BinExpr(+, StringLit(In bang nhan tu 1 den 20 voi ), Id(n)), StringLit( :\\n))), ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<=, Id(i), IntegerLit(20)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([CallStmt(print, BinExpr(+, BinExpr(+, BinExpr(+, BinExpr(+, BinExpr(+, Id(n), StringLit(\\t x\\t)), Id(i)), StringLit(\\t =\\t)), BinExpr(*, Id(n), Id(i))), StringLit(\\n)))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 395))

    def test_more_complex_program92(self):
        """More complex program"""
        input = """simpleFunc: function void () {
            n: integer;
            do{
                getInput(n);
                if(n < 0) break;
                print(n + " ");
            }while(1);
            return;
        }"""
        expect = """Program([
	FuncDecl(simpleFunc, VoidType, [], None, BlockStmt([VarDecl(n, IntegerType), DoWhileStmt(IntegerLit(1), BlockStmt([CallStmt(getInput, Id(n)), IfStmt(BinExpr(<, Id(n), IntegerLit(0)), BreakStmt()), CallStmt(print, BinExpr(+, Id(n), StringLit( )))])), ReturnStmt()]))
])"""
        self.assertTrue(TestAST.test(input, expect, 396))

    def test_more_complex_program93(self):
        """More complex program"""
        input = """simpleFunc: function void () {
            i,S,n: float;
            print("Nhap n: ");
            getInput(n);
            S = 0;
            for (i = 1 ,i <= n, i+1) {
                S = S + 1 / (i * i * i);
            }
            print(setprecision(S, 5));
        }"""
        expect = """Program([
	FuncDecl(simpleFunc, VoidType, [], None, BlockStmt([VarDecl(i, FloatType), VarDecl(S, FloatType), VarDecl(n, FloatType), CallStmt(print, StringLit(Nhap n: )), CallStmt(getInput, Id(n)), AssignStmt(Id(S), IntegerLit(0)), ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<=, Id(i), Id(n)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([AssignStmt(Id(S), BinExpr(+, Id(S), BinExpr(/, IntegerLit(1), BinExpr(*, BinExpr(*, Id(i), Id(i)), Id(i)))))])), CallStmt(print, FuncCall(setprecision, [Id(S), IntegerLit(5)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 397))

    def test_more_complex_program94(self):
        """More complex program"""
        input = """simpleFunc: function void () {
        x,y: integer;
		print("Nhap x,y: ");
		getInput(x, y);
        while (x>y)
        {
            print("Nhap lai x,y: ");
            getInput(x, y);
        }
        
        i: integer;
        sum: integer = 0;
        for (i=x, i<=y, i+1) 
        {
            sum=sum+i*i;
        }
        print("Tong binh phuong cac so tu " + x + " den " + y + " la: " + sum);
        }"""
        expect = """Program([
	FuncDecl(simpleFunc, VoidType, [], None, BlockStmt([VarDecl(x, IntegerType), VarDecl(y, IntegerType), CallStmt(print, StringLit(Nhap x,y: )), CallStmt(getInput, Id(x), Id(y)), WhileStmt(BinExpr(>, Id(x), Id(y)), BlockStmt([CallStmt(print, StringLit(Nhap lai x,y: )), CallStmt(getInput, Id(x), Id(y))])), VarDecl(i, IntegerType), VarDecl(sum, IntegerType, IntegerLit(0)), ForStmt(AssignStmt(Id(i), Id(x)), BinExpr(<=, Id(i), Id(y)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([AssignStmt(Id(sum), BinExpr(+, Id(sum), BinExpr(*, Id(i), Id(i))))])), CallStmt(print, BinExpr(+, BinExpr(+, BinExpr(+, BinExpr(+, BinExpr(+, StringLit(Tong binh phuong cac so tu ), Id(x)), StringLit( den )), Id(y)), StringLit( la: )), Id(sum)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 398))

    def test_more_complex_program95(self):
        """More complex program"""
        input = """simpleFunc: function void () {
            n,i: integer;
            getInput(n);
            while(n==-1){
                print("Nhap lai n: ");
                getInput(n);
            }
            if(n > -100){
                for(i = n, i>= -100, i-1){
                    print(i + "\\n");
                }
            }
            else{
                for(i = n, i <= -100, i+1){
                    print(i + "\\n");
                }
            }
        }"""
        expect = """Program([
	FuncDecl(simpleFunc, VoidType, [], None, BlockStmt([VarDecl(n, IntegerType), VarDecl(i, IntegerType), CallStmt(getInput, Id(n)), WhileStmt(BinExpr(==, Id(n), UnExpr(-, IntegerLit(1))), BlockStmt([CallStmt(print, StringLit(Nhap lai n: )), CallStmt(getInput, Id(n))])), IfStmt(BinExpr(>, Id(n), UnExpr(-, IntegerLit(100))), BlockStmt([ForStmt(AssignStmt(Id(i), Id(n)), BinExpr(>=, Id(i), UnExpr(-, IntegerLit(100))), BinExpr(-, Id(i), IntegerLit(1)), BlockStmt([CallStmt(print, BinExpr(+, Id(i), StringLit(\\n)))]))]), BlockStmt([ForStmt(AssignStmt(Id(i), Id(n)), BinExpr(<=, Id(i), UnExpr(-, IntegerLit(100))), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([CallStmt(print, BinExpr(+, Id(i), StringLit(\\n)))]))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 399))

    def test_more_complex_program96(self):
        """More complex program"""
        input = """istuc: function boolean(x: integer){
            s: integer = 0;
            for (i = 1, i < x, i+1){
                if (x%i == 0) s = s + i;
            }
            if (s==x) return true;
            else return false;
        }"""
        expect = """Program([
	FuncDecl(istuc, BooleanType, [Param(x, IntegerType)], None, BlockStmt([VarDecl(s, IntegerType, IntegerLit(0)), ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<, Id(i), Id(x)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(==, BinExpr(%, Id(x), Id(i)), IntegerLit(0)), AssignStmt(Id(s), BinExpr(+, Id(s), Id(i))))])), IfStmt(BinExpr(==, Id(s), Id(x)), ReturnStmt(BooleanLit(True)), ReturnStmt(BooleanLit(False)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 400))

    def test_more_complex_program97(self):
        """More complex program"""
        input = """
        pow: function float(x: float, y: integer){
            res: float = 1;
            for (i = 1, i <= y, i+1) {
                res = res * x;
            } 
            return res;
        }
        simpleFunc: function void () {
            print(pow(2.0036E-7, 2));
        }"""
        expect = """Program([
	FuncDecl(pow, FloatType, [Param(x, FloatType), Param(y, IntegerType)], None, BlockStmt([VarDecl(res, FloatType, IntegerLit(1)), ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<=, Id(i), Id(y)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([AssignStmt(Id(res), BinExpr(*, Id(res), Id(x)))])), ReturnStmt(Id(res))]))
	FuncDecl(simpleFunc, VoidType, [], None, BlockStmt([CallStmt(print, FuncCall(pow, [FloatLit(2.0036e-07), IntegerLit(2)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 401))

    def test_more_complex_program98(self):
        """More complex program"""
        input = """simpleFunc: function void () {
            x,y,sumEven,sumOdd: integer;
            getInput(x,y);
            sumEven = 0;
            sumOdd = 0;
            for(i = x, i<=y, i+1){
                if(i%2==0) sumEven=sumEven+i;
                else sumOdd=sumOdd+i;
            }
            print("Sum even num from x to y: " + sumEven + "\\n Sum odd num from x to y: " + sumOdd);
        }"""
        expect = """Program([
	FuncDecl(simpleFunc, VoidType, [], None, BlockStmt([VarDecl(x, IntegerType), VarDecl(y, IntegerType), VarDecl(sumEven, IntegerType), VarDecl(sumOdd, IntegerType), CallStmt(getInput, Id(x), Id(y)), AssignStmt(Id(sumEven), IntegerLit(0)), AssignStmt(Id(sumOdd), IntegerLit(0)), ForStmt(AssignStmt(Id(i), Id(x)), BinExpr(<=, Id(i), Id(y)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(==, BinExpr(%, Id(i), IntegerLit(2)), IntegerLit(0)), AssignStmt(Id(sumEven), BinExpr(+, Id(sumEven), Id(i))), AssignStmt(Id(sumOdd), BinExpr(+, Id(sumOdd), Id(i))))])), CallStmt(print, BinExpr(+, BinExpr(+, BinExpr(+, StringLit(Sum even num from x to y: ), Id(sumEven)), StringLit(\\n Sum odd num from x to y: )), Id(sumOdd)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 402))

    def test_more_complex_program99(self):
        """More complex program"""
        input = """simpleFunc: function void () {
            arr: array [10] of integer = {23,4,5,6,15,45,37,21,19,2};      
            for(k=1, k<10, k+1){  
                temp: integer = arr[k];  
                j: integer = k-1;  
                while((j>=0) && (temp <= arr[j])){ 
                    arr[j+1] = arr[j];   
                    j = j-1;  
                }  
                arr[j+1] = temp;  
            }  
            print("Sorted list is \\n");
            for(i=0,i<10,i+1){ 
                print(arr[i] + "\\t"); 
            }  
        }"""
        expect = """Program([
	FuncDecl(simpleFunc, VoidType, [], None, BlockStmt([VarDecl(arr, ArrayType([10], IntegerType), ArrayLit([IntegerLit(23), IntegerLit(4), IntegerLit(5), IntegerLit(6), IntegerLit(15), IntegerLit(45), IntegerLit(37), IntegerLit(21), IntegerLit(19), IntegerLit(2)])), ForStmt(AssignStmt(Id(k), IntegerLit(1)), BinExpr(<, Id(k), IntegerLit(10)), BinExpr(+, Id(k), IntegerLit(1)), BlockStmt([VarDecl(temp, IntegerType, ArrayCell(arr, [Id(k)])), VarDecl(j, IntegerType, BinExpr(-, Id(k), IntegerLit(1))), WhileStmt(BinExpr(&&, BinExpr(>=, Id(j), IntegerLit(0)), BinExpr(<=, Id(temp), ArrayCell(arr, [Id(j)]))), BlockStmt([AssignStmt(ArrayCell(arr, [BinExpr(+, Id(j), IntegerLit(1))]), ArrayCell(arr, [Id(j)])), AssignStmt(Id(j), BinExpr(-, Id(j), IntegerLit(1)))])), AssignStmt(ArrayCell(arr, [BinExpr(+, Id(j), IntegerLit(1))]), Id(temp))])), CallStmt(print, StringLit(Sorted list is \\n)), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(10)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([CallStmt(print, BinExpr(+, ArrayCell(arr, [Id(i)]), StringLit(\\t)))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 403))

    def test_more_complex_program100(self):
        """More complex program"""
        input = """
        selection_sort: function void(arr: array [100] of integer, n: integer) {
            i, j, min_idx: integer;
            for (i = 0, i < n-1, i+1){
                min_idx = i;
                for (j = i+1, j < n, j+1){
                    if (arr[j] < arr[min_idx])
                        min_idx = j;
                    swap(arr[min_idx], arr[i]);
                }
            }
        }
        simpleFunc: function void () {
            arr: array [7] of integer = {92, 71, 84, 33, 11, 65, 40};
            selection_sort(arr, 7);
            printArray(arr);
        }"""
        expect = """Program([
	FuncDecl(selection_sort, VoidType, [Param(arr, ArrayType([100], IntegerType)), Param(n, IntegerType)], None, BlockStmt([VarDecl(i, IntegerType), VarDecl(j, IntegerType), VarDecl(min_idx, IntegerType), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), BinExpr(-, Id(n), IntegerLit(1))), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([AssignStmt(Id(min_idx), Id(i)), ForStmt(AssignStmt(Id(j), BinExpr(+, Id(i), IntegerLit(1))), BinExpr(<, Id(j), Id(n)), BinExpr(+, Id(j), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(<, ArrayCell(arr, [Id(j)]), ArrayCell(arr, [Id(min_idx)])), AssignStmt(Id(min_idx), Id(j))), CallStmt(swap, ArrayCell(arr, [Id(min_idx)]), ArrayCell(arr, [Id(i)]))]))]))]))
	FuncDecl(simpleFunc, VoidType, [], None, BlockStmt([VarDecl(arr, ArrayType([7], IntegerType), ArrayLit([IntegerLit(92), IntegerLit(71), IntegerLit(84), IntegerLit(33), IntegerLit(11), IntegerLit(65), IntegerLit(40)])), CallStmt(selection_sort, Id(arr), IntegerLit(7)), CallStmt(printArray, Id(arr))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 404))


