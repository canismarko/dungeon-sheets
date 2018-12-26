from .features import Feature


# PHB
class FontOfMagic(Feature):
    """At 2nd level, you tap into a deep wellspring of magic within yourself. This
    wellspring is represented by sorcery points, which allow you to create a
    variety of magical effects.

    **Sorcery Points**: You have sorcery points equal to your Sorceror
    Level. You can never have more sorcery points than shown on the table for
    your level. You regain all spent sorcery points when you finish a long
    rest.

    **Flexible Casting**: You can use your sorcery points to gain additional
    spell slots, or sacrifice spell slots to gain additional sorcery
    points. You learn other ways to use your sorcery points as you reach higher
    levels. You can transform unexpended sorcery points into one spell slot as
    a bonus action on your turn. The Creating Spell Slots table shows the cost
    of creating a spell slot of a given level. You can create spell slots no
    higher in level than 5th. As a bonus action on your turn, you can expend
    one spell slot and gain a number of sorcery points equal to the slot’s
    level.

    1st Level Slot <--> 2 sorcery points

    2nd Level Slot <--> 3 sorcery points

    3rd Level Slot <--> 5 sorcery points

    4th Level Slot <--> 6 sorcery points

    5th Level Slot <--> 7 sorcery points

    """
    name = "Font of Magic"
    source = "Sorceror"


class Metamagic(Feature):
    """At 3rd level, you gain the ability to twist your spells to suit your
    needs. You gain two of the following Metamagic options of your choice. You
    gain another one at 10th and 17th level. You can use only one Metamagic
    option on a spell when you cast it, unless otherwise noted

    """
    name = "Metamagic"
    source = "Sorceror (Metamagic)"


class SorcerousRestoration(Feature):
    """At 20th level, you regain 4 expended sorcery points whenever you finish a
    short rest.

    """


# Metamagic
class CarefulSpell(Metamagic):
    """When you cast a spell that forces other creatures to make a saving throw,
    you can protect some of those creatures from the spell’s full force. To do
    so, you spend 1 sorcery point and choose a number o f those creatures up to
    your Charisma modifier (minimum of one creature). A chosen creature
    automatically succeeds on its saving throw against the spell.

    """
    name = "Careful Spell"


class DistantSpell(Metamagic):
    """When you cast a spell that has a range of 5 feet or greater, you can spend
    1 sorcery point to double the range of the spell. When you cast a spell
    that has a range of touch, you can spend 1 sorcery point to make the range
    of the spell 30 feet

    """
    name = "Distant Spell"


class EmpoweredSpell(Metamagic):
    """When you roll damage for a spell, you can spend 1 sorcery point to reroll a
    number of the damage dice up to your Charisma modifier (minimum of
    one). You must use the new rolls. You can use Empowered Spell even if you
    have already used a different Metamagic option during the casting of the
    spell.

    """
    name = "Empowered Spell"


class ExtendedSpell(Metamagic):
    """When you cast a spell that has a duration of 1 minute or longer, you can
    spend 1 sorcery point to double its duration, to a maximum duration of 24
    hours.

    """
    name = "Extended Spell"


class HeightenedSpell(Metamagic):
    """When you cast a spell that forces a creature to make a saving throw to
    resist its effects, you can spend 3 sorcery points to give one target of
    the spell disadvantage on its first saving throw made against the spell

    """
    name = "Heightened Spell"


class QuickenedSpell(Metamagic):
    """When you cast a spell that has a casting time of 1 action, you can spend 2
    sorcery points to change the casting time to 1 bonus action for this
    casting.

    """
    name = "Quickened Spell"


class SubtleSpell(Metamagic):
    """When you cast a spell, you can spend 1 sorcery point to cast it without any
    somatic or verbal components.

    """
    name = "Subtle Spell"


class TwinnedSpell(Metamagic):
    """When you cast a spell that targets only one creature and doesn’t have a
    range of self, you can spend a number of sorcery points equal to the
    spell’s level to target a second creature in range with the same spell (1
    sorcery point if the spell is a cantrip)

    """
    name = "Twinned Spell"


# Wild Magic
class WildMagicSurge(Feature):
    """Starting when you choose this origin at 1st level, your spellcasting can
    unleash surges of untamed magic. Immediately after you cast a sorcerer
    spell of 1st level or higher, the DM can have you roll a d20. If you roll a
    1, roll on the Wild Magic Surge table to create a random magical effect.

    """
    name = "Wild Magic Surge"
    source = "Sorceror (Wild Magic)"


class TidesOfChaos(Feature):
    """Starting at 1st level, you can manipulate the forces of chance and chaos to
    gain advantage on one attack roll, ability check, or saving throw. Once you
    do so, you must finish a long rest before you can use this feature again.

    Any time before you regain the use of this feature, the DM can have you
    roll on the Wild Magic Surge table immediately after you cast a sorcerer
    spell of 1st level or higher. You then regain the use of this feature.

    """
    name = "Tides of Chaos"
    source = "Sorceror (Wild Magic)"


class BendLuck(Feature):
    """Starting at 6th level, you have the ability to twist fate using your wild
    magic. When another creature you can see makes an attack roll, an ability
    check, or a saving throw, you can use your reaction and spend 2 sorcery
    points to roll 1d4 and apply the number rolled as a bonus or penalty (your
    choice) to the creature’s roll. You can do so after the creature rolls but
    before any effects of the roll occur.

    """
    name = 'Bend Luck'
    source = 'Sorceror (Wild Magic)'


class ControlledChaos(Feature):
    """At 14th level, you gain a modicum of control over the surges of your wild
    magic. Whenever you roll on the Wild Magic Surge table, you can roll twice
    and use either number.

    """
    name = 'Controlled Chaos'
    source = "Sorceror (Wild Magic)"


class SpellBombardment(Feature):
    """Beginning at 18th level, the harmful energy of your spells
    intensifies. When you roll damage for a spell and roll the highest number
    possible on any of the dice, choose one of those dice, roll it again and
    add that roll to the damage. You can use the feature only once per turn.

    """
    name = "Spell Bombardment"
    source = "Sorceror (Wild Magic)"


# Draconic Ancestry
class DraconicResilience(Feature):
    """As magic flows through your body, it causes physical traits of your dragon
    ancestors to emerge. At 1st level, your hit point maximum increases by 1
    and increases by 1 again whenever you gain a level in this class.

    Additionally, parts of your skin are covered by a thin sheen of dragon-like
    scales. When you aren’t wearing armor, your AC equals 13 + your Dexterity
    modifier.

    This bonus is computed in the AC given on the Character Sheet above.

    """
    name = "Draconic Resilience"
    source = "Sorceror (Draconic Bloodline)"
