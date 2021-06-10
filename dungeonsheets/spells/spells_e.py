from dungeonsheets.spells.spells import Spell


class EarthTremor(Spell):
    """You cause a tremor in the ground in a 10-foot radius. Each creature other than
    you in that area must make a Dexterity saving throw. On a failed save, a
    creature takes 1d6 bludgeoning damage and is knocked prone. If the ground in
    that area is loose earth or stone, it becomes difficult terrain until cleared.
    At Higher Levels. When you cast this spell using a spell slot of 2nd level or
    higher, the damage increases by 1d6 for each slot level above 1st.
    """

    name = "Earth Tremor"
    level = 1
    casting_time = "1 action"
    casting_range = "Self (10-foot radius)"
    components = ("V", "S")
    materials = ""
    duration = "Instantaneous"
    ritual = False
    magic_school = "Evocation"
    classes = ("Bard", "Druid", "Sorcerer", "Wizard")


class Earthbind(Spell):
    """Choose one creature you can see within range. Yellow strips of magical energy
    loop around the creature. The target must succeed on a Strength saving throw or
    its flying speed (if any) is reduced to 0 feet for the spell's duration. An
    airborne creature affected by this spell descends at 60 feet per round until it
    reaches the ground or the spell ends.
    """

    name = "Earthbind"
    level = 2
    casting_time = "1 action"
    casting_range = "300 feet"
    components = ("V",)
    materials = ""
    duration = "Concentration, up to 1 minute"
    ritual = False
    magic_school = "Transmutation"
    classes = ("Druid", "Sorcerer", "Warlock", "Wizard")


class Earthquake(Spell):
    """You create a seismic disturbance at a point on the ground that you can see
    within range.
    For the duration, an intense tremor rips through the ground in a
    100-foot- radius circle centered on that point and shakes creatures and
    structures in contact with the ground in that area.

    The ground in the area
    becomes difficult terrain. Each creature on the ground that is concentrating
    must make a Constitution saving throw. On a failed save, the creature's
    concentration is broken.

    When you cast this spell and at the end of each turn
    you spend concentrating on it, each creature on the ground in the area must make
    a Dexterity saving throw. On a failed save, the creature is knocked prone.


    This spell can have additional effects depending on the terrain in the area, as
    determined by the DM.
    Fissures.
    Fissures open throughout the spell's area at
    the start of your next turn after you cast the spell. A total of 1d6 such
    fissures open in locations chosen by the DM. Each is 1d10 x 10 feet deep, 10
    feet wide, and extends from one edge of the spell's area to the opposite side. A
    creature standing on a spot where a fissure opens must succeed on a Dexterity
    saving throw or fall in. A creature that successfully saves moves with the
    fissure's edge as it opens.
    A fissure that opens beneath a structure causes it
    to automatically collapse (see below).

    Structures.
    The tremor deals 50
    bludgeoning damage to any structure in contact with the ground in the area when
    you cast the spell and at the start of each of your turns until the spell ends.
    If a structure drops to 0 hit points, it collapses and potentially damages
    nearby creatures. A creature within half the distance of a structure's height
    must make a Dexterity saving throw. On a failed save, the creature takes 5d6
    bludgeoning damage, is knocked prone, and is buried in the rubble, requiring a
    DC 20 Strength (Athletics) check as an action to escape. The DM can adjust the
    DC higher or lower, depending on the nature of the rubble. On a successful save,
    the creature takes half as much damage and doesn't fall prone or become buried.
    """

    name = "Earthquake"
    level = 8
    casting_time = "1 action"
    casting_range = "500 feet"
    components = ("V", "S", "M")
    materials = "A pinch o f dirt, a piece o f rock, and a lump of clay"
    duration = "Concentration, up to 1 minute"
    ritual = False
    magic_school = "Evocation"
    classes = ("Cleric", "Druid", "Sorcerer")


