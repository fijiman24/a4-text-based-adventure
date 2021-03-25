from unittest import TestCase
import unittest.mock
import io
from game import story_introduction_text


class Test(TestCase):
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_ascii_intro_print(self, mock_stdout):
        story_introduction_text()
        expected = "In the distant future, humankind has colonized the vast, cold reaches of space. From suburban " \
                   "planets to entire solar systems dedicated to vice, there isn't a sector in the\nMilky Way Galaxy " \
                   "that's been left untouched by our ever-expanding race. One such sector is devoted to storing all " \
                   "of humanity's physical wealth and fortune. Many a space\npirate has tried their hand at laying " \
                   "siege to this sector in hopes of plundering some riches for themselves, and all have been gunned " \
                   "down by the local security militias. \n\nAll except you. You put together a ragtag crew, " \
                   "formulated the perfect plan, and somehow managed to fill your ship with as much stolen loot as " \
                   "she could carry. Now all you\nhave to do is escape to the nearest wormhole, treasure in tow, " \
                   "and you'll be christened the first ever space captain to have successfully pilfered from...\n\n"
        self.assertEqual(expected, mock_stdout.getvalue())
