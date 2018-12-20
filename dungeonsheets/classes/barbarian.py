from .. import (weapons)
from .. import features as feats
from .classes import CharClass


class Barbarian(CharClass):
    class_name = 'Barbarian'
    hit_dice_faces = 12
    saving_throw_proficiencies = ('strength', 'constitution')
    _proficiencies_text = ('light armor', 'medium armor', 'shields',
                           'simple weapons', 'martial weapons')
    weapon_proficiencies = (weapons.simple_weapons + weapons.martial_weapons)
    class_skill_choices = ('Animal Handling', 'Athletics',
                           'Intimidation', 'Nature', 'Perception', 'Survival')
    
