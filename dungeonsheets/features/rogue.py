from math import ceil

from dungeonsheets.features.features import Feature


# PHB
class RogueExpertise(Feature):
    """At 1st level, choose two of your skill proficiencies, or one of your skill
    proficiencies and your proficiency with thieves' tools. Your proficiency
    bonus is doubled for any ability check you make that uses either of the
    chosen proficiencies.

    At 6th level, you can choose two more of your
    proficiencies (in skills or with thieves' tools) to gain this benefit.

    Add these skills to "skill_expertise" in your character.py file

    """

    name = "Expertise"
    source = "Rogue"


class SneakAttack(Feature):
    """Beginning at 1st level, you know how to strike subtly and exploit a foe's
    distraction. Once per turn, you can deal an extra 1d6 damage to one
    creature you hit with an attack if you have advantage on the attack
    roll. The attack must use a finesse or a ranged weapon.

    You don't need advantage on the attack roll if another enemy of the target
    is within 5 feet of it, that enemy isn't incapacitated, and you don't have
    disadvantage on the attack roll.

    The amount of the extra damage increases as you gain levels in this class,
    as shown in the Sneak Attack column of the Rogue table.
    """

    _name = "Sneak Attack"
    source = "Rogue"

    @property
    def name(self):
        level = self.owner.Rogue.level
        dice = ceil(level / 2.0)
        name = self._name + " ({:d}d6)".format(dice)
        return name


class CunningAction(Feature):
    """Starting at 2nd level, your quick thinking and agility allow you to move
    and act quickly. You can take a bonus action on each of your turns in
    combat. This action can be used only to take the Dash, Disengage, or Hide
    action.

    """

    name = "Cunning Action"
    source = "Rogue"


class UncannyDodge(Feature):
    """Starting at 5th level, when an attacker that you can see hits you with an
    attack, you can use your reaction to halve the attack's damage against you.

    """

    name = "Uncanny Dodge"
    source = "Class (many)"


class Evasion(Feature):
    """Beginning at 7th level, you can nimbly dodge out o f the way of certain
    area effects, such as a red dragon's fiery breath or an ice storm
    spell. When you are subjected to an effect that allows you to make a
    Dexterity saving throw to take only half damage, you instead take no damage
    if you succeed on the saving throw, and only half damage if you fail.

    """

    name = "Evasion"
    source = "Class (many)"


class ReliableTalent(Feature):
    """By 11th level, you have refined your chosen skills until they approach
    perfection. Whenever you make an ability check that lets you add your
    proficiency bonus, you can treat a d20 roll of 9 or lower as a 10.

    """

    name = "Reliable Talent"
    source = "Rogue"


class BlindSense(Feature):
    """Starting at 14th level, if you are able to hear, you are aware of the
    location of any hidden or invisible creature within 10 feet of you.
    """

    name = "Blind Sense"
    source = "Rogue"


class SlipperyMind(Feature):
    """By 15th level, you have acquired greater mental strength. You gain
    proficiency in Wisdom saving throws.

    """
    name = "Slippery Mind"
    source = "Rogue"


class Elusive(Feature):
    """Beginning at 18th level, you are so evasive that attackers rarely gain the
    upper hand against you. No attack roll has advantage against you while you
    aren't incapacitated.

    """

    name = "Elusive"
    source = "Rogue"


class StrokeOfLuck(Feature):
    """At 20th level, you have an uncanny knack for succeeding when you need
    to. If your attack m isses a target within range, you can turn the miss
    into a hit. Alternatively, if you fail an ability check, you can treat the
    d20 roll as a 20.

    Once you use this feature, you can't use it again until you finish a short
    or long rest.

    """

    name = "Stroke of Luck"
    source = "Rogue"


# Thief
class FastHands(Feature):
    """Starting at 3rd level, you can use the bonus action granted by your Cunning
    Action to make a Dexterity (Sleight of Hand) check, use your thieves' tools
    to disarm a trap or open a lock, or take the Use an Object action.

    """

    name = "Fast Hands"
    source = "Rogue (Thief)"


