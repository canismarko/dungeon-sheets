from .spells import Spell


class Earthquake(Spell):
    """You create a seismic disturbance at a point on the ground that you
    can see within range. For the duration, an intense tremor rips
    through the ground in a 100-foot-radius circle centered on that
    point and shakes creatures and structures in contact with the
    ground in that area. The ground in the area becomes difficult
    terrain. Each creature on the ground that is concentrating must
    make a Constitution saving throw. On a failed save, the creature’s
    concentration is broken. When you cast this spell and at the end
    of each turn you spend concentrating on it, each creature on the
    ground in the area must make a Dexterity saving throw. On a failed
    save, the creature is knocked prone. This spell can have
    additional effects depending on the terrain in the area, as
    determined by the DM. Fissures. Fissures open throughout the
    spell’s area at the start of your next turn after you cast the
    spell. A total of 1d6 such fissures open in locations chosen by
    the DM. Each is 1d10 × 10 feet deep, 10 feet wide, and extends
    from one edge of the spell’s area to the opposite side. A creature
    standing on a spot where a fissure opens must succeed on a
    Dexterity saving throw or fall in. A creature that successfully
    saves moves with the fissure’s edge as it opens. A fissure that
    opens beneath a structure causes it to automatically collapse (see
    below). Structures. The tremor deals 50 bludgeoning damage to any
    structure in contact with the ground in the area when you cast the
    spell and at the start of each of your turns until the spell
    ends. If a structure drops to 0 hit points, it collapses and
    potentially damages nearby creatures. A creature within half the
    distance of a structure’s height must make a Dexterity saving
    throw. On a failed save, the creature takes 5d6 bludgeoning
    damage, is knocked prone, and is buried in the rubble, requiring a
    DC 20 Strength (Athletics) check as an action to escape. The DM
    can adjust the DC higher or lower, depending on the nature of the
    rubble. On a successful save, the creature takes half as much
    damage and doesn’t fall prone or become buried.
    
    """
    name = "Earthquake"
    level = 8
    casting_time = "1 action"
    components = ('V', 'S', 'M')
    materials = "a pinch of dirt, a piece of rock, and a lump of clay"
    duration = "Concentration, up to 1 minute"
    magic_school = "Evocation"
    classes = ()


class EldritchBlast(Spell):
    """A beam of crackling energy streaks toward a creature within
    range. Make a ranged spell attack against the target. On a hit,
    the target takes 1d10 force damage.
    
    The spell creates more than one beam when you reach higher levels:
    two beams at 5th level, three beams at 11th level, and four beams
    at 17th level. You can direct the beams at the same target or at
    different ones. Make a separate attack roll for each beam.
    Evocation Cantrip
    
    """
    name = 'Eldritch Blast'
    level = 0
    casting_time = "1 action"
    casting_range = "120 feet"
    components = ('V', 'S')
    duration = "Instantaneous"
    magic_school = "Evocation"
    classes = ('Warlock', )


class ElementalWeapon(Spell):
    """A nonmagical weapon you touch becomes a magic weapon. Choose one of
    the following damage types: acid, cold, fire, lightning, or
    thunder. For the duration, the weapon has a +1 bonus to attack
    rolls and deals an extra 1d4 damage of the chosen type when it
    hits.
    
    **At Higher Levels** When you cast this spell using a spell slot
    of 5th or 6th level, the bonus to attack rolls increases to +2 and
    the extra damage increases to 2d4. When you use a spell slot of
    7th level or higher, the bonus increases to +3 and the extra
    damage increases to 3d4.
    
    """
    name = 'Elemental Weapon'
    level = 3
    casting_time = "1 action"
    casting_range = "Touch"
    components = ('V', 'S')
    duration = "Concentration, up to 1 hour"
    magic_school = "Transmutation"
    classes = ('Paladin', )


class Entangle(Spell):
    """Grasping weeds and vines sprout from the ground in a 20-foot square
    starting from a point within range. For the duration, these plants
    turn the ground in the area into difficult terrain.
    
    A creature in the area when you cast the spell must succeed on a
    Strength saving throw or be restrained by the entangling plants
    until the spell ends. A creature restrained by the plants can use
    its action to make a Strength check against your spell save DC. On
    a success, it frees itself.
    
    When the spell ends, the conjured plants wilt away.
    
    """
    level = 1
    name = "Entangle"
    casting_time = "1 action"
    casting_range = "90 ft (20 ft area)"
    components = ("V", "S")
    duration = "Concentration, up to 1 minute"
    magic_school = "Conjuration"
    classes = ('Druid')

    
