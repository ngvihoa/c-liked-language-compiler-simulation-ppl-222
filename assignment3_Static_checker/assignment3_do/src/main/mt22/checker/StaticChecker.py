from AST import *
from Visitor import Visitor
from StaticError import *


class StaticChecker(Visitor):
    def __init__(self, ast):
        self.ast = ast
        self.waitingInfered = {}
        self.listFunction = {}
        self.numTravel = 0
        self.currentFunction = None
        self.parentFunction = None
        self.isInLoop = []
        self.envParamFunction = {}
        self.preventFlag = False
        self.waitingParam = {}
        self.numReturn = 0

    def check(self):
        o = [{}]
        self.visit(self.ast, o)
        return []

    # def setType(self, name, typ, param): # many case not set 
    #     for i in param:
    #         if name in i:
    #             i[name] = typ
    #     raise Undeclared(Identifier(), name)  

    # def getScope(self, name, param):
    #     for i in range(len(param)):
    #         if name in param[i]:
    #             return i

    def setTypeWaiting(self, typ, name: List[str]):
        # for e in self.waitingInfered:
        #     if type(self.waitingInfered[e]) == AutoType:
        #         self.waitingInfered[e] = typ
        for i in name:
            self.waitingInfered[i] = typ
    
    def setTypeParam(self, typ, name:List[str], param):
        for i in name:
            for j in param:
                if i in j:
                    j[i] = self.waitingParam[i] = typ
                    

    def setAuto(self, lstAst, typ, param):
        lstFuncall = []
        lstParam = []
        for i in lstAst:
            if type(i) == FuncCall:
                lstFuncall  += [i.name]
            else:
                lstParam += [i.name]
        
        self.setTypeWaiting(typ, lstFuncall)
        self.setTypeParam(typ, lstParam, param)


#=============================================================================== Done
    def visitIntegerType(self, ast, param): 
        return ast
    def visitFloatType(self, ast, param): 
        return ast       
    def visitBooleanType(self, ast, param): 
        return ast
    def visitStringType(self, ast, param): 
        return ast
    def visitArrayType(self, ast, param): 
        return ast
    def visitAutoType(self, ast, param): 
        return ast
    def visitVoidType(self, ast, param): 
        return ast
