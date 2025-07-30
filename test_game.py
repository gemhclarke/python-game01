import unittest
from unittest.mock import patch
from io import StringIO
import sys

# Assuming your main code is in game.py
import Game


class TestAdventureGame(unittest.TestCase):

    def test_start_right_swim(self):
        inputs = ["right", "swim"]
        expected_output = [
            "You are in the woods.",
            "You continue down the path to the right.",
            "You reach a river.",
            "You swim across the river and find a treasure chest!"
        ]

        with patch("builtins.input", side_effect=inputs), patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            Game.start()
            output = mock_stdout.getvalue()
            for line in expected_output:
                self.assertIn(line, output)

    def test_start_left_enter(self):
        inputs = ["left", "enter"]
        expected_output = [
            "You are in the woods.",
            "You continue down the path to the left.",
            "You arrive at a small fort.",
            "You enter the fort and find a hidden passage."
        ]

        with patch("builtins.input", side_effect=inputs), patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            Game.start()
            output = mock_stdout.getvalue()
            for line in expected_output:
                self.assertIn(line, output)

    def test_invalid_start_then_right_walk(self):
        inputs = ["forward", "right", "walk"]
        expected_output = [
            "That's not a valid direction.",
            "You continue down the path to the right.",
            "You walk along the bank and find a fishing spot."
        ]

        with patch("builtins.input", side_effect=inputs), patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            Game.start()
            output = mock_stdout.getvalue()
            for line in expected_output:
                self.assertIn(line, output)


if __name__ == '__main__':
    unittest.main()
