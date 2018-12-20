__all__ = ('Ranger', 'Revisedranger')

from .. import (weapons, features)
from .classes import CharClass
from collections import defaultdict


class Ranger(CharClass):
    class_name = 'Ranger'
    hit_dice_faces = 10
    saving_throw_proficiencies = ('strength', 'dexterity')
    _proficiencies_text = ("light armor", "medium armor", "shields",
                           "simple weapons", "martial weapons")
    weapon_proficiencies = weapons.simple_weapons + weapons.martial_weapons
    class_skill_choices = ('Animal Handling', 'Athletics', 'Insight',
                           'Investigation', 'Nature', 'Perception', 'Stealth',
                           'Survival')
    num_skill_choices = 3
    spellcasting_ability = 'wisdom'
    features_by_level = defaultdict(list)
    spell_slots_by_level = {
        # char_lvl: (cantrips, 1st, 2nd, 3rd, ...)
        1:  (0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
        2:  (0, 2, 0, 0, 0, 0, 0, 0, 0, 0),
        3:  (0, 3, 0, 0, 0, 0, 0, 0, 0, 0),
        4:  (0, 3, 0, 0, 0, 0, 0, 0, 0, 0),
        5:  (0, 4, 2, 0, 0, 0, 0, 0, 0, 0),
        6:  (0, 4, 2, 0, 0, 0, 0, 0, 0, 0),
        7:  (0, 4, 3, 0, 0, 0, 0, 0, 0, 0),
        8:  (0, 4, 3, 0, 0, 0, 0, 0, 0, 0),
        9:  (0, 4, 3, 2, 0, 0, 0, 0, 0, 0),
        10: (0, 4, 3, 2, 0, 0, 0, 0, 0, 0),
        11: (0, 4, 3, 3, 0, 0, 0, 0, 0, 0),
        12: (0, 4, 3, 3, 0, 0, 0, 0, 0, 0),
        13: (0, 4, 3, 3, 1, 0, 0, 0, 0, 0),
        14: (0, 4, 3, 3, 1, 0, 0, 0, 0, 0),
        15: (0, 4, 3, 3, 2, 0, 0, 0, 0, 0),
        16: (0, 4, 3, 3, 2, 0, 0, 0, 0, 0),
        17: (0, 4, 3, 3, 3, 1, 0, 0, 0, 0),
        18: (0, 4, 3, 3, 3, 1, 0, 0, 0, 0),
        19: (0, 4, 3, 3, 3, 2, 0, 0, 0, 0),
        20: (0, 4, 3, 3, 3, 2, 0, 0, 0, 0),
    }

    def __init__(self, level, subclass=None, **params):
        super().__init__(level, subclass=subclass, **params)
        fighting_style = features.select_ranger_fighting_style(
            feature_choices=params.get('feature_choices', []))
        self.features_by_level[2].append(fighting_style)

    
# Custom Classes
class Revisedranger(Ranger):
    class_name = 'Revised Ranger'
