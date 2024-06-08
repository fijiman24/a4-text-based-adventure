from unittest import TestCase
import io
from unittest.mock import patch
from project.game import cardinal_direction


class Test(TestCase):
    @patch('builtins.input', return_value="one")
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_cardinal_direction_invalid_input(self, mock_output, mock_input):
        self.assertFalse(cardinal_direction())

    @patch('builtins.input', return_value="1")
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_cardinal_direction_valid_input(self, mock_output, mock_input):
        expected = 1
        self.assertEqual(expected, cardinal_direction())

    @patch('builtins.input', return_value="1")
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_cardinal_direction_correct_print(self, mock_output, mock_input):
        cardinal_direction()
        actual = mock_output.getvalue()
        expected = "Please enter a number corresponding to the direction you wish to move in.\n[(1, 'North'), " \
                   "(2, 'East'), (3, 'South'), (4, 'West')]\n"
        self.assertEqual(expected, actual)
