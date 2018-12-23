from .features import Feature
from .. import (weapons, armor)


class UnarmoredDefenseMonk(Feature):
    """Beginning at 1st level, while you are wearing no armor and not wearing a
    shield, your AC equals 10 + your Dexterity modifier + your Wisdom modifier.

    This bonus is computed in the AC given on the Character Sheet above.

    """
    name = "Unarmored Defense"
    source = 'Monk'


class MartialArts(Feature):
    """At 1st level, your practice of martial arts gives you mastery of combat
    styles that use unarmed strikes and monk weapons, which are shortswords and
    any simple melee weapons that don’t have the two-handed or heavy
    property. You gain the following benefits while you are unarmed or wielding
    only monk weapons and you aren’t wearing armor or wielding a shield:

    -- You can use Dexterity instead of Strength for the attack and damage rolls
    of your unarmed strikes and monk weapons.

    -- You can roll a d4 in place of the normal damage of your unarmed strike or
    monk weapon. This die changes as you gain monk levels, as shown in the
    Martial Arts column of the Monk table.

    -- When you use the Attack action with an unarmed strike or a monk weapon on
    your turn, you can make one unarmed strike as a bonus action. For example,
    if you take the Attack action and attack with a quarter- staff, you can
    also make an unarmed strike as a bonus action, assuming you haven't already
    taken a bonus action this turn.

    Certain monasteries use specializepd forms of the monk weapons. For
    example, you might use a club that is two lengths of w ood connected by a
    short chain (called a nunchaku) or a sickle with a shorter, straighter
    blade (called a kama). Whatever name you use for a monk weapon, you can use
    the game statistics provided for

    """
    name = "Martial Arts"
    source = 'Monk'
    die = 'd4'

    def __init__(self, owner):
        self.owner = owner
        if self.owner.level >= 5:
            self.die = 'd6'
        if self.owner.level >= 11:
            self.die = 'd8'
        if self.owner.level >= 17:
            self.die = 'd10'

    def weapon_func(self, weapon: weapons.Weapon, char=None, **kwargs):
        """
        Update increasing damage dice and DEX mod of Monk weapons
        """
        is_monk_weapon = any([isinstance(weapon, w)
                              for w in weapons.monk_weapons])
        if not is_monk_weapon:
            return weapon
        if char is None:
            return weapon
        # check if new damage is better than default
        if self.die > int(weapon.base_damage.split('d')[-1]):
            weapon.base_damage = '1d' + str(self.die)
        weapon.is_finesse = True
        return weapon


class UnarmoredMovement(Feature):
    """Starting at 2nd level, your speed increases by 10 feet while you are not
    wearing armor or wielding a shield. This bonus increases when you reach
    certain monk levels, as shown in the Monk table.

    At 9th level, you gain the ability to move along vertical surfaces and
    across liquids on your turn without falling during the move.

    """
    name = "Unarmored Movement"
    source = "Monk"
    speed_bonus = 10

    def __init__(self, owner):
        self.owner = owner
        if self.owner.level >= 6:
            self.speed_bonus = 15
        if self.owner.level >= 10:
            self.speed_bonus = 20
        if self.owner.level >= 14:
            self.speed_bonus = 25
        if self.owner.level >= 18:
            self.speed_bonus = 30
