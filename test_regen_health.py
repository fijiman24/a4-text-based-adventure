from unittest import TestCase
from unittest.mock import patch
import io

from game import regen_health


class TestRegenHealth(TestCase):
    def test_full_health(self):
        actual = regen_health(20, 20)
        expected = 20

        self.assertEqual(actual, expected)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_full_amount_healed(self, mock_output):
        actual_health = regen_health(10, 20)
        actual_output = mock_output.getvalue()

        expected_health = 14
        expected_output = "You repaired your ship by \033[94m4\033[0m points!\n"

        self.assertEqual(actual_health, expected_health)
        self.assertEqual(actual_output, expected_output)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_partial_amount_healed(self, mock_output):
        actual_health = regen_health(18, 20)
        actual_output = mock_output.getvalue()

        expected_health = 20
        expected_output = "You repaired your ship \033[94mcompletely\033[0m!\n"

        self.assertEqual(actual_health, expected_health)
        self.assertEqual(actual_output, expected_output)
