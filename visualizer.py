import sys
from PyQt5.QtWidgets import QApplication, QTreeWidget, QTreeWidgetItem

class TreeVisualizer:
    def __init__(self, turns):
        self.turns = turns

    def show(self):
        app = QApplication(sys.argv)
        tree = QTreeWidget()
        tree.setHeaderLabels(["Etiqueta", "Jugada"])

        root = QTreeWidgetItem(["Partida", ""])
        tree.addTopLevelItem(root)

        for num, w, b in self.turns:
            turn_node = QTreeWidgetItem([f"Turno {num}", ""])
            root.addChild(turn_node)

            white_node = QTreeWidgetItem(["Blancas", w])
            turn_node.addChild(white_node)

            black_move = b if b else "–"
            black_node = QTreeWidgetItem(["Negras", black_move])
            turn_node.addChild(black_node)

        tree.expandAll()
        tree.setWindowTitle("Árbol de Turnos SAN")
        tree.resize(400, 600)
        tree.show()
        sys.exit(app.exec_())
