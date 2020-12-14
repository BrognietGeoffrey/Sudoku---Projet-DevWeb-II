import sys


from PyQt5.QtGui     import *
from PyQt5.QtCore    import *
from PyQt5.QtWidgets import *


class Window(QWidget):

    def __init__(self):

        super().__init__()
        self.resize(512, 512)
        self.setWindowTitle("Sudoku ")

    def paintEvent(self, event):
        painter = QPainter(self)
        size = 40

        for i in range(10):
            if i < 9:
                for j in range(9):
                    painter.setPen(Qt.black)
                    painter.drawRect(80+(j*size), 10+(i*size), size, size)
            if i % 3 == 0:
                painter.setPen(Qt.cyan)
                painter.drawLine(80, 10+(i*size), 11 * size, 10+(i*size))

        print(self.children())


if __name__ == "__main__":

    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())