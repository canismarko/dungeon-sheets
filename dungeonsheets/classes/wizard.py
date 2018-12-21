from .. import (weapons, features)
from .classes import CharClass, SubClass
from collections import defaultdict


# PHB
class Abjuration(SubClass):
    name = "School of Abjuration"
    features_by_level = defaultdict(list)


class Conjuration(SubClass):
    name = "School of Conjuration"
    features_by_level = defaultdict(list)


class Divination(SubClass):
    name = "School of Divination"
    features_by_level = defaultdict(list)


class Enchantment(SubClass):
    name = "School of Enchantment"
    features_by_level = defaultdict(list)


class Evocation(SubClass):
    name = "School of Evocation"
    features_by_level = defaultdict(list)


class Illusion(SubClass):
    name = "School of Illusion"
    features_by_level = defaultdict(list)


class Necromancy(SubClass):
    name = "School of Necromancy"
    features_by_level = defaultdict(list)


class Transmutation(SubClass):
    name = "School of Transmutation"
    features_by_level = defaultdict(list)


# SCAG
class Bladeslinging(SubClass):
    name = "School of Bladeslinging"
    features_by_level = defaultdict(list)


# XGTE
class WarMagic(SubClass):
    name = "School of War Magic"
    features_by_level = defaultdict(list)


class Wizard(CharClass):
    class_name = 'Wizard'
    hit_dice_faces = 6
    saving_throw_proficiencies = ('intelligence', 'wisdom')
    _proficiencies_text = ('daggers', 'darts', 'slings',
                           'quarterstaffs', 'light crossbows')
    weapon_proficiencies = (weapons.Dagger, weapons.Dart,
                            weapons.Sling, weapons.Quarterstaff,
                            weapons.LightCrossbow)
    class_skill_choices = ('Arcana', 'History', 'Investigation',
                           'Medicine', 'Religion')
    features_by_level = defaultdict(list)
    subclasses_available = (Abjuration, Conjuration, Divination, Enchantment,
                            Evocation, Illusion, Necromancy, Transmutation,
                            Bladeslinging, WarMagic)
    spellcasting_ability = 'intelligence'
    spell_slots_by_level = {
        # char_lvl: (cantrips, 1st, 2nd, 3rd, ...)
        1:  (3, 2, 0, 0, 0, 0, 0, 0, 0, 0),
        2:  (3, 3, 0, 0, 0, 0, 0, 0, 0, 0),
        3:  (3, 4, 2, 0, 0, 0, 0, 0, 0, 0),
        4:  (4, 4, 3, 0, 0, 0, 0, 0, 0, 0),
        5:  (4, 4, 3, 2, 0, 0, 0, 0, 0, 0),
        6:  (4, 4, 3, 3, 0, 0, 0, 0, 0, 0),
        7:  (4, 4, 3, 3, 1, 0, 0, 0, 0, 0),
        8:  (4, 4, 3, 3, 2, 0, 0, 0, 0, 0),
        9:  (4, 4, 3, 3, 3, 1, 0, 0, 0, 0),
        10: (5, 4, 3, 3, 3, 2, 0, 0, 0, 0),
        11: (5, 4, 3, 3, 3, 2, 1, 0, 0, 0),
        12: (5, 4, 3, 3, 3, 2, 1, 0, 0, 0),
        13: (5, 4, 3, 3, 3, 2, 1, 1, 0, 0),
        14: (5, 4, 3, 3, 3, 2, 1, 1, 0, 0),
        15: (5, 4, 3, 3, 3, 2, 1, 1, 1, 0),
        16: (5, 4, 3, 3, 3, 2, 1, 1, 1, 0),
        17: (5, 4, 3, 3, 3, 2, 1, 1, 1, 1),
        18: (5, 4, 3, 3, 3, 3, 1, 1, 1, 1),
        19: (5, 4, 3, 3, 3, 3, 2, 1, 1, 1),
        20: (5, 4, 3, 3, 3, 3, 2, 2, 1, 1),
    }

    