class Enthrall(Spell):
    """You weave a distracting string of words, causing creatures of your choice
    that you can see within range and that can hear you to make a Wisdom saving
    throw. Any creature that can’t be charmed succeeds on this saving throw
    automatically, and if you or your companions are fighting a creature, it has
    advantage on the save. On a failed save, the target has disadvantage on Wisdom
    (Perception) checks made to perceive any creature other than you until the
    spell ends or until the target can no longer hear you. The spell ends if you
    are incapacitated or can no longer speak.
    
    """
    level = 2
    name = "Enthrall"
    casting_time = '1 action'
    casting_range = '60 feet'
    components = ('V', 'S')
    duration = "1 minute"
    magic_shool = "Enchantment"
    classes = ('Bard', 'Warlock')


class Etherealness(Spell):
    """You step into the border regions of the Ethereal Plane, in the area
    where it overlaps with your current plane. You remain in the
    Border Ethereal for the duration or until you use your action to
    dismiss the spell. During this time, you can move in any
    direction. If you move up or down, every foot of movement costs an
    extra foot. You can see and hear the plane you originated from,
    but everything there looks gray, and you can’t see anything more
    than 60 feet away. While on the Ethereal Plane, you can only
    affect and be affected by other creatures on that plane. Creatures
    that aren’t on the Ethereal Plane can’t perceive you and can’t
    interact with you, unless a special ability or magic has given
    them the ability to do so. You ignore all objects and effects that
    aren’t on the Ethereal Plane, allowing you to move through objects
    you perceive on the plane you originated from. When the spell
    ends, you immediately return to the plane you originated from in
    the spot you currently occupy. If you occupy the same spot as a
    solid object or creature when this happens, you are immediately
    shunted to the nearest unoccupied space that you can occupy and
    take force damage equal to twice the number of feet you are
    moved. This spell has no effect if you cast it while you are on
    the Ethereal Plane or a plane that doesn’t border it, such as one
    of the Outer Planes. At Higher Levels. When you cast this spell
    using a spell slot of 8th level or higher, you can target up to
    three willing creatures (including you) for each slot level above
    7th. The creatures must be within 10 feet of you when you cast the
    spell.
    
    """
    name = "Etherealness"
    level = 7
    casting_time = "1 action"
    components = ('V', 'S')
    materials = ""
    duration = "Up to 8 hours"
    magic_school = "Transmutation"
    classes = ()


class Eyebite(Spell):
    """For the spell's duration, your eyes become an inky void imbued with
    dread power. One creature of your choice within 60 feet of you
    that you can see must succeed on a Wisdom saving throw or be
    affected by one of the following effects of your choice for the
    duration. On each of your turns until the spell ends, you can use
    your action to target another creature but can't target a creature
    again if it has succeeded on a saving throw against this casting
    of **eyebite**.
    
    **Asleep.** The target falls unconscious. It wakes up if it takes
      any damage or if another creature uses its action to shake the
      sleeper awake.
    
    **Panicked.** The target is frightened of you. On each of its
      turns, the frightened creature must take the Dash action and
      move away from you by the safest and shortest available route,
      unless there is nowhere to move. If the target moves to a place
      at least 60 feet away from you where it can no longer see you,
      this effect ends.
    
    **Sickened.** The target has disadvantage on attack rolls and
      ability checks. At the end of each of its turns, it can make
      another Wisdom saving throw. If it succeeds, the effect ends.

    """
    name = "Eyebite"
    level = 6
    casting_time = "1 action"
    casting_range = "Self"
    components = ('V', 'S',)
    materials = ""
    duration = "1 minute"
    magic_school = "Necromancy"
    classes = ('Bard', 'Sorceror', 'Warlock', 'Wizard', )


class FalseLife(Spell):
    """Bolstering yourself with a necromantic facsimile of life, you gain
    1d4+4 temporary hit points for the duration.
    
    At Higher Levels: When you cast this spell using a spell slot of
    2nd level or higher, you gain 5 additional temporary hit points
    for each slot level above 1st.
    
    """
    name = "False Life"
    level = 1
    casting_time = "1 action"
    casting_range = "Self (30 feet)"
    components = ("V", "S", "M")
    materials = "A small amount of alcohol or distilled spirits"
    duration = "1 hour"
    magic_school = "Necromancy"
    classes = ('Sorceror', 'Wizard', )


