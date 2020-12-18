from CodePyQt5.logic.create_board import *


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
    game_start = Sudoku()
    game_start.game()