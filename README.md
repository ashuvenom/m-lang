# MCode

MCode is a simple story-teller programming language inspired by cinematic storytelling and Marathi cultural flavor. This language was built as a team project to implement a lexer, parser, and interpreter using ANTLR and Python. It supports core operations like variable declarations, printing, arithmetic, and control flow.

---

## 👨‍💻 Team

- Ashutosh Kumbhar  
- Rajesh Sawant  
- Girish Nalawade  
- Mitesh Parab  

---

## 🧰 Tools Used

- **ANTLR (v4)**: For lexical analysis and parser generation (`MarathiCode.g4`)
- **Python**: Interpreter runtime (`main.py`, `MarathiInterpreter.py`)
- **Git**: Version control

---

## 🧱 Installation

Before starting, make sure the required tools are installed:

1. pip install antlr4-tools
2. pip install antlr4-python3-runtime


---

### 🐧 On Linux (Ubuntu)

```bash
sudo apt update
sudo apt install default-jre python3-pip -y
pip install antlr4-python3-runtime

🪟 On Windows (Using WSL)
wsl --install

**Open Ubuntu terminal and run:**
sudo apt update
sudo apt install default-jre python3-pip -y
pip install antlr4-python3-runtime

🍎 On Mac (Homebrew must be installed)
brew install openjdk python3
pip3 install antlr4-python3-runtime


⚙️ Compilation

cd into your main folder structure.. 

1. Run the below command:
wget https://www.antlr.org/download/antlr-4.13.0-complete.jar

2. Generate Lexer, Parser, and Visitor in the main folder itself
java -Xmx500M -cp ".:antlr-4.13.0-complete.jar" org.antlr.v4.Tool -Dlanguage=Python3 -visitor -listener MarathiCode.g4

This generates 4 files :

1. MarathiCodeLexer.py
2. MarathiCodeParser.py
3. MarathiCodeVisitor.py
4. MarathiCodeListener.py

▶️ Running a Program
python3 main.py sample.mc

Project Structure:

Root-Level Files

MarathiCode.g4
Grammar file written in ANTLR v4 syntax. This defines the lexical and syntactic structure of the Marathi-inspired programming language (MCode).

MarathiCodeLexer.py, MarathiCodeParser.py, MarathiCodeListener.py, MarathiCodeVisitor.py
Auto-generated Python files created from the .g4 grammar using ANTLR. These form the lexer and parser components.

MarathiInterpreter.py
Main interpreter implementation. This file walks the parsed tree and executes logic according to the rules defined in MCode.

antlr-4.13.0-complete.jar
The complete ANTLR v4 tool used to generate lexer/parser code from .g4 grammar.

README.md
Project documentation explaining motivation, setup instructions, and contribution guide.

Intermediate & Runtime Files

.interp, .tokens Files
Intermediate files created by ANTLR during the generation process to help with syntax matching.

__pycache__/
Compiled Python bytecode for performance (automatically created when modules are imported).
