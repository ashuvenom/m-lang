# EBNF Grammar for Mlang

The following Extended Backus–Naur Form (EBNF) defines the core structure of mlang programs:


program         ::= { statement } EOF ;

statement       ::= variableDecl
                  | assignStmt
                  | printStmt
                  | ifStmt
                  | whileStmt
                  | forStmt
                  | breakStmt
                  | continueStmt
                  | functionDecl
                  | functionCall
                  | returnStmt ;

variableDecl    ::= "cast" ID "is" expr ";" ;
assignStmt      ::= ID "is" expr ";" ;
printStmt       ::= "say" expr ";" ;

ifStmt          ::= "cutIf" expr "action" { statement } "cut"
                    { elifStmt } [ elseStmt ] ;

elifStmt        ::= "altCut" expr "action" { statement } "cut" ;
elseStmt        ::= "plotTwist" "action" { statement } "cut" ;

whileStmt       ::= "rollWhile" expr "action" { statement } "cut" ;

forStmt         ::= "montage" variableDecl expr ";" assignStmt
                    "action" { statement } "cut" ;

breakStmt       ::= "pause" ";" ;
continueStmt    ::= "replay" ";" ;

functionDecl    ::= "scene" ID [ "with" paramList ] "action"
                    { statement } "cut" ;

functionCall    ::= functionCallExpr ";" ;
functionCallExpr::= "call" ID [ "with" argList ] ;

returnStmt      ::= "wrap" expr ";" ;

paramList       ::= ID { "," ID } ;
argList         ::= expr { "," expr } ;

expr            ::= expr "cut?" expr "plotTwist" expr         
                  | expr "*" expr
                  | expr "/" expr
                  | expr "%" expr
                  | expr "+" expr
                  | expr "-" expr
                  | expr "andAlso" expr
                  | expr "orElse" expr
                  | expr "sameAs" expr
                  | expr "notSame" expr
                  | expr "smallerThan" expr
                  | expr "biggerThan" expr
                  | expr "biggerOrEqual" expr
                  | expr "smallerOrEqual" expr
                  | "not" expr
                  | functionCallExpr
                  | BOOL
                  | INT
                  | STRING
                  | ID ;

BOOL            ::= "truth" | "lie" ;
ID              ::= (letter | "_") { letter | digit | "_" } ;
INT             ::= digit { digit } ;
STRING          ::= '"' { any-character-except-quote-or-newline } '"' ;
COMMENT         ::= "note:" { any-character-except-newline } ;