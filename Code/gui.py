import sys
from Sudoku import create_board

from PyQt5.QtGui import *
from PyQt5.QtCore import *
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
        color = Qt.black

        for i in range(9):
            for j in range(9):
                # Draws the squares of the Sudoku
                painter.setPen(Qt.gray)
                painter.drawRect(80 + (j * size), shift + (i * size), size, size)
                        
        for i in [0,3,6,9]:
            # Trace vertical lines
            painter.setPen(color)
            painter.drawLine(10 + shift + (i * size), shift, 10 + shift + (i * size), size * 9 + shift)
            # Trace horizontal lines
            painter.drawLine(80, shift + (i * size), 11 * size, shift + (i * size))


if __name__ == "__main__":

    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())