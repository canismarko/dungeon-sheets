import math


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



class Ability():
    value = 10
    ability_name = None
    character = None
    
    def __init__(self, value=10):
        self.value = value
    
    def __set_name__(self, character, name):
        self.ability_name = name
    
    def __get__(self, character, Character):
        self.character = character
        return self
    
    def __set__(self, obj, val):
        self.value = val
    
    @property
    def modifier(self):
        return math.floor((self.value - 10) / 2)
    
    @property
    def saving_throw(self):
        modifier = self.modifier
        # Check for proficiency
        if self.ability_name is not None:
            is_proficient = (self.ability_name in self.character.saving_throw_proficiencies)
            if is_proficient:
                modifier += self.character.proficiency_bonus
        # Return the value
        return modifier


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
