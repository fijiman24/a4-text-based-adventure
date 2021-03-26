from unittest import TestCase
from game import magician_ship


class TestMagicianShip(TestCase):
    def test_correct_length(self):
        actual = magician_ship({})
        self.assertEqual(actual, 5)

    def test_correct_keys(self):
        actual = magician_ship({})
        self.assertIn("ship", actual)
        self.assertIn("player_class", actual)
        self.assertIn("player_class_special_action", actual)
        self.assertIn("special_action_counter", actual)
        self.assertIn("damage", actual)

    def test_correct_values(self):
        actual = magician_ship({})
        self.assertEqual(actual["ship"], "Magician")
        self.assertEqual(actual["player_class"], "Sapper")
        self.assertEqual(actual["player_class_special_action"], "Magic Blast")
        self.assertEqual(actual["special_action_counter"], 0)
        self.assertEqual(actual["damage"], 16)

