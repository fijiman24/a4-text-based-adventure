from unittest import TestCase
from project.game import make_player
from project.game import make_appropriate_boss_phase
from project.game import make_enemy_boss_phase_one
from project.game import make_enemy_boss_phase_two
from project.game import make_enemy_boss_phase_three


class Test(TestCase):
    def test_make_appropriate_boss_phase_one(self):
        player = make_player()
        actual = make_appropriate_boss_phase(player)
        expected = make_enemy_boss_phase_one()
        self.assertEqual(expected, actual)

    def test_make_appropriate_boss_phase_two(self):
        player = make_player()
        player["boss_phase_counter"] = 2
        actual = make_appropriate_boss_phase(player)
        expected = make_enemy_boss_phase_two()
        self.assertEqual(expected, actual)

    def test_make_appropriate_boss_phase_three(self):
        player = make_player()
        player["boss_phase_counter"] = 1
        actual = make_appropriate_boss_phase(player)
        expected = make_enemy_boss_phase_three()
        self.assertEqual(expected, actual)