class SecondStoryWork(Feature):
    """When you choose this archetype at 3rd level, you gain the ability to climb
    faster than normal; climbing no longer costs you extra movement. In
    addition, when you make a running jump, the distance you cover increases by
    a number of feet equal to your Dexterity modifier.

    """

    name = "Second-Story Work"
    source = "Rogue (Thief)"


class SupremeSneak(Feature):
    """Starting at 9th level, you have advantage on a Dexterity (Stealth) check if
    you move no more than half your speed on the same turn

    """

    name = "Supreme Sneak"
    source = "Rogue (Thief)"


class UseMagicDevice(Feature):
    """By 13th level, you have learned enough about the workings of magic that you
    can improvise the use of items even when they are not intended for you. You
    ignore all class, race, and level requirements on the use of magic items

    """

    name = "Use Magic Device"
    source = "Rogue (Thief)"


class ThiefsReflexes(Feature):
    """When you reach 17th level, you have become adept at laying ambushes and
    quickly escaping danger. You can take two turns during the first round of
    any combat. You take your first turn at your normal initiative and your
    second turn at your initiative minus 10. You can't use this feature when
    you are surprised.

    """

    name = "Thief's Reflexes"
    source = "Rogue (Thief)"


# Assassin
class Assassinate(Feature):
    """Starting at 3rd level, you are at your deadliest when you get the drop on
    your enemies. You have advantage on attack rolls against any creature that
    hasn't taken a turn in the combat yet. In addition, any hit you score
    against a creature that is surprised is a critical hit.

    """

    name = "Assassinate"
    source = "Rogue (Assassin)"


class InfiltrationExpertise(Feature):
    """Starting at 9th level, you can unfailingly create false identities for
    yourself. You must spend seven days and 25 gp to establish the history,
    profession, and affiliations for an identity. You can't establish an
    identity that belongs to someone else. For example, you might acquire
    appropriate clothing, letters of introduction, and official- looking
    certification to establish yourself as a member of a trading house from a
    remote city so you can insinuate yourself into the company of other wealthy
    merchants. Thereafter, if you adopt the new identity as a disguise, other
    creatures believe you to be that person until given an obvious reason not
    to.

    """

    name = "Infiltration Expertise"
    source = "Rogue (Assassin)"


class Imposter(Feature):
    """At 13th level, you gain the ability to unerringly mimic another person's
    speech, writing, and behavior. You must spend at least three hours studying
    these three components of the person's behavior, listening to speech,
    examining handwriting, and observing mannerisms. Your ruse is indiscernible
    to the casual observer. If a wary creature suspects something is amiss, you
    have advantage on any Charisma (Deception) check you make to avoid
    detection

    """

    name = "Imposter"
    source = "Rogue (Assassin)"


class DeathStrike(Feature):
    """Starting at 17th level, you become a master of instant death. When you
    attack and hit a creature that is surprised, it must make a Constitution
    saving throw (DC 8 + your Dexterity modifier + your proficiency bonus). On
    a failed save, double the damage of your attack against the creature

    """

    name = "Death Strike"
    source = "Rogue (Assassin)"


# Arcane Trickster
class MageHandLegerdemain(Feature):
    """Starting at 3rd level, when you cast mage hand, you can make the
    spectral hand invisible, and you can perform the following
    additional tasks with it:

    - You can stow one object the hand is holding in a container worn
      or carried by another creature.
    - You can retrieve an object in a container worn or carried by
      another creature.
    - You can use thieves' tools to pick locks and disarm traps at
      range

    You can perform one of these tasks without being noticed by a
    creature if you succeed on a Dexterity (Sleight of Hand) check
    contested by the creature's Wisdom (Perception) check. In
    addition, you can use the bonus action granted by your Cunning
    Action to control the hand.

    """

    name = "Mage Hand Legerdemain"
    source = "Rogue (Arcane Trickster)"