#===============================================================================
    """
    BinExpr and UnExpr should return LitType and ArrayType
    If AutoType, store element name into waitingInfered{} and waiting to be infered
    """

    """
    == Equal                    int/boolean
    != Not equal                int/boolean
    < Less than                 int/float
    > Greater than              int/float
    <= Less than or equal       int/float
    >= Greater than or equal    int/float

    :: string concatenation string

    ! Negation      boolean
    && Conjunction  boolean
    || Disjunction  boolean

    - Number sign negation      int/float
    + Number Addition           int/float
    - Number Subtraction        int/float
    * Number Multiplication     int/float
    / Number Division           int/float
    % Number Remainder          int


    Multiplying     *, /, %                 Binary Infix Left
    Adding          +, -                    Binary Infix Left
    Logical         &&, ||                  Binary Infix Left
    Relational      ==, !=, <, >, <=, >=    Binary Infix None
    String          ::                      Binary Infix None
    """
    def visitBinExpr(self, ast, param): 
        op = ast.op

        #return type of both
        left = self.visit(ast.left, param)
        right = self.visit(ast.right, param)

        waiting_local = []

        # infer auto
        if type(left) == AutoType:
            left = right
            waiting_local += [ast.left]
            self.setAuto(waiting_local, right, param)
        elif type(right) == AutoType:
            right = left
            waiting_local += [ast.right]
            self.setAuto(waiting_local, left, param)

        # print(op)
        # print("Left: " + str(left))
        # print("Right: " + str(right))

        # concate
        if op in ['::']:
            if type(left) != StringType or type(right) != StringType:
                raise TypeMismatchInExpression(ast)
            else: 
                return StringType()
        
        # add, sub, mul, div, lt, gt, le, ge
        elif op in ['+', '-', '*', '/', '>', '<', '>=', '<=']:
            if (type(left) != IntegerType and type(left) != FloatType) or (type(right) != IntegerType and type(right) != FloatType):
                raise TypeMismatchInExpression(ast)
            elif op in ['>', '<', '>=', '<=']:
                return BooleanType()
            else:
                if type(left) == FloatType or type(right) == FloatType:
                    return FloatType()
                else:
                    return IntegerType()

        # ==, !=
        elif op in ['==', '!=']:
            lstType = [IntegerType, BooleanType]
            if type(left) == type(right) and type(left) in lstType:
                return BooleanType()
            else:
                raise TypeMismatchInExpression(ast)

        # %
        elif op in ['%']:
            if type(left) != IntegerType or type(right) != IntegerType:
                raise TypeMismatchInExpression(ast)
            else: 
                return IntegerType()

        # &&, ||
        else:
            if type(left) != BooleanType or type(right) != BooleanType:
                raise TypeMismatchInExpression(ast)
            else: 
                return BooleanType()

    """
    Sign    -   Unary Prefix     Right
    Logical !   Unary Prefix  Right
    """
    def visitUnExpr(self, ast, param): 
        op = ast.op
        val = self.visit(ast.val, param)

        if op in ['-']:
            if type(val) not in [IntegerType, FloatType]:
                return TypeMismatchInExpression(ast)        
        else:
            if type(val) != BooleanType:
                return TypeMismatchInExpression(ast)

        return val

    def visitId(self, ast, param):
        for i in param:
            if ast.name in i:
                typ = i[ast.name]
                if type(typ) != FuncDecl:
                    return typ
        raise Undeclared(Identifier(), ast.name)

    """
    return a Type (ArrayType or Atomic)
    1. check name
    2. check len(cell)
    3. check expr in cell, must in IntegerType
    """
    def visitArrayCell(self, ast, param):
        name = ast.name
        listCell = ast.cell

        typeA = ""
        isExist = False
        for i in param:
            if name in i:
                typeA = i[name]
                isExist = True
                break
        
        if isExist:
            if type(typeA) == ArrayType and len(listCell) <= len(typeA.dimensions):
                dim = typeA.dimensions
                atomicType = typeA.typ

                # check list expr indices
                for i in listCell:
                    tmptype = self.visit(i, param)
                    if type(tmptype) == AutoType:
                        self.setAuto([i], IntegerType(), param)
                    elif type(tmptype) != IntegerType:
                        raise TypeMismatchInExpression(ast)
                
                # get new dim
                n = len(listCell)
                new_dim = dim[n:len(dim)]

                if len(new_dim) == 0:
                    return atomicType
                else:
                    return ArrayType(new_dim, atomicType)
                
            else:
                raise TypeMismatchInExpression(ast)
        else:
            raise Undeclared(Identifier(), ast.name)

#=============================================================================== Done
    def visitIntegerLit(self, ast, param): 
        return IntegerType()
    def visitFloatLit(self, ast, param): 
        return FloatType()
    def visitStringLit(self, ast, param): 
        return StringType()
    def visitBooleanLit(self, ast, param): 
        return BooleanType()
