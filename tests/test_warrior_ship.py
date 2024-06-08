from unittest import TestCase
from project.game import warrior_ship


class TestWarriorShip(TestCase):
    def test_correct_length(self):
        actual = len(warrior_ship({}))
        self.assertEqual(actual, 7)

    def test_correct_keys(self):
        actual = warrior_ship({})
        self.assertIn("health", actual)
        self.assertIn("maximum_health", actual)
        self.assertIn("ship", actual)
        self.assertIn("player_class", actual)
        self.assertIn("player_class_special_action", actual)
        self.assertIn("special_action_counter", actual)
        self.assertIn("damage", actual)

    def test_correct_values(self):
        actual = warrior_ship({})
        self.assertEqual(actual["health"], 18)
        self.assertEqual(actual["maximum_health"], 18)
        self.assertEqual(actual["ship"], "Warrior")
        self.assertEqual(actual["player_class"], "Squire")
        self.assertEqual(actual["player_class_special_action"], "Resurrect")
        self.assertEqual(actual["special_action_counter"], 1)
        self.assertEqual(actual["damage"], 25)
