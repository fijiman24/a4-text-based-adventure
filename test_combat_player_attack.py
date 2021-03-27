from unittest import TestCase
from unittest.mock import patch
import io

from game import combat_player_attack
from game import make_player


class TestCombatPlayerAttack(TestCase):
    @patch('random.randint', side_effect=[5])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_remaining_enemy_health(self, mock_output, random_number_generator):
        player = make_player()
        actual_health = combat_player_attack(10, player)
        actual_output = mock_output.getvalue()

        expected_health = 5
        expected_output = "You did \033[94m5\033[0m damage to the enemy \033[91mDinghy\033[0m!\n\n"

        self.assertEqual(actual_output, expected_output)
        self.assertEqual(actual_health, expected_health)

    @patch('random.randint', side_effect=[20])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_negative_enemy_health(self, mock_output, random_number_generator):
        player = make_player()
        actual_health = combat_player_attack(10, player)
        actual_output = mock_output.getvalue()

        expected_health = -10
        expected_output = "You did \033[94m20\033[0m damage to the enemy \033[91mDinghy\033[0m!\n\n"

        self.assertEqual(actual_output, expected_output)
        self.assertEqual(actual_health, expected_health)

    @patch('random.randint', side_effect=[15])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_zero_enemy_health(self, mock_output, random_number_generator):
        player = make_player()
        actual_health = combat_player_attack(15, player)
        actual_output = mock_output.getvalue()

        expected_health = 0
        expected_output = "You did \033[94m15\033[0m damage to the enemy \033[91mDinghy\033[0m!\n\n"

        self.assertEqual(actual_output, expected_output)
        self.assertEqual(actual_health, expected_health)
