from unittest import TestCase
from unittest.mock import patch
import io

from game import backstab


class Testbackstab(TestCase):
    @patch('random.randint', return_value=5)
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_escape(self, mock_output, random_number_generator):
        actual_health = backstab(10)
        actual_output = mock_output.getvalue()

        expected_health = 10
        expected_output = "You successfully escape back into darkness of space.\n"

        self.assertEqual(actual_health, expected_health)
        self.assertEqual(actual_output, expected_output)

    @patch('random.randint', side_effect = [1, 4])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_backstab(self, mock_output, random_number_generator):
        actual_health = backstab(10)
        actual_output = mock_output.getvalue()

        expected_health = 6
        expected_output = "The enemy shot you for \033[91m4\033[0m damage as you fled!\n"

        self.assertEqual(actual_health, expected_health)
        self.assertEqual(actual_output, expected_output)

    @patch('random.randint', side_effect= [1, 4])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_backstab_death(self, mock_output, random_number_generator):
        backstab(3)
        actual = mock_output.getvalue()

        expected = "Your ship's integrity has been breached! Sector Six has claimed another crew of would-be" \
                   " thieves.\n\n" \
                   "\033[91mYOU ARE DEAD\033[0m\n"

        self.assertEqual(actual, expected)