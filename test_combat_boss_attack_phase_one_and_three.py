from unittest import TestCase
import io
from unittest.mock import patch
from game import combat_boss_attack_phase_one_and_three
from game import make_player


class Test(TestCase):
    @patch("random.randint", return_value=2)
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_combat_boss_attack_phase_one_correct_print(self, mock_output, random_number_generator):
        player = make_player()
        combat_boss_attack_phase_one_and_three(player)
        actual = mock_output.getvalue()
        expected = "The [95mIntergalactic Space Worm[0m did [95m2[0m damage to you!\n\n"
        self.assertEqual(expected, actual)

    @patch("random.randint", return_value=2)
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_combat_boss_attack_phase_three_correct_print(self, mock_output, random_number_generator):
        player = make_player()
        player["boss_phase_counter"] = 1
        combat_boss_attack_phase_one_and_three(player)
        actual = mock_output.getvalue()
        expected = "The [95mHeadless Intergalactic Space Worm[0m did [95m2[0m damage to you!\n\n"
        self.assertEqual(expected, actual)

    @patch("random.randint", return_value=5)
    def test_combat_boss_attack_phase_one_and_three_updates_player_health(self, random_number_generator):
        player = make_player()
        player["health"] = 10
        actual = combat_boss_attack_phase_one_and_three(player)
        expected = 5
        self.assertEqual(expected, actual)


