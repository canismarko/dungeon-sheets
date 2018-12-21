from .. import (weapons, features)
from .classes import CharClass, SubClass
from collections import defaultdict


# PHB
class Thief(SubClass):
    name = "Thief"
    features_by_level = defaultdict(list)


class Assassin(SubClass):
    name = "Assassin"
    features_by_level = defaultdict(list)


class ArcaneTrickster(SubClass):
    name = "Arcane Trickster"
    features_by_level = defaultdict(list)
    spellcasting_ability = 'intelligence'
    multiclass_spellslots_by_level = {
        # char_lvl: (cantrips, 1st, 2nd, 3rd, ...)
        1:  (0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
        2:  (0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
        3:  (3, 2, 0, 0, 0, 0, 0, 0, 0, 0),
        4:  (3, 3, 0, 0, 0, 0, 0, 0, 0, 0),
        5:  (3, 3, 0, 0, 0, 0, 0, 0, 0, 0),
        6:  (3, 3, 0, 0, 0, 0, 0, 0, 0, 0),
        7:  (3, 4, 2, 0, 0, 0, 0, 0, 0, 0),
        8:  (3, 4, 2, 0, 0, 0, 0, 0, 0, 0),
        9:  (3, 4, 2, 0, 0, 0, 0, 0, 0, 0),
        10: (4, 4, 3, 0, 0, 0, 0, 0, 0, 0),
        11: (4, 4, 3, 0, 0, 0, 0, 0, 0, 0),
        12: (4, 4, 3, 0, 0, 0, 0, 0, 0, 0),
        13: (4, 4, 3, 2, 0, 0, 0, 0, 0, 0),
        14: (4, 4, 3, 2, 0, 0, 0, 0, 0, 0),
        15: (4, 4, 3, 2, 0, 0, 0, 0, 0, 0),
        16: (4, 4, 3, 3, 0, 0, 0, 0, 0, 0),
        17: (4, 4, 3, 3, 0, 0, 0, 0, 0, 0),
        18: (4, 4, 3, 3, 0, 0, 0, 0, 0, 0),
        19: (4, 4, 3, 3, 1, 0, 0, 0, 0, 0),
        20: (4, 4, 3, 3, 1, 0, 0, 0, 0, 0),
    }


# XGTE
class Inquisitive(SubClass):
    name = "Inquisitive"
    features_by_level = defaultdict(list)


class Mastermind(SubClass):
    name = "Mastermind"
    features_by_level = defaultdict(list)


class Swashbuckler(SubClass):
    name = "Swashbuckler"
    features_by_level = defaultdict(list)


class Rogue(CharClass):
    class_name = 'Rogue'
    hit_dice_faces = 8
    saving_throw_proficiencies = ('dexterity', 'intelligence')
    _proficiencies_text = (
        'light armor', 'simple weapons', 'hand crossbows', 'longswords',
        'rapiers', 'shortswords', "thieves' tools")
    weapon_proficiencies = weapons.simple_weapons + (
        weapons.HandCrossbow, weapons.Longsword, weapons.Rapier,
        weapons.Shortsword)
    class_skill_choices = ('Acrobatics', 'Athletics', 'Deception',
                           'Insight', 'Intimidation', 'Investigation',
                           'Perception', 'Performance', 'Persuasion',
                           'Sleight of Hand', 'Stealth')
    features_by_level = defaultdict(list)
    subclasses_available = (Thief, Assassin, ArcaneTrickster,
                            Inquisitive, Mastermind, Swashbuckler)
