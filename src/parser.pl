:- module(parser, [parse/2]).
:- use_module(library(dcg/basics)).

parse(Tokens, AST) :-
    ( phrase(program(AST), Tokens) ->
        true
    ; write('Parser failed on tokens: '), writeln(Tokens), fail
    ).

program(AST) --> statements(AST).

statements([Stmt|Rest]) --> statement(Stmt), statements(Rest).
statements([]) --> [].

statement(print(Expr)) --> [tell], expression(Expr), [';'].

expression(literal(Str)) --> [string(Str)].