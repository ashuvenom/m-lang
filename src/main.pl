:- use_module(tokenizer).
:- use_module(parser).

main :-
    ( current_prolog_flag(argv, [File]) ->
        ( exists_file(File) ->
            read_file_to_string(File, Content, []),
            write('File Content: '), writeln(Content),
            ( tokenize(Content, Tokens) ->
                write('Tokens: '), writeln(Tokens),
                ( parse(Tokens, AST) ->
                    write('AST: '), writeln(AST)
                ; write('Error: Parsing failed'), nl, fail
                )
            ; write('Error: Tokenization failed'), nl, fail
            )
        ; write('Error: File not found: '), writeln(File), fail
        )
    ; write('Usage: swipl -s src/main.pl <filename>'), nl, fail
    ).

:- main.