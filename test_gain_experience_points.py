from unittest import TestCase
from unittest.mock import patch
import io

from game import gain_experience_points
from game import magician_ship
from game import make_player


class TestGainExperiencePoints(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_max_level(self, mock_output):
        player = make_player()
        player["level"] = 3
        gain_experience_points(player)
        actual = mock_output.getvalue()

        expected = "You are already at the max level of \033[94m3\033[0m!\n" \
                   " You did not gain any scrap from the battle.\n"

        self.assertEqual(actual, expected)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_magician(self, mock_output):
        player = magician_ship(make_player())
        gain_experience_points(player)
        actual_experience = player["exp"]
        actual_counter = player["special_action_counter"]
        actual_output = mock_output.getvalue()

        expected_experience = 25
        expected_counter = 1
        expected_output = "You won the battle! You gained \033[94m25\033[0m scrap.\n" \
                          "You gained a charge on your special attack." \
                          " You now have a total of \033[94m1\033[0m charge(s).\n"

        self.assertEqual(actual_experience, expected_experience)
        self.assertEqual(actual_counter, expected_counter)
        self.assertEqual(actual_output, expected_output)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_gain_exp(self, mock_output):
        player = make_player()
        gain_experience_points(player)
        actual_experience = player["exp"]
        actual_output = mock_output.getvalue()

        expected_experience = 25
        expected_output = "You won the battle! You gained \033[94m25\033[0m scrap.\n"

        self.assertEqual(actual_experience, expected_experience)
        self.assertEqual(actual_output, expected_output)