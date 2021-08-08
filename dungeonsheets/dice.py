import random
import re
from collections import namedtuple
from itertools import groupby

from dungeonsheets.exceptions import DiceError

dice_re = re.compile(r"(\d+)d(\d+)", flags=re.I)
dice_part_re = re.compile(r"[0-9d]+", flags=re.I)
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


def combine_dice(dice_str):
    """Condense a dice string into its simplest representation.

    For example: "1d8 + 5 + 2d8 + 2" would be reduced to "3d8 + 7".

    Returns
    =======
    new_dice_str
      A new, condensed string for the given dice.
    
    """
    dice = []
    bonuses = 0
    # Sort out each portion of the dice string
    for part in dice_part_re.findall(dice_str):
        try:
            dice.append(read_dice_str(part))
        except DiceError:
            bonuses += int(part)
    # Recombine the dice into a more concise string
    new_parts = []
    dice = sorted(dice, key=lambda x: x.faces)
    for faces, grp in groupby(dice, key=lambda x: x.faces):
        new_parts.append(f"{sum([d.num for d in grp])}d{faces}")
    if bonuses > 0:
        new_parts.append(str(bonuses))
    new_dice_str = " + ".join(new_parts)
    return new_dice_str


def roll(a, b=None):
    """roll(20) means roll 1d20, roll(2, 6) means roll 2d6"""
    if b is None:
        return random.randint(1, a)
    else:
        return sum([random.randint(1, b) for _ in range(a)])
