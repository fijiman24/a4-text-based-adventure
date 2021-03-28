from unittest import TestCase
from unittest.mock import patch
import io

from game import combat_initiative_roll
from game import make_player


class TestCombatInitiativeRoll(TestCase):
    @patch('random.randint', side_effect=["50", "50", "1", "2"])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_draw(self, mock_output, random_number_generator):
        player = make_player()
        combat_initiative_roll(player)
        actual = mock_output.getvalue()

        expected = "Draw! You both rolled a \033[94m50\033[0m. Rerolling....\n\n" \
                   "You rolled a \033[94m1\033[0m and the enemy \033[91mDinghy\033[0m" \
                   " rolled \033[91m2\033[0m. The enemy \033[91mDinghy\033[0m will attack first.\n\n"

        self.assertEqual(actual, expected)

    @patch('random.randint', side_effect=["40", "50"])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_enemy_attack_first(self, mock_output, random_number_generator):
        player = make_player()
        combat_initiative_roll(player)
        actual = mock_output.getvalue()

        expected = "You rolled a \033[94m40\033[0m and the enemy \033[91mDinghy\033[0m" \
                   " rolled \033[91m50\033[0m. The enemy \033[91mDinghy\033[0m will attack first.\n\n"

        self.assertEqual(actual, expected)

    @patch('random.randint', side_effect=["50", "40"])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_player_attack_first(self, mock_output, random_number_generator):
        player = make_player()
        combat_initiative_roll(player)
        actual = mock_output.getvalue()

        expected = "You rolled a \033[94m50\033[0m and the enemy \033[91mDinghy\033[0m rolled a \033[91m40\033[0m." \
                   " You will attack first.\n\n"

        self.assertEqual(actual, expected)
