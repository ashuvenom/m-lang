grammar mlang;

program: statement* EOF;

statement
    : variableDecl
    | assignStmt
    | printStmt
    | ifStmt
    | whileStmt
    | forStmt
    | breakStmt
    | continueStmt
    ;

variableDecl: 'cast' ID 'is' expr ';';
assignStmt: ID 'is' expr ';';
printStmt: 'say' expr ';';

ifStmt
    : 'cutIf' expr 'action' statement* 'cut' (elifStmt)* (elseStmt)?
    ;

elifStmt
    : 'altCut' expr 'action' statement* 'cut'
    ;

elseStmt
    : 'plotTwist' 'action' statement* 'cut'
    ;

whileStmt
    : 'rollWhile' expr 'action' statement* 'cut'
    ;

forStmt
    : 'montage' variableDecl expr ';' assignStmt 'action' statement* 'cut'
    ;

breakStmt: 'pause' ';';
continueStmt: 'replay' ';';

expr
    : expr op=('*'|'/'|'%') expr
    | expr op=('+'|'-') expr
    | expr op=('andAlso'|'orElse') expr
    | expr op=('sameAs'|'notSame'|'smallerThan'|'biggerThan'|'biggerOrEqual'|'smallerOrEqual') expr
    | 'not' expr
    | BOOL
    | INT
    | STRING
    | ID
    ;

BOOL: 'truth' | 'lie';
ID: [a-zA-Z_][a-zA-Z0-9_]*;
INT: [0-9]+;
STRING: '"' (~["\r\n])* '"';
WS: [ \t\r\n]+ -> skip;
COMMENT: 'note:' ~[\r\n]* -> skip;
