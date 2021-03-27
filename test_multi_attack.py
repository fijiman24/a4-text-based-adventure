from unittest import TestCase
from unittest.mock import patch
import io

from game import multi_attack
from game import make_player


class TestMultiAttack(TestCase):
    @patch('random.randint', return_value=5)
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_damage(self, mock_output, random_number_generator):
        player = make_player()
        actual = multi_attack(player)
        actual_output = mock_output.getvalue()

        expected = 25
        expected_output = "You dealt \033[94m5\033[0m damage to the enemy!\n" \
                          "You dealt \033[94m5\033[0m damage to the enemy!\n" \
                          "You dealt \033[94m5\033[0m damage to the enemy!\n" \
                          "You dealt \033[94m5\033[0m damage to the enemy!\n" \
                          "You dealt \033[94m5\033[0m damage to the enemy!\n"

        self.assertEqual(actual, expected)
        self.assertEqual(actual_output, expected_output)

    @patch('random.randint', side_effect=[1, 2, 3, 4, 5])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_damage_different_values(self, mock_output, random_number_generator):
        player = make_player()
        multi_attack(player)
        actual_output = mock_output.getvalue()

        expected_output = "You dealt \033[94m1\033[0m damage to the enemy!\n" \
                          "You dealt \033[94m2\033[0m damage to the enemy!\n" \
                          "You dealt \033[94m3\033[0m damage to the enemy!\n" \
                          "You dealt \033[94m4\033[0m damage to the enemy!\n" \
                          "You dealt \033[94m5\033[0m damage to the enemy!\n"
        self.assertEqual(actual_output, expected_output)
