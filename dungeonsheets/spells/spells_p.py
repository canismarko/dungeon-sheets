from dungeonsheets.spells.spells import Spell


class PassWithoutTrace(Spell):
    """A veil of shadows and silence radiates from you, masking you and your companions
    from detection.
    For the duration, each creature you choose within 30 feet of
    you (including you) has a +10 bonus to Dexterity (Stealth) checks and can't be
    tracked except by magical means. A creature that receives this bonus leaves
    behind no tracks or other traces of its passage.
    """

    name = "Pass Without Trace"
    level = 2
    casting_time = "1 action"
    casting_range = "Self"
    components = ("V", "S", "M")
    materials = "Ashes from a burned leaf of mistletoe and a sprig of spruce"
    duration = "Concentration, up to 1 hour"
    ritual = False
    magic_school = "Abjuration"
    classes = ("Druid", "Ranger")


class Passwall(Spell):
    """A passage appears at a point of your choice that you can see on a wooden,
    plaster, or stone surface (such as a wall, a ceiling, or a floor) within range,
    and lasts for the duration. You choose the opening's dimensions: up to 5 feet
    wide, 8 feet tall, and 20 feet deep. The passage creates no instability in a
    structure surrounding it.

    When the opening disappears, any creatures or objects
    still in the passage created by the spell are safely ejected to an unoccupied
    space nearest to the surface on which you cast the spell.
    """

    name = "Passwall"
    level = 5
    casting_time = "1 action"
    casting_range = "30 feet"
    components = ("V", "S", "M")
    materials = "A pinch of sesame seeds"
    duration = "1 hour"
    ritual = False
    magic_school = "Transmutation"
    classes = ("Wizard",)


class PhantasmalForce(Spell):
    """You craft an illusion that takes root in the mind of a creature
    that you can see within range. The target must make an
    Intelligence saving throw. On a failed save, you create a
    phantasmal object, creature, or other visible phenomenon of your
    choice that is no larger than a 10-foot cube and that is
    perceivable only to the target for the duration. This spell has no
    effect on undead or constructs.

    The phantasm includes sound, temperature, and other stimuli, also
    evident only to the creature.

    The target can use its action to examine the phantasm with an
    Intelligence (Investigation) check against your spell save DC. If
    the check succeeds, the target realizes that the phantasm is an
    illusion, and the spell ends.

    While a target is affected by the spell, the target treats the
    phantasm as if it were real. The target rationalizes any illogical
    outcomes from interacting with the phantasm. For example, a target
    attempting to walk across a phantasmal bridge that spans a chasm
    falls once it steps onto the bridge. If the target survives the
    fall, it still believes that the bridge exists and comes up with
    some other explanation for its fall - it was pushed, it slipped,
    or a strong wind might have knocked it off.

    An affected target is so convinced of the phantasm's reality that
    it can even take damage from the illusion. A phantasm created to
    appear as a creature can attack the target. Similarly, a phantasm
    created to appear as fire, a pool of acid, or lava can burn the
    target. Each round on your turn, the phantasm can deal 1d6 psychic
    damage to the target if it is in the phantasm's area or within 5
    feet of the phantasm, provided that the illusion is of a creature
    or hazard that could logically deal damage, such as by
    attacking. The target perceives the damage as a type appropriate
    to the illusion.

    """

    name = "Phantasmal Force"
    level = 2
    casting_time = "1 action"
    casting_range = "60 feet"
    components = ("V", "S", "M")
    materials = "A bit of fleece"
    duration = "Concentration, up to 1 minute"
    ritual = False
    magic_school = "Illusion"
    classes = ("Bard", "Sorcerer", "Wizard")


class PhantasmalKiller(Spell):
    """You tap into the nightmares of a creature you can see within range
    and create an illusory manifestation of its deepest fears, visible
    only to that creature.  The target must make a Wisdom saving
    throw. On a failed save, the target becomes frightened for the
    duration. At the end of each of the target's turns before the
    spell ends, the target must succeed on a Wisdom saving throw or
    take 4d10 psychic damage. On a successful save, the spell ends.

    **At Higher Levels:** When you cast this spell using a spell slot
    of 5th level or higher, the damage increases by 1d10 for each slot
    level above 4th.

    """

    name = "Phantasmal Killer"
    level = 4
    casting_time = "1 action"
    casting_range = "120 feet"
    components = ("V", "S")
    materials = ""
    duration = "Concentration, up to 1 minute"
    ritual = False
    magic_school = "Illusion"
    classes = ("Wizard",)


