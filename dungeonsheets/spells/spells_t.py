from .spells import Spell


class TashasHideousLaughter(Spell):
    """A creature of your choice that you can see within range perceives everything as 
    hilariously funny and falls into fits of laughter if this spell affects it. The 
    target must succeed on a Wisdom saving throw or fall prone, becoming 
    incapacitated and unable to stand up for the duration. A creature with an 
    Intelligence score of 4 or less isn’t affected.
    
    At the end of each of its 
    turns, and each time it takes damage, the target can make another Wisdom saving 
    throw. The target has advantage on the saving throw ifit’s triggered by damage. 
    On a success, the spell ends.
    """
    name = "Tashas Hideous Laughter"
    level = 1
    casting_time = "1 action"
    casting_range = "30 feet"
    components = ('V', 'S', 'M')
    materials = """Tiny tarts and a feather that is waved in the air"""
    duration = "Concentration, up to 1 minute"
    ritual = False
    magic_school = "Enchantment"
    classes = ('Bard', 'Wizard')


class Telekinesis(Spell):
    """You gain the ability to move or manipulate creatures or objects by thought.
    When
     you cast the spell, and as your action each round for the duration, you can 
    exert your will on one creature or object that you can see within range, causing
     the appropriate effect below. You can affect the same target round after round,
     or choose a new one at any time. If you switch targets, the prior target is no 
    longer affected by the spell.
    
    Creature
    You can try to move a Huge or smaller 
    creature. Make an ability check with your spellcasting ability contested by the 
    creature’s Strength check. If you win the contest, you move the creature up to 
    30 feet in any direction, including upward but not beyond the range of this 
    spell. Until the end of your next turn, the creature is restrained in your 
    telekinetic grip. A creature lifted upward is suspended in mid-air.
    On 
    subsequent rounds, you can use your action to attempt to maintain your 
    telekinetic grip on the creature by repeating the contest.
    
    Object
    You can try 
    to move an object that weighs up to 1,000 pounds. If the object isn’t being worn
     or carried, you automatically move it up to 30 feet in any direction, but not 
    beyond the range of this spell.
    If the object is worn or carried by a creature, 
    you must make an ability check with your spellcasting ability contested by that 
    creature’s Strength check. If you succeed, you pull the object away from that 
    creature and can move it up to 30 feet in any direction but not beyond the range
     of this spell.
    You can exert fine control on objects with your telekinetic 
    grip, such as manipulating a simple tool, opening a door or a container, stowing
     or retrieving an item from an open container, or pouring the contents from a 
    vial.
    """
    name = "Telekinesis"
    level = 5
    casting_time = "1 action"
    casting_range = "60 feet"
    components = ('V', 'S')
    materials = """"""
    duration = "Concentration, up to 10 minutes"
    ritual = False
    magic_school = "Transmutation"
    classes = ('Sorcerer', 'Wizard')


class Telepathy(Spell):
    """You create a telepathic link between yourself and a willing creature with which 
    you are familiar.
    The creature can be anywhere on the same plane of existence as
     you. The spell ends if you or the target are no longer on the same plane.
    
    
    Until the spell ends, you and the target can instantaneously share words, 
    images, sounds, and other sensory messages with one another through the link, 
    and the target recognizes you as the creature it is communicating with. The 
    spell enables a creature with an Intelligence score of at least 1 to understand 
    the meaning of your words and take in the scope of any sensory messages you send
     to it.
    """
    name = "Telepathy"
    level = 8
    casting_time = "1 action"
    casting_range = "Unlimited"
    components = ('V', 'S', 'M')
    materials = """A pair of linked silver rings"""
    duration = "24 hours"
    ritual = False
    magic_school = "Evocation"
    classes = ('Wizard',)


