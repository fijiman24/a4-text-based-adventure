from unittest import TestCase
from unittest.mock import patch
import io

from game import combat_choice


class TestCombatChoice(TestCase):
    @patch('builtins.input', side_effect=['1'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_statement(self, mock_output, mock_input):
        combat_choice()
        actual = mock_output.getvalue()

        expected = "You are engaged in a space battle. What will you do next?\n" \
                   " [(1, 'Normal Attack'), (2, 'Special Ability'), (3, 'Flee')]\n"

        self.assertEqual(actual, expected)