class PhantomSteed(Spell):
    """A Large quasi-real, horselike creature appears on the ground in an unoccupied
    space of your choice within range. You decide the creature's appearance, but it
    is equipped with a saddle, bit, and bridle. Any of the equipment created by the
    spell vanishes in a puff of smoke if it is carried more than 10 feet away from
    the steed.

    For the duration, you or a creature you choose can ride the steed.
    The creature uses the statistics for a riding horse, except it has a speed of
    100 feet and can travel 10 miles in an hour, or 13 miles at a fast pace. When
    the spell ends, the steed gradually fades, giving the rider 1 minute to
    dismount. The spell ends if you use an action to dismiss it or if the steed
    takes any damage.
    """

    name = "Phantom Steed"
    level = 3
    casting_time = "1 minute"
    casting_range = "30 feet"
    components = ("V", "S")
    materials = ""
    duration = "1 hour"
    ritual = True
    magic_school = "Illusion"
    classes = ("Wizard",)


class PlanarAlly(Spell):
    """You beseech an otherworldly entity for aid.
    The being must be known to you: a
    god, a primordial, a demon prince, or some other being of cosmic power. That
    entity sends a celestial, an elemental, or a fiend loyal to it to aid you,
    making the creature appear in an unoccupied space within range. If you know a
    specific creature's name, you can speak that name when you cast this spell to
    request that creature, though you might get a different creature anyway (DM's
    choice).

    When the creature appears, it is under no compulsion to behave in any
    particular way. You can ask the creature to perform a service in exchange for
    payment, but it isn't obliged to do so. The requested task could range from
    simple (fly us across the chasm, or help us fight a battle) to complex (spy on
    our enemies, or protect us during our foray into the dungeon). You must be able
    to communicate with the creature to bargain for its services.

    Payment can take
    a variety of forms. A celestial might require a sizable donation of gold or
    magic items to an allied temple, while a fiend might demand a living sacrifice
    or a gift of treasure. Some creatures might exchange their service for a quest
    undertaken by you.

    As a rule of thumb, a task that can be measured in minutes
    requires a payment worth 100 gp per minute. A task measured in hours requires
    1,000 gp per hour. And a task m easured in days (up to 10 days) requires 10,000
    gp per day. The DM can adjust these payments based on the circumstances under
    which you cast the spell. If the task is aligned with the creature's ethos, the
    payment might be halved or even waived. Nonhazardous tasks typically require
    only half the suggested payment, while especially dangerous tasks might require
    a greater gift. Creatures rarely accept tasks that seem suicidal.

    After the
    creature completes the task, or when the agreed-upon duration of service
    expires, the creature returns to its home plane after reporting back to you, if
    appropriate to the task and if possible. If you are unable to agree on a price
    for the creature's service, the creature immediately returns to its home plane.


    A creature enlisted to join your group counts as a member of it, receiving a
    full share of experience points awarded.
    """

    name = "Planar Ally"
    level = 6
    casting_time = "10 minutes"
    casting_range = "60 feet"
    components = ("V", "S")
    materials = ""
    duration = "Instantaneous"
    ritual = False
    magic_school = "Conjuration"
    classes = ("Cleric",)


