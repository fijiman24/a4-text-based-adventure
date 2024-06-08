from unittest import TestCase
from project.game import make_appropriate_enemy_type
from project.game import make_enemy_difficulty_one
from project.game import make_enemy_difficulty_two
from project.game import make_enemy_difficulty_three
from project.game import make_enemy_difficulty_four
from project.game import make_player


class Test(TestCase):
    def test_make_appropriate_enemy_difficulty_one(self):
        player_character = make_player()
        actual = make_appropriate_enemy_type(player_character)
        expected = make_enemy_difficulty_one()
        self.assertEqual(expected, actual)

    def test_make_appropriate_enemy_difficulty_two_player_minimum_x_coordinate(self):
        player_character = make_player()
        player_character["x-coordinate"] = 5
        actual = make_appropriate_enemy_type(player_character)
        expected = make_enemy_difficulty_two()
        self.assertEqual(expected, actual)

    def test_make_appropriate_enemy_difficulty_two_player_minimum_y_coordinate(self):
        player_character = make_player()
        player_character["y-coordinate"] = 5
        actual = make_appropriate_enemy_type(player_character)
        expected = make_enemy_difficulty_two()
        self.assertEqual(expected, actual)

    def test_make_appropriate_enemy_difficulty_three_player_minimum_x_coordinate(self):
        player_character = make_player()
        player_character["x-coordinate"] = 15
        actual = make_appropriate_enemy_type(player_character)
        expected = make_enemy_difficulty_three()
        self.assertEqual(expected, actual)

    def test_make_appropriate_enemy_difficulty_three_player_minimum_y_coordinate(self):
        player_character = make_player()
        player_character["y-coordinate"] = 15
        actual = make_appropriate_enemy_type(player_character)
        expected = make_enemy_difficulty_three()
        self.assertEqual(expected, actual)

    def test_make_appropriate_enemy_difficulty_four_player_minimum_x_coordinate(self):
        player_character = make_player()
        player_character["x-coordinate"] = 20
        actual = make_appropriate_enemy_type(player_character)
        expected = make_enemy_difficulty_four()
        self.assertEqual(expected, actual)

    def test_make_appropriate_enemy_difficulty_four_player_minimum_y_coordinate(self):
        player_character = make_player()
        player_character["y-coordinate"] = 20
        actual = make_appropriate_enemy_type(player_character)
        expected = make_enemy_difficulty_four()
        self.assertEqual(expected, actual)
