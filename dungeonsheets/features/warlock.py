from .features import Feature
from .. import spells


# All Invocations
class Invocation(Feature):
    """
    A generic Eldritch Invocation. Add details in features/warlock.py
    """
    name = 'Unnamed Invocation'
    source = "Warlock (Eldritch Invocations)"
    at_will_spells = ()

    def cast_spell_at_will(self, spell):
        s = spell()
        s.level = 0
        if 'V' in s.components:
            c = list(s.components)
            c.remove('V')
            s.components = tuple(c)
        self.spells_known += (s,)
        self.spells_prepared += (s,)

    def __init__(self):
        for s in self.at_will_spells:
            self.cast_spell_at_will(s)


# PHB
class AgonizingBlast(Invocation):
    """When you cast eldritch blast, add your Charisma modifier to the damage it
    deals on a hit.

    """
    name = "Agonizing Blast"
    needs_implementation = True


class ArmorOfShadows(Invocation):
    """You can cast mage armor on yourself at will, without expending a spell slot
    or material components

    """
    name = "Armor of Shadows"
    at_will_spells = (spells.MageArmor,)


class AscendantStep(Invocation):
    """You can cast levitate on yourself at will, without expending a spell slot
    or material components.

    **Prerequisite: 9th level**

    """
    name = 'Ascendant Step'
    at_will_spells = (spells.Levitate,)


class BeastSpeech(Invocation):
    """You can cast speak with animals at will, without expending a spell slot.

    """
    name = "Beast Speech"
    at_will_spells = (spells.SpeakWithAnimals,)


class BeguilingInfluence(Invocation):
    """You gain proficiency in the Deception and Persuasion skills.

    """
    name = "Beguiling Influence"
    needs_implementation = True


class BewitchingWhispers(Invocation):
    """You can cast compulsion once using a warlock spell slot. You can’t do so
    again until you finish a long rest

    **Prerequisite**: 7th Level
    """
    name = "Bewitching Whispers"

    
class BookOfAncientSecrets(Invocation):
    """You can now inscribe magical rituals in your Book of Shadows. Choose two
    1st-level spells that have the ritual tag from any class’s spell list. The
    spells appear in the book and don’t count against the number of spells you
    know. With your Book of Shadows in hand, you can cast the chosen spells as
    rituals. You can’t cast the spells except as rituals, unless you’ve learned
    them by some other means. You can also cast a warlock spell you know as a
    ritual if it has the ritual tag.

    On your adventures, you can add other ritual spells to your Book o f
    Shadows. When you find such a spell, you can add it to the book if the
    spell’s level is equal to or less than half your warlock level (rounded up)
    and if you can spare the time to transcribe the spell. For each level of
    the spell, the transcription process takes 2 hours and costs 50 gp for the
    rare inks needed to inscribe it

    """
    name = "Book of Ancient Secrets"


class ChainsOfCarceri(Invocation):
    """You can cast hold monster at will—targeting a celestial, fiend, or
    elemental—without expending a spell slot or material components. You must
    finish a long rest before you can use this invocation on the same creature
    again.

    **Prerequisites**: 15th level, Pact of the Chain Feature
    """
    name = "Chains of Carceri"


class DevilsSight(Invocation):
    """You can see normally in darkness, both magical and nonmagical, to a
    distance of 120 feet.

    """
    name = "Devil's Sight"


class DreadfulWord(Invocation):
    """You can cast confusion once using a warlock spell slot. You can’t do so
    again until you finish a long rest.

    """
    name = "Dreadful Word"

    
class EldritchSight(Invocation):
    """You can cast detect magic at will, without expending a spell slot.

    """
    name = "Eldritch Sight"
    at_will_spells = (spells.DetectMagic,)


class EldritchSpear(Invocation):
    """When you cast eldritch blast, its range is 300 feet.

    """
    name = "Eldritch Spear"
    needs_implementation = True


class EyesOfTheRuneKeeper(Invocation):
    """
    You can read all writing.

    """
    name = "Eyes of the Rune Keeper"


class FiendishVigor(Invocation):
    """You can cast false life on yourself at will as a 1st-level spell, without
    expending a spell slot or material components.

    """
    name = "Fiendish Vigor"
    at_will_spells = (spells.FalseLife,)


