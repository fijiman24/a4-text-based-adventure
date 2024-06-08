from unittest import TestCase
import io
from unittest.mock import patch
from project.game import boss_battle_print_health_values
from project.game import make_player
from project.game import make_appropriate_boss_phase


class Test(TestCase):
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_boss_phase_one_print_health_values(self, mock_output):
        player = make_player()
        player["player_class"] = "Ghost"
        boss = make_appropriate_boss_phase(player)
        boss_battle_print_health_values(player, boss)
        actual = mock_output.getvalue()
        expected = "Your [94mGhost[0m can take [94m20[0m more points of damage.\nThe enemy " \
                   "[95mIntergalactic Space Worm[0m can take [95m40[0m more points of damage.\n\n"
        self.assertEqual(expected, actual)

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_boss_phase_two_print_health_values(self, mock_output):
        player = make_player()
        player["player_class"] = "Ghost"
        player["boss_phase_counter"] = 2
        boss = make_appropriate_boss_phase(player)
        boss_battle_print_health_values(player, boss)
        actual = mock_output.getvalue()
        expected = "Your [94mGhost[0m can take [94m20[0m more points of damage.\nThe enemy " \
                   "[95mTwo-Headed Intergalactic Space Worm[0m can take [95m50[0m more points of damage.\n\n"
        self.assertEqual(expected, actual)

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_boss_phase_three_print_health_values(self, mock_output):
        player = make_player()
        player["player_class"] = "Ghost"
        player["boss_phase_counter"] = 1
        boss = make_appropriate_boss_phase(player)
        boss_battle_print_health_values(player, boss)
        actual = mock_output.getvalue()
        expected = "Your [94mGhost[0m can take [94m20[0m more points of damage.\nThe enemy " \
                   "[95mHeadless Intergalactic Space Worm[0m can take [95m80[0m more points of damage.\n\n"
        self.assertEqual(expected, actual)
