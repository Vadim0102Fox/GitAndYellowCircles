import sys
from PyQt6 import uic
from ui import Ui_Form
from PyQt6.QtGui import QPainter, QPen, QColor, QPixmap
from PyQt6.QtWidgets import QWidget, QApplication
from random import randint


class MainWindow(QWidget, Ui_Form):  # main app
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pixmap = QPixmap(400, 400)
        self.pixmap.fill(QColor("white"))
        self.label.setPixmap(self.pixmap)
        self.pushButton.clicked.connect(self.place_circle)

    def place_circle(self):
        painter = QPainter(self.pixmap)
        pen = QPen()
        pen.setWidth(3)
        pen.setColor(QColor(200, 100, 0))
        painter.setPen(pen)
        r, g, b = randint(1, 255), randint(1, 255), randint(1, 255)
        painter.setBrush(QColor(r, g, b))
        w = randint(10, 100)
        x = randint(0, self.pixmap.width() - w)
        y = randint(0, self.pixmap.height() - w)
        painter.drawEllipse(x, y, w, w)
        painter.end()
        self.label.setPixmap(self.pixmap)


def exception_hook(cls, exception, traceback):
    sys.__exception_hook__(cls, exception, traceback)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.excepthook = exception_hook
    window.show()
    sys.exit(app.exec())
