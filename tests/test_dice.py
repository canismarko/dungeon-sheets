from unittest import TestCase

from dungeonsheets.dice import roll
from dungeonsheets.exceptions import DiceError
from dungeonsheets import dice


class TestDice(TestCase):

    def test_read_dice_str(self):
        out = dice.read_dice_str("1d6")
        self.assertEqual(out.faces, 6)
        self.assertEqual(out.num, 1)
        # Multiple digits
        out = dice.read_dice_str("15d10")
        self.assertEqual(out.faces, 10)
        self.assertEqual(out.num, 15)
        # Check a bad value
        with self.assertRaises(DiceError):
            dice.read_dice_str("Ed15")

    def test_simple_rolling(self):
        num_tests = 100
        for _ in range(num_tests):
            result = roll(6)
            self.assertGreaterEqual(result, 1)
            self.assertLessEqual(result, 6)

    def test_multi_rolling(self):
        num_tests = 100
        for _ in range(num_tests):
            result = roll(2, 4)  # Roll 2d4
            self.assertGreaterEqual(result, 2)
            self.assertLessEqual(result, 8)
