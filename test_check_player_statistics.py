from unittest import TestCase
from unittest.mock import patch
import io
from game import make_player
from game import check_player_statistics


class Test(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_check_player_statistics_default_player_values(self, mock_output):
        player = make_player()
        check_player_statistics(player)
        actual = mock_output.getvalue()
        expected = "You are Captain [94mNone[0m.\nCaptain None pilots a [94mNone[0m, which has the " \
                   "special ability [94mNone[0m.\nYour None can take [94m20[0m more points of damage." \
                   "\nYour None is level [94m1[0m.\nYou have [94m0[0m scrap, [94m300[0m scrap away " \
                   "from a [94mship upgrade[0m.\n\n"
        self.assertEqual(expected, actual)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_check_player_statistics_new_player_values(self, mock_output):
        player = make_player()
        player["name"] = "Gerry"
        player["player_class"] = "Ghost"
        player["player_class_special_action"] = "Multi Attack"
        check_player_statistics(player)
        actual = mock_output.getvalue()
        expected = "You are Captain [94mGerry[0m.\nCaptain Gerry pilots a [94mGhost[0m, which has the " \
                   "special ability [94mMulti Attack[0m.\nYour Ghost can take [94m20[0m more points of " \
                   "damage.\nYour Ghost is level [94m1[0m.\nYou have [94m0[0m scrap, [94m300[0m " \
                   "scrap away from a [94mship upgrade[0m.\n\n"
        self.assertEqual(expected, actual)
