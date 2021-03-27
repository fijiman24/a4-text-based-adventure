from unittest import TestCase
from game import move_y_axis


class TestMoveYAxis(TestCase):
    def test_move_up(self):
        actual = move_y_axis(1, 5)
        expected = 4

        self.assertTrue(actual, expected)

    def test_move_down(self):
        actual = move_y_axis(3, 6)
        expected = 7

        self.assertTrue(actual, expected)

    def test_not_valid_movement(self):
        actual = move_y_axis(2, 5)
        expected = 5
        self.assertEqual(actual, expected)