class Teleport(Spell):
    """This spell instantly transports you and up to eight willing creatures of your 
    choice that you can see within range, or a single object that you can see within
     range, to a destination you select. If you target an object, it must be able to
     fit entirely inside a 10-foot cube, and it can’t be held or carried by an 
    unwilling creature.
    
    The destination you choose must be known to you, and it 
    must be on the same plane of existence as you. Your familiarity with the 
    destination determines whether you arrive there successfully. The DM rolls d100 
    and consults the table.
    
    Familiarity 
        Mishap  Similar Area  Off Target  On Target
    Permanent circle   —       — 
            —     01-100
    Associated object    —       —       —       01-100
    Very 
    familiar     01-05      06-13     14-24    25-100
    Seen casually     01-33      
    34-43     44-53    54-100
    Viewed once    01-43      44-53     54-73    74-100
    
    Description       01-43      44-53     54-73    74-100
    False destination  01-50 
          51-100      —      —
    
    Familiarity.
    "Permanent circle" means a permanent 
    teleportation circle whose sigil sequence you know. "Associated object" means 
    that you possess an object taken from the desired destination within the last 
    six months, such as a book from a wizard's library, bed linen from a royal 
    suite, or a chunk of marble from a lich's secret tomb.
    "Very familiar" is a 
    place you have been very often, a place you have carefully studied, or a place 
    you can see when you cast the spell. "Seen casually" is someplace you have seen 
    more than once but with which you aren't very familiar. "Viewed once" is a place
     you have seen once, possibly using magic. "Description" is a place whose 
    location and appearance you know through someone else's description, perhaps 
    from a map.
    "False destination" is a place that doesn't exist. Perhaps you tried
     to scry an enemy's sanctum but instead viewed an illusion, or you are 
    attempting to teleport to a familiar location that no longer exists.
    
    On Target
    
    You and your group (or the target object) appear where you want to.
    
    Off Target
    
    You and your group (or the target object) appear a random distance away from the
     destination in a random direction. Distance off target is 1d10 x 1d10 percent 
    of the distance that was to be traveled. For example, if you tried to travel 120
     miles, landed off target, and rolled a 5 and 3 on the two d10s, then you would 
    be off target by 15 percent, or 18 miles. The DM determines the direction off 
    target randomly by rolling a d8 and designating 1 as north, 2 as northeast, 3 as
     east, and so on around the points of the compass. If you were teleporting to a 
    coastal city and wound up 18 miles out at sea, you could be in trouble.
    
    Similar
     Area
    You and your group (or the target object) wind up in a different area 
    that's visually or thematically similar to the target area. If you are heading 
    for your home laboratory, for example, you might wind up in another wizard's 
    laboratory or in an alchemical supply shop that has many of the same tools and 
    implements as your laboratory. Generally, you appear in the closest similar 
    place, but since the spell has no range limit, you could conceivably wind up 
    anywhere on the plane.
    
    Mishap
    The spell's unpredictable magic results in a 
    difficult journey. Each teleporting creature (or the target object) takes 3d10 
    force damage, and the DM rerolls on the table to see where you wind up (multiple
     mishaps can occur, dealing damage each time).
    """
    name = "Teleport"
    level = 7
    casting_time = "1 action"
    casting_range = "10 feet"
    components = ('V',)
    materials = """"""
    duration = "Instantaneous"
    ritual = False
    magic_school = "Conjuration"
    classes = ('Bard', 'Sorcerer', 'Wizard')


class TeleportationCircle(Spell):
    """As you cast the spell, you draw a 10-foot-diameter circle on the ground 
    inscribed with sigils that link your location to a permanent teleportation 
    circle of your choice whose sigil sequence you know and that is on the same 
    plane of existence as you.
    A shimmering portal opens within the circle you drew 
    and remains open until the end of your next turn. Any creature that enters the 
    portal instantly appears within 5 feet of the destination circle or in the 
    nearest unoccupied space if that space is occupied.
    
    Many major temples, guilds,
     and other important places have permanent teleportation circles inscribed 
    somewhere within their confines. Each such circle includes a unique sigil 
    sequence – a string of magical runes arranged in a particular pattern. When you 
    first gain the ability to cast this spell, you learn the sigil sequences for two
     destinations on the Material Plane, determined by the DM. You can learn 
    additional sigil sequences during your adventures. You can commit a new sigil 
    sequence to memory after studying it for 1 minute.
    
    You can create a permanent 
    teleportation circle by casting this spell in the same location every day for 
    one year. You need not use the circle to teleport when you cast the spell in 
    this way.
    """
    name = "Teleportation Circle"
    level = 5
    casting_time = "1 minute"
    casting_range = "10 feet"
    components = ('V', 'M')
    materials = """Rare chalks and inks infused with precious gems with 50 gp, which the spell consumes"""
    duration = "1 round"
    ritual = False
    magic_school = "Conjuration"
    classes = ('Bard', 'Sorcerer', 'Wizard')


