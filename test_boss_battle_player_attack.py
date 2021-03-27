import io
from unittest import TestCase
from unittest.mock import patch
from game import boss_battle_player_attack
from game import make_player
from game import make_appropriate_boss_phase


class Test(TestCase):
    @patch('random.randint', return_value=5)
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_boss_battle_phase_one_player_attack_correct_print(self, mock_output, random_number_generator):
        player = make_player()
        boss = make_appropriate_boss_phase(player)
        boss_battle_player_attack(boss, player)
        actual = mock_output.getvalue()
        expected = "You did [94m5[0m damage to the [95mIntergalactic Space Worm[0m!\n\n"
        self.assertEqual(expected, actual)

    @patch('random.randint', return_value=5)
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_boss_battle_phase_two_player_attack_correct_print(self, mock_output, random_number_generator):
        player = make_player()
        player["boss_phase_counter"] = 2
        boss = make_appropriate_boss_phase(player)
        boss_battle_player_attack(boss, player)
        actual = mock_output.getvalue()
        expected = "You did [94m5[0m damage to the [95mTwo-Headed Intergalactic Space Worm[0m!\n\n"
        self.assertEqual(expected, actual)

    @patch('random.randint', return_value=5)
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_boss_battle_phase_three_player_attack_correct_print(self, mock_output, random_number_generator):
        player = make_player()
        player["boss_phase_counter"] = 1
        boss = make_appropriate_boss_phase(player)
        boss_battle_player_attack(boss, player)
        actual = mock_output.getvalue()
        expected = "You did [94m5[0m damage to the [95mHeadless Intergalactic Space Worm[0m!\n\n"
        self.assertEqual(expected, actual)

    @patch('random.randint', return_value=5)
    def test_boss_battle_phase_player_attack_updates_boss_health(self, random_number_generator):
        player = make_player()
        boss = make_appropriate_boss_phase(player)
        boss["health"] = 10
        actual = boss_battle_player_attack(boss, player)
        expected = 5
        self.assertEqual(expected, actual)