class MagicalAmbush(Feature):
    """Starting at 9th level, if you are hidden from a creature when you cast a
    spell on it, the creature has disadvantage on any saving throw it makes
    against the spell this turn

    """

    name = "Magical Ambush"
    source = "Rogue (Arcane Trickster)"


class VersatileTrickster(Feature):
    """At 13th level, you gain the ability to distract targets with your mage
    hand. As a bonus action on your turn, you can designate a creature within 5
    feet of the spectral hand created by the spell. Doing so gives you
    advantage on attack rolls against that creature until the end of the turn.

    """

    name = "Versatile Trickster"
    source = "Rogue (Arcane Trickster)"


class SpellThief(Feature):
    """At 17th level, you gain the ability to magically steal the knowledge of how
    to cast a spell from another spellcaster. Immediately after a creature
    casts a spell that targets you or includes you in its area of effect, you
    can use your reaction to force the creature to make a saving throw with its
    spellcasting ability modifier. The DC equals your spell save DC.

    On a failed save, you negate the spell's effect against you, and you steal
    the knowledge of the spell if it is at least 1st level and of a level you
    can cast (it doesn't need to be a wizard spell). For the next 8 hours, you
    know the spell and can cast it using your spell slots. The creature can't
    cast that spell until the 8 hours have passed. Once you use this feature,
    you can't use it again until you finish a long rest

    """

    name = "Spell Thief"
    source = "Rogue (Arcane Trickster)"


# Inquisitive
class EarForDeceit(Feature):
    """When you choose this archetype at 3rd level, you de- velop a talent for
    picking out lies. Whenever you make a Wisdom (Insight) check to determine
    whether a creature is lying, treat a roll of 7 or lower on the c120 as an
    8.

    """

    name = "Ear for Deceit"
    source = "Rogue (Inquisitive)"


class EyeForDetail(Feature):
    """Starting at 3rd level, you can use a bonus action to make a Wisdom
    (Perception) check to spot a hidden creature or object or to make an
    Intelligence (Investigation) check to uncover or decipher clues

    """

    name = "Eye for Detail"
    source = "Rogue (Inquisitive)"


class InsightfulFighting(Feature):
    """At 3rd level, you gain the ability to decipher an opponent's tactics and
    develop a counter to them. As a bonus action, you can make a Wisdom
    (Insight) check against a creature you can see that isn't incapacitated,
    contested by the target's Charisma (Deception) check. If you suc- ceed, you
    can use your Sneak Attack against that target even ifyou don't have
    advantage on the attack roll, but not if you have disadvantage on it. This
    benefit lasts for 1 minute or until you successfully use this feature
    against a different target

    """

    name = "Insightful Fighting"
    source = "Rogue (Inquisitive)"


# Optional class feature from *Tasha's Guide to Everything*
class SteadyAim(Feature):
    """As a bonus action, you give yourself advantage on your next attack
    roll on the current turn. You can use this bonus action only if
    you haven't moved during this turn, and after you use the bonus
    action, your speed is 0 until the end of the current turn.
    
    """
    name = "Steady Aim"
    source = "Rogue (3rd level, optional)"


class SteadyEye(Feature):
    """Starting at 9th level, you have advantage on any Wisdom (Perception) or
    Intelligence (Investigation) check if you move no more than half your speed
    on the same turn

    """

    name = "Steady Eye"
    source = "Rogue (Inquisitive)"


class UnerringEye(Feature):
    """Beginning at 13th level, your senses are almost im« possible to foil. As an
    action, you sense the presence of illusions, shapechangers not in their
    original form, and other magic designed to deceive the senses within 30
    feet ofyou, provided you aren't blinded or deafened. You sense that an
    effect is attempting to trick you, but you gain no insight into what is
    hidden or into its true nature. You can use this feature a number of times
    equal to your Wisdom modifier (minimum of once), and you regain all
    expended uses of it when you finish a long rest

    """

    name = "Unerring Eye"
    source = "Rogue (Inquisitive)"


