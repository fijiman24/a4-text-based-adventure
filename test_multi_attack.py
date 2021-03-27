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
