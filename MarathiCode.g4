grammar MarathiCode;

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
    : expr op=('*'|'/') expr
    | expr op=('+'|'-') expr
    | INT
    | ID
    ;

ID: [a-zA-Z_][a-zA-Z0-9_]*;
INT: [0-9]+;
WS: [ \t\r\n]+ -> skip;
