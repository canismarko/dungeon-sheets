from dungeonsheets.spells.spells import Spell


class WallOfFire(Spell):
    """You create a wall of fire on a solid surface within range. You can
    make the wall up to 60 feet long, 20 feet high, and 1 foot thick,
    or a ringed wall up to 20 feet in diameter, 20 feet high, and 1
    foot thick. The wall is opaque and lasts for the duration.

    When the wall appears, each creature within its area must make a
    Dexterity saving throw. On a failed save, a creature takes 5d8
    fire damage, or half as much damage on a successful save.

    One side of the wall, selected by you when you cast this spell,
    deals 5d8 fire damage to each creature that ends its turn within
    10 feet of that side or inside the wall. A creature takes the same
    damage when it enters the wall for the first time on a turn or
    ends its turn there. The other side of the wall deals no damage.

    **At Higher Levels:** When you cast this spell using a spell slot
    of 5th level or higher, the damage increases by 1d8 for each slot
    level above 4th.

    """

    name = "Wall Of Fire"
    level = 4
    casting_time = "1 action"
    casting_range = "120 feet"
    components = ("V", "S", "M")
    materials = "A small piece of phosphorus"
    duration = "Concentration, up to 1 minute"
    ritual = False
    magic_school = "Evocation"
    classes = ("Druid", "Sorcerer", "Wizard")


class WallOfForce(Spell):
    """An invisible wall of force springs into existence at a point you
    choose within range.  The wall appears in any orientation you
    choose, as a horizontal or vertical barrier or at an angle. It can
    be free floating or resting on a solid surface. You can form it
    into a hemispherical dome or a sphere with a radius of up to 10
    feet, or you can shape a flat surface made up of ten
    10-foot-by-10-foot panels. Each panel must be continguous with
    another panel. In any form, the wall is 1/4 inch thick. It lasts
    for the duration. If the wall cuts through a creature's space when
    it appears, the creature is pushed to one side of the wall (your
    choice which side).

    Nothing can physically pass through the wall. It is immune to all
    damage and can't be dispelled by dispel magic. A disintegrate
    spell destroys the wall instantly, however. The wall also extends
    into the Ethereal Plane, blocking ethereal travel through the
    wall.

    """

    name = "Wall Of Force"
    level = 5
    casting_time = "1 action"
    casting_range = "120 feet"
    components = ("V", "S", "M")
    materials = "A pinch of powder made by crushing a clear gemstone"
    duration = "Concentration, up to 10 minutes"
    ritual = False
    magic_school = "Evocation"
    classes = ("Wizard",)


class WallOfIce(Spell):
    """You create a wall of ice on a solid surface within range. You can
    form it into a hemispherical dome or a sphere with radius of up to
    10 feet, or you can shape a flat surfcae made up of ten
    10-foot-square panels. Each panel must be contiguous with another
    panel. In any form, the wall is 1 foot thick and lasts for the
    duration.

    If the wall cuts through a creature's space when it appears, the
    creature within its area is pushed to one side of the wall and
    must make a Dexterity saving throw. On a failed save, the creature
    takes 10d6 cold damage, or half as much damage on a successful
    save.

    The wall is an object that can be damaged and thus breached. It
    has AC 12 and 30 hit points per 10-foot section, and it is
    vulnerable to fire damage. Reducing a 10-foot section of wall to 0
    hit points destroys it and leaves behind a sheet of frigid air int
    he space the wall occupied. A creature moving through the sheet of
    frigid air for the first time on a turn must make a Constitution
    saaving throw. The creature takes 5f6 cold damage on a failed
    save, or half as much damage on a successful one.

    **At Higher Levels:** When you cast this spell using a spell slot
    of 7th level or higher, the damage the wall deals when it appears
    increases by 2d6, and the damage from passing through the sheet of
    frigid air increases by 1d6, for each slot level above 6th.

    """

    name = "Wall Of Ice"
    level = 6
    casting_time = "1 action"
    casting_range = "120 feet"
    components = ("V", "S", "M")
    materials = "A small piece of quartz"
    duration = "Concentration, up to 10 minutes"
    ritual = False
    magic_school = "Evocation"
    classes = ("Wizard",)


