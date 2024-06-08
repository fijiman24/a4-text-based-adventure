from unittest import TestCase
from unittest.mock import patch
import io

from project.game import make_player
from project.game import warrior_ship
from project.game import magician_ship
from project.game import thief_ship
from project.game import priest_ship
from project.game import special_action_selector
from project.game import resurrect


class TestSpecialActionSelector(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_select_warrior(self, mock_output):
        player = warrior_ship(make_player())
        actual = id(special_action_selector(player))
        actual_output = mock_output.getvalue()

        expected = id(resurrect(player))
        expected_output = "Your passive will allow you to survive a critical attack.\n\n"

        self.assertEqual(actual, expected)
        self.assertEqual(actual_output, expected_output)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_select_magician(self, mock_output):
        player = magician_ship(make_player())
        actual_damage = special_action_selector(player)
        actual_output = mock_output.getvalue()

        expected_damage = 0
        expected_output = "You relinquished your charges to deal \033[94m0\033[0m to the enemy!\n"

        self.assertEqual(actual_damage, expected_damage)
        self.assertEqual(actual_output, expected_output)

    @patch('random.randint', return_value=5)
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_select_thief(self, mock_output, random_number_generator):
        player = thief_ship(make_player())
        actual = special_action_selector(player)
        actual_output = mock_output.getvalue()

        expected = 25
        expected_output = "You dealt \033[94m5\033[0m damage to the enemy!\n" \
                          "You dealt \033[94m5\033[0m damage to the enemy!\n" \
                          "You dealt \033[94m5\033[0m damage to the enemy!\n" \
                          "You dealt \033[94m5\033[0m damage to the enemy!\n" \
                          "You dealt \033[94m5\033[0m damage to the enemy!\n"

        self.assertEqual(actual, expected)
        self.assertEqual(actual_output, expected_output)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_select_priest(self, mock_output):
        player = priest_ship(make_player())
        special_action_selector(player)
        actual = mock_output.getvalue()

        expected = "You repaired your hull for \033[94m0\033[0m health.\n"

        self.assertEqual(actual, expected)
