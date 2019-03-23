from .features import Feature, FeatureSelector
from .ranger import Dueling, TwoWeaponFighting

# PHB
class BardicInspiration(Feature):
    """You can inspire others through stirring words or music. To do so, you use a
    bonus action on your turn to choose one creature other than yourself within
    60 feet of you who can hear you. That creature gains one Bardic Inspiration
    die, a d6.

    Once within the next 10 minutes, the creature can roll the die and add the
    number rolled to one ability check, attack roll, or saving throw it
    makes. The creature can wait until after it rolls the d20 before deciding
    to use the Bardic Inspiration die, but must decide before the DM says
    whether the roll succeeds or fails. Once the Bardic Inspiration die is
    rolled, it is lost. A creature can have only one Bardic Inspiration die at
    a time

    You can use this feature a number of times equal to your Charisma modifier
    (a minimum of once). You regain any expended uses when you finish a long
    rest.

    Your Bardic Inspiration die changes when you reach certain levels in this
    class. The die becomes a d8 at 5th level, a d10 at 10th level, and a d12
    at 15th level.

    """
    _name = "Bardic Inspiration"
    source = "Bard"

    @property
    def name(self):
        level = self.owner.Bard.level
        die = 'd6'
        if level >= 5:
            die = 'd8'
        if level >= 10:
            die = 'd10'
        if level >= 15:
            die = 'd12'
        num = max(1, self.owner.charisma.modifier)
        rest = 'LR'
        if level >= 5:  # font of inspiration
            rest = 'SR'
        return self._name + " ({:d}{:s}/{:s})".format(num, die, rest)


class JackOfAllTrades(Feature):
    """Starting at 2nd level, you can add half your proficiency bonus, rounded
    down, to any ability check you make that doesn’t already include your
    proficiency bonus. (Included in stats on Character Sheet above).

    """
    name = "Jack of All Trades"
    source = "Bard"


class SongOfRest(Feature):
    """Beginning at 2nd level, you can use soothing music or oration to help
    revitalize your wounded allies during a short rest. If you or any friendly
    creatures who can hear your performance regain hit points at the end of the
    short rest, each of those creatures regains an extra 1d6 hit points. The
    extra hit points increase when you reach certain levels in this class: to
    1d8 at 9th level, to 1d10 at 13th level, and to 1d12 at 17th level.

    """
    _name = "Song of Rest"
    source = "Bard"

    @property
    def name(self):
        level = self.owner.Bard.level
        die = ' (1d6)'
        if level >= 9:
            die = ' (1d8)'
        if level >= 13:
            die = ' (1d10)'
        if level >= 17:
            die = ' (1d12)'
        return self._name + die


class BardExpertise(Feature):
    """At 3rd level, choose two of your skill proficiencies. Your proficiency
    bonus is doubled for any ability check you make that uses either of the
    chosen proficiencies. At 10th level, you can choose another two skill
    proficiencies to gain this benefit.

    Add these skills to "skill_expertise" in your character.py file

    """
    name = "Expertise"
    source = "Bard"


class FontOfInspiration(Feature):
    """Beginning when you reach 5th level, you regain all of your expended uses of
    Bardic Inspiration when you finish a short or long rest.

    """
    name = "Font of Inspiration"
    source = "Bard"


class Countercharm(Feature):
    """At 6th level, you gain the ability to use musical notes or words of power
    to disrupt mind-influencing effects. As an action, you can start a
    performance that lasts until the end of your next turn. During that time,
    you and any friendly creatures within 30 feet of you have advantage on
    saving throws against being frightened or charmed. A creature must be able
    to hear you to gain this benefit. The performance ends early if you are
    incapacitated or silenced or if you voluntarily end it (no action
    required).

    """
    name = "Countercharm"
    source = "Bard"


class MagicalSecrets(Feature):
    """By 10th level, you have plundered magical knowledge from a wide spectrum of
    disciplines. Choose two spells from any class, including Bard. A spell
    you choose must be of a level you can cast, as shown on the Bard table, or
    a cantrip. The chosen spells count as bard spells for you and are included
    in the number in the Spells Known column of the Bard table. You learn two
    additional spells from any class at 14th level and again at 18th level.

    """
    name = "Magical Secrets"
    source = "Bard"


