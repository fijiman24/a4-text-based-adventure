from unittest import TestCase
from unittest.mock import patch
import io

from project.game import confirm_player_class
from project.game import make_player


class TestConfirmPlayerClass(TestCase):
    @patch('builtins.input', side_effect=['1'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_confirm_yes(self, mock_output, mock_input):
        actual = confirm_player_class("Squire", make_player())
        actual_output = mock_output.getvalue()

        expected_output = "A Lazarus Engine™ allows for this ship to repair itself after its hull integrity has " \
                          "been completely breached for the first time.\nDo you pilot a [94mSquire[0m?\n" \
                          "[(1, 'Yes'), (2, 'No')]\n"
        self.assertIsNone(actual)
        self.assertEqual(actual_output, expected_output)

    @patch('builtins.input', side_effect=['2', '1', '1'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_confirm_no_then_yes(self, mock_output, mock_input):
        confirm_player_class("Squire", make_player())
        actual = mock_output.getvalue()

        expected = "A Lazarus Engine™ allows for this ship to repair itself after" \
                   " its hull integrity has been completely breached for the first time.\n" \
                   "Do you pilot a \033[94mSquire\033[0m?\n" \
                   "[(1, 'Yes'), (2, 'No')]\n"\
                   "Select a \033[94mspaceship\033[0m: \n" \
                   " [(1, 'Squire'), (2, 'Sapper'), (3, 'Ghost'), (4, 'Cherub')]\n" \
                   "A Lazarus Engine™ allows for this ship to repair itself after" \
                   " its hull integrity has been completely breached for the first time.\n" \
                   "Do you pilot a \033[94mSquire\033[0m?\n" \
                   "[(1, 'Yes'), (2, 'No')]\n"

        self.assertEqual(actual, expected)

    @patch('builtins.input', side_effect=['5', '1'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_confirm_invalid_then_yes(self, mock_output, mock_input):
        confirm_player_class("Squire", make_player())
        actual = mock_output.getvalue()

        expected = "A Lazarus Engine™ allows for this ship to repair itself after its hull integrity has " \
                   "been completely breached for the first time.\nDo you pilot a [94mSquire[0m?\n" \
                   "[(1, 'Yes'), (2, 'No')]\nThat is not a valid choice! \n\n"

        self.assertEqual(actual, expected)