class TempleOfTheGods(Spell):
    """You cause a temple to shimmer into existence on ground you can see within range.
     The temple must fit within an unoccupied cube of space, up to 120 feet on each 
    side. The temple remains until the spell ends. It is dedicated to whatever god, 
    pantheon, or philosophy is represented by the holy symbol used in the casting.
    
    You make all decisions about the temple’s appearance. The interior is enclosed 
    by a floor, walls, and a roof, with one door granting access to the interior and
     as many windows as you wish. Only you and any creatures you designate when you 
    cast the spell can open or close the door.
    The temple’s interior is an open 
    space with an idol or altar at one end. You decide whether the temple is 
    illuminated and whether that illumination is bright light or dim light. The 
    smell of burning incense fills the air within, and the temperature is mild.
    The 
    temple opposes types of creatures you choose when you cast this spell. Choose 
    one or more of the following: celestials, elementals, fey, fiends, or undead. If
     a creature of the chosen type attempts to enter the temple, that creature must 
    make a Charisma saving throw. On a failed save, it can’t enter the temple for 24
     hours. Even if the creature can enter the temple, the magic there hinders it; 
    whenever it makes an attack roll, an ability check, or a saving throw inside the
     temple, it must roll a d4 and subtract the number rolled from the d20 roll.
    In 
    addition, the sensors created by divination spells can’t appear inside the 
    temple, and creatures within can’t be targeted by divination spells.
    Finally, 
    whenever any creature in the temple regains hit points from a spell of 1st level
     or higher, the creature regains additional hit points equal to your Wisdom 
    modifier (minimum 1 hit point).
    The temple is made from opaque magical force 
    that extends into the Ethereal Plane, thus blocking ethereal travel into the 
    temple’s interior. Nothing can physically pass through the temple’s exterior. It
     can’t be dispelled by dispel magic, and antimagic field has no effect on it. A 
    disintegrate spell destroys the temple instantly.
    Casting this spell on the same
     spot every day for a year makes this effect permanent.
    """
    name = "Temple Of The Gods"
    level = 7
    casting_time = "1 hour"
    casting_range = "120 feet"
    components = ('V', 'S', 'M')
    materials = """A holy symbol worth at least 5 gp"""
    duration = "24 hours"
    ritual = False
    magic_school = "Conjuration"
    classes = ('Cleric',)


class TensersFloatingDisk(Spell):
    """This spell creates a circular, horizontal plane of force, 3 feet in diameter and
     1 inch thick, that floats 3 feet above the ground in an unoccupied space of 
    your choice that you can see within range.
    The disk remains for the duration, 
    and can hold up to 500 pounds. If more weight is placed on it, the spell ends, 
    and everything on the disk falls to the ground.
    
    The disk is immobile while you 
    are within 20 feet of it. If you move more than 20 feet away from it, the disk 
    follows you so that it remains within 20 feet of you. It can more across uneven 
    terrain, up or down stairs, slopes and the like, but it can’t cross an elevation
     change of 10 feet or more. For example, the disk can’t move across a 10-foot-
    deep pit, nor could it leave such a pit if it was created at the bottom.
    
    If you
     move more than 100 feet from the disk (typically because it can’t move around 
    an obstacle to follow you), the spell ends.
    """
    name = "Tensers Floating Disk"
    level = 1
    casting_time = "1 action"
    casting_range = "30 feet"
    components = ('V', 'S', 'M')
    materials = """A drop of mercury"""
    duration = "1 hour"
    ritual = True
    magic_school = "Conjuration"
    classes = ('Wizard',)


