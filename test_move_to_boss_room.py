from unittest import TestCase
from unittest.mock import patch
import io

from game import confirm_move_to_boss_room


class TestMoveToBossRoom(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=['1'])
    def test_confirm(self, mock_input, mock_output):
        actual_return = confirm_move_to_boss_room()
        actual_output = mock_output.getvalue()

        expected_output = "You're about to enter the gravitational pull of the wormhole. " \
                          "This is a point of no return. You've almost escaped Sector Six with your treasure," \
                          " but you have a feeling you\nmay face some final resistance...\n" \
                          "Are you sure you wish to proceed?\n" \
                          "[(1, 'Yes'), (2, 'No')]\n"

        self.assertTrue(actual_return)
        self.assertEqual(actual_output, expected_output)

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=['2'])
    def test_do_not_confirm(self, mock_input, mock_output):
        actual_return = confirm_move_to_boss_room()
        actual_output = mock_output.getvalue()

        expected_output = "You're about to enter the gravitational pull of the wormhole. " \
                          "This is a point of no return. You've almost escaped Sector Six with your treasure," \
                          " but you have a feeling you\nmay face some final resistance...\n" \
                          "Are you sure you wish to proceed?\n" \
                          "[(1, 'Yes'), (2, 'No')]\n"

        self.assertFalse(actual_return)
        self.assertEqual(actual_output, expected_output)

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=['3'])
    def test_invalid_input(self, mock_input, mock_output):
        actual_return = confirm_move_to_boss_room()
        actual_output = mock_output.getvalue()

        expected_output = "You're about to enter the gravitational pull of the wormhole. " \
                          "This is a point of no return. You've almost escaped Sector Six with your treasure," \
                          " but you have a feeling you\nmay face some final resistance...\n" \
                          "Are you sure you wish to proceed?\n" \
                          "[(1, 'Yes'), (2, 'No')]\n"

        self.assertIsNone(actual_return)
        self.assertEqual(actual_output, expected_output)
