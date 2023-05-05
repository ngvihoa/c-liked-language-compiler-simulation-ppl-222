from MT22Visitor import MT22Visitor
from MT22Parser import MT22Parser
from AST import *


class ASTGeneration(MT22Visitor):
    def visitProgram(self, ctx: MT22Parser.ProgramContext):
        return Program(self.visit(ctx.declarations()))
    
    ##
    def visitDeclarations(self, ctx:MT22Parser.DeclarationsContext):
        if ctx.getChildCount() == 0:
            return []
        lst = self.visit(ctx.declaration()) + self.visit(ctx.declarations2())
        return lst


    ##
    def visitDeclarations2(self, ctx:MT22Parser.Declarations2Context):
        if ctx.getChildCount() == 0:
            return []
        lst = self.visit(ctx.declaration()) + self.visit(ctx.declarations2())
        return lst


    ##
    def visitDeclaration(self, ctx:MT22Parser.DeclarationContext):
        if ctx.var_declaration():
            return self.visit(ctx.var_declaration())
        return self.visit(ctx.funct_declaration())


    ##
    def visitVar_declaration(self, ctx:MT22Parser.Var_declarationContext):
        if ctx.var_dec():
            return self.visit(ctx.var_dec())
        return self.visit(ctx.param_dec())


    ##
    def visitVar_dec(self, ctx:MT22Parser.Var_decContext):
        if ctx.var_dec_short():
            return self.visit(ctx.var_dec_short())
        name, exp, typ = self.visit(ctx.var_dec_full())
        lst = []
        for i in range(len(name)):
            lst = lst + [VarDecl(name[i], typ, exp[i])]
        return lst


    ##
    def visitVar_dec_short(self, ctx:MT22Parser.Var_dec_shortContext):
        typ = self.visit(ctx.var_type2())
        idlist = self.visit(ctx.id_list())
        return [VarDecl(x, typ) for x in idlist]

    ##
    def visitVar_type(self, ctx:MT22Parser.Var_typeContext):
        if ctx.atomic_type():
            return self.visit(ctx.atomic_type())
        return self.visit(ctx.array_type_decl())


    ##
    def visitId_list(self, ctx:MT22Parser.Id_listContext):
        idd = [ctx.ID().getText()]
        if ctx.getChildCount() == 1:
            return idd
        idd = idd + self.visit(ctx.id_list2())
        return idd


    ##
    def visitId_list2(self, ctx:MT22Parser.Id_list2Context):
        if ctx.getChildCount() == 0:
            return []
        idd = [ctx.ID().getText()] + self.visit(ctx.id_list2())
        return idd


    ##
    def visitVar_dec_full(self, ctx:MT22Parser.Var_dec_fullContext):
        if ctx.ASSIGN():
            return [ctx.ID().getText()], [self.visit(ctx.expression())], self.visit(ctx.var_type2())
        tmp1, tmp2, tmp3 = self.visit(ctx.var_dec_full())
        tmp1 = [ctx.ID().getText()] + tmp1
        tmp2 = tmp2 + [self.visit(ctx.expression())]
        return  tmp1, tmp2, tmp3


    ##
    def visitVar_type2(self, ctx:MT22Parser.Var_type2Context):
        if ctx.AUTO():
            return AutoType()
        return self.visit(ctx.var_type())


    ##
    def visitParam_dec(self, ctx:MT22Parser.Param_decContext):
        out = True if ctx.OUT() else False
        inhe = True if ctx.INHERIT() else False
        return [ParamDecl(ctx.ID().getText(), self.visit(ctx.var_type2()), out, inhe)]


    ##
    def visitFunct_declaration(self, ctx:MT22Parser.Funct_declarationContext):
        name = ctx.ID().getText()
        returnType = self.visit(ctx.var_type3())
        paramList = self.visit(ctx.param_list())
        inhe = self.visit(ctx.inherit_func())
        body = self.visit(ctx.block_Statement())
        return [FuncDecl(name, returnType, paramList, inhe, body)]


    ##
    def visitParam_list(self, ctx:MT22Parser.Param_listContext):
        if ctx.getChildCount() == 0:
            return []
        idd = self.visit(ctx.param_dec()) + self.visit(ctx.param_list2())
        return idd


    ##
    def visitParam_list2(self, ctx:MT22Parser.Param_list2Context):
        if ctx.getChildCount() == 0:
            return []
        idd = self.visit(ctx.param_dec()) + self.visit(ctx.param_list2())
        return idd


    ## dont know return str or Id()
    def visitInherit_func(self, ctx:MT22Parser.Inherit_funcContext):
        if ctx.getChildCount() == 0:
            return None
        return ctx.ID().getText()


    ##
    def visitVar_type3(self, ctx:MT22Parser.Var_type3Context):
        if ctx.var_type2():
            return self.visit(ctx.var_type2())
        return self.visit(ctx.void_type())

    ##
    def visitEle_array_list(self, ctx:MT22Parser.Ele_array_listContext):
        if ctx.getChildCount() == 0:
            return []
        lst  = [self.visit(ctx.expression())] + self.visit(ctx.ele_array_list2())
        return lst

    ##
    def visitEle_array_list2(self, ctx:MT22Parser.Ele_array_list2Context):
        if ctx.getChildCount() == 0:
            return []
        lst  = [self.visit(ctx.expression())] + self.visit(ctx.ele_array_list2())
        return lst


    ##
    def visitVoid_type(self, ctx:MT22Parser.Void_typeContext):
        return VoidType()


    ##
    def visitAtomic_type(self, ctx:MT22Parser.Atomic_typeContext):
        if ctx.BOOLEAN():
            return BooleanType()
        if ctx.INTEGER():
            return IntegerType()
        if ctx.FLOAT():
            return FloatType()
        if ctx.STRING():
            return StringType()


    ## return ArrayType()
    def visitArray_type_decl(self, ctx:MT22Parser.Array_type_declContext):
        dimensions = self.visit(ctx.array_type_dimension())
        typ = self.visit(ctx.atomic_type())
        return ArrayType(dimensions, typ)


    ## return list[int]
    def visitArray_type_dimension(self, ctx:MT22Parser.Array_type_dimensionContext):
        return self.visit(ctx.dimension_size_list())


    ##
    def visitDimension_size_list(self, ctx:MT22Parser.Dimension_size_listContext):
        e = [int(ctx.INT_LIT().getText())]
        if ctx.getChildCount() == 1:
            return e
        return e + self.visit(ctx.dimension_size_list2())


    ##
    def visitDimension_size_list2(self, ctx:MT22Parser.Dimension_size_list2Context):
        if ctx.getChildCount() == 0:
            return []
        e = [int(ctx.INT_LIT().getText())]
        return e + self.visit(ctx.dimension_size_list2())


    ## temporarily return list[exp]
    def visitExpr_list(self, ctx:MT22Parser.Expr_listContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.expression())]
        expList = [self.visit(ctx.expression())] + self.visit(ctx.expr_list2())
        return expList

    ##
    def visitExpr_list2(self, ctx:MT22Parser.Expr_list2Context):
        if ctx.getChildCount() == 0:
            return []
        expList = [self.visit(ctx.expression())] + self.visit(ctx.expr_list2())
        return expList


    ##
    def visitExpression(self, ctx:MT22Parser.ExpressionContext):
        return self.visit(ctx.string_expression())


    ##
    def visitString_expression(self, ctx:MT22Parser.String_expressionContext):
        if ctx.DCOLON():
            return BinExpr(ctx.DCOLON().getText(), self.visit(ctx.relational_expression(0)), self.visit(ctx.relational_expression(1)))
        return self.visit(ctx.relational_expression(0))


    ##
    def visitRelational_expression(self, ctx:MT22Parser.Relational_expressionContext):
        if ctx.relational_operator():
            return BinExpr(self.visit(ctx.relational_operator()), self.visit(ctx.logical_expression(0)), self.visit(ctx.logical_expression(1)))
        return self.visit(ctx.logical_expression(0))


    ##
    def visitLogical_expression(self, ctx:MT22Parser.Logical_expressionContext):
        if ctx.logical_operator():
            return BinExpr(self.visit(ctx.logical_operator()), self.visit(ctx.logical_expression()), self.visit(ctx.adding_expression()))
        return self.visit(ctx.adding_expression())


    ##
    def visitAdding_expression(self, ctx:MT22Parser.Adding_expressionContext):
        if ctx.adding_operator():
            return BinExpr(self.visit(ctx.adding_operator()), self.visit(ctx.adding_expression()), self.visit(ctx.multiplying_expression()))
        return self.visit(ctx.multiplying_expression())


    ##
    def visitMultiplying_expression(self, ctx:MT22Parser.Multiplying_expressionContext):
        if ctx.multiplying_operator():
            return BinExpr(self.visit(ctx.multiplying_operator()), self.visit(ctx.multiplying_expression()), self.visit(ctx.not_expression()))
        return self.visit(ctx.not_expression())


    ##
    def visitNot_expression(self, ctx:MT22Parser.Not_expressionContext):
        if ctx.not_operator():
            return UnExpr(self.visit(ctx.not_operator()), self.visit(ctx.not_expression()))
        return self.visit(ctx.sign_expression())


    ##
    def visitSign_expression(self, ctx:MT22Parser.Sign_expressionContext):
        if ctx.sign_operator():
            return UnExpr(self.visit(ctx.sign_operator()), self.visit(ctx.sign_expression()))
        return self.visit(ctx.index_expression())


    ## confusing about operator [,] and its Expr
    def visitIndex_expression(self, ctx:MT22Parser.Index_expressionContext):
        if ctx.ID():
            return ArrayCell(ctx.ID().getText(), self.visit(ctx.index_operator()))
        return self.visit(ctx.expr_ele())


    ## confusing about if Id(ctx.ID().getText())
    def visitExpr_ele(self, ctx:MT22Parser.Expr_eleContext):
        if ctx.LB():
            return self.visit(ctx.expression())
        if ctx.full_literal():
            return self.visit(ctx.full_literal())
        if ctx.ID(): ####
            return Id(ctx.ID().getText())
        a,b = self.visit(ctx.function_call())
        return FuncCall(a, b)


    ## return list[Expr]
    def visitIndex_operator(self, ctx:MT22Parser.Index_operatorContext):
        return self.visit(ctx.expr_list())


    ##
    def visitNot_operator(self, ctx:MT22Parser.Not_operatorContext):
        return ctx.NOT().getText()


    ##
    def visitSign_operator(self, ctx:MT22Parser.Sign_operatorContext):
        return ctx.SUB().getText()


    ##
    def visitMultiplying_operator(self, ctx:MT22Parser.Multiplying_operatorContext):
        if ctx.MUL():
            return ctx.MUL().getText()
        if ctx.DIV():
            return ctx.DIV().getText()
        return ctx.MOD().getText()


    ##
    def visitAdding_operator(self, ctx:MT22Parser.Adding_operatorContext):
        if ctx.ADD():
            return ctx.ADD().getText()
        return ctx.SUB().getText()


    ##
    def visitLogical_operator(self, ctx:MT22Parser.Logical_operatorContext):
        if ctx.OR():
            return ctx.OR().getText()
        return ctx.AND().getText()


    ##
    def visitRelational_operator(self, ctx:MT22Parser.Relational_operatorContext):
        if ctx.EQUAL():
            return ctx.EQUAL().getText()
        if ctx.UNEQUAL():
            return ctx.UNEQUAL().getText()
        if ctx.LT():
            return ctx.LT().getText()
        if ctx.GT():
            return ctx.GT().getText()
        if ctx.LTE():
            return ctx.LTE().getText()
        return ctx.GTE().getText()


    ##
    def visitFunction_call(self, ctx:MT22Parser.Function_callContext):
        name = ctx.ID().getText()
        args = self.visit(ctx.argument_list()) #get [Expr]
        return name, args


    ##
    def visitArgument_list(self, ctx:MT22Parser.Argument_listContext):
        if ctx.getChildCount() == 0:
            return []
        expList = [self.visit(ctx.expression())] + self.visit(ctx.argument_list2())
        return expList


    ##
    def visitArgument_list2(self, ctx:MT22Parser.Argument_list2Context):
        if ctx.getChildCount() == 0:
            return []
        expList = [self.visit(ctx.expression())] + self.visit(ctx.argument_list2())
        return expList


    ##
    def visitStatement(self, ctx:MT22Parser.StatementContext):
        if ctx.assignment_Statement():
            return self.visit(ctx.assignment_Statement())
        if ctx.if_Statement():
            return self.visit(ctx.if_Statement())
        if ctx.for_Statement():
            return self.visit(ctx.for_Statement())
        if ctx.while_Statement():
            return self.visit(ctx.while_Statement())
        if ctx.do_while_Statement():
            return self.visit(ctx.do_while_Statement())
        if ctx.break_Statement():
            return self.visit(ctx.break_Statement())
        if ctx.continue_Statement():
            return self.visit(ctx.continue_Statement())
        if ctx.return_Statement():
            return self.visit(ctx.return_Statement())
        if ctx.call_Statement():
            return self.visit(ctx.call_Statement())
        return self.visit(ctx.block_Statement())


    ##
    def visitAssignment_Statement(self, ctx:MT22Parser.Assignment_StatementContext):
        lhs = self.visit(ctx.lhs())
        rhs = self.visit(ctx.expression())
        return AssignStmt(lhs, rhs)


    ## confusing at index_expression
    def visitLhs(self, ctx:MT22Parser.LhsContext):
        if ctx.scalar_var():
            return self.visit(ctx.scalar_var())
        name = ctx.ID().getText()
        cell = self.visit(ctx.index_operator())
        return ArrayCell(name, cell)


    ##
    def visitScalar_var(self, ctx:MT22Parser.Scalar_varContext):
        return Id(ctx.ID().getText())


    ##
    def visitIf_Statement(self, ctx:MT22Parser.If_StatementContext):
        cond = self.visit(ctx.expression())
        tstmt = self.visit(ctx.statement(0))
        fstmt = self.visit(ctx.statement(1)) if ctx.ELSE() else None
        return IfStmt(cond, tstmt, fstmt)


    ##
    def visitFor_Statement(self, ctx:MT22Parser.For_StatementContext):
        init = AssignStmt(self.visit(ctx.lhs()), self.visit(ctx.expression(0)))
        cond = self.visit(ctx.expression(1)) 
        upd = self.visit(ctx.expression(2))
        stmt = self.visit(ctx.statement())
        return ForStmt(init, cond, upd, stmt)


    ##
    def visitWhile_Statement(self, ctx:MT22Parser.While_StatementContext):
        cond = self.visit(ctx.expression())
        stmt = self.visit(ctx.statement())
        return WhileStmt(cond, stmt)


    ##
    def visitDo_while_Statement(self, ctx:MT22Parser.Do_while_StatementContext):
        cond = self.visit(ctx.expression())
        stmt = self.visit(ctx.block_Statement())
        return DoWhileStmt(cond, stmt)


    ##
    def visitBreak_Statement(self, ctx:MT22Parser.Break_StatementContext):
        return BreakStmt()


    ##
    def visitContinue_Statement(self, ctx:MT22Parser.Continue_StatementContext):
        return ContinueStmt()


    ##
    def visitReturn_Statement(self, ctx:MT22Parser.Return_StatementContext):
        if ctx.expression():
            return ReturnStmt(self.visit(ctx.expression()))
        return ReturnStmt()


    ##
    def visitCall_Statement(self, ctx:MT22Parser.Call_StatementContext):
        a,b = self.visit(ctx.function_call())
        return CallStmt(a, b)


    ##
    def visitBlock_Statement(self, ctx:MT22Parser.Block_StatementContext):
        body = self.visit(ctx.block_list())
        return BlockStmt(body)


    ##
    def visitBlock_list(self, ctx:MT22Parser.Block_listContext):
        if ctx.getChildCount() == 0:
            return []
        ele = self.visit(ctx.block_ele()) + self.visit(ctx.block_list2())
        return ele


    ##
    def visitBlock_list2(self, ctx:MT22Parser.Block_list2Context):
        if ctx.getChildCount() == 0:
            return []
        ele = self.visit(ctx.block_ele()) + self.visit(ctx.block_list2())
        return ele


    ## confusing at statement whether return list
    def visitBlock_ele(self, ctx:MT22Parser.Block_eleContext):
        if ctx.var_dec():
            return self.visit(ctx.var_dec())
        return [self.visit(ctx.statement())]

    ##
    def visitInt_literal(self, ctx:MT22Parser.Int_literalContext):
        return IntegerLit(int(ctx.INT_LIT().getText()))

    ##
    def visitFloat_literal(self, ctx:MT22Parser.Float_literalContext):
        return FloatLit(float(ctx.FLOAT_LIT().getText()))

    ##
    def visitBool_literal(self, ctx:MT22Parser.Bool_literalContext):
        if ctx.TRUE():
            return BooleanLit(ctx.TRUE().getText() == 'true')
        return BooleanLit(ctx.FALSE().getText() == 'true')


    ##
    def visitString_literal(self, ctx:MT22Parser.String_literalContext):
        return StringLit(ctx.STRING_LIT().getText())

    ##
    def visitNormal_literal(self, ctx:MT22Parser.Normal_literalContext):
        if ctx.int_literal():
            return self.visit(ctx.int_literal())
        if ctx.float_literal():
            return self.visit(ctx.float_literal())
        if ctx.bool_literal():
            return self.visit(ctx.bool_literal())
        if ctx.string_literal():
            return self.visit(ctx.string_literal())

    ##
    def visitArry_literal(self, ctx:MT22Parser.Arry_literalContext):
        return ArrayLit(self.visit(ctx.ele_array_list()))

    ##
    def visitFull_literal(self, ctx:MT22Parser.Full_literalContext):
        if ctx.normal_literal():
            return self.visit(ctx.normal_literal())
        return self.visit(ctx.arry_literal())
    