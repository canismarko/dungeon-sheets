from dungeonsheets import spells
from dungeonsheets.features.features import Feature


# Cleric Features
class ChannelDivinity(Feature):
    """At 2nd level, you gain the ability to channel divine energy directly from
    your deity, using that energy to fuel magical effects. You start with two
    such effects: Turn Undead and an effect determined by your domain. Some
    domains grant you additional effects as you advance in levels, as noted in
    the domain description.

    When you use your Channel Divinity, you choose which effect to create. You
    must then finish a short or long rest to use your Channel Divinity again.

    Some Channel Divinity effects require saving throws.  When you use such an
    effect from this class, the DC equals your cleric spell save DC.

    Beginning at 6th level, you can use your Channel Divinity twice between
    rests, and beginning at 18th level you can use it three times between
    rests. When you finish a short or long rest, you regain your expended uses.

    """

    _name = "Channel Divinity"
    source = "Cleric"

    @property
    def name(self):
        level = self.owner.Cleric.level
        if level < 6:
            return "Channel Divinity (1x/SR)"
        elif level < 18:
            return "Channel Divinity (2x/SR)"
        else:
            return "Channel Divinity (3x/SR)"


class TurnUndead(Feature):
    """As an action, you present your holy symbol and speak a prayer censuring the
    undead. Each undead that can see or hear you within 30 feet of you must
    make a Wisdom saving throw. If the creature fails its saving throw, it is
    turned for 1 minute or until it takes any damage.

    A turned creature must spend its turns trying to move as far away from you
    as it can, and it can't willingly move to a space within 30 feet of you. It
    also can't take reactions. For its action, it can use only the Dash action
    or try to escape from an effect that prevents it from moving. If there's
    nowhere to move, the creature can use the Dodge action.

    """

    name = "Channel Divinity: Turn Undead"
    source = "Cleric"


class DestroyUndead(Feature):
    """Starting at 5th level, when an undead fails its saving throw against your
    Turn Undead feature, the creature is instantly destroyed if its challenge
    rating is at or below a certain threshold, as shown in the Destroy Undead
    table.

    """

    _name = "Destroy Undead"
    source = "Cleric"

    @property
    def name(self):
        level = self.owner.Cleric.level
        name = self._name + " (CR 1/2)"
        if level >= 8:
            name = self._name + " (CR 1)"
        if level >= 11:
            name = self._name + " (CR 2)"
        if level >= 14:
            name = self._name + " (CR 3)"
        if level >= 17:
            name = self._name + " (CR 4)"
        return name


class DivineIntervention(Feature):
    """Beginning at 10th level, you can call on your deity to intervene on your
    behalf when your need is great.

    Imploring your deity's aid requires you to use your action. Describe the
    assistance you seek, and roll percentile dice. If you roll a number equal
    to or lower than your cleric level, your deity intervenes. The DM chooses
    the nature of the intervention; the effect of any cleric spell or cleric
    domain spell would be appropriate.

    If your deity intervenes, you can't use this feature again for 7
    days. Otherwise, you can use it again after you finish a long rest.

    At 20th level, your call for intervention succeeds automatically, no roll
    required.

    """

    name = "Divine Intervention"
    source = "Cleric"


class DivineStrike(Feature):
    """
    Generic Divine Strike
    """

    _name = "Divine Strike"
    source = "Cleric"

    @property
    def name(self):
        level = self.owner.Cleric.level
        damage = " (1d8)"
        if level >= 14:
            damage = " (2d8)"
        return self._name + damage


# Knowledge Domain
class BlessingsOfKnowledge(Feature):
    """At 1st level, you learn two languages of your choice. You also become
    proficient in your choice o f two of the following skills: Arcana, History,
    Nature, or Religion. Your proficiency bonus is doubled for any ability
    check you make that uses either of those skills.

    """

    name = "Blessings of Knowledge"
    source = "Cleric (Knowledge Domain)"


class KnowledgeOfTheAncients(DivineIntervention):
    """Starting at 2nd level, you can use your Channel Divinity to tap into a
    divine well o f knowledge. As an action, you choose one skill or tool. For
    10 minutes, you have proficiency with the chosen skill or tool.

    """

    name = "Divine Intervention: Knowledge of the Ancients"
    source = "Cleric (Knowledge Domain)"


