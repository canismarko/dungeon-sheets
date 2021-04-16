from dungeonsheets import spells
from dungeonsheets.features.features import Feature


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
    one spell slot and gain a number of sorcery points equal to the slot's
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

    name = "Sorcerous Restoration"
    source = "Sorceror"


# Metamagic
class CarefulSpell(Metamagic):
    """When you cast a spell that forces other creatures to make a saving throw,
    you can protect some of those creatures from the spell's full force. To do
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
    """When you cast a spell that targets only one creature and doesn't have a
    range of self, you can spend a number of sorcery points equal to the
    spell's level to target a second creature in range with the same spell (1
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
    choice) to the creature's roll. You can do so after the creature rolls but
    before any effects of the roll occur.

    """

    name = "Bend Luck"
    source = "Sorceror (Wild Magic)"


class ControlledChaos(Feature):
    """At 14th level, you gain a modicum of control over the surges of your wild
    magic. Whenever you roll on the Wild Magic Surge table, you can roll twice
    and use either number.

    """

    name = "Controlled Chaos"
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
    scales. When you aren't wearing armor, your AC equals 13 + your Dexterity
    modifier.

    This bonus is computed in the AC given on the Character Sheet above.

    """

    name = "Draconic Resilience"
    source = "Sorceror (Draconic Bloodline)"


class DragonAncestor(Feature):
    """At 1st level, you choose one type of dragon as your ancestor. The damage
    type associated with each dragon is used by features you gain later

    Dragon : Damage

    Black : Acid

    Blue : Lightning

    Brass : Fire

    Bronze : Lightning

    Copper : Acid

    Gold : Fire

    Green : Poison

    Red : Fire

    Silver : Cold

    White : Cold

    You can speak, read, and write Draconic. Additionally, whenever you make a
    Charisma check when interacting with dragons, your proficiency bonus is
    doubled if it applies to the check.

    """

    name = "Dragon Ancestor"
    source = "Sorceror (Draconic Bloodline)"


class ElementalAffinity(Feature):
    """Starting at 6th level, when you cast a spell that deals damage of the type
    associated with your draconic ancestry, add your Charisma modifier to that
    damage. At the same time, you can spend 1 sorcery point to gain resistance
    to that damage type for 1 hour

    """

    name = "Elemental Affinity"
    source = "Sorceror (Draconic Bloodline)"


class ElementalAdept(Feature):
    """When you gain this feat, choose one of the following damage types: acid,
    cold, fire, lightning, or thunder. Spells you cast ignore resistance to damage
    of the chosen type. In addition, when you roll damage for a spell you cast
    that deals damage of that type, you can treat any 1 on a damage die as a 2.
    You can select this feat multiple times. Each time you do so, you must choose
    a different damage type.

    """

    name = "Elemental Adept"
    source = "Sorceror (Feats)"


class DragonWings(Feature):
    """At 14th level, you gain the ability to sprout a pair of dragon wings from
    your back, gaining a flying speed equal to your current speed. You can
    create these wings as a bonus action on your turn. They last until you
    dismiss them as a bonus action on your turn. You can't manifest your wings
    while wearing armor unless the armor is made to accommodate them, and
    clothing not made to accommodate your wings might be destroyed when you
    manifest them

    """

    name = "Dragon Wings"
    source = "Sorceror (Draconic Bloodline)"


class DraconicPresence(Feature):
    """Beginning at 18th level, you can channel the dread presence of your dragon
    ancestor, causing those around you to become awestruck or frightened. As an
    action, you can spend 5 sorcery points to draw on this power and exude an
    aura of awe or fear (your choice) to a distance of 60 feet. For 1 minute or
    until you lose your concentration (as if you were casting a concentration
    spell), each hostile creature that starts its turn in this aura must
    succeed on a Wisdom saving throw or be charmed (if you chose awe) or
    frightened (if you chose fear) until the aura ends. A creature that
    succeeds on this saving throw is immune to your aura for 24 hours.

    """

    name = "Draconic Presence"
    source = "Sorceror (Draconic Bloodline)"


