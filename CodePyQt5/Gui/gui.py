import sys
from CodePyQt5.logic.create_board import *

from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

from PyQt5 import QtCore
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from datetime import timedelta
import copy
import platform
from datetime import timedelta
from os import system
from random import sample, randint
from time import time

size = 40
shiftV = 70
shiftH = 80
color_board = Qt.black
color_inside_board = Qt.gray


class SudokuGUI(QtWidgets.QMainWindow):
    def __init__(self):

        super().__init__()
        # Game logic variables
        self.started = False
        self.board, self.player_board = [], []
        self.difficulty = 1
        self.playtime = 0
        self.penalty = 0
        self.square_grid = 3
        self.size = self.square_grid ** 2
        self.square_size_counter = range(self.square_grid)
        self.list_buttons = []
        self.time_stoped = -1

        # Window
        self.setFixedSize(512, 512)
        self.setWindowTitle("Sudoku ")

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

        # New game button
        self.start_btn = QtWidgets.QPushButton(self)
        self.start_btn.setEnabled(False)
        self.start_btn.setText("New Game")
        self.start_btn.clicked.connect(self.timer_start)

        # Save button
        self.save_btn = QtWidgets.QPushButton(self)
        self.save_btn.setEnabled(False)
        self.save_btn.setText("Save")
        self.save_btn.move(100, 0)
        self.save_btn.clicked.connect(self.timer_stop)

        # Sudoku
        self.difficulty_selection()
        self.sudoku_buttons_init()
        self.update_gui()
        #self.menu_buttons()

    # Sudoku logic
    def difficulty_selection(self):
        """
        Changes the difficulty when the player has clicked on the validation button

        PRE: -
        POST: -
        """
        self.difficulty_box = QComboBox(self)
        self.difficulty_box.setGeometry(200, 0, 50, 30)
        difficulty_list = ["Easy", "Medium", "Hard"]

        # adding list of items to combo box
        self.difficulty_box.addItems(difficulty_list)
        self.selected_level = QPushButton("Level validation", self)
        self.selected_level.setGeometry(270, 0, 120, 30)
        self.selected_level.pressed.connect(self.hide_button)

    def hide_button(self):
        """
        Hide the difficulty related buttons, activates the start and save button and shows the player's board

        PRE: -
        POST: -
        """
        self.start_btn.setEnabled(True)
        self.save_btn.setEnabled(True)
        if self.difficulty_box.currentText() == "Hard":
            self.difficulty += 2
        elif self.difficulty_box.currentText() == "Medium":
            self.difficulty += 1
        self.difficulty_box.hide()
        self.selected_level.hide()
        self.sudoku_buttons()

    def create_board(self):
        """
        Function that creates the sudoku board.

        PRE: -
        POST:
            returns self.board: a completed sudoku board game in a matrix format.
        """
        lines, columns = [], []
        table = self.shuffle(range(1, self.size + 1))
        # Creating a line and a column with random values
        for i in self.shuffle(self.square_size_counter):
            for j in self.shuffle(self.square_size_counter):
                lines.append(j * self.square_grid + i)

        for i in self.shuffle(self.square_size_counter):
            for j in self.shuffle(self.square_size_counter):
                columns.append(j * self.square_grid + i)

        # Creating the sudoku while checking on the possibilities with pattern(x,y)
        for i in lines:
            temp = []
            for j in columns:
                temp.append(table[self.pattern(i, j)])
            self.board.append(temp)
        return self.board

    def pattern(self, line, column):
        """
        Function that returns a valid number for the sudoku board from a predefined pattern.

        PRE:
            line: a integer from a number of a line.
            column: a integer from a number of a column.

        POST:
            returns an int: a integer calculated with a number of a line, a column and the size of the sudoku.
        """
        return (self.square_grid * (line % self.square_grid) + line // self.square_grid + column) % self.size

    def shuffle(self, table):
        """
        Function that shuffles a list.

        PRE:
            table: a list of integer.

        POST:
            returns a list: a randomized list from table, randomized with the sample() method.
        """
        return sample(table, len(table))

    def create_player_board(self):
        """
        Function that creates a board for the player to play, by randomly removing numbers in the board

        PRE: -
        POST: -
        """
        for i in range(self.size - 1):
            for j in range(self.size - 1):
                if randint(0, 10) < self.difficulty:
                    # Remove more or less tiles randomly depending on the difficulty
                    self.player_board[i][j] = 0
        if self.win():
            # Recreates the board in case the player got lucky and doesn't need to complete it
            self.create_player_board()

    def win(self):
        """
        Function that checks if the player's board is completed or not.

        PRE: -
        POST:
            returns a boolean: returns True if the board is completed, False otherwise.
        """
        for i in range(self.size):
            for j in range(self.size):
                if self.player_board[i][j] == 0:
                    return False
        return True

    # Time related functions
    def timer_start(self):
        """"
        Starts the timer

        PRE: -
        POST: -
        """
        self.my_qtimer.timeout.connect(self.timer_timeout)
        self.my_qtimer.start()
        self.update_gui()
        self.started = True

    def timer_timeout(self):
        """
        Counts the time

        PRE: -
        POST: -
        """
        self.game_time += 1
        self.update_gui()

    def update_gui(self):
        """
        Updates the time

        PRE: -
        POST: -
        """
        self.time_passed.setText(str(timedelta(milliseconds=self.game_time/4)))

    def timer_stop(self):
        """
        Stops the time

        PRE: -
        POST: -
        """
        self.my_qtimer.stop()

    def sudoku_buttons_init(self):
        """
        Creates the button that composes the board

        PRE: -
        POST: -
        """
        for i in range(9):
            for j in range(9):
                button = QtWidgets.QPushButton(self)
                button.setFixedWidth(41)
                button.setFixedHeight(41)
                button.move(shiftH + (i * size), shiftV + (j * size))
                button.setText("")

    def sudoku_buttons(self):
        """
        Fills the grid with the player's game board

        PRE: -
        POST: -
        """
        self.player_board = copy.deepcopy(self.create_board())
        self.create_player_board()
        table = self.player_board
        for i in range(len(table)):
            for j in range(len(table)):
                button = QtWidgets.QPushButton(self)
                button.setFixedWidth(41)
                button.setFixedHeight(41)
                button.move(shiftH + (i * size), shiftV + (j * size))
                button.setText(str(table[i][j] if table[i][j] != 0 else ""))

    def paintEvent(self, event):
        """
        Draws the grid 9x9 for the player before the game starts

        PRE:
            event: when the game is initialized
        POST: -
        """
        painter = QPainter(self)
        # Draws the squares of the Sudoku
        for i in range(9):
            for j in range(9):
                painter.setPen(color_inside_board)
                painter.drawRect(shiftH + (j * size), shiftV + (i * size), size, size)

        # Draws the separations of the sudoku for eye comfort
        for i in [0,3,6,9]:
            # Trace vertical lines
            painter.setPen(color_board)
            painter.drawLine(10 + shiftV + (i * size), shiftV, 10 + shiftV + (i * size), size * 9 + shiftV)
            # Trace horizontal lines
            painter.drawLine(shiftH, shiftV + (i * size), 11 * size, shiftV + (i * size))

    # TODO ------------------------------------------------------
    """def game(self):
        \"""
        Function that calls all other functions to launch the game.
        Will loop till the game is finished.
        \"""

        self.difficulty_selection()
        self.player_board = copy.deepcopy(self.create_board())
        self.create_player_board()

        # TO DO
        while self.started:
            #self.print_board()
            self.sudoku_buttons()

            # Checks the board with the player's number.
            if not self.compare_board(x, y, number):
                # Adds penalty points when a wrong number is given.
                self.penalty += 10
            else:
                # Adds the correct number in the player's board.
                self.player_board[x - 1][y - 1] = number
                # Check if the player completed the board.
                if self.win():
                    self.playtime = self.getTime()
                    self.print_board()"""


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SudokuGUI()
    window.show()
    sys.exit(app.exec_())