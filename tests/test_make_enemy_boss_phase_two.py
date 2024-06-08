from unittest import TestCase
from project.game import make_enemy_boss_phase_two


class Test(TestCase):
    def test_correct_length(self):
        boss = make_enemy_boss_phase_two()
        expected_length = 3
        self.assertEqual(expected_length, len(boss))

    def test_correct_keys(self):
        boss = make_enemy_boss_phase_two()
        self.assertIn("name", boss)
        self.assertIn("health", boss)
        self.assertIn("maximum_damage", boss)

    def test_correct_values(self):
        boss = make_enemy_boss_phase_two()
        self.assertEqual("Two-Headed Intergalactic Space Worm", boss["name"])
        self.assertEqual(50, boss["health"])
        self.assertEqual(5, boss["maximum_damage"])