class PlanarBinding(Spell):
    """With this spell, you attempt to bind a celestial, an elemental, a fey, or a
    fiend to your service.
    The creature must be within range for the entire casting
    of the spell. (Typically, the creature is first summoned into the center of an
    inverted magic circle in order to keep it trapped while this spell is cast.) At
    the completion of the casting, the target must make a Charisma saving throw. On
    a failed save, it is bound to serve you for the duration. If the creature w as
    summoned or created by another spell, that spell's duration is extended to match
    the duration of this spell.

    A bound creature must follow your instructions to
    the best of its ability. You might command the creature to accompany you on an
    adventure, to guard a location, or to deliver a message. The creature obeys the
    letter of your instructions, but if the creature is hostile to you, it strives
    to twist your words to achieve its own objectives. If the creature carries out
    your instructions completely before the spell ends, it travels to you to report
    this fact if you are on the same plane of existence. If you are on a different
    plane of existence, it returns to the place where you bound it and remains there
    until the spell ends.

    **At Higher Levels:** When you cast this spell using a spell
    slot of a higher level, the duration increases to:
    10 days with a 6th-level
    slot,
    30 days with a 7th-level slot,
    180 days with an 8th-level slot,
    1 year
    and 1 day with a 9th-level spell slot.
    """

    name = "Planar Binding"
    level = 5
    casting_time = "1 hour"
    casting_range = "60 feet"
    components = ("V", "S", "M")
    materials = "A jewel worth at least 1,000 gp, which the spell consumes"
    duration = "24 hours"
    ritual = False
    magic_school = "Abjuration"
    classes = ("Bard", "Cleric", "Druid", "Wizard")


class PlaneShift(Spell):
    """You and up to eight willing creatures who link hands in a circle are transported
    to a different plane of existence. You can specify a target destination in
    general terms, such as the City of Brass on the Elemental Plane of Fire or the
    palace of Dispater on the second level of the Nine Hells, and you appear in or
    near that destination. If you are trying to reac the City of Brass, for example,
    you might arrive in its Street of Steel, before its Gate of Ashes, or looking
    at the city from across the Sea of Fire, at the DM's discretion.

    Alternatively,
    if you know the sigil sequence of a teleportation circle on another plane of
    existence, this spell can take you to that circle. If the teleportation circle
    is too small to hold all the creatures you transported, they appear in the
    closest unoccupied spaces next to the circle.

    You can use this spell to banish
    an unwilling creature to another plane. Choose a creature within your reach and
    make a melee spell attack against it. On a hit, the creature must make a
    Charisma saving throw. If the creature fails the save, it is transported to a
    random location on the plane of existence you specify. A creature so transported
    must find its own way back to your current plane of existence.
    """

    name = "Plane Shift"
    level = 7
    casting_time = "1 action"
    casting_range = "Touch"
    components = ("V", "S", "M")
    materials = (
        "A forked, metal rod worth at least 250 gp, attuned to a particular plane of"
        " existence"
    )
    duration = "Instantaneous"
    ritual = False
    magic_school = "Conjuration"
    classes = ("Cleric", "Druid", "Sorcerer", "Warlock", "Wizard")


class PlantGrowth(Spell):
    """This spell channels vitality into plants within a specific area. There are two
    possible uses for the spell, granting either immediate or long-term benefits.


    If you cast this spell using 1 action, choose a point within range. All normal
    plants in a 100-foot radius centered on that point become thick and overgrown. A
    creature moving through the area must spend 4 feet of movement for every 1 foot
    it moves.

    You can exclude one or more areas of any size within the spell's
    area from being affected.

    If you cast this spell over 8 hours, you enrich the
    land. All plants in a half-mile radius centered on a point within range become
    enriched for 1 year. The plants yield twice the normal amount of food when
    harvested.
    """

    name = "Plant Growth"
    level = 3
    casting_time = "Special"
    casting_range = "150 feet"
    components = ("V", "S")
    materials = ""
    duration = "Instantaneous"
    ritual = False
    magic_school = "Transmutation"
    classes = ("Bard", "Druid", "Ranger")


class PoisonSpray(Spell):
    """You extend your hand toward a creature you can see within range and project a
    puff of noxious gas from your palm. The creature must succeed on a Constitution
    saving throw or take 1d12 poison damage.

    **At Higher Levels:** This spell's damage
    increases by 1d12 when you reach 5th level (2d12), 11th level (3d12), 17th level
    (4d12).
    """

    name = "Poison Spray"
    level = 0
    casting_time = "1 action"
    casting_range = "10 feet"
    components = ("V", "S")
    materials = ""
    duration = "Instantaneous"
    ritual = False
    magic_school = "Conjuration"
    classes = ("Druid", "Sorcerer", "Warlock", "Wizard")


