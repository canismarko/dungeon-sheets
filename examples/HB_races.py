"""This file defines some homebrew mechanics that can be imported into
character sheets using ``dungeonsheets.import_homebrew``. See
``homebrew.py`` for an example of how these homebrew mechanics can be
used.

"""

from dungeonsheets import race
from dungeonsheets import features as feats
# from dungeonsheets import mecanics

class WildCompanion(feats.Feature):
    """You gain the ability to summon a spirit that assumes an animal form:
        as an action, you can expend a use of your Wild Shape feature
        to cast the *find familiar* spell, without material components.
        
        When you cast the spell in this way, the familiar
        is a fey instead of a beast, and the familiar disapears after
        a number of hours equal to half your druid level.
    """
    
    name = "Wild Companion"
    source = "Class (Druid)"

# shifters
class Shifting(feats.Feature):
    """As a bonus action, you can assume a more bestial appearence.
    This transformation lasts for 1 minute, until you die, or until 
    you revert to your normal appearence as a bonus action. When you shift, 
    you gain temporary hit points equal to your level +  your Constitution
    modifier (minimum of 1 temporary hit point). You also gain additional
    benefits that depend on your shifter subrace. Once you shift, 
    you can't to so again until you finish a short or long rest.
    """

    name = "Beasthide Shifting"
    source = "Race (Beasthide Shifter)"

class BeasthideShifting(feats.Feature):
    """Whenever you shift, you gain 1d6 additional temporary hit points.
    While shifted, you have a +1 bonus to your Armor Class.

    """

    name = "Beasthide Shifting (1x/SR)"
    source = "Race (Beasthide Shifter)"

class LongtoothShifting(feats.Feature):
    """While shifted, you can use your elongated fangs to make an unarmed
    strike as a bonus action. If you hit with your fangs, you can deal
    piercing damage equal to 1d6 + your Strength modifier, instead
    of the bludgeoning damage normal for an unarmed attack.

    """

    name = "Longtooth Shifting (1x/SR)"
    source = "Race (Longtooth Shifter)"
    
class SwiftstrideShifting(feats.Feature):
    """While shifted, your walking speed increases by 10 feet. Additionally,
    you can move up to 10 feet as a reaction when a creature ends its turn
    within 5 feet of you. This reactive movement doesn't provoke
    opportunity attacks.

    """

    name = "Swiftstride Shifting (1x/SR)"
    source = "Race (Swiftstride Shifter)"
    
class WildhuntShifting(feats.Feature):
    """While shifted, you have advantage on Wisdom checks, and no creature
    within 30 feet of you can make an attack roll with advantage against you,
    unless you are incapacitated.

    """

    name = "Wildhunt Shifting (1x/SR)"
    source = "Race (Beasthide Shifter)"

class NaturalAthlete(feats.Feature):
    """You have proficiency in the Athletics skill.
    """
    
    name = "Natural Athlete"
    source = "Race (Beasthide Shifter)"
    
class Fierce(feats.Feature):
    """You have proficiency in the Intimidation skill.
    """
    
    name = "Fierce"
    source = "Race (Longtooth Shifter)"
    
class Graceful(feats.Feature):
    """You have proficiency in the Acrobatics skill.
    """
    
    name = "Graceful"
    source = "Race (Swiftstride Shifter)"

class NaturalTracker(feats.Feature):
    """You have proficiency in the Survival skill.
    """
    
    name = "Natural Tracker"
    source = "Race (Wildhunt Shifter)"


class _Shifter(race.Race):
    name = "Shifter"
    size = "medium"
    speed = 30
    languages = ("Common", )
    features = (feats.Darkvision, Shifting)


class BeasthideShifter(_Shifter):
    name = "Beasthide Shifter"
    constitution_bonus = 2
    strength_bonus = 1
    features = _Shifter.features + (BeasthideShifting, NaturalAthlete)
    
class LongtoothShifter(_Shifter):
    name = "Longtooth Shifter"
    constitution_bonus = 2
    strength_bonus = 1
    features = _Shifter.features + (LongtoothShifting, Fierce)
    
class SwiftstrideShifter(_Shifter):
    name = "Swiftstride Shifter"
    dexterity_bonus = 2
    charisma_bonus = 1
    features = _Shifter.features + (SwiftstrideShifting, Graceful)

class WildhuntShifter(_Shifter):
    name = "Wildhunt Shifter"
    constitution_bonus = 2
    strength_bonus = 1
    features = _Shifter.features + (WildhuntShifting, NaturalTracker)
    
class DualMind(feats.Feature):
    """You have advantage on all Wisdom saving throws.
    """
    name = "Dual Mind"
    source = "Race (Kalashtar)"

class MentalDiscipline(feats.Feature):
    """You have resistance to psychic damage.
    """
    name = "Mental Discipline"
    source = "Race (Kalashtar)"
    
class MindLink(feats.Feature):
    """You can speak telepathically to any creature you can see, provided 
    the crature is within a number of feet of you equal to 10 times your level.
    You don't need to share a language with the creature for it to understand 
    your telepathic utterances, but the creature must be able to 
    understand at least one language.
    
    When you are using this trait to speak telepathically to a creature, 
    you can use your action to give that crature the ability to speak 
    telepatically with you for 1 hour or until you end this effect as an
    action. To use this ability, the creature must be able to see you and must
    be within this trait's range. You can give this ability to only
    one creature at a time; giving it to another creature takes it away from
    another creature who has it."""
    name = "Mind Link"
    source = "Race (Kalashtar)"
    
class SeveredFromDreams(feats.Feature):
    """Kalashtar sleep, but they don't connect to the plane of dreams
    as other creatures do. Instead, their minds draw from the memoires
    of their otherworldly spirit while they sleep. As such, 
    you are immune to spells that require you to dream, like *dream*,
    but not to spells and other magical effects that put you to sleep.
    """
    name = "Severed from Dreams"
    source = "Race (Kalashtar)"

class Kalashtar(race.Race):
    name = "Kalashtar"
    size = "medium"
    speed = 30
    charisma_bonus = 1
    wisdom_bonus = 2
    languages = ("Common", "Quori", )
    features = (DualMind, MentalDiscipline, MindLink, SeveredFromDreams)
    
class PoisonResiliense(feats.Feature):
    """You have advantage on saving throws you make to avoid or end the 
    poisoned condition on yourself. You also have resistance to poison damage.
    """
    name = "Poison Resilience"
    source = "Race (Yuan-Ti)"
    
class SerpentineSpellcasting(feats.Feature):
    """You know the poison spray cantrip. You can cast animal friendship an 
    unlimited number of times with this trait, but you can target only 
    snakes with it. Starting at 3rd level, you can also cast suggestion 
    with this trait. Once you cast it, you can't do so again until you 
    finish a long rest. You can also cast it using any spell slots you 
    have of 2nd level or higher.
    
    Intelligence, Wisdom, or Charisma is your spellcasting ability 
    for these spells when you cast them with this trait 
    (choose when you select this race).
    """
    
class Yuan_Ti(race.Race):
    name = "Yuan-Ti"
    size = "medium"
    speed = 30
    languages = ("Common", )
    features = (feats.Darkvision, feats.MagicResistance, PoisonResiliense,
                SerpentineSpellcasting)


    
