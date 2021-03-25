from unittest import TestCase
import unittest.mock
import io
from game import boss_fight_start_text
from game import make_player


class Test(TestCase):
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_boss_fight_start_text_phase_one(self, mock_stdout):
        player_character = make_player()
        boss_fight_start_text(player_character)
        expected = "You've almost escaped from Sector Six, treasure in tow. To your surprise, the enemy militia is " \
                   "nowhere to be found. Where's their final resistance?\nAs you begin your approach to the " \
                   "wormhole's entrance, a shrill scream surrounds your ship. Sound...isn't supposed to travel " \
                   "through space. Whatever made that\nsound transcends the laws of nature itself. From the pitch" \
                   " black of the wormhole, you notice a pair of scarlet eyes peering back at you from the darkness." \
                   "\nA titanic, grotesque [95mpink[0m body emerges from the wormhole. It's an...\n" \
                   "[95mIntergalactic Space Worm[0m!\n\n"
        self.assertEqual(expected, mock_stdout.getvalue())

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_boss_fight_start_text_phase_two(self, mock_stdout):
        player_character = make_player()
        player_character["boss_phase_counter"] = 2
        boss_fight_start_text(player_character)
        expected = "It's a [95mTwo-Headed Intergalactic Space Worm[0m!\n\n"
        self.assertEqual(expected, mock_stdout.getvalue())

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_boss_fight_start_text_phase_three(self, mock_stdout):
        player_character = make_player()
        player_character["boss_phase_counter"] = 1
        boss_fight_start_text(player_character)
        expected = "Get rid of the [95mHeadless Intergalactic Space Worm[0m to finally escape Sector Six!\n\n"
        self.assertEqual(expected, mock_stdout.getvalue())
