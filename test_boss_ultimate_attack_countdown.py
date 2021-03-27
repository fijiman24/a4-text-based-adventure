from unittest import TestCase
from unittest.mock import patch
import io
from game import boss_ultimate_attack_countdown
from game import make_enemy_boss_phase_three


class Test(TestCase):
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_boss_ultimate_attack_countdown_correct_print(self, mock_output):
        boss = make_enemy_boss_phase_three()
        boss_ultimate_attack_countdown(boss)
        actual = mock_output.getvalue()
        expected = "The [95mHeadless Intergalactic Space Worm[0m's body writhes.\n"
        self.assertEqual(expected, actual)

    def test_boss_ultimate_attack_countdown_decrement_counter(self):
        boss = make_enemy_boss_phase_three()
        boss["special_ability_counter"] = 5
        boss_ultimate_attack_countdown(boss)
        actual = boss["special_ability_counter"]
        expected = 4
        self.assertEqual(expected, actual)

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_boss_ultimate_attack_countdown_no_print_below_zero(self, mock_output):
        boss = make_enemy_boss_phase_three()
        boss["special_ability_counter"] = 0
        boss_ultimate_attack_countdown(boss)
        actual = mock_output.getvalue()
        expected = ""
        self.assertEqual(expected, actual)