class WallOfLight(Spell):
    """A shimmering wall of bright light appears at a point you choose
    within range.  The wall appears in any orientation you choose:
    horizontally, vertically, or diagonally. It can be free floating,
    or it can rest on a solid surface. The wall can be up to 60 feet
    long, 10 feet high, and 5 feet thick. The wall blocks line of
    sight, but creatures and objects can pass through it. It emits
    bright light out to 120 feet and dim light for an additional 120
    feet.

    When the wall appears, each creature in its area must make a
    Constitution saving throw. On a failed save, a creature takes 4d8
    radiant damage, and it is blinded for 1 minute. On a successful
    save, it takes half as much damage and isn't blinded. A blinded
    creature can make a Constitution saving throw at the end of each
    of its turns, ending the effect on itself on a success.

    A creature that ends its turn in the wall's area takes 4d8 radiant
    damage.  Until the spell ends, you can use an action to launch a
    beam of radiance from the wall at one creature you can see within
    60 feet of it. Make a ranged spell attack. On a hit, the target
    takes 4d8 radiant damage. Whether you hit or miss, reduce the
    length of the wall by 10 feet. If the wall's length drops to 0
    feet, the spell ends.

    **At Higher Levels:** When you cast this spell using a spell slot
    of 6th level or higher, the damage increases by 1d8 for each slot
    level above 5th.

    """

    name = "Wall Of Light"
    level = 5
    casting_time = "1 action"
    casting_range = "120 feet"
    components = ("V", "S", "M")
    materials = "A hand mirror"
    duration = "Concentration, up to 10 minutes"
    ritual = False
    magic_school = "Evocation"
    classes = ("Sorcerer", "Warlock", "Wizard")


class WallOfSand(Spell):
    """You conjure up a wall of swirling sand on the ground at a point you can see
    within range. You can make the wall up to 30 feet long, 10 feet high, and 10
    feet thick, and it vanishes when the spell ends. It blocks line of sight but not
    movement. A creature is blinded while in the wall's space and must spend 3 feet
    of movement for every 1 foot it moves there.
    """

    name = "Wall Of Sand"
    level = 3
    casting_time = "1 action"
    casting_range = "90 feet"
    components = ("V", "S", "M")
    materials = "A handful of sand"
    duration = "Instantaneous"
    ritual = False
    magic_school = "Evocation"
    classes = ("Wizard",)


class WallOfStone(Spell):
    """A nonmagical wall of solid stone springs into existence at a point
    you choose within range.  The wall is 6 inches thick and is
    composed of ten 10-foot- by-10-foot panels. Each panel must be
    contiguous with at least on other panel.  Alternatively, you can
    create 10-foot-by-20-foot panels that are only 3 inches thick.

    If the wall cuts through a creature's space when it appears, the
    creature is pushed to one side of the wall (your choice). If a
    creature would be surrounded on all sides by the wall (or the wall
    and another solid surface), that creature can make a Dexterity
    saving throw. On a success, it can use its reaction to move up to
    its speed so that it is no longer enclosed by the wall.

    The wall can have any shape you desire, though it can't occupy the
    same space as a creature or object. the wall doesn't need to be
    vertical or resting on any firm foundation. It must, however,
    merge with and be solidly supported by existing stone. Thus you
    can use this spell to bridge a chasm or create a ramp.

    If you create a span greater than 20 feet in length, you must
    halve the size of each panel to create supports. You can crudely
    shape the wall to create crenellations, battlements, and so on.

    The wall is an object made of stone that can be damaged and thus
    breached. Each panel has AC 15 and 30 hit points per inch of
    thickness. Reducing a panel to 0 hit points destroys it and might
    cause connected panels to collapse at the DM's discretion.

    If you maintain your concentration on this spell for its whole
    duration, the wall becomes permanent and can't be
    dispelled. Otherwise, the wall disappears when the spell ends.

    """

    name = "Wall Of Stone"
    level = 5
    casting_time = "1 action"
    casting_range = "120 feet"
    components = ("V", "S", "M")
    materials = "A small block of granite"
    duration = "Concentration, up to 10 minutes"
    ritual = False
    magic_school = "Evocation"
    classes = ("Druid", "Sorcerer", "Wizard")


