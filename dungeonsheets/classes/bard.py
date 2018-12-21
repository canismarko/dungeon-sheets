from .. import (weapons, features)
from .classes import CharClass, SubClass
from collections import defaultdict


# PHB
class CollegeOfLore(SubClass):
    name = "College of Lore"
    class_features_by_level = defaultdict(list)
    

class CollegeOfValor(SubClass):
    name = "College of Valor"
    class_features_by_level = defaultdict(list)


# XGTE
class CollegeOfGlamour(SubClass):
    name = "College of Glamour"
    class_features_by_level = defaultdict(list)


class CollegeOfSwords(SubClass):
    name = "College of Swords"
    class_features_by_level = defaultdict(list)


class CollegeOfWhispers(SubClass):
    name = "College of Whispers"
    class_features_by_level = defaultdict(list)


class Bard(CharClass):
    class_name = 'Bard'
    hit_dice_faces = 8
    saving_throw_proficiencies = ('dexterity', 'charisma')
    _proficiencies_text = (
        'Light armor', 'simple weapons', 'hand crossbows', 'longswords',
        'rapiers', 'shortswords', 'three musical instruments of your choice')
    weapon_proficiencies = ((weapons.HandCrossbow, weapons.Longsword,
                            weapons.Rapier, weapons.Shortsword) +
                            weapons.simple_weapons)
    class_skill_choices = ('Acrobatics', 'Animal Handling', 'Arcana',
                           'Athletics', 'Deception', 'History', 'Insight',
                           'Intimidation', 'Investigation', 'Medicine',
                           'Nature', 'Perception', 'Performance', 'Persuasion',
                           'Religion', 'Sleight of Hand', 'Stealth',
                           'Survival')
    num_skill_choices = 3
    features_by_level = defaultdict(list)
    subclasses_available = (CollegeOfLore, CollegeOfValor, CollegeOfGlamour,
                            CollegeOfSwords, CollegeOfWhispers)
    spellcasting_ability = 'charisma'
    spell_slots_by_level = {
        # char_lvl: (cantrips, 1st, 2nd, 3rd, ...)
        1:  (2, 2, 0, 0, 0, 0, 0, 0, 0, 0),
        2:  (2, 3, 0, 0, 0, 0, 0, 0, 0, 0),
        3:  (2, 4, 2, 0, 0, 0, 0, 0, 0, 0),
        4:  (3, 4, 3, 0, 0, 0, 0, 0, 0, 0),
        5:  (3, 4, 3, 2, 0, 0, 0, 0, 0, 0),
        6:  (3, 4, 3, 3, 0, 0, 0, 0, 0, 0),
        7:  (3, 4, 3, 3, 1, 0, 0, 0, 0, 0),
        8:  (3, 4, 3, 3, 2, 0, 0, 0, 0, 0),
        9:  (4, 4, 3, 3, 3, 1, 0, 0, 0, 0),
        10: (4, 4, 3, 3, 3, 2, 0, 0, 0, 0),
        11: (4, 4, 3, 3, 3, 2, 1, 0, 0, 0),
        12: (4, 4, 3, 3, 3, 2, 1, 0, 0, 0),
        13: (4, 4, 3, 3, 3, 2, 1, 1, 0, 0),
        14: (4, 4, 3, 3, 3, 2, 1, 1, 0, 0),
        15: (4, 4, 3, 3, 3, 2, 1, 1, 1, 0),
        16: (4, 4, 3, 3, 3, 2, 1, 1, 1, 0),
        17: (4, 4, 3, 3, 3, 2, 1, 1, 1, 1),
        18: (4, 4, 3, 3, 3, 3, 1, 1, 1, 1),
        19: (4, 4, 3, 3, 3, 3, 2, 1, 1, 1),
        20: (4, 4, 3, 3, 3, 3, 2, 2, 1, 1),
    }
