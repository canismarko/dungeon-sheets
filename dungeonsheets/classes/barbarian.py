from .. import (features, weapons)
from .classes import (CharClass, SubClass)
from collections import defaultdict


# PHB
class BerserkerPath(SubClass):
    """For some barbarians, rage is a means to an end-—that end being
    violence. The Path of the Berserker is a path of untrammeled fury, slick
    with blood. As you enter the berserker’s rage, you thrill in the chaos of
    battle, heedless of your own health or well-being.

    """
    name = "Path of the Berserker"
    class_features_by_level = defaultdict(list)


class TotemWarriorPath(SubClass):
    """The Path of the Totem Warrior is a spiritual journey, as the barbarian
    accepts a spirit animal as guide, protector, and inspiration. In battle,
    your totem spirit fills you with supernatural might, adding magical fuel to
    your barbarian rage.

    Most barbarian tribes consider a totem animal to be kin to a particular
    clan. In such cases, it is unusual for an individual to have more than one
    totem animal spirit, though exceptions exist.

    """
    name = "Path of the Totem Warrior"
    class_features_by_level = defaultdict(list)
    

# SCAG
class BattleragerPath(SubClass):
    """Known as Kuldjargh (literally "axe idiot") in Dwarvish, battleragers are
    dwarf followers of the gods of war and take the Path of the
    Battlerager. They specialize in wearing bulky, spiked armor and throwing
    themselves into combat, striking with their body itself and giving
    themselves over to the fury of battle.

    """
    name = "Path of the Battlerager"
    class_features_by_level = defaultdict(list)


# XGTE
class AncestralGuardianPath(SubClass):
    """Some barbarians hail from cultures that revere their ancestors. These
    tribes teach that the warriors of the past linger in the world as mighty
    spirits, who can guide and protect the living. When a barbarian who follows
    this path rages, the barbarian contacts the spirit world and calls on these
    guardian spirits for aid.

    Barbarians who draw on their ancestral guardians can better fight to
    protect their tribes and their allies. In order to cement ties to their
    ancestral guardians, barbarians who follow this path cover themselves in
    elabo— rate tattoos that celebrate their ancestors’ deeds. These tattoos
    tell sagas of victories against terrible monsters and other fearsome
    rivals.

    """
    name = "Path of the Ancestral Guardian"
    class_features_by_level = defaultdict(list)

    
class StormHeraldPath(SubClass):
    """All barbarians harbor a fury within. Their rage grants them superior
    strength, durability, and speed. Barbarians who follow the Path of the
    Storm Herald learn to transform that rage into a mantle of primal magic,
    which swirls around them. When in a fury, a barbarian ofthis path taps into
    the forces of nature to create powerful magical effects.

    Storm heralds are typically elite champions who train alongside druids,
    rangers, and others sworn to protect nature. Other storm heralds hone their
    craft in lodges in regions wracked by storms, in the frozen reaches at the
    world’s end, or deep in the hottest deserts.

    """
    name = "Path of the Storm Herald"
    class_features_by_level = defaultdict(list)


class ZealotPath(SubClass):
    """Some deities inspire their followers to pitch themselves into a ferocious
    battle fury. These barbarians are zealots—warriors who channel their rage
    into powerful disn plays of divine power.

    A variety of gods across the worlds of D&D inspire their followers to
    embrace this path. Tempus from the Forgotten Realms and Hextor and Erythnul
    of Greyhawk are all prime examples. In general, the gods who inspire
    zealots are deities of combat, destruction, and violence. Not all are evil,
    but few are good

    """
    name = "Path of the Zealot"
    class_features_by_level = defaultdict(list)
    

class Barbarian(CharClass):
    name = 'Barbarian'
    hit_dice_faces = 12
    saving_throw_proficiencies = ('strength', 'constitution')
    weapon_proficiencies = (weapons.simple_weapons + weapons.martial_weapons)
    _proficiencies_text = ('light armor', 'medium armor', 'shields',
                           'simple weapons', 'martial weapons')
    multiclass_weapon_proficiencies = weapon_proficiencies
    _multiclass_proficiencies_text = ('shields', 'simple weapons', 'martial weapons')
    class_skill_choices = ('Animal Handling', 'Athletics',
                           'Intimidation', 'Nature', 'Perception', 'Survival')
    subclasses_available = (BerserkerPath, TotemWarriorPath, BattleragerPath,
                            AncestralGuardianPath, StormHeraldPath, ZealotPath)
    features_by_level = defaultdict(list)