class ReadThoughts(DivineIntervention):
    """At 6th level, you can use your Channel Divinity to read a creature's
    thoughts. You can then use your access to the creature's mind to command
    it.  As an action, choose one creature that you can see within 60 feet of
    you. That creature must make a Wisdom saving throw. If the creature
    succeeds on the saving throw, you can't use this feature on it again until
    you finish a long rest.

    If the creature fails its save, you can read its surface thoughts (those
    foremost in its mind, reflecting its current emotions and what it is
    actively thinking about) when it is within 60 feet of you. This effect
    lasts for 1 minute. During that time, you can use your action to end this
    effect and cast the suggestion spell on the creature without expending a
    spell slot. The target automatically fails its saving throw against the
    spell.

    """

    name = "Divine Intervention: Read Thoughts"
    source = "Cleric (Knowledge Domain)"


class PotentSpellcasting(Feature):
    """Starting at 8th level, you add your W isdom modifier to the damage you deal
    with any cleric cantrip.

    """

    name = "Potent Spellcasting"
    source = "Cleric"


class VisionsOfThePast(Feature):
    """Starting at 17th level, you can call up visions of the past that relate to
    an object you hold or your immediate surroundings. You spend at least 1
    minute in meditation and prayer, then receive dreamlike, shadowy glimpses
    of recent events. You can meditate in this way for a number of minutes
    equal to your Wisdom score and must maintain concentration during that
    time, as if you were casting a spell. Once you use this feature, you can't
    use it again until you finish a short or long rest.

    **Object Reading**: Holding an object as you meditate, you can see visions
    of the object's previous owner. After meditating for 1 minute, you learn
    how the owner acquired and lost the object, as well as the most recent
    significant event involving the object and that owner. If the object was
    owned by another creature in the recent past (within a number of days equal
    to your Wisdom score), you can spend 1 additional minute for each owner to
    learn the same information about that creature.

    **Area Reading**: As you meditate, you see visions of recent events in your
    immediate vicinity (a room, street, tunnel, clearing, or the like, up to a
    50-foot cube), going back a number of days equal to your Wisdom score. For
    each minute you meditate, you learn about one significant event, beginning
    with the most recent. Significant events typically involve powerful
    emotions, such as battles and betrayals, marriages and murders, births and
    funerals. However, they might also include more mundane events that are
    nevertheless important in your current situation.

    """

    name = "Visions of the Past"
    source = "Cleric (Knowledge Domain)"


# Life Domain
class DiscipleOfLife(Feature):
    """Also starting at 1st level, your healing spells are more
    effective. Whenever you use a spell of 1st level or higher to restore hit
    points to a creature, the creature regains additional hit points equal to 2
    + the spell's level

    """

    name = "Disciple of Life"
    source = "Cleric (Life Domain)"


class PreserveLife(ChannelDivinity):
    """Starting at 2nd level, you can use your Channel Divinity to heal the badly
    injured. As an action, you present your holy symbol and evoke healing
    energy that can restore a number of hit points equal to five times your
    cleric level. Choose any creatures within 30 feet of you, and divide those
    hit points among them. This feature can restore a creature to no more than
    half of its hit point maximum. You can't use this feature on an undead or a
    construct.

    """

    name = "Channel Divinity: Preserve Life"
    source = "Cleric (Life Domain)"


class BlessedHealer(Feature):
    """Beginning at 6th level, the healing spells you cast on others heal you as
    well. When you cast a spell of 1st level or higher that restores hit points
    to a creature other than you, you regain hit points equal to 2 + the
    spell's level.

    """

    name = "Blessed Healer"
    source = "Cleric (Life Domain)"


class DivineStrikeLife(DivineStrike):
    """At 8th level, you gain the ability to infuse your weapon strikes with
    divine energy. Once on each o f your turns when you hit a creature with a
    weapon attack, you can cause the attack to deal an extra 1d8 radiant damage
    to the target. When you reach 14th level, the extra damage increases to
    2d8.

    """

    source = "Cleric (Life Domain)"


