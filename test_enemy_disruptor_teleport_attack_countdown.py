from unittest import TestCase
import unittest.mock
import io
from game import enemy_disruptor_teleport_attack_countdown
from game import make_enemy_difficulty_three


class Test(TestCase):
    def test_enemy_special_ability_counter_decrement(self):
        enemy = make_enemy_difficulty_three()
        original_charge_value = enemy["special_ability_counter"]
        enemy_disruptor_teleport_attack_countdown(enemy)
        expected = original_charge_value - 1
        self.assertEqual(expected, enemy["special_ability_counter"])

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_charging_attack_print_statement(self, mock_stdout):
        enemy = make_enemy_difficulty_three()
        enemy_disruptor_teleport_attack_countdown(enemy)
        expected = "The enemy \033[91mDisruptor\033[0m is charging...something.\n"
        self.assertEqual(expected, mock_stdout.getvalue())

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_no_print_counter_under_zero(self, mock_stdout):
        enemy = make_enemy_difficulty_three()
        enemy["special_ability_counter"] = -1
        expected = ""
        self.assertEqual(expected, mock_stdout.getvalue())
