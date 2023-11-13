from PyQt6.QtWidgets import QLabel,QWidget, QVBoxLayout
from PyQt6.QtCore import Qt
from instr import *
class Th_Win(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.init_UI()

    def set_appear(self):
        self.setWindowTitle("beton3")
        self.resize(1020, 600)
        self.show()

    def init_UI(self):
        line = QVBoxLayout()
        index = QLabel(txt_index)
        results = QLabel(txt_workheart)
        line.addWidget(index, alignment=Qt.AlignmentFlag.AlignCenter)
        line.addWidget(results, alignment=Qt.AlignmentFlag.AlignCenter)
        self.setLayout(line)



