class SuperiorInspiration(Feature):
    """At 20th level, when you roll initiative and have no uses of Bardic
    Inspiration left, you regain one use.

    """
    name = "Superior Inspiration"
    source = "Bard"


# College of Lore
class LoreProficiencies(Feature):
    """When you join the College of Lore at 3rd level, you gain proficiency with
    three skills o f your choice.

    """
    name = "Bonus Proficiencies"
    source = "Bard (College of Lore)"


class CuttingWords(Feature):
    """Also at 3rd level, you learn how to use your wit to distract, confuse, and
    otherwise sap the confidence and competence of others. When a creature that
    you can see within 60 feet of you makes an attack roll, an ability check,
    or a damage roll, you can use your reaction to expend one of your uses of
    Bardic Inspiration, rolling a Bardic Inspiration die and subtracting the
    number rolled from the creature’s roll. You can choose to use this feature
    after the creature makes its roll, but before the DM determines whether the
    attack roll or ability check succeeds or fails, or before the creature
    deals its damage. The creature is immune if it can’t hear you or if it’s
    immune to being charmed.

    """
    name = "Cutting Words"
    source = "Bard (College of Lore)"


class AdditionalMagicalSecrets(Feature):
    """At 6th level, you learn two spells of your choice from any class. A spell
    you choose must be of a level you can cast, as shown on the Bard table, or
    a cantrip. The chosen spells count as bard spells for you but don’t count
    against the number of bard spells you know.

    """
    name = "Additional Magical Secrets"
    source = "Bard (College of Lore)"

    
class PeerlessSkill(Feature):
    """Starting at 14th level, when you make an ability check, you can expend one
    use of Bardic Inspiration. Roll a Bardic Inspiration die and add the number
    rolled to your ability check. You can choose to do so after you roil the
    die for the ability check, but before the DM tells you whether you succeed
    or fail

    """
    name = "Peerless Skill"
    source = "Bard (College of Lore)"


# College of Valor
class CombatInspiration(Feature):
    """Also at 3rd level, you learn to inspire others in battle. A creature that
    has a Bardic Inspiration die from you can roll that die and add the number
    rolled to a weapon damage roll it just made. Alternatively, when an attack
    roll is made against the creature, it can use its reaction to roll the
    Bardic Inspiration die and add the number rolled to its AC against that
    attack, after seeing the roll but before knowing whether it hits or misses

    """
    name = "Combat Inspiration"
    source = "Bard (College of Valor)"


class BardExtraAttack(Feature):
    """Starting at 6th level, you can attack twice, instead of once, whenever you
    take the Attack action on your turn

    """
    name = "Extra Attack (x2)"
    source = "Bard (College of Valor)"


class BardBattleMagic(Feature):
    """At 14th level, you have mastered the art of weaving spellcasting and weapon
    use into a single harmonious act. When you use your action to cast a bard
    spell, you can make one weapon attack as a bonus action

    """
    name = "Battle Magic"
    source = "Bard (College of Valor)"


