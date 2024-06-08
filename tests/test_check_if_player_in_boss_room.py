from unittest import TestCase
from project.game import check_if_player_in_boss_room


class Test(TestCase):
    def test_zero_coordinates(self):
        self.assertFalse(check_if_player_in_boss_room(0, 0))

    def test_equal_positive_coordinates(self):
        self.assertFalse(check_if_player_in_boss_room(12, 12))

    def test_equal_negative_coordinates(self):
        self.assertFalse(check_if_player_in_boss_room(-5, -5))

    def test_unequal_positive_coordinates(self):
        self.assertFalse(check_if_player_in_boss_room(215, 45))

    def test_unequal_negative_coordinates(self):
        self.assertFalse(check_if_player_in_boss_room(-20, -5))

    def test_in_boss_room(self):
        self.assertTrue(check_if_player_in_boss_room(24, 24))

