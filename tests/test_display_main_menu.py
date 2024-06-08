from unittest import TestCase
from unittest.mock import patch
import io
from project.game import display_main_menu


class Test(TestCase):
    @patch('builtins.input', return_value=1)
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_display_main_menu_correct_print(self, mock_output, mock_input):
        display_main_menu()
        actual = mock_output.getvalue()
        expected = "[(1, 'Move'), (2, 'Status Report'), (3, 'Quit Game')]\n"
        self.assertEqual(expected, actual)

    @patch('builtins.input', return_value=1)
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_display_main_menu_correct_print(self, mock_output, mock_input):
        actual = display_main_menu()
        expected = 1
        self.assertEqual(expected, actual)