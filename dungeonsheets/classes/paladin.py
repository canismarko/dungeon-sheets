from .. import (weapons, features)
from .classes import CharClass, SubClass
from collections import defaultdict


class OathOfDevotion(SubClass):
    name = "Oath of Devotion"
    features_by_level = defaultdict(list)
    
    
class OathOfAncients(SubClass):
    name = "Oath of The Ancients"
    features_by_level = defaultdict(list)
    
    
class OathOfVengance(SubClass):
    name = "Oath of Vengance"
    features_by_level = defaultdict(list)
    
    
class OathOfCrown(SubClass):
    name = "Oath of The Crown"
    features_by_level = defaultdict(list)
    
    
class OathOfConquest(SubClass):
    name = "Oath of Conquest"
    features_by_level = defaultdict(list)
    
    
class OathOfRedemption(SubClass):
    name = "Oath of Redemption"
    features_by_level = defaultdict(list)
    
    
class Paladin(CharClass):
    class_name = 'Paladin'
    hit_dice_faces = 10
    saving_throw_proficiencies = ('wisdom', 'charisma')
    _proficiencies_text = ('All armor', 'shields', 'simple weapons',
                           'martial weapons')
    weapon_proficiencies = weapons.simple_weapons + weapons.martial_weapons
    class_skill_choices = ("Athletics", 'Insight', 'Intimidation',
                           'Medicine', 'Persuasion', 'Religion')
    features_by_level = defaultdict(list)
    subclasses_available = (OathOfDevotion, OathOfAncients, OathOfVengance,
                            OathOfCrown, OathOfConquest, OathOfRedemption)
    spellcasting_ability = 'charisma'
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