class GazeOfTwoMinds(Invocation):
    """You can use your action to touch a willing humanoid and perceive through
    its senses until the end of your next turn. As long as the creature is on
    the same plane of existence as you, you can use your action on subsequent
    turns to maintain this connection, extending the duration until the end of
    your next turn. While perceiving through the other creature’s senses, you
    benefit from any special senses possessed by that creature, and you are
    blinded and deafened to your own surroundings.

    """
    name = "Gaze of Two Minds"


class LifeDrinker(Invocation):
    """When you hit a creature with your pact weapon, the creature takes extra
    necrotic damage equal to your Charisma modifier (minimum 1).
    
    **Prerequisite**: 12th Level, Pact of the Blade
    """
    name = "Life Drinker"
    needs_implementation = True


class MaskOfManyFaces(Invocation):
    """You can cast disguise self at will, without expending a spell slot.

    """
    name = "Mask of Many Faces"
    at_will_spells = (spells.DisguiseSelf,)


class MasterOfMyriadForms(Invocation):
    """
    You can cast alter self at will, without expending a spell slot.

    **Prerequisite**: 15th Level
    """
    name = "Master of Myriad Forms"
    at_will_spells = (spells.AlterSelf,)

    
class MinionsOfChaos(Invocation):
    """You can cast conjure elemental once using a warlock spell slot. You can’t
    do so again until you finish a long rest.

    **Prerequisite**: 9th Level
    """
    name = "Minions of Chaos"

    
class MireTheMind(Invocation):
    """You can cast slow once using a warlock spell slot. You can’t do so again
    until you finish a long rest.

    """
    name = "Mire the Mind"


class MistyVisions(Invocation):
    """You can cast silent image at will, without expending a spell slot or
    material components.

    """
    name = "Misty Visions"
    at_will_spells = (spells.MistyVisions,)


class OneWithShadows(Invocation):
    """When you are in an area of dim light or darkness, you can use your action
    to become invisible until you move or take an action or a reaction.

    **Prerequisite**: 5th Level
    """
    name = "One with Shadows"


class OtherworldlyLeap(Invocation):
    """You can cast jump on yourself at will, without expending a spell slot or
    material components.

    **Prerequisite**: 9th Level

    """
    name = "Otherworldly Leap"
    at_will_spells = (spells.Jump,)


class RepellingBlast(Invocation):
    """When you hit a creature with eldritch blast, you can push the creature up
to 10 feet away from you in a straight line.

    """
    name = "Repelling Blast"


class SculptorOfFlesh(Invocation):
    """You can cast polymorph once using a warlock spell slot. You can’t do so
    again until you finish a long rest.

    **Prerequisite**: 7th Level
    """
    name = "Sculptor of Flesh"


class SignOfIllOmen(Invocation):
    """You can cast bestow curse once using a warlock spell slot. You can’t do so
    again until you finish a long rest.

    **Prerequisite**: 5th Level

    """
    name = "Sign of Ill Omen"

    
class ThiefOfFiveFates(Invocation):
    """You can cast bane once using a warlock spell slot. You can’t do so again
    until you finish a long rest.

    """
    name = "Thief of Five Fates"
    needs_implementation = True


class ThirstingBlade(Invocation):
    """You can attack with your pact weapon twice, instead of once, whenever you
    take the Attack action on your turn.
    
    **Prerequisite**: 5th Level, Pact of the Blade
    """
    name = "Thirsting Blade"


class VisionsOfDistantRealms(Invocation):
    """
    You can cast arcane eye at will, without expending a spell slot
    
    **Prerequisite**: 15th level
    """
    name = "Visions of Distant Realms"
    at_will_spells = (spells.ArcaneEye,)

    
class VoiceOfTheChain(Invocation):
    """You can communicate telepathically with your familiar and perceive through
    your familiar’s senses as long as you are on the same plane of
    existence. Additionally, while perceiving through your familiar’s senses,
    you can also speak through your familiar in your own voice, even if your
    familiar is normally incapable of speech.

    **Prerequisite**: Pact of the Chain

    """
    name = "Voice of the Chain"


class WhispersOfTheGrave(Invocation):
    """You can cast speak with dead at will, without expending a spell slot

    **Prerequsite**: 9th Level

    """
    name = "Whispers of the Grave"
    at_will_spells = (spells.SpeakWithDead,)


class WitchSight(Invocation):
    """You can see the true form of any shapechanger or creature concealed by
    illusion or transmutation magic while the creature is within 30 feet of you
    and within line of sight.

    """
    name = "Witch Sight"