class SupremeHealing(Feature):
    """Starting at 17th level, when you would normally roll one or more dice to
    restore hit points with a spell, you instead use the highest number
    possible for each die. For example, instead of restoring 2d6 hit points to
    a creature, you restore 12.

    """

    name = "Supreme Healing"
    source = "Cleric (Life Domain)"


# Light Domain
class WardingFlare(Feature):
    """At 1st level, you can interpose divine light between yourself and an
    attacking enemy. When you are attacked by a creature within 30 feet of you
    that you can see, you can use your reaction to impose disadvantage on the
    attack roll, causing light to flare before the attacker before it hits or
    misses. An attacker that can't be blinded is immune to this feature. You
    can use this feature a number of times equal to your Wisdom modifier (a
    minimum of once). You regain all expended uses when you finish a long rest

    """

    _name = "Warding Flare"
    source = "Cleric (Light Domain)"

    @property
    def name(self):
        times = max(1, self.owner.wisdom.modifier)
        return self._name + " ({:d}x/LR)".format(times)


class RadianceOfTheDawn(ChannelDivinity):
    """Starting at 2nd level, you can use your Channel Divinity to harness
    sunlight, banishing darkness and dealing radiant damage to your foes. As an
    action, you present your holy symbol, and any magical darkness within 30
    feet of you is dispelled.

    Additionally, each hostile creature within 30 feet of you must make a
    Constitution saving throw. A creature takes radiant damage equal to 2d10 +
    your cleric level on a failed saving throw, and half as much damage on a
    successful one. A creature that has total cover from you is not affected.

    """

    name = "Channel Divinity: Radiance of the Dawn"
    source = "Cleric (Light Domain)"


class ImprovedFlare(Feature):
    """Starting at 6th level, you can also use your Warding Flare feature when a
    creature that you can see within 30 feet o f you attacks a creature other
    than you.

    """

    name = "Improved Flare"
    source = "Cleric (Light Domain)"


class CoronaOfLight(Feature):
    """Starting at 17th level, you can use your action to activate an aura of
    sunlight that lasts for 1 minute or until you dismiss it using another
    action. You emit bright light in a 60-foot radius and dim light 30 feet
    beyond that. Your enemies in the bright light have disadvantage on saving
    throws against any spell that deals fire or radiant damage

    """

    name = "Corona of Light"
    source = "Cleric (Light Domain)"


# Nature Domain
class AcolyteOfNature(Feature):
    """At 1st level, you learn one druid cantrip of your choice. You also gain
    proficiency in one of the following skills of your choice: Animal Handling,
    Nature, or Survival.

    """

    name = "Acolyte of Nature"
    source = "Cleric (Nature Domain)"


class CharmAnimalsAndPlants(ChannelDivinity):
    """Starting at 2nd level, you can use your Channel Divinity to charm animals
    and plants. As an action, you present your holy symbol and invoke the name
    of your deity. Each beast or plant creature that can see you within 30 feet
    of you must make a Wisdom saving throw.

    If the creature fails its saving throw, it is charmed by you for 1 minute
    or until it takes damage. While it is charmed by you, it is friendly to you
    and other creatures you designate.

    """

    name = "Channel Divinity: Charm Animals and Plants"
    source = "Cleric (Nature Domain)"


class DampenElements(Feature):
    """Starting at 6th level, when you or a creature within 30 feet of you takes
    acid, cold, fire, lightning, or thunder damage, you can use your reaction
    to grant resistance to the creature against that instance of the damage.

    """

    name = "Dampen Elements"
    source = "Cleric (Nature Domain)"


class DivineStrikeNature(DivineStrike):
    """At 8th level, you gain the ability to infuse your weapon strikes with
    divine energy. Once on each of your turns when you hit a creature with a
    weapon attack, you can cause the attack to deal an extra 1d8 cold, fire, or
    lightning damage (your choice) to the target. When you reach 14th level,
    the extra damage increases to 2d8.

    """

    source = "Cleric (Nature Domain)"