class Polymorph(Spell):
    """This spell transforms a creature that you can see within range into a new form.
    An unwilling creature must make a Wisdom saving throw to avoid the effect. A
    shapechanger automatically succeeds on this saving throw.

    The transformation
    lasts for the duration, or until the target drops to 0 hit points or dies. The
    new form can be any beast whose challenge rating is equal to or less than the
    target's (or the target's level, if it doesn't have a challenge rating). The
    target's game statistics, including mental ability scores, are replaced by the
    statistics of the chosen beast. It retains its alignment and personality.

    The
    target assumes the hit points of its new form. When it reverts to its normal
    form, the creature returns to the number of hit points it had before it
    transformed. If it reverts as a result of dropping to 0 hit points, any excess
    damage carries over to its normal form. As long as the excess damage doesn't
    reduce the creature's normal form to 0 hit points, it isn't knocked unconscious.


    The creature is limited in the actions it can perform by the nature of its new
    form, and it can't speak, cast spells, or take any other action that requires
    hands or speech.

    The target's gear melds into the new form. The creature can't
    activate, use, wield, or otherwise benefit from any of its equipment. This spell
    can't affect a target that has 0 hit points.
    """

    name = "Polymorph"
    level = 4
    casting_time = "1 action"
    casting_range = "60 feet"
    components = ("V", "S", "M")
    materials = "A caterpillar cocoon"
    duration = "Concentration, up to 1 hour"
    ritual = False
    magic_school = "Transmutation"
    classes = ("Bard", "Druid", "Sorcerer", "Wizard")


class PowerWordHeal(Spell):
    """A wave of healing energy washes over the creature you touch. The target regains
    all its hit points. If the creature is charmed, frightened, paralyzed, or
    stunned, the condition ends. If the creature is prone, it can use its reaction
    to stand up. This spell has no effect on undead or constructs.
    """

    name = "Power Word Heal"
    level = 9
    casting_time = "1 action"
    casting_range = "Touch"
    components = ("V", "S")
    materials = ""
    duration = "Instantaneous"
    ritual = False
    magic_school = "Evocation"
    classes = ("Bard",)


class PowerWordKill(Spell):
    """You utter a word of power that can compel one creature you can see within range
    to die instantly. If the creature you chose has 100 hit points or fewer, it
    dies. Otherwise, the spell has no effect.
    """

    name = "Power Word Kill"
    level = 9
    casting_time = "1 action"
    casting_range = "60 feet"
    components = ("V",)
    materials = ""
    duration = "Instantaneous"
    ritual = False
    magic_school = "Enchantment"
    classes = ("Bard", "Sorcerer", "Warlock", "Wizard")


class PowerWordPain(Spell):
    """You speak a word of power that causes waves of intense pain to assail one
    creature you can see within range. If the target has 100 hit points or fewer, it
    is subject to crippling pain. Otherwise, the spell has no effect on it. A
    target is also unaffected if it is immune to being charmed.
    While the target is
    affected by crippling pain, any speed it has can be no higher than 10 feet. The
    target also has disadvantage on attack rolls, ability checks, and saving throws,
    other than Constitution saving throws. Finally, if the target tries to cast a
    spell, it must first succeed on a Constitution saving throw, or the casting
    fails and the spell is wasted.
    A target suffering this pain can make a
    Constitution saving throw at the end of each of its turns. On a successful save,
    the pain ends.
    """

    name = "Power Word Pain"
    level = 7
    casting_time = "1 action"
    casting_range = "60 feet"
    components = ("V",)
    materials = ""
    duration = "Instantaneous"
    ritual = False
    magic_school = "Enchantment"
    classes = ("Sorcerer", "Warlock", "Wizard")


class PowerWordStun(Spell):
    """You speak a word of power that can overwhelm the mind of one creature you can
    see within range, leaving it dumbfounded. If the target has 150 hit points or
    fewer, it is stunned. Otherwise, the spell has no effect. The stunned target
    must make a Constitution saving throw at the end of each of its turns. On a
    successful save, this stunning effect ends.
    """

    name = "Power Word Stun"
    level = 8
    casting_time = "1 action"
    casting_range = "60 feet"
    components = ("V",)
    materials = ""
    duration = "Instantaneous"
    ritual = False
    magic_school = "Enchantment"
    classes = ("Bard", "Sorcerer", "Warlock", "Wizard")


