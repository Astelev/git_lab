import sys
from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QPen, QColor
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow
import random


class UfoControl(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('01.ui', self)
        self.pushButton.clicked.connect(self.repaint)
    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.push(qp)
        qp.end()
    def push(self, qp):
        qp.setBrush(QColor(200, 150, 0))
        r = random.randint(10, 100)
        qp.drawEllipse(random.randint(10, 600), random.randint(10, 600), r, r)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = UfoControl()
    ex.show()
    sys.exit(app.exec())