class EldritchBlast(Spell):
    """A beam of crackling energy streaks toward a creature within range. Make a ranged
    spell attack against the target. On a hit, the target takes 1d10 force damage.


    **At Higher Levels:** The spell creates more than one beam when you reach higher
    levels:
    Two beams at 5th level
    Three beams at 11th level
    Four beams at 17th
    level.
    You can direct the beams at the same target or at different ones. Make
    a separate attack roll for each beam.
    """

    name = "Eldritch Blast"
    level = 0
    casting_time = "1 action"
    casting_range = "120 feet"
    components = ("V", "S")
    materials = ""
    duration = "Instantaneous"
    ritual = False
    magic_school = "Evocation"
    classes = ("Warlock",)


class ElementalBane(Spell):
    """Choose one creature you can see within range, and choose one of the following
    damage types: acid, cold, fire, lightning, or thunder.
    The target must succeed
    on a Constitution saving throw or be affected by the spell for its duration. The
    first time each turn the affected target takes damage of the chosen type, the
    target takes an extra 2d6 damage of that type. Moreover, the target loses any
    resistance to that damage type until the spell ends.

    **At Higher Levels:** When you
    cast this spell using a spell slot of 5th level or higher, you can target one
    additional creature for each slot level above 4th. The creatures must be within
    30 feet of each other when you target them.
    """

    name = "Elemental Bane"
    level = 4
    casting_time = "1 action"
    casting_range = "90 feet"
    components = ("V", "S")
    materials = ""
    duration = "Concentration, up to 1 minute"
    ritual = False
    magic_school = "Transmutation"
    classes = ("Druid", "Wizard", "Warlock")


class ElementalWeapon(Spell):
    """A nonmagical weapon you touch becomes a magic weapon.
    Choose one of the
    following damage types: acid, cold, fire, lightning, or thunder. For the
    duration, the weapon has a +1 bonus to attack rolls and deals an extra 1d4
    damage of the chosen type when it hits.

    **At Higher Levels:** When you cast this
    spell using a spell slot of 5th or 6th level, the bonus to attack rolls
    increases to +2 and the extra damage increases to 2d4.
    When you use a spell
    slot of 7th level or higher, the bonus increases to +3 and the extra damage
    increases to 3d4.
    """

    name = "Elemental Weapon"
    level = 3
    casting_time = "1 action"
    casting_range = "Touch"
    components = ("V", "S")
    materials = ""
    duration = "Concentration, up to 1 hour"
    ritual = False
    magic_school = "Transmutation"
    classes = ("Paladin",)


class EnemiesAbound(Spell):
    """You reach into the mind of one creature you can see and force it to make an
    Intelligence saving throw. A creature automatically succeeds if it is immune to
    being frightened. On a failed save, the target loses the ability to distinguish
    friend from foe, regarding all creatures it can see as enemies until the spell
    ends. Each time the target takes damage, it can repeat the saving throw, ending
    the effect on itself on a success. Whenever the affected creature chooses
    another creature as a target, it must choose the target at random from among the
    creatures it can see within range of the attack, spell, or other ability it's
    using. If an enemy provokes an opportunity attack from the affected creature,
    the creature must make that attack if it is able to.
    """

    name = "Enemies Abound"
    level = 3
    casting_time = "1 action"
    casting_range = "120 feet"
    components = ("V", "S")
    materials = ""
    duration = "Concentration, up to 1 minute"
    ritual = False
    magic_school = "Enchantment"
    classes = ("Bard", "Sorcerer", "Warlock", "Wizard")


