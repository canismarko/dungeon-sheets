from .. import (weapons)
from .. import features as feats
from .classes import CharClass


class Fighter(CharClass):
    class_name = 'Fighter'
    hit_dice_faces = 10
    saving_throw_proficiencies = ('strength', 'constitution')
    _proficiencies_text = ('All armor', 'shields', 'simple weapons',
                           'martial weapons')
    weapon_proficiencies = weapons.simple_weapons + weapons.martial_weapons
    multiclass_weapon_proficiencies = weapon_proficiencies
    _multiclass_proficiencies_text = ('light armor', 'medium armor',
                                      'shields', 'simple weapons',
                                      'martial weapons')
    class_skill_choices = ('Acrobatics', 'Animal Handling',
                           'Athletics', 'History', 'Insight', 'Intimidation',
                           'Perception', 'Survival')

