

%{
#include <stdio.h>
void yyerror(const char *s) { printf("Error: %s\n", s); }
int yylex(void);
int vars[26]; // a-z ke liye variables store karne ka array
%}
%union { int num; char *str; }  // Values ke types
%token <num> NUMBER             // Number token
%token <str> STRING ID          // String aur ID token
%token TRUE FALSE ASSIGN PRINT PLUS MINUS MULT DIV  // Keywords aur operators
%type <num> expr                // Expression ka type
%%
program: statements             // Program mein statements hote hain
statements: statement           // Ek statement
          | statements statement // Ya kai statements
statement: ID ASSIGN expr { vars[$1[0] - 'a'] = $3; } // x = value
         | PRINT expr     { printf("Output: %d\n", $2); }   // Print number
         | PRINT STRING   { printf("Output: %s\n", $2); }   // Print string
expr: NUMBER             { $$ = $1; }         // Number
    | ID                 { $$ = vars[$1[0] - 'a']; } // Variable value
    | expr PLUS expr     { $$ = $1 + $3; }    // +
    | expr MINUS expr    { $$ = $1 - $3; }    // -
    | expr MULT expr     { $$ = $1 * $3; }    // *
    | expr DIV expr      { $$ = $1 / $3; }    // /
%%
int main() { return yyparse(); }  // Program start karne ke liye