class EyeForWeakness(Feature):
    """At 17th level, you learn to exploit a creature's weak- nesses by carefully
    studying its tactics and movement. While your Insightful Fighting feature
    applies to a creature, your Sneak Attack damage against that creature
    increases by 3d6

    """

    name = "Eye for Weakness"
    source = "Rogue (Inquisitive)"


# Mastermind
class MasterOfIntrigue(Feature):
    """When you choose this archetype at 3rd level, you gain proficiency with the
    disguise kit, the forgery kit, and one gaming set Of your choice. You also
    learn two languages of your choice. Additionally, you can unerringly mimic
    the speech patterns and accent of a creature that you hear speak for at
    least 1 minute, enabling you to pass yourself off as a native speaker of a
    particular land, provided that you know the language.

    """

    name = "Master of Intrigue"
    source = "Rogue (Mastermind)"


class MasterOfTactics(Feature):
    """Starting at 3rd level, you can use the Help action as a bonus
    action. Additionally, when you use the Help action to aid an ally in
    attacking a creature, the target of that attack can be within 30 feet of
    you, rather than within 5 feet of you, if the target can see or hear you

    """

    name = "Master of Tactics"
    source = "Rogue (Mastermind)"


class InsightfulManipulator(Feature):
    """Starting at 9th level, if you spend at least 1 minute observing or
    interacting with another creature outside combat, you can learn certain
    information about its ca- pabilities compared to your own. The DM tells you
    if the creature is your equal, superior, or inferior in regard to two of
    the following characteristics of your choice:

    • Intelligence score

    • Wisdom score

    • Charisma score

    --Class levels (if any)

    At the DM's option, you might also realize you know a piece of the
    creature's history or one of its personality traits, if it has any

    """

    name = "Insightful Manipulator"
    source = "Rogue (Mastermind)"


class Misdirection(Feature):
    """Beginning at 13th level, you can sometimes cause another creature to
    suffer an attack meant for you. When you are targeted by an attack while a
    creature within 5 feet of you is granting you cover against that attack,
    you can use your reaction to have the attack target that crea- ture instead
    of you

    """

    name = "Misdirection"
    source = "Rogue (Mastermind)"


class SoulOfDeceit(Feature):
    """Starting at 17th level, your thoughts can't be read by telepathy or other
    means, unless you allow it. You can present false thoughts by succeeding on
    a Charisma (Deception) check contested by the mind reader's Wis- dom
    (Insight) check. Additionally, no matter what you say, magic that would
    determine if you are telling the truth indicates you are being truthful if
    you so choose, and you can't be compelled to tell the truth by magic

    """

    name = "Soul of Deceit"
    source = "Rogue (Masterind)"


# Scout
class Skirmisher(Feature):
    """Starting at 3rd level, you are difficult to pin down during a fight. You
    can move up to halfyour speed as a reaction when an enemy ends its turn
    within 5 feet of you. This movement doesn't provoke opportunity attacks

    """

    name = "Skirmisher"
    source = "Rogue (Scout)"


class Survivalist(Feature):
    """When you choose this archetype at 3rd level, you gain proficiency in the
    Nature and Survival skills if you don't already have it. Your proficiency
    bonus is doubled for any ability check you make that uses either of those
    pro- ficiencies

    """

    def __init__(self, owner=None):
        super().__init__(owner=owner)
        self.owner.skill_expertise += ("nature", "survival")


class SuperiorMobility(Feature):
    """At 9th level, your walking speed increases by 10 feet. If you have a
    climbing or swimming speed, this increase applies to that speed as well.

    """

    name = "Superior Mobility"
    source = "Rogue (Scout)"
    needs_implementation = True  # apply to climbing and swimming


