import sys
from Sudoku.create_board import *

from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

from PyQt5 import QtCore
from PyQt5 import QtWidgets
from datetime import timedelta

size = 40
shiftV = 70
shiftH = 80
color_board = Qt.black
color_inside_board = Qt.gray

class Sudoku_GUI(QtWidgets.QMainWindow):
    def __init__(self):

        super().__init__()
        self.resize(512, 512)
        self.setWindowTitle("Sudoku ")

        self.list_buttons = []

        self.time_stoped = -1
        # Shows the time
        self.my_qtimer = QtCore.QTimer(self)
        self.game_time = 0
        self.widget_counter_int = 0

        central_widget = QtWidgets.QWidget()
        self.setCentralWidget(central_widget)
        time_box = QtWidgets.QVBoxLayout()
        central_widget.setLayout(time_box)

        self.align_bottom = QtWidgets.QStackedWidget()
        time_box.addWidget(self.align_bottom)
        self.time_passed = QtWidgets.QLabel()
        time_box.addWidget(self.time_passed)
        # Align the time in bottom center of the screen
        self.time_passed.setAlignment(Qt.AlignCenter)

        self.update_gui()

        self.menu_buttons()

    # Time related functions
    def timer_start(self):
        # Starts the timer
        self.my_qtimer.timeout.connect(self.timer_timeout)
        self.my_qtimer.start()
        self.update_gui()

    def timer_timeout(self):
        # Counts the time
        self.game_time += 1
        self.update_gui()

    def update_gui(self):
        # Updates the time
        self.time_passed.setText(str(timedelta(milliseconds=self.game_time/4)))

    def timer_stop(self):
        # Stops the time
        self.my_qtimer.stop()

    # Buttons
    def menu_buttons(self):
        # New game button
        self.start_btn = QtWidgets.QPushButton(self)
        self.start_btn.setText("New Game")
        self.start_btn.clicked.connect(self.timer_start)

        # Save button
        self.save_btn = QtWidgets.QPushButton(self)
        self.save_btn.setText("Save")
        self.save_btn.move(100, 0)
        self.save_btn.clicked.connect(self.timer_stop)

        for i in range(9):
            temp = []
            for j in range(9):
                temp.append(QtWidgets.QPushButton(self))
                temp[j].setFixedWidth(41)
                temp[j].setFixedHeight(41)
                temp[j].move(shiftH+(i*size), shiftV+(j*size))
                #temp[j].setText(str(player_board[i][j]))
            self.list_buttons.extend(temp)

    def paintEvent(self, event):
        painter = QPainter(self)
        for i in range(9):
            for j in range(9):
                # Draws the squares of the Sudoku
                painter.setPen(color_inside_board)
                painter.drawRect(shiftH + (j * size), shiftV + (i * size), size, size)

        for i in [0,3,6,9]:
            # Trace vertical lines
            painter.setPen(color_board)
            painter.drawLine(10 + shiftV + (i * size), shiftV, 10 + shiftV + (i * size), size * 9 + shiftV)
            # Trace horizontal lines
            painter.drawLine(shiftH, shiftV + (i * size), 11 * size, shiftV + (i * size))

    def game(self):
        """
        Function that calls all other functions to launch the game.
        Will loop till the game is finished.
        """
        self.difficulty_selection()
        self.player_board = copy.deepcopy(self.create_board())
        self.create_player_board()
        self.start = time()
        wrong = False
        # Infinite loop till the game's over.
        while True:
            system("{}".format("cls" if platform.system() == "Windows" else "clear"))
            if wrong:
                # Outputs a message saying that the player got a wrong answer.
                print("Too bad, it's wrong!")
                wrong = False
            self.print_board()
            try:
                # Ask the player numbers for the line, column and number.
                x = int(input("Line:"))
                y = int(input("Column:"))
                number = int(input("Number:"))

                # Checks the board with the player's number.
                if not self.compare_board(x, y, number):
                    # Adds penalty points when a wrong number is given.
                    self.penalty += 10
                    wrong = True
                else:
                    # Adds the correct number in the player's board.
                    self.player_board[x - 1][y - 1] = number
                    # Check if the player completed the board.
                    if self.win():
                        self.playtime = self.getTime()
                        system("{}".format("cls" if platform.system() == "Windows" else "clear"))
                        self.print_board()
                        break

            # Ask the player to enter a correct value if it was not the case.
            except ValueError:
                print(self.msg_error_number)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Sudoku_GUI()
    window.show()
    sys.exit(app.exec_())