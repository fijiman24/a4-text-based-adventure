from unittest import TestCase
from game import make_enemy_difficulty_two


class Test(TestCase):
    def test_correct_length(self):
        player_character = make_enemy_difficulty_two()
        expected_length = 4
        self.assertEqual(expected_length, len(player_character))

    def test_correct_keys(self):
        enemy = make_enemy_difficulty_two()
        self.assertIn("name", enemy)
        self.assertIn("health", enemy)
        self.assertIn("experience_points", enemy)
        self.assertIn("maximum_damage", enemy)

    def test_correct_values(self):
        enemy = make_enemy_difficulty_two()
        self.assertEqual("Gunner", enemy["name"])
        self.assertEqual(20, enemy["health"])
        self.assertEqual(50, enemy["experience_points"])
        self.assertEqual(10, enemy["maximum_damage"])
