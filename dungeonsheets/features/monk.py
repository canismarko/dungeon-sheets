from .features import Feature
from .. import (weapons, armor)


class UnarmoredDefense(Feature):
    """Beginning at 1st level, while you are wearing no armor and not wearing a
    shield, your AC equals 10 + your Dexterity modifier + your Wisdom modifier.

    """
    name = "Unarmored Defense"
    source = 'Monk'

    def AC_func(self, char, **kwargs):
        no_armor = ((char.armor is None)
                    or (isinstance(char.armor, armor.NoAmor)))
        no_shield = ((char.shield is None)
                     or (isinstance(char.shield, armor.NoShield)))
        if no_armor and no_shield:
            return 10 + char.dexterity.modifier + char.wisdom.modifier
        else:
            return -100


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
    die_by_level = {1: 'd4', 2: 'd4', 3: 'd4', 4: 'd4',
                    5: 'd6', 6: 'd6', 7: 'd6', 8: 'd6',
                    9: 'd6', 10: 'd6', 11: 'd8', 12: 'd8',
                    13: 'd8', 14: 'd8', 15: 'd8', 16: 'd8',
                    17: 'd10', 18: 'd10', 19: 'd10', 20: 'd10'}
    level = 1
    
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
        new_die = int(self.die_by_level[self.level].strip('d'))
        if new_die > int(weapon.base_damage.split('d')[-1]):
            weapon.base_damage = '1d' + str(new_die)
        weapon.is_finesse = True
        return weapon