class TensersTransformation(Spell):
    """You endow yourself with endurance and martial prowess fueled by magic. Until the
     spell ends, you can’t cast spells, and you gain the following benefits:
    - You 
    gain 50 temporary hit points. If any of these remain when the spell ends, they 
    are lost.
    - You have advantage on attack rolls that you make with simple and 
    martial weapons.
    - When you hit a target with a weapon attack, that target takes
     an extra 2d12 force
    damage.
    - You have proficiency with all armor, shields, 
    simple weapons, and martial weapons.
    - You have proficiency in Strength and 
    Constitution saving throws.
    - You can attack twice, instead of once, when you 
    take the Attack action on your turn. You ignore this benefit if you already have
     a feature, like Extra Attack, that gives you extra attacks.
    
    Immediately after 
    the spell ends, you must succeed on a DC 15 Constitution saving throw or suffer 
    one level of exhaustion.
    """
    name = "Tensers Transformation"
    level = 6
    casting_time = "1 action"
    casting_range = "Self"
    components = ('V', 'S', 'M')
    materials = """A few hairs from a bull"""
    duration = "Concentration, up to 10 minutes"
    ritual = False
    magic_school = "Transmutation"
    classes = ('Wizard',)


class Thaumaturgy(Spell):
    """You manifest a minor wonder, a sign of supernatural power, within range. You 
    create one of the following magical effects within range:
    
    * Your voice booms up
     to three times as loud as normal for 1 minute.
    * You cause flames to flicker, 
    brighten, dim, or change color for 1 minute.
    * You cause harmless tremors in the
     ground for 1 minute.
    * You create an instantaneous sound that originates from a
     point of your choice within range, such as a rumble of thunder, the cry of a 
    raven, or ominous whispers.
    * You instantaneously cause an unlocked door or 
    window to fly open or slam shut.
    * You alter the appearance of your eyes for 1 
    minute.
    
    If you cast this spell multiple times, you can have up to three of its 
    1-minute effects active at a time, and you can dismiss such an effect as an 
    action.
    """
    name = "Thaumaturgy"
    level = 0
    casting_time = "1 action"
    casting_range = "30 feet"
    components = ('V',)
    materials = """"""
    duration = "Up to 1 minute"
    ritual = False
    magic_school = "Transmutation"
    classes = ('Cleric',)


class ThornWhip(Spell):
    """You create a long, vine-like whip covered in thorns that lashes out at your 
    command toward a creature in range. Make a melee spell attack against the 
    target. If the attack hits, the creature takes 1d6 piercing damage, and if the 
    creature is Large or smaller, you pull the creature up to 10 feet closer to you.
    
    
    At Higher Levels: This spell’s damage increases by 1d6 when you reach 5th 
    level (2d6), 11th level (3d6), and 17th level (4d6).
    """
    name = "Thorn Whip"
    level = 0
    casting_time = "1 action"
    casting_range = "30 feet"
    components = ('V', 'S', 'M')
    materials = """The stem of a plant with thorns"""
    duration = "Instantaneous"
    ritual = False
    magic_school = "Transmutation"
    classes = ('Druid',)


class ThunderStep(Spell):
    """You teleport yourself to an unoccupied space you can see within range. 
    Immediately after you disappear, a thunderous boom sounds, and each creature 
    within 10 feet of the space you left must make a Constitution saving throw, 
    taking 3d10 thunder damage on a failed save, or half as much damage on a 
    successful one. The thunder can be heard from up to 300 feet away.
    You can bring
     along objects as long as their weight doesn’t exceed what you can carry. You 
    can also teleport one willing creature of your size or smaller who is carrying 
    gear up to its carrying capacity. The creature must be within 5 feet of you when
     you cast this spell, and there must be an unoccupied space within 5 feet of 
    your destination space for the creature to appear in; otherwise, the creature is
     left behind.
    
    At Higher Levels: When you cast this spell using a spell slot of 
    4th level or higher, the damage increases by 1d10 for each slot level above 3rd.
    """
    name = "Thunder Step"
    level = 3
    casting_time = "1 action"
    casting_range = "90 feet"
    components = ('V',)
    materials = """"""
    duration = "Instantaneous"
    ritual = False
    magic_school = "Conjuration"
    classes = ('Sorcerer', 'Warlock', 'Wizard')


