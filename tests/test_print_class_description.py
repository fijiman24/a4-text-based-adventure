from unittest import TestCase
from unittest.mock import patch
import io

from project.game import print_class_description


class TestPrintClassDescription(TestCase):

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_squire_class(self, mock_output):
        print_class_description("Squire")
        actual = mock_output.getvalue()
        expected = "A Lazarus Engine™ allows for this ship to repair itself after its hull " \
                   "integrity has been completely breached for the first time.\n"
        self.assertEqual(actual, expected)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_sapper_class(self, mock_output):
        print_class_description("Sapper")
        actual = mock_output.getvalue()
        expected = "Destroy enemy ships to steal their energy and charge up your Quasar Cannon™ " \
                   "for a devastating attack.\n"
        self.assertEqual(actual, expected)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_ghost_class(self, mock_output):
        print_class_description("Ghost")
        actual = mock_output.getvalue()
        expected = "A nimble ship covered in aerodynamic SlipStream™ technology allows the pilot to make" \
                   " the first move in combat, and attack multiple times in one turn.\n"
        self.assertEqual(actual, expected)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_cherub_class(self, mock_output):
        print_class_description("Cherub")
        actual = mock_output.getvalue()
        expected = "QuickFix™ Protocols allows this ship to repair itself during combat.\n"
        self.assertEqual(actual, expected)