class Enervation(Spell):
    """A tendril of inky darkness reaches out from you, touching a creature you can see
    within range to drain life from it. The target must make a Dexterity saving
    throw. On a successful save, the target takes 2d8 necrotic damage, and the spell
    ends. On a failed save, the target takes 4d8 necrotic damage, and until the
    spell ends, you can use your action on each of your turns to automatically deal
    4d8 necrotic damage to the target. The spell ends ifyou use your action to do
    anything else, if the target is ever outside the spell's range, or if the target
    has total cover from you. Whenever the spell deals damage to a target, you
    regain hit points equal to half the amount of necrotic damage the target takes.


    **At Higher Levels:** When you cast this spell using a spell slot of 6th level or
    higher, the damage increases by 1d8 for each slot level above 5th.
    """

    name = "Enervation"
    level = 5
    casting_time = "1 action"
    casting_range = "60 feet"
    components = ("V", "S")
    materials = ""
    duration = "Concentration, up to 1 minute"
    ritual = False
    magic_school = "Necromancy"
    classes = ("Sorcerer", "Warlock", "Wizard")


class EnhanceAbility(Spell):
    """You touch a creature and bestow upon it a magical enhancement. Choose one of the
    following effects: the target gains the effect until the spell ends.
    - Bear's
    Endurance. The target has advantage on Constitution checks. It also gains 2d6
    temporary hit points, which are lost when the spell ends.
    - Bull's Strength. The
    target has advantage on Strength checks, and his or her carrying capacity
    doubles.
    - Cat's Grace. The target has advantage on Dexterity checks. It also
    doesn't take damage from falling 20 feet or less if it isn't incapacitated.
    -
    Eagle's Splendor. The target has advantage on Charisma checks.
    - Fox's Cunning.
    The target thas advantage on Intelligence checks.
    - Owl's Wisdom. The target has
    advantage on Wisdom checks.

    **At Higher Levels:** When you cast this spell using a
    spell slot of 3rd level or higher, you can target one additional creature for
    each slot level above 2nd.
    """

    name = "Enhance Ability"
    level = 2
    casting_time = "1 action"
    casting_range = "Touch"
    components = ("V", "S", "M")
    materials = "Fur or a feather from a beast"
    duration = "Concentration, up to 1 hour"
    ritual = False
    magic_school = "Transmutation"
    classes = ("Bard", "Cleric", "Druid", "Sorcerer")


class Enlargereduce(Spell):
    """You cause a creature or an object you can see within range to grow larger or
    smaller for the duration. Choose either a creature or an object that is neither
    worn nor carried. If the target is unwilling, it can make a Constitution saving
    throw. On a success, the spell has no effect.

    If the target is a creature,
    everything it is wearing and carrying changes size with it. Any item dropped by
    an affected creature returns to normal size at once.

    Enlarge
    The target's
    size doubles in all dimensions, and its weight is multiplied by eight. This
    growth increases its size by one category – from Medium to Large, for example.
    If there isn't enough room for the target to double its size, the creature or
    object attains the maximum possible size in the space available. Until the spell
    ends, the target also has advantage on Strength checks and Strength saving
    throws. The target's weapons also grow to match its new size. While these
    weapons are enlarged, the target's attack with them deal 1d4 extra damage.


    Reduce
    The target's size is halved in all dimensions, and its weight is reduced
    to one-eighth of normal. This reduction decreases its size by one category –
    from Medium to Small, for example. Until the spell ends, the target also has
    disadvantage on Strength checks and Strength saving throws. The target's weapons
    also shrink to match its new size. While these weapons are reduced, the
    target's attacks with them deal 1d4 less damage (this can't reduce the damage
    below 1).
    """

    name = "Enlarge/Reduce"
    level = 2
    casting_time = "1 action"
    casting_range = "30 feet"
    components = ("V", "S", "M")
    materials = "A pinch of powdered iron"
    duration = "Concentration, up to 1 minute"
    ritual = False
    magic_school = "Transmutation"
    classes = ("Sorcerer", "Wizard")


