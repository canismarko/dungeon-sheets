from .. import (weapons, features)
from .classes import CharClass, SubClass
from collections import defaultdict


class KnowledgeDomain(SubClass):
    name = "Knowledge Domain"
    features_by_level = defaultdict(list)


class LifeDomain(SubClass):
    name = "Life Domain"
    features_by_level = defaultdict(list)


class LightDomain(SubClass):
    name = "Light Domain"
    features_by_level = defaultdict(list)


class NatureDomain(SubClass):
    name = "Nature Domain"
    features_by_level = defaultdict(list)


class TempestDomain(SubClass):
    name = "Tempest Domain"
    features_by_level = defaultdict(list)


class TrickeryDomain(SubClass):
    name = "Trickery Domain"
    features_by_level = defaultdict(list)


class WarDomain(SubClass):
    name = "War Domain"
    features_by_level = defaultdict(list)


# SCAG
class ArcanaDomain(SubClass):
    name = "Arcana Domain"
    features_by_level = defaultdict(list)


# XGTE
class ForgeDomain(SubClass):
    name = "Forge Domain"
    features_by_level = defaultdict(list)


class GraveDomain(SubClass):
    name = "Grave Domain"
    features_by_level = defaultdict(list)


class Cleric(CharClass):
    class_name = 'Cleric'
    hit_dice_faces = 8
    saving_throw_proficiencies = ('wisdom', 'charisma')
    _proficiencies_text = ('light armor', 'medium armor', 'shields',
                           'all simple weapons')
    weapon_proficiencies = weapons.simple_weapons
    class_skill_choices = ('History', 'Insight', 'Medicine',
                           'Persuasion', 'Religion')
    features_by_level = defaultdict(list)
    subclasses_available = (KnowledgeDomain, LifeDomain, LightDomain,
                            NatureDomain, TempestDomain, TrickeryDomain,
                            WarDomain, ArcanaDomain, ForgeDomain,
                            GraveDomain)
    spellcasting_ability = 'wisdom'
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