class FindThePath(Spell):
    """This spell allows you to find the shortest, most direct physical
    route to a specific fixed location that you are familiar with on
    the same plane of existence. If you name a destination on another
    plane of existence, a destination that moves (such as a mobile
    fortress), or a destination that isn’t specific (such as “a green
    dragon’s lair”), the spell fails. For the duration, as long as you
    are on the same plane of existence as the destination, you know
    how far it is and in what direction it lies. While you are
    traveling there, whenever you are presented with a choice of paths
    along the way, you automatically determine which path is the
    shortest and most direct route (but not necessarily the safest
    route) to the destination. Faerie Fire 1st-level evocation Casting
    Time: 1 action Range: 60 feet Components: V Duration:
    Concentration, up to 1 minute Each object in a 20-foot cube within
    range is outlined in blue, green, or violet light (your
    choice). Any creature in the area when the spell is cast is also
    outlined in light if it fails a Dexterity saving throw. For the
    duration, objects and affected creatures shed dim light in a
    10-foot radius. Any attack roll against an affected creature or
    object has advantage if the attacker can see it, and the affected
    creature or object can’t benefit from being invisible.
    
    """
    name = "Find the Path"
    level = 6
    casting_time = "1 minute"
    components = ('V', 'S', 'M')
    materials = "a set of divinatory tools—such as bones, ivory sticks, cards, teeth, or carved runes— worth 100 gp and an object from the location you wish to find"
    duration = "Concentration, up to 1 day"
    magic_school = "Divination"
    classes = ()


class FingerOfDeath(Spell):
    """You send negative energy coursing through a creature that you can
    see within range, causing it searing pain. The target must make a
    Constitution saving throw. It takes 7d8 + 30 necrotic damage on a
    failed save, or half as much damage on a successful one. A
    humanoid killed by this spell rises at the start of your next turn
    as a zombie that is permanently under your command, following your
    verbal orders to the best of its ability.
    
    """
    name = "Finger of Death"
    level = 7
    casting_time = "1 action"
    casting_range = "60 feet"
    components = ('V', 'S')
    materials = ""
    duration = "Instantaneous"
    magic_school = "Necromancy"
    classes = ('Sorceror', 'Warlock', 'Wizard', )


class FireBolt(Spell):
    """You hurl a mote of fire at a creature or object within range. Make
    a ranged spell attack against the target. On a hit, the target
    takes 1d10 fire damage. A flammable object hit by this spell
    ignites if it isn’t being worn or carried. This spell’s damage
    increases by 1d10 when you reach 5th level (2d10), 11th level
    (3d10), and 17th level (4d10).
    
    """
    name = "Fire Bolt"
    level = 0
    casting_time = "1 action"
    components = ('V', 'S')
    materials = ""
    duration = "Instantaneous"
    magic_school = "Evocation"
    classes = ()


class FireStorm(Spell):
    """A storm made up of sheets of roaring flame appears in a location
    you choose within range. The area of the storm consists of up to
    ten 10-foot cubes, which you can arrange as you wish. Each cube
    must have at least one face adjacent to the face of another
    cube. Each creature in the area must make a Dexterity saving
    throw. It takes 7d10 fire damage on a failed save, or half as much
    damage on a successful one. The fire damages objects in the area
    and ignites flammable objects that aren’t being worn or
    carried. If you choose, plant life in the area is unaffected by
    this spell.
    
    """
    name = "Fire Storm"
    level = 7
    casting_time = "1 action"
    components = ('V', 'S')
    materials = ""
    duration = "Instantaneous"
    magic_school = "Evocation"
    classes = ()


class Fireball(Spell):
    """A bright streak flashes from your pointing finger to a point you
    choose within range and then blossoms with a low roar into an
    explosion of flame. Each creature in a 20-foot-radius sphere
    centered on that point must make a Dexterity saving throw. A
    target takes 8d6 fire damage on a failed save, or half as much
    damage on a successful one. The fire spreads around corners. It
    ignites flammable objects in the area that aren’t being worn or
    carried. At Higher Levels. When you cast this spell using a spell
    slot of 4th level or higher, the damage increases by 1d6 for each
    slot level above 3rd.
    
    """
    name = "Fireball"
    level = 3
    casting_time = "1 action"
    components = ('V', 'S', 'M')
    materials = "a tiny ball of bat guano and sulfur"
    duration = "Instantaneous"
    magic_school = "Evocation"
    classes = ()


class FlameStrike(Spell):
    """A vertical column of divine fire roars down from the heavens in a
    location you specify. Each creature in a 10-foot-radius,
    40-foot-high cylinder centered on a point within range must make a
    Dexterity saving throw. A creature takes 4d6 fire damage and 4d6
    radiant damage on a failed save, or half as much damage on a
    successful one. At Higher Levels. When you cast this spell using a
    spell slot of 6th level or higher, the fire damage or the radiant
    damage (your choice) increases by 1d6 for each slot level above
    5th.
    
    """
    name = "Flame Strike"
    level = 5
    casting_time = "1 action"
    components = ('V', 'S', 'M')
    materials = "pinch of sulfur"
    duration = "Instantaneous"
    magic_school = "Evocation"
    classes = ()


