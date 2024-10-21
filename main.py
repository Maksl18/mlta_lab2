from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication
from datatypes.graph import create_directed_graph, create_undirected_graph
from ui import MainWindow

class Main(MainWindow):

    def __init__(self):
        super(Main, self).__init__()

        self.btn_generate.clicked.connect(self.btn_generate_click)

    def btn_generate_click(self):
        graph_type: int = self.cb_graph_type.currentIndex()
        traverse_type: int = self.cb_traverse_type.currentIndex()
        graph = create_directed_graph()

        if graph_type == 0:
            graph = create_directed_graph()
        elif graph_type == 1:
            graph = create_undirected_graph()

        self.vertices = [node.data for node in graph.node_list]

        if traverse_type == 0:
            self.tb_traverse.setText(graph.depth_first_search(self.cb_vertex.currentIndex()))
        elif traverse_type == 1:
            self.tb_traverse.setText(graph.breath_first_search(self.cb_vertex.currentIndex()))

        self.img_graph.setPixmap(QPixmap('./media/graph.png'))

def main():
    app = QApplication([])
    window = Main()
    window.show()
    app.exec()

if __name__ == '__main__':
    main()
