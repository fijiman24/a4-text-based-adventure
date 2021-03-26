from unittest import TestCase
from unittest.mock import patch
import io

from game import magic_blast
from game import make_player


class TestMagicBlast(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_zero_counter(self, mock_output):
        player = make_player()
        player["special_action_counter"] = 0
        actual_damage = magic_blast(player)
        actual_output = mock_output.getvalue()

        expected_output = "You relinquished your charges to deal \033[94m0\033[0m to the enemy!\n"
        expected_damage = 0

        self.assertEqual(actual_output, expected_output)
        self.assertEqual(actual_damage, expected_damage)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_not_zero_counter(self, mock_output):
        player = make_player()
        player["special_action_counter"] = 3
        actual_damage = magic_blast(player)
        actual_output = mock_output.getvalue()

        expected_output = "You relinquished your charges to deal \033[94m15\033[0m to the enemy!\n"
        expected_damage = 15

        self.assertEqual(actual_output, expected_output)
        self.assertEqual(actual_damage, expected_damage)