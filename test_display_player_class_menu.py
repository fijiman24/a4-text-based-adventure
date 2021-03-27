from unittest import TestCase
from unittest.mock import patch
import io

from game import display_player_class_menu


class TestDisplayPlayerClassMenu(TestCase):
    @patch('builtins.input', side_effect=['1'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_statement(self, mock_output, mock_input):
        display_player_class_menu()
        actual = mock_output.getvalue()

        expected = "Select a \033[94mspaceship\033[0m: \n" \
                   " [(1, 'Squire'), (2, 'Sapper'), (3, 'Ghost'), (4, 'Cherub')]\n"

        self.assertEqual(actual, expected)
