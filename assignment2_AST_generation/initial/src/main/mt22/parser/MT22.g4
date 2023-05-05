// 2052486
grammar MT22;

@lexer::header {
from lexererr import *
}

options{
	language=Python3;
}

program: declarations EOF;

declarations
	: declaration declarations2
	| 
	;

declarations2
	: declaration declarations2
	|
	;

declaration
	: var_declaration 
	| funct_declaration
	;

var_declaration
	: var_dec
	| param_dec
	;

var_dec
	: var_dec_short SMCOLON
	| var_dec_full SMCOLON
	;

var_dec_short
	: id_list COLON var_type
	;

var_type
	: atomic_type
	| array_type_decl
	;

id_list
	: ID id_list2
	| ID
	;

id_list2
	: COMMA ID id_list2
	| 
	;

var_dec_full
	: ID COMMA var_dec_full COMMA expression
	| ID COLON var_type2 ASSIGN expression
	;

var_type2
	: var_type
	| AUTO
	;

param_dec
	: INHERIT? OUT? ID COLON var_type2
	;

funct_declaration
	: ID COLON FUNCTION var_type3 LB param_list RB inherit_func block_Statement
	;

param_list
	: param_dec param_list2
	| 
	;

param_list2
	: COMMA param_dec param_list2
	| 
	;

inherit_func
	: INHERIT ID
	| 
	;

var_type3
	: var_type2
	| void_type
	;

ele_array_list
	: expression ele_array_list2 
	| 
	;

ele_array_list2
	: COMMA expression ele_array_list2 
	| 
	;

// Element type
void_type
	: VOID
	;

atomic_type
	: BOOLEAN
	| INTEGER
	| STRING
	| FLOAT
	;

// array declare
array_type_decl
	: ARRAY array_type_dimension OF atomic_type
	;

array_type_dimension
	: LSB dimension_size_list RSB
	;

dimension_size_list
	: INT_LIT dimension_size_list2
	| INT_LIT
	;

dimension_size_list2
	: COMMA INT_LIT dimension_size_list2
	| 
	;

// Expression

expr_list
	: expression expr_list2
	| expression
	;

expr_list2
	: COMMA expression expr_list2
	| 
	;

expression
	: string_expression
	;

string_expression
	: relational_expression
	| relational_expression DCOLON relational_expression
	;

relational_expression
	: logical_expression
	| logical_expression relational_operator logical_expression
	;

logical_expression
	: adding_expression
	| logical_expression logical_operator adding_expression 
	;


adding_expression
	: multiplying_expression
	| adding_expression adding_operator multiplying_expression 
	;

multiplying_expression
	: not_expression
	| multiplying_expression multiplying_operator not_expression
	;

not_expression
	: not_operator not_expression
	| sign_expression
	;

sign_expression
	: index_expression
	| sign_operator sign_expression 
	;


index_expression
	: ID index_operator
	| expr_ele
	;

expr_ele
	: LB expression RB
	| full_literal
	| ID
	| function_call
	;

index_operator
	: LSB expr_list RSB 
	;

not_operator
	: NOT
	;

sign_operator
	: SUB
	;

multiplying_operator
	: MUL
	| DIV
	| MOD
	;

adding_operator
	: ADD
	| SUB
	;

logical_operator
	: AND
	| OR
	;

relational_operator
	: EQUAL
	| UNEQUAL
	| LT
	| GT
	| LTE
	| GTE 
	;

function_call
	: ID LB argument_list RB 
	;

argument_list
	: expression argument_list2
	|
	;

argument_list2
	: COMMA expression argument_list2
	| 
	;

// Statement
statement
	: assignment_Statement 
	| if_Statement
	| for_Statement
	| while_Statement
	| do_while_Statement
	| break_Statement
	| continue_Statement
	| return_Statement
	| call_Statement
	| block_Statement
	;

assignment_Statement
	: lhs ASSIGN expression SMCOLON
	;

lhs
	: scalar_var 
	| ID index_operator
	;

scalar_var: ID; 

if_Statement
	: IF LB expression RB statement (ELSE statement)?
	;

for_Statement
	: FOR LB lhs ASSIGN expression COMMA expression COMMA expression RB statement
	;

