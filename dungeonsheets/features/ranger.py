from .features import Feature
from .. import (weapons, armor)


def select_ranger_fighting_style(feature_choices=[]):
        lower_choices = [fc for fc in map(str.lower, feature_choices)]
        if 'archery' in lower_choices:
            return Archery()
        elif 'defense' in lower_choices:
            return Defense()
        elif 'dueling' in lower_choices:
            return Dueling()
        elif 'two-weapon fighting' in lower_choices:
            return TwoWeaponFighting()
        else:
            return RangerFightingStyle()
    

class RangerFightingStyle(Feature):
    """
    Select a Fighting Style by choosing in feature_choices:

    archery
 
    defense

    dueling

    two-weapon fighting
    """
    name = "Fighting Style (Select One)"
    source = "Ranger"
            
        
class Archery(Feature):
    """
    You gain a +2 bonus to attack rolls you make
    with ranged weapons.
    """
    name = "Fighting Style (Archery)"
    source = "Ranger"

    def weapon_func(self, weapon: weapons.Weapon, **kwargs):
        """
        +2 attack roll bonus if weapon is ranged
        """
        if weapon.is_ranged:
            weapon.attack_bonus += 2
        return weapon

    
class Defense(Feature):
    """
    While you are wearing armor, you gain a +1 bonus to AC.
    """
    name = "Fighting Style (Defense)"
    source = "Ranger"

    def AC_func(self, char, **kwargs):
        """
        Apply a +1 bonus if wearing armor
        """
        if (char.armor is None) or (isinstance(char.armor, armor.NoArmor)):
            return char.default_AC
        else:
            return char.default_AC + 1

        
class Dueling(Feature):
    """When you are wielding a melee weapon in one hand and no other weapons, you
    gain a +2 bonus to damage rolls with that weapon.

    """
    name = "Fighting Style (Dueling)"
    source = "Ranger"
    needs_implementation = True

    
class TwoWeaponFighting(Feature):
    """When you engage in two-weapon fighting, you can add your ability modifier
    to the damage of the second attack.

    """
    name = "Fighting Style (Two-Weapon Fighting)"
    source = "Ranger"
    needs_implementation = True