# Divine Soul
class DivineMagic(Feature):
    """Your link to the divine allows you to learn spells from the cleric
    class. When your Spellcasting feature lets you learn or replace a sorcerer
    cantrip or a sorcerer spell of 1st level or higher, you can choose the new
    spell from the cleric spell list or the sorcerer spell list. You must
    otherwise obey all the restrictions for selecting the spell, and it becomes
    a sorcerer spell for you.

    In addition, choose an affinity for the source of your divine power: good,
    evil, law, chaos, or neutrality. You learn an additional spell based on
    that affinity, as shown below. It is a sorcerer spell for you, but it
    doesn't count against your number of sorcerer spells known. If you later
    replace this spell, you must replace it with a Spell from the cleric spell
    list

    Good : Cure Wounds

    Evil : Inflict Wounds

    Law : Bless

    Chaos : Bane

    Neutrality : Protection from Evil and Good

    """

    name = "Divine Magic"
    source = "Sorceror (Divine Soul)"


class FavoredByTheGods(Feature):
    """Starting at 1st level, divine power guards your destiny. If you fail a
    saving throw or miss with an attack roll, you can roll 2d4 and add it to
    the total, possibly changing

    """

    name = "Favored by the Gods"
    source = "Sorceror (Divine Soul)"


class EmpoweredHealing(Feature):
    """Starting at 6th level, the divine energy coursing through you can empower
    healing spells. Whenever you or an ally within 5 feet of you rolls dice to
    determine the number of hit points a spell restores, you can spend 1
    sorcery point to reroll any number of those dice once, provided you aren't
    incapacitated. You can use this feature only once per turn.

    """

    name = "Empowered Healing"
    source = "Sorceror (Divine Soul)"


class OtherworldlyWings(Feature):
    """Starting at 14th level, you can use a bonus action to manifest a pair of
    spectral wings from your back. While the wings are present, you have a
    flying speed of 30 feet. The wings last until you're incapacitated, you
    die, or you dismiss them as a bonus action. The affinity you chose for your
    Divine Magic feature determines the appearance of the spectral wings: eagle
    wings for good or law, bat wings for evil or chaos, and dragonfly wings for
    neutrality

    """

    name = "Otherworldly Wings"
    source = "Sorceror (Divine Soul)"


class UnearthlyRecovery(Feature):
    """At 18th level, you gain the ability to overcome grievous injuries. As a
    bonus action when you have fewer than half of your hit points remaining,
    you can regain a number of hit points equal to half your hit point
    maximum. Once you use this feature, you can't use it again until you finish
    a long rest

    """

    name = "Unearthly Recovery"
    source = "Sorceror (Divine Soul)"


class EyesOfTheDark(Feature):
    """Starting at lst level, you have darkvision with a range of 120 feet. When
    you reach 3rd level in this class, you learn the darkness spell, which
    doesn't count against your number of sorcerer spells known. In addition,
    you can cast it by spending 2 sorcery points or by expending a spell
    slot. If you cast it with sorcery points, you can see through the darkness
    created by the spell.

    """

    name = "Eyes of the Dark"
    source = "Sorceror (Shadow Magic)"
    spells_known = (spells.Darkness,)
    spells_prepared = (spells.Darkness,)


class StrengthOfTheGrave(Feature):
    """Starting at lst level, your existence in a twilight state between life
    and death makes you difficult to defeat. When damage reduces you to 0 hit
    points, you can make a Charisma saving throw (DC 5 + the damage taken). On
    a success, you instead drop to 1 hit point. You can't use this feature if
    you are reduced to 0 hit points by radiant damage or by a critical
    hit. After the saving throw succeeds, you can't use this feature again
    until you finish a long rest

    """

    name = "Strength of the Grave"
    source = "Sorceror (Shadow Magic)"


class HoundOfIllOmen(Feature):
    """At 6th level, you gain the ability to call forth a howling creature of
    darkness to harass your foes. As a bonus action, you can spend 3 sorcery
    points to magically summon a hound of ill omen to target one creature you
    can see within 120 feet of you. The hound uses the dire wolf's statistics
    (see the Monster Manual or appendix C in the Player's Handbook), with the
    following changes:

    - The hound is size Medium, not Large, and it counts as a
      monstrosity, not a beast.
    - It appears with a number of temporary hit points equal to half
      your sorcerer level.
    - It can move through other creatures and objects as if they were
      difficult terrain. The bound takes 5 force damage if it ends its
      turn inside an object.
    - At the start of its turn, the hound automatically knows its
      target's location. If the target was hidden, it is no longer
      hidden from the hound.

    The hound appears in an unoccupied space of your choice within 30
    feet of the target. Roll initiative for the hound. On its turn, it
    can move only toward its target by the most direct route, and it
    can use its action only to attack its target. The hound can make
    opportunity attacks but only against its target. Additionally,
    while the hound is within 5 feet of the target, the target has
    disadvantage on saving throws against any spell you cast. The
    hound disappears if it is reduced to 0 hit points, if its target
    is reduced to 0 hit points, or after 5 minutes.

    """

    name = "Hound of Ill Omen"
    source = "Sorceror (Shadow Magic)"


class ShadowWalk(Feature):
    """At 14th level, you gain the ability to step from one shadow into
    another. When you are in dim light or darkness, as a bonus action, you
    can magically teleport up to 120 feet to an unoccupied space you can see
    that is also in dim light or darkness

    """

    name = "Shadow Walk"
    source = "Sorceror (Shadow Magic)"


class UmbralForm(Feature):
    """Starting at 18th level, you can spend 6 sorcery points as a bonus action to
    magically transform yourself into a shadowy form. In this form, you have
    resistance to all damage except force and radiant damage, and you can move
    through other creatures and objects as if they were difficult terrain. You
    take 5 force damage if you end your turn inside an object. You remain in
    this form for 1 minute. It ends early if you are incapacitated, if you die,
    or if you dismiss it as a bonus action.

    """

    name = "Umbral Form"
    source = "Sorceror (Shadow Magic)"


# Storm Sorcery
class TempestuousMagic(Feature):
    """Starting at 1st level, you can use a bonus action on your turn to cause
    whirling gusts of elemental air to briefly surround you, immediately before
    or after you cast a spell of 1st level or higher. Doing so allows you to
    fly up to 10 feet without provoking opportunity attacks

    """

    name = "Tempestuous Magic"
    source = "Sorceror (Storm Sorcery)"


class HeartOfTheStorm(Feature):
    """At 6th level, you gain resistance to lightning and thunder damage. In
    addition, whenever you start casting a spell of 1st level or higher that
    deals lightning or thunder damage, stormy magic erupts from you. This
    eruption causes creatures ofyour choice that you can see within 10 feet of
    you to take lightning or thunder damage (choose each time this ability
    activates) equal to half your sorcerer level.

    """

    name = "Heart of the Storm"
    source = "Sorceror (Storm Sorcery)"


class StormGuide(Feature):
    """At 6th level, you gain the ability to subtly control the weather around
    you. Ifit is raining, you can use an action to cause the rain to stop
    falling in a 20-foot-radius sphere centered on you. You can end this effect
    as a bonus action. If it is windy, you can use a bonus action each round to
    choose the direction that the wind blows in a IOO-foot-radius sphere
    centered on you. The wind blows in that direction until the end ofyour next
    turn. This feature doesn't alter the speed of the wind.

    """

    name = "Storm Guide"
    source = "Sorceror (Storm Sorcery)"


class StormsFury(Feature):
    """Starting at 14th level, when you are hit by a melee attack, you can use
    your reaction to deal lightning damage to the attacker. The damage equals
    your sorcerer level. The attacker must also make a Strength saving throw
    against your sorcerer spell save DC. On a failed save, the attacker is
    pushed in a straight line up to 20 feet away from you.

    """

    name = "Storm's Fury"
    source = "Sorceror (Storm Sorcery)"


class WindSoul(Feature):
    """At 18th level, you gain immunity to lightning and thunder damage. You also
    gain a magical flying speed of 60 feet. As an action. you can reduce your
    flying speed to 30 feet for 1 hour and choose a number of creatures within
    30 feet ofyou equal to 3 + your Charisma modifier. The chosen creatures
    gain a magical flying speed of 30 feet for 1 hour. Once you reduce your
    flying speed in this way, you can't do so again until you finish a short or
    long rest

    """

    name = "Wind Soul"
    source = "Sorceror (Storm Sorcery)"