while_Statement
	: WHILE LB expression RB statement
	;

do_while_Statement
	: DO block_Statement WHILE LB expression RB SMCOLON
	;

break_Statement
	: BREAK SMCOLON
	;

continue_Statement
	: CONTINUE SMCOLON
	;

return_Statement
	: RETURN expression? SMCOLON
	;

call_Statement
	: function_call SMCOLON
	; // not join to any expression, like void	

block_Statement
	: LCB block_list RCB
	;

block_list
	: block_ele block_list2
	|
	;

block_list2
	: block_ele block_list2
	| 
	;

block_ele
	: var_dec
	| statement
	;

int_literal: INT_LIT;
float_literal: FLOAT_LIT;
bool_literal: TRUE | FALSE;
string_literal: STRING_LIT;

normal_literal
	: int_literal
	| float_literal
	| bool_literal
	| string_literal
	;

arry_literal
	: LCB ele_array_list RCB
	;

full_literal
	: normal_literal
	| arry_literal
	;

//------------------------------------------------------//

// operators
ADD: '+';
SUB: '-';
MUL: '*';
DIV: '/';
MOD: '%';
NOT: '!';
AND: '&&';
OR: '||';
EQUAL: '==';
UNEQUAL: '!=';
LT: '<';
LTE: '<=';
GT: '>';
GTE: '>=';
DCOLON: '::';
fragment UNDERSCORE: '_';

// Seperator
LB: '(';
RB: ')';
LSB: '[';
RSB: ']';
LCB: '{';
RCB: '}';
DOT: '.';
COMMA: ',';
COLON: ':';
SMCOLON: ';';
ASSIGN: '=';


// Keys
ARRAY: 'array';
AUTO: 'auto';
BREAK: 'break';
BOOLEAN: 'boolean';
DO: 'do';
ELSE: 'else';
FALSE: 'false';
FLOAT: 'float';
FOR: 'for';
FUNCTION: 'function';
IF: 'if';
INTEGER: 'integer';
RETURN: 'return';
STRING: 'string';
TRUE: 'true';
VOID: 'void';
WHILE: 'while';
OUT: 'out';
CONTINUE: 'continue';
OF: 'of';
INHERIT: 'inherit';

ID: [a-zA-Z_] [a-zA-Z0-9_]*;

// Literal
INT_LIT
	:  INT_PART
	{
		self.text = self.text.replace('_','')
	}
	;

FLOAT_LIT
	: INT_PART DECPART
	{
		self.text = self.text.replace('_','')
	} 
	| INT_PART DECPART? EXP
	{
		self.text = self.text.replace('_','')
	}
	| INT_PART? DECPART EXP
	{
		self.text = self.text.replace('_','')
	}
	;

fragment DIGIT_Z: [0-9];
fragment DIGIT_N: [1-9];
fragment INT_PART: ( '0' | DIGIT_N ( UNDERSCORE? DIGIT_Z )*); 
fragment DECPART: DOT DIGIT_Z*;
fragment EXP: [eE] ( '-' | '+' )? DIGIT_Z+; 

// fragment STRING_C: ;

STRING_LIT
	: '"' STRING_SEQUENCE? '"' 
	{
		self.text = self.text[1:-1]
	}
	;

// fragment STRING_SEQUENCE: ( ~('\\' ~[bfrnt'"\\]) | ESCAPE_C)+;
fragment STRING_SEQUENCE: ( ~[\n\r"\\] | ESCAPE_C)+;

fragment ESCAPE_C: '\\' [bfrnt'"\\];
fragment ILLEGAL_C: '\\' ~[bfrnt'"\\];


BLOCK_COMMENT: '/*' .*? '*/' -> skip;
INLINE_COMMENT: '//' ~[\n\r]* -> skip;

WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines


ERROR_CHAR: . {raise ErrorToken(self.text)};

UNCLOSE_STRING
	: '"' STRING_SEQUENCE?
	{
		self.text = self.text[1:]
		raise UncloseString(self.text)
	}
	;

ILLEGAL_ESCAPE
	: '"' STRING_SEQUENCE? ILLEGAL_C
	{
		self.text = self.text[1:]
		raise IllegalEscape(self.text)
	}
	;
