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
        # Modifier
        out = dice.read_dice_str("2d20 + 5")
        self.assertEqual(out.faces, 20)
        self.assertEqual(out.num, 2)
        self.assertEqual(out.modifier, 5)
        # Check a bad value
        with self.assertRaises(DiceError):
            dice.read_dice_str("Ed15")

    def test_combine_dice(self):
        self.assertEqual(dice.combine_dice("1d8 + 6 + 2d8 + 12"), "3d8 + 18")
        self.assertEqual(dice.combine_dice("1d8 + 1d5 + 2d8 + 1d5"), "2d5 + 3d8")
        
    def test_dice_mean(self):
        dd = dice.read_dice_str("1d10")
        dd_mean = dice._dice_mean(dd)
        self.assertEqual(dd_mean, 5.5)
        dd = dice.read_dice_str("2d20+4")
        dd_mean = dice._dice_mean(dd)
        self.assertEqual(dd_mean, 25)
        
    def test_dice_roll_mean(self):
        dd_mean = dice.dice_roll_mean("1d6")
        self.assertEqual(dd_mean, 4)
        dd_mean = dice.dice_roll_mean("2d20+2")
        self.assertEqual(dd_mean, 23)
        
    def test_simple_rolling(self):
        num_tests = 100
        # Do a bunch of rolls and make sure the numbers are within the requsted range
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
