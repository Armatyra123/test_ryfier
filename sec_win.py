from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QLineEdit
from PyQt6.QtCore import Qt, QSize, QTime, QTimer
from PyQt6.QtGui import QFont
from instr import *
from third_window import Th_Win
class SecWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.init_UI()
        self.connects()

    def set_appear(self):
        self.setWindowTitle("beton2")
        self.resize(1200, 800)
        self.show()

    def init_UI(self):
        line = QVBoxLayout()
        name_input = QLineEdit("Ф.И.О.")
        age_input = QLineEdit("0")
        pulse1_input = QLineEdit("0")
        pulse2_input = QLineEdit("0")
        pulse3_input = QLineEdit("0")
        self.baton = QPushButton(txt_sendresults)
        self.baton.setFixedSize(QSize(1200, 30))
        self.s_f = QPushButton(txt_starttest1)
        self.s_s = QPushButton(txt_starttest2)
        self.s_t = QPushButton(txt_starttest3)
        self.timer_txt = QLabel("00:00:00")
        self.timer_txt.setFont(QFont("Times", 36))
        n_sn_tn = QLabel(txt_name)
        age = QLabel(txt_age)
        f_step = QLabel(txt_test1)
        s_step = QLabel(txt_test2)
        t_step = QLabel(txt_test3)
        line.addWidget(n_sn_tn, alignment=Qt.AlignmentFlag.AlignLeft)
        line.addWidget(name_input, alignment=Qt.AlignmentFlag.AlignLeft)
        line.addWidget(age, alignment=Qt.AlignmentFlag.AlignLeft)
        line.addWidget(age_input, alignment=Qt.AlignmentFlag.AlignLeft)
        line.addWidget(f_step, alignment=Qt.AlignmentFlag.AlignLeft)
        line.addWidget(self.s_f, alignment=Qt.AlignmentFlag.AlignLeft)
        line.addWidget(self.timer_txt, alignment=Qt.AlignmentFlag.AlignRight)
        line.addWidget(pulse1_input, alignment=Qt.AlignmentFlag.AlignLeft)
        line.addWidget(s_step, alignment=Qt.AlignmentFlag.AlignLeft)
        line.addWidget(self.s_s, alignment=Qt.AlignmentFlag.AlignLeft)
        line.addWidget(t_step, alignment=Qt.AlignmentFlag.AlignLeft)
        line.addWidget(self.s_t, alignment=Qt.AlignmentFlag.AlignLeft)
        line.addWidget(pulse2_input, alignment=Qt.AlignmentFlag.AlignLeft)
        line.addWidget(pulse3_input, alignment=Qt.AlignmentFlag.AlignLeft)
        line.addWidget(self.baton, alignment=Qt.AlignmentFlag.AlignCenter)
        self.setLayout(line)

    def connects(self):
        self.baton.clicked.connect(self.next)
        self.s_f.clicked.connect(self.timer1)
        self.s_s.clicked.connect(self.timer2)
        self.s_t.clicked.connect(self.timer3)

    def next(self):
        self.thw = Th_Win()
        self.hide()

    def timer1(self):
        global time
        time = QTime(0, 0, 15)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer1_event)
        self.timer.start(1000)

    def timer2(self):
        global time
        time = QTime(0, 0, 30)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer2_event)
        self.timer.start(1500)

    def timer3(self):
        global time
        time = QTime(0, 1, 0)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer3_event)
        self.timer.start(1000)

    def timer1_event(self):
        global  time
        time = time.addSecs(-1)
        self.timer_txt.setText(time.toString('hh:mm:ss'))
        self.timer_txt.setStyleSheet('color: rgb(0,0,0)')
        if time.toString('ss') == '00':
            self.timer.stop()

    def timer2_event(self):
        global  time
        time = time.addSecs(-1)
        self.timer_txt.setText(time.toString('ss'))
        self.timer_txt.setStyleSheet('color: rgb(0,0,0)')
        if time.toString('ss') == '00':
            self.timer.stop()

    def timer3_event(self):
        global  time
        time = time.addSecs(-1)
        self.timer_txt.setText(time.toString('hh:mm:ss'))
        if time.toString('ss') == '59':
            self.timer_txt.setStyleSheet('color: rgb(0,255,0)')
        if time.toString('ss') == '45':
            self.timer_txt.setStyleSheet('color: rgb(0,174,175)')
        if time.toString('ss') == '15':
            self.timer_txt.setStyleSheet('color: rgb(0,255,0)')
        if time.toString('ss') == '00':
            self.timer.stop()
            self.timer_txt.setStyleSheet('color: rgb(0,0,0)')




































