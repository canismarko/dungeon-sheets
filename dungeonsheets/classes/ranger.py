__all__ = ('Ranger', 'RevisedRanger')

from .. import (weapons, features)
from .classes import CharClass, SubClass
from collections import defaultdict


# PHB
class Hunter(SubClass):
    name = "Hunter"
    features_by_level = defaultdict(list)


class BeastMaster(SubClass):
    name = "Beast Master"
    features_by_level = defaultdict(list)


# XGTE
class GloomStalker(SubClass):
    name = "Gloom Stalker"
    features_by_level = defaultdict(list)


class HorizonWalker(SubClass):
    name = "Horizon Walker"
    features_by_level = defaultdict(list)


class MonsterSlayer(SubClass):
    name = "Monster Slayer"
    features_by_level = defaultdict(list)


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
    features_by_level = defaultdict(list)
    subclasses_available = (Hunter, BeastMaster, GloomStalker,
                            HorizonWalker, MonsterSlayer)
    spellcasting_ability = 'wisdom'
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

    
# Revised Ranger
class BeastConclave(SubClass):
    name = "Beast Conclave"
    features_by_level = defaultdict(list)
    

class HunterConclave(SubClass):
    name = "Hunter Conclave"
    features_by_level = defaultdict(list)
    

class DeepStalkerConclave(SubClass):
    name = "Deep Stalker Conclave"
    features_by_level = defaultdict(list)
    

class RevisedRanger(Ranger):
    class_name = 'Revised Ranger'
    features_by_level = defaultdict(list)
    subclasses_available = (BeastConclave, HunterConclave, DeepStalkerConclave)
    
