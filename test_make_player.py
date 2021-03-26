from unittest import TestCase
from game import make_player


class Test(TestCase):
    def test_correct_length(self):
        player_character = make_player()
        expected_length = 13
        self.assertEqual(expected_length, len(player_character))

    def test_correct_keys(self):
        player_character = make_player()
        self.assertIn("health", player_character)
        self.assertIn("maximum_health", player_character)
        self.assertIn("x-coordinate", player_character)
        self.assertIn("y-coordinate", player_character)
        self.assertIn("name", player_character)
        self.assertIn("exp", player_character)
        self.assertIn("ship", player_character)
        self.assertIn("player_class", player_character)
        self.assertIn("player_class_special_action", player_character)
        self.assertIn("special_action_counter", player_character)
        self.assertIn("level", player_character)
        self.assertIn("damage", player_character)
        self.assertIn("boss_phase_counter", player_character)

    def test_correct_values(self):
        player_character = make_player()
        self.assertEqual(20, player_character["health"])
        self.assertEqual(20, player_character["maximum_health"])
        self.assertEqual(0, player_character["x-coordinate"])
        self.assertEqual(0, player_character["y-coordinate"])
        self.assertIsNone(player_character["name"])
        self.assertEqual(0, player_character["exp"])
        self.assertIsNone(player_character["ship"])
        self.assertIsNone(player_character["player_class"])
        self.assertIsNone(player_character["player_class_special_action"])
        self.assertEqual(0, player_character["special_action_counter"])
        self.assertEqual(1, player_character["level"])
        self.assertEqual(20, player_character["damage"])
        self.assertEqual(3, player_character["boss_phase_counter"])