class MasterOfNature(Feature):
    """At 17th level, you gain the ability to command animals and plant
    creatures. While creatures are charmed by your Charm Animals and Plants
    feature, you can take a bonus action on your turn to verbally command what
    each of those creatures will do on its next turn.

    """

    name = "Master of Nature"
    source = "Cleric (Nature Domain)"


# Tempest Domain
class WrathOfTheStorm(Feature):
    """Also at 1st level, you can thunderously rebuke attackers. When a creature
    within 5 feet of you that you can see hits you with an attack, you can use
    your reaction to cause the creature to make a Dexterity saving throw. The
    creature takes 2d8 lightning or thunder damage (your choice) on a failed
    saving throw, and half as much damage on a successful one.

    You can use this feature a number of times equal to your Wisdom modifier (a
    minimum of once). You regain all expended uses when you finish a long rest.

    """

    _name = "Wrath of the Storm"
    source = "Cleric (Tempest Domain)"

    @property
    def name(self):
        num_uses = max(1, self.owner.wisdom.modifier)
        return self._name + " ({:d}x/LR)".format(num_uses)


class DestructiveWrath(ChannelDivinity):
    """Starting at 2nd level, you can use your Channel Divinity to wield the power
    of the storm with unchecked ferocity.

    When you roll lightning or thunder damage, you can use your Channel
    Divinity to deal maximum damage, instead of rolling.

    """

    name = "Channel Divinity: Destructive Wrath"
    source = "Cleric (Tempest Domain)"


class ThunderboltStrike(Feature):
    """At 6th level, when you deal lightning damage to a Large or smaller
    creature, you can also push it up to 10 feet away from you.

    """

    name = "Thunderbolt Strike"
    source = "Cleric (Tempest Domain)"


class DivineStrikeTempest(DivineStrike):
    """At 8th level, you gain the ability to infuse your weapon strikes with
    divine energy. Once on each of your turns when you hit a creature with a
    weapon attack, you can cause the attack to deal an extra 1d8 thunder damage
    to the target. When you reach 14th level, the extra damage increases to
    2d8.

    """

    source = "Cleric (Tempest Domain)"


class Stormborn(Feature):
    """At 17th level, you have a flying speed equal to your current walking speed
    whenever you are not underground or indoors.

    """

    name = "Stormborn"
    source = "Cleric (Tempest Domain)"


# Trickery Domain
class BlessingOfTheTrickster(Feature):
    """Starting when you choose this domain at 1st level, you can use your action
    to touch a willing creature other than yourself to give it advantage on
    Dexterity (Stealth) checks. This blessing lasts for 1 hour or until you use
    this feature again

    """

    name = "Blessing of the Trickster"
    source = "Cleric (Trickery Domain)"


class InvokeDuplicity(ChannelDivinity):
    """Starting at 2nd level, you can use your Channel Divinity to create an
    illusory duplicate o f yourself. As an action, you create a perfect
    illusion of yourself that lasts for 1 minute, or until you lose your
    concentration (as if you were concentrating on a spell). The illusion
    appears in an unoccupied space that you can see within 30 feet of you. As a
    bonus action on your turn, you can move the illusion up to 30 feet to a
    space you can see, but it must remain within 120 feet of you.

    For the duration, you can cast spells as though you were in the illusion's
    space, but you must use your own senses. Additionally, when both you and
    your illusion are within 5 feet of a creature that can see the illusion,
    you have advantage on attack rolls against that creature, given how
    distracting the illusion is to the target.

    """

    name = "Channel Divinity: Invoke Duplicity"
    source = "Cleric (Trickery Domain)"


class CloakOfShadows(ChannelDivinity):
    """Starting at 6th level, you can use your Channel Divinity to vanish. As an
    action, you become invisible until the end of your next turn. You become
    visible if you attack or cast a spell.

    """

    name = "Channel Divinity: Cloak of Shadows"
    source = "Cleric (Trickery Domain)"


class DivineStrikeTrickery(DivineStrike):
    """At 8th level, you gain the ability to infuse your weapon strikes with
    poison-a gift from your deity. Once on each of your turns when you hit a
    creature with a weapon attack, you can cause the attack to deal an extra
    1d8 poison damage to the target. When you reach 14th level, the extra
    damage increases to 2d8.

    """

    source = "Cleric (Trickery Domain)"


