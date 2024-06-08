from unittest import TestCase
from unittest.mock import patch
import io

from project.game import combat_enemy_attack
from project.game import make_player


class TestCombatEnemyAttack(TestCase):
    @patch('random.randint', side_effect=[10])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_player_remaining_health(self, mock_output, random_number_generator):
        player = make_player()
        actual_health = combat_enemy_attack(player)
        actual_output = mock_output.getvalue()

        expected_health = 10
        expected_output = "The enemy \033[91mDinghy\033[0m did \033[91m10\033[0m damage to you!\n\n"

        self.assertEqual(actual_output, expected_output)
        self.assertEqual(actual_health, expected_health)

    @patch('random.randint', side_effect=[10])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_player_zero_health(self, mock_output, random_number_generator):
        player = make_player()
        player["health"] = 10
        actual_health = combat_enemy_attack(player)
        actual_output = mock_output.getvalue()

        expected_health = 0
        expected_output = "The enemy \033[91mDinghy\033[0m did \033[91m10\033[0m damage to you!\n\n"

        self.assertEqual(actual_output, expected_output)
        self.assertEqual(actual_health, expected_health)

    @patch('random.randint', side_effect=[15])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_player_negative_health(self, mock_output, random_number_generator):
        player = make_player()
        player["health"] = 10
        actual_health = combat_enemy_attack(player)
        actual_output = mock_output.getvalue()

        expected_health = -5
        expected_output = "The enemy \033[91mDinghy\033[0m did \033[91m15\033[0m damage to you!\n\n"

        self.assertEqual(actual_output, expected_output)
        self.assertEqual(actual_health, expected_health)
