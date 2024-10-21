from PyQt5.QtCore import QSize
from PyQt5.QtGui import QMovie, QPixmap, QTextBlock
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QHBoxLayout, QLabel, \
    QComboBox, QSpacerItem, QSizePolicy, QTextEdit


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        label_font_size: int = 24
        self.vertices = []
        self.setWindowTitle("Лабораторна робота 2")
        self.setStyleSheet('font-size: 14px')
        self.setMinimumSize(QSize(1200, 560))

        # Layouts
        self.layout_main: QHBoxLayout = QHBoxLayout()

        self.layout_sidebar: QVBoxLayout = QVBoxLayout()
        self.layout_buttons_sub: QVBoxLayout = QVBoxLayout()
        self.layout_select_sub: QVBoxLayout = QVBoxLayout()

        self.layout_preview_sub: QHBoxLayout = QHBoxLayout()
        self.layout_graph_sub: QVBoxLayout = QVBoxLayout()
        self.layout_visual_sub: QVBoxLayout = QVBoxLayout()

        # Labels
        self.lbl_graph: QLabel = QLabel("Початковий граф")
        self.lbl_graph.setStyleSheet(f'font-size: {label_font_size}px')
        self.lbl_visual: QLabel = QLabel("Обхід графу")
        self.lbl_visual.setStyleSheet(f'font-size: {label_font_size}px')
        self.lbl_control: QLabel = QLabel("Керування")
        self.lbl_control.setStyleSheet(f"font-size: {label_font_size}px")
        self.lbl_graph_type: QLabel = QLabel("Тип графу")
        self.lbl_traverse_type: QLabel = QLabel("Тип обходу")
        self.lbl_vertex: QLabel = QLabel("Вершина")

        # Combo-boxes
        self.cb_graph_type: QComboBox = QComboBox()
        self.cb_graph_type.addItems(["Направлений", "Не направлений"])
        self.cb_traverse_type: QComboBox = QComboBox()
        self.cb_traverse_type.addItems(["В глибину", "В ширину"])
        self.cb_vertex: QComboBox = QComboBox()
        self.cb_vertex.addItems(['A', 'B', 'C', 'D', 'E', 'F'])

        # Displays
        self.img_graph: QLabel = QLabel()
        self.tb_traverse: QTextEdit = QTextEdit()
        self.tb_traverse.setStyleSheet('font-size: 28px')
        self.img_graph.setFixedSize(QSize(600, 500))
        self.tb_traverse.setDisabled(True)
        # Buttons
        self.btn_generate: QPushButton = QPushButton("Згенерувати")

        # Move elements
        self.main: QWidget = QWidget()
        self.main.setLayout(self.layout_main)
        self.setCentralWidget(self.main)

        # Main Layout
        self.layout_main.addLayout(self.layout_sidebar, 1)
        self.layout_main.addLayout(self.layout_preview_sub, 4)

        # Sidebar layout
        self.layout_sidebar.addWidget(self.lbl_control)
        self.layout_sidebar.addLayout(self.layout_select_sub)
        self.layout_sidebar.addLayout(self.layout_buttons_sub)
        self.layout_sidebar.addItem(QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding))
        self.layout_sidebar.addWidget(self.btn_generate)

        # Preview layout
        self.layout_preview_sub.addLayout(self.layout_graph_sub)
        self.layout_preview_sub.addLayout(self.layout_visual_sub)
        self.layout_graph_sub.addWidget(self.lbl_graph)
        self.layout_graph_sub.addWidget(self.img_graph)
        self.layout_visual_sub.addWidget(self.lbl_visual)
        self.layout_visual_sub.addWidget(self.tb_traverse)

        # Select layout
        self.layout_select_sub.addWidget(self.lbl_graph_type)
        self.layout_select_sub.addWidget(self.cb_graph_type)
        self.layout_select_sub.addWidget(self.lbl_traverse_type)
        self.layout_select_sub.addWidget(self.cb_traverse_type)
        self.layout_select_sub.addWidget(self.lbl_vertex)
        self.layout_select_sub.addWidget(self.cb_vertex)
