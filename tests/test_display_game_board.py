from unittest import TestCase
import io
from unittest.mock import patch
from project.game import display_game_board
from project.game import game_board_coordinates


class Test(TestCase):
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_display_game_board_one_coordinate(self, mock_output):
        board = game_board_coordinates(0, 0, 1, 1)
        display_game_board(0, 0, 1, board)
        actual = mock_output.getvalue()
        expected = " [94m[95mW[0m[0m\nYou are at 0, 0.\n"
        self.assertEqual(expected, actual)

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_display_game_board_multiple_coordinates(self, mock_output):
        board = game_board_coordinates(0, 0, 2, 2)
        display_game_board(0, 0, 2, board)
        actual = mock_output.getvalue()
        expected = " [94m[93m@[0m[0m [94m*[0m \n [94m*[0m [94m[95mW[0m[0m\nYou are at 0, 0.\n"
        self.assertEqual(expected, actual)

