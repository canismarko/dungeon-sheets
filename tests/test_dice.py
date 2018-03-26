from unittest import TestCase

from dungeonsheets.exceptions import DiceError
from dungeonsheets import dice

class TestDice(TestCase):

    def test_read_dice_str(self):
        out = dice.read_dice_str('1d6')
        self.assertEqual(out.faces, 6)
        self.assertEqual(out.num, 1)
        # Multiple digits
        out = dice.read_dice_str('15d10')
        self.assertEqual(out.faces, 10)
        self.assertEqual(out.num, 15)
        # Check a bad value
        with self.assertRaises(DiceError):
            dice.read_dice_str('Ed15')