class EnsnaringStrike(Spell):
    """The next time you hit a creature with a weapon attack before this spell ends, a
    writhing mass of thorny vines appears at the point of impact, and the target
    must succeed on a Strength saving throw or be restrained by the magical vines
    until the spell ends. A Large or larger creature has advantage on this saving
    throw. If the target succeeds on the save, the vines shrivel away.

    While
    restrained by this spell, the target takes 1d6 piercing damage at the start of
    each of its turns. A creature restrained by the vines or one that can touch the
    creature can use its action to make a Strength check against your spell save DC.
    On a success, the target is freed.

    **At Higher Levels:** If you cast this spell
    using a spell slot of 2nd level or higher, the damage increases by 1d6 for each
    slot level above 1st.
    """

    name = "Ensnaring Strike"
    level = 1
    casting_time = "1 bonus action"
    casting_range = "Self"
    components = ("V",)
    materials = ""
    duration = "Concentration, up to 1 minute"
    ritual = False
    magic_school = "Conjuration"
    classes = ("Ranger",)


class Entangle(Spell):
    """Grasping weeds and vines sprout from the ground in a 20-foot square starting
    from a point within range. For the duration, these plants turn the ground in the
    area into difficult terrain.

    A creature in the area when you cast the spell
    must succeed on a Strength saving throw or be restrained by the entangling
    plants until the spell ends. A creature restrained by the plants can use its
    action to make a Strength check against your spell save DC. On a success, it
    frees itself.

    When the spell ends, the conjured plants wilt away.
    """

    name = "Entangle"
    level = 1
    casting_time = "1 action"
    casting_range = "90 feet"
    components = ("V", "S")
    materials = ""
    duration = "Concentration, up to 1 minute"
    ritual = False
    magic_school = "Conjuration"
    classes = ("Druid",)


class Enthrall(Spell):
    """You weave a distracting string of words, causing creatures of your choice that
    you can see within range and that can hear you to make a Wisdom saving throw.
    Any creature that can't be charmed succeeds on this saving throw automatically,
    and if you or your companions are fighting a creature, it has advantage on the
    save. On a failed save, the target has disadvantage on Wisdom (Perception)
    checks made to perceive any creature other than you until the spell ends or
    until the target can no longer hear you. The spell ends if you are incapacitated
    or can no longer speak.
    """

    name = "Enthrall"
    level = 2
    casting_time = "1 action"
    casting_range = "60 feet"
    components = ("V", "S")
    materials = ""
    duration = "1 minute"
    ritual = False
    magic_school = "Enchantment"
    classes = ("Bard", "Warlock")


class EruptingEarth(Spell):
    """Choose a point you can see on the ground within range. A fountain of churned
    earth and stone erupts in a 20-foot cube centered on that point. Each creature
    in that area must make a Dexterity saving throw. A creature takes 3d12
    bludgeoning damage on a failed save, or half as much damage on a successful one.
    Additionally, the ground in that area becomes difficult terrain until cleared
    away. Each 5-foot-square portion of the area requires at least 1 minute to clear
    by hand.

    **At Higher Levels:** When you cast this spell using a spell slot of 4rd
    level or higher, the damage increases by 1d12 for each slot level above 3rd.
    """

    name = "Erupting Earth"
    level = 3
    casting_time = "1 action"
    casting_range = "120 feet"
    components = ("V", "S", "M")
    materials = "A piece of obsidian"
    duration = "Instantaneous"
    ritual = False
    magic_school = "Transmutation"
    classes = ("Druid", "Sorcerer", "Wizard")


