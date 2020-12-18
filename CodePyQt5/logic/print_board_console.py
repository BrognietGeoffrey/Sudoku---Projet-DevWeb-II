from CodePyQt5.logic.create_board import *


class ConsoleBoard:
    def __init__(self):
        super(ConsoleBoard, self).__init__()

    def print_board(self, player_board, size):
        """
        Function that prints the game board in console line in the most readable way.
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