class PrayerOfHealing(Spell):
    """Up to six creatures of your choice that you can see within range each regain hit
    points equal to 2d8 + your spellcasting ability modifier. This spell has no
    effect on undead or constructs.

    **At Higher Levels:** When you cast this spell
    using a spell slot of 3rd level or higher, the healing increases by 1d8 for each
    slot level above 2nd.
    """

    name = "Prayer Of Healing"
    level = 2
    casting_time = "10 minutes"
    casting_range = "30 feet"
    components = ("V",)
    materials = ""
    duration = "Instantaneous"
    ritual = False
    magic_school = "Evocation"
    classes = ("Cleric",)


class Prestidigitation(Spell):
    """This spell is a minor magical trick that novice spellcasters use for practice.
    You create one of the following magical effects within range:
     -You create an
    instantaneous, harmless sensory effect, such as a shower of sparks, a puff of
    wind, faint musical notes, or an odd odor.
    -You instantaneously light or snuff
    out a candle, a torch, or a small campfire.
    -You instantaneously clean or soil
    an object no larger than 1 cubic foot.
    -You chill, warm, or flavor up to 1
    cubic foot of nonliving material for 1 hour.
    -You make a color, a small mark,
    or a symbol appear on an object or a surface for 1 hour.
    -You create a
    nonmagical trinket or an illusory image that can fit in your hand and that lasts
    until the end of your next turn.
    If you cast this spell multiple times, you
    can have up to three of its non-instantaneous effects active at a time, and you
    can dismiss such an effect as an action.
    """

    name = "Prestidigitation"
    level = 0
    casting_time = "1 action"
    casting_range = "10 feet"
    components = ("V", "S")
    materials = ""
    duration = "Up to 1 hour"
    ritual = False
    magic_school = "Transmutation"
    classes = ("Bard", "Sorcerer", "Warlock", "Wizard")


class PrimalSavagery(Spell):
    """You channel primal magic to cause your teeth or fingernails to sharpen, ready to
    deliver a corrosive attack. Make a melee spell attack against one creature
    within 5 feet of you. On a hit, the target takes 1d10 acid damage. After you
    make the attack, your teeth or fingernails return to normal. The spell's damage
    increases by 1d10 when you reach 5th level (2d10), 11th level (3d10), and 17th
    level (4d10).
    """

    name = "Primal Savagery"
    level = 0
    casting_time = "1 action"
    casting_range = "Self"
    components = ("S",)
    materials = ""
    duration = "Instantaneous"
    ritual = False
    magic_school = "Transmutation"
    classes = ("Druid",)


class PrimordialWard(Spell):
    """You have resistance to acid, cold, fire, lightning, and thunder damage for the
    spell's duration.
    When you take damage of one of those types, you can use your
    reaction to gain immunity to that type
    of damage, including against the
    triggering damage. If you do so, the resistances end, and you have the immunity
    until the end of your next turn, at which time the spell ends.
    """

    name = "Primordial Ward"
    level = 6
    casting_time = "1 action"
    casting_range = "Self"
    components = ("V", "S")
    materials = ""
    duration = "Concentration, up to 1 minute"
    ritual = False
    magic_school = "Abjuration"
    classes = ("Druid",)


class PrismaticSpray(Spell):
    """Eight multicolored rays of light flash from your hand. Each ray is a different
    color and has a different power and purpose. Each creature in a 60-foot cone
    must make a Dexterity saving throw. For each target, roll a d8 to determine
    which color ray affects it.

    1. Red. The target takes 10d6 fire damage on a
    failed save, or half as much damage on a successful one.

    2. Orange. The target
    takes 10d6 acid damage on a failed save, or half as much damage on a successful
    one.

    3. Yellow. The target takes 10d6 lightning damage on a failed save, or
    half as much damage on a successful one.

    4. Green. The target takes 10d6 poison
    damage on a failed save, or half as much damage on a successful one.

    5. Blue.
    The target takes 10d6 cold damage on a failed save, or half as much damage on a
    successful one.

    6. Indigo. On a failed save, the target is restrained. It must
    then make a Constitution saving throw at the end of each of its turns. If it
    successfully saves three times, the spell ends. If it fails its save three
    times, it permanently turns to stone and is subjected to the petrified
    condition. The successes and failures don't need to be consecutive; keep track
    of both until the target collects three of a kind.

    7. Violet. On a failed save,
    the target is blinded. It must then make a Wisdom saving throw at the start of
    your next turn. A successful save ends the blindness. If it fails that save, the
    creature is transported to another plane of existence of the DM's choosing and
    is no longer blinded. (Typically, a creature that is on a plane that isn't its
    home plane is banished home, while other creatures are usually cast into the
    Astral or Ethereal planes.)

    8. Special. The target is struck by two rays. Roll
    twice more, rerolling any 8.
    """

    name = "Prismatic Spray"
    level = 7
    casting_time = "1 action"
    casting_range = "Self (60-foot cone)"
    components = ("V", "S")
    materials = ""
    duration = "Instantaneous"
    ritual = False
    magic_school = "Evocation"
    classes = ("Sorcerer", "Wizard")