#===============================================================================
    """
    ArrayLit() check:
    return ArrayType(dim, AtomicType)
    will not have case { auto, auto, auto}
    can have case { auto, lit, auto, ...}
    {} is illegal but not need to check
    {auto} nevermind
    if has foo(), ... etc. add in waitingInfered[{foo: IntType()}]
    way to check:
      - update dim if 1si ele is Array
      - case len > 1:
          <continue compared to 1st element>
          * case ArrayType() both:
              dim=, typ= else: raise error
          * case Atomic both:
              auto-auto_ continue 
              -> auto-lit _ set 
              all ele in global waiting dict to new Type, 
              update typ 
              -> lit_auto _ set all ele in global waiting dict to new Type
              else: (lit != lit/lit_Array) raise error
          * case raise error
      - update typ and dim -> return
    """
    def visitArrayLit(self, ast, param):  ## 
        lst = ast.explist
        waiting_lst = []
        dimension = []
        first_ele = self.visit(lst[0], param) # 1st element
        type_check = first_ele

        if type(type_check) == ArrayType:
            dimension = type_check.dimensions

        if len(lst) > 1:
            for i in range(1,len(lst)):
                compared_ele = self.visit(lst[i], param)
                if type(type_check) == ArrayType and type(compared_ele) == ArrayType:
                    if dimension == compared_ele.dimensions and type(type_check.typ) == type(compared_ele.typ):
                        continue
                    else:
                        raise IllegalArrayLiteral(ast)
                elif type(type_check) == AutoType and type(compared_ele) == AutoType:
                    if lst[0] not in waiting_lst:
                        waiting_lst += [lst[0]]
                    if lst[i] not in waiting_lst:
                        waiting_lst += [lst[i]]
                elif type(type_check) == AutoType: # and type(compared_ele) != FuncDecl:
                    if lst[0] not in waiting_lst:
                        waiting_lst += [lst[0]]
                    self.setAuto(waiting_lst, compared_ele, param)
                    type_check = compared_ele
                    waiting_lst = []
                elif type(compared_ele) == AutoType: # and type(type_check) != FuncDecl:
                    self.setAuto([lst[i]], type_check, param)
                elif type(type_check) != type(compared_ele): # or (type(type_check) == type(compared_ele) and type(type_check) == FuncDecl): 
                    raise IllegalArrayLiteral(ast)                        

        if type(type_check) == ArrayType:
            type_check = type_check.typ
        dimension = [len(lst)] + dimension

        return ArrayType(dimension, type_check)

    """
    return function type
    1. check name exist
        flag
        - check in param
            check it is function or vardecl_raise TypeMismatchInExpression()
            get Type
            mark flag
        - check in listFunction{}
            get Type
            mark flag
        - check exist with flag
    2. check function: return type -> paramlist
        - void -> error
        - auto => call before declared => check if exist in waitingInfered: get Type(include AutoType) ? add to waitingInfered
        - other Type => get Type

        - check paramlist:
            + visit element in args compared to params
            + check len
        - update FuncDecl: prototype to function in dictionary
        - return type
    """
    def visitFuncCall(self, ast, param): 
        name = ast.name
        args = ast.args

        flag = False
        prototype = ""

        # check if function declared before
        for i in param:
            if name in i:
                if type(i[name]) != FuncDecl:
                    raise TypeMismatchInExpression(ast)
                else:
                    prototype = i[name]
                    flag = True
        
        # print(prototype)

        # check if function not declared yet 
        if not flag:
            if name in self.listFunction:
                prototype = self.listFunction[name]
                flag = True
        
        # check if exist 
        if flag: # the function exist
            typ = ""

            if type(prototype.return_type) == VoidType:
                raise TypeMismatchInExpression(ast)
            elif type(prototype.return_type) == AutoType:
                if prototype.name in self.waitingInfered:
                    typ = self.waitingInfered[prototype.name]
                else:
                    typ = self.waitingInfered[prototype.name] = AutoType()
            else:
                typ = prototype.return_type
            
            i = 0
            params = prototype.params

            while(i < len(params) and i < len(args)):
                ag = self.visit(args[i], param)
                # never have case auto both
                if type(ag) == AutoType:
                    self.setAuto([args[i]], params[i].typ, param)
                elif type(params[i].typ) == AutoType:
                    params[i].typ = ag
                elif type(ag) == ArrayType and type(params[i].typ) == ArrayType:
                    if ag.dimensions != params[i].typ.dimensions or type(ag.typ) != type(params[i].typ.typ):
                        raise TypeMismatchInExpression(ast)
                elif type(ag) != type(params[i].typ):
                    if not (type(ag) == IntegerType and type(params[i].typ) == FloatType):
                        raise TypeMismatchInExpression(ast)                
                i += 1

            # if len(params) < len(args):
            #     raise TypeMismatchInExpression(args[len(params)])
            # if len(params) > len(args):
            #     raise TypeMismatchInExpression("") 
            
            if len(params) != len(args):
                raise TypeMismatchInExpression(ast)

            # update params
            prototype.params = params
            # update prototype
            if name in param[-1]:
                param[-1][name] = prototype
            self.listFunction[name] = prototype                

            # if everything normal
            return typ
        else: 
            raise Undeclared(Function(), name)


