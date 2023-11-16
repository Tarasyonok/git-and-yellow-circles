import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QColor, QPainter, QPen, QBrush
from PyQt5.QtCore import QPointF, Qt
from random import randint


class YellowCircles(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("UI.ui", self)
        self.do_paint = False
        self.drawButton.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw(qp)
            qp.end()

    def paint(self):
        self.drawButton.hide()
        self.do_paint = True
        self.repaint()

    def draw(self, qp):
        for i in range(randint(5, 10)):
            r = randint(20, 100) - 2
            x = randint(0, self.width())
            y = randint(0, self.height())
            color = QColor(255, 255, 0)
            qp.setBrush(QBrush(color, Qt.SolidPattern))
            qp.setPen(QPen(Qt.black, 1, Qt.SolidLine))
            qp.drawEllipse(QPointF(x, y), r, r)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    yc = YellowCircles()
    yc.show()
    sys.exit(app.exec_())