class WallOfThorns(Spell):
    """You create a wall of tough, pliable, tangled brush bristling with needle-sharp
    thorns. The wall appears within range on a solid surface and lasts for the
    duration. You choose to make the wall up to 60 feet long, 10 feet high, and 5
    feet thick or a circle that has a 20-foot diameter and is up to 20 feet high and
    5  feet thick. The wall blocks line of sight.

    When the wall appears, each
    creature within its area must make a Dexterity saving throw. On a failed save, a
    creature takes 7d8 piercing damage, or half as much damage on a successful
    save.

    A creature can move through the wall, albeit slowly and painfully. For
    every 1 foot a creature moves through the wall, it must spend 4 feet of
    movement. Furthermore, the first time a creature enters the wall on a turn or
    ends its turn there, the creature must make a Dexterity saving throw. It takes
    7d8 slashing damage on a failed save, or half as much on a successful save.

    At
    Higher Levels: When you cast this spell using a spell slot of 7th level or
    higher, both types o f damage increase by 1d8 for each slot level above 6th.
    """

    name = "Wall Of Thorns"
    level = 6
    casting_time = "1 action"
    casting_range = "120 feet"
    components = ("V", "S", "M")
    materials = "A handful of thorns"
    duration = "Concentration, up to 10 minutes"
    ritual = False
    magic_school = "Conjuration"
    classes = ("Druid",)


class WallOfWater(Spell):
    """(a drop of water)

    You conjure up a wall of water on the ground at a point you can
    see within range. You can make the wall up to 30 feet long, 10
    feet high, and 1 foot thick, or you can make a ringed wall up to
    20 feet in diameter, 20 feet high, and 1 foot thick. The wall
    vanishes when the spell ends. The wall's space is difficult
    terrain.

    Any ranged weapon attack that enters the wall's space has
    disadvantage on the attack roll, and fire damage is halved if the
    fire effect passes through the wall to reach its target. Spells
    that deal cold damage that pass through the wall cause the area of
    the wall they pass through to freeze solid (at least a 5-foot
    square section is frozen). Each 5-foot-square frozen section has
    AC 5 and 15 hit points. Reducing a frozen section to 0 hit points
    destroys it. When a section is destroyed, the wall’s water doesn’t
    fill it.

    """

    name = "Wall Of Water"
    level = 3
    casting_time = "1 action"
    casting_range = "60 feet"
    components = ("V", "S", "M")
    materials = ""
    duration = "Instantaneous"
    ritual = False
    magic_school = "Evocation"
    classes = ("Druid", "Sorcerer", "Wizard")


class WardingBond(Spell):
    """This spell wards a willing creature you touch and creates a mystic connection
    between you and the target until the spell ends.

    While the target is within 60
    feet of you, it gains a +1 bonus to AC and saving throws, and it has resistance
    to all damage. Also, each time it takes damage, you take the same amount of
    damage.

    The spell ends if you drop to 0 hit points or if you and the target
    become separated by more than 60 feet. It also ends if the spell is cast again
    on either of the connected creatures. You can also dismiss the spell as an
    action.
    """

    name = "Warding Bond"
    level = 2
    casting_time = "1 action"
    casting_range = "Touch"
    components = ("V", "S", "M")
    materials = (
        "A pair of platinum rings worth at least 50 gp each, which you and target must"
        " wear for the duration"
    )
    duration = "1 hour"
    ritual = False
    magic_school = "Abjuration"
    classes = ("Cleric",)