# =============================================================================
    # for bockstmt in stmt, dont open new scope
    def visitAssignStmt(self, ast, param): 
        lhs = self.visit(ast.lhs, param)
        rhs = self.visit(ast.rhs, param)

        if(type(lhs) == VoidType or type(lhs) == ArrayType):
            raise TypeMismatchInStatement(ast)
        
        if type(lhs) == AutoType: # case lhs is parameter
            self.setAuto([ast.lhs], rhs, param)
        elif type(rhs) == AutoType:
            self.setAuto([ast.rhs], lhs, param)
        elif type(lhs) != type(rhs):
            if not (type(lhs) == FloatType and type(rhs) == IntegerType):
                raise TypeMismatchInStatement(ast)

    def visitBlockStmt(self, ast, param): 
        # tmp = self.envParamFunction
        env = [self.envParamFunction] + param
        self.envParamFunction = {}
        body = ast.body
        for i in body:
            self.visit(i, env)
        
    def visitIfStmt(self, ast, param): 
        # check expr condition
        cond = self.visit(ast.cond, param)
        if type(cond) == AutoType:
            self.setAuto([ast.cond], BooleanType(), param)
        elif type(cond) != BooleanType:
            raise TypeMismatchInStatement(ast)
        
        # check stmt ???
        self.visit(ast.tstmt, param)

        if ast.fstmt is not None:
            self.visit(ast.fstmt, param)


    def visitForStmt(self, ast, param): 
        initpart = ast.init
        condpart = ast.cond
        updpart = ast.upd
        # check init in IntType()
        self.visit(initpart, param)
        tmp = self.visit(initpart.lhs, param)
        if type(tmp) != IntegerType:
            raise TypeMismatchInStatement(ast) # not sure

        # check cond in BooleanType()
        tmp2 = self.visit(condpart, param)
        if type(tmp2) == AutoType:
            self.setAuto([ast.cond], BooleanType(), param)
        elif type(tmp2) != BooleanType:
            raise TypeMismatchInStatement(ast)
        
        # check upd in IntegerType()
        tmp3 = self.visit(updpart, param)
        if type(tmp3) == AutoType:
            self.setAuto([ast.upd], IntegerType(), param)
        elif type(tmp3) != IntegerType:
            raise TypeMismatchInStatement(ast) # not sure
        
        self.isInLoop = [True] + self.isInLoop
        # traverse in Stmt
        self.visit(ast.stmt, param)
        self.isInLoop = self.isInLoop[1:]
        
    def visitWhileStmt(self, ast, param): 
        # check expr condition
        cond = self.visit(ast.cond, param)
        if type(cond) == AutoType:
            self.setAuto([ast.cond], BooleanType(), param)
        elif type(cond) != BooleanType:
            raise TypeMismatchInStatement(ast)
        
        # check stmt??
        self.isInLoop = [True] + self.isInLoop
        self.visit(ast.stmt, param)
        self.isInLoop = self.isInLoop[1:]

        
    def visitDoWhileStmt(self, ast, param): 
        # check stmt first????
        self.isInLoop = [True] + self.isInLoop
        self.visit(ast.stmt, param)
        self.isInLoop = self.isInLoop[1:]

        # check expr condition
        cond = self.visit(ast.cond, param)
        if type(cond) == AutoType:
            self.setAuto([ast.cond], BooleanType(), param)
        elif type(cond) != BooleanType:
            raise TypeMismatchInStatement(ast)

    def visitBreakStmt(self, ast, param): 
        if len(self.isInLoop) == 0:
            raise MustInLoop(ast)

    def visitContinueStmt(self, ast, param): 
        if len(self.isInLoop) == 0:
            raise MustInLoop(ast)

    def visitReturnStmt(self, ast, param): 
        self.numReturn += 1
        if ast.expr is not None:
            tmp = self.visit(ast.expr, param)
            # print(str(tmp))
            if type(self.currentFunction.return_type) == AutoType:
                self.currentFunction.return_type = tmp
            elif type(tmp) == AutoType and type(self.currentFunction.return_type) != VoidType:
                self.setAuto([ast.expr], self.currentFunction.return_type, param)
            elif type(tmp) == ArrayType and type(self.currentFunction.return_type) == ArrayType:
                if tmp.dimensions != self.currentFunction.return_type.dimensions or type(tmp.typ) != type(self.currentFunction.return_type.typ):
                    raise TypeMismatchInStatement(ast)
            elif type(tmp) != type(self.currentFunction.return_type):
                if not (type(tmp) == IntegerType and type(self.currentFunction.return_type) == FloatType):
                    raise TypeMismatchInStatement(ast)
        else:
            if type(self.currentFunction.return_type) == AutoType:
                self.currentFunction.return_type = VoidType()
    
    def visitCallStmt(self, ast, param): 
        # because no test case special function in line different from the first line
        # ==> frist line is special function or others
        if ast.name == 'super':
            paramsparent = self.parentFunction.params
            callparam = ast.args
            i = 0
            while(i < len(paramsparent) and i < len(callparam)):
                ag = self.visit(callparam[i], param)
                # never have case auto both
                if type(ag) == AutoType: # case callparam[i] is id _ param from parent or child
                    self.setAuto([callparam[i]], paramsparent[i].typ, param)
                elif type(paramsparent[i].typ) == AutoType:
                    paramsparent[i].typ = ag
                    if paramsparent[i].inherit:
                        param[0][paramsparent[i].name] = ag
                elif type(ag) == ArrayType and type(paramsparent[i].typ) == ArrayType:
                    if ag.dimensions != paramsparent[i].typ.dimensions or type(ag.typ) != type(paramsparent[i].typ.typ):
                        raise TypeMismatchInExpression(callparam[i])
                elif type(ag) != type(paramsparent[i].typ):
                    if not (type(ag) == IntegerType and type(paramsparent[i].typ) == FloatType): 
                        raise TypeMismatchInExpression(callparam[i])
                
                i += 1

            if len(paramsparent) < len(callparam):
                raise TypeMismatchInExpression(callparam[len(paramsparent)])
            if len(paramsparent) > len(callparam):
                raise TypeMismatchInExpression("") # may fix tghe Static Error later

        elif ast.name == 'preventDefault':
            args = ast.args
            if len(args) != 0:
                raise InvalidStatementInFunction(ast)
        elif ast.name == 'readInteger' or ast.name == 'readFloat' or ast.name == 'readBoolean' or ast.name == 'readString':
            args = ast.args
            if len(args) != 0:
                raise TypeMismatchInStatement(ast)
        elif ast.name == 'printInteger':
            args = ast.args
            if len(args) != 1:
                raise TypeMismatchInStatement(ast)
            
            t = self.visit(args[0], param)
            if type(t) == AutoType:
                self.setAuto([args[0]], IntegerType(), param)
            elif type(t) != IntegerType:
                raise TypeMismatchInStatement(ast)
        elif ast.name == 'printFloat':
            args = ast.args
            if len(args) != 1:
                raise TypeMismatchInStatement(ast)
            
            t = self.visit(args[0], param)
            if type(t) == AutoType:
                self.setAuto([args[0]], FloatType(), param)
            elif type(t) != FloatType:
                if type(t) != IntegerType:
                    raise TypeMismatchInStatement(ast)
        elif ast.name == 'printBoolean':
            args = ast.args
            if len(args) != 1:
                raise TypeMismatchInStatement(ast)
            
            t = self.visit(args[0], param)
            if type(t) == AutoType:
                self.setAuto([args[0]], BooleanType(), param)
            elif type(t) != BooleanType:
                raise TypeMismatchInStatement(ast)
        elif ast.name == 'printString':
            args = ast.args
            if len(args) != 1:
                raise TypeMismatchInStatement(ast)
            
            t = self.visit(args[0], param)
            if type(t) == AutoType:
                self.setAuto([args[0]], StringType(), param)
            elif type(t) != StringType:
                raise TypeMismatchInStatement(ast)
        else:
            name = ast.name
            args = ast.args

            flag = False
            prototype = ""

            # check if function declared before
            for i in param:
                if name in i:
                    if type(i[name]) != FuncDecl:
                        flag = False
                    else:
                        prototype = i[name]
                        flag = True
            
            # check if function not declared yet 
            if not flag:
                if name in self.listFunction:
                    prototype = self.listFunction[name]
                    flag = True
            
            # check if exist 
            if flag: # the function exist
                typ = ""

                if type(prototype.return_type) == AutoType:
                    if prototype.name in self.waitingInfered:
                        typ = self.waitingInfered[prototype.name]
                    else:
                        typ = self.waitingInfered[prototype.name] = AutoType()
                else:
                    # print(type(prototype.return_type))
                    typ = prototype.return_type
                
                i = 0
                params = prototype.params

                while(i < len(params) and i < len(args)):
                    ag = self.visit(args[i], param)
                    # never have case auto both
                    if type(ag) == AutoType:
                        self.setAuto([args[i]], params[i].typ, param)
                    elif type(params[i].typ) == AutoType:
                        params[i].typ = ag
                    elif type(ag) == ArrayType and type(params[i].typ) == ArrayType:
                        if ag.dimensions != params[i].typ.dimensions or type(ag.typ) != type(params[i].typ.typ):
                            raise TypeMismatchInStatement(ast)
                    elif type(ag) != type(params[i].typ):
                        if not (type(ag) == IntegerType and type(params[i].typ) == FloatType):
                            raise TypeMismatchInStatement(ast)
                    
                    i += 1

                # if len(params) < len(args):
                #     raise TypeMismatchInExpression(args[len(params)])
                # if len(params) > len(args):
                #     raise TypeMismatchInExpression("") 

                if len(params) != len(args):
                    raise TypeMismatchInStatement(ast)
                
                # update params
                prototype.params = params
                # update prototype
                if name in param[-1]:
                    param[-1][name] = prototype
                self.listFunction[name] = prototype

                # if everything normal

            else: 
                raise Undeclared(Function(), name)
        

