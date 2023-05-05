# Generated from main/bkool/parser/BKOOL.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .BKOOLParser import BKOOLParser
else:
    from BKOOLParser import BKOOLParser

# This class defines a complete generic visitor for a parse tree produced by BKOOLParser.

class BKOOLVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by BKOOLParser#program.
    def visitProgram(self, ctx:BKOOLParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#decls.
    def visitDecls(self, ctx:BKOOLParser.DeclsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#decl.
    def visitDecl(self, ctx:BKOOLParser.DeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#vardecl.
    def visitVardecl(self, ctx:BKOOLParser.VardeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#idlist.
    def visitIdlist(self, ctx:BKOOLParser.IdlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#idlist2.
    def visitIdlist2(self, ctx:BKOOLParser.Idlist2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#funcdecl.
    def visitFuncdecl(self, ctx:BKOOLParser.FuncdeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#paramdecl.
    def visitParamdecl(self, ctx:BKOOLParser.ParamdeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#paramlist.
    def visitParamlist(self, ctx:BKOOLParser.ParamlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#paramlist2.
    def visitParamlist2(self, ctx:BKOOLParser.Paramlist2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#param.
    def visitParam(self, ctx:BKOOLParser.ParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#body.
    def visitBody(self, ctx:BKOOLParser.BodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#body_ele_list.
    def visitBody_ele_list(self, ctx:BKOOLParser.Body_ele_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#body_ele_list2.
    def visitBody_ele_list2(self, ctx:BKOOLParser.Body_ele_list2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#body_ele.
    def visitBody_ele(self, ctx:BKOOLParser.Body_eleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#statement.
    def visitStatement(self, ctx:BKOOLParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#statement_kind.
    def visitStatement_kind(self, ctx:BKOOLParser.Statement_kindContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#assignSt.
    def visitAssignSt(self, ctx:BKOOLParser.AssignStContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#callSt.
    def visitCallSt(self, ctx:BKOOLParser.CallStContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#returnSt.
    def visitReturnSt(self, ctx:BKOOLParser.ReturnStContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#exprlist.
    def visitExprlist(self, ctx:BKOOLParser.ExprlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#exprlist2.
    def visitExprlist2(self, ctx:BKOOLParser.Exprlist2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#expr.
    def visitExpr(self, ctx:BKOOLParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#addexpr.
    def visitAddexpr(self, ctx:BKOOLParser.AddexprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#subexpr.
    def visitSubexpr(self, ctx:BKOOLParser.SubexprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#mulexpr.
    def visitMulexpr(self, ctx:BKOOLParser.MulexprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#divexpr.
    def visitDivexpr(self, ctx:BKOOLParser.DivexprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#numlit.
    def visitNumlit(self, ctx:BKOOLParser.NumlitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#var_type.
    def visitVar_type(self, ctx:BKOOLParser.Var_typeContext):
        return self.visitChildren(ctx)



del BKOOLParser