from unittest import TestCase
import unittest.mock
import io
from game import story_ending_text
from game import make_player


class Test(TestCase):
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_story_ending_text_print(self, mock_stdout):
        player_character = make_player()
        player_character["name"] = "Tirion"
        story_ending_text(player_character)
        expected = "You and your crew disappear into the wormhole, along with untold treasure. For millennia, the " \
                   "galaxy will tell tales of the legendary\nCaptain [94mTirion[0m, the first space captain " \
                   "to pilfer from...\n\n"\
                   "[93m  /$$$$$$                        /$$                                /$$$$$$  /$$          " \
                   "\n /$$__  $$                      | $$                               /$$__  $$|__/          \n" \
                   "| $$  \\__/  /$$$$$$   /$$$$$$$ /$$$$$$    /$$$$$$   /$$$$$$       | $$  \\__/ /$$ /$$   /$$\n" \
                   "|  $$$$$$  /$$__  $$ /$$_____/|_  $$_/   /$$__  $$ /$$__  $$      |  $$$$$$ | $$|  $$ /$$/\n" \
                   " \\____  $$| $$$$$$$$| $$        | $$    | $$  \\ $$| $$  \\__/       \\____  $$| $$ \\  $$$$/ \n" \
                   " /$$  \\ $$| $$_____/| $$        | $$ /$$| $$  | $$| $$             /$$  \\ $$| $$  >$$  $$ \n" \
                   "|  $$$$$$/|  $$$$$$$|  $$$$$$$  |  $$$$/|  $$$$$$/| $$            |  $$$$$$/| $$ /$$/\\  $$\n" \
                   " \\______/  \\_______/ \\_______/   \\___/   \\______/ |__/             \\______/ |__/|__/  \\_" \
                   "_/\n[0m\n" \
                   "Thanks for playing!\n"
        self.assertEqual(expected, mock_stdout.getvalue())
