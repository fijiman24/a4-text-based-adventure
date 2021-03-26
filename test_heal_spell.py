from unittest import TestCase
from game import heal_spell
from unittest.mock import patch
import io


class TestHealSpell(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_full_health(self, mock_output):
        player = {"health": 20, "maximum_health": 20, "level": 1}
        heal_spell(player)
        actual_output = mock_output.getvalue()
        actual_healed = player["health"]

        expected_healed = 20
        expected_output = "You repaired your hull for \033[94m0\033[0m health.\n"

        self.assertEqual(actual_healed, expected_healed)
        self.assertEqual(actual_output, expected_output)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_full_amount_healed(self, mock_output):
        player = {"health": 5, "maximum_health": 20, "level": 1}
        heal_spell(player)
        actual_output = mock_output.getvalue()
        actual_healed = player["health"]

        expected_healed = 11
        expected_output = "You repaired your hull for \033[94m6\033[0m health.\n"

        self.assertEqual(actual_healed, expected_healed)
        self.assertEqual(actual_output, expected_output)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_partial_amount_healed(self, mock_output):
        player = {"health": 18, "maximum_health": 20, "level": 1}
        heal_spell(player)
        actual_output = mock_output.getvalue()
        actual_healed = player["health"]

        expected_healed = 20
        expected_output = "You repaired your hull for \033[94m2\033[0m health.\n"

        self.assertEqual(actual_healed, expected_healed)
        self.assertEqual(actual_output, expected_output)
