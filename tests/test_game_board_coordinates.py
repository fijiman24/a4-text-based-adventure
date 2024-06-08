from unittest import TestCase
from project.game import game_board_coordinates


class Test(TestCase):
    def test_game_board_coordinates_one_coordinate(self):
        actual = game_board_coordinates(0, 0, 0, 0)
        expected = {(-1, -1): '\x1b[95mW\x1b[0m', (0, 0): '\x1b[93m@\x1b[0m'}
        self.assertEqual(expected, actual)

    def test_game_board_coordinates_correct_length(self):
        actual = len(game_board_coordinates(0, 0, 5, 5))
        expected = 5 * 5
        self.assertEqual(expected, actual)

    def test_game_board_coordinates_unoccupied_coordinates(self):
        actual = game_board_coordinates(0, 0, 2, 2)
        expected = {(0, 0): '\x1b[93m@\x1b[0m', (0, 1): '*', (1, 0): '*', (1, 1): '\x1b[95mW\x1b[0m'}
        self.assertEqual(expected, actual)

    def test_game_board_correct_values(self):
        board = game_board_coordinates(0, 0, 2, 2)
        self.assertIn("*", board.values())
        self.assertIn('\x1b[93m@\x1b[0m', board.values())
        self.assertIn('\x1b[95mW\x1b[0m', board.values())
