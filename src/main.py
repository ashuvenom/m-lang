import sys
import os

# Ensure imports from src/ work
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "src"))

from antlr4 import *
from mlangLexer import mlangLexer
from mlangParser import mlangParser
from mlangInterpreter import mlangInterpreter
from antlr4.tree.Trees import Trees
import pydot

def tree_to_dot(tree, parser, filename="tree.png"):
    nodes = []
    edges = []
    count = [0]

    def walk(t, parent_id=None):
        node_text = Trees.getNodeText(t, parser.ruleNames)
        my_id = count[0]
        count[0] += 1
        nodes.append((my_id, node_text))
        if parent_id is not None:
            edges.append((parent_id, my_id))
        for i in range(t.getChildCount()):
            walk(t.getChild(i), my_id)
    walk(tree)

    graph = pydot.Dot(graph_type='digraph')
    for node_id, label in nodes:
        graph.add_node(pydot.Node(str(node_id), label=label))
    for src, dst in edges:
        graph.add_edge(pydot.Edge(str(src), str(dst)))

    graph.write_png(filename)
    print(f"✅ Parse tree saved as {filename}")

def main():
    input_file_path = sys.argv[1]
    input_stream = FileStream(input_file_path)
    lexer = mlangLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = mlangParser(stream)
    tree = parser.program()

    print(tree.toStringTree(recog=parser))  # console parse tree

    base_name = os.path.splitext(os.path.basename(input_file_path))[0]
    project_root = os.path.dirname(os.path.dirname(__file__))  
    tree_dir = os.path.join(project_root, "data", "trees")
    os.makedirs(tree_dir, exist_ok=True)
    output_file = os.path.join(tree_dir, f"{base_name}tree.png")

    tree_to_dot(tree, parser, output_file)

    interpreter = mlangInterpreter()
    interpreter.visit(tree)

if __name__ == '__main__':
    main()