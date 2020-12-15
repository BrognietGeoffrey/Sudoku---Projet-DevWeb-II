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
        shift = 70

        for i in range(10):
            if i < 9:
                for j in range(10):
                    if j < 9:
                        # Draws the squares of the Sudoku
                        painter.setPen(Qt.black)
                        painter.drawRect(80 + (j * size), shift + (i * size), size, size)
                    if j % 3 == 0:
                        # Trace vertical lines
                        painter.setPen(Qt.cyan)
                        painter.drawLine(10 + shift + (j * size), shift, 10 + shift + (j * size), size * 9 + shift)
            if i % 3 == 0:
                # Trace horizontal lines
                painter.setPen(Qt.cyan)
                painter.drawLine(80, shift + (i * size), 11 * size, shift + (i * size))


        print(self.children())


if __name__ == "__main__":

    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())