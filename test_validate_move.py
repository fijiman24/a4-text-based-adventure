from unittest import TestCase
from unittest.mock import patch
import io

from game import validate_move
from game import confirm_move_to_boss_room


class TestValidateMove(TestCase):
    @patch('builtins.input', return_value=[1])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_boss_room(self, mock_input, mock_output):
        actual_return = validate_move(2, 23, 24)
        actual_output = mock_output.getvalue()

        expected_return = confirm_move_to_boss_room()
        expected_output = mock_output.getvalue()

        self.assertEqual(actual_return, expected_return)
        self.assertEqual(actual_output, expected_output)

    def test_valid_move(self):
        self.assertTrue(validate_move(1, 2, 2))

    def test_top_boundary(self):
        self.assertFalse(validate_move(1, 2, 0))

    def test_right_boundary(self):
        self.assertFalse(validate_move(2, 24, 1))

    def test_bottom_boundary(self):
        self.assertFalse(validate_move(3, 5, 24))

    def test_left_boundary(self):
        self.assertFalse(validate_move(4, 0, 5))

    def test_invalid_direction(self):
        self.assertFalse(validate_move(5, 2, 2))