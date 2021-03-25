from unittest import TestCase
import unittest.mock
import io
from game import ascii_intro


class TestAsciiIntro(TestCase):
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_ascii_intro_print(self, mock_stdout):
        ascii_intro()
        expected = "[93m  /$$$$$$                        /$$                                /$$$$$$  /$$          " \
                   "\n /$$__  $$                      | $$                               /$$__  $$|__/          \n" \
                   "| $$  \\__/  /$$$$$$   /$$$$$$$ /$$$$$$    /$$$$$$   /$$$$$$       | $$  \\__/ /$$ /$$   /$$\n" \
                   "|  $$$$$$  /$$__  $$ /$$_____/|_  $$_/   /$$__  $$ /$$__  $$      |  $$$$$$ | $$|  $$ /$$/\n" \
                   " \\____  $$| $$$$$$$$| $$        | $$    | $$  \\ $$| $$  \\__/       \\____  $$| $$ \\  $$$$/ \n" \
                   " /$$  \\ $$| $$_____/| $$        | $$ /$$| $$  | $$| $$             /$$  \\ $$| $$  >$$  $$ \n" \
                   "|  $$$$$$/|  $$$$$$$|  $$$$$$$  |  $$$$/|  $$$$$$/| $$            |  $$$$$$/| $$ /$$/\\  $$\n" \
                   " \\______/  \\_______/ \\_______/   \\___/   \\______/ |__/             \\______/ |__/|__/  \\_" \
                   "_/\n[0m\n"
        self.assertEqual(expected, mock_stdout.getvalue())