class FlamingSphere(Spell):
    """A 5-foot-diameter sphere of fire appears in an unoccupied space of
    your choice within range and lasts for the duration. Any creature
    that ends its turn within 5 feet of the sphere must make a
    Dexterity saving throw. The creature takes 2d6 fire damage on a
    failed save, or half as much damage on a successful one.
    
    As a bonus action, you can move the sphere up to 30 feet. If you
    ram the sphere into a creature, that creature must make the saving
    throw against the sphere’s damage, and the sphere stops moving
    this turn.
    
    When you move the sphere, you can direct it over barriers up to 5
    feet tall and jump it across pits up to 10 feet wide. The sphere
    ignites flammable objects not being worn or carried, and it sheds
    bright light in a 20-foot radius and dim light for an additional
    20 feet.
    
    **At Higher Levels** When you cast this spell using a spell slot
    of 3rd level or higher, the damage increases by 1d6 for each slot
    level above 2nd.
    
    """
    name = "Flaming Sphere"
    level = 2
    casting_time = "1 action"
    casting_range = "60 feet"
    components = ('V', 'S', 'M')
    materials = "a bit of tallow, a pinch of brimstone, and a dusting of powdered iron"
    duration = "Concentration, up to 1 minute"
    magic_school = "Conjuration"
    classes = ('Druid', 'Wizard', )


class Fly(Spell):
    """You touch a willing creature. The target gains a flying speed of 60
    feet for the duration. When the spell ends, the target falls if it
    is still aloft, unless it can stop the fall. At Higher
    Levels. When you cast this spell using a spell slot of 4th level
    or higher, you can target one additional creature for each slot
    level above 3rd.
    
    """
    name = "Fly"
    level = 3
    casting_time = "1 action"
    components = ('V', 'S', 'M')
    materials = "a wing feather from any bird"
    duration = "Concentration, up to 10 minutes"
    magic_school = "Transmutation"
    classes = ()


class FindSteed(Spell):
    """You summon a spirit that assumes the form of an unusually
    intelligent, strong and loyal steed, creating a long lasting bond
    with it. Appearing in an unoccupied space within range, the steed
    takes on a form that you choose: a warhorse, a pony, a camel, an
    elk, or a mastiff. (Your DM might allow other animals to be
    summoned as steeds.) The steed has the statistics of the chosen
    form, though it is a celestial, fey or fiend (your choice) instead
    of its normal type. Additionally if your steed has an intelligence
    of 5 or less, its intelligence becomes 6, and it gains the ability
    to understand one language of your choice that you speak.
    
    The steed serves as a mount, both in combat and out, and you have
    an instinctive bond with it that allows you to fight as a seamless
    unit. While mounted on your steed, you can make any spell you cast
    that targets only you also target your steed.
    
    When the steed drops to 0 hit points, it disappears, leaving
    behind no physical form. You can dismiss your steed at any time as
    an action, causing it to disappear. In either case, casting this
    spell again summons the same steed, restored to its hit point
    maximum.
    
    While the steed is within 1 mile of you, you can communicate with
    it telepathically.
    
    You cannot have more than one steed bonded by this spell at a
    time. As an action, you can release the steed from its bond at any
    time, causing it to disappear.
    
    """
    name = "Find Steed"
    level = 2
    casting_time = "10 minutes"
    components = ('V', 'S')
    duration = "Instantaneous"
    magic_school = "Conjuration"
    classes = ('Paladin', )


class Foresight(Spell):
    """You touch a willing creature and bestow a limited ability to see
    into the immediate future. For the duration, the target can’t be
    surprised and has advantage on attack rolls, ability checks, and
    saving throws. Additionally, other creatures have disadvantage on
    attack rolls against the target for the duration. This spell
    immediately ends if you cast it again before its duration ends.
    
    """
    name = "Foresight"
    level = 9
    casting_time = "1 minute"
    components = ('V', 'S', 'M')
    materials = "a hummingbird feather"
    duration = "8 hours"
    magic_school = "Divination"
    classes = ()


class FreedomOfMovement(Spell):
    """You touch a willing creature. For the duration, the target’s
    movement is unaffected by difficult terrain, and spells and other
    magical effects can neither reduce the target’s speed nor cause
    the target to be paralyzed or restrained. The target can also
    spend 5 feet of movement to automatically escape from nonmagical
    restraints, such as manacles or a creature that has it
    grappled. Finally, being underwater imposes no penalties on the
    target’s movement or attacks.
    
    """
    name = "Freedom of Movement"
    level = 4
    casting_time = "1 action"
    components = ('V', 'S', 'M')
    materials = "a leather strap, bound around the arm or a similar appendage"
    duration = "1 hour"
    magic_school = "Abjuration"
    classes = ()


