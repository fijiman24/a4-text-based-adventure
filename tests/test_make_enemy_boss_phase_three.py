from unittest import TestCase
from project.game import make_enemy_boss_phase_three


class Test(TestCase):
    def test_correct_length(self):
        boss = make_enemy_boss_phase_three()
        expected_length = 4
        self.assertEqual(expected_length, len(boss))

    def test_correct_keys(self):
        boss = make_enemy_boss_phase_three()
        self.assertIn("name", boss)
        self.assertIn("health", boss)
        self.assertIn("maximum_damage", boss)
        self.assertIn("special_ability_counter", boss)

    def test_correct_values(self):
        boss = make_enemy_boss_phase_three()
        self.assertEqual("Headless Intergalactic Space Worm", boss["name"])
        self.assertEqual(80, boss["health"])
        self.assertEqual(2, boss["maximum_damage"])
        self.assertEqual(5, boss["special_ability_counter"])