class WardingWind(Spell):
    """A strong wind (20 miles per hour) blows around you in a 10-foot
    radius and moves with you, remaining centered on you. The wind
    lasts for the spell's duration.

    The wind has the following effects:

    - It deafens you and other creatures in its area.
    - It extinguishes unprotected flames in its area that are
      torch-sized or smaller.
    - The area is difficult terrain for creatures other than you.
    - The attack rolls of ranged weapon attacks have disadvantage if
      they pass in or out of the wind.
    - It hedges out vapor, gas, and fog that can be dispersed by
      strong wind.

    """

    name = "Warding Wind"
    level = 2
    casting_time = "1 action"
    casting_range = "Self"
    components = ("V",)
    materials = ""
    duration = "Concentration, up to 10 minutes"
    ritual = False
    magic_school = "Evocation"
    classes = ("Bard", "Druid", "Sorcerer", "Wizard")


class WaterBreathing(Spell):
    """This spell grants up to ten willing creatures you can see within range the
    ability to breathe underwater until the spell ends. Affected creatures also
    retain their normal mode of respiration.
    """

    name = "Water Breathing"
    level = 3
    casting_time = "1 action"
    casting_range = "30 feet"
    components = ("V", "S", "M")
    materials = "A short reed or piece of straw"
    duration = "24 hours"
    ritual = True
    magic_school = "Transmutation"
    classes = ("Druid", "Ranger", "Sorcerer", "Wizard")


class WaterWalk(Spell):
    """This spell grants the ability to move across any liquid surface – such as water,
    acid, mud, snow, quicksand, or lava – as if it were harmless solid ground
    (creatures crossing molten lava can still take damage from the heat).
    Up to ten
    willing creatures you can see within range gain this ability for the duration.


    If you target a creature submerged in a liquid, the spell carries the target to
    the surface of the liquid at a rate of 60 feet per round.
    """

    name = "Water Walk"
    level = 3
    casting_time = "1 action"
    casting_range = "30 feet"
    components = ("V", "S", "M")
    materials = "A piece of cork"
    duration = "1 hour"
    ritual = True
    magic_school = "Transmutation"
    classes = ("Cleric", "Druid", "Ranger", "Sorcerer")


class WaterySphere(Spell):
    """You conjure up a sphere of water with a 5-foot radius on a point
    you can see within range. The sphere can hover in the air, but no
    more than 10 feet off the ground. The sphere remains for the
    spell's duration.

    Any creature in the sphere's space must make a Strength saving
    throw. On a successful save, a creature is ejected from that space
    to the nearest unoccupied space outside it.  A Huge or larger
    creature succeeds on the saving throw automatically. On a failed
    save, a creature is restrained by the sphere and is engulfed by
    the water. At the end of each of its turns, a restrained target
    can repeat the saving throw.

    The sphere can restrain a maximum of four Medium or smaller
    creatures or one Large creature. If the sphere restrains a
    creature in excess of these numbers, a random creature that was
    already restrained by the sphere falls out of it and lands prone
    in a space within 5 feet of it.

    As an action, you can move the sphere up to 30 feet in a straight
    line. If it moves over a pit, cliff, or other drop, it safely
    descends until it is hovering 10 feet over ground. Any creature
    restrained by the sphere moves with it. You can ram the sphere
    into creatures, forcing them to make the saving throw, but no more
    than once per turn.

    When the spell ends, the sphere falls to the ground and
    extinguishes all normal flames within 30 feet of it. Any creature
    restrained by the sphere is knocked prone in the space where it
    falls.

    """

    name = "Watery Sphere"
    level = 4
    casting_time = "1 action"
    casting_range = "90 feet"
    components = ("V", "S", "M")
    materials = "A droplet of water"
    duration = "Concentration, up to 1 minute"
    ritual = False
    magic_school = "Conjuration"
    classes = ("Druid", "Sorcerer", "Wizard")