class Gate(Spell):
    """You conjure a portal linking an unoccupied space you can see within
    range to a precise location on a different plane of existence. The
    portal is a circular opening, which you can make 5 to 20 feet in
    diameter. You can orient the portal in any direction you
    choose. The portal lasts for the duration. The portal has a front
    and a back on each plane where it appears. Travel through the
    portal is possible only by moving through its front. Anything that
    does so is instantly transported to the other plane, appearing in
    the unoccupied space nearest to the portal. Deities and other
    planar rulers can prevent portals created by this spell from
    opening in their presence or anywhere within their domains. When
    you cast this spell, you can speak the name of a specific creature
    (a pseudonym, title, or nickname doesn’t work). If that creature
    is on a plane other than the one you are on, the portal opens in
    the named creature’s immediate vicinity and draws the creature
    through it to the nearest unoccupied space on your side of the
    portal. You gain no special power over the creature, and it is
    free to act as the DM deems appropriate. It might leave, attack
    you, or help you.
    
    """
    name = "Gate"
    level = 9
    casting_time = "1 action"
    components = ('V', 'S', 'M')
    materials = "a diamond worth at least 5,000 gp"
    duration = "Concentration, up to 1 minute"
    magic_school = "Conjuration"
    classes = ()


class GentleRepose(Spell):
    """You touch a corpse or other remains. For the duration, the target
    is protected from decay and can't become undead.
    
    The spell also effectively extends the time limit on raising the
    target from the dead, since days spent under the influence of this
    spell don't count against the time limit of spells such as raise
    dead.
    
    """
    name = "Gentle Repose"
    level = 2
    casting_time = "1 action"
    casting_range = "Touch"
    components = ('V', 'S', 'M')
    materials = "a pinch of salt and one copper piece placed on each of the corpse's eyes, which must remain there for the duration"
    duration = "10 days"
    magic_school = "Necromancy"
    classes = ('Cleric', 'Wizard')

class GlobeOfInvulnerability(Spell):
    """An immobile, faintly shimmering barrier springs into existence in a
    10-foot radius around you and remains for the duration. Any spell
    of 5th level or lower cast from outside the barrier can’t affect
    creatures or objects within it, even if the spell is cast using a
    higher level spell slot. Such a spell can target creatures and
    objects within the barrier, but the spell has no effect on
    them. Similarly, the area within the barrier is excluded from the
    areas affected by such spells. At Higher Levels. When you cast
    this spell using a spell slot of 7th level or higher, the barrier
    blocks spells of one level higher for each slot level above
    6th.
    
    """
    name = "Globe of Invulnerability"
    level = 6
    casting_time = "1 action"
    components = ('V', 'S', 'M')
    materials = "a glass or crystal bead that shatters when the spell ends"
    duration = "Concentration, up to 1 minute"
    magic_school = "Abjuration"
    classes = ()


class GreaterInvisibility(Spell):
    """You or a creature you touch becomes invisible until the spell
    ends. Anything the target is wearing or carrying is invisible as
    long as it is on the target’s person.
    
    """
    name = "Greater Invisibility"
    level = 4
    casting_time = "1 action"
    components = ('V', 'S')
    materials = ""
    duration = "Concentration, up to 1 minute"
    magic_school = "Illusion"
    classes = ()


class GreaterRestoration(Spell):
    """You imbue a creature you touch with positive energy to undo a
    debilitating effect. You can reduce the target’s exhaustion level
    by one, or end one of the following effects on the target: • One
    effect that charmed or petrified the target • One curse, including
    the target’s attunement to a cursed magic item • Any reduction to
    one of the target’s ability scores • One effect reducing the
    target’s hit point maximum
    
    """
    name = "Greater Restoration"
    level = 5
    casting_time = "1 action"
    components = ('V', 'S', 'M')
    materials = "diamond dust worth at least 100 gp, which the spell consumes"
    duration = "Instantaneous"
    magic_school = "Abjuration"
    classes = ()


class GuardianOfFaith(Spell):
    """A Large spectral guardian appears and hovers for the duration in an
    unoccupied space of your choice that you can see within range. The
    guardian occupies that space and is indistinct except for a
    gleaming sword and shield emblazoned with the symbol of your
    deity. Any creature hostile to you that moves to a space within 10
    feet of the guardian for the first time on a turn must succeed on
    a Dexterity saving throw. The creature takes 20 radiant damage on
    a failed save, or half as much damage on a successful one. The
    guardian vanishes when it has dealt a total of 60 damage.
    
    """
    name = "Guardian of Faith"
    level = 4
    casting_time = "1 action"
    components = ('V',)
    materials = ""
    duration = "8 hours"
    magic_school = "Conjuration"
    classes = ()


class Guidance(Spell):
    """You touch one willing creature. Once before the spell ends, the
    target can roll a d4 and add the number rolled to one ability
    check of its choice. It can roll the die before or after making
    the ability check. The spell then ends.
    
    """
    name = "Guidance"
    level = 0
    casting_time = "1 action"
    components = ('V', 'S')
    materials = ""
    duration = "Concentration, up to 1 minute"
    magic_school = "Divination"
    classes = ('Cleric', 'Druid')


