from unittest import TestCase
from game import make_player
from game import warrior_ship
from game import magician_ship
from game import thief_ship
from game import priest_ship
from game import class_upgrade


class TestClassUpgrade(TestCase):
    def test_warrior_upgrade(self):
        player = warrior_ship(make_player())
        player["level"] = 2
        actual_level_two = class_upgrade(player)
        expected_level_two = 'Knight'

        self.assertEqual(actual_level_two["player_class"], expected_level_two)

        player["level"] = 3
        actual_level_three = class_upgrade(player)
        expected_level_three = 'Phoenix'

        self.assertEqual(actual_level_three["player_class"], expected_level_three)

    def test_magician_upgrade(self):
        player = magician_ship(make_player())
        player["level"] = 2
        actual_level_two = class_upgrade(player)
        expected_level_two = 'Drainer'

        self.assertEqual(actual_level_two["player_class"], expected_level_two)

        player["level"] = 3
        actual_level_three = class_upgrade(player)
        expected_level_three = 'Charybdis'

        self.assertEqual(actual_level_three["player_class"], expected_level_three)

    def test_thief_upgrade(self):
        player = thief_ship(make_player())
        player["level"] = 2
        actual_level_two = class_upgrade(player)
        expected_level_two = 'Banshee'

        self.assertEqual(actual_level_two["player_class"], expected_level_two)

        player["level"] = 3
        actual_level_three = class_upgrade(player)
        expected_level_three = 'Revenant'

        self.assertEqual(actual_level_three["player_class"], expected_level_three)

    def test_priest_upgrade(self):
        player = priest_ship(make_player())
        player["level"] = 2
        actual_level_two = class_upgrade(player)
        expected_level_two = 'Archangel'

        self.assertEqual(actual_level_two["player_class"], expected_level_two)

        player["level"] = 3
        actual_level_three = class_upgrade(player)
        expected_level_three = 'Seraphim'

        self.assertEqual(actual_level_three["player_class"], expected_level_three)