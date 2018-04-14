import math
from collections import namedtuple


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
    if modifier > 0:
        mod_str = '+' + str(modifier)
    else:
        mod_str = str(modifier)
    return mod_str


AbilityScore = namedtuple('AbilityScore', ('value', 'modifier', 'saving_throw'))


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
        if self.ability_name is not None:
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
        self.skill_name = name
        self.character = character
    
    def __get__(self, character, owner):
        ability = getattr(character, self.ability_name)
        modifier = ability.modifier
        # Check for proficiency
        is_proficient = self.skill_name in character.skill_proficiencies
        if is_proficient:
            modifier += character.proficiency_bonus
        return modifier
