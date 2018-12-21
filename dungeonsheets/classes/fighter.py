from .. import (weapons, features)
from .classes import CharClass, SubClass
from collections import defaultdict


# PHB
class Champion(SubClass):
    name = "Champion"
    features_by_level = defaultdict(list)
    

class BattleMaster(SubClass):
    name = "Battle Master"
    features_by_level = defaultdict(list)
    

class EldritchKnight(SubClass):
    name = "Eldritch Knight"
    features_by_level = defaultdict(list)
    spellcasting_ability = 'intelligence'
    multiclass_spellslots_by_level = {
        # char_lvl: (cantrips, 1st, 2nd, 3rd, ...)
        1:  (0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
        2:  (0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
        3:  (2, 2, 0, 0, 0, 0, 0, 0, 0, 0),
        4:  (2, 3, 0, 0, 0, 0, 0, 0, 0, 0),
        5:  (2, 3, 0, 0, 0, 0, 0, 0, 0, 0),
        6:  (2, 3, 0, 0, 0, 0, 0, 0, 0, 0),
        7:  (2, 4, 2, 0, 0, 0, 0, 0, 0, 0),
        8:  (2, 4, 2, 0, 0, 0, 0, 0, 0, 0),
        9:  (2, 4, 2, 0, 0, 0, 0, 0, 0, 0),
        10: (3, 4, 3, 0, 0, 0, 0, 0, 0, 0),
        11: (3, 4, 3, 0, 0, 0, 0, 0, 0, 0),
        12: (3, 4, 3, 0, 0, 0, 0, 0, 0, 0),
        13: (3, 4, 3, 2, 0, 0, 0, 0, 0, 0),
        14: (3, 4, 3, 2, 0, 0, 0, 0, 0, 0),
        15: (3, 4, 3, 2, 0, 0, 0, 0, 0, 0),
        16: (3, 4, 3, 3, 0, 0, 0, 0, 0, 0),
        17: (3, 4, 3, 3, 0, 0, 0, 0, 0, 0),
        18: (3, 4, 3, 3, 0, 0, 0, 0, 0, 0),
        19: (3, 4, 3, 3, 1, 0, 0, 0, 0, 0),
        20: (3, 4, 3, 3, 1, 0, 0, 0, 0, 0),
    }
    

# SCAG
class PurpleDragonKnight(SubClass):
    name = "Purple Dragon Knight"
    features_by_level = defaultdict(list)
    

# XGTE
class ArcaneArcher(SubClass):
    name = "Arcane Archer"
    features_by_level = defaultdict(list)
    

class Cavalier(SubClass):
    name = "Cavalier"
    features_by_level = defaultdict(list)
    

class Samurai(SubClass):
    name = "Samurai"
    features_by_level = defaultdict(list)
    

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
    features_by_level = defaultdict(list)
    subclasses_available = (Champion, BattleMaster, EldritchKnight,
                            PurpleDragonKnight, ArcaneArcher, Cavalier,
                            Samurai)
