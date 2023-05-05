import unittest
from TestUtils import TestAST
from AST import *


class ASTGenSuite(unittest.TestCase):
    def test_301(self):
        input = """a, b, c: float = 1.0e3, 0.25E-8, 0.01;"""
        expect = """Program([
	VarDecl(a, FloatType, FloatLit(1000.0))
	VarDecl(b, FloatType, FloatLit(2.5e-09))
	VarDecl(c, FloatType, FloatLit(0.01))
])"""
        self.assertTrue(TestAST.test(input, expect, 301))

    def test_302(self):
        input = """a: integer = 2;"""
        expect = """Program([
	VarDecl(a, IntegerType, IntegerLit(2))
])"""
        self.assertTrue(TestAST.test(input, expect, 302))

    def test_303(self):
        input = """a, b, c, d: string = "Patrick", "Lavon", "Mahomes", "II \\n";"""
        expect = """Program([
	VarDecl(a, StringType, StringLit(Patrick))
	VarDecl(b, StringType, StringLit(Lavon))
	VarDecl(c, StringType, StringLit(Mahomes))
	VarDecl(d, StringType, StringLit(II \\n))
])"""
        self.assertTrue(TestAST.test(input, expect, 303))

    def test_304(self):
        input = """PPL, y11, _z5_87: auto = !3, 2-a, "String \\t" :: "String again \\b";"""
        expect = """Program([
	VarDecl(PPL, AutoType, UnExpr(!, IntegerLit(3)))
	VarDecl(y11, AutoType, BinExpr(-, IntegerLit(2), Id(a)))
	VarDecl(_z5_87, AutoType, BinExpr(::, StringLit(String \\t), StringLit(String again \\b)))
])"""
        self.assertTrue(TestAST.test(input, expect, 304))

    def test_305(self):
        input = """X, y, z: boolean = -3 || "A string", 2 && 12, 34 && true;"""
        expect = """Program([
	VarDecl(X, BooleanType, BinExpr(||, UnExpr(-, IntegerLit(3)), StringLit(A string)))
	VarDecl(y, BooleanType, BinExpr(&&, IntegerLit(2), IntegerLit(12)))
	VarDecl(z, BooleanType, BinExpr(&&, IntegerLit(34), BooleanLit(True)))
])"""
        self.assertTrue(TestAST.test(input, expect, 305))

    def test_306(self):
        input = """_cbd, b, c: array[2] of integer = {1, 2}, {3, 4}, {5, 6};"""
        expect = """Program([
	VarDecl(_cbd, ArrayType([2], IntegerType), ArrayLit([IntegerLit(1), IntegerLit(2)]))
	VarDecl(b, ArrayType([2], IntegerType), ArrayLit([IntegerLit(3), IntegerLit(4)]))
	VarDecl(c, ArrayType([2], IntegerType), ArrayLit([IntegerLit(5), IntegerLit(6)]))
])"""
        self.assertTrue(TestAST.test(input, expect, 306))

    def test_307(self):
        input = """tNhP_222: array[2] of string = {"Did u watch da show? \\b", "Already answered \\t"};"""
        expect = """Program([
	VarDecl(tNhP_222, ArrayType([2], StringType), ArrayLit([StringLit(Did u watch da show? \\b), StringLit(Already answered \\t)]))
])"""
        self.assertTrue(TestAST.test(input, expect, 307))

    def test_308(self):
        input = """isTrue, isFalse, isGreaterThanZero: boolean = true, false, !(3 + (-2) < 0);"""
        expect = """Program([
	VarDecl(isTrue, BooleanType, BooleanLit(True))
	VarDecl(isFalse, BooleanType, BooleanLit(False))
	VarDecl(isGreaterThanZero, BooleanType, UnExpr(!, BinExpr(<, BinExpr(+, IntegerLit(3), UnExpr(-, IntegerLit(2))), IntegerLit(0))))
])"""
        self.assertTrue(TestAST.test(input, expect, 308))

    def test_309(self):
        input = """a, b, c: integer = 2_02_221, 3, 4;"""
        expect = """Program([
	VarDecl(a, IntegerType, IntegerLit(202221))
	VarDecl(b, IntegerType, IntegerLit(3))
	VarDecl(c, IntegerType, IntegerLit(4))
])"""
        self.assertTrue(TestAST.test(input, expect, 309))

    def test_310(self):
        input = """a, b, c: float;"""
        expect = """Program([
	VarDecl(a, FloatType)
	VarDecl(b, FloatType)
	VarDecl(c, FloatType)
])"""
        self.assertTrue(TestAST.test(input, expect, 310))

    def test_311(self):
        input = """x, y: boolean = checkFibo(2), false || ppl < 10;"""
        expect = """Program([
	VarDecl(x, BooleanType, FuncCall(checkFibo, [IntegerLit(2)]))
	VarDecl(y, BooleanType, BinExpr(<, BinExpr(||, BooleanLit(False), Id(ppl)), IntegerLit(10)))
])"""
        self.assertTrue(TestAST.test(input, expect, 311))

    def test_312(self):
        input = """a: array[2, 4] of string;"""
        expect = """Program([
	VarDecl(a, ArrayType([2, 4], StringType))
])"""
        self.assertTrue(TestAST.test(input, expect, 312))

    def test_313(self):
        input = """_23x12: array[4] of integer;"""
        expect = """Program([
	VarDecl(_23x12, ArrayType([4], IntegerType))
])"""
        self.assertTrue(TestAST.test(input, expect, 313))

    def test_314(self):
        input = """_12, abc: array[2, 4] of integer;"""
        expect = """Program([
	VarDecl(_12, ArrayType([2, 4], IntegerType))
	VarDecl(abc, ArrayType([2, 4], IntegerType))
])"""
        self.assertTrue(TestAST.test(input, expect, 314))

    def test_315(self):
        input = """a: integer = 12_0182 + 32 / 46 * 20;"""
        expect = """Program([
	VarDecl(a, IntegerType, BinExpr(+, IntegerLit(120182), BinExpr(*, BinExpr(/, IntegerLit(32), IntegerLit(46)), IntegerLit(20))))
])"""
        self.assertTrue(TestAST.test(input, expect, 315))

    def test_316(self):
        input = """a: integer = -2+3*54;
fact: function integer(out n: auto) {}"""
        expect = """Program([
	VarDecl(a, IntegerType, BinExpr(+, UnExpr(-, IntegerLit(2)), BinExpr(*, IntegerLit(3), IntegerLit(54))))
	FuncDecl(fact, IntegerType, [OutParam(n, AutoType)], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 316))

    def test_317(self):
        input = """a: array[3] of integer = {2, 3, 4};