class PrismaticWall(Spell):
    """A shimmering, multicolored plane of light forms a vertical opaque
    wall-up to 90 feet long, 30 feet high, and 1 inch thick-centered
    on a point you can see within range. Alternatively, you can shape
    the wall into a sphere up to 30 feet in diameter centered on a
    point you choose within range. The wall remains in place for the
    duration. If you position the wall so that it passes through a
    space occupied by a creature, the spell fails, and your action and
    the spell slot are wasted.

    The wall sheds bright light out to a range of 100 feet and dim
    light for an additional 100 feet. You and creatures you designate
    at the time you cast the spell can pass through and remain near
    the wall without harm. If another creature that can see the wall
    moves to within 20 feet of it or starts its turn there, the
    creature must succeed on a Constitution saving throw or become
    blinded for 1 minute.

    The wall consists of seven layers, each with a different
    color. When a creature attempts to reach into or pass through the
    wall, it does so one layer at a time through all the wall's
    layers. As it passes or reaches through each layer, the creature
    must make a Dexterity saving throw or be affected by that layer's
    properties as described below.

    The wall can be destroyed, also one layer at a time, in order from
    red to violet, by means specific to each layer. Once a layer is
    destroyed, it remains so for the duration of the spell. A rod of
    cancellation destroys a prismatic wall, but an antimagic field has
    no effect on it.

    1. Red. The creature takes 10d6 fire damage on a failed save, or
    half as much damage on a successful one. While this layer is in
    place, nonmagical ranged attacks can't pass through the wall. The
    layer can be destroyed by dealing at least 25 cold damage to it.

    2. Orange. The creature takes 10d6 acid damage on a failed save,
    or half as much damage on a successful one. While this layer is in
    place, magical ranged attacks can't pass through the wall. The
    layer is destroyed by a strong wind.

    3. Yellow. The creature takes 10d6 lightning damage on a failed
    save, or half as much damage on a successful one. This layer can
    be destroyed by dealing at least 60 force damage to it.

    4. Green. The creature takes 10d6 poison damage on a failed save,
    or half as much damage on a successful one. A passwall spell, or
    another spell of equal or greater level that can open a portal on
    a solid surface, destroys this layer.

    5. Blue. The creature takes 10d6 cold damage on a failed save, or
    half as much damage on a successful one. This layer can be
    destroyed by dealing at least 25 fire damage to it.

    6. Indigo. On a failed save, the creature is restrained. It must
    then make a Constitution saving throw at the end of each of its
    turns. If it successfully saves three times, the spell ends. If it
    fails its save three times, it permanently turns to stone and is
    subjected to the petrified condition. The successes and failures
    don't need to be consecutive; keep track of both until the
    creature collects three of a kind. While this layer is in place,
    spells can't be cast through the wall. The layer is destroyed by
    bright light shed by a daylight spell or a similar spell of equal
    or higher level.

    7. Violet. On a failed save, the creature is blinded. It must then
    make a Wisdom saving throw at the start of your next turn. A
    successful save ends the blindness. If it fails that save, the
    creature is transported to another plane of the DM's choosing and
    is no longer blinded. (Typically, a creature that is on a plane
    that isn't its home plane is banished home, while other creatures
    are usually cast into the Astral or Ethereal planes.) This layer
    is destroyed by a dispel magic spell or similar spell of equal or
    higher level that can end spells and magical effects.

    """

    name = "Prismatic Wall"
    level = 9
    casting_time = "1 action"
    casting_range = "60 feet"
    components = ("V", "S")
    materials = ""
    duration = "10 minutes"
    ritual = False
    magic_school = "Abjuration"
    classes = ("Wizard",)


