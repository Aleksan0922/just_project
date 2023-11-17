import sys
from random import randint
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QPainter, QColor
from UI import Ui_MainWindow


class Arifmometr(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.flag = False
        self.pushButton.clicked.connect(self.pushed)

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.draw_el(qp)
        qp.end()

    def draw_el(self, qp):
        if self.flag:
            rad = randint(10, 50)
            r = randint(0, 255)
            g = randint(0, 255)
            b = randint(0, 255)
            qp.setBrush(QColor(r, g, b))
            qp.drawEllipse(30, 30, rad * 2, rad * 2)
            rad = randint(10, 50)
            r = randint(0, 255)
            g = randint(0, 255)
            b = randint(0, 255)
            qp.setBrush(QColor(r, g, b))
            qp.drawEllipse(140, 30, rad * 2, rad * 2)

    def pushed(self):
        self.flag = True
        self.repaint()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ev = Arifmometr()
    ev.show()
    sys.exit(app.exec())
