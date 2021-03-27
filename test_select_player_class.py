from unittest import TestCase
from unittest.mock import patch
import io

from game import make_player
from game import select_player_class


class TestSelectPlayerClass(TestCase):

    @patch('builtins.input', side_effect=['1', '1'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_squire_class(self, mock_output, mock_input):
        actual = select_player_class(make_player())
        actual_output = mock_output.getvalue()
        expected = "Squire"
        expected_output = "Select a \033[94mspaceship\033[0m: \n" \
                          " [(1, 'Squire'), (2, 'Sapper'), (3, 'Ghost'), (4, 'Cherub')]\n" \
                          "A Lazarus Engine™ allows for this ship to repair itself after its hull integrity has been" \
                          " completely breached for the first time.\n" \
                          "Do you pilot a \033[94mSquire\033[0m?\n" \
                          "[(1, 'Yes'), (2, 'No')]\n"
        self.assertEqual(actual["player_class"], expected)
        self.assertEqual(actual_output, expected_output)

    @patch('builtins.input', side_effect=['2', '1'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_sapper_class(self, mock_output, mock_input):
        actual = select_player_class(make_player())
        actual_output = mock_output.getvalue()
        expected = "Sapper"
        expected_output = "Select a \033[94mspaceship\033[0m: \n" \
                          " [(1, 'Squire'), (2, 'Sapper'), (3, 'Ghost'), (4, 'Cherub')]\n" \
                          "Destroy enemy ships to steal their energy and charge" \
                          " up your Quasar Cannon™ for a devastating attack.\n" \
                          "Do you pilot a \033[94mSapper\033[0m?\n" \
                          "[(1, 'Yes'), (2, 'No')]\n"
        self.assertEqual(actual["player_class"], expected)
        self.assertEqual(actual_output, expected_output)

    @patch('builtins.input', side_effect=['3', '1'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_ghost_class(self, mock_output, mock_input):
        actual = select_player_class(make_player())
        actual_output = mock_output.getvalue()
        expected = "Ghost"
        expected_output = "Select a \033[94mspaceship\033[0m: \n" \
                          " [(1, 'Squire'), (2, 'Sapper'), (3, 'Ghost'), (4, 'Cherub')]\n" \
                          "A nimble ship covered in aerodynamic SlipStream™ technology allows the pilot" \
                          " to make the first move in combat, and attack multiple times in one turn.\n" \
                          "Do you pilot a \033[94mGhost\033[0m?\n" \
                          "[(1, 'Yes'), (2, 'No')]\n"
        self.assertEqual(actual["player_class"], expected)
        self.assertEqual(actual_output, expected_output)

    @patch('builtins.input', side_effect=['4', '1'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_cherub_class(self, mock_output, mock_input):
        actual = select_player_class(make_player())
        actual_output = mock_output.getvalue()
        expected = "Cherub"
        expected_output = "Select a \033[94mspaceship\033[0m: \n" \
                          " [(1, 'Squire'), (2, 'Sapper'), (3, 'Ghost'), (4, 'Cherub')]\n" \
                          "QuickFix™ Protocols allows this ship to repair itself during combat.\n" \
                          "Do you pilot a \033[94mCherub\033[0m?\n" \
                          "[(1, 'Yes'), (2, 'No')]\n"
        self.assertEqual(actual["player_class"], expected)
        self.assertEqual(actual_output, expected_output)

    @patch('builtins.input', side_effect=['spaghetti', '1', '1'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_invalid_input(self, mock_output, mock_input):
        select_player_class(make_player())
        actual_output = mock_output.getvalue()

        expected = "Select a \033[94mspaceship\033[0m: \n" \
                   " [(1, 'Squire'), (2, 'Sapper'), (3, 'Ghost'), (4, 'Cherub')]\n" \
                   "That is not a valid choice! \n\n" \
                   "Select a \033[94mspaceship\033[0m: \n" \
                   " [(1, 'Squire'), (2, 'Sapper'), (3, 'Ghost'), (4, 'Cherub')]\n" \
                   "A Lazarus Engine™ allows for this ship to repair itself after its hull integrity" \
                   " has been completely breached for the first time.\n" \
                   "Do you pilot a \033[94mSquire\033[0m?\n" \
                   "[(1, 'Yes'), (2, 'No')]\n"

        self.assertEqual(actual_output, expected)