class ProduceFlame(Spell):
    """A flickering flame appears in your hand.
    The flame remains there for the
    duration and harms neither you nor your equipment. The flame sheds bright light
    in a 10-foot radius and dim light for an additional 10 feet. The spell ends if
    you dismiss it as an action or if you cast it again.

    You can also attack with
    the flame, although doing so ends the spell. When you cast this spell, or as an
    action on a later turn, you can hurl the flame at a creature within 30 feet of
    you. Make a ranged spell attack. On a hit, the target takes 1d8 fire damage.

    At
    Higher Levels: This spell's damage increases by 1d8 when you reach 5th level
    (2d8), 11th level (3d8), and 17th level (4d8).
    """

    name = "Produce Flame"
    level = 0
    casting_time = "1 action"
    casting_range = "Self"
    components = ("V", "S")
    materials = ""
    duration = "10 minutes"
    ritual = False
    magic_school = "Conjuration"
    classes = ("Druid",)


class ProgrammedIllusion(Spell):
    """You create an illusion of an object, a creature, or some other visible
    phenomenon within range that activates when a specific condition occurs. The
    illusion is imperceptible until then. It must be no larger than a 30-foot cube,
    and you decide when you cast the spell how the illusion behaves and what sounds
    it makes. This scripted performance can last up to 5 minutes.

    When the
    condition you specify occurs, the illusion springs into existence and performs
    in the manner you described. Once the illusion finishes performing, it
    disappears and remains dormant for 10 minutes. After this time, the illusion can
    be activated again.

    The triggering condition can be as general or as detailed
    as you like, though it must be based on visual or audible conditions that occur
    within 30 feet of the area. For example, you could create an illusion of
    yourself to appear and warn off others who attempt to open a trapped door, or
    you could set the illusion to trigger only when a creature says the correct word
    or phrase.

    Physical interaction with the image reveals it to be an illusion,
    because things can pass through it. A creature that uses its action to examine
    the image can determine that it is an illusion with a successful Intelligence
    (Investigation) check against your spell save DC. If a creature discerns the
    illusion for what it is, the creature can see through the image, and any noise
    it makes sounds hollow to the creature.
    """

    name = "Programmed Illusion"
    level = 6
    casting_time = "1 action"
    casting_range = "120 feet"
    components = ("V", "S", "M")
    materials = "A bit of fleece and jade dust worth at least 25 gp"
    duration = "Until dispelled"
    ritual = False
    magic_school = "Illusion"
    classes = ("Bard", "Wizard")


class ProjectImage(Spell):
    """You create an illusory copy of yourself that lasts for the duration.
    The copy
    can appear at any location within range that you have seen before, regardless of
    intervening obstacles. The illusion looks and sounds like you but is
    intangible. If the illusion takes any damage, it disappears, and the spell ends.


    You can use your action to move this illusion up to twice your speed, and make
    it gesture, speak, and behave in whatever way you choose. It mimics your
    mannerisms perfectly.

    You can see through its eyes and hear through its ears as
    if you were in its space. On your turn as a bonus action, you can switch from
    using its senses to using your own, or back again. While you are using its
    senses, you are blinded and deafened in regard to your own surroundings.


    Physical interaction with the image reveals it to be an illusion, because things
    can pass through it. A creature that uses its action to examine the image can
    determine that it is an illusion with a successful Intelligence (Investigation)
    check against your spell save DC. If a creature discerns the illusion for what
    it is, the creature can see through the image, and any noise it makes sounds
    hollow to the creature.
    """

    name = "Project Image"
    level = 7
    casting_time = "1 action"
    casting_range = "500 miles"
    components = ("V", "S", "M")
    materials = "A small replica of you made from materials worth at least 5 gp"
    duration = "Concentration, up to 1 day"
    ritual = False
    magic_school = "Illusion"
    classes = ("Bard", "Wizard")


