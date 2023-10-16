from PyQt6.QtWidgets import QWidget, QApplication, QVBoxLayout, QLabel, QPushButton
class MainWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.init_UI()
        self.connects()

    def set_appear(self):
        self.setWindowTitle("massa")
        self.resize(1000, 600)

    def init_UI(self):
        line = QVBoxLayout()
        label = QLabel('ggg')
        label1 = QLabel("jjj")
        baton = QPushButton('press-idiot')
        line.addWidget(label)
        line.addWidget(label1)
        line.addWidget(baton)
        self.setLayout(line)
    def connects(self):
        pass

main = QApplication([])
window = MainWin()
window.show()
main.exec()
