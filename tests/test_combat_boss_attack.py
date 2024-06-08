from unittest import TestCase
from unittest.mock import patch
from project.game import combat_boss_attack
from project.game import combat_boss_attack_phase_one_and_three
from project.game import combat_boss_attack_phase_two
from project.game import make_player


class Test(TestCase):
    @patch("random.randint", side_effect=[2, 2])
    def test_combat_boss_phase_one_attack(self, random_number_generator):
        player = make_player()
        player["health"] = 20
        actual = combat_boss_attack(player)
        player["health"] = 20
        expected = combat_boss_attack_phase_one_and_three(player)
        self.assertEqual(expected, actual)

    @patch("random.randint", side_effect=[2, 2, 2, 2])
    def test_combat_boss_phase_two_attack(self, random_number_generator):
        player = make_player()
        player["boss_phase_counter"] = 2
        player["health"] = 20
        actual = combat_boss_attack(player)
        player["health"] = 20
        expected = combat_boss_attack_phase_two(player)
        self.assertEqual(expected, actual)

    @patch("random.randint", side_effect=[2, 2])
    def test_combat_boss_phase_three_attack(self, random_number_generator):
        player = make_player()
        player["boss_phase_counter"] = 1
        player["health"] = 20
        actual = combat_boss_attack(player)
        player["health"] = 20
        expected = combat_boss_attack_phase_one_and_three(player)
        self.assertEqual(expected, actual)
