grammar MP;

@lexer::header {
from lexererr import *
}

options{
	language=Python3;
}

program: vardecls EOF;

vardecls: vardecl+;

vardecl: mptype ids SEMI;

mptype: INTTYPE | FLOATTYPE;

ids: ID (COMMA ids)*; 

INTTYPE: 'int';

FLOATTYPE: 'float';

SEMI: ';' ;

COMMA: ',' ;

ID: [a-z]+ ;

WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines

ERROR_CHAR: .;