class GuidingBolt(Spell):
    """A flash of light streaks toward a creature of your choice within
    range. Make a ranged spell attack against the target. On a hit,
    the target takes 4d6 radiant damage, and the next attack roll made
    against this target before the end of your next turn has
    advantage, thanks to the mystical dim light glittering on the
    target until then. At Higher Levels. When you cast this spell
    using a spell slot of 2nd level or higher, the damage increases by
    1d6 for each slot level above 1st.
    
    """
    name = "Guiding Bolt"
    level = 1
    casting_time = "1 action"
    components = ('V', 'S')
    materials = ""
    duration = "1 round"
    magic_school = "Evocation"
    classes = ()


class Harm(Spell):
    """You unleash a virulent disease on a creature that you can see
    within range. The target must make a Constitution saving throw. On
    a failed save, it takes 14d6 necrotic damage, or half as much
    damage on a successful save. The damage can’t reduce the target’s
    hit points below 1. If the target fails the saving throw, its hit
    point maximum is reduced for 1 hour by an amount equal to the
    necrotic damage it took. Any effect that removes a disease allows
    a creature’s hit point maximum to return to normal before that
    time passes.
    
    """
    name = "Harm"
    level = 6
    casting_time = "1 action"
    components = ('V', 'S')
    materials = ""
    duration = "Instantaneous"
    magic_school = "Necromancy"
    classes = ()


class Haste(Spell):
    """Choose a willing creature that you can see within range. Until the
    spell ends, the target’s speed is doubled, it gains a +2 bonus to
    AC, it has advantage on Dexterity saving throws, and it gains an
    additional action on each of its turns. That action can be used
    only to take the Attack (one weapon attack only), Dash, Disengage,
    Hide, or Use an Object action. When the spell ends, the target
    can’t move or take actions until after its next turn, as a wave of
    lethargy sweeps over it.
    
    """
    name = "Haste"
    level = 3
    casting_time = "1 action"
    components = ('V', 'S', 'M')
    materials = "a shaving of licorice root"
    duration = "Concentration, up to 1 minute"
    magic_school = "Transmutation"
    classes = ()


class Heal(Spell):
    """Choose a creature that you can see within range. A surge of
    positive energy washes through the creature, causing it to regain
    70 hit points. This spell also ends blindness, deafness, and any
    diseases affecting the target. This spell has no effect on
    constructs or undead. At Higher Levels. When you cast this spell
    using a spell slot of 7th level or higher, the amount of healing
    increases by 10 for each slot level above 6th.
    
    """
    name = "Heal"
    level = 6
    casting_time = "1 action"
    components = ('V', 'S')
    materials = ""
    duration = "Instantaneous"
    magic_school = "Evocation"
    classes = ()


class HealingWord(Spell):
    """A creature of your choice that you can see within range regains hit
    points equal to 1d4 + your spellcasting ability modifier. This
    spell has no effect on undead or constructs. At Higher
    Levels. When you cast this spell using a spell slot of 2nd level
    or higher, the healing increases by 1d4 for each slot level above
    1st.
    
    """
    name = "Healing Word"
    level = 1
    casting_time = "1 bonus action"
    components = ('V',)
    materials = ""
    duration = "Instantaneous"
    magic_school = "Evocation"
    classes = ()

    
class HellishRebuke(Spell):
    """Reaction: you are being damaged by a creature within 60 feet of you that you
    can see. You point your finger, and the creature that damaged you is
    momentarily surrounded by hellish flames. The creature must make a
    Dexterity saving throw. It takes 2d10 fire damage on a failed save, or half
    as much damage on a successful one. At higher levels: When you cast this
    spell using a spell slot of 2nd level or higher, the damage increases by
    1dlO for each slot level above 1st.

    """
    name = 'Hellish Rebuke'
    level = 1
    casting_time = '1 reaction'
    components = ('V', 'S')
    materials = ''
    duration = 'Instantaneous'
    magic_school = 'Evolcation'
    classes = ('Warlock',)


class HeroesFeast(Spell):
    """You bring forth a great feast, including magnificent food and
    drink. The feast takes 1 hour to consume and disappears at the end
    of that time, and the beneficial effects don’t set in until this
    hour is over. Up to twelve other creatures can partake of the
    feast. A creature that partakes of the feast gains several
    benefits. The creature is cured of all diseases and poison,
    becomes immune to poison and being frightened, and makes all
    Wisdom saving throws with advantage. Its hit point maximum also
    increases by 2d10, and it gains the same number of hit
    points. These benefits last for 24 hours.
    
    """
    name = "Heroes' Feast"
    level = 6
    casting_time = "10 minutes"
    components = ('V', 'S', 'M')
    materials = "a gem-encrusted bowl worth at least 1,000 gp, which the spell consumes"
    duration = "Instantaneous"
    magic_school = "Conjuration"
    classes = ()


