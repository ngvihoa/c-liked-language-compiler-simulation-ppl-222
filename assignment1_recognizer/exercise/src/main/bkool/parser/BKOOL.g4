grammar BKOOL;

@lexer::header {
from lexererr import *
}

options{
	language=Python3;
}

program: decl decls EOF;
decls: decl decls | ;

decl: vardecl | funcdecl;

vardecl: var_type idlist SEMI ;

idlist: ID idlist2 | ID;
idlist2: COMMA ID idlist2 | ;


funcdecl: var_type ID paramdecl body ;

paramdecl: LRB paramlist RRB;

paramlist: param paramlist2 | ;
paramlist2: SEMI param paramlist2 | ;

param: var_type idlist;

body: LCB  body_ele_list RCB;

body_ele_list: body_ele body_ele_list2 | ;
body_ele_list2: body_ele body_ele_list2 | ;

body_ele: vardecl | statement;

statement: statement_kind SEMI;

statement_kind: assignSt | callSt | returnSt;

assignSt: ID EQUAL expr;
callSt: ID LRB exprlist RRB;
returnSt: RETURN expr;

exprlist: expr exprlist2 | ;
exprlist2: COMMA expr exprlist2 | ;

expr: addexpr;

addexpr: subexpr ADD addexpr | subexpr;

subexpr: mulexpr SUB mulexpr | mulexpr;

mulexpr: mulexpr MUL divexpr | divexpr;

divexpr: divexpr DIV numlit | numlit;

numlit: INTLIT | FLOATLIT | ID | callSt | LRB subexpr RRB;

var_type: INT | FLOAT;

INT: 'int';
FLOAT: 'float';
SEMI: ';';
COMMA: ',';
LRB: '(';
RRB: ')';
LCB: '{';
RCB: '}';
EQUAL: '=';
ADD: '+';
SUB: '-';
MUL: '*';
DIV: '/';
RETURN: 'return';
INTLIT: INTPART;
FLOATLIT: INTPART DECPART;
fragment INTPART: ('0' | [1-9] [0-9]*);
fragment DECPART: '.' [0-9]+;

ID: [a-zA-Z]+;

//---------------- Q1 --------------------------

// fragment LITIP: ('2'[0-5]|'1'[0-9]|[1-9])?[0-9];
// IP: LITIP'.'LITIP'.'LITIP'.'LITIP;


//---------------- Q2 --------------------------

//ID: [a-z][a-z0-9]+;

//---------------- Q3 --------------------------

//REAL: INTPART DECPART | INTPART DECPART? EXP;
//fragment INTPART: [0-9]+;
//fragment DECPART: '.' [0-9]+;
//fragment EXP: [eE] '-'? [0-9]+; 

//---------------- Q4 --------------------------

//STRING: ['] (~['] | [']['])* ['];

//---------------- Q5 --------------------------

//ID: ('0' | [1-9] [0-9_]*) {self.text = self.text.replace('_','')};


WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines


ERROR_CHAR: .{raise ErrorToken(self.text)};
UNCLOSE_STRING: .;
ILLEGAL_ESCAPE: .;