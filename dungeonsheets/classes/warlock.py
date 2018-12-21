from .. import (weapons, features)
from .classes import CharClass, SubClass
from collections import defaultdict


# PHB
class Archfey(SubClass):
    name = "The Archfey Patron"
    features_by_level = defaultdict(list)


class Fiend(SubClass):
    name = "The Fiend Patron"
    features_by_level = defaultdict(list)


class GreatOldOne(SubClass):
    name = "The Great Old One Patron"
    features_by_level = defaultdict(list)


# SCAG
class Undying(SubClass):
    name = "The Undying Patron"
    features_by_level = defaultdict(list)


# XGTE
class Celestial(SubClass):
    name = "The Celestial Patron"
    features_by_level = defaultdict(list)


class Hexblade(SubClass):
    name = "Hexblade Patron"
    features_by_level = defaultdict(list)


class Warlock(CharClass):
    class_name = 'Warlock'
    hit_dice_faces = 8
    saving_throw_proficiencies = ('wisdom', 'charisma')
    _proficiencies_text = ("light Armor", "simple weapons")
    class_skill_choices = ('Arcana', 'Deception', 'History',
                           'Intimidation', 'Investigation', 'Nature',
                           'Religion')
    weapon_proficiencies = weapons.simple_weapons
    features_by_level = defaultdict(list)
    subclasses_available = (Archfey, Fiend, GreatOldOne, Undying, Celestial,
                            Hexblade)
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