class Thunderclap(Spell):
    """You create a burst of thunderous sound, which can be heard 100 feet away. 
    Each 
    creature other than you within 5 feet of you must make a Constitution saving 
    throw. On a failed save, the creature takes 1d6 thunder damage. 
    The spell’s 
    damage increases by 1d6 when you reach 5th level (2d6), 11th level (3d6), and 
    17th level (4d6).
    """
    name = "Thunderclap"
    level = 0
    casting_time = "1 action"
    casting_range = "5 feet"
    components = ('S',)
    materials = """"""
    duration = "Instantaneous"
    ritual = False
    magic_school = "Evocation"
    classes = ('Bard', 'Sorcerer', 'Druid', 'Warlock', 'Wizard')


class ThunderousSmite(Spell):
    """The first time you hit with a melee weapon attack during this spell’s duration, 
    your weapon rings with thunder that is audible within 300 feet of you, and the 
    attack deals an extra 2d6 thunder damage to the target. Additionally, if the 
    target is a creature, it must succeed on a Strength saving throw or be pushed 10
     feet away from you and knocked prone.
    """
    name = "Thunderous Smite"
    level = 1
    casting_time = "1 bonus action"
    casting_range = "Self"
    components = ('V',)
    materials = """"""
    duration = "Concentration, up to 1 minute"
    ritual = False
    magic_school = "Evocation"
    classes = ('Paladin',)


class Thunderwave(Spell):
    """A wave of thunderous force sweeps out from you.
    Each creature in a 15-foot cube 
    originating from you must make a Constitution saving throw. On a failed save, a 
    creature takes 2d8 thunder damage and is pushed 10 feet away from you. On a 
    successful save, the creature takes half as much damage and isn’t pushed.
    
    In 
    addition, unsecured objects that are completely within the area of effect are 
    automatically pushed 10 feet away from you by the spell’s effect, and the spell 
    emits a thunderous boom audible out to 300 feet.
    
    At Higher Levels: When you 
    cast this spell using a spell slot of 2nd level or higher, the damage increases 
    by 1d8 for each slot level above 1st.
    """
    name = "Thunderwave"
    level = 1
    casting_time = "1 action"
    casting_range = "Self (15-foot cube)"
    components = ('V', 'S')
    materials = """"""
    duration = "Instantaneous"
    ritual = False
    magic_school = "Evocation"
    classes = ('Bard', 'Druid', 'Sorcerer', 'Wizard')


class TidalWave(Spell):
    """You conjure up a wave of water that crashes down on an area within range. The 
    area can be up to 30 feet long, up to 10 feet wide, and up to 10 feet tall. Each
     creature in that area must make a Dexterity saving throw. On a failed save, a 
    creature takes 4d8 bludgeoning damage and is knocked prone. On a successful 
    save, a creature takes half as much damage and isn’t knocked prone. The water 
    then spreads out across the ground in all directions, extinguishing unprotected 
    flames in its area and within 30 feet of it, and then it vanishes.
    """
    name = "Tidal Wave"
    level = 3
    casting_time = "1 action"
    casting_range = "120 feet"
    components = ('V', 'S', 'M')
    materials = """A drop of water"""
    duration = "Instantaneous"
    ritual = False
    magic_school = "Conjuration"
    classes = ('Druid', 'Wizard', 'Sorcerer')


class TimeStop(Spell):
    """You briefly stop the flow of time for everyone but yourself. No time passes for 
    other creatures, while you take 1d4 + 1 turns in a row, during which you can use
     actions and move as normal.
    
    This spell ends if one of the actions you use 
    during this period, or any effects that you create during this period, affects a
     creature other than you or an object being worn or carried by someone other 
    than you. In addition, the spell ends if you move to a place more than 1,000 
    feet from the location where you cast it.
    """
    name = "Time Stop"
    level = 9
    casting_time = "1 action"
    casting_range = "Self"
    components = ('V',)
    materials = """"""
    duration = "Instantaneous"
    ritual = False
    magic_school = "Transmutation"
    classes = ('Sorcerer', 'Wizard')


