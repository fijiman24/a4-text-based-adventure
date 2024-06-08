from unittest import TestCase
from project.game import make_enemy_difficulty_three


class Test(TestCase):
    def test_correct_length(self):
        player_character = make_enemy_difficulty_three()
        expected_length = 5
        self.assertEqual(expected_length, len(player_character))

    def test_correct_keys(self):
        enemy = make_enemy_difficulty_three()
        self.assertIn("name", enemy)
        self.assertIn("health", enemy)
        self.assertIn("experience_points", enemy)
        self.assertIn("maximum_damage", enemy)
        self.assertIn("special_ability_counter", enemy)

    def test_correct_values(self):
        enemy = make_enemy_difficulty_three()
        self.assertEqual("Disruptor", enemy["name"])
        self.assertEqual(60, enemy["health"])
        self.assertEqual(100, enemy["experience_points"])
        self.assertEqual(5, enemy["maximum_damage"])
        self.assertEqual(4, enemy["special_ability_counter"])
