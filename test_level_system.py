from unittest import TestCase
from unittest.mock import patch
import io

from game import level_system
from game import magician_ship
from game import make_player


class TestLevelSystem(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_level_up(self, mock_output):
        player = make_player()
        player["exp"] = 300
        player["ship"] = "Warrior"
        level_system(player)
        actual_output = mock_output.getvalue()
        actual_experience = player["exp"]
        actual_level = player["level"]
        actual_damage = player["damage"]
        actual_health = player["health"]
        actual_maximum_health = player["maximum_health"]

        expected_output = "You gained a level! You are now level \033[94m2\033[0m and your ship has been upgraded to" \
                          " a \033[94mKnight\033[0m.\n"
        expected_experience = 0
        expected_level = 2
        expected_damage = 22
        expected_health = 25
        expected_maximum_health = 25

        self.assertEqual(actual_output, expected_output)
        self.assertEqual(actual_experience, expected_experience)
        self.assertEqual(actual_level, expected_level)
        self.assertEqual(actual_damage, expected_damage)
        self.assertEqual(actual_health, expected_health)
        self.assertEqual(actual_maximum_health, expected_maximum_health)

    def test_no_level_up(self):
        actual = level_system(make_player())

        expected = make_player()

        self.assertEqual(actual, expected)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_magician_level_up(self, mock_output):
        player = magician_ship(make_player())
        player["exp"] = 300
        level_system(player)
        actual_output = mock_output.getvalue()
        actual_counters = player["special_action_counter"]

        expected_output = "You gained a level! You are now level \033[94m2\033[0m and your ship has been upgraded to" \
                          " a \033[94mDrainer\033[0m.\n"\
                          "You also gained another charge on your special attack!" \
                          " You now have a total of \033[94m1\033[0m.\n"
        expected_counters = 1

        self.assertEqual(actual_counters, expected_counters)
        self.assertEqual(actual_output, expected_output)
