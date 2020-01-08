from .spells import Spell


class RaiseDead(Spell):
    """You return a dead creature you touch to life, provided that it has been dead no 
    longer than 10 days. If the creature's soul is both willing and at liberty to 
    rejoin the body, the creature returns to life with 1 hit point.
    
    This spell also
     neutralizes any poison and cures nonmagical diseases that affected the creature
     at the time it died. This spell doesn't, however, remove magical diseases, 
    curses, or similar effects; if these aren't first removed prior to casting the 
    spell, they take effect when the creature returns to life. The spell can't 
    return an undead creature to life.
    
    This spell closes all mortal wounds, but it 
    doesn't restore missing body parts. If the creature is lacking body parts or 
    organs integral for its survival – its head, for instance – the spell 
    automatically fails.
    
    Coming back from the dead is an ordeal. The target takes a
     -4 penalty to all attack rolls, saving throws, and ability checks. Every time 
    the target finishes a long rest, the penalty is reduced by 1 until it 
    disappears.
    """
    name = "Raise Dead"
    level = 5
    casting_time = "1 hour"
    casting_range = "Touch"
    components = ('V', 'S', 'M')
    materials = """A diamond worth at least 500 gp, which the spell consumes"""
    duration = "Instantaneous"
    ritual = False
    magic_school = "Necromancy"
    classes = ('Bard', 'Cleric', 'Paladin')


class RarysTelepathicBond(Spell):
    """You forge a telepathic link among up to eight willing creatures of your choice 
    within range, psychically linking each creature to all the others for the 
    duration. Creatures with Intelligence scores of 2 or less aren't affected by 
    this spell.
    
    Until the spell ends, the targets can communicated telepathically 
    through the bond whether or not they have a common language. The communication 
    is possible over any distance, though it can't extend to other planes of 
    existence.
    """
    name = "Rarys Telepathic Bond"
    level = 5
    casting_time = "1 action"
    casting_range = "30 feet"
    components = ('V', 'S', 'M')
    materials = """Pieces of eggshell from two different kinds of creatures"""
    duration = "1 hour"
    ritual = True
    magic_school = "Divination"
    classes = ('Wizard',)


class RayOfEnfeeblement(Spell):
    """A black beam of enervating energy springs from your finger toward a creature 
    within range.
    Make a ranged spell attack against the target. On a hit, the 
    target deals only half damage with weapon attacks that use Strength until the 
    spell ends.
    
    At the end of each of the target's turns, it can make a 
    Constitution saving throw against the spell. On a success, the spell ends.
    """
    name = "Ray Of Enfeeblement"
    level = 2
    casting_time = "1 action"
    casting_range = "60 feet"
    components = ('V', 'S')
    materials = """"""
    duration = "Concentration, up to 1 minute"
    ritual = False
    magic_school = "Necromancy"
    classes = ('Warlock', 'Wizard')


class RayOfFrost(Spell):
    """A frigid beam of blue-white light streaks toward a creature within range. Make a
     ranged spell attack against the target. On a hit, it takes 1d8 cold damage, and
     its speed is reduced by 10 feet until the start of your next turn.
    
    At Higher 
    Levels: The spell's damage increases by 1d8 when you reach 5th level (2d8), 11th
     level (3d8), and 17th level (4d8).
    """
    name = "Ray Of Frost"
    level = 0
    casting_time = "1 action"
    casting_range = "60 feet"
    components = ('V', 'S')
    materials = """"""
    duration = "Instantaneous"
    ritual = False
    magic_school = "Evocation"
    classes = ('Sorcerer', 'Wizard')


