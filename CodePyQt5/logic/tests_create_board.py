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

    def test_get_player_board(self):
        self.assertEqual(Sudoku.get_player_board(self), self.player_board)
        self.assertNotEqual(Sudoku.get_player_board(self), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
        self.assertNotEqual(Sudoku.get_player_board(self), self.board)
        self.assertNotEqual(Sudoku.get_player_board(self), 1)
        self.assertNotEqual(Sudoku.get_player_board(self), -1)
        self.assertNotEqual(Sudoku.get_player_board(self), "[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]")

    def test_get_size(self):
        self.assertEqual(Sudoku.get_size(self), 9)
        self.assertNotEqual(Sudoku.get_size(self), 2)
        self.size = 5
        self.assertEqual(Sudoku.get_size(self), 5)
        self.assertNotEqual(Sudoku.get_size(self), 15)
        self.assertRaises(TypeError, Sudoku.get_size(self), "p")
        self.assertRaises(TypeError, Sudoku.get_size(self), "&")

    def test_pattern(self):
        # Calcul: (3 * (arg1 % 3) + arg1 // 3 + arg2) % 9
        self.square_grid = 3
        self.size = 9

        self.assertEqual(Sudoku.pattern(self, 2, 5), 2)
        self.assertEqual(Sudoku.pattern(self, 1, 7), 1)
        self.assertIsInstance(Sudoku.pattern(self, 9, 4), int)
        self.assertFalse(type(Sudoku.pattern(self, 2, 8)) is str)

        self.assertRaises(TypeError, Sudoku.pattern, self, "&", "p")
        self.assertRaises(TypeError, Sudoku.pattern, self, 4, "p")
        self.assertRaises(TypeError, Sudoku.pattern, self, "&", 6)

    def test_shuffle(self):
        self.assertNotEqual(Sudoku.shuffle(self, [1, 2, 3]), [1, 2, 3])
        self.assertNotEqual(Sudoku.shuffle(self, [1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

        self.assertEqual(len(Sudoku.shuffle(self, [1, 2, 3])), 3)
        self.assertNotEqual(len(Sudoku.shuffle(self, [1, 2, 3])), 5)
        self.assertEqual(len(Sudoku.shuffle(self, [1, 2, 3, 4, 5, 6, 7, 8, 9])), 9)
        self.assertNotEqual(len(Sudoku.shuffle(self, [1, 2, 3, 4, 5, 6, 7, 8, 9])), 2)

        self.assertNotEqual(Sudoku.shuffle(self, ["1", "2", "3"]), ["1", "2", "3"])
        self.assertNotEqual(Sudoku.shuffle(self, ["1", "2", "3", "4", "5"]), ["1", "2", "3", "4", "5"])

        self.assertEqual(len(Sudoku.shuffle(self, ["1", "2", "3"])), 3)
        self.assertNotEqual(len(Sudoku.shuffle(self, ["1", "2", "3"])), 5)
        self.assertEqual(len(Sudoku.shuffle(self, ["1", "2", "3", "4", "5", "6", "7", "8", "9"])), 9)
        self.assertNotEqual(len(Sudoku.shuffle(self, ["1", "2", "3", "4", "5", "6", "7", "8", "9"])), 2)

    def test_win(self):
        self.size = 3
        self.player_board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.assertTrue(Sudoku.win(self))

        self.player_board = [[1, 2, 0], [4, 5, 6], [7, 8, 9]]
        self.assertFalse(Sudoku.win(self))

        self.player_board = [[1, 0, 3], [4, 5, 0], [7, 8, 9]]
        self.assertFalse(Sudoku.win(self))

        self.player_board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.assertFalse(Sudoku.win(self))

    def test_print(self):
        print(Sudoku.print_board(self))

    def test_compare_board(self):
        # tests the comparison of the board with the input
        self.assertEqual(Sudoku.compare_board(self, 1, 1, 1), True)
        self.assertEqual(Sudoku.compare_board(self, 1, 1, 7), False)
        self.assertEqual(Sudoku.compare_board(self, 1, 7, 7), True)
        self.assertEqual(Sudoku.compare_board(self, 1, 7, 9), False)
        self.assertEqual(Sudoku.compare_board(self, 4, 9, 3), True)

    @mock.patch('builtins.input', return_value="a")
    def str_testing(self, mock_input):
        return "a"

    @mock.patch('builtins.input', return_value=1)
    def test_difficulty_selection(self, mock_input):
        self.msg_difficulty = "Please select a difficulty: 1 for easy, 2 for medium et 3 for hard: "
        self.difficulty = 5
        Sudoku.difficulty_selection(self)
        self.assertEqual(self.difficulty, 1)

        self.difficulty = 0
        Sudoku.difficulty_selection(self)
        self.assertEqual(self.difficulty, 1)

        self.difficulty = -1
        Sudoku.difficulty_selection(self)
        self.assertEqual(self.difficulty, 1)

        self.difficulty = 0
        Sudoku.difficulty_selection(self)
        self.difficulty = self.str_testing()
        self.assertNotEqual(self.difficulty, 1)

    @mock.patch('builtins.input', return_value=2)
    def test_difficulty_selection2(self, mock_input):
        self.msg_difficulty = "Please select a difficulty: 1 for easy, 2 for medium et 3 for hard: "
        self.difficulty = 5
        Sudoku.difficulty_selection(self)
        self.assertEqual(self.difficulty, 2)

        self.difficulty = 0
        Sudoku.difficulty_selection(self)
        self.assertEqual(self.difficulty, 2)

        self.difficulty = -1
        Sudoku.difficulty_selection(self)
        self.assertEqual(self.difficulty, 2)

        self.difficulty = 0
        Sudoku.difficulty_selection(self)
        self.difficulty = self.str_testing()
        self.assertNotEqual(self.difficulty, 2)

    @mock.patch('builtins.input', return_value=3)
    def test_difficulty_selection3(self, mock_input):
        self.msg_difficulty = "Please select a difficulty: 1 for easy, 2 for medium et 3 for hard: "
        self.difficulty = 5
        Sudoku.difficulty_selection(self)
        self.assertEqual(self.difficulty, 3)

        self.difficulty = 0
        Sudoku.difficulty_selection(self)
        self.assertEqual(self.difficulty, 3)

        self.difficulty = -1
        Sudoku.difficulty_selection(self)
        self.assertEqual(self.difficulty, 3)

        self.difficulty = 0
        Sudoku.difficulty_selection(self)
        self.difficulty = self.str_testing()
        self.assertNotEqual(self.difficulty, 3)

    def test_get_score(self):
        name = "test"
        self.playtime = timedelta(seconds=30)
        self.penalty = 0
        self.assertMultiLineEqual((Sudoku.get_score(self, name)), "0:00:30")
        self.penalty = 10
        self.assertMultiLineEqual((Sudoku.get_score(self, name)), "0:00:40")
        self.penalty = 20
        self.assertMultiLineEqual((Sudoku.get_score(self, name)), "0:00:50")


if __name__ == "__main__":
    unittest.main()
