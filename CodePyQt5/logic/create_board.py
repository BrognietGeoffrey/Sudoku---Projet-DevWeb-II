import copy
import platform
from datetime import timedelta
from os import system
from random import sample, randint
from time import time


class Sudoku:
    def __init__(self):
        self.start = 0
        self.board, self.player_board = [], []
        self.difficulty = 0
        self.playtime = 0
        self.penalty = 0
        self.square_grid = 3
        self.size = self.square_grid ** 2
        self.square_size_counter = range(self.square_grid)
        self.msg_difficulty = "Please select a difficulty: 1 for easy, 2 for medium et 3 for hard: "
        self.msg_error_number = "Please insert a number between 1 and {}".format(self.size)
        self.msg_error_difficulty = "Please insert a number between 1 and 3"
        self.msg_win = "Congratulations {}! You finished the game in {} {}"

    #  Getters:
    def get_player_board(self):
        """
		Get the player's board

		PRE: -
		POST:
			returns self.player_board: matrix composed of int numbers from 0 to 9
		"""
        return self.player_board

    def get_size(self):
        """
		Get the size of the sudoku

		PRE: -
		POST:
			returns self.size: int number representing the size of the sudoku
		"""
        return self.size

    def getTime(self):
        """
		Get the time spent solving the sudoku

		PRE: -
		POST:
			returns str: a string representing a time
		"""
        return timedelta(seconds=time() - self.start)

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

    def print_board(self):
        """
		Function that prints the game board in console line in the most readable way.

		PRE: -
		POST: -
		"""

        for i in range(1, self.size + 1):
            # Prints the first line where the column numbers are on top to ease the board reading
            if i == 1:
                print("    ", end="")
            print(i, end="   " if i % 3 != 0 else "\n" if i == self.size else "    ")

        # Prints the board itself
        for i in range(self.size):
            # Loop for every line of the sudoku
            if i % 3 == 0 or i == 0:
                # Prints a line to separate each square
                print(" =" * (self.size * 2 + 3))
            # Prints the line number on the left part of the game board
            print("{} ||".format(i + 1), end="")

            for j, x in enumerate(self.player_board[i]):
                # Prints the contents of a line, that are the columns of that line
                if j % 3 == 0 and j != 0:
                    # Prints a separation for each square
                    print("|", end="")
                # Prints a separation for each column
                print(" {} |".format(x if x != 0 else " "), end="")
            print("|")
            # Prints the bottom line of the board
            if i == self.size - 1:
                print(" =" * (self.size * 2 + 3))

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

    def compare_board(self, x, y, number):
        """
		Function that matches the player's board with the board in a certain x and y axis on both boards.

		PRE:
		 	x: integer that represents the x axis.
		 	y: integer that represents the y axis.
		 	number: integer of the user's input.

		POST:
			returns a boolean: returns True when the number in x and y axis matches on both board tables.
		"""
        return number == self.board[x - 1][y - 1]

    def difficulty_selection(self):
        """
		Function that checks if the user wrote a correct number of difficulty, and ask again if not the case.

		PRE: -
		POST: -
		"""
        while self.difficulty < 1 or self.difficulty > 4:
            try:
                self.difficulty = int(input(self.msg_difficulty))
                if self.difficulty < 1 or self.difficulty > 4:
                    print(self.msg_error_difficulty)
            except ValueError:
                print(self.msg_error_difficulty)

    def get_score(self, player_name):
        """
		Function that returns and prints the score of the player.

		PRE:
			player_name: name of the player taken as a string.
		POST: -
		"""
        penalty_time = str(timedelta(seconds=self.penalty) + self.playtime).split(".")[0]
        msg = self.msg_win.format(player_name, str(self.playtime).split(".")[0],
                                         "without any mistake!" if self.penalty == 0 else
                                         "with as final time: {} and {} error{}.".format(
                                             penalty_time, self.penalty // 10, "" if self.penalty // 10 < 2 else "s"))
        print(msg)
        return msg

    def game(self):
        """
        Function that calls all other functions to launch the game.
        Will loop till the game is finished.

        PRE: -
        POST: -
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
