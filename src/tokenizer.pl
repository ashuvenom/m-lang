:- module(tokenizer, [tokenize/2]).

tokenize(Input, Tokens) :-
    atom_chars(Input, Chars),
    tokenize_chars(Chars, Tokens).

tokenize_chars([], []).
tokenize_chars([H|T], Tokens) :-
    ( is_space(H) -> tokenize_chars(T, Tokens)
    ; H = ';' -> Tokens = [';'|Rest], tokenize_chars(T, Rest)
    ; H = '"' -> collect_string(T, Str, Rest),
                 Tokens = [string(Str)|RestTokens],
                 tokenize_chars(Rest, RestTokens)
    ; is_alpha(H) -> collect_identifier([H|T], Id, Rest),
                     ( keyword(Id, Tok) -> Tokens = [Tok|RestTokens]
                     ; Tokens = [id(Id)|RestTokens] ),
                     tokenize_chars(Rest, RestTokens)
    ; Tokens = [unknown(H)|Rest], tokenize_chars(T, Rest)
    ).

collect_string(Chars, Str, Rest) :-
    collect_string_chars(Chars, [], StrChars, Rest),
    reverse(StrChars, RevChars),
    atom_chars(Str, RevChars).

collect_string_chars(['"'|T], Acc, Acc, T).
collect_string_chars([H|T], Acc, Str, Rest) :-
    H \= '\n',
    collect_string_chars(T, [H|Acc], Str, Rest).
collect_string_chars([], _, _, _) :-
    throw(error('Unterminated string', [])).

collect_identifier([H|T], Id, Rest) :-
    ( is_alpha(H) ; is_digit(H) ; H = '_' ),
    collect_identifier_chars(T, [H], IdChars, Rest),
    reverse(IdChars, RevChars),
    atom_chars(Id, RevChars).
collect_identifier([], Id, []) :- atom_chars(Id, []).
collect_identifier([H|T], Acc, Id, [H|T]) :- \+ (is_alpha(H) ; is_digit(H) ; H = '_'), 
    reverse(Acc, RevAcc), atom_chars(Id, RevAcc).

collect_identifier_chars([], Acc, Acc, []).
collect_identifier_chars([H|T], Acc, Id, Rest) :-
    ( is_alpha(H) ; is_digit(H) ; H = '_' ),
    collect_identifier_chars(T, [H|Acc], Id, Rest).
collect_identifier_chars([H|T], Acc, Acc, [H|T]) :- \+ (is_alpha(H) ; is_digit(H) ; H = '_').

keyword(tell, tell).