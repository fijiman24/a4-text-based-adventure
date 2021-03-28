from unittest import TestCase
from game import assign_player_class
from game import make_player


class Test(TestCase):
    def test_assign_player_class_warrior(self):
        player = make_player()
        assign_player_class("Squire", player)
        actual_class = player['player_class']
        expected_class = "Squire"
        actual_class_ability = player['player_class_special_action']
        expected_class_ability = "Resurrect"
        self.assertEqual(expected_class, actual_class)
        self.assertEqual(expected_class_ability, actual_class_ability)

    def test_assign_player_class_priest(self):
        player = make_player()
        assign_player_class("Cherub", player)
        actual_class = player['player_class']
        expected_class = "Cherub"
        actual_class_ability = player['player_class_special_action']
        expected_class_ability = "Healing Spell"
        self.assertEqual(expected_class, actual_class)
        self.assertEqual(expected_class_ability, actual_class_ability)

    def test_assign_player_class_magician(self):
        player = make_player()
        assign_player_class("Sapper", player)
        actual_class = player['player_class']
        expected_class = "Sapper"
        actual_class_ability = player['player_class_special_action']
        expected_class_ability = "Magic Blast"
        self.assertEqual(expected_class, actual_class)
        self.assertEqual(expected_class_ability, actual_class_ability)

    def test_assign_player_class_thief(self):
        player = make_player()
        assign_player_class("Ghost", player)
        actual_class = player['player_class']
        expected_class = "Ghost"
        actual_class_ability = player['player_class_special_action']
        expected_class_ability = "Multi Strike"
        self.assertEqual(expected_class, actual_class)
        self.assertEqual(expected_class_ability, actual_class_ability)
