__all__ = ('Monk')

from .. import (features, weapons)
from .classes import CharClass, SubClass
from collections import defaultdict


# PHB
class OpenHandWay(SubClass):
    """Monks of the Way of the Open Hand are the ultimate masters of martial arts
    combat, whether armed or unarmed. They learn techniques to push and trip
    their opponents, manipulate ki to heal damage to their bodies, and practice
    advanced meditation that can protect them from harm.

    """
    name = "Way of the Open Hand"
    features_by_level = defaultdict(list)


class ShadowWay(SubClass):
    """Monks of the Way of Shadow follow a tradition that values stealth and
    subterfuge. These monks might be called ninjas or shadowdancers, and they
    serve as spies and assassins. Sometimes the members of a ninja monastery
    are family members, forming a clan sworn to secrecy about their arts and
    missions. Other monasteries are more like thieves’ guilds, hiring out their
    services to nobles, rich merchants, or anyone else who can pay their
    fees. Regardless of their methods, the heads of these monasteries expect
    the unquestioning obedience of their students

    """
    name = "Way of Shadow"
    features_by_level = defaultdict(list)
    

class FourElementsWay(SubClass):
    """You follow a monastic tradition that teaches you to harness the
    elements. When you focus your ki, you can align yourself with the forces of
    creation and bend the four elements to your will, using them as an
    extension of your body. Some members of this tradition dedicate themselves
    to a single element, but others weave the elements together.

    Many monks of this tradition tattoo their bodies with representations of
    their ki powers, commonly imagined as coiling dragons, but also as
    phoenixes, fish, plants, mountains, and cresting waves.

    """
    name = "Way of the Four Elements"
    features_by_level = defaultdict(list)


# SCAG
class SunSoulWay(SubClass):
    """Monks of the Way of the Sun Soul learn to channel their own life energy
    into searing bolts of light. They teach that meditation can unlock the
    ability to unleash the indomitable light shed by the soul of every living
    creature

    """
    name = "Way of the Sun Soul"
    features_by_level = defaultdict(list)


class LongDeathWay(SubClass):
    """Monks of the Way of the Long Death are obsessed with the meaning and
    mechanics of dying. They capture creatures and prepare elaborate
    experiments to capture, record, and understand the moments of their
    demise. They then use this knowledge to guide their understanding of
    martial arts, yielding a deadly fighting style.

    """
    name = "Way of the Long Death"
    features_by_level = defaultdict(list)


# XGTE
class DrunkenMasterWay(SubClass):
    """The Way of the Drunken Master teaches its students to move with the jerky,
    unpredictable movements of a drunkard. A drunken master sways, tottering on
    unsteady feet, to present what seems like an incompetent combatant who
    proves frustrating to engage. The drunken master’s erratic stumbles conceal
    a carefully executed dance of blocks, parries, advances, attacks, and
    retreats.

    A drunken master often enjoys playing the fool to bring gladness to the
    despondent or to demonstrate humility to the arrogant, but when battle is
    joined, the drunken master can be a maddening, masterful foe

    """
    name = "Way of the Drunken Master"
    features_by_level = defaultdict(list)


class KenseiWay(SubClass):
    """Monks of the Way of the Kensei train relentlessly with their weapons, to
    the point where the weapon becomes an extension of the body. Founded on a
    mastery of sword fighting, the tradition has expanded to include many
    different weapons.

    A kensei sees a weapon in much the same way a calligrapher or painter
    regards a pen or brush. Whatever the weapon, the kensei views it as a tool
    used to express the beauty and precision of the martial arts. That such
    mastery makes a kensei a peerless warrior is but a side effect of intense
    devotion, practice, and study.

    """
    name = "Way of the Kensei"
    features_by_level = defaultdict(list)


class Monk(CharClass):
    name = 'Monk'
    hit_dice_faces = 8
    saving_throw_proficiencies = ('strength', 'dexterity')
    primary_abilities = ('dexterity', 'wisdom')
    _proficiencies_text = (
        'simple weapons', 'shortswords', 'unarmed',
        "one type of artisan's tools or one musical instrument")
    weapon_proficiencies = (weapons.Shortsword, weapons.Unarmed,
                            weapons.SimpleWeapon)
    multiclass_weapon_proficiencies = weapon_proficiencies
    _multiclass_proficiencies_text = ('simple weapons', 'shortswords',
                                      'unarmed')
    class_skill_choices = ('Acrobatics', 'Athletics', 'History', 'Insight',
                           'Religion', 'Stealth')
    subclasses_available = (OpenHandWay, ShadowWay,
                            FourElementsWay, SunSoulWay,
                            LongDeathWay, DrunkenMasterWay,
                            KenseiWay)
    features_by_level = defaultdict(list)
    features_by_level[1] = [features.UnarmoredDefenseMonk,
                            features.MartialArts]

    def __init__(self, level, subclass=None, **params):
        super().__init__(level, subclass=subclass, **params)
        for f in self.features_by_level[1]:
            if isinstance(f, features.MartialArts):
                f.level = self.level