class Web(Spell):
    """You conjure a mass of thick, sticky webbing at a point of your
    choice within range.  The webs fill a 20-foot cube from that point
    for the duration. The webs are difficult terrain and lightly
    obscure their area.

    If the webs aren't anchored between two solid masses (such as
    walls or trees) or layered across a floor, wall, or ceiling, the
    conjured web collapses on itself, and the spell ends at the start
    of your next turn. Webs layered over a flat surface have a depth
    of 5 feet.

    Each creature that starts its turn in the webs or that enters them
    during its turn must make a Dexterity saving throw. On a failed
    save, the creature is restrained as long as it remains in the webs
    or until it breaks free.

    A creature restrained by the webs can use its action to make a
    Strength check against your spell save DC. If it succeeds, it is
    no longer restrained.

    The webs are flammable. Any 5-foot cube of webs exposed to fire
    burns away in 1 round, dealing 2d4 fire damage to any creature
    that starts its turn in the fire.

    """

    name = "Web"
    level = 2
    casting_time = "1 action"
    casting_range = "60 feet"
    components = ("V", "S", "M")
    materials = "A bit of spiderweb"
    duration = "Concentration, up to 1 hour"
    ritual = False
    magic_school = "Conjuration"
    classes = ("Sorcerer", "Wizard")


class Weird(Spell):
    """Drawing on the deepest fears of a group of creatures, you create
    illusory creatures in their minds, visible only to them.  Each
    creature in a 30-foot-radius sphere centered on a point of your
    choice within range must make a Wisdom saving throw. On a failed
    save, a creature becomes frightened for the duration.

    The illusion calls on the creature's deepest fears, manifesting
    its worst nightmares as an implacable threat. At the end of each
    of the frightened creature's turns, it must succeed on a Wisdom
    saving throw or take 4d10 psychic damage. On a successful save,
    the spell ends for that creature.

    """

    name = "Weird"
    level = 9
    casting_time = "1 action"
    casting_range = "120 feet"
    components = ("V", "S")
    materials = ""
    duration = "Concentration, up to 1 minute"
    ritual = False
    magic_school = "Illusion"
    classes = ("Wizard",)


class Whirlwind(Spell):
    """A whirlwind howls down to a point that you can see on the ground
    within range.  The whirlwind is a 10-foot-radius, 30-foot-high
    cylinder centered on that point.  Until the spell ends, you can
    use your action to move the whirlwind up to 30 feet in any
    direction along the ground. The whirlwind sucks up any Medium or
    smaller objects that aren't secured to anything and that aren't
    worn or carried by anyone.

    A creature must make a Dexterity saving throw the first time on a
    turn that it enters the whirlwind or that the whirlwind enters its
    space, including when the whirlwind first appears. A creature
    takes 10d6 bludgeoning damage on a failed save, or half as much
    damage on a successful one. In addition, a Large or smaller
    creature that fails the save must succeed on a Strength saving
    throw or become restrained in the whirlwind until the spell
    ends. When a creature starts its turn restrained by the whirlwind,
    the creature is pulled 5 feet higher inside it, unless the
    creature is at the top.

    A restrained creature moves with the whirlwind and falls when the
    spell ends, unless the creature has some means to stay aloft. A
    restrained creature can use an action to make a Strength or
    Dexterity check against your spell save DC. If successful, the
    creature is no longer restrained by the whirlwind and is hurled
    3d6 x 10 feet away from it in a random direction.

    """

    name = "Whirlwind"
    level = 7
    casting_time = "1 action"
    casting_range = "300 feet"
    components = ("V", "M")
    materials = "A piece of straw"
    duration = "Concentration, up to 1 minute"
    ritual = False
    magic_school = "Evocation"
    classes = ("Druid", "Wizard", "Sorcerer")


