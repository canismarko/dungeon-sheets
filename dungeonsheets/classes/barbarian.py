from .. import (features, weapons)
from .classes import (CharClass, SubClass)
from collections import defaultdict


# PHB
class BerserkerPath(SubClass):
    name = "Path of the Berserker"
    class_features_by_level = defaultdict(list)


class TotemWarriorPath(SubClass):
    name = "Path of the Totem Warrior"
    class_features_by_level = defaultdict(list)
    

# SCAG
class BattleragerPath(SubClass):
    name = "Path of the Battlerager"
    class_features_by_level = defaultdict(list)


# XGTE
class AncestralGuardianPath(SubClass):
    name = "Path of the Ancestral Guardian"
    class_features_by_level = defaultdict(list)

    
class StormHeraldPath(SubClass):
    name = "Path of the Storm Herald"
    class_features_by_level = defaultdict(list)


class ZealotPath(SubClass):
    name = "Path of the Zealot"
    class_features_by_level = defaultdict(list)
    

class Barbarian(CharClass):
    class_name = 'Barbarian'
    hit_dice_faces = 12
    saving_throw_proficiencies = ('strength', 'constitution')
    _proficiencies_text = ('light armor', 'medium armor', 'shields',
                           'simple weapons', 'martial weapons')
    weapon_proficiencies = (weapons.simple_weapons + weapons.martial_weapons)
    class_skill_choices = ('Animal Handling', 'Athletics',
                           'Intimidation', 'Nature', 'Perception', 'Survival')
    subclasses_available = (BerserkerPath, TotemWarriorPath, BattleragerPath,
                            AncestralGuardianPath, StormHeraldPath, ZealotPath)
    features_by_level = defaultdict(list)

