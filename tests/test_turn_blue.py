from unittest import TestCase
from project.game import turn_blue


class Test(TestCase):
    def test_turn_blue_string(self):
        actual = turn_blue("Hello")
        expected = "[94mHello[0m"
        self.assertEqual(expected, actual)

    def test_turn_blue_empty_string(self):
        actual = turn_blue("")
        expected = "[94m[0m"
        self.assertEqual(expected, actual)

    def test_turn_blue_integer_argument(self):
        actual = turn_blue(1)
        expected = "[94m1[0m"
        self.assertEqual(expected, actual)
