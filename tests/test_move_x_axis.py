from unittest import TestCase
from project.game import move_x_axis


class TestMoveXAxis(TestCase):
    def test_move_left(self):
        actual = move_x_axis(2, 3)
        expected = 2
        self.assertTrue(actual, expected)

    def test_move_right(self):
        actual = move_x_axis(4, 11)
        expected = 12
        self.assertTrue(actual, expected)

    def test_not_valid_movement(self):
        actual = move_x_axis(1, 4)
        expected = 4
        self.assertEqual(actual, expected)