class Hex(Spell):
    """You place a curse on a creature that you can see within range. Until the
    spell ends, you deal an extra 1d6 necrotic damage to the target whenever
    you hit it with an attack. Also, choose one ability when you cast the
    spell. The target has disadvantage on ability checks made with the chosen
    ability. If the target drops to 0 hit points before this spell ends, you
    can use a bonus action on a subsequent turn of yours to curse a new
    creature. A remove curse cast on the target ends this spell early. At
    higher level: When you cast this spell using a spell slot of 3rd or 4th
    level, you can maintain your concentration on the spell for up to 8 hours.
    When you use a spell slot of 5th level or higher, you can maintain your
    concentration on the spell for up to 24 hours."""
    name = 'Hex'
    level = 1
    casting_time = '1 bonus action'
    casting_range = '90 feet'
    components = ('V', 'S', 'M')
    materials = 'The petrified eye of a newt'
    duration = 'Concentration, up to 1 hour'
    magic_school = 'Enchantment'
    classes = ('Warlock',)

    
class HoldPerson(Spell):
    """Choose a humanoid that you can see within range. The target must
    succeed on a Wisdom saving throw or be paralyzed for the
    duration. At the end of each of its turns, the target can make
    another Wisdom saving throw. On a success, the spell ends on the
    target. At Higher Levels. When you cast this spell using a spell
    slot of 3rd level or higher, you can target one additional
    humanoid for each slot level above 2nd. The humanoids must be
    within 30 feet of each other when you target them.
    
    """
    name = "Hold Person"
    level = 2
    casting_time = "1 action"
    components = ('V', 'S', 'M')
    materials = "a small, straight piece of iron"
    duration = "Concentration, up to 1 minute"
    magic_school = "Enchantment"
    classes = ()


class HolyAura(Spell):
    """Divine light washes out from you and coalesces in a soft radiance
    in a 30-foot radius around you. Creatures of your choice in that
    radius when you cast this spell shed dim light in a 5-foot radius
    and have advantage on all saving throws, and other creatures have
    disadvantage on attack rolls against them until the spell ends. In
    addition, when a fiend or an undead hits an affected creature with
    a melee attack, the aura flashes with brilliant light. The
    attacker must succeed on a Constitution saving throw or be blinded
    until the spell ends.
    
    """
    name = "Holy Aura"
    level = 8
    casting_time = "1 action"
    components = ('V', 'S', 'M')
    materials = "a tiny reliquary worth at least 1,000 gp containing a sacred relic, such as a scrap of cloth from a saint’s robe or a piece of parchment from a religious text"
    duration = "Concentration, up to 1 minute"
    magic_school = "Abjuration"
    classes = ()


class IceStorm(Spell):
    """A hail of rock-hard ice pounds to the ground in a 20-foot-radius,
    40-foot-high cylinder centered on a point within range. Each
    creature in the cylinder must make a Dexterity saving throw. A
    creature takes 2d8 bludgeoning damage and 4d6 cold damage on a
    failed save, or half as much damage on a successful
    one. Hailstones turn the storm’s area of effect into difficult
    terrain until the end of your next turn. At Higher Levels. When
    you cast this spell using a spell slot of 5th level or higher, the
    bludgeoning damage increases by 1d8 for each slot level above
    4th.
    
    """
    name = "Ice Storm"
    level = 4
    casting_time = "1 action"
    components = ('V', 'S', 'M')
    materials = "a pinch of dust and a few drops of water"
    duration = "Instantaneous"
    magic_school = "Evocation"
    classes = ()


class Identify(Spell):
    """You choose one object that you must touch throughout the casting of
    the spell. If it is a magic item or some other magic-imbued
    object, you learn its properties and how to use them, whether it
    requires attunement to use, and how many charges it has, if
    any. You learn whether any spells are affecting the item and what
    they are. If the item was created by a spell, you learn which
    spell created it. If you instead touch a creature throughout the
    casting, you learn what spells, if any, are currently affecting
    it.
    
    """
    name = "Identify"
    level = 1
    casting_time = "1 minute"
    components = ('V', 'S', 'M')
    materials = "a pearl worth at least 100 gp and an owl feather"
    duration = "Instantaneous"
    magic_school = "Divination"
    classes = ()