class Etherealness(Spell):
    """You step into the border regions of the Ethereal Plane, in the area where it
    overlaps with your current plane. You remain in the Border Ethereal for the
    duration or until you use your action to dismiss the spell. During this time,
    you can move in any direction. If you move up or down, every foot of movement
    costs an extra foot. You can see and hear the plan you originated from, but
    everything there looks gray, and you can't see anything more than 60 feet away.


    While on the Ethereal Plane, you can only affect and be affected by other
    creatures on that plane. Creatures that aren't on the Ethereal Plance can't
    perceive you and can't interact with you, unless a special ability or magic has
    given them the ability to do so.

    You ignore all objects and effects that
    aren't on the Ethereal Plane, allowing you to move through objects you perceive
    on the plan you originated from. When the spell ends, you immediately return to
    the plane you originiated from in teh spot you currently occupy. If you occupy
    the same spot as a solid object or creature when this happens, you are
    imediately shunted to the neares unoccupied space that you can occupy and take
    force damage equal to twice the number of feet you are moved.

    This spell has
    no effect if you cast it while you are on the Ethereal Plane or a plane that
    doesn't border it, such as one of the Outer Planes.

    **At Higher Levels:** When you cast this spell using a spell slot
    of 8th level or higher, you can target up to three willing
    creatures (including you) for each slot level above 7th. The
    creatures must be within 10 feet of you when you cast the spell.

    """

    name = "Etherealness"
    level = 7
    casting_time = "1 action"
    casting_range = "Self"
    components = ("V", "S")
    materials = ""
    duration = "Up to 8 hours"
    ritual = False
    magic_school = "Transmutation"
    classes = ("Bard", "Cleric", "Sorcerer", "Warlock", "Wizard")


class EvardsBlackTentacles(Spell):
    """Squirming, ebony tentacles fill a 20-foot square on ground that you can see
    within range. For the duration, these tentacles turn the ground in the area into
    difficult terrain.

    When a creature enters the affected area for the first
    time on a turn or starts its turn there, the creature must succeed on a
    Dexterity saving throw or take 3d6 bludgeoning damage and be restrained by the
    tentacles until the spell ends. A creature that starts its turn in the area and
    is already restrained by the tentacles takes 3d6 bludgeoning damage.

    A
    creature restrained by the tentacles can use its action to make a Strength or
    Dexterity check (its choice) against your spell save DC. On a success, it frees
    itself.
    """

    name = "Evards Black Tentacles"
    level = 4
    casting_time = "1 action"
    casting_range = "90 feet"
    components = ("V", "S", "M")
    materials = "A piece of tentacle from a giant octopus or a giant squid"
    duration = "Concentration, up to 1 minute"
    ritual = False
    magic_school = "Conjuration"
    classes = ("Wizard",)


class ExpeditiousRetreat(Spell):
    """This spell allows you to move at an incredible pace. When you cast this spell,
    and then as a bonus action on each of your turns until the spell ends, you can
    take the Dash action.
    """

    name = "Expeditious Retreat"
    level = 1
    casting_time = "1 bonus action"
    casting_range = "Self"
    components = ("V", "S")
    materials = ""
    duration = "Concentration, up to 10 minutes"
    ritual = False
    magic_school = "Transmutation"
    classes = ("Sorcerer", "Warlock", "Wizard")


class Eyebite(Spell):
    """For the spell's duration, your eyes become an inky void imbued with
    dread power.  One creature of your choice within 60 feet of you
    that you can see must succeed on a Wisdom saving throw or be
    affected by one of the following effects of your choice for the
    duration. On each of your turns until the spell ends, you can use
    your action to target another creature but can't target a creature
    again if it has succeeded on a saving throw against this casting
    of eyebite.

    Asleep
      The target falls unconscious. It wakes up if it takes any damage
      or if another creature uses its action to shake the sleeper
      awake.

    Panicked
      The target is frightened of you. On each of its turns, the
      frightened creature must take the Dash action and move away from
      you by the safest and shortest available route, unless there is
      nowhere to move. If the target moves to a place at least 60 feet
      away from you where it can no longer see you, this effect ends.

    Sickened
      The target has disadvantage on attack rolls and ability
      checks. At the end of each of its turns, it can make another
      Wisdom saving throw. If it succeeds, the effect ends.

    """

    name = "Eyebite"
    level = 6
    casting_time = "1 action"
    casting_range = "Self"
    components = ("V", "S")
    materials = ""
    duration = "Concentration, up to 1 minute"
    ritual = False
    magic_school = "Necromancy"
    classes = ("Bard", "Sorcerer", "Warlock", "Wizard")