# College of Glamour
class MantleOfInspiration(Feature):
    """When you join the College of Glamour at 3rd level, you gain the ability to
    weave a song of fey magic that imbues your allies with vigor and speed. As
    a bonus action, you can expend one use of your Bardic Inspiration to grant
    yourself a wondrous appearance. When you do so, choose a number of
    creatures you can see and that can see you within 60 feet of you, up to a
    number equal to your Charisma modifier (mini mum of one). Each of them
    gains 5 temporary hit points. When a creature gains these temporary hit
    points, it can immediately use its reaction to move up to its speed,
    without provoking opportunity attacks. The number of temporary hit points
    inoreases when you reach certain levels in this class, increasing to 8 at
    5th level, 11 at 10th level, and 14 at 15th level.

    """
    _name = "Mantle of Inspiration"
    source = "Bard (College of Glamour)"

    @property
    def name(self):
        level = self.owner.Bard.level
        hp = 5 + 3*(level // 5)
        return self._name + " ({:d}HP)".format(hp)
    

class EnthrallingPerformance(Feature):
    """Starting at 3rd level, you can charge your performance with seductive, fey
    magic. If you perform for at least 1 minute, you can attempt to inspire
    wonder in your audience by singing, reciting a poem, or dancing. At the end
    of the performance, choose a number of humanoids within 60 feet ofyou who
    watched and listened to all of it, up to a number equal tO your Charisma
    modifier (minimum of one). Each target must succeed on a Wisdom saving
    throw against your spell save DC or be charmed by you. While charmed in
    this way, the target idolizes you, it speaks glowingly Of you to anyone who
    talks to it, and it hinders anyone who Opposes you, although it avoids
    violence unless it was already inclined to fight on your behalf. This
    effect ends on a target after 1 hour, if it takes any damage, if you attack
    it, or if it witnesses you attacking or damaging any of its allies.

    If a target succeeds on its saving throw, the target has no hint that you
    tried to charm it. Once you use this feature, you can’t use it again until
    you finish a short or long rest

    """
    name = "Enthralling Performance"
    source = "Bard (College of Glamour)"


class MantleOfMajesty(Feature):
    """At 6th level, you gain the ability to cloak yourself in a fey magic that
    makes Others want to serve you. As a bonus action, you cast command,
    without expending a spell slot, and you take on an appearance of unearthly
    beauty for 1 minute or until your concentration ends (as if you were
    concentrating on a spell). During this time, you can cast command as a
    bonus action on each of your turns, without expending a spell slot.

    Any creature charmed by you automatically failfs its saving throw against
    the command you cast with this feature. Once you use this feature, you
    can’t use it again until you finish a long rest

    """
    name = "Mantle of Majesty"
    source = "Bard (College of Glamour)"


class UnbreakableMajesty(Feature):
    """At 14th level, your appearance permanently gains an otherworldly aspect that
    makes you look more lovely and fierce. In addition, as a bonus action, you
    can assume a magically majestic presence for 1 minute or until you are
    incapacitated. For the duration, whenever any creature tries to attack you
    for the first time on a turn, the at— tacker must make a Charisma saving
    throw against your spell save DC. On a failed save, it can’t attack you on
    this turn, and it must choose a new target for its attack or the attack is
    wasted.

    On a successful save, it can attack you on this turn, but it has
    disadvantage on any saving throw it makes against your spells on your next
    turn. Once you assume this majestic presence, you can’t do so again until
    you finish a short or long rest.

    """
    name = "Unbreakable Majesty"
    source = "Bard (College of Glamour)"


# College of Swords
class SwordsProficiency(Feature):
    """When you join the College of Swords at 3rd level, you gain proficiency with
    medium armor and the scimitar. If you‘re proficient with a simple or
    martial melee weapon, you can use it as a spellcasting focus for your hard
    spells

    """
    name = "Bonus Proficiencies"
    source = "Bard (College of Swords)"


class BardFightingStyle(FeatureSelector):
    """
    Select a Fighting Style by choosing in feature_choices:

    dueling

    two-weapon fighting
    """
    options = {'dueling': Dueling,
               'two-weapon fighting': TwoWeaponFighting,
               'two-weapon': TwoWeaponFighting,
               'dual wield': TwoWeaponFighting}
    name = "Fighting Style (Select One)"
    source = "Bard (College of Swords)"


class BladeFlourish(Feature):
    """At 3rd level, you learn to perform impressive displays of martial prowess
    and speed. Whenever you take the Attack action on your turn, your walking
    speed increases by 10 feet until the end of the turn, and if a weapon
    attack that you make as part of this action hits a creature, you can use
    one of the following Blade Flourish options of your choice. You can use
    only one Blade Flourish option per turn.

    **Defensive Flourish**: You can expend one use of your Bardic Inspiration
    to cause the weapon to deal extra damage to the target you hit. The damage
    equals the number you roll on the Bardic Inspiration die. You also add the
    number rolled to your AC until the start ofyour next turn.

    **Slashing Flourish**: You can expend one use ofyour Bardic Inspiration to
    cause the weapon to deal extra damage to the target you hit and to any
    other creature ofyour choice that you can see within 5 feet ofyou. The
    damage equalsthe number you roll on the Bardic Inspi— ration die.

    **Mobile Flourish**: You can expend one use ofyour Bar— dic InSpiration to
    cause the weapon to deal extra dam— age to the target you hit. The damage
    equals the number you roll on the Bardic Inspiration die. You can also push
    the target up to 5 feet away from you, plus a number of feet equal to the
    number you roll on that die. You can then immediately use your reaction to
    move up to your walking speed to an unoccupied space within 5 feet of the
    target.

    """
    name = "Blade Flourish"
    source = "Bard (College of Swords)"


class MastersFlourish(Feature):
    """Starting at 14th level, whenever you use a Blade Flourish option, you can
    roll a d6 and use it instead of expend— ing a Bardic Inspiration die.
    """
    name = "Master's Flourish"
    source = "Bard (College of Swords)"


# College of Whispers
class PsychicBlades(Feature):
    """When you join the College of Whispers at 3rd level, you gain the ability to
    make your weapon attacks magically toxic to a creature’s mind. When you hit
    a creature with a weapon attack, you can expend one use ofyour Bardic
    Inspiration to deal an extra 2d6 psychic damage to that target. You can do
    so only once per round on your turn. The psychic damage increases when you
    reach certain levels in this class, increasing to 3d6 at 5th level, 5d6
    at 10th level, and 8d6 at 15th level.
    
    """
    _name = "Psychic Blades"
    source = "Bard (College of Whispers)"

    @property
    def name(self):
        level = self.owner.Bard.level
        dice = ' (2d6)'
        if level >= 5:
            dice = ' (3d6)'
        if level >= 10:
            dice = ' (5d6)'
        if level >= 15:
            dice = ' (8d6)'
        return self._name + dice


class WordsOfTerror(Feature):
    """At 3rd level, you learn to infuse innocent-seeming words with an insidious
    magic that can inspire terror. If you speak to a humanoid alone for at
    least 1 minute, you can attempt to seed paranoia in its mind. At the end of
    the conversation, the target must succeed on a Wisdom saving throw against
    your spell save DC or be frightened of you or another creature ofyour
    choice. The target is frightened in this way for 1 hour, until it is at—
    tacked or damaged, or until it witnesses its allies being attacked or
    damaged.
    
    If the target succeeds on its saving throw, the target has no hint that you
    tried to frighten it. Once you use this feature, you can't use it again
    until you finish a short or long rest.

    """
    name = "Words of Terror"
    source = "Bard (College of Whispers)"


class MantleOfWhispers(Feature):
    """At 6th level, you gain the ability to adopt a humanoid’s persona. When a
    humanoid dies within 30 feet of you, you can magically capture its shadow
    using your reac— tion. You retain this shadow until you use it or you
    finish a long rest. You can use the shadow as an action. When you do so, it
    vanishes, magically transforming into a disguise that appears on you. You
    now look like the dead person, but healthy and alive.This disguise lasts
    for 1 hour or until you end it as a bonus action.

    While you’re in the disguise, you gain access to all information that the
    humanoid would freely share with a casual acquaintance. Such information
    includes general details on its background and personal life, but doesn’t
    include secrets. The information is enough that you can pass yourself off
    as the person by drawing on its memories. Another creature can see through
    this disguise by succeeding on a Wisdom (Insight) check contested by your
    Charisma (Deception) check. You gain a +5 bonus to your check. Once you
    capture a shadow with this feature, you can’t capture another one with it
    until you finish a short or long rest.

    """
    name = "Mantle of Whispers"
    source = "Bard (College of Whispers)"


class ShadowLore(Feature):
    """At 14th level, you gain the ability to weave dark magic into your words and
    tap into a creature’s deepest fears. As an action, you magically whisper a
    phrase that only one creature ofyour choice within 30 feet of you can
    hear. The target must make a Wisdom saving throw against your spell save
    DC. It automatically succeeds if it doesn’t share a language with you or if
    it can’t hear you. On a successful saving throw, your whisper sounds like
    unintelligible mumbling and has no effect.

    On a failed saving throw, the target is charmed by you for the next 8 hours
    or until you or your allies attack it, damage it, or force it to make a
    saving throw. It interprets the whispers as a description of its most
    mortifying secret. You gain no knowledge of this secret, but the target
    is convinced you know it. The charmed creature obeys your commands for fear
    that you will reveal its secret. It won’t risk its life for you or fight
    for you, unless it was already inclined to do so. It grants you favors and
    gifts it would offer to a close friend. When the effect ends, the creature
    has no understanding of why it held you in such fear. Once you use this
    feature, you can’t use it again until / you finish a long rest.

    """
    name = "Shadow Lore"
    source = "Bard (College of Whispers)"
