from unittest import TestCase
from unittest.mock import patch

from project.game import combat_enemy_flee


class TestCombatEnemyFlee(TestCase):
    @patch('random.randint', side_effect=[1])
    def test_flee_success(self, random_number_generator):
        self.assertTrue(combat_enemy_flee)

    @patch('random.randint', side_effect=[2])
    def test_flee_fail(self, random_number_generator):
        self.assertFalse(combat_enemy_flee())
