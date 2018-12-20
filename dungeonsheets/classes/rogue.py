from .. import (weapons)
from .. import features as feats
from .classes import CharClass


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

