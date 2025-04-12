### Adding Boolean Support to MLang

#### Overview
The MLang programming language has been enhanced to support basic boolean operations. This includes the addition of boolean literals (`true` and `false`) and logical operators (`andAlso`, `orElse`, and `not`). These changes align with Python's boolean logic rules.

---

### Changes Made

#### 1. Grammar Updates (`mlang.g4`)
- Added support for boolean literals (`true` and `false`) using the `BOOL` token.
- Updated the `expr` rule to include:
  - `andAlso` for logical AND.
  - `orElse` for logical OR.
  - `not` for logical NOT.

**Updated Grammar:**
```antlr
expr
    : expr op=('*'|'/') expr
    | expr op=('+'|'-') expr
    | expr op=('andAlso'|'orElse') expr
    | 'not' expr
    | BOOL
    | INT
    | ID
    ;
```
