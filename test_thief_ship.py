from unittest import TestCase
from game import thief_ship


class TestWarriorShip(TestCase):
    def test_correct_length(self):
        actual = thief_ship({})
        self.assertEqual(actual, 4)

    def test_correct_keys(self):
        actual = thief_ship({})
        self.assertIn("ship", actual)
        self.assertIn("player_class", actual)
        self.assertIn("player_class_special_action", actual)
        self.assertIn("damage", actual)

    def test_correct_values(self):
        actual = thief_ship({})
        self.assertEqual(actual["ship"], "Thief")
        self.assertEqual(actual["player_class"], "Ghost")
        self.assertEqual(actual["player_class_special_action"], "Multi Strike")
        self.assertEqual(actual["damage"], 20)
