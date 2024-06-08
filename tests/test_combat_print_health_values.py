from unittest import TestCase
from unittest.mock import patch
import io

from project.game import combat_print_health_values
from project.game import make_player
from project.game import make_appropriate_enemy_type
from project.game import warrior_ship


class TestCombatPrintHealthValues(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_statement(self, mock_output):
        player = warrior_ship(make_player())
        enemy = make_appropriate_enemy_type(player)
        combat_print_health_values(player, enemy)
        actual = mock_output.getvalue()

        expected = "Your \033[94mSquire\033[0m can take \033[94m18\033[0m more points of damage.\n" \
                   "The enemy \033[91mDinghy\033[0m can take \033[91m10\033[0m more points of damage.\n\n"

        self.assertEqual(actual, expected)
