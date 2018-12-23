from .features import Feature
from .. import (weapons, armor)


class UnarmoredDefenseBarbarian(Feature):
    """While you are not wearing any armor, your Armor Class equals 10 + your
    Dexterity modifier + your Constitution modifier. You can use a shield and
    still gain this benefit.

    This bonus is computed in the AC given on the Character Sheet above.

    """
    name = "Unarmored Defense"
    source = 'Barbarian'


class FastMovement(Feature):
    """Starting at 5th level, your speed increases by 10 feet while you aren’t
    wearing heavy armor.

    """
    name = "Fast Movement"
    source = "Barbarian"
