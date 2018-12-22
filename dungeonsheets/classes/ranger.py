__all__ = ('Ranger', 'RevisedRanger')

from .. import (weapons, features)
from .classes import CharClass, SubClass
from collections import defaultdict


# PHB
class Hunter(SubClass):
    """Emulating the Hunter archetype means accepting your place as a bulwark
    between civilization and the terrors of the wilderness. As you walk the
    Hunter’s path, you learn specialized techniques for fighting the threats
    you face, from rampaging ogres and hordes of orcs to towering giants and
    terrifying dragons.

    """
    name = "Hunter"
    features_by_level = defaultdict(list)


class BeastMaster(SubClass):
    """The Beast Master archetype embodies a friendship between the civilized
    races and the beasts of the world. United in focus, beast and ranger work
    as one to fight the monstrous foes that threaten civilization and the
    wilderness alike. Emulating the Beast Master archetype means committing
    yourself to this ideal, working in partnership with an animal as its
    companion and friend.

    """
    name = "Beast Master"
    features_by_level = defaultdict(list)


# XGTE
class GloomStalker(SubClass):
    """Gloom Stalkers are at home in the darkest places: deep under the earth, in
    gloomy alleyways, in primeval forests, and wherever else the light
    dims. Most folk enter such places with trepidation, but a Gloom Stalker
    ventures boldly into the darkness, seeking to ambush threats before they
    can reach the broader world. Such rangers are often found in the Underdark,
    but they will go any place Where evil lurks in the shadows

    """
    name = "Gloom Stalker"
    features_by_level = defaultdict(list)


class HorizonWalker(SubClass):
    """Horizon Walkers guard the world against threats that originate from other
    planes or that seek to ravage the mortal realm with otherworldly
    magic. They seek out planar portals and keep watch over them, venturing to
    the Inner Planes and the Outer Planes as needed to pursue their foes. These
    rangers are also friends to any forces in the multiverse—especially
    benevolent dragons, fey, and elementals—that work to preserve life and the
    order of the planes

    """
    name = "Horizon Walker"
    features_by_level = defaultdict(list)


class MonsterSlayer(SubClass):
    """You have dedicated yourself to hunting down creatures of the night and
    wielders of grim magic. A Monster Slayer seeks out vampires, dragons, evil
    fey, fiends, and other magical threats. Trained in supernatural tech-
    niques to overcome such monsters, Slayers are experts at unearthing and
    defeating mighty, mystical foes.

    """
    name = "Monster Slayer"
    features_by_level = defaultdict(list)


class Ranger(CharClass):
    name = 'Ranger'
    hit_dice_faces = 10
    saving_throw_proficiencies = ('strength', 'dexterity')
    _proficiencies_text = ("light armor", "medium armor", "shields",
                           "simple weapons", "martial weapons")
    weapon_proficiencies = weapons.simple_weapons + weapons.martial_weapons
    multiclass_weapon_proficiencies = weapon_proficiencies
    _multiclass_proficiencies_text = ('light armor', 'medium armor', 'shields',
                                      'simple weapons', 'martial weapons',
                                      '[choose one skill from Ranger list]')
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
    """Many rangers are more at home in the wilds than in civilization, to the
    point where animals consider them kin. Rangers of the Beast Conclave
    develop a close bond with a beast, then further strengthen that bond
    through the use of magic.

    """
    name = "Beast Conclave"
    features_by_level = defaultdict(list)
    

class HunterConclave(SubClass):
    """Some rangers seek to master weapons to better protect civilization from the
    terrors of the wilderness. Members of the Hunter Conclave learn specialized
    fighting techniques for use against the most dire threats, from rampaging
    ogres and hordes of orcs to towering giants and terrifying dragons

    """
    name = "Hunter Conclave"
    features_by_level = defaultdict(list)
    

class DeepStalkerConclave(SubClass):
    """Most folk descend into the depths of the Underdark only under the most
    pressing conditions, undertaking some desperate quest or following the
    promise of vast riches. All too often, evil festers beneath the earth
    unnoticed, and rangers of the Deep Stalker Conclave strive to uncover and
    defeat such threats before they can reach the surface.

    """
    name = "Deep Stalker Conclave"
    features_by_level = defaultdict(list)
    

class RevisedRanger(Ranger):
    name = 'Revised Ranger'
    features_by_level = defaultdict(list)
    subclasses_available = (BeastConclave, HunterConclave, DeepStalkerConclave)
    
