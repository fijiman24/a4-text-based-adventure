from unittest import TestCase
from unittest.mock import patch

from game import spawn_enemy


class TestSpawnEnemy(TestCase):
    @patch('random.randint', side_effect=[1])
    def test_spawn(self, random_number_generator):
        self.assertTrue(spawn_enemy())

    @patch('random.randint', side_effect=[3])
    def test_not_spawn(self, random_number_generator):
        self.assertFalse(spawn_enemy())
