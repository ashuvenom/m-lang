grammar mlang;

program: statement* EOF;

statement
    : variableDecl
    | assignStmt
    | printStmt
    ;

variableDecl: 'cast' ID 'is' expr ';';
assignStmt: ID 'is' expr ';';
printStmt: 'say' expr ';';

expr
    : expr op=('*'|'/'|'%') expr
    | expr op=('+'|'-') expr
    | expr op=('andAlso'|'orElse') expr
    | expr op=('smallerThan'|'greaterThan'|'greaterThanOrEqualTo'|'lessThanOrEqualTo') expr
    | 'not' expr
    | BOOL
    | INT
    | ID
    ;

BOOL: 'truth' | 'lie';
ID: [a-zA-Z_][a-zA-Z0-9_]*;
INT: [0-9]+;
WS: [ \t\r\n]+ -> skip;
MOD: '%'; 