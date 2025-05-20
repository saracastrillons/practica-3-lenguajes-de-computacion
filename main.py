import sys
from parser import SANParser
from visualizer import TreeVisualizer

def main():
    if len(sys.argv) != 2:
        print("Uso: python main.py partida.san")
        sys.exit(1)

    ruta = sys.argv[1]
    text = open(ruta, encoding="utf-8").read()
    parser = SANParser(text)

    try:
        turns = parser.parse()
    except ValueError as e:
        print("Error de sintaxis:", e)
        sys.exit(1)

    viz = TreeVisualizer(turns)
    viz.show()

if __name__ == "__main__":
    main()
