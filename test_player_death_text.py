from unittest import TestCase
import unittest.mock
import io
from game import player_death_text


class Test(TestCase):
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_player_death_text_print(self, mock_stdout):
        player_death_text()
        expected = "Your ship's integrity has been breached! Sector Six has claimed another crew of would-be " \
                   "thieves.\n\n\033[91mYOU ARE DEAD\033[0m\n"
        self.assertEqual(expected, mock_stdout.getvalue())