class TinyServant(Spell):
    """You touch one Tiny, nonmagical object that isn’t attached to another object or a
     surface and isn’t being carried by another creature. The target animates and 
    sprouts little arms and legs, becoming a creature under your control until the 
    spell ends or the creature drops to 0 hit points. See the stat block for its 
    statistics.
    As a bonus action, you can mentally command the creature if it is 
    within 120 feet of you. (If you control multiple creatures with this spell, you 
    can command any or all of them at the same time, issuing the same command to 
    each one.) You decide what action the creature will take and where it will move 
    during its next turn, or you can issue a simple, general command, such as to 
    fetch a key, stand watch, or stack some books. If you issue no commands, the 
    servant does nothing other than defend itself against hostile creatures. Once 
    given an order, the servant continues to follow that order until its task is 
    complete.
    When the creature drops to 0 hit points, it reverts to its original 
    form, and any remaining damage carries over to that form.
    
    At Higher Levels: 
    When you cast this spell using a spell slot of 4th level or higher, you can 
    animate two additional objects for each slot level above 3rd.
    """
    name = "Tiny Servant"
    level = 3
    casting_time = "1 minute"
    casting_range = "Touch"
    components = ('V', 'S')
    materials = """"""
    duration = "8 hours"
    ritual = False
    magic_school = "Transmutation"
    classes = ('Wizard',)


class TollTheDead(Spell):
    """You point at one creature you can see within range, and the sound of a dolorous 
    bell fills the air around it for a moment. The target must succeed on a Wisdom 
    saving throw or take 1d8 necrotic damage. If the target is missing any of its 
    hit points, it instead takes 1d12 necrotic damage.
    The spell’s damage increases 
    by one die when you reach 5th level (2d8 or 2d12), 11th level (3d8 or 3d12), and
     17th level (4d8 or 4d12).
    """
    name = "Toll The Dead"
    level = 0
    casting_time = "1 action"
    casting_range = "60 feet"
    components = ('V', 'S')
    materials = """"""
    duration = "Instantaneous"
    ritual = False
    magic_school = "Necromancy"
    classes = ('Warlock', 'Wizard', 'Cleric')


class Tongues(Spell):
    """This spell grants the creature you touch the ability to understand any spoken 
    language it hears. Moreover, when the target speaks, any creature that knows at 
    least one language and can hear the target understands what it says.
    """
    name = "Tongues"
    level = 3
    casting_time = "1 action"
    casting_range = "Touch"
    components = ('V', 'M')
    materials = """A small clay model of a ziggurat"""
    duration = "1 hour"
    ritual = False
    magic_school = "Divination"
    classes = ('Bard', 'Cleric', 'Sorcerer', 'Warlock', 'Wizard')


class TransmuteRock(Spell):
    """You choose an area of stone or mud that you can see that fits within a 40-foot 
    cube and is within range, and choose one of the following effects.
    Transmute 
    Rock to Mud. Nonmagical rock of any sort in the area becomes an equal volume of 
    thick, flowing mud that remains for the spell’s duration.
    The ground in the 
    spell’s area becomes muddy enough that creatures can sink into it. Each foot 
    that a creature moves through the mud costs 4 feet of movement, and any creature
     on the ground when you cast the spell must make a Strength saving throw. A 
    creature must also make the saving throw when it moves into the area for the 
    first time on a turn or ends its turn there. On a failed save, a creature sinks 
    into the mud and is restrained, though it can use an action to end the 
    restrained condition on itself by pulling itself free of the mud.
    If you cast 
    the spell on a ceiling, the mud falls. Any creature under the mud when it falls 
    must make a Dexterity saving throw. A creature takes 4d8 bludgeoning damage on a
     failed save, or half as much damage on a successful one.
    Transmute Mud to Rock.
     Nonmagical mud or quicksand in the area no more than 10 feet deep transforms 
    into soft stone for the spell’s duration. Any creature in the mud when it 
    transforms must make a Dexterity saving throw. On a successful save, a creature 
    is shunted safely to the surface in an unoccupied space. On a failed save, a 
    creature becomes restrained by the rock. A restrained creature, or another 
    creature within reach, can use an action to try to break the rock by succeeding 
    on a DC 20 Strength check or by dealing damage to it. The rock has AC 15 and 25 
    hit points, and it is immune to poison and psychic damage.
    """
    name = "Transmute Rock"
    level = 5
    casting_time = "1 action"
    casting_range = "120 feet"
    components = ('V', 'S', 'M')
    materials = """Clay and water"""
    duration = "Instantaneous"
    ritual = False
    magic_school = "Transmutation"
    classes = ('Druid', 'Wizard')


