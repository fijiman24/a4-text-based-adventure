from unittest import TestCase
import unittest.mock
import io
from project.game import enemy_death_text
from project.game import make_player


class Test(TestCase):
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_enemy_difficulty_one_death_text_print(self, mock_stdout):
        player_character = make_player()
        enemy_death_text(player_character)
        expected = "The enemy \033[91mDinghy\033[0m has been defeated!\n\n"
        self.assertEqual(expected, mock_stdout.getvalue())

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_enemy_difficulty_two_death_text_print(self, mock_stdout):
        player_character = make_player()
        player_character["x-coordinate"] = 5
        enemy_death_text(player_character)
        expected = "The enemy \033[91mGunner\033[0m has been defeated!\n\n"
        self.assertEqual(expected, mock_stdout.getvalue())

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_enemy_difficulty_three_death_text_print(self, mock_stdout):
        player_character = make_player()
        player_character["x-coordinate"] = 15
        enemy_death_text(player_character)
        expected = "The enemy \033[91mDisruptor\033[0m has been defeated!\n\n"
        self.assertEqual(expected, mock_stdout.getvalue())

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_enemy_difficulty_four_death_text_print(self, mock_stdout):
        player_character = make_player()
        player_character["x-coordinate"] = 20
        enemy_death_text(player_character)
        expected = "The enemy \033[91mShredder\033[0m has been defeated!\n\n"
        self.assertEqual(expected, mock_stdout.getvalue())