fact: function integer(inherit n: integer) {}"""
        expect = """Program([
	VarDecl(a, ArrayType([3], IntegerType), ArrayLit([IntegerLit(2), IntegerLit(3), IntegerLit(4)]))
	FuncDecl(fact, IntegerType, [InheritParam(n, IntegerType)], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 317))

    def test_318(self):
        input = """fact: function integer(n: string, s: boolean, inherit t: auto) {}"""
        expect = """Program([
	FuncDecl(fact, IntegerType, [Param(n, StringType), Param(s, BooleanType), InheritParam(t, AutoType)], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 318))

    def test_319(self):
        input = """func: function integer() {
    result = calc(2, 3, "+");
    printInteger(result);
}"""
        expect = """Program([
	FuncDecl(func, IntegerType, [], None, BlockStmt([AssignStmt(Id(result), FuncCall(calc, [IntegerLit(2), IntegerLit(3), StringLit(+)])), CallStmt(printInteger, Id(result))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 319))

    def test_320(self):
        input = """fact: function integer(inherit x: boolean, out y: integer) inherit fact0 {}"""
        expect = """Program([
	FuncDecl(fact, IntegerType, [InheritParam(x, BooleanType), OutParam(y, IntegerType)], fact0, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 320))

    def test_321(self):
        input = """fact: function integer() {}"""
        expect = """Program([
	FuncDecl(fact, IntegerType, [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 321))

    def test_322(self):
        input = """toBool: function boolean(n: string) {
    return n == "true";
}"""
        expect = """Program([
	FuncDecl(toBool, BooleanType, [Param(n, StringType)], None, BlockStmt([ReturnStmt(BinExpr(==, Id(n), StringLit(true)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 322))

    def test_323(self):
        input = """fact: function array[2_023] of integer() inherit fact1 {}"""
        expect = """Program([
	FuncDecl(fact, ArrayType([2023], IntegerType), [], fact1, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 323))

    def test_324(self):
        input = """fact: function integer(n: integer) {}"""
        expect = """Program([
	FuncDecl(fact, IntegerType, [Param(n, IntegerType)], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 324))

    def test_325(self):
        input = """fact: function integer(out n: string) {}"""
        expect = """Program([
	FuncDecl(fact, IntegerType, [OutParam(n, StringType)], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 325))

    def test_326(self):
        input = """main: function void() { x: float = 0.e-5; }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(x, FloatType, FloatLit(0.0))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 326))

    def test_327(self):
        input = """main: function void() {
    printString("Hello :v");
}"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(printString, StringLit(Hello :v))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 327))

    def test_328(self):
        input = """x: boolean = true;
main: function void() { printBoolean(x); }"""
        expect = """Program([
	VarDecl(x, BooleanType, BooleanLit(True))
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(printBoolean, Id(x))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 328))

    def test_329(self):
        input = """bolean: function boolean() inherit bool {}"""
        expect = """Program([
	FuncDecl(bolean, BooleanType, [], bool, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 329))

    def test_330(self):
        input = """main: function void(args: array[2] of integer) {
    printInteger(args[1]);
    if (args[2] == 12) printString("Tom Brady");
}"""
        expect = """Program([
	FuncDecl(main, VoidType, [Param(args, ArrayType([2], IntegerType))], None, BlockStmt([CallStmt(printInteger, ArrayCell(args, [IntegerLit(1)])), IfStmt(BinExpr(==, ArrayCell(args, [IntegerLit(2)]), IntegerLit(12)), CallStmt(printString, StringLit(Tom Brady)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 330))

    def test_331(self):
        input = """a: integer = -2;"""
        expect = """Program([
	VarDecl(a, IntegerType, UnExpr(-, IntegerLit(2)))
])"""
        self.assertTrue(TestAST.test(input, expect, 331))

    def test_332(self):
        input = """main: function void() { fact(2+3_02, someInt, anotherInt / 2); }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(fact, BinExpr(+, IntegerLit(2), IntegerLit(302)), Id(someInt), BinExpr(/, Id(anotherInt), IntegerLit(2)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 332))

    def test_333(self):
        input = """main: function void() { fact(randomInt(0, 12, 4), "234", true && ("bully" == "tnbd")); }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(fact, FuncCall(randomInt, [IntegerLit(0), IntegerLit(12), IntegerLit(4)]), StringLit(234), BinExpr(&&, BooleanLit(True), BinExpr(==, StringLit(bully), StringLit(tnbd))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 333))

    def test_334(self):
        input = """main: function void() { fact(1, 2_23, 3.e5); }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(fact, IntegerLit(1), IntegerLit(223), FloatLit(300000.0))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 334))

    def test_335(self):
        input = """main: function void() { fact(); }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(fact, )]))
])"""
        self.assertTrue(TestAST.test(input, expect, 335))

    def test_336(self):
        input = """main: function void() { a: string; a = "A random string"; }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, StringType), AssignStmt(Id(a), StringLit(A random string))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 336))

    def test_337(self):
        input = """main: function void() { a: string; a = "A string \\t"; }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, StringType), AssignStmt(Id(a), StringLit(A string \\t))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 337))

    def test_338(self):
        input = """main: function void() {
    if(a != 2) {} else {}
}"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(!=, Id(a), IntegerLit(2)), BlockStmt([]), BlockStmt([]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 338))

    def test_339(self):
        input = """main: function void() {
    if(a && 2) printString("What" :: "the **** \\t");
}"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(&&, Id(a), IntegerLit(2)), CallStmt(printString, BinExpr(::, StringLit(What), StringLit(the **** \\t))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 339))

    def test_340(self):
        input = """ain: function void() {
    if(a + 2 == 3) return true;
}"""
        expect = """Program([
	FuncDecl(ain, VoidType, [], None, BlockStmt([IfStmt(BinExpr(==, BinExpr(+, Id(a), IntegerLit(2)), IntegerLit(3)), ReturnStmt(BooleanLit(True)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 340))

    def test_341(self):
        input = """main: function void() {
    if(qbv >= 7) messi();
    else ronaldo("siuuuuu");
}"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(>=, Id(qbv), IntegerLit(7)), CallStmt(messi, ), CallStmt(ronaldo, StringLit(siuuuuu)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 341))

    def test_342(self):
        input = """main: function void() {
    if(true) {
        a = a + 2;
        b = b || false;
    } else {
        func_aaa();
    }
}"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BooleanLit(True), BlockStmt([AssignStmt(Id(a), BinExpr(+, Id(a), IntegerLit(2))), AssignStmt(Id(b), BinExpr(||, Id(b), BooleanLit(False)))]), BlockStmt([CallStmt(func_aaa, )]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 342))

    def test_343(self):
        input = """main: function void() {
    if(true) {
        a = a + 2;
        b = b || false;
    } else {
        a = b :: c;
        b = toString("I don\\'t know what I\\'m doing");    
    }
}"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BooleanLit(True), BlockStmt([AssignStmt(Id(a), BinExpr(+, Id(a), IntegerLit(2))), AssignStmt(Id(b), BinExpr(||, Id(b), BooleanLit(False)))]), BlockStmt([AssignStmt(Id(a), BinExpr(::, Id(b), Id(c))), AssignStmt(Id(b), FuncCall(toString, [StringLit(I don\\'t know what I\\'m doing)]))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 343))

    def test_344(self):
        input = """main: function void() {
    if(true) a = 2;
    else continue;
}"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BooleanLit(True), AssignStmt(Id(a), IntegerLit(2)), ContinueStmt())]))
])"""
        self.assertTrue(TestAST.test(input, expect, 344))

    def test_345(self):
        input = """main: function void() {
    if(a == 2)
        if(b == 3) siuuuu();
        else boooo("10 minutes to submit question 1");
    else b = false;
}"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(==, Id(a), IntegerLit(2)), IfStmt(BinExpr(==, Id(b), IntegerLit(3)), CallStmt(siuuuu, ), CallStmt(boooo, StringLit(10 minutes to submit question 1))), AssignStmt(Id(b), BooleanLit(False)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 345))

    def test_346(self):
        input = """notMain: function integer() {
    i: integer;
    for(i = 23 * ab, i < 23, i + 1) {
        writeInt(i);
    }
    return i * 2;
}"""
        expect = """Program([
	FuncDecl(notMain, IntegerType, [], None, BlockStmt([VarDecl(i, IntegerType), ForStmt(AssignStmt(Id(i), BinExpr(*, IntegerLit(23), Id(ab))), BinExpr(<, Id(i), IntegerLit(23)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([CallStmt(writeInt, Id(i))])), ReturnStmt(BinExpr(*, Id(i), IntegerLit(2)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 346))

    def test_347(self):
        input = """main: function void() {
    i: integer;
    for(a[23] = sb("lvii \\b"), a[23] != 3, a[23] / 4) {
        kansasCity("Champs");
        a = a + 3;
        if(a < 3) break;
    }
}"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(i, IntegerType), ForStmt(AssignStmt(ArrayCell(a, [IntegerLit(23)]), FuncCall(sb, [StringLit(lvii \\b)])), BinExpr(!=, ArrayCell(a, [IntegerLit(23)]), IntegerLit(3)), BinExpr(/, ArrayCell(a, [IntegerLit(23)]), IntegerLit(4)), BlockStmt([CallStmt(kansasCity, StringLit(Champs)), AssignStmt(Id(a), BinExpr(+, Id(a), IntegerLit(3))), IfStmt(BinExpr(<, Id(a), IntegerLit(3)), BreakStmt())]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 347))

    def test_348(self):
        input = """main: function void() inherit anotherMain {
    i: integer;
    for(i = a && 3, i != 3, i / 4) {
        phillyEagles("Fly Eagles Fly!");
        a = a - 1;
        if(a < 3) continue;
    }
}"""
        expect = """Program([
	FuncDecl(main, VoidType, [], anotherMain, BlockStmt([VarDecl(i, IntegerType), ForStmt(AssignStmt(Id(i), BinExpr(&&, Id(a), IntegerLit(3))), BinExpr(!=, Id(i), IntegerLit(3)), BinExpr(/, Id(i), IntegerLit(4)), BlockStmt([CallStmt(phillyEagles, StringLit(Fly Eagles Fly!)), AssignStmt(Id(a), BinExpr(-, Id(a), IntegerLit(1))), IfStmt(BinExpr(<, Id(a), IntegerLit(3)), ContinueStmt())]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 348))

    def test_349(self):
        input = """main: function void() {
    i: integer;
    for(i = a && 3, i != 3, i / 4) {
        kansasCity("Champs");
        a = a + 3;
        if(a < 3) return;
    }
}"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(i, IntegerType), ForStmt(AssignStmt(Id(i), BinExpr(&&, Id(a), IntegerLit(3))), BinExpr(!=, Id(i), IntegerLit(3)), BinExpr(/, Id(i), IntegerLit(4)), BlockStmt([CallStmt(kansasCity, StringLit(Champs)), AssignStmt(Id(a), BinExpr(+, Id(a), IntegerLit(3))), IfStmt(BinExpr(<, Id(a), IntegerLit(3)), ReturnStmt())]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 349))

    def test_350(self):
        input = """main: function void() {
    i: integer;
    for(i = a * 3, i != 3, i / 4) {
        kansasCity("Champs");
        a = a + 3;
        if(a < 3) break;
    }
}"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(i, IntegerType), ForStmt(AssignStmt(Id(i), BinExpr(*, Id(a), IntegerLit(3))), BinExpr(!=, Id(i), IntegerLit(3)), BinExpr(/, Id(i), IntegerLit(4)), BlockStmt([CallStmt(kansasCity, StringLit(Champs)), AssignStmt(Id(a), BinExpr(+, Id(a), IntegerLit(3))), IfStmt(BinExpr(<, Id(a), IntegerLit(3)), BreakStmt())]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 350))

    def test_351(self):
        input = """main: function void() {
    i: integer;
    for(i = a - 3 * (2_029 - 10_11), i != 3, i / 4) {
        kansasCity("Champs");
        a = a + 3;
        if(a < 3) break;
    }
}"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(i, IntegerType), ForStmt(AssignStmt(Id(i), BinExpr(-, Id(a), BinExpr(*, IntegerLit(3), BinExpr(-, IntegerLit(2029), IntegerLit(1011))))), BinExpr(!=, Id(i), IntegerLit(3)), BinExpr(/, Id(i), IntegerLit(4)), BlockStmt([CallStmt(kansasCity, StringLit(Champs)), AssignStmt(Id(a), BinExpr(+, Id(a), IntegerLit(3))), IfStmt(BinExpr(<, Id(a), IntegerLit(3)), BreakStmt())]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 351))

    def test_352(self):
        input = """main: function void() {
    i: integer;
    for(i = a, i <= 3, i / 4) {
        notAuto("Champs");
        a = a + 3;
        if(a < 3) break;
    }
}"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(i, IntegerType), ForStmt(AssignStmt(Id(i), Id(a)), BinExpr(<=, Id(i), IntegerLit(3)), BinExpr(/, Id(i), IntegerLit(4)), BlockStmt([CallStmt(notAuto, StringLit(Champs)), AssignStmt(Id(a), BinExpr(+, Id(a), IntegerLit(3))), IfStmt(BinExpr(<, Id(a), IntegerLit(3)), BreakStmt())]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 352))

    def test_353(self):
        input = """main: function void() {
    i: integer;
    for(i = a + 2, i >= 2, i / 4) {
        kansasCity("Champs");
        a = a + 3;
        if(a < 3) break;
    }
}"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(i, IntegerType), ForStmt(AssignStmt(Id(i), BinExpr(+, Id(a), IntegerLit(2))), BinExpr(>=, Id(i), IntegerLit(2)), BinExpr(/, Id(i), IntegerLit(4)), BlockStmt([CallStmt(kansasCity, StringLit(Champs)), AssignStmt(Id(a), BinExpr(+, Id(a), IntegerLit(3))), IfStmt(BinExpr(<, Id(a), IntegerLit(3)), BreakStmt())]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 353))

    def test_354(self):
        input = """main: function void() {
    i: integer;
    for(i = 1, i < 3, i + 1) {
        kansasCity("Champs");
        a = a + 3 <= 3;
        j: integer;
        for(j = 0.E3, pc[23], 23 + j) a = a[3] - 2 :: 1;
    }
}"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(i, IntegerType), ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<, Id(i), IntegerLit(3)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([CallStmt(kansasCity, StringLit(Champs)), AssignStmt(Id(a), BinExpr(<=, BinExpr(+, Id(a), IntegerLit(3)), IntegerLit(3))), VarDecl(j, IntegerType), ForStmt(AssignStmt(Id(j), FloatLit(0.0)), ArrayCell(pc, [IntegerLit(23)]), BinExpr(+, IntegerLit(23), Id(j)), AssignStmt(Id(a), BinExpr(::, BinExpr(-, ArrayCell(a, [IntegerLit(3)]), IntegerLit(2)), IntegerLit(1))))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 354))

    def test_355(self):
        input = """main: function void() {
    i: integer;
    for(i = 1, i < 3, i + 1) {
        kansasCity("Champs");
        arr[i] = arr[i] + i;
    }
}"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(i, IntegerType), ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<, Id(i), IntegerLit(3)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([CallStmt(kansasCity, StringLit(Champs)), AssignStmt(ArrayCell(arr, [Id(i)]), BinExpr(+, ArrayCell(arr, [Id(i)]), Id(i)))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 355))

    def test_356(self):
        input = """add: function integer(a: integer, b: integer) inherit addAgain { return a+b; }
main: function void() {
    while(1 < 3) add(a, 3);
}"""
        expect = """Program([
	FuncDecl(add, IntegerType, [Param(a, IntegerType), Param(b, IntegerType)], addAgain, BlockStmt([ReturnStmt(BinExpr(+, Id(a), Id(b)))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([WhileStmt(BinExpr(<, IntegerLit(1), IntegerLit(3)), CallStmt(add, Id(a), IntegerLit(3)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 356))

    def test_357(self):
        input = """main: function void() {
    while(a < 3) { a = a+1; }
}"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([WhileStmt(BinExpr(<, Id(a), IntegerLit(3)), BlockStmt([AssignStmt(Id(a), BinExpr(+, Id(a), IntegerLit(1)))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 357))

    def test_358(self):
        input = """main: function void() {
    while(a < b) { a = b /  2 - 3 + 4; }
}"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([WhileStmt(BinExpr(<, Id(a), Id(b)), BlockStmt([AssignStmt(Id(a), BinExpr(+, BinExpr(-, BinExpr(/, Id(b), IntegerLit(2)), IntegerLit(3)), IntegerLit(4)))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 358))

    def test_359(self):
        input = """main: function void() {
    while(a < 19) 
        for(i = 100, i > 5, i - 2)
            if(i > 3) printInt(i);
}"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([WhileStmt(BinExpr(<, Id(a), IntegerLit(19)), ForStmt(AssignStmt(Id(i), IntegerLit(100)), BinExpr(>, Id(i), IntegerLit(5)), BinExpr(-, Id(i), IntegerLit(2)), IfStmt(BinExpr(>, Id(i), IntegerLit(3)), CallStmt(printInt, Id(i)))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 359))

    def test_360(self):
        input = """main: function void() {
    while(a < 19) 
        randomFunc(i == 100, i > 5, i - 2);
}"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([WhileStmt(BinExpr(<, Id(a), IntegerLit(19)), CallStmt(randomFunc, BinExpr(==, Id(i), IntegerLit(100)), BinExpr(>, Id(i), IntegerLit(5)), BinExpr(-, Id(i), IntegerLit(2))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 360))

    def test_361(self):
        input = """main: function void() {
    while((i == i) && (i == i)) 
        randomFunc(100, i > 5, i - 2);
}"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([WhileStmt(BinExpr(&&, BinExpr(==, Id(i), Id(i)), BinExpr(==, Id(i), Id(i))), CallStmt(randomFunc, IntegerLit(100), BinExpr(>, Id(i), IntegerLit(5)), BinExpr(-, Id(i), IntegerLit(2))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 361))

    def test_362(self):
        input = """main: function void() {
    while(i >= 1) 
        for(a = i && i + i && i, a < 0, a+1)
            randomFunc(100, i > 5, i - 2);
}"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([WhileStmt(BinExpr(>=, Id(i), IntegerLit(1)), ForStmt(AssignStmt(Id(a), BinExpr(&&, BinExpr(&&, Id(i), BinExpr(+, Id(i), Id(i))), Id(i))), BinExpr(<, Id(a), IntegerLit(0)), BinExpr(+, Id(a), IntegerLit(1)), CallStmt(randomFunc, IntegerLit(100), BinExpr(>, Id(i), IntegerLit(5)), BinExpr(-, Id(i), IntegerLit(2)))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 362))

    def test_363(self):
        input = """main: function void() {
    while((i == 4) && (a < 2)) {
        block();
        if(a == 1_002) return;
    }
}"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([WhileStmt(BinExpr(&&, BinExpr(==, Id(i), IntegerLit(4)), BinExpr(<, Id(a), IntegerLit(2))), BlockStmt([CallStmt(block, ), IfStmt(BinExpr(==, Id(a), IntegerLit(1002)), ReturnStmt())]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 363))

    def test_364(self):
        input = """main: function void() {
    while(a < 2) {
        a = a || fact(2) * 3 && b < 3;
        b = "Hello" :: (name :: " and welcome to LOLand :))) \\t");
    }
}"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([WhileStmt(BinExpr(<, Id(a), IntegerLit(2)), BlockStmt([AssignStmt(Id(a), BinExpr(<, BinExpr(&&, BinExpr(||, Id(a), BinExpr(*, FuncCall(fact, [IntegerLit(2)]), IntegerLit(3))), Id(b)), IntegerLit(3))), AssignStmt(Id(b), BinExpr(::, StringLit(Hello), BinExpr(::, Id(name), StringLit( and welcome to LOLand :))) \\t))))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 364))

    def test_365(self):
        input = """main: function void() {
    while(a < 2) {
        a = 1_023 + {1.0002, 1.e4 < _Constant} || 12 - 54 * 1.e+03 && "String \\t" :: "String again \\b";
    }
}"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([WhileStmt(BinExpr(<, Id(a), IntegerLit(2)), BlockStmt([AssignStmt(Id(a), BinExpr(::, BinExpr(&&, BinExpr(||, BinExpr(+, IntegerLit(1023), ArrayLit([FloatLit(1.0002), BinExpr(<, FloatLit(10000.0), Id(_Constant))])), BinExpr(-, IntegerLit(12), BinExpr(*, IntegerLit(54), FloatLit(1000.0)))), StringLit(String \\t)), StringLit(String again \\b)))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 365))

    def test_366(self):
        input = """main: function void() {
    do { toint("Three"); }
    while(i < 2);
}"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([DoWhileStmt(BinExpr(<, Id(i), IntegerLit(2)), BlockStmt([CallStmt(toint, StringLit(Three))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 366))

    def test_367(self):
        input = """main: function void() {
    do {
        continue;
        fact(foo("String 1" :: ("S???~!!!! hihi \\b" :: "Awkward string lol :>>> :v ~~??? -.-")));
    }
    while(__random == true);
}"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([DoWhileStmt(BinExpr(==, Id(__random), BooleanLit(True)), BlockStmt([ContinueStmt(), CallStmt(fact, FuncCall(foo, [BinExpr(::, StringLit(String 1), BinExpr(::, StringLit(S???~!!!! hihi \\b), StringLit(Awkward string lol :>>> :v ~~??? -.-)))]))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 367))

    def test_368(self):
        input = """main: function void(inherit out m: integer) {
    do {
        fun(23, 1.54E-2);
    }
    while (true);
}"""
        expect = """Program([
	FuncDecl(main, VoidType, [InheritOutParam(m, IntegerType)], None, BlockStmt([DoWhileStmt(BooleanLit(True), BlockStmt([CallStmt(fun, IntegerLit(23), FloatLit(0.0154))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 368))

    def test_369(self):
        input = """main: function void() {
    do {
        x = increase(1, 10);
    }
    while (true);
}"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([DoWhileStmt(BooleanLit(True), BlockStmt([AssignStmt(Id(x), FuncCall(increase, [IntegerLit(1), IntegerLit(10)]))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 369))

    def test_370(self):
        input = """a: float = 12.5E+007 - "Hello sir \\n" && 2_44;
main: function void() {
    do 
        { a = a / 3 + 2 * fuc(__32, 1.43e7, true == "A string \\b") + 23; }
    while (a > 0);
}"""
        expect = """Program([
	VarDecl(a, FloatType, BinExpr(&&, BinExpr(-, FloatLit(125000000.0), StringLit(Hello sir \\n)), IntegerLit(244)))
	FuncDecl(main, VoidType, [], None, BlockStmt([DoWhileStmt(BinExpr(>, Id(a), IntegerLit(0)), BlockStmt([AssignStmt(Id(a), BinExpr(+, BinExpr(+, BinExpr(/, Id(a), IntegerLit(3)), BinExpr(*, IntegerLit(2), FuncCall(fuc, [Id(__32), FloatLit(14300000.0), BinExpr(==, BooleanLit(True), StringLit(A string \\b))]))), IntegerLit(23)))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 370))

    def test_371(self):
        input = """main: function void() { do {} while(true); }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([DoWhileStmt(BooleanLit(True), BlockStmt([]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 371))

    def test_372(self):
        input = """main: function void() { do { a = a + 1; } while((a >= 2) || (a <= 18)); }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([DoWhileStmt(BinExpr(||, BinExpr(>=, Id(a), IntegerLit(2)), BinExpr(<=, Id(a), IntegerLit(18))), BlockStmt([AssignStmt(Id(a), BinExpr(+, Id(a), IntegerLit(1)))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 372))

    def test_373(self):
        input = """main: function void() {
    do {
        if(a + 3 < 90.) randomFunc("I dunno \\b");
        else return true;
        a = a + 3;
    }
    while(a < 25);
}"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([DoWhileStmt(BinExpr(<, Id(a), IntegerLit(25)), BlockStmt([IfStmt(BinExpr(<, BinExpr(+, Id(a), IntegerLit(3)), FloatLit(90.0)), CallStmt(randomFunc, StringLit(I dunno \\b)), ReturnStmt(BooleanLit(True))), AssignStmt(Id(a), BinExpr(+, Id(a), IntegerLit(3)))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 373))

    def test_374(self):
        input = """a: array[2_33, 4] of float = {1_442.25e+0071};
main: function void() {
    do {
        a: integer = 3;
        a = a + 2;
        continue;
    }
    while(a < 3);
}"""
        expect = """Program([
	VarDecl(a, ArrayType([233, 4], FloatType), ArrayLit([FloatLit(1.44225e+74)]))
	FuncDecl(main, VoidType, [], None, BlockStmt([DoWhileStmt(BinExpr(<, Id(a), IntegerLit(3)), BlockStmt([VarDecl(a, IntegerType, IntegerLit(3)), AssignStmt(Id(a), BinExpr(+, Id(a), IntegerLit(2))), ContinueStmt()]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 374))

    def test_375(self):
        input = """__funFunc: function integer(inherit a: integer, out _221: boolean) {
    do {
        func();
    }
    while(i < 3);
}
main: function void() { __funFunc(); }"""
        expect = """Program([
	FuncDecl(__funFunc, IntegerType, [InheritParam(a, IntegerType), OutParam(_221, BooleanType)], None, BlockStmt([DoWhileStmt(BinExpr(<, Id(i), IntegerLit(3)), BlockStmt([CallStmt(func, )]))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(__funFunc, )]))
])"""
        self.assertTrue(TestAST.test(input, expect, 375))

    def test_376(self):
        input = """main: function void() { a[1] = "A string \\t"; }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(ArrayCell(a, [IntegerLit(1)]), StringLit(A string \\t))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 376))

    def test_377(self):
        input = """main: function void() { __arr[23] = "Another random string \\t"; }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(ArrayCell(__arr, [IntegerLit(23)]), StringLit(Another random string \\t))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 377))

    def test_378(self):
        input = """main: function void() { 
    __array[array_a[23] - 2 * b] = "A string \\t";
    arr[a[12]] = 24; 
}"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(ArrayCell(__array, [BinExpr(-, ArrayCell(array_a, [IntegerLit(23)]), BinExpr(*, IntegerLit(2), Id(b)))]), StringLit(A string \\t)), AssignStmt(ArrayCell(arr, [ArrayCell(a, [IntegerLit(12)])]), IntegerLit(24))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 378))

    def test_379(self):
        input = """main: function void() { 
    a = arr[len(("String lmao" :: "Concat tis \\f") :: "Eeeee lol")]; 
}"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(a), ArrayCell(arr, [FuncCall(len, [BinExpr(::, BinExpr(::, StringLit(String lmao), StringLit(Concat tis \\f)), StringLit(Eeeee lol))])]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 379))

    def test_380(self):
        input = """main: function void() { c = a[b[1]] + b[a[0]]; }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(c), BinExpr(+, ArrayCell(a, [ArrayCell(b, [IntegerLit(1)])]), ArrayCell(b, [ArrayCell(a, [IntegerLit(0)])])))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 380))

    def test_381(self):
        input = """main: function void() { a = {2, 3_44, 5}; }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(a), ArrayLit([IntegerLit(2), IntegerLit(344), IntegerLit(5)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 381))

    def test_382(self):
        input = """main: function void() { a = (a :: "34") :: _randomF12(); }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(a), BinExpr(::, BinExpr(::, Id(a), StringLit(34)), FuncCall(_randomF12, [])))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 382))

    def test_383(self):
        input = """main: function void() { a = 1_021.E+832 + a_12 || arr[23]; }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(a), BinExpr(||, BinExpr(+, FloatLit(inf), Id(a_12)), ArrayCell(arr, [IntegerLit(23)])))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 383))

    def test_384(self):
        input = """main: function void() { a = a - 3 * 12 || b % 3e2 / len("Siuuuuuuu \\b"); }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(a), BinExpr(||, BinExpr(-, Id(a), BinExpr(*, IntegerLit(3), IntegerLit(12))), BinExpr(/, BinExpr(%, Id(b), FloatLit(300.0)), FuncCall(len, [StringLit(Siuuuuuuu \\b)]))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 384))

    def test_385(self):
        input = """main: function void() { lhs = "Pi pi eo" :: "0, 4" && -33_9402.21 || {n, h, d}; }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(lhs), BinExpr(::, StringLit(Pi pi eo), BinExpr(||, BinExpr(&&, StringLit(0, 4), UnExpr(-, FloatLit(339402.21))), ArrayLit([Id(n), Id(h), Id(d)]))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 385))

    def test_386(self):
        input = """randomFunc___23: function void() { a = "A string \\t"; }"""
        expect = """Program([
	FuncDecl(randomFunc___23, VoidType, [], None, BlockStmt([AssignStmt(Id(a), StringLit(A string \\t))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 386))

    def test_387(self):
        input = """__32Func: function void(_ab6: string) { a = "A string \\t"; }"""
        expect = """Program([
	FuncDecl(__32Func, VoidType, [Param(_ab6, StringType)], None, BlockStmt([AssignStmt(Id(a), StringLit(A string \\t))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 387))

    def test_388(self):
        input = """fact: function void(inherit out a: boolean) { a = "A string \\t"; }"""
        expect = """Program([
	FuncDecl(fact, VoidType, [InheritOutParam(a, BooleanType)], None, BlockStmt([AssignStmt(Id(a), StringLit(A string \\t))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 388))

    def test_389(self):
        input = """mahomies_15: function void(inherit out qb: integer) { a = "NFL 2022 MVP and SB LVII champs \\t"; }"""
        expect = """Program([
	FuncDecl(mahomies_15, VoidType, [InheritOutParam(qb, IntegerType)], None, BlockStmt([AssignStmt(Id(a), StringLit(NFL 2022 MVP and SB LVII champs \\t))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 389))

    def test_390(self):
        input = """chiefs_champs: function void(out a: integer, inherit b: float, c: string) inherit rams2021 { a = "A string \\t"; }"""
        expect = """Program([
	FuncDecl(chiefs_champs, VoidType, [OutParam(a, IntegerType), InheritParam(b, FloatType), Param(c, StringType)], rams2021, BlockStmt([AssignStmt(Id(a), StringLit(A string \\t))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 390))

    def test_391(self):
        input = """main: function void() {
    N: integer = 1000;
    check: array[1001] of boolean;

    // Initialize [2...N] all being prime numbers
    i: integer;
    for (i = 2, i <= N, i+1) check[i] = true;


    // Sieve of Eratosthenes 
    for (i = 2, i <= N, i+1) {
        if (check[i] == true) {
            for (j = 2 * i, j <= N, j + i) {
                check[j] = false;
            }
        }
    }

    // Print all prime numbers
    i = 2;
    while (i <= N) {
        if (check[i] == true) {
            printInteger(i);
        }
        i = i+1;
    }
}"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(N, IntegerType, IntegerLit(1000)), VarDecl(check, ArrayType([1001], BooleanType)), VarDecl(i, IntegerType), ForStmt(AssignStmt(Id(i), IntegerLit(2)), BinExpr(<=, Id(i), Id(N)), BinExpr(+, Id(i), IntegerLit(1)), AssignStmt(ArrayCell(check, [Id(i)]), BooleanLit(True))), ForStmt(AssignStmt(Id(i), IntegerLit(2)), BinExpr(<=, Id(i), Id(N)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(==, ArrayCell(check, [Id(i)]), BooleanLit(True)), BlockStmt([ForStmt(AssignStmt(Id(j), BinExpr(*, IntegerLit(2), Id(i))), BinExpr(<=, Id(j), Id(N)), BinExpr(+, Id(j), Id(i)), BlockStmt([AssignStmt(ArrayCell(check, [Id(j)]), BooleanLit(False))]))]))])), AssignStmt(Id(i), IntegerLit(2)), WhileStmt(BinExpr(<=, Id(i), Id(N)), BlockStmt([IfStmt(BinExpr(==, ArrayCell(check, [Id(i)]), BooleanLit(True)), BlockStmt([CallStmt(printInteger, Id(i))])), AssignStmt(Id(i), BinExpr(+, Id(i), IntegerLit(1)))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 391))

    def test_392(self):
        input = """factorial: function integer(n: integer) {
    i: integer;
    fact: integer = 1;
    for(i = 1, i <= n, i+1) fact = fact * i;
    return fact;
}

a: integer = 5_00;

main: function void() {
    i: integer;
    while(i <= a) {
        res: integer = factorial(i);
        printInteger(i);
        i = i+1;
    }
}"""
        expect = """Program([
	FuncDecl(factorial, IntegerType, [Param(n, IntegerType)], None, BlockStmt([VarDecl(i, IntegerType), VarDecl(fact, IntegerType, IntegerLit(1)), ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<=, Id(i), Id(n)), BinExpr(+, Id(i), IntegerLit(1)), AssignStmt(Id(fact), BinExpr(*, Id(fact), Id(i)))), ReturnStmt(Id(fact))]))
	VarDecl(a, IntegerType, IntegerLit(500))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(i, IntegerType), WhileStmt(BinExpr(<=, Id(i), Id(a)), BlockStmt([VarDecl(res, IntegerType, FuncCall(factorial, [Id(i)])), CallStmt(printInteger, Id(i)), AssignStmt(Id(i), BinExpr(+, Id(i), IntegerLit(1)))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 392))

    def test_393(self):
        input = """fibo: function integer(n: integer) {
    if(n < 1) return -1;
    else if(n == 1) return 0;
    else if(n == 2) return 1;
    else return fibo(n - 1) + fibo(n - 2);
}

main: function void() {
    a: integer = 15_82;
    i: integer;
    for(i = 1, i <= a, i+1){
        if(i % 2 == 0) printInt(fibo(i));
    }
}"""
        expect = """Program([
	FuncDecl(fibo, IntegerType, [Param(n, IntegerType)], None, BlockStmt([IfStmt(BinExpr(<, Id(n), IntegerLit(1)), ReturnStmt(UnExpr(-, IntegerLit(1))), IfStmt(BinExpr(==, Id(n), IntegerLit(1)), ReturnStmt(IntegerLit(0)), IfStmt(BinExpr(==, Id(n), IntegerLit(2)), ReturnStmt(IntegerLit(1)), ReturnStmt(BinExpr(+, FuncCall(fibo, [BinExpr(-, Id(n), IntegerLit(1))]), FuncCall(fibo, [BinExpr(-, Id(n), IntegerLit(2))]))))))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, IntegerType, IntegerLit(1582)), VarDecl(i, IntegerType), ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<=, Id(i), Id(a)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(==, BinExpr(%, Id(i), IntegerLit(2)), IntegerLit(0)), CallStmt(printInt, FuncCall(fibo, [Id(i)])))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 393))

    def test_394(self):
        input = """a: array[4] of float = {-1_034E-2, 0.24e-9, 12e7, -1_00.34};
                
dumbGPT: function void(n: float, out result: string) {
    if(n <= 0.0) result = "This number is small \\n";
    else result = "This number is greater than zero";
}

main: function void() {
    i: integer = 0;
    res: array[4] of string;
    do {
        dumbGPT(a[i], res[i]);
        i = i+1;
    } while(i < 4);

    for(i = 0, i < 4, i+1) printString(res[i]);
}"""
        expect = """Program([
	VarDecl(a, ArrayType([4], FloatType), ArrayLit([UnExpr(-, FloatLit(10.34)), FloatLit(2.4e-10), FloatLit(120000000.0), UnExpr(-, FloatLit(100.34))]))
	FuncDecl(dumbGPT, VoidType, [Param(n, FloatType), OutParam(result, StringType)], None, BlockStmt([IfStmt(BinExpr(<=, Id(n), FloatLit(0.0)), AssignStmt(Id(result), StringLit(This number is small \\n)), AssignStmt(Id(result), StringLit(This number is greater than zero)))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(i, IntegerType, IntegerLit(0)), VarDecl(res, ArrayType([4], StringType)), DoWhileStmt(BinExpr(<, Id(i), IntegerLit(4)), BlockStmt([CallStmt(dumbGPT, ArrayCell(a, [Id(i)]), ArrayCell(res, [Id(i)])), AssignStmt(Id(i), BinExpr(+, Id(i), IntegerLit(1)))])), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(4)), BinExpr(+, Id(i), IntegerLit(1)), CallStmt(printString, ArrayCell(res, [Id(i)])))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 394))

    def test_395(self):
        input = """dumbCalc: function void(n: integer) inherit lMaoTrachDong {
    a, b: float;
    printString("Input a and b: ");
    a = readFloat(); b = readFloat();
    // Case +
    if(n == 1) {
        printString("Sum is: ");
        printFloat(a + b);
    }
    // Case -
    else if(n == 2) {
        printString("Subtraction is: ");
        printFloat(a - b);
    }
}

main: function void() {
    stop: boolean = false;
    while(stop == false) {
        n: integer = readInteger();
        dumbCalc(n);
        op: integer = readInteger();
        if(op != 0) stop = true;
    }
}"""
        expect = """Program([
	FuncDecl(dumbCalc, VoidType, [Param(n, IntegerType)], lMaoTrachDong, BlockStmt([VarDecl(a, FloatType), VarDecl(b, FloatType), CallStmt(printString, StringLit(Input a and b: )), AssignStmt(Id(a), FuncCall(readFloat, [])), AssignStmt(Id(b), FuncCall(readFloat, [])), IfStmt(BinExpr(==, Id(n), IntegerLit(1)), BlockStmt([CallStmt(printString, StringLit(Sum is: )), CallStmt(printFloat, BinExpr(+, Id(a), Id(b)))]), IfStmt(BinExpr(==, Id(n), IntegerLit(2)), BlockStmt([CallStmt(printString, StringLit(Subtraction is: )), CallStmt(printFloat, BinExpr(-, Id(a), Id(b)))])))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(stop, BooleanType, BooleanLit(False)), WhileStmt(BinExpr(==, Id(stop), BooleanLit(False)), BlockStmt([VarDecl(n, IntegerType, FuncCall(readInteger, [])), CallStmt(dumbCalc, Id(n)), VarDecl(op, IntegerType, FuncCall(readInteger, [])), IfStmt(BinExpr(!=, Id(op), IntegerLit(0)), AssignStmt(Id(stop), BooleanLit(True)))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 395))

    def test_396(self):
        input = """dumbCalc: function void(n: integer) inherit lMaoTrachDong {
    a, b: float;
    printString("Input a and b: ");
    a = readFloat(); b = readFloat();
    // Case +
    if(n == 1) {
        printString("Sum is: ");
        printFloat(a + b);
    }
    // Case -
    else if(n == 2) {
        printString("Subtraction is: ");
        printFloat(a - b);
    }
}

main: function void() {
    while(true) {
        n: integer = readInteger();
        dumbCalc(n);
        op: integer = readInteger();
        if(op != 0) break;
    }
}"""
        expect = """Program([
	FuncDecl(dumbCalc, VoidType, [Param(n, IntegerType)], lMaoTrachDong, BlockStmt([VarDecl(a, FloatType), VarDecl(b, FloatType), CallStmt(printString, StringLit(Input a and b: )), AssignStmt(Id(a), FuncCall(readFloat, [])), AssignStmt(Id(b), FuncCall(readFloat, [])), IfStmt(BinExpr(==, Id(n), IntegerLit(1)), BlockStmt([CallStmt(printString, StringLit(Sum is: )), CallStmt(printFloat, BinExpr(+, Id(a), Id(b)))]), IfStmt(BinExpr(==, Id(n), IntegerLit(2)), BlockStmt([CallStmt(printString, StringLit(Subtraction is: )), CallStmt(printFloat, BinExpr(-, Id(a), Id(b)))])))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([WhileStmt(BooleanLit(True), BlockStmt([VarDecl(n, IntegerType, FuncCall(readInteger, [])), CallStmt(dumbCalc, Id(n)), VarDecl(op, IntegerType, FuncCall(readInteger, [])), IfStmt(BinExpr(!=, Id(op), IntegerLit(0)), BreakStmt())]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 396))

    def test_397(self):
        input = """printSeq: function void(out n: integer) {
    i: integer;
    for(i = 1, i <= n, i+1) printInteger(i);
}

main: function void() {
    n: integer = readInteger();
    if(n < 1) printString("Only positive number plz");
    else printSeq(n);
}"""
        expect = """Program([
	FuncDecl(printSeq, VoidType, [OutParam(n, IntegerType)], None, BlockStmt([VarDecl(i, IntegerType), ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<=, Id(i), Id(n)), BinExpr(+, Id(i), IntegerLit(1)), CallStmt(printInteger, Id(i)))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(n, IntegerType, FuncCall(readInteger, [])), IfStmt(BinExpr(<, Id(n), IntegerLit(1)), CallStmt(printString, StringLit(Only positive number plz)), CallStmt(printSeq, Id(n)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 397))

    def test_398(self):
        input = """main: function void() {
    do {
        isUnder18: boolean = readBoolean();
        if(isUnder18 == true) printString("You\\'re not allowed to have driving license \\t\\b");
        else printString("Happy road crashing :>");
        cont: boolean = readBoolean();
        if(cont == true) break;
    } while(true);
}"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([DoWhileStmt(BooleanLit(True), BlockStmt([VarDecl(isUnder18, BooleanType, FuncCall(readBoolean, [])), IfStmt(BinExpr(==, Id(isUnder18), BooleanLit(True)), CallStmt(printString, StringLit(You\\'re not allowed to have driving license \\t\\b)), CallStmt(printString, StringLit(Happy road crashing :>))), VarDecl(cont, BooleanType, FuncCall(readBoolean, [])), IfStmt(BinExpr(==, Id(cont), BooleanLit(True)), BreakStmt())]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 398))

    def test_399(self):
        input = """main: function void() {
    // Multiple lines comment!
    // ~~~&$$$
    // Hihi

    /* Block comment
    Weeeeeee
    Wooooo
    */
}"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 399))

    def test_400(self):
        input = """main: function void() { a = "Adios \\t"; printString(a); }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(a), StringLit(Adios \\t)), CallStmt(printString, Id(a))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 400))