class RayOfSickness(Spell):
    """A ray of sickening greenish energy lashes out toward a creature within range.
    
    Make a ranged spell attack against the target. On a hit, the target takes 2d8 
    poison damage and must make a Constitution saving throw. On a failed save, it is
     also poisoned until the end of your next turn.
    
    At Higher Levels: When you cast
     this spell using a spell slot of 2nd level or higher, the damage increases by 
    1d8 for each slot level above 1st.
    """
    name = "Ray Of Sickness"
    level = 1
    casting_time = "1 action"
    casting_range = "60 feet"
    components = ('V', 'S')
    materials = """"""
    duration = "Instantaneous"
    ritual = False
    magic_school = "Necromancy"
    classes = ('Sorcerer', 'Wizard')


class Regenerate(Spell):
    """You touch a creature and stimulate its natural healing ability.
    The target 
    regains 4d8 + 15 hit points. For the duration of the spell, the target regains 1
     hit point at the start of each of its turns (10 hit points each minute).
    
    The 
    target's severed body members (fingers, legs, tails, and so on), if any, are 
    restored after 2 minutes. If you have the severed part and hold it to the stump,
     the spell instantaneously causes the limb to knit to the stump.
    """
    name = "Regenerate"
    level = 7
    casting_time = "1 minute"
    casting_range = "Touch"
    components = ('V', 'S', 'M')
    materials = """A prayer wheel and holy water"""
    duration = "1 hour"
    ritual = False
    magic_school = "Transmutation"
    classes = ('Bard', 'Cleric', 'Druid')


class Reincarnate(Spell):
    """You touch a dead humanoid or a piece of a dead humanoid. Provided that the 
    creature has been dead no longer than 10 days, the spell forms a new adult body 
    for it and then calls the soul to enter that body. If the target's soul isn't 
    free or willing to do so, the spell fails.
    
    The magic fashions a new body for 
    the creature to inhabit, which likely causes the creature's race to change. The 
    DM rolls a d 100 and consults the following table to determine what form the 
    creature takes when restored to life, or the DM chooses a form.
    
    d100  Race
    
    01-04 Dragonborn
    05-13 Dwarf, hill
    14-21 Dwarf, mountain
    22-25 Elf, dark
    26-34 
    Elf, high
    35-42 Elf, wood
    43-46 Gnome, forest
    47-52 Gnome, rock
    53-56  Half-elf
    
    57-60 Half-orc
    61-68 Halfling, lightfoot
    69-76 Halfling, stout
    77-96 Human
    97-00
     Tiefling
    
    The reincarnated creature recalls its former life and experiences. It
     retains the capabilities it had in its original form, except it exchanges its 
    original race for the new one and changes its racial traits accordingly.
    """
    name = "Reincarnate"
    level = 5
    casting_time = "1 hour"
    casting_range = "Touch"
    components = ('V', 'S', 'M')
    materials = """Rare oils and unguents worth at least 1,000 gp, which the spell consumes"""
    duration = "Instantaneous"
    ritual = False
    magic_school = "Transmutation"
    classes = ('Druid',)


class RemoveCurse(Spell):
    """At your touch, all curses affecting one creature or object end. If the object is
     a cursed magic item, its curse remains, but the spell breaks its owner's 
    attunement to the object so it can be removed or discarded.
    """
    name = "Remove Curse"
    level = 3
    casting_time = "1 action"
    casting_range = "Touch"
    components = ('V', 'S')
    materials = """"""
    duration = "Instantaneous"
    ritual = False
    magic_school = "Abjuration"
    classes = ('Cleric', 'Paladin', 'Warlock', 'Wizard')


class Resistance(Spell):
    """You touch one willing creature. Once before the spell ends, the target can roll 
    a d4 and add the number rolled to one saving throw of its choice. It can roll 
    the die before or after the saving throw. The spell then ends.
    """
    name = "Resistance"
    level = 0
    casting_time = "1 action"
    casting_range = "Touch"
    components = ('V', 'S', 'M')
    materials = """A miniature cloak"""
    duration = "Concentration, up to 1 minute"
    ritual = False
    magic_school = "Abjuration"
    classes = ('Cleric', 'Druid')