class IllusoryScript(Spell):
    """You write on parchment, paper, or some other suitable writing material and
    imbue it with a potent illusion that lasts for the duration.  To you and
    any creatures you designate when you cast the spell, the writing appears
    normal, written in your hand, and conveys whatever meaning you intended
    when you wrote the text. To all others, the writing appears as if it were
    written in an unknown or magical script that is
    unintelligible. Alternatively, you can cause the writing to appear to be an
    entirely different message, written in a different hand and language,
    though the language must be one you know.  Should the spell be dispelled,
    the original script and the illusion both disappear.  A creature with
    truesight can read the hidden message.

    """
    name = 'Illusory Script'
    level = 1
    casting_time = '1 minute'
    casting_range = 'Touch'
    components = ('S', 'M')
    materials = "a lead-based ink worth at least 10 gp, which the spell consumes"
    duration = "10 days"
    magic_school = "Illusion"
    ritual = True
    classes = ('Bard', 'Warlock', 'Wizard')


class Imprisonment(Spell):
    """You create a magical restraint to hold a creature that you can see
    within range. The target must succeed on a Wisdom saving throw or
    be bound by the spell; if it succeeds, it is immune to this spell
    if you cast it again. While affected by this spell, the creature
    doesn’t need to breathe, eat, or drink, and it doesn’t
    age. Divination spells can’t locate or perceive the target. When
    you cast the spell, you choose one of the following forms of
    imprisonment. Burial. The target is entombed far beneath the earth
    in a sphere of magical force that is just large enough to contain
    the target. Nothing can pass through the sphere, nor can any
    creature teleport or use planar travel to get into or out of
    it. The special component for this version of the spell is a small
    mithral orb. Chaining. Heavy chains, firmly rooted in the ground,
    hold the target in place. The target is restrained until the spell
    ends, and it can’t move or be moved by any means until then. The
    special component for this version of the spell is a fine chain of
    precious metal. Hedged Prison. The spell transports the target
    into a tiny demiplane that is warded against teleportation and
    planar travel. The demiplane can be a labyrinth, a cage, a tower,
    or any similar confined structure or area of your choice. The
    special component for this version of the spell is a miniature
    representation of the prison made from jade. Minimus
    Containment. The target shrinks to a height of 1 inch and is
    imprisoned inside a gemstone or similar object. Light can pass
    through the gemstone normally (allowing the target to see out and
    other creatures to see in), but nothing else can pass through,
    even by means of teleportation or planar travel. The gemstone
    can’t be cut or broken while the spell remains in effect. The
    special component for this version of the spell is a large,
    transparent gemstone, such as a corundum, diamond, or
    ruby. Slumber. The target falls asleep and can’t be awoken. The
    special component for this version of the spell consists of rare
    soporific herbs. Ending the Spell. During the casting of the
    spell, in any of its versions, you can specify a condition that
    will cause the spell to end and release the target. The condition
    can be as specific or as elaborate as you choose, but the DM must
    agree that the condition is reasonable and has a likelihood of
    coming to pass. The conditions can be based on a creature’s name,
    identity, or deity but otherwise must be based on observable
    actions or qualities and not based on intangibles such as level,
    class, or hit points. A dispel magic spell can end the spell only
    if it is cast as a 9th-level spell, targeting either the prison or
    the special component used to create it. You can use a particular
    special component to create only one prison at a time. If you cast
    the spell again using the same component, the target of the first
    casting is immediately freed from its binding.
    
    """
    name = "Imprisonment"
    level = 9
    casting_time = "1 minute"
    components = ('V', 'S', 'M')
    materials = "a vellum depiction or a carved statuette in the likeness of the target, and a special component that varies according to the version of the spell you choose, worth at least 500 gp per Hit Die of the target"
    duration = "Until dispelled"
    magic_school = "Abjuration"
    classes = ()


class InflictWounds(Spell):
    """Make a melee spell attack against a creature you can reach. On a
    hit, the target takes 3d10 necrotic damage. At Higher Levels. When
    you cast this spell using a spell slot of 2nd level or higher, the
    damage increases by 1d10 for each slot level above 1st.
    
    """
    name = "Inflict Wounds"
    level = 1
    casting_time = "1 action"
    components = ('V', 'S')
    materials = ""
    duration = "Instantaneous"
    magic_school = "Necromancy"
    classes = ()


class Invisibility(Spell):
    """A creature you touch becomes invisible until the spell
    ends. Anything the target is wearing or carrying is invisible as
    long as it is on the target’s person. The spell ends for a target
    that attacks or casts a spell. At Higher Levels. When you cast
    this spell using a spell slot of 3rd level or higher, you can
    target one additional creature for each slot level above 2nd.
    
    """
    name = "Invisibility"
    level = 2
    casting_time = "1 action"
    components = ('V', 'S', 'M')
    materials = "an eyelash encased in gum arabic"
    duration = "Concentration, up to 1 hour"
    magic_school = "Illusion"
    classes = ()