class WildCunning(Spell):
    """You call out to the spirits of nature to aid you. When you cast this
    spell, choose one of the following effects:
    -- If there are any tracks on the ground within range, you know where they
    are, and you make Wisdom (Survival) checks to follow these tracks with
    advantage for 1 hour or until you cast this spell again.

    -- If there is edible forage within range, you know it and where to find
    it.

    -- If there is clean drinking water within range, you know it and where to
    find it.

    -- If there is suitable shelter for you and your companions with range, you
    know it and where to find it.

    -- Send the spirits to bring back wood for a fire and to set up a campsite
    in the area using your supplies. The spirits build the fire in a circle of
    stones, put up tents, unroll bedrolls, and put out any rations and water
    for consumption.

    -- Have the spirits instantly break down a campsite, which includes putting
    out a fire, taking down tents, packing up bags, and burying any rubbish.
    """

    name = "Wild Cunning"
    level = 1
    casting_time = "1 action"
    casting_range = "120 feet"
    components = ("V", "S")
    materials = ""
    duration = "Insantaneous"
    magic_school = "Transmutation"
    classes = ("Druid", "Ranger")


class WindWalk(Spell):
    """You and up to ten willing creatures you can see within range assume
    a gaseous form for the duration, appearing as wisps of cloud.
    While in this cloud form, a creature has a flying speed of 300
    feet and has resistance to damage from nonmagical weapons. The
    only actions a creature can take in this form are the Dash action
    or to revert to its normal form.  Reverting takes 1 minute, during
    which time a creature is incapacitated and can't move. Until the
    spell ends, a creature can revert to cloud form, which also
    requires the 1-minute transformation.

    If a creature is in cloud form and flying when the effect ends,
    the creature descends 60 feet per round for 1 minute until it
    lands, which it does safely. If it can't land after 1 minute, the
    creature falls the remaining distance.

    """

    name = "Wind Walk"
    level = 6
    casting_time = "1 minute"
    casting_range = "30 feet"
    components = ("V", "S", "M")
    materials = "Fire and holy water"
    duration = "8 hours"
    ritual = False
    magic_school = "Transmutation"
    classes = ("Druid",)


class WindWall(Spell):
    """A wall of strong wind rises from the ground at a point you choose
    within range.

    You can make the wall up to 50 feet long, 15 feet high, and 1 foot
    thick. You can shape the wall in any way you choose so long as it
    makes one continuous path along the ground. The wall lasts for the
    duration.

    When the wall appears, each creature within its area must make a
    Strength saving throw. A creature takes 3d8 bludgeoning damage on
    a failed save, or half as much damage on a successful one.

    The strong wind keeps fog, smoke, and other gases at bay. Small or
    smaller flying creatures or objects can't pass through the
    wall. Loose, lightweight materials brought into the wall fly
    upward. Arrows, bolts, and other ordinary projectiles launched at
    targets behind the wall are deflected upward and automatically
    miss. (Boulders hurled by giants or siege engines, and similar
    projectiles, are unaffected.) Creatures in gaseous form can't pass
    through it.

    """

    name = "Wind Wall"
    level = 3
    casting_time = "1 action"
    casting_range = "120 feet"
    components = ("V", "S", "M")
    materials = "A tiny fan and a feather of exotic origin"
    duration = "Concentration, up to 1 minute"
    ritual = False
    magic_school = "Evocation"
    classes = ("Druid", "Ranger")


