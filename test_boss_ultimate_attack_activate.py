from unittest import TestCase
import io
from unittest.mock import patch
from game import boss_ultimate_attack_activate
from game import make_enemy_boss_phase_three
from game import make_player


class Test(TestCase):
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_boss_ultimate_attack_activate_counter_nothing_above_zero(self, mock_output):
        player = make_player()
        boss = make_enemy_boss_phase_three()
        boss_ultimate_attack_activate(boss, player)
        actual = mock_output.getvalue()
        expected = ""
        self.assertEqual(expected, actual)

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_boss_ultimate_attack_activate_counter_zero_correct_print(self, mock_output):
        player = make_player()
        boss = make_enemy_boss_phase_three()
        boss["special_ability_counter"] = 0
        boss_ultimate_attack_activate(boss, player)
        actual = mock_output.getvalue()
        expected = "The [95mHeadless Intergalactic Space Worm[0m's body unleashes overwhelming astral power!" \
                   "\nYou, your ship, your crew, and everything else in Sector Six takes [95m99999[0m damage!\n\n"
        self.assertEqual(expected, actual)

    def test_boss_ultimate_attack_activate_counter_zero_correct_damage(self):
        player = make_player()
        player["health"] = 99999
        boss = make_enemy_boss_phase_three()
        boss["special_ability_counter"] = 0
        boss_ultimate_attack_activate(boss, player)
        actual = player["health"]
        expected = 0
        self.assertEqual(expected, actual)

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_boss_ultimate_attack_activate_counter_under_zero_correct_print(self, mock_output):
        player = make_player()
        boss = make_enemy_boss_phase_three()
        boss["special_ability_counter"] = -1
        boss_ultimate_attack_activate(boss, player)
        actual = mock_output.getvalue()
        expected = "The [95mHeadless Intergalactic Space Worm[0m's body unleashes EVEN MORE overwhelming astral" \
                   " power!\nYou, your ship, your crew, and everything else in Sector Six takes [95m99999[0m " \
                   "damage! Again!\n\n"
        self.assertEqual(expected, actual)

    def test_boss_ultimate_attack_activate_counter_under_zero_correct_damage(self):
        player = make_player()
        player["health"] = 99999
        boss = make_enemy_boss_phase_three()
        boss["special_ability_counter"] = -500
        boss_ultimate_attack_activate(boss, player)
        actual = player["health"]
        expected = 0
        self.assertEqual(expected, actual)