__all__ = ('Monk')

from .. import (features, weapons)
from .classes import CharClass, SubClass
from collections import defaultdict


class OpenHandWay(SubClass):
    name = "Way of the Open Hand"
    features_by_level = defaultdict(list)


class ShadowWay(SubClass):
    name = "Way of Shadow"
    features_by_level = defaultdict(list)
    

class FourElementsWay(SubClass):
    name = "Way of the Four Elements"
    features_by_level = defaultdict(list)

    
class SunSoulWay(SubClass):
    name = "Way of the Sun Soul"
    features_by_level = defaultdict(list)


class LongDeathWay(SubClass):
    name = "Way of the Long Death"
    features_by_level = defaultdict(list)


class DrunkenMasterWay(SubClass):
    name = "Way of the Drunken Master"
    features_by_level = defaultdict(list)


class KenseiWay(SubClass):
    name = "Way of the Kensei"
    features_by_level = defaultdict(list)


class Monk(CharClass):
    class_name = 'Monk'
    hit_dice_faces = 8
    saving_throw_proficiencies = ('strength', 'dexterity')
    _proficiencies_text = (
        'simple weapons', 'shortswords', 'unarmed',
        "one type of artisan's tools or one musical instrument")
    weapon_proficiencies = (weapons.Shortsword, weapons.Unarmed) + weapons.simple_weapons
    class_skill_choices = ('Acrobatics', 'Athletics', 'History', 'Insight',
                           'Religion', 'Stealth')
    subclasses_available = (OpenHandWay, ShadowWay,
                            FourElementsWay, SunSoulWay,
                            LongDeathWay, DrunkenMasterWay,
                            KenseiWay)
    features_by_level = defaultdict(list)
    features_by_level[1] = [features.UnarmoredDefense,
                            features.MartialArts]

    def __init__(self, level, subclass=None, **params):
        super().__init__(level, subclass=subclass, **params)
        for f in self.features_by_level[1]:
            if isinstance(f, features.MartialArts):
                f.level = self.class_level