class Wish(Spell):
    """Wish is the mightiest spell a mortal creature can cast. By simply
    speaking aloud, you can alter the very foundations of reality in
    accord with your desires.

    The basic use of this spell is to duplicate any other spell of 8th
    level or lower. You don't need to meet any requirements in that
    spell, including costly components. The spell simply takes effect.
    Alternatively, you can create one of the following effects of your
    choice:

    - You create one object of up to 25,000 gp in value that isn't a
      magic item. The object can be no more than 300 feet in any
      dimension, and it appears in an unoccupied space you can see on
      the ground.
    - You allow up to twenty creatures that you can see to regain all
      hit points, and you end all effects on them described in the
      greater restoration spell.
    - You grant up to ten creatures that you can see resistance to a
      damage type you choose.
    - You grant up to ten creatures you can see immunity to a single
      spell or other magical effect for 8 hours. For instance, you
      could make yourself and all your com panions immune to a lich's
      life drain attack.
    - You undo a single recent event by forcing a reroll of any roll
      made within the last round (including your last turn). Reality
      reshapes itself to accommodate the new result. For example, a
      wish spell could undo an opponent's successful save, a foe's
      critical hit, or a friend's failed save. You can force the
      reroll to be made with advantage or disadvantage, and you can
      choose whether to use the reroll or the original roll.

    You might be able to achieve something beyond the scope of the
    above examples. State your wish to the DM as precisely as
    possible.  The DM has great latitude in ruling what occurs in such
    an instance; the greater the wish, the greater the likelihood that
    something goes wrong. This spell might simply fail, the effect you
    desire might only be partly achieved, or you might suffer some
    unforeseen consequence as a result of how you worded the wish. For
    example, wishing that a villain were dead might propel you forward
    in time to a period when that villain is no longer alive,
    effectively removing you from the game. Similarly, wishing for a
    legendary magic item or artifact might instantly transport you to
    the presence of the item's current owner.

    The stress of casting this spell to produce any effect other than
    duplicating another spell weakens you. After enduring that stress,
    each time you cast a spell until you finish a long rest, you take
    1d10 necrotic damage per level of that spell. This damage can't be
    reduced or prevented in any way. In addition, your Strength drops
    to 3, if it isn't 3 or lower already, for 2d4 days. For each of
    those days that you spend resting and doing nothing more than
    light activity, your remaining recovery time decreases by 2
    days. Finally, there is a 33 percent chance that you are unable to
    cast wish ever again if you suffer this stress.

    """

    name = "Wish"
    level = 9
    casting_time = "1 action"
    casting_range = "Self"
    components = ("V",)
    materials = ""
    duration = "Instantaneous"
    ritual = False
    magic_school = "Conjuration"
    classes = ("Sorcerer", "Wizard")


class WitchBolt(Spell):
    """A beam of crackling, blue energy lances out toward a creature within range,
    forming a sustained arc of lightning between you and the target.

    Make a ranged spell attack against that creature. On a hit, the
    target takes 1d12 lightning damage, and on each of your turns for
    the duration, you can use your action to deal 1d12 lightning
    damage to the target automatically. The spell ends if you use your
    action to do anything else. The spell also ends if the target is
    ever outside the spell's range or if it has total cover from you.

    **At Higher Levels:** When you cast this spell using a spell slot
    of 2nd level or higher, the initial damage increases by 1d12 for
    each slot level above 1st.

    """

    name = "Witch Bolt"
    level = 1
    casting_time = "1 action"
    casting_range = "30 feet"
    components = ("V", "S", "M")
    materials = "A twig from a tree that has been struck by lightning"
    duration = "Concentration, up to 1 minute"
    ritual = False
    magic_school = "Evocation"
    classes = ("Sorcerer", "Warlock", "Wizard")


class WordOfRadiance(Spell):
    """You utter a divine word, and burning radiance erupts from you. Each
    creature of your choice that you can see within range must succeed
    on a Constitution saving throw or take 1d6 radiant damage.

    The spell's damage increases by 1d6 when you reach 5th level
    (2d6), 11th level (3d6), and 17th level (4d6).

    """

    name = "Word Of Radiance"
    level = 0
    casting_time = "1 action"
    casting_range = "5 feet"
    components = ("V", "M")
    materials = "A holy symbol"
    duration = "Instantaneous"
    ritual = False
    magic_school = "Evocation"
    classes = ("Cleric",)


