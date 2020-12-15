import sys
from Sudoku import create_board

from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

from PyQt5 import QtCore
from PyQt5 import QtWidgets
from datetime import timedelta

class Sudoku_GUI(QtWidgets.QMainWindow):
    def __init__(self):

        super().__init__()
        self.resize(512, 512)
        self.setWindowTitle("Sudoku ")

        # Initialization of the time widget
        self.my_qtimer = QtCore.QTimer(self)
        self.game_time = 0
        self.widget_counter_int = 0

        central_widget = QtWidgets.QWidget()
        self.setCentralWidget(central_widget)
        vbox = QtWidgets.QVBoxLayout()
        central_widget.setLayout(vbox)

        self.pages_qsw = QtWidgets.QStackedWidget()
        vbox.addWidget(self.pages_qsw)
        self.time_passed = QtWidgets.QLabel()
        vbox.addWidget(self.time_passed)

        self.timer_start()
        self.update_gui()

    # Time related functions
    def timer_start(self):
        # Starts the timer
        self.my_qtimer.timeout.connect(self.timer_timeout)
        self.my_qtimer.start(1000)
        self.update_gui()

    def timer_timeout(self):
        # Counts the time
        self.game_time += 1
        self.update_gui()

    def update_gui(self):
        # Update the time
        self.time_passed.setText(str(timedelta(seconds=self.game_time)))

    # Grid creation
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
    window = Sudoku_GUI()
    window.show()
    sys.exit(app.exec_())