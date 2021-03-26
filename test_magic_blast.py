from unittest import TestCase
from unittest.mock import patch
import io

from game import magic_blast
from game import make_player


class TestMagicBlast(TestCase):
    def test_zero_counter(self):
        player = make_player()
        player["special_action_counter"] = 0
        actual = magic_blast(player)

        expected = 0

        self.assertEqual(actual, expected)

    def test_not_zero_counter(self):
        player = make_player()
        player["special_action_counter"] = 3
        actual = magic_blast(player)

        expected = 15

        self.assertEqual(actual, expected)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_statement(self, mock_output):
        player = make_player()
        player["special_action_counter"] = 3
        magic_blast(player)
        actual = mock_output.getvalue()

        expected = "You relinquished your charges to deal \033[94m15\033[0m to the enemy!\n"

        self.assertEqual(actual, expected)