class WordOfRecall(Spell):
    """You and up to five willing creatures within 5 feet of you instantly
    teleport to a previously designated sanctuary.  You and any
    creatures that teleport with you appear in the nearest unoccupied
    space to the spot you designated when you prepared your sanctuary
    (see below). If you cast this spell without first preparing a
    sanctuary, the spell has no effect.

    You must designate a sanctuary by casting this spell within a
    location, such as a temple, dedicated to or strongly linked to
    your deity. If you attempt to cast the spell in this manner in an
    area that isn’t dedicated to your deity, the spell has no effect.

    """

    name = "Word Of Recall"
    level = 6
    casting_time = "1 action"
    casting_range = "5 feet"
    components = ("V",)
    materials = ""
    duration = "Instantaneous"
    ritual = False
    magic_school = "Conjuration"
    classes = ("Cleric",)


class WrathOfNature(Spell):
    """You call out to the spirits of nature to rouse them against your enemies. Choose
    a point you can see within range. The spirits cause trees, rocks, and grasses
    in a 60-foot cube centered on that point to become animated until the spell
    ends.
    Grasses and Undergrowth. Any area of ground in the cube that is covered by
    grass or undergrowth is difficult terrain for your enemies.
    Trees. At the start
    of each of your turns, each of your enemies within 10 feet of any tree in the
    cube must succeed on a Dexterity saving throw or take 4d6 slashing damage from
    whipping branches.
    Roots and Vines. At the end of each of your turns, one
    creature of your choice that is on the ground in the cube must succeed on a
    Strength saving throw or become restrained until the spell ends. A restrained
    creature can use an action to make a Strength (Athletics) check against your
    spell save DC, ending the effect on itself on a success.
    Rocks. As a bonus
    action on your turn, you can cause a loose rock in the cube to launch at a
    creature you can see in the cube. Make a ranged spell attack against the target.
    On a hit, the target takes 3d8 nonmagical bludgeoning damage, and it must
    succeed on a Strength saving throw or fall prone.
    """

    name = "Wrath Of Nature"
    level = 5
    casting_time = "1 action"
    casting_range = "120 feet"
    components = ("V", "S")
    materials = ""
    duration = "Concentration, up to 1 minute"
    ritual = False
    magic_school = "Evocation"
    classes = ("Druid", "Ranger")


class WrathfulSmite(Spell):
    """The next time you hit with a melee weapon attack during this
    spell's duration, your attack deals an extra 1d6 psychic damage.
    Additionally, if the target is a creature, it must make a Wisdom
    saving throw or be frightened of you until the spell ends. As an
    action, the creature can make a Wisdom check against your spell
    save DC to steel its resolve and end this spell.
    """

    name = "Wrathful Smite"
    level = 1
    casting_time = "1 bonus action"
    casting_range = "Self"
    components = ("V",)
    materials = ""
    duration = "Concentration, up to 1 minute"
    ritual = False
    magic_school = "Evocation"
    classes = ("Paladin",)


class Wristpocket(Spell):
    """You flick your wrist, causing one object in your hand to vanish.
    The object, which only you can be holding and can weigh no more than
    5 pounds, is transported to an extradimensional space, where it remains for
    the duration.
    Until the spell ends, you can use your action to summon the object to your
    free hand, and you can use your action to return the object to
    the extradimensional space. An object still in the pocket plane when
    the spell ends appears in your space, at your feet.
    """

    name = "Wristpocket"
    level = 2
    casting_time = "1 action"
    casting_range = "Self"
    components = ("S",)
    materials = ""
    duration = "Concentration, up to 1 hour"
    ritual = True
    magic_school = "Dunamancy"
    classes = ("Wizard",)
