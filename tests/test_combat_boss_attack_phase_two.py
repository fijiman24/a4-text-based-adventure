from unittest import TestCase
import io
from unittest.mock import patch
from project.game import make_player
from project.game import combat_boss_attack_phase_two


class Test(TestCase):
    @patch("random.randint", side_effect=[1, 2])
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_combat_boss_attack_phase_two_correct_print(self, mock_output, random_number_generator):
        player = make_player()
        combat_boss_attack_phase_two(player)
        actual = mock_output.getvalue()
        expected = "The [95mIntergalactic Space Worm[0m's left head did [95m1[0m damage to you!\nThe " \
                   "[95mIntergalactic Space Worm[0m's right head did [95m2[0m damage to you!\n\n"
        self.assertEqual(expected, actual)

    @patch("random.randint", side_effect=[3, 2])
    def test_combat_boss_attack_phase_two_updates_health(self, random_number_generator):
        player = make_player()
        player["health"] = 10
        actual = combat_boss_attack_phase_two(player)
        expected = 5
        self.assertEqual(expected, actual)