class ImprovedDuplicity(Feature):
    """At 17th level, you can create up to four duplicates of yourself, instead of
    one, when you use Invoke Duplicity. As a bonus action on your turn, you can
    move any number of them up to 30 feet, to a maximum range of 120 feet.

    """

    name = "Improved Duplicity"
    source = "Cleric (Trickery Domain)"


# War Domain
class WarPriest(Feature):
    """From 1st level, your god delivers bolts of inspiration to you while you are
    engaged in battle. When you use the Attack action, you can make one weapon
    attack as a bonus action. You can use this feature a number of times equal
    to your Wisdom modifier (a minimum of once). You regain all expended uses
    when you finish a long rest

    """

    _name = "War Priest"
    source = "Cleric (War Domain)"

    @property
    def name(self):
        num = max(1, self.owner.wisdom.modifier)
        return self._name + " ({:d}x/LR)".format(num)


class GuidedStrike(ChannelDivinity):
    """Starting at 2nd level, you can use your Channel Divinity to strike with
    supernatural accuracy. When you make an attack roll, you can use your
    Channel Divinity to gain a +10 bonus to the roll. You make this choice
    after you see the roll, but before the DM says whether the attack hits or
    misses

    """

    name = "Channel Divinity: Guided Strike"
    source = "Cleric (War Domain)"


class WarGodsBlessing(ChannelDivinity):
    """At 6th level, when a creature within 30 feet of you makes an attack roll,
    you can use your reaction to grant that creature a +10 bonus to the roll,
    using your Channel Divinity. You make this choice after you see the roll,
    but before the DM says whether the attack hits or misses.

    """

    name = "Channel Divinity: War Gods Blessing"
    source = "Cleric (War Domain)"


class DivineStrikeWar(DivineStrike):
    """At 8th level, you gain the ability to infuse your weapon strikes with
    divine energy. Once on each of your turns when you hit a creature with a
    weapon attack, you can cause the attack to deal an extra 1d8 damage of the
    same type dealt by the weapon to the target. When you reach 14th level, the
    extra damage increases to 2d8.
    """

    source = "Cleric (War Domain)"


class AvatarOfBattle(Feature):
    """At 17th level, you gain resistance to bludgeoning, piercing, and slashing
    damage from nonmagical weapons.

    """

    name = "Avatar of Battle"
    source = "Cleric (War Domain)"


# Arcana Domain
class ArcaneInitiate(Feature):
    """When you choose this domain at 1st level, you gain proficiency in the
    Arcana skill, and you gain two cantrips of your choice from the wizard
    spell list. For you, these cantrips count as cleric cantrips

    """

    name = "Arcane Initiate"
    source = "Cleric (Arcana Domain)"


class ArcaneAbjuration(ChannelDivinity):
    """Starting at 2nd level, you can use your Channel Divinity to abjure
    otherworldly creatures. As an action, you present your holy symbol, and one
    celestial, elemental, fey, or fiend of your choice that is within 30 feet
    of you must make a Wisdom saving throw, provided that the creature can see
    or hear you. If the creature fails its saving throw, it is turned for 1
    minute or until it takes any damage.

    A turned creature must spend its turns trying to move as far away from you
    as it can, and it can't willingly end its move in a space within 30 feet of
    you. It also can't take reactions. For its action, it can only use the Dash
    action or try to escape from an effect that prevents it from moving. If
    there's nowhere to move, the creature can use the Dodge action.

    After you reach 5th level, when a creature fails its saving throw against
    your Arcane Abjuration feature, the creature is banished for 1 minute (as
    in the banishment spell, no concentration required) if it isn't on its
    plane of origin and its challenge rating is at or below a certain
    threshold, as shown on the Arcane Banishment table.

    5th level : CR 1/2
    8th level : CR 1
    11th level : CR 2
    14th level : CR 3
    17th level : CR 4

    """

    name = "Channel Divinity: Arcane Abjuration"
    source = "Cleric (Arcana Domain)"


