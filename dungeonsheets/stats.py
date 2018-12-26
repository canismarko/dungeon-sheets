import math
from collections import namedtuple
from .armor import NoArmor, NoShield, HeavyArmor
from .features import (UnarmoredDefenseMonk, UnarmoredDefenseBarbarian,
                       DraconicResilience, Defense, FastMovement,
                       UnarmoredMovement, GiftOfTheDepths, RemarkableAthelete)
from math import ceil


def findattr(obj, name):
    """Similar to builtin getattr(obj, name) but more forgiving to
    whitespace and capitalization.
    
    """
    # Come up with several options
    py_name = name.replace('-', '_').replace(' ', '_').replace("'", "")
    camel_case = "".join([s.capitalize() for s in py_name.split('_')])
    if hasattr(obj, py_name):
        # Direct lookup
        attr = getattr(obj, py_name)
    elif hasattr(obj, camel_case):
        # CamelCase lookup
        attr = getattr(obj, camel_case)
    else:
        raise AttributeError(f'{obj} has no attribute {name}')
    return attr


def mod_str(modifier):
    """Converts a modifier to a string, eg 2 -> '+2'."""
    return '{:+d}'.format(modifier)
    if modifier == 0:
        return str(modifier)
    else:
        return '{:+}'.format(modifier)


AbilityScore = namedtuple('AbilityScore',
                          ('value', 'modifier', 'saving_throw'))


class Ability():
    ability_name = None
    
    def __init__(self, default_value=10):
        self.default_value = default_value
    
    def __set_name__(self, character, name):
        self.ability_name = name
    
    def _check_dict(self, obj):
        if not hasattr(obj, '_ability_scores'):
            # No ability score dictionary exists
            obj._ability_scores = {
                self.ability_name: self.default_value
            }
        elif self.ability_name not in obj._ability_scores.keys():
            # ability score dictionary exists but doesn't have this ability
            obj._ability_scores[self.ability_name] = self.default_value
    
    def __get__(self, character, Character):
        self._check_dict(character)
        score = character._ability_scores[self.ability_name]
        modifier = math.floor((score - 10) / 2)
        # Check for proficiency
        saving_throw = modifier
        if self.ability_name is not None and hasattr(character, 'saving_throw_proficiencies'):
            is_proficient = (self.ability_name in character.saving_throw_proficiencies)
            if is_proficient:
                saving_throw += character.proficiency_bonus
        # Create the named tuple
        value = AbilityScore(modifier=modifier, value=score, saving_throw=saving_throw)
        return value
    
    def __set__(self, character, val):
        self._check_dict(character)
        character._ability_scores[self.ability_name] = val
        self.value = val


class Skill():
    """An ability-based skill, such as athletics."""
    
    def __init__(self, ability):
        self.ability_name = ability
    
    def __set_name__(self, character, name):
        self.skill_name = name.lower().replace('_', ' ')
        self.character = character
    
    def __get__(self, character, owner):
        ability = getattr(character, self.ability_name)
        modifier = ability.modifier
        # Check for proficiency
        is_proficient = self.skill_name in character.skill_proficiencies
        if is_proficient:
            modifier += character.proficiency_bonus
        elif any([isinstance(f, RemarkableAthelete) for f in character.features]):
            if self.ability_name.lower() in ('strength',
                                             'dexterity', 'constitution'):
                modifier += ceil(character.proficiencies_bonus / 2.)
        # Check for expertise
        is_expert = self.skill_name in character.skill_expertise
        if is_expert:
            modifier += character.proficiency_bonus
        return modifier


class ArmorClass():
    """
    The Armor Class of a character
    """

    def __get__(self, char, Character):
        armor = char.armor or NoArmor()
        ac = armor.base_armor_class
        shield = char.shield or NoShield()
        ac += shield.base_armor_class
        # calculate and apply modifiers
        if armor.dexterity_mod_max is None:
            ac += char.dexterity.modifier
        else:
            ac += min(char.dexterity.modifier, armor.dexterity_mod_max)
        # Compute feature-specific additions
        if any([isinstance(f, UnarmoredDefenseMonk) for f in char.features]):
            if (isinstance(armor, NoArmor) and isinstance(shield, NoShield)):
                ac += char.wisdom.modifier
        if any([isinstance(f, UnarmoredDefenseBarbarian) for f in char.features]):
            if isinstance(armor, NoArmor):
                ac += char.constitution.modifier
        if any([isinstance(f, DraconicResilience) for f in char.features]):
            if isinstance(armor, NoArmor):
                ac += 3
        if any([isinstance(f, Defense) for f in char.features]):
            if not isinstance(armor, NoArmor):
                ac += 1
        # Check if any magic items add to AC
        for mitem in char.magic_items:
            if hasattr(mitem, 'ac_bonus'):
                ac += mitem.ac_bonus
        return ac
        

class Speed():
    """
    The speed of a character
    """

    def __get__(self, char, Character):
        speed = char.race.speed
        other_speed = ''
        if isinstance(speed, str):
            other_speed = speed[2:]
            speed = int(speed[:2])  # ignore other speeds, like fly
        if any([isinstance(f, FastMovement) for f in char.features]):
            if not isinstance(char.armor, HeavyArmor):
                speed += 10
        if isinstance(char.armor, NoArmor) or (char.armor is None):
            for f in char.features:
                if isinstance(f, UnarmoredMovement):
                    speed += f.speed_bonus
        if any([isinstance(f, GiftOfTheDepths) for f in char.features]):
            if 'swim' not in other_speed:
                other_speed += ' ({:d} swim)'.format(speed)
        return '{:d}{:s}'.format(speed, other_speed)
