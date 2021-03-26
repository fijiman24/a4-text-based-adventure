from unittest import TestCase
import unittest.mock
import io
from game import boss_phase_death_text
from game import make_player


class Test(TestCase):
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_boss_death_text_phase_one(self, mock_stdout):
        player_character = make_player()
        boss_phase_death_text(player_character)
        expected = "You manage to obliterate the [95mIntergalactic Space Worm[0m's head!\nHowever, its " \
                   "smouldering corpse begins to convulse, and from the gaping hole in its neck sprouts two more " \
                   "heads!\n\n"
        self.assertEqual(expected, mock_stdout.getvalue())

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_boss_death_text_phase_two(self, mock_stdout):
        player_character = make_player()
        player_character["boss_phase_counter"] = 2
        boss_phase_death_text(player_character)
        expected = "You manage to obliterate the [95mTwo-Headed Intergalactic Space Worm[0m's heads!\nHowever, " \
                   "its corpse now blocks the entrance to the wormhole.\n\n"
        self.assertEqual(expected, mock_stdout.getvalue())

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_boss_death_text_phase_three(self, mock_stdout):
        player_character = make_player()
        player_character["boss_phase_counter"] = 1
        boss_phase_death_text(player_character)
        expected = "You finally obliterate the [95mHeadless Intergalactic Space Worm[0m!\n\n"
        self.assertEqual(expected, mock_stdout.getvalue())