class SpellBreaker(Feature):
    """Starting at 6th level, when you restore hit points to an ally with a spell
    of 1st level or higher, you can also end one spell of your choice on that
    creature. The level of the spell you end must be equal to or lower than the
    level of the spell slot you use to cast the healing spell

    """

    name = "Spell Breaker"
    source = "Cleric (Arcana Domain)"


class ArcaneMastery(Feature):
    """At 17th level, you choose four spells from the wizard spell list, one from
    each of the following levels: 6th, 7th, 8th, and 9th. You add them to your
    list of domain spells. Like your other domain spells, they are always
    prepared and count as cleric spells for you.

    """

    name = "Arcane Mastery"
    source = "Cleric (Arcana Domain)"


# Forge Domain
class BlessingOfTheForge(Feature):
    """At 1st level, you gain the ability to imbue magic into a weapon or
    armor. At the end of a long rest, you can touch one nonmagical object that
    is a suit of armor or a simple or martial weapon. Until the end of your
    next long rest or until you die, the object becomes a magic item, granting
    a +1 bonus to AC if it's armor or a +1 bo- nus to attack and damage rolls
    if it's a weapon. Once you use this feature, you can't use it again until
    you finish a long rest

    """

    name = "Blessing of the Forge"
    source = "Cleric (Forge Domain)"


class ArtisansBlessing(Feature):
    """Starting at 2nd level, you can use your Channel Divinity to create simple
    items. You conduct an hour-long ritual that crafts a nonmagi- cal item that
    must include some metal: a simple or martial weapon, a suit of armor, ten
    pieces of ammunition, a set of tools, or another metal Object (see chapter
    5, "Equipment," in the Player's Handbook for examples of these items). The
    creation is completed at the end of the hour, coalescing in an unoccupied
    space of your choice on a surface within 5 feet of you. The thing you
    create can be something that is worth no more than 100 gp.

    As part of this ritual, you must lay out metal, which can include coins,
    with a value equal to the creation. The metal irretrievably coalesces and
    transforms into the creation at the ritual's end, magically forming even
    nonmetal parts of the creation. The ritual can create a duplicate of a
    nonmagical item that contains metal, such as a key, if you possess the
    original during the ritual.

    """

    name = "Channel Divinity: Artisans Blessing"
    source = "Cleric (Forge Domain)"


class SoulOfTheForge(Feature):
    """Starting at 6th level, your mastery of the forge grants you special
    abilities:

    • You gain resistance to fire damage.

    • While wearing heavy armor, you gain a +1 bonus to AC.

    """

    name = "Soul of the Forge"
    source = "Cleric (Forge Domain)"


class DivineStrikeForge(DivineStrike):
    """At 8th level, you gain the ability to infuse your weapon strikes
    with the fiery power of the forge. Once on each ofyour turns when
    you hit a creature with a weapon attack, you can cause the attack
    to deal an extra 1d8 fire damage to the target. When you reach
    14th level, the extra damage increases to 2d8

    """

    source = "Cleric (Forge Domain)"


class SaintOfForgeAndFire(Feature):
    """At 17th level, your blessed affinity with fire and metal becomes
    more powerful:

    - You gain immunity to fire damage.
    - While wearing heavy armor, you have resistance to bludgeoning,
      piercing, and slashing damage from non-magical attacks

    """

    name = "Saint of Forge and Fire"
    source = "Cleric (Forge Domain)"


# Grave Domain
class CircleOfMortality(Feature):
    """At 1st level, you gain the ability to manipulate the line between life and
    death. When you would normally roll one or more dice to restore hit points
    with a spell to a creature at 0 hit points, you instead use the highest
    number possible for each die. In addition, you learn the spare the dying
    cantrip, which doesn't count against the number of cleric cantrips you
    know. For you, it has a range of 30 feet, and you can cast it as a bonus
    action

    """

    spells_known = (spells.SpareTheDying,)
    spells_prepared = (spells.SpareTheDying,)
    name = "Circle of Mortality"
    source = "Cleric (Grave Domain)"


