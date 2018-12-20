from .spells import Spell


class VampiricTouch(Spell):
    """The touch of your shadow-wreathed hand can siphon life force from
    others to heal your wounds. Make a melee spell attack against a
    creature within your reach. On a hit, the target takes 3d6
    necrotic damage, and you regain hit points equal to half the
    amount of necrotic damage dealt. Until the spell ends, you can
    make the attack again on each of your turns as an action.
    
    **At Higher Levels.** When you cast this spell using a spell slot
    of 4th level or higher, the damage increases by 1d6 for each slot
    level above 3rd.
    
    """
    name = "Vampiric Touch"
    level = 3
    casting_time = "1 action"
    casting_range = "Self"
    components = ('V', 'S', )
    materials = ""
    duration = "Concentration (1 minute)"
    magic_school = "Necromancy"
    classes = ('Warlock', 'Wizard', )


class WallOfFire(Spell):
    """You create a wall of fire on a solid surface within range. You can
    make the wall up to 60 feet long, 20 feet high, and 1 foot thick,
    or a ringed wall up to 20 feet in diameter, 20 feet high, and 1
    foot thick. The wall is opaque and lasts for the duration. When
    the wall appears, each creature within its area must make a
    Dexterity saving throw. On a failed save, a creature takes 5d8
    fire damage, or half as much damage on a successful save. One side
    of the wall, selected by you when you cast this spell, deals 5d8
    fire damage to each creature that ends its turn within 10 feet of
    that side or inside the wall. A creature takes the same damage
    when it enters the wall for the first time on a turn or ends its
    turn there. The other side of the wall deals no damage. At Higher
    Levels. When you cast this spell using a spell slot of 5th level
    or higher, the damage increases by 1d8 for each slot level above
    4th.
    
    """
    name = "Wall of Fire"
    level = 4
    casting_time = "1 action"
    components = ('V', 'S', 'M')
    materials = "a small piece of phosphorus"
    duration = "Concentration, up to 1 minute"
    magic_school = "Evocation"
    classes = ()


class WallOfStone(Spell):
    """A nonmagical wall of solid stone springs into existence at a point
    you choose within range. The wall is 6 inches thick and is
    composed of ten 10-foot-by-10-foot panels. Each panel must be
    contiguous with at least one other panel. Alternatively, you can
    create 10-foot-by-20-foot panels that are only 3 inches thick. If
    the wall cuts through a creature’s space when it appears, the
    creature is pushed to one side of the wall (your choice). If a
    creature would be surrounded on all sides by the wall (or the wall
    and another solid surface), that creature can make a Dexterity
    saving throw. On a success, it can use its reaction to move up to
    its speed so that it is no longer enclosed by the wall. The wall
    can have any shape you desire, though it can’t occupy the same
    space as a creature or object. The wall doesn’t need to be
    vertical or rest on any firm foundation. It must, however, merge
    with and be solidly supported by existing stone. Thus, you can use
    this spell to bridge a chasm or create a ramp. If you create a
    span greater than 20 feet in length, you must halve the size of
    each panel to create supports. You can crudely shape the wall to
    create crenellations, battlements, and so on. The wall is an
    object made of stone that can be damaged and thus breached. Each
    panel has AC 15 and 30 hit points per inch of thickness. Reducing
    a panel to 0 hit points destroys it and might cause connected
    panels to collapse at the DM’s discretion. If you maintain your
    concentration on this spell for its whole duration, the wall
    becomes permanent and can’t be dispelled. Otherwise, the wall
    disappears when the spell ends.
    
    """
    name = "Wall of Stone"
    level = 5
    casting_time = "1 action"
    components = ('V', 'S', 'M')
    materials = "a small block of granite"
    duration = "Concentration, up to 10 minutes"
    magic_school = "Evocation"
    classes = ()


class WardingBond(Spell):
    """This spell wards a willing creature you touch and creates a mystic
    connection between you and the target until the spell ends. While
    the target is within 60 feet of you, it gains a +1 bonus to AC and
    saving throws, and it has resistance to all damage. Also, each
    time it takes damage, you take the same amount of damage. The
    spell ends if you drop to 0 hit points or if you and the target
    become separated by more than 60 feet. It also ends if the spell
    is cast again on either of the connected creatures. You can also
    dismiss the spell as an action.
    
    """
    name = "Warding Bond"
    level = 2
    casting_time = "1 action"
    components = ('V', 'S', 'M')
    materials = "a pair of platinum rings worth at least 50 gp each, which you and the target must wear for the duration"
    duration = "1 hour"
    magic_school = "Abjuration"
    classes = ()


class Web(Spell):
    """You conjure a mass of thick, sticky webbing at a point of your
    choice within range. The webs fill a 20-foot cube from that point
    for the duration. The webs are difficult terrain and lightly
    obscure their area. If the webs aren’t anchored between two solid
    masses (such as walls or trees) or layered across a floor, wall,
    or ceiling, the conjured web collapses on itself, and the spell
    ends at the start of your next turn. Webs layered over a flat
    surface have a depth of 5 feet. Each creature that starts its turn
    in the webs or that enters them during its turn must make a
    Dexterity saving throw. On a failed save, the creature is
    restrained as long as it remains in the webs or until it breaks
    free. A creature restrained by the webs can use its action to make
    a Strength check against your spell save DC. If it succeeds, it is
    no longer restrained. The webs are flammable. Any 5-foot cube of
    webs exposed to fire burns away in 1 round, dealing 2d4 fire
    damage to any creature that starts its turn in the fire.
    
    """
    name = "Web"
    level = 2
    casting_time = "1 action"
    components = ('V', 'S', 'M')
    materials = "a bit of spiderweb"
    duration = "Concentration, up to 1 hour"
    magic_school = "Conjuration"
    classes = ()
