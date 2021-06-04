import random
import re
from collections import namedtuple

from dungeonsheets.exceptions import DiceError

dice_re = re.compile(r"(\d+)d(\d+)", flags=re.I)
Dice = namedtuple("Dice", ("num", "faces"))


def read_dice_str(dice_str):
    """Interpret a D&D dice string, eg. 3d10.

    Returns
    -------
    dice : tuple
      A named tuple with the scheme (num, faces), so '3d10' return
      (num=3, faces=10)

    """
    match = dice_re.match(dice_str)
    if match is None:
        raise DiceError(f"Cannot interpret dice string {dice_str}")
    dice = Dice(num=int(match.group(1)), faces=int(match.group(2)))
    return dice


def roll(a, b=None):
    """roll(20) means roll 1d20, roll(2, 6) means roll 2d6"""
    if b is None:
        return random.randint(1, a)
    else:
        return sum([random.randint(1, b) for _ in range(a)])