class Resurrection(Spell):
    """You touch a dead creature that has been dead for no more than a century, that 
    didn't die of old age, and that isn't undead. If its soul is free and willing, 
    the target returns to life with all its hit points.
    
    This spell neutralizes any 
    poisons and cures normal diseases afflicting the creature when it died. It 
    doesn't, however, remove magical diseases, curses, and the like; if such affects
     aren't removed prior to casting the spell, they afflict the target on its 
    return to life.
    
    This spell closes all mortal wounds and restores any missing 
    body parts.
    
    Coming back from the dead is an ordeal. The target takes a -4 
    penalty to all attack rolls, saving throws, and ability checks. Every time the 
    target finishes a long rest, the penalty is reduced by 1 until it disappears.
    
    
    Casting this spell to restore life to a creature that has been dead for one year
     or longer taxes you greatly. Until you finish a long rest, you can't cast 
    spells again, and you have disadvantage on all attack rolls, ability checks, and
     saving throws.
    """
    name = "Resurrection"
    level = 7
    casting_time = "1 hour"
    casting_range = "Touch"
    components = ('V', 'S', 'M')
    materials = """A diamond worth at least 1,000 gp, which the spell consumes"""
    duration = "Instantaneous"
    ritual = False
    magic_school = "Necromancy"
    classes = ('Bard', 'Cleric')


class ReverseGravity(Spell):
    """This spell reverses gravity in a 50-foot-radius, 100-foot high cylinder centered
     on a point within range.
    All creatures and objects that aren't somehow anchored
     to the ground in the area fall upward and reach the top of the area when you 
    cast this spell. A creature can make a Dexterity saving throw to grab onto a 
    fixed object it can reach, thus avoiding the fall.
    
    If some solid object (such 
    as a ceiling) is encountered in this fall, falling objects and creatures strike 
    it just as they would during a normal downward fall. If an object or creature 
    reaches the top of the area without striking anything, it remains there, 
    oscillating slightly, for the duration.
    
    At the end of the duration, affected 
    objects and creatures fall back down.
    """
    name = "Reverse Gravity"
    level = 7
    casting_time = "1 action"
    casting_range = "100 feet"
    components = ('V', 'S', 'M')
    materials = """A lodestone and iron filings"""
    duration = "Concentration, up to 1 minute"
    ritual = False
    magic_school = "Transmutation"
    classes = ('Druid', 'Sorcerer', 'Wizard')


class Revivify(Spell):
    """You touch a creature that has died within the last minute. That creature returns
     to life with 1 hit point. This spell can't return to life a creature that has 
    died of old age, nor can it restore any missing body parts.
    """
    name = "Revivify"
    level = 3
    casting_time = "1 action"
    casting_range = "Touch"
    components = ('V', 'S', 'M')
    materials = """Diamonds worth 300 gp, which the spell consumes"""
    duration = "Instantaneous"
    ritual = False
    magic_school = "Necromancy"
    classes = ('Cleric', 'Paladin')


class RopeTrick(Spell):
    """You touch a length of rope that is up to 60 feet long. One end of the rope then 
    rises into the air until the whole rope hangs perpendicular to the ground. At 
    the upper end of the rope, an invisible entrance opens to an extradimensional 
    space that lasts until the spell ends.
    
    The extradimensional space can be 
    reached by climbing to the top of the rope. The space can hold as many as eight 
    Medium or smaller creatures. The rope can be pulled into the space, making the 
    rope disappear from view outside the space.
    
    Attacks and spells can't cross 
    through the entrance into or out of the extradimensional space, but those inside
     can see out of it as if through a 3-foot-by-5-foot window centered on the rope.
    
    
    Anything inside the extradimensional space drops out when the spell ends.
    """
    name = "Rope Trick"
    level = 2
    casting_time = "1 action"
    casting_range = "Touch"
    components = ('V', 'S', 'M')
    materials = """Powdered corn extract and a twisted loop of parchment"""
    duration = "1 hour"
    ritual = False
    magic_school = "Transmutation"
    classes = ('Wizard',)


