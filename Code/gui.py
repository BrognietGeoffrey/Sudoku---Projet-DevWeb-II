import sys


from PyQt5.QtGui     import *
from PyQt5.QtCore    import *
from PyQt5.QtWidgets import *


class Window(QWidget):

    def __init__(self):

        super().__init__()
        self.resize(512, 512)
        self.setWindowTitle("Sudoku ")

        # Create a QHBoxLayout instance
    def paintEvent(self, event):
        painter = QPainter(self)
        size = 40

        for i in range(9):
            for j in range(9):
                painter.setPen(Qt.black)
                painter.drawRect(80+(j*size), 10+(i*size), size, size)

        # Set the layout on the application's window
        painter.setPen(Qt.cyan)
        painter.drawLine(80, 10, 11 * size, 10)
        painter.drawLine(80, 130, 11 * size, 130)
        painter.drawLine(80, 250, 11 * size, 250)
        painter.drawLine(80, 370, 11 * size, 370)
        print(self.children())


if __name__ == "__main__":

    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())