# ==========================================================================
    def visitVarDecl(self, ast, param):
        if ast.name in param[0]:
            raise Redeclared(Identifier(), ast.name)
        
        typ = self.visit(ast.typ, param)
        param[0][ast.name] = typ
        if type(typ) == AutoType and ast.init is None:
            raise Invalid(Variable(), ast.name)
        elif type(typ) == AutoType and ast.init is not None:
            init_type = self.visit(ast.init, param)
            typ = init_type
        elif type(typ) != AutoType and ast.init is not None:
            init_type = self.visit(ast.init, param)
            if type(typ) == ArrayType and type(init_type) == ArrayType:
                if typ.dimensions != init_type.dimensions or typ.typ != init_type.typ:
                    raise TypeMismatchInVarDecl(ast)
            else:
                if type(init_type) == AutoType:
                    self.setAuto([ast.init], typ, param)
                elif type(typ) != type(init_type):
                    if not (type(typ) == FloatType and type(init_type) == IntegerType):
                        raise TypeMismatchInVarDecl(ast)
        param[0][ast.name] = typ
        # print(param[0][ast.name])

    def visitParamDecl(self, ast, param): 
        # check if parameter redeclared in current Fucntion
        if ast.name in param[0]:
            inheritFunc = self.parentFunction
            # check if it redeclared parameter in parent Function with "inherit"
            if inheritFunc is not None and not self.preventFlag:
                parentParam = inheritFunc.params
                for i in parentParam:
                    if i.name == ast.name and i.inherit == True:
                        raise Invalid(Parameter(), ast.name)

            raise Redeclared(Parameter(), ast.name)
        else:
            param[0][ast.name] = ast.typ

    def visitFuncDecl(self, ast, param): 
        ## first travel get prototype
        if self.numTravel == 0:
            if ast.name not in param[0]:
                param[0][ast.name] = ast
        ## second travel to check type
        else:
            name = ast.name
            # check name function
            if name in param[0]:
                # print(param[0][name])
                raise Redeclared(Function(), name)

            funcdecl = self.listFunction[name]
            self.currentFunction = funcdecl

            parentname = ast.inherit
            # print(parentname)
            parentdecl = ""
            # check inherit function
            if parentname is not None:
                if parentname not in self.listFunction:
                    raise Undeclared(Function(), parentname)
                parentdecl = self.listFunction[parentname]
                self.parentFunction = parentdecl
            
            # infered auto function if it called before
            if type(ast.return_type) == AutoType:
                if ast.name in self.waitingInfered:
                    self.currentFunction.return_type = self.waitingInfered[name]
                    self.waitingInfered.pop(name)

            Funcbody = funcdecl.body # get BlockStmt
            lstStmtBody = Funcbody.body # get list Stmt

            # check first Stmt
            lsttmp = ['super', 'preventDefault']
            firstStmt = lstStmtBody[0] if len(lstStmtBody) > 0 else None
            if self.parentFunction is not None:
                if len(self.parentFunction.params) != 0: 
                    if not (type(firstStmt) == CallStmt and firstStmt.name in lsttmp):
                        raise InvalidStatementInFunction(name)  

                if type(firstStmt) == CallStmt and firstStmt.name == 'preventDefault':
                        self.preventFlag = True
            else:
                if type(firstStmt) == CallStmt and firstStmt.name in lsttmp:
                    raise InvalidStatementInFunction(name)  

            env = [{}] + param

            # take param inherit from dad
            if self.parentFunction is not None and not self.preventFlag:
                for i in self.parentFunction.params:
                    if i.name not in env[0] and i.inherit == True:
                        env[0][i.name] = i.typ
            # check list param
            lstparam = funcdecl.params
            for i in lstparam:
                self.visit(i, env)

            self.envParamFunction = env[0]


            # check body
            self.visit(Funcbody, param)

            if self.numReturn == 0 and type(self.currentFunction.return_type) == AutoType:
                self.currentFunction.return_type = VoidType()

            self.numReturn = 0

            # update all param in the body
            for i in self.waitingParam:
                if self.parentFunction is not None and not self.preventFlag:
                    for j in self.parentFunction.params:
                        if i == j.name and j.inherit == True:
                            j.typ = self.waitingParam[i]

                for j in self.currentFunction.params:
                    if i == j.name:
                        j.typ = self.waitingParam[i]

            self.waitingParam = {}

            # update prototype of func child and parent
            param[0][name] = self.currentFunction
            # print(param)
            if self.parentFunction is not None :
                if parentname in param[0]:
                    # print("got u")
                    param[0][parentname] = self.parentFunction
                self.listFunction[parentname] = self.parentFunction
            # print(param)
            self.currentFunction = None
            self.parentFunction = None
            self.preventFlag = False

    def visitProgram(self, ast, param): 
        for decl in ast.decls:
            if type(decl) == FuncDecl:
                self.visit(decl, [self.listFunction])

        self.numTravel = 1

        for decl in ast.decls:
            self.visit(decl, param)       

        if 'main' not in self.listFunction:
            raise NoEntryPoint()
        else:
            typ = self.listFunction['main']
            if not (isinstance(typ, FuncDecl) and isinstance(typ.return_type, VoidType) and len(typ.params) == 0 and typ.inherit is None):
                raise NoEntryPoint()

