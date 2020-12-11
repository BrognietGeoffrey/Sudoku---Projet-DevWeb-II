from random import sample, randint
from os import system
import copy, platform
from time import time
from datetime import timedelta


class Sudoku:
    def __init__(self):
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
        self.msg_win = "Congratulations {}, you finished the game in {} {}"

    def create_board(self):
        """ Creating the board """
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
        Algorithme qui renvoie un nombre valide pour le board selon un paterne
        prédéfini pour le sudoku
        """
        return (self.square_grid * (line % self.square_grid) + line // self.square_grid + column) % self.size

    def shuffle(self, table):
        """ Mélange les lines et les columns """
        return sample(table, len(table))

    def print_board(self):
        """ Imprime le board en console de manière la plus lisible possible """

        for i in range(1, self.size + 1):
            if i == 1:
                print("    ", end="")
            print(i, end="   " if i % 3 != 0 else "\n" if i == self.size else "    ")

        for i in range(self.size):
            if i % 3 == 0 or i == 0:
                print(" =" * (self.size * 2 + 3))
            print("{} ||".format(i + 1), end="")
            for j, x in enumerate(self.player_board[i]):
                if j % 3 == 0 and j != 0:
                    print("|", end="")
                print(" {} |".format(x if x != 0 else " "), end="")
            print("|")
            if i == self.size - 1:
                print(" =" * (self.size * 2 + 3))

    def create_player_board(self):
        for i in range(self.size - 1):
            for j in range(self.size - 1):
                if randint(0, 10) < self.difficulty:
                    self.player_board[i][j] = 0

    def win(self):
        for i in range(self.size):
            for j in range(self.size):
                if self.player_board[i][j] == 0:
                    return False
        return True

    def verif_number(self, x):
        return int("") if x < 1 or x > self.size else x

    def compare_board(self, x, y, number):
        return number == self.board[x - 1][y - 1]

    def game(self):
        while self.difficulty < 1 or self.difficulty > 4:
            try:
                self.difficulty = int(input(self.msg_difficulty))
            except:
                print(self.msg_error_difficulty)
        self.player_board = copy.deepcopy(self.create_board())
        self.create_player_board()
        start = time()
        wrong = False
        while True:
            system("{}".format("cls" if platform.system() == "Windows" else "clear"))
            if wrong:
                print("Too bad, it's wrong!")
                wrong = False
            self.print_board()
            try:
                x = self.verif_number(int(input("Line:")))
                y = self.verif_number(int(input("Column:")))
                number = self.verif_number(int(input("Number:")))
                if not self.compare_board(x, y, number):
                    self.penalty += 10
                    wrong = True
                else:
                    self.player_board[x - 1][y - 1] = number
            except:
                print(self.msg_error_number)
            if self.win():
                self.playtime = timedelta(seconds=time() - start)
                system("{}".format("cls" if platform.system() == "Windows" else "clear"))
                self.print_board()
                break

    def get_score(self, player_name):
        penalty_time = str(timedelta(seconds=self.penalty) + self.playtime).split(".")[0]
        print(self.msg_win.format(player_name, str(self.playtime).split(".")[0],
                                  "without any mistake!" if self.penalty == 0 else
                                  "with as final time: {} and {} error{}.".format(
                                      penalty_time, self.penalty // 10, "" if self.penalty // 10 < 2 else "s")))


def ask_name():
    name = (input("Type your name or 'exit' to quit the game: "))
    if not name.isalpha() or name == "":
        print("You typed a number or nothing, please retry.")
        return ask_name()
    return name


if __name__ == "__main__":
    while True:
        nom = ask_name()
        if nom == "exit":
            print("Bye bye!")
            break
        a = Sudoku()
        a.game()
        a.get_score(nom)
