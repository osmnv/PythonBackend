
import sys
import builtins
import unittest
from unittest.mock import patch
from io import StringIO

from tictactoe import TicTacToe

def step_gen(steps):
    for step in steps:
        yield step

class TestTicTacToe(unittest.TestCase):
    def setUp(self):
        self.game = TicTacToe()

    def test_check_pos(self):
        self.assertEqual(self.game._check_pos("12"), "OK")
        self.assertEqual(self.game._check_pos("9"), "INVALID")
        self.assertEqual(self.game._check_pos("32"), "OK")
        self.assertEqual(self.game._check_pos("qwe"), "INVALID")
        self.assertEqual(self.game._check_pos("-3"), "INVALID")
        self.assertEqual(self.game._check_pos("14"), "INVALID")
        self.assertEqual(self.game._check_pos(""), "INVALID")

    def test_check_win(self):
        self.game._board = [['X', 'O', '-'],
                            ['-', 'X', 'O'],
                            ['-', '-', '-']]
        self.assertEqual(self.game._check_win(), None)

        self.game._board = [['-', '-', 'O'],
                            ['X', 'O', 'X'],
                            ['O', 'X', '-']]
        self.assertEqual(self.game._check_win(), "Player O won!")

        self.game._board = [['X', '-', 'O'],
                            ['-', 'X', 'X'],
                            ['O', 'O', 'X']]
        self.assertEqual(self.game._check_win(), "Player X won!")

    def test_start_game(self):
        steps_1 = step_gen(["11", "12", "22", "23", "33"])
        with patch('builtins.input', lambda :next(steps_1)),\
             patch('sys.stdout', StringIO()) as p:
            self.game.start_game()
            self.assertEqual(p.getvalue().strip()[-len("Player X won!"):], "Player X won!")

        self.game = TicTacToe()

        steps_2 = step_gen(["12", "31", "33", "22", "21", "13"])
        with patch('builtins.input', lambda :next(steps_2)),\
             patch('sys.stdout', StringIO()) as p:
            self.game.start_game()
            self.assertEqual(p.getvalue().strip()[-len("Player O won!"):], "Player O won!")

        self.game = TicTacToe()

        steps_3 = step_gen(["11", "21", "31", "22", "12", "13", "32", "33", "23"])
        with patch('builtins.input', lambda :next(steps_3)),\
             patch('sys.stdout', StringIO()) as p:
            self.game.start_game()
            self.assertEqual(p.getvalue().strip()[-len("Draw!"):], "Draw!")

if __name__ == "__main__":
    unittest.main()
