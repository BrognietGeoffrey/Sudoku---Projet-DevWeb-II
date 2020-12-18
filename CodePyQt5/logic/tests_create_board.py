import unittest, mock
from random import seed

from CodePyQt5.logic.create_board import *


class SudokuTest(unittest.TestCase):
    def __init__(self, methodName):
        super().__init__(methodName)
        seed(5)
        self.size = 9
        self.difficulty = 1
        self.msg_win = "Congratulations {}! You finished the game in {} {}"
        self.player_board = [[0, 2, 3, 4, 5, 6, 7, 8, 9],
                             [0, 3, 4, 5, 6, 7, 8, 9, 1],
                             [0, 4, 5, 6, 7, 8, 9, 1, 2],
                             [0, 5, 6, 7, 8, 9, 1, 2, 3],
                             [0, 6, 7, 8, 9, 1, 2, 3, 4],
                             [0, 7, 8, 9, 1, 2, 3, 4, 5],
                             [0, 8, 9, 1, 2, 3, 4, 5, 6],
                             [0, 9, 1, 2, 3, 4, 5, 6, 7],
                             [0, 1, 2, 3, 4, 5, 6, 7, 8]]

        self.board = [[1, 2, 3, 4, 5, 6, 7, 8, 9],
                      [2, 3, 4, 5, 6, 7, 8, 9, 1],
                      [3, 4, 5, 6, 7, 8, 9, 1, 2],
                      [4, 5, 6, 7, 8, 9, 1, 2, 3],
                      [5, 6, 7, 8, 9, 1, 2, 3, 4],
                      [6, 7, 8, 9, 1, 2, 3, 4, 5],
                      [7, 8, 9, 1, 2, 3, 4, 5, 6],
                      [8, 9, 1, 2, 3, 4, 5, 6, 7],
                      [9, 1, 2, 3, 4, 5, 6, 7, 8]]

    def test_print(self):
        print(Sudoku.print_board(self))

    def test_compare_board(self):
        # tests the comparison of the board with the input
        self.assertEqual(Sudoku.compare_board(self, 1, 1, 1), True)
        self.assertEqual(Sudoku.compare_board(self, 1, 1, 7), False)
        self.assertEqual(Sudoku.compare_board(self, 1, 7, 7), True)
        self.assertEqual(Sudoku.compare_board(self, 1, 7, 9), False)
        self.assertEqual(Sudoku.compare_board(self, 4, 9, 3), True)

        print("Test compare board: ok")

    def test_get_score(self):
        name = "test"
        no_mistakes = "Congratulations test! You finished the game in 0:00:30 without any mistake!"
        one_mistake = "Congratulations test! You finished the game in 0:00:30 with as final time: 0:00:40 and 1 error."
        two_mistake = "Congratulations test! You finished the game in 0:00:30 with as final time: 0:00:50 and 2 errors."
        self.playtime = timedelta(seconds=30)
        self.penalty = 0
        self.assertMultiLineEqual((Sudoku.get_score(self, name)), no_mistakes)
        self.penalty = 10
        self.assertMultiLineEqual((Sudoku.get_score(self, name)), one_mistake)
        self.penalty = 20
        self.assertMultiLineEqual((Sudoku.get_score(self, name)), two_mistake)


if __name__ == "__main__":
    unittest.main()
