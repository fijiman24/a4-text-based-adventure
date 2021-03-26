from unittest import TestCase
from game import priest_ship


class TestWarriorShip(TestCase):
    def test_correct_length(self):
        actual = len(priest_ship({}))
        self.assertEqual(actual, 6)

    def test_correct_keys(self):
        actual = priest_ship({})
        self.assertIn("health", actual)
        self.assertIn("maximum_health", actual)
        self.assertIn("ship", actual)
        self.assertIn("player_class", actual)
        self.assertIn("player_class_special_action", actual)
        self.assertIn("damage", actual)

    def test_correct_values(self):
        actual = priest_ship({})
        self.assertEqual(actual["health"], 16)
        self.assertEqual(actual["maximum_health"], 16)
        self.assertEqual(actual["ship"], "Priest")
        self.assertEqual(actual["player_class"], "Cherub")
        self.assertEqual(actual["player_class_special_action"], "Healing Spell")
        self.assertEqual(actual["damage"], 20)
