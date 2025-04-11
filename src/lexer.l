%{
#include "parser.tab.h"
%}
%option noyywrap
%%
"Kharay"    { return TRUE; }
"Khotay"    { return FALSE; }
"="         { return ASSIGN; }
"dakhva"    { return PRINT; }
"+"         { return PLUS; }
"-"         { return MINUS; }
"*"         { return MULT; }
"/"         { return DIV; }
[0-9]+      { yylval.num = atoi(yytext); return NUMBER; }
\"[^\"]*\"  { yylval.str = strdup(yytext); return STRING; }
[a-zA-Z]+   { yylval.str = strdup(yytext); return ID; }
[ \t\n]     ; // Spaces aur newlines ignore kar
.           { printf("Galat cheez: %s\n", yytext); }
%%