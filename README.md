# 🎬 mlang

mlang is a simple, cinematic storytelling-inspired programming language designed to feel like writing a screenplay. Built using ANTLR and Python, mlang supports essential programming features such as variable declarations, arithmetic expressions, print statements, and more — all expressed with a theatrical twist.

---


## 👥 Team Members

- Ashutosh Kumbhar  
- Rajesh Sawant  
- Girish Nalawade  
- Mitesh Parab  

---

## 🛠️ Tools & Technologies

- 🧠 **ANTLR v4** – Grammar-based lexer and parser generation (`mlang.g4`)
- 🐍 **Python** – Interpreter and runtime execution (`main.py`, `mlangInterpreter.py`)
- 🌳 **Graphviz + pydot** – For generating visual parse trees (`sampletree.png`)
- 💻 **Git** – Version control

---

## 📦 Installation

### 🔁 Requirements

Install ANTLR runtime and related packages:

```bash
pip install antlr4-python3-runtime pydot

---

### 🐧 On Linux (Ubuntu)

```bash
sudo apt update
sudo apt install default-jre python3-pip -y
pip install antlr4-python3-runtime

🪟 On Windows (Using WSL)
wsl --install
# Inside Ubuntu (WSL):
**Open Ubuntu terminal and run:**
sudo apt update
sudo apt install default-jre python3-pip graphviz -y
pip install antlr4-python3-runtime pydot


🍎 On Mac (Homebrew must be installed)
brew install openjdk python3 graphviz
pip3 install antlr4-python3-runtime pydot


⚙️ Compilation

cd into src . 

1. Run the below command in :
wget https://www.antlr.org/download/antlr-4.13.0-complete.jar

or using Curl

curl -O https://www.antlr.org/download/antlr-4.13.0-complete.jar


2. Generate Lexer, Parser, and Visitor in the src folder 
java -Xmx500M -cp "antlr-4.13.0-complete.jar" org.antlr.v4.Tool -Dlanguage=Python3 -visitor -listener mlang.g4 -o .

This generates 4 files :

1. mlangLexer.py
2. mlangParser.py
3. mlangVisitor.py
4. mlangListener.py

▶️ Running a Program
python3 main.py data/sample.mlang
