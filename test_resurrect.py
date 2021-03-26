from unittest import TestCase
from unittest.mock import patch
import io

from game import resurrect
from game import make_player


class TestResurrect(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_one_counter_with_health(self, mock_output):
        player = make_player()
        player["special_action_counter"] = 1
        resurrect(player)
        actual = mock_output.getvalue()

        expected = "Your passive will allow you to survive a critical attack.\n\n"

        self.assertEqual(actual, expected)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_zero_counter(self, mock_output):
        player = make_player()
        player["special_action_counter"] = 0
        resurrect(player)
        actual = mock_output.getvalue()

        expected = "Your passive have already been used. You will not revive if your hp hits 0.\n\n"

        self.assertEqual(actual, expected)

    def test_one_counter_no_health(self):
        actual = {"health": 0, "level": 1, "special_action_counter": 1}
        resurrect(actual)

        expected = {"health": 10, "level": 1, "special_action_counter": 0}

        self.assertEqual(actual, expected)