class ProtectionFromEnergy(Spell):
    """For the duration, the willing creature you touch has resistance to one damage
    type of your choice: acid, cold, fire, lightning, or thunder.
    """

    name = "Protection From Energy"
    level = 3
    casting_time = "1 action"
    casting_range = "Touch"
    components = ("V", "S")
    materials = ""
    duration = "Concentration, up to 1 hour"
    ritual = False
    magic_school = "Abjuration"
    classes = ("Cleric", "Druid", "Ranger", "Sorcerer", "Wizard")


class ProtectionFromEvilAndGood(Spell):
    """Until the spell ends, one willing creature you touch is protected against
    certain types of creatures: aberrations, celestials, elementals, fey, fiends,
    and undead.

    The protection grants several benefits. Creatures of those types
    have disadvantage on attack rolls against the target. The target also can't be
    charmed, frightened, or possessed by them. If the target is already charmed,
    frightened, or possessed by such a creature, the target has advantage on any new
    saving throw against the relevant effect.
    """

    name = "Protection From Evil And Good"
    level = 1
    casting_time = "1 action"
    casting_range = "Touch"
    components = ("V", "S", "M")
    materials = "Holy water or powdered silver and iron, which the spell consumes"
    duration = "Concentration, up to 10 minutes"
    ritual = False
    magic_school = "Abjuration"
    classes = ("Cleric", "Paladin", "Warlock", "Wizard")


class ProtectionFromPoison(Spell):
    """You touch a creature. If it is poisoned, you neutralize the poison. If more than
    one poison afflicts the target, you neutralize one poison that you know is
    present, or you neutralize one at random.

    For the duration, the target has
    advantage on saving throws against being poisoned, and it has resistance to
    poison damage.
    """

    name = "Protection From Poison"
    level = 2
    casting_time = "1 action"
    casting_range = "Touch"
    components = ("V", "S")
    materials = ""
    duration = "1 hour"
    ritual = False
    magic_school = "Abjuration"
    classes = ("Cleric", "Druid", "Paladin", "Ranger")


class PsychicScream(Spell):
    """You unleash the power of your mind to blast the intellect of up to ten creatures
    of your choice that you can see within range. Creatures that have an
    Intelligence score of 2 or lower are unaffected.
    Each target must make an
    Intelligence saving throw. On a failed save, a target takes 14d6 psychic damage
    and is stunned. On a successful save, a target takes half as much damage and
    isn't stunned. If a target is killed by this damage, its head explodes, assuming
    it has one.
    A stunned target can make an Intelligence saving throw at the end
    of each of its turns. On a successful save, the stunning effect ends.
    """

    name = "Psychic Scream"
    level = 9
    casting_time = "1 action"
    casting_range = "90 feet"
    components = ("S",)
    materials = ""
    duration = "Instantaneous"
    ritual = False
    magic_school = "Enchantment"
    classes = ("Bard", "Sorcerer", "Warlock", "Wizard")


class PurifyFoodAndDrink(Spell):
    """All nonmagical food and drink within a 5-foot-radius sphere centered on a point
    of your choice within range is purified and rendered free of poison and disease.
    """

    name = "Purify Food And Drink"
    level = 1
    casting_time = "1 action"
    casting_range = "10 feet"
    components = ("V", "S")
    materials = ""
    duration = "Instantaneous"
    ritual = True
    magic_school = "Transmutation"
    classes = ("Cleric", "Druid", "Paladin")


class Pyrotechnics(Spell):
    """Choose an area of nonmagical flame that you can see and that fits within a
    5-foot cube within range. You can extinguish the fire in that area, and you
    create either fireworks or smoke when you do so.
    Fireworks. The target explodes
    with a dazzling display of colors. Each creature within 10 feet of the target
    must succeed on a Constitution saving throw or become blinded until the end of
    your next turn.
    Smoke. Thick black smoke spreads out from the target in a
    20-foot radius, moving around corners. The area of the smoke is heavily
    obscured. The smoke persists for 1 minute or until a strong wind disperses it.
    """

    name = "Pyrotechnics"
    level = 2
    casting_time = "1 action"
    casting_range = "60 feet"
    components = ("V", "S")
    materials = ""
    duration = "Instantaneous"
    ritual = False
    magic_school = "Transmutation"
    classes = ("Bard", "Sorcerer", "Wizard")
