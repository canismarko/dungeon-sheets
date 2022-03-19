import random
import re
from collections import namedtuple
from itertools import groupby

from dungeonsheets.exceptions import DiceError

dice_re = re.compile(r"(\d+)d(\d+)([+-]\d+)*", flags=re.I)
dice_part_re = re.compile(r"[0-9d]+", flags=re.I)
Dice = namedtuple("Dice", ("num", "faces", "modifier"))


def read_dice_str(dice_str):
    """Interpret a D&D dice string, eg. 3d10+2.

    Returns
    -------
    dice : tuple
      A named tuple with the scheme (num, faces), so '3d10-2' return
      (num=3, faces=10, modifier=-2)

    """
    dice_str = dice_str.replace(" ", "").replace("\n", "")
    match = dice_re.search(dice_str)
    if match is None:
        raise DiceError(f"Cannot interpret dice string {dice_str}")
    num, faces = int(match.group(1)), int(match.group(2))
    if match.group(3) is None:
        modifier = 0
    else:
        modifier = int(match.group(3))
    dice = Dice(num, faces, modifier)
    return dice

def _dice_mean(dice, force_min=True):
    """Support function for calculating dice string mean."""
    dmg_min = dice.num + dice.modifier
    dmg_max = dice.num*dice.faces + dice.modifier
    return (dmg_max - dmg_min)/2.0 + dmg_min

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
    
def dice_roll_mean(dice_text):
    """Takes a dice string like '3d6 +3' and returns its average roll."""
    dice = read_dice_str(dice_text)
    return round(_dice_mean(dice))

