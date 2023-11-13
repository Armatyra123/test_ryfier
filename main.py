from PyQt6.QtWidgets import QWidget, QApplication, QVBoxLayout, QLabel, QPushButton
from instr import *
from sec_win import SecWin
class MainWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.init_UI()
        self.connects()

    def set_appear(self):
        self.setWindowTitle("beton1")
        self.resize(1000, 600)

    def init_UI(self):
        line = QVBoxLayout()
        label = QLabel(txt_hello)
        label1 = QLabel(txt_instruction)
        self.baton = QPushButton(txt_next)
        line.addWidget(label)
        line.addWidget(label1)
        line.addWidget(self.baton)
        self.setLayout(line)
    def connects(self):
        self.baton.clicked.connect(self.next)

    def next(self):
        self.sw = SecWin()
        self.hide()

main = QApplication([])
window = MainWin()
window.show()
main.exec()
















