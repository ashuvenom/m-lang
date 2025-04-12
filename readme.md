# Movie Language

MovieLang is a simple story-teller programming language inspired by cinematic storytelling and Marathi cultural flavor. This language was built as a team project to implement a lexer, parser, and interpreter using ANTLR and Python. It supports core operations like variable declarations, printing, arithmetic, and control flow.

## 👨‍💻 Team

- Ashutosh Kumbhar  
- Rajesh Sawant  
- Girish Nalawade  
- Mitesh Parab 


## 🧰 Tools Used

- **ANTLR (v4)**: For lexical analysis and parser generation (`MovieCode.g4`)
- **Python**: Interpreter runtime (`main.py`, `MovieInterpreter.py`)
- **Git**: Version control

## 🧱 Setup & Installation

### On Linux (Ubuntu)

```bash
sudo apt update

sudo apt install default-jre python3-pip -y

pip3 install antlr4-tools

pip install antlr4-python3-runtime

```

---

### On Windows (Powershell)

Install WSL on windows
```bash
wsl --install
```
Open Ubuntu terminal and run:

```bash
sudo apt update
sudo apt install default-jre python3-pip -y
pip install antlr4-python3-runtime
```

---

### On MacOS (zsh/bash)

Install openjdk and python3
```bash
brew install openjdk python3
pip3 install antlr4-python3-runtime
```

---

## ⚙️ Compilation

```bash
cd src

#Generate Lexer, Parser, and Visitor in the src folder itself.

java -Xmx500M -cp ".:antlr-4.13.0-complete.jar" org.antlr.v4.Tool -Dlanguage=Python3 -visitor -listener MarathiCode.g4

# This generates 4 files :

# 1. MovieCodeLexer.py
# 2. MovieCodeParser.py
# 3. MovieCodeVisitor.py
# 4. MovieCodeListener.py

```

## ▶️ Running a Program

```bash
cd src
python3 main.py ../data/sample.mc
```