class AmbushMaster(Feature):
    """Starting at 13th level, you excel at leading ambushes and acting first in a
    fight. You have advantage on initiative rolls. In addition, the first
    creature you hit during the first round of a combat becomes easier for you
    and others to strike; attack rolls against that target have advantage until
    the start ofyour next turn

    """

    name = "Ambush Master"
    source = "Rogue (Scout)"


class SuddenStrike(Feature):
    """Starting at 17th level, you can strike with deadly speed. If you take the
    Attack action on your turn, you can make one additional attack as a bonus
    action. This attack can benefit from your Sneak Attack even if you have
    already used it this turn, but you can't use your Sneak Attack against the
    same target more than once in a turn

    """

    name = "Sudden Strike"
    source = "Rogue (Scout)"


# Swashbuckler
class FancyFootwork(Feature):
    """When you choose this archetype at 3rd level, you learn how to land a strike
    and then slip away without reprisal. During your turn, if you make a melee
    attack against a creature, that creature can't make opportunity attacks
    against you for the rest ofyour turn

    """

    name = "Fancy Footwork"
    source = "Rogue (Swashbuckler)"


class RakishAudacity(Feature):
    """Starting at 3rd level, your confidence propels you into battle. You can give
    yourself a bonus to your initiative rolls equal to your Charisma
    modifier. You also gain an additional way to use your Sneak Attack; you
    don't need advantage on the attack roll to use your Sneak Attack against a
    creature if you are within 5 feet of it, no other creatures are within 5
    feet of you, and you don't have disadvantage on the attack roll. All the
    other rules for Sneak Attack still apply to you.

    """

    name = "Rakish Audacity"
    source = "Rogue (Swashbuckler)"


class Panache(Feature):
    """At 9th level, your charm becomes extraordinarily be- guiling. As an action,
    you can make a Charisma (Persuasion) check contested by a creature's
    Wisdom (Insight) check. The creature must be able to hear you, and the
    two ofyou must share a language. If you succeed on the check and the
    creature is hostile to you, it has disadvantage on attack rolls against
    targets other than you and can't make opportunity attacks against targets
    other than you.

    This effect lasts for 1 minute, until one of your companions attacks the
    target or affects it with a spell, or until you and the target are more
    than 60 feet apart. If you succeed on the check and the creature isn't
    hostile to you, it is charmed by you for 1 minute. While charmed, it
    regards you as a friendly acquaintance. This effect ends immediately if you
    or your companions do anything harmful to it

    """

    name = "Panache"
    source = "Rogue (Swashbuckler)"


class ElegantManeuver(Feature):
    """Starting at 13th level, you can use a bonus action on your turn to gain
    advantage on the next Dexterity (Ac- robatics) or Strength (Athletics)
    check you make during the same turn

    """

    name = "Elegant Maneuver"
    source = "Rogue (Swashbuckler)"


class MasterDuelist(Feature):
    """Beginning at 17th level, your mastery of the blade lets you turn failure
    into success in combat. Ifyou miss with an attack roll, you can roll it
    again with advantage. Once you do so, you can't use this feature again
    until you finish a short or long rest

    """

    name = "Master Duelist"
    source = "Rogue (Swashbuckler)"


