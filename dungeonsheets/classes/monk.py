__all__ = ('Monk')

from .. import (features, weapons)
from .classes import CharClass
from collections import defaultdict


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
    subclasses_available = ('SunSoul', 'OpenHand')
    features_by_level = defaultdict(list)
    features_by_level[1] = [features.UnarmoredDefense,
                            features.MartialArts]

    def __init__(self, level, subclass=None, **params):
        super().__init__(level, subclass=subclass, **params)
        for f in self.features_by_level[1]:
            if isinstance(f, features.MartialArts):
                f.level = self.class_level
        if subclass == 'sunsoul':
            self.subclass = SunSoul(level=self.class_level)
        else:
            self.subclass = None
        if self.subclass is not None:
            self._proficiencies_text += self.subclass._proficiencies_text
            self.weapon_proficiences += self.subclass.weapon_proficiencies

            
class SunSoul:
    class_features_by_level = defaultdict(list)
    weapon_proficiencies = ()
    _profiencies_text = ()

    def __init__(self, level):
        self.class_level = level