class TransportViaPlants(Spell):
    """This spell creates a magical link between a Large or larger inanimate plant 
    within range and another plant, at any distance, on the same plane of existence.
     You must have seen or touched the destination plant at least once before. For 
    the duration, any creature can step into the target plant and exit from the 
    destination plant by using 5 feet of movement.
    """
    name = "Transport Via Plants"
    level = 6
    casting_time = "1 action"
    casting_range = "10 feet"
    components = ('V', 'S')
    materials = """"""
    duration = "1 round"
    ritual = False
    magic_school = "Conjuration"
    classes = ('Druid',)


class TreeStride(Spell):
    """You gain the ability to enter a tree and move from inside it to inside another 
    tree of the same kind within 500 feet.
    Both trees must be living and at least 
    the same size as you. You must use 5 feet of movement to enter a tree. You 
    instantly know the location of all other trees of the same kind within 500 feet 
    and, as part of the move used to enter the tree, can either pass into one of 
    those trees or step out of the tree you’re in. You appear in a spot of your 
    choice within 5 feet of the destination tree, using another 5 feet of movement. 
    If you have no movement left, you appear within 5 feet of the tree you entered.
    
    
    You can use this transportation ability once per round for the duration. You 
    must end each turn outside a tree.
    """
    name = "Tree Stride"
    level = 5
    casting_time = "1 action"
    casting_range = "Self"
    components = ('V', 'S')
    materials = """"""
    duration = "Concentration, up to 1 minute"
    ritual = False
    magic_school = "Conjuration"
    classes = ('Druid', 'Ranger')


class TruePolymorph(Spell):
    """Choose one creature or nonmagical object that you can see within range. You 
    transform the creature into a different creature, the creature into an object, 
    or the object into a creature (the object must be neither worn nor carried by 
    another creature). The transformation lasts for the duration, or until the 
    target drops to 0 hit points or dies. If you concentrate on this spell for the 
    full duration, the transformation becomes permanent.
    
    Shapechangers aren’t 
    affected by this spell. An unwilling creature can make a Wisdom saving throw, 
    and if it succeeds, it isn’t affected by this spell.
    
    Creature into Creature
    If 
    you turn a creature into another kind of creature, the new form can be any kind 
    you choose whose challenge rating is equal to or less than the target’s (or its 
    level, if the target doesn’t have a challenge rating). The target’s game 
    statistics, including mental ability scores, are replaced by the statistics of 
    the new form. It retains its alignment and personality.
    The target assumes the 
    hit points of its new form, and when it reverts to its normal form, the creature
     returns to the number of hit points it had before it transformed. If it reverts
     as a result of dropping to 0 hit points, any excess damage carries over to its 
    normal form. As long as the excess damage doesn’t reduce the creature’s normal 
    form to 0 hit points, it isn’t knocked unconscious.
    The creature is limited in 
    the actions it can perform by the nature of its new form, and it can’t speak, 
    cast spells, or take any other action that requires hands or speech unless its 
    new form is capable of such actions.
    The target’s gear melds into the new form. 
    The creature can’t activate, use, wield, or otherwise benefit from any of its 
    equipment.
    
    Object into Creature
    You can turn an object into any kind of 
    creature, as long as the creature’s size is no larger than the object’s size and
     the creature’s challenge rating is 9 or lower. The creature is friendly to you 
    and your companions. It acts on each of your turns. You decide what action it 
    takes and how it moves. The DM has the creature’s statistics and resolves all of
     its actions and movement.
    If the spell becomes permanent, you no longer control
     the creature. It might remain friendly to you, depending on how you have 
    treated it.
    
    Creature into Object
    If you turn a creature into an object, it 
    transforms along with whatever it is wearing and carrying into that form. The 
    creature’s statistics become those of the object, and the creature has no memory
     of time spent in this form, after the spell ends and it returns to its normal 
    form.
    
    This spell can’t affect a target that has 0 hit points.
    """
    name = "True Polymorph"
    level = 9
    casting_time = "1 action"
    casting_range = "30 feet"
    components = ('V', 'S', 'M')
    materials = """A drop of mercury, a dollop of gum arabic, and a wisp of smoke"""
    duration = "Concentration, up to 1 hour"
    ritual = False
    magic_school = "Transmutation"
    classes = ('Bard', 'Warlock', 'Wizard')


