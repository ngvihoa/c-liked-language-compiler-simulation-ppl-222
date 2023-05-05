# Generated from main/mt22/parser/MT22.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MT22Parser import MT22Parser
else:
    from MT22Parser import MT22Parser

# This class defines a complete generic visitor for a parse tree produced by MT22Parser.

class MT22Visitor(ParseTreeVisitor):

    # Visit a parse tree produced by MT22Parser#program.
    def visitProgram(self, ctx:MT22Parser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#declarations.
    def visitDeclarations(self, ctx:MT22Parser.DeclarationsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#declarations2.
    def visitDeclarations2(self, ctx:MT22Parser.Declarations2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#declaration.
    def visitDeclaration(self, ctx:MT22Parser.DeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#var_declaration.
    def visitVar_declaration(self, ctx:MT22Parser.Var_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#var_dec.
    def visitVar_dec(self, ctx:MT22Parser.Var_decContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#var_dec_short.
    def visitVar_dec_short(self, ctx:MT22Parser.Var_dec_shortContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#var_type.
    def visitVar_type(self, ctx:MT22Parser.Var_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#id_list.
    def visitId_list(self, ctx:MT22Parser.Id_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#id_list2.
    def visitId_list2(self, ctx:MT22Parser.Id_list2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#var_dec_full.
    def visitVar_dec_full(self, ctx:MT22Parser.Var_dec_fullContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#var_type2.
    def visitVar_type2(self, ctx:MT22Parser.Var_type2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#param_dec.
    def visitParam_dec(self, ctx:MT22Parser.Param_decContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#funct_declaration.
    def visitFunct_declaration(self, ctx:MT22Parser.Funct_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#param_list.
    def visitParam_list(self, ctx:MT22Parser.Param_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#param_list2.
    def visitParam_list2(self, ctx:MT22Parser.Param_list2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#inherit_func.
    def visitInherit_func(self, ctx:MT22Parser.Inherit_funcContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#var_type3.
    def visitVar_type3(self, ctx:MT22Parser.Var_type3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#ele_array_list.
    def visitEle_array_list(self, ctx:MT22Parser.Ele_array_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#ele_array_list2.
    def visitEle_array_list2(self, ctx:MT22Parser.Ele_array_list2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#void_type.
    def visitVoid_type(self, ctx:MT22Parser.Void_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#auto_type.
    def visitAuto_type(self, ctx:MT22Parser.Auto_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#atomic_type.
    def visitAtomic_type(self, ctx:MT22Parser.Atomic_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#array_type_decl.
    def visitArray_type_decl(self, ctx:MT22Parser.Array_type_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#array_type_dimension.
    def visitArray_type_dimension(self, ctx:MT22Parser.Array_type_dimensionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#dimension_size_list.
    def visitDimension_size_list(self, ctx:MT22Parser.Dimension_size_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#dimension_size_list2.
    def visitDimension_size_list2(self, ctx:MT22Parser.Dimension_size_list2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expr_list.
    def visitExpr_list(self, ctx:MT22Parser.Expr_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expr_list2.
    def visitExpr_list2(self, ctx:MT22Parser.Expr_list2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expression.
    def visitExpression(self, ctx:MT22Parser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#string_expression.
    def visitString_expression(self, ctx:MT22Parser.String_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#relational_expression.
    def visitRelational_expression(self, ctx:MT22Parser.Relational_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#logical_expression.
    def visitLogical_expression(self, ctx:MT22Parser.Logical_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#adding_expression.
    def visitAdding_expression(self, ctx:MT22Parser.Adding_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#multiplying_expression.
    def visitMultiplying_expression(self, ctx:MT22Parser.Multiplying_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#not_expression.
    def visitNot_expression(self, ctx:MT22Parser.Not_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#sign_expression.
    def visitSign_expression(self, ctx:MT22Parser.Sign_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#index_expression.
    def visitIndex_expression(self, ctx:MT22Parser.Index_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expr_ele.
    def visitExpr_ele(self, ctx:MT22Parser.Expr_eleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#index_operator.
    def visitIndex_operator(self, ctx:MT22Parser.Index_operatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#not_operator.
    def visitNot_operator(self, ctx:MT22Parser.Not_operatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#sign_operator.
    def visitSign_operator(self, ctx:MT22Parser.Sign_operatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#multiplying_operator.
    def visitMultiplying_operator(self, ctx:MT22Parser.Multiplying_operatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#adding_operator.
    def visitAdding_operator(self, ctx:MT22Parser.Adding_operatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#logical_operator.
    def visitLogical_operator(self, ctx:MT22Parser.Logical_operatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#relational_operator.
    def visitRelational_operator(self, ctx:MT22Parser.Relational_operatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#function_call.
    def visitFunction_call(self, ctx:MT22Parser.Function_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#argument_list.
    def visitArgument_list(self, ctx:MT22Parser.Argument_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#argument_list2.
    def visitArgument_list2(self, ctx:MT22Parser.Argument_list2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#statement.
    def visitStatement(self, ctx:MT22Parser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#assignment_Statement.
    def visitAssignment_Statement(self, ctx:MT22Parser.Assignment_StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#lhs.
    def visitLhs(self, ctx:MT22Parser.LhsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#scalar_var.
    def visitScalar_var(self, ctx:MT22Parser.Scalar_varContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#if_Statement.
    def visitIf_Statement(self, ctx:MT22Parser.If_StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#for_Statement.
    def visitFor_Statement(self, ctx:MT22Parser.For_StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#while_Statement.
    def visitWhile_Statement(self, ctx:MT22Parser.While_StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#do_while_Statement.
    def visitDo_while_Statement(self, ctx:MT22Parser.Do_while_StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#break_Statement.
    def visitBreak_Statement(self, ctx:MT22Parser.Break_StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#continue_Statement.
    def visitContinue_Statement(self, ctx:MT22Parser.Continue_StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#return_Statement.
    def visitReturn_Statement(self, ctx:MT22Parser.Return_StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#call_Statement.
    def visitCall_Statement(self, ctx:MT22Parser.Call_StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#block_Statement.
    def visitBlock_Statement(self, ctx:MT22Parser.Block_StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#block_list.
    def visitBlock_list(self, ctx:MT22Parser.Block_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#block_list2.
    def visitBlock_list2(self, ctx:MT22Parser.Block_list2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#block_ele.
    def visitBlock_ele(self, ctx:MT22Parser.Block_eleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#int_literal.
    def visitInt_literal(self, ctx:MT22Parser.Int_literalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#float_literal.
    def visitFloat_literal(self, ctx:MT22Parser.Float_literalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#bool_literal.
    def visitBool_literal(self, ctx:MT22Parser.Bool_literalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#string_literal.
    def visitString_literal(self, ctx:MT22Parser.String_literalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#normal_literal.
    def visitNormal_literal(self, ctx:MT22Parser.Normal_literalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#arry_literal.
    def visitArry_literal(self, ctx:MT22Parser.Arry_literalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#full_literal.
    def visitFull_literal(self, ctx:MT22Parser.Full_literalContext):
        return self.visitChildren(ctx)



del MT22Parser