class EyesOfTheGrave(Feature):
    """At lst level, you gain the ability to occasionally sense the presence of the
    undead, whose existence is an insult to the natural cycle of life. As an
    action, you can open your awareness to magically detect undead. Until the
    end ofyour next turn, you know the location of any undead within 60 feet of
    you that isn't behind total cover and that isn't protected from divination
    magic.

    This sense doesn't tell you anything about a creature's capabilities or
    identity. You can use this feature a number of times equal to your Wisdom
    modifier (minimum Of once). You regain all expended uses when you finish a
    long rest

    """

    _name = "Eyes of the Grave"
    source = "Cleric (Grave Domain)"

    @property
    def name(self):
        num = max(1, self.owner.wisdom.modifier)
        return self._name + " ({:d}x/LR)".format(num)


class PathToTheGrave(ChannelDivinity):
    """Starting at 2nd level, you can use your Channel Divinity to mark another
    creature's life force for termination. As an action, you choose one
    creature you can see within 30 feet of you, cursing it until the end Of
    your next turn. The next time you or an ally Ofyours hits the cursed
    creature with an attack, the creature has vulnerability tO all of that
    attack's damage, and then the curse ends

    """

    name = "Channel Divinity: Path to the Grave"
    source = "Cleric (Grave Domain)"


class SentinelAtDeathsDoor(Feature):
    """At 6th level, you gain the ability to impede death's progress. As a
    reaction when you or a creature you can see within 30 feet of you suffers a
    critical hit, you can turn that hit into a normal hit. Any effects
    triggered by a critical hit are canceled. You can use this feature a
    number of times equal to your Wisdom modifier (minimum of once). You regain
    all expended uses when you finish a long rest.

    """

    _name = "Sentinel at Death's Door"
    source = "Cleric (Grave Domain)"

    @property
    def name(self):
        num = max(1, self.owner.wisdom.modifier)
        return self._name + " ({:d}x/LR)".format(num)


class KeeperOfSouls(Feature):
    """Starting at 17th level. you can seize a trace of vitality from a parting
    soul and use it to heal the living. When an enemy you can see dies within
    60 feet of you, you or one creature of your choice that is within 60 feet
    of you regains hit points equal to the enemy's number of Hit Dice. You can
    use this feature only if you aren't incapacitated. Once you use it, you
    can't do so again until the start ofyour next turn.

    """

    name = "Keeper of Souls"
    source = "Cleric (Grave Domain)"


class Reaper(Feature):
    """At 1st level, you learn one necromancy cantrip of your choice from any
    spell list. When you cast a necromancy cantrip that normally targets only
    one creature, the spell can instead target two creatures within range and
    within 5 feet of each other.

    """

    name = "Reaper"
    source = "Cleric (Death Domain)"


class TouchOfDeathCleric(Feature):
    """Starting at 2nd level, you can use Channel Divinity to destroy another
    creature's life force by touch. When you hit a creature with a melee
    attack, you can use Channel Divinity to deal extra necrotic damage to
    the target. The damage equals 5 + twice your cleric level.

    """

    name = "Channel Divinity: Touch of Death"
    source = "Cleric (Death Domain)"


class InescapableDestruction(Feature):
    """Starting at 6th level, your ability to channel negative energy becomes
    more potent. Necrotic damage dealt by your cleric spells and Channel
    Divinity options ignores resistance to necrotic damage

    """

    name = "Inescapable Destruction"
    source = "Cleric (Death Domain)"


class DivineStrikeDeath(DivineStrike):
    """At 8th level, you gain the ability to infuse your weapon strikes with
    necrotic energy. Once on each of your turns when you hit a creature with
    a weapon attack, you can cause the attack to deal an a 1d8 necrotic
    damage to the target. When you reach 14th level, the extra damage
    increases to 2d8.

    """

    source = "Cleric (Death Domain)"


class ImprovedReaper(Feature):
    """Starting at 17th level, when you cast a necromancy spell of 1st through
    5th level that targets only one creature, the spell can instead target two
    creatures within range and within 5 feet of each other. If the spell
    consumes its material components, you must provide them for each target.

    """

    name = "Improved Reaper"
    source = "Cleric (Death Domain)"