# Soulknife
class PsionicPower(Feature):
    """You harbor a wellspring of psionic energy within yourself. This·
    energy is represented by your Psionic Energy dice, which are each
    a ``d6``. You have a number of these dice equal to twice your
    proficiency bonus, and they fuel various psionic powers you have,
    which are detailed below.
    
    Some of your powers expend the Psionic Energy die they use, as
    specified in a power's description, and you can't use a power if
    it requires you to use a die when your dice are all expended. You
    regain all your expended Psionic Energy dice when you finish a
    long rest. In addition, as a bonus action, you can regain one
    expended Psionic Energy die, but you can't do so again until you
    finish a short or long rest.
    
    When you reach certain levels in this class, the size of your
    Psionic Energy dice increases: at 5th level (``d8``), 11th level
    (``dlO``), and 17th level (``d12``).
    
    The powers below use your Psionic Energy dice.
    
    Psi-Bolstered Knack
      When your nonpsionic training fails you, your psionic power can
      help: if you fail an ability check using a skill or tool with
      which you have proficiency, you can roll one Psionic Energy die
      and add the number rolled to the check, potentially turning
      failure into success. You expend the die only if the roll
      succeeds.
    Psychic Whispers
      You can establish telepathic communication between yourself and
      others-perfect for quiet infiltration. As an action, choose one
      or more creatures you can see, up to a number of creatures equal
      to your proficiency bonus, and then roll one Psionic Energy
      die. For a number of hours equal to the number rolled, the
      chosen creatures can speak telepathically with you, and you can
      speak telepathically with them. To send or receive a message (no
      action required), you and the other creature must be within 1
      mile of each other. A creature can't use this telepathy if it
      can't speak any languages, and a creature can end the telepathic
      connection at any time (no action required). You and the
      creature don't need to speak a common language to understand
      each other.
      
      The first time you use this power after each long rest, you
      don't expend the Psionic Energy die. All other times you use the
      power, you expend the die.
    
    """
    name = "Psionic Power"
    source = "Rogue (Soulknife)"


class PsychicBlades(Feature):
    """You can manifest your psionic power as shimmering blades of psychic
    energy. Whenever you take the Attack action, you can manifest a
    psychic blade from your free hand and make the attack with that
    blade. This magic blade is a simple melee weapon with the finesse
    and thrown properties. It has a normal range of 60 feet and no
    long range, and on a hit, it deals psychic damage equal to 1d6
    plus the ability modifier you used for the attack roll. The blade
    vanishes immediately after it hits or misses its target, and it
    leaves no mark on its target if it deals damage.
    
    After you attack with the blade, you can make a melee or ranged
    weapon attack with a second psychic blade as a bonus action on the
    same turn, provided your other hand is free to create it. The
    damage die of this bonus attack is 1d4, instead of 1d6.

    """
    name = "Psychic Blades"
    source = "Rogue (Soulknife)"


class SoulBlades(Feature):
    """Your Psychic Blades are now an expression of your psi-suffused
    soul, giving you these powers that use your Psionic Energy dice:
    
    Homing Strikes
      If you make an attack roll with your Psychic Blades and miss the
      target, you can roll one Psionic Energy die and add the number
      rolled to the attack roll. If this causes the attack to hit, you
      expend the Psionic Energy die.
    Psychic Teleportation
      As a bonus action, you manifest one of your Psychic Blades,
      expend one Psionic Energy die and roll it, and throw the blade
      at an unoccupied space you can see, up to a number of feet away
      equal to 10 times the number rolled. You then teleport to that
      space, and the blade vanishes.
    
    """
    name = "Soul Blades"
    source = "Rogue (Soulknife)"


class PsychicVeil(Feature):
    """You can weave a veil of psychic static to mask yourself. As an
    action, you can magically become invisible, along with anything
    you are wearing or carrying, for 1 hour or until you dismiss this
    effect (no action required). This invisibility ends early
    immediately after you deal damage to a creature or you force a
    creature to make a saving throw.
    
    Once you use this feature, you can't do so again until you finish
    a long rest, unless you expend a Psionic Energy die to use this
    feature again.
    
    """
    name = "Psychic Veil"
    source = "Rogue (Soulknife)"


class RendMind(Feature):
    """You can sweep your Psychic Blades directly through a creature's
    mind. When you use your Psychic Blades to deal Sneak Attack damage
    to a creature, you can force that target to make a Wisdom saving
    throw (DC equal to 8 + your proficiency bonus + your Dexterity
    modifier). If the save fails, the target is stunned for 1
    minute. The stunned target can repeat the saving throw at the end
    of each of its turns, ending the effect on itself on a success.

    Once you use this feature, you can't do so again until you finish
    a long rest, unless you expend three Psionic Energy dice to use it
    again.

    """
    name = "Rend Mind"
    source = "Rogue (Soulknife)"
    
