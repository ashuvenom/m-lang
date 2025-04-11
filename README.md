# MarathiCode

MarathiCode is a simple programming language inspired by Marathi, designed as a team project to implement a lexical analyzer, parser, and runtime environment. The language supports basic operations like assignment, printing, arithmetic, conditionals, loops, and boolean operations with a Marathi flavor.

## Team
- Ashutosh Kumbhar 
- Rajesh Sawant 
- Girish Nalawade 
- Mitesh Parab 

## Tools
- **Flex**: For lexical analysis (`lexer.l`).
- **Bison**: For parsing (`parser.y`).
- **GCC**: For compiling C code.
- **Git**: For version control.

## Installation
Before starting, ensure the following tools are installed:


### On Linux (Ubuntu)
```bash

sudo apt update
sudo apt install flex bison gcc git -y

```

### On Windows (Using WSL)
On Windows, use WSL: open PowerShell, run wsl --install, get Ubuntu from Microsoft Store, then in Ubuntu terminal:
```bash

sudo apt update
sudo apt install flex bison gcc git -y

```


### On Mac 
On Mac, install Xcode tools with xcode-select --install, then Homebrew with /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)", and finally:
```bash
brew install flex bison git
```

Check if everything’s installed:

```bash
flex --version
bison --version
gcc --version
git --version
```

## Compilation

Now, compile the project. From the MarathiCode folder, generate the lexer:

```bash
flex src/lexer.l
```

This creates src/lex.yy.c. Next, generate the parser:

```bash
bison -d src/parser.y
```

This makes src/parser.tab.c and src/parser.tab.h. Then, compile everything:
```bash
gcc src/lex.yy.c src/parser.tab.c -o marathi
```

This builds the marathi executable in src/. Or use one command:
```bash
flex src/lexer.l && bison -d src/parser.y && gcc src/lex.yy.c src/parser.tab.c -o marathi
```

To run a program, like the basic sample:
```bash
./marathi < data/sample.marathi
```

## Project Structure

To Do





