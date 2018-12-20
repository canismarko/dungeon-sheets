from .. import (weapons)
from .. import features as feats
from .classes import CharClass


class Warlock(CharClass):
    class_name = 'Warlock'
    hit_dice_faces = 8
    saving_throw_proficiencies = ('wisdom', 'charisma')
    _proficiencies_text = ("light Armor", "simple weapons")
    class_skill_choices = ('Arcana', 'Deception', 'History',
                           'Intimidation', 'Investigation', 'Nature',
                           'Religion')
    weapon_proficiencies = weapons.simple_weapons
    spellcasting_ability = 'charisma'
    spell_slots_by_level = {
        1:  (2, 1, 0, 0, 0, 0, 0, 0, 0, 0),
        2:  (2, 2, 0, 0, 0, 0, 0, 0, 0, 0),
        3:  (2, 0, 2, 0, 0, 0, 0, 0, 0, 0),
        4:  (3, 0, 2, 0, 0, 0, 0, 0, 0, 0),
        5:  (3, 0, 0, 3, 0, 0, 0, 0, 0, 0),
        6:  (3, 0, 0, 3, 0, 0, 0, 0, 0, 0),
        7:  (3, 0, 0, 0, 2, 0, 0, 0, 0, 0),
        8:  (3, 0, 0, 0, 2, 0, 0, 0, 0, 0),
        9:  (3, 0, 0, 0, 0, 2, 0, 0, 0, 0),
        10: (4, 0, 0, 0, 0, 2, 0, 0, 0, 0),
        11: (4, 0, 0, 0, 0, 3, 0, 0, 0, 0),
        12: (4, 0, 0, 0, 0, 3, 0, 0, 0, 0),
        13: (4, 0, 0, 0, 0, 3, 0, 0, 0, 0),
        14: (4, 0, 0, 0, 0, 3, 0, 0, 0, 0),
        15: (4, 0, 0, 0, 0, 3, 0, 0, 0, 0),
        16: (4, 0, 0, 0, 0, 3, 0, 0, 0, 0),
        17: (4, 0, 0, 0, 0, 4, 0, 0, 0, 0),
        18: (4, 0, 0, 0, 0, 4, 0, 0, 0, 0),
        19: (4, 0, 0, 0, 0, 4, 0, 0, 0, 0),
        20: (4, 0, 0, 0, 0, 4, 0, 0, 0, 0),
    }