class TrueResurrection(Spell):
    """You touch a creature that has been dead for no longer than 200 years and that 
    died for any reason except old age. If the creature’s soul is free and willing, 
    the creature is restored to life with all its hit points.
    
    This spell closes all
     wounds, neutralizes any poison, cures all diseases, and lifts any curses 
    affecting the creature when it died. The spell replaces damaged or missing 
    organs or limbs.
    
    The spell can even provide a new body if the original no 
    longer exists, in which case you must speak the creature’s name. The creature 
    then appears in an unoccupied space you choose within 10 feet of you.
    """
    name = "True Resurrection"
    level = 9
    casting_time = "1 hour"
    casting_range = "Touch"
    components = ('V', 'S', 'M')
    materials = """A sprinkle of holy water and diamonds worth at least 25,000 gp, which the spell consumes"""
    duration = "Instantaneous"
    ritual = False
    magic_school = "Necromancy"
    classes = ('Cleric', 'Druid')


class TrueSeeing(Spell):
    """This spell gives the willing creature you touch the ability to see things as 
    they actually are. For the duration, the creature has truesight,  notices secret
     doors hidden by magic, and can see into the Ethereal Plane, all out to a range 
    of 120 feet.
    """
    name = "True Seeing"
    level = 6
    casting_time = "1 action"
    casting_range = "Touch"
    components = ('V', 'S', 'M')
    materials = """An ointment for the eyes that costs 25 gp; is made from mushroom powder, saffron, and fat; and is consumed by the spell"""
    duration = "1 hour"
    ritual = False
    magic_school = "Divination"
    classes = ('Bard', 'Cleric', 'Sorcerer', 'Warlock', 'Wizard')


class TrueStrike(Spell):
    """You extend your hand and point a finger at a target in range. Your magic grants 
    you a brief insight into the target’s defenses. On your next turn, you gain 
    advantage on your first attack roll against the target, provided that this spell
     hasn’t ended.
    """
    name = "True Strike"
    level = 0
    casting_time = "1 action"
    casting_range = "30 feet"
    components = ('S',)
    materials = """"""
    duration = "Concentration, up to 1 round"
    ritual = False
    magic_school = "Divination"
    classes = ('Bard', 'Sorcerer', 'Warlock', 'Wizard')


class Tsunami(Spell):
    """A wall of water springs into existence at a point you choose within range. You 
    can make the wall up to 300 feet long, 300 feet high, and 50 feet thick. The 
    wall lasts for the duration.
    
    When the wall appears, each creature within its 
    area must make a Strength saving throw. On a failed save, a creature takes 6d10 
    bludgeoning damage, or half as much damage on a successful save.
    
    At the start 
    of each of your turns after the wall appears, the wall, along with any creatures
     in it, moves 50 feet away from you. Any Huge or smaller creature inside the 
    wall or whose space the wall enters when it moves must succeed on a Strength 
    saving throw or take 5d10 bludgeoning damage. A creature can take this damage 
    only once per round. At the end of the turn, the wall’s height is reduced by 50 
    feet, and the damage creatures take from the spell on subsequent rounds is 
    reduced by 1d10. When the wall reaches 0 feet in height, the spell ends.
    
    A 
    creature caught in the wall can move by swimming. Because of the force of the 
    wave, though, the creature must make a successful Strength (Athletics) check 
    against your spell save DC in order to move at all. If it fails the check, it 
    can’t move. A creature that moves out of the area falls to the ground.
    """
    name = "Tsunami"
    level = 8
    casting_time = "1 minute"
    casting_range = "Sight"
    components = ('V', 'S')
    materials = """"""
    duration = "Concentration, up to 6 rounds"
    ritual = False
    magic_school = "Conjuration"
    classes = ('Druid',)


