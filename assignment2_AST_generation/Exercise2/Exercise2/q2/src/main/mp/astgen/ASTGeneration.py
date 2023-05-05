from MPVisitor import MPVisitor
from MPParser import MPParser
from AST import *
from functools import *

class ASTGeneration(MPVisitor):

    def visitProgram(self,ctx:MPParser.ProgramContext):
        return Program(ctx.vardecls().accept(self))

    def visitVardecls(self,ctx:MPParser.VardeclsContext):
        return list(map(lambda x: , ctx.vardecl()))

    def visitVardecl(self,ctx:MPParser.VardeclContext):
        lst = ctx.ids()
        ty = ctx.mptype().accept(self)
        return [map(lambda e: [VarDecl(e.accept(self), ty)], lst)]

    def visitMptype(self,ctx:MPParser.MptypeContext): 
        return IntType() if ctx.INTTYPE() else FloatType()

    def visitIds(self,ctx:MPParser.IdsContext):
        return [Id(x.getText()) for x in ctx.ID()]
    

        

