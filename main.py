import sys
from random import randint
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QPainter, QColor
from PyQt5 import uic


class Arifmometr(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.flag = False
        self.pushButton.clicked.connect(self.pushed)

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.draw_el(qp)
        qp.end()

    def draw_el(self, qp):
        if self.flag:
            rad = randint(1, 40)
            qp.setBrush(QColor(255, 255, 0))
            qp.drawEllipse(30, 30, rad * 2, rad * 2)
            rad = randint(1, 40)
            qp.drawEllipse(140, 30, rad * 2, rad * 2)

    def pushed(self):
        self.flag = True
        self.repaint()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ev = Arifmometr()
    ev.show()
    sys.exit(app.exec())
