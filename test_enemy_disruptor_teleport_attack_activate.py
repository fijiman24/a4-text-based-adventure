import io
from unittest import TestCase
from unittest.mock import patch
from game import make_player
from game import enemy_disruptor_teleport_attack_activate
from game import make_enemy_difficulty_three


class Test(TestCase):
    @patch('random.randint', side_effect=[5, 5])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_disruptor_ability_counter_greater_than_zero(self, mock_output, random_number_generator):
        player_character = make_player()
        enemy = make_enemy_difficulty_three()
        enemy_disruptor_teleport_attack_activate(enemy, player_character)
        the_game_printed_this = mock_output.getvalue()
        expected_output = ""
        self.assertEqual(expected_output, the_game_printed_this)

    @patch('random.randint', side_effect=[5, 5])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_disruptor_ability_counter_less_than_zero(self, mock_output, random_number_generator):
        player_character = make_player()
        enemy = make_enemy_difficulty_three()
        enemy["special_ability_counter"] = -1
        enemy_disruptor_teleport_attack_activate(enemy, player_character)
        the_game_printed_this = mock_output.getvalue()
        expected_output = ""
        self.assertEqual(expected_output, the_game_printed_this)

    @patch('random.randint', side_effect=[5, 5])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_disruptor_teleport_attack_earliest_location(self, mock_output, random_number_generator):
        player_character = make_player()
        enemy = make_enemy_difficulty_three()
        enemy["special_ability_counter"] = 0
        enemy_disruptor_teleport_attack_activate(enemy, player_character)
        the_game_printed_this = mock_output.getvalue()
        expected_output = "The enemy [91mDisruptor[0m opened a rift in spacetime and teleported you to 5, 5!\n"
        self.assertEqual(expected_output, the_game_printed_this)

    @patch('random.randint', side_effect=[9, 9])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_disruptor_teleport_attack_latest_location(self, mock_output, random_number_generator):
        player_character = make_player()
        enemy = make_enemy_difficulty_three()
        enemy["special_ability_counter"] = 0
        enemy_disruptor_teleport_attack_activate(enemy, player_character)
        the_game_printed_this = mock_output.getvalue()
        expected_output = "The enemy [91mDisruptor[0m opened a rift in spacetime and teleported you to 9, 9!\n"
        self.assertEqual(expected_output, the_game_printed_this)
