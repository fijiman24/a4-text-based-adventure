from unittest import TestCase
from unittest.mock import patch
import io
from game import input_player_name


class Test(TestCase):
    @patch('builtins.input', side_effect=['Lazarus'])
    def test_input_valid_name(self, mock_input):
        actual = input_player_name()
        expected = 'Lazarus'
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['laZaRuS'])
    def test_name_becomes_title_case(self, mock_input):
        actual = input_player_name()
        expected = 'Lazarus'
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=[''])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_no_name_given(self, mock_output, mock_input):
        input_player_name()
        actual = mock_output.getvalue()
        expected_output = "Every space captain needs a name! \n\n"
        self.assertEqual(expected_output, actual)

    @patch('builtins.input', side_effect=['chris'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_instructor_name_given(self, mock_output, mock_input):
        input_player_name()
        actual = mock_output.getvalue()
        expected_output = "You can be more adventurous than that! \n\n"
        self.assertEqual(expected_output, actual)
