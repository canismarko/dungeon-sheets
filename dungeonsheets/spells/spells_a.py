from .spells import Spell


class AbiDalzimsHorridWilting(Spell):
    """You draw the moisture from every creature in a 30-foot cube centered on a point 
    you choose within range. Each creature in that area must make a Constitution 
    saving throw. Constructs and undead aren’t affected, and plants and water 
    elementals make this saving throw with disadvantage. A creature takes 12d8 
    necrotic damage on a failed save, or half as much damage on a successful one. 
    
    Nonmagical plants in the area that aren’t creatures, such as trees and shrubs, 
    wither and die instantly.
    """
    name = "Abi-Dalzims Horrid Wilting"
    level = 8
    casting_time = "1 action"
    casting_range = "150 feet"
    components = ('V', 'S', 'M')
    materials = """A bit of sponge"""
    duration = "Instantaneous"
    ritual = False
    magic_school = "Necromancy"
    classes = ('Sorcerer', 'Wizard')


class AbsorbElements(Spell):
    """1 Reaction, which you take when you take acid, cold, fire, lightning, or thunder
     damage
    
    The spell captures some of the incoming energy, lessening its effect on
     you and storing it for your next melee attack. You have resistance to the 
    triggering damage type until the start of your next turn. Also, the first time 
    you hit with a melee attack on your next turn, the target takes an extra 1d6 
    damage of the triggering type, and the spell ends.
    
    At Higher Levels: When you 
    cast this spell using a spell slot of 2nd level or higher, the extra damage 
    increases by 1d6 for each slot level above 1st.
    """
    name = "Absorb Elements"
    level = 1
    casting_time = "Special"
    casting_range = "Self"
    components = ('S',)
    materials = """"""
    duration = "1 round"
    ritual = False
    magic_school = "Abjuration"
    classes = ('Druid', 'Ranger', 'Wizard', 'Sorcerer')


class AcidSplash(Spell):
    """You hurl a bubble of acid. 
    Choose one creature within range, or choose two 
    creatures within range that are within 5 feet of each other. A target must 
    succeed on a Dexterity saving throw or take 1d6 acid damage.
    
    At Higher Levels: 
    This spell’s damage increases by 1d6 when you reach 5th level (2d6), 11th level 
    (3d6), and 17th level (4d6).
    """
    name = "Acid Splash"
    level = 0
    casting_time = "1 action"
    casting_range = "60 feet"
    components = ('V', 'S')
    materials = """"""
    duration = "Instantaneous"
    ritual = False
    magic_school = "Conjuration"
    classes = ('Sorcerer', 'Wizard')


class AganazzarsScorcher(Spell):
    """A line of roaring flame 30 feet long and 5 feet wide emanates from you in a 
    direction you choose. 
    Each creature in the line must make a Dexterity saving 
    throw. A creature takes 3d8 fire damage on a failed save, or half as much damage
     on a successful one.
    
    At Higher Levels: When you cast this spell using a spell 
    slot of 3rd level or higher, the damage increases by 1d8 for each slot level 
    above 2nd.
    """
    name = "Aganazzars Scorcher"
    level = 2
    casting_time = "1 action"
    casting_range = "30 feet"
    components = ('V', 'S', 'M')
    materials = """A red dragon’s scale"""
    duration = "Instantaneous"
    ritual = False
    magic_school = "Evocation"
    classes = ('Sorcerer', 'Wizard')


class Aid(Spell):
    """Your spell bolsters your allies with toughness and resolve. 
    Choose up to three 
    creatures within range. Each target’s hit point maximum and current hit points 
    increase by 5 for the duration.
    
    At Higher Levels: When you cast this spell 
    using a spell slot of 3rd level or higher, a target’s hit points increase by an 
    additional 5 for each slot level above 2nd.
    """
    name = "Aid"
    level = 2
    casting_time = "1 action"
    casting_range = "30 feet"
    components = ('V', 'S', 'M')
    materials = """A tiny strip of white cloth"""
    duration = "8 hours"
    ritual = False
    magic_school = "Abjuration"
    classes = ('Cleric', 'Paladin')


class Alarm(Spell):
    """You set an alarm against unwanted intrusion. 
    Choose a door, a window, or an 
    area within range that is no larger than a 20-foot cube. Until the spell ends, 
    an alarm alerts you whenever a tiny or larger creature touches or enters the 
    warded area. When you cast the spell, you can designate creatures that won’t set
     off the alarm. You also choose whether the alarm is mental or audible. 
    
    A 
    mental alarm alerts you with a ping in your mind if you are within 1 mile of the
     warded area. This ping awakens you if you are sleeping. 
    An audible alarm 
    produces the sound of a hand bell for 10 seconds within 60 feet.
    """
    name = "Alarm"
    level = 1
    casting_time = "1 minute"
    casting_range = "30 feet"
    components = ('V', 'S', 'M')
    materials = """A tiny bell and a piece of fine silver wire"""
    duration = "8 hours"
    ritual = True
    magic_school = "Abjuration"
    classes = ('Ranger', 'Wizard')


class AlterSelf(Spell):
    """You assume a different form.
    When you cast the spell, choose one of the 
    following options, the effects of which last for the duration of the spell. 
    While the spell lasts, you can end one option as an action to gain the benefits 
    of a different one.
    
    Aquatic Adaptation. You adapt your body to an aquatic 
    environment, sprouting gills, and growing webbing between your fingers. You can 
    breathe underwater and gain a swimming speed equal to your walking speed.
    Change
     Appearance. You transform your appearance. You decide what you look like, 
    including your height, weight, facial features, sound of your voice, hair 
    length, coloration, and distinguishing characteristics, if any. You can make 
    yourself appear as a member of another race, though none of your statistics 
    change. You also don’t appear as a creature of a different size than you, and 
    your basic shape stays the same; if you're bipedal, you can’t use this spell to 
    become quadrupedal, for instance. At any time for the duration of the spell, you
     can use your action to change your appearance in this way again.
    Natural 
    Weapons. You grow claws, fangs, spines, horns, or a different natural weapon of 
    your choice. Your unarmed strikes deal 1d6 bludgeoning, piercing, or slashing 
    damage, as appropriate to the natural weapon you chose, and you are proficient 
    with your unarmed strikes. Finally, the natural weapon is magic and you have a 
    +1 bonus to the attack and damage rolls you make using it.
    """
    name = "Alter Self"
    level = 2
    casting_time = "1 action"
    casting_range = "Self"
    components = ('V', 'S')
    materials = """"""
    duration = "Concentration, up to 1 hour"
    ritual = False
    magic_school = "Transmutation"
    classes = ('Sorcerer', 'Wizard')


class AnimalFriendship(Spell):
    """This spell lets you convince a beast that you mean it no harm.
    Choose a beast 
    that you can see within range. It must see and hear you. If the beast’s 
    Intelligence is 4 or higher, the spell fails. Otherwise, the beast must succeed 
    on a Wisdom saving throw or be charmed by you for the spell’s duration. If you 
    or one of your companions harms the target, the spell ends.
    
    At Higher Levels: 
    When you cast this spell using a spell slot of 2nd level or higher, you can 
    affect one additional beast for each slot level above 1st.
    """
    name = "Animal Friendship"
    level = 1
    casting_time = "1 action"
    casting_range = "30 feet"
    components = ('V', 'S', 'M')
    materials = """A morsel of food"""
    duration = "Instantaneous"
    ritual = False
    magic_school = "Enchantment"
    classes = ('Bard', 'Druid', 'Ranger')


class AnimalMessenger(Spell):
    """By means of this spell, you use an animal to deliver a message.
    Choose a Tiny 
    beast you can see within range, such as a squirrel, a blue ray, or a bat. You 
    specify a location, which you must have visited, and a recipient who matches a 
    general description, such as a man or woman dressed in the uniform of the town 
    guard or a red-haired dwarf wearing a pointed hat. You also speak a message of 
    up to twenty-five words. The target beast travels for the duration of the spell 
    towards the specified location, covering about 50 miles per 24 hours for a 
    flying messenger or 25 miles for other animals.
    
    When the messenger arrives, it 
    delivers your message to the creature that you described, replicating the sound 
    of your voice. The messenger speaks only to a creature matching the description 
    you gave. If the messenger doesn’t reach its destination before the spell ends, 
    the message is lost, and the beast makes it way back to where you cast this 
    spell.
    
    At Higher Levels: If you cast this spell using a spell slot of 3rd level
     or higher, the duration of the spell increases by 48 hours for each slot level 
    above 2nd.
    """
    name = "Animal Messenger"
    level = 2
    casting_time = "1 action"
    casting_range = "30 feet"
    components = ('V', 'S', 'M')
    materials = """A morsel of food"""
    duration = "24 hours"
    ritual = True
    magic_school = "Enchantment"
    classes = ('Bard', 'Druid', 'Ranger')


class AnimalShapes(Spell):
    """Your magic turns others into beasts. 
    Choose any number of willing creatures 
    that you can see within range. You transform each target into the form of a 
    large or smaller beast with a challenge rating of 4 or lower. On subsequent 
    turns, you can use your actions to transform affected creatures into new forms. 
    
    
    The transformation lasts for the duration for each target, or until the target
     drops to 0 hit points or dies. You can choose a different form for each target.
     A target’s game statistics are replaced by the statistics of the chosen beast, 
    though the target retains its alignment and Intelligence, Wisdom, and Charisma 
    scores. The target assumes the hit points of its new form, and when it reverts 
    to its normal form, it returns to the number of hit point it had before it 
    transformed. If it reverts as a result of dropping to 0 hit points, any excess 
    damage carries over to its normal form. As long as the excess damage doesn’t 
    reduce the creature’s normal form to 0 hit points, it isn’t knocked unconcious. 
    The creature is limited in the actions it can perform by the nature of its new 
    form, and it can’t speak or cast spells. 
     
    The target’s gear melds into the new
     form. The target can’t activate, wield, or otherwise benefit from any of its 
    equipment.
    """
    name = "Animal Shapes"
    level = 8
    casting_time = "1 action"
    casting_range = "30 feet"
    components = ('V', 'S')
    materials = """"""
    duration = "Concentration, up to 24 hours"
    ritual = False
    magic_school = "Transmutation"
    classes = ('Druid',)


class AnimateDead(Spell):
    """This spell creates an undead servant. 
    Choose a pile of bones or a corpse of a 
    Medium or Small humanoid within range. Your spell imbues the target with a foul 
    mimicry of life, raising it as an undead creature. The target becomes a skeleton
     if you chose bones or a zombie if you chose a corpse (the DM has the creature’s
     game statistics). 
    
    On each of your turns, you can use a bonus action to 
    mentally command any creature you made with this spell if the creature is within
     60 feet of you (if you control multiple creatures, you can command any or all 
    of them at the same time, issuing the same command to each one). You decide what
     action the creature will take and where it will move during its next turn, or 
    you can issue a general command, such as to guard a particular chamber or 
    corridor. If you issue no commands, the creature only defends itself against 
    hostile creatures. Once given an order, the creature continues to follow it 
    until its task is complete.
    
    The creature is under your control for 24 hours, 
    after which it stops obeying any command you’ve given it. To maintain the 
    control of the creature for another 24 hours, you must cast this spell on the 
    creature again before the current 24-hour period ends. This use of the spell 
    reasserts your control over up to four creatures you have animated with this 
    spell, rather than animating a new one.
    
    At Higher Levels: When you cast this 
    spell using a spell slot of 4th level or higher, you animate or reassert control
     over two additional undead creatures for each slot level above 3rd. Each of the
     creatures must come from a different corpse or pile of bones.
    """
    name = "Animate Dead"
    level = 3
    casting_time = "1 minute"
    casting_range = "10 feet"
    components = ('V', 'S', 'M')
    materials = """A drop of blood, a piece of flesh, and a pinch of bone dust"""
    duration = "Instantaneous"
    ritual = False
    magic_school = "Necromancy"
    classes = ('Cleric', 'Wizard')


class AnimateObjects(Spell):
    """Objects come to life at your command. 
    Choose up to ten nonmagical objects 
    within range that are not being worn or carried. Medium targets count as two 
    objects, Large targets count as four objects, Huge targets count as eight 
    objects. You can’t animate any object larger than Huge. Each target animates and
     becomes a creature under your control until the spell ends or until reduced to 
    0 hit points. 
    
    As a bonus action, you can mentally command any creature you 
    made with this spell if the creature is within 500 feet of you (if you control 
    multiple creatures, you can command any or all of them at the same time, issuing
     the same command to each one). You decide what action the creature will take 
    and where it will move during its next turn, or you can issue a general command,
     such as to guard a particular chamber or corridor. If you issue no commands, 
    the creature only defends itself against hostile creatures. Once given an order,
     the creature continues to follow it until its task is complete. 
    
    Animated 
    Object Statistics 
    Tiny – HP: 20, AC: 18, Attack: +8 to hit, 1d4 + 4 damage, 
    Str: 4, Dex: 18 
    Small – HP: 25, AC: 16, Attack: +6 to hit, 1d8 + 2 damage, Str:
     6, Dex: 14 
    Medium – HP: 40, AC: 13, Attack: +5 to hit, 2d6 + 1 damage, Str: 
    10, Dex: 12 
    Large – HP: 50, AC: 10, Attack: +6 to hit, 2d10 + 2 damage, Str: 
    14, Dex: 10 
    Huge – HP: 80, AC: 10, Attack: +8 to hit, 2d12 + 4 damage, Str: 18,
     Dex: 6 
    
    An animated object is a construct with AC, hit points, attacks, 
    Strength, and Dexterity determine by its size. Its Constitution is 10 and its 
    Intelligence and Wisdom are 3, and its Charisma is 1. Its speed is 30 feet; if 
    the objects lack legs or other appendages it can use for locomotion, it instead 
    has a flying speed of 30 feet and can hover. If the object is securely attached 
    to a surface or larger object, such as a chain bolted to a wall, its speed is 0.
     It has blindsight with a radius of 30 feet and is blind beyond that distance. 
    When the animated object drops to 0 hit points, it reverts to its original 
    object form, and any remaining damage carries over to its original object form.
     
    
    If you command an object to attack, it can make a single melee attack against
     a creature within 5 feet of it. It makes a slam attack with an attack bonus and
     bludgeoning damage determine by its size. The DM might rule that a specific 
    object inflicts slashing or piercing damage based on its form.
    
    At Higher 
    Levels: If you cast this spell using a spell slot of 6th level or higher, you 
    can animate two additional objects for each slot level above 5th.
    """
    name = "Animate Objects"
    level = 5
    casting_time = "1 action"
    casting_range = "120 feet"
    components = ('V', 'S')
    materials = """"""
    duration = "Concentration, up to 1 minute"
    ritual = False
    magic_school = "Transmutation"
    classes = ('Bard', 'Sorcerer', 'Wizard')


class AntilifeShell(Spell):
    """A shimmering barrier extends out from you in a 10-foot radius and moves with 
    you, remaining centered on you and hedging out creatures other than undead and 
    constructs. 
    The barrier lasts for the duration. The barrier prevents an 
    affected creature from passing or reaching through. An affected creature can 
    cast spells or make attacks with ranged or reach weapons through the barrier. 
    
    If you move so that an affect creature is forced to pass through the barrier, 
    the spell ends.
    """
    name = "Antilife Shell"
    level = 5
    casting_time = "1 action"
    casting_range = "Self (10-foot radius)"
    components = ('V', 'S')
    materials = """"""
    duration = "Concentration, up to 1 hour"
    ritual = False
    magic_school = "Abjuration"
    classes = ('Druid',)


class AntimagicField(Spell):
    """A 10-foot-radius invisible sphere of antimagic surrounds you. 
    This area is 
    divorced from the magical energy that suffeses the multiverse. Within the 
    sphere, spells can’t be cast, summoned creatures disappear, and even magic items
     become mundane. Until the spell ends, the spere moves with you, centered on 
    you. 
    Spells and other magical effects, except those created by an artifact or a
     deity, are suppressed in the sphere and can’t protrude into it. A slot expended
     to cast a suppressed spell is consumed. While an effect is suppressed, it 
    doesn’t function, but the time it spends suppressed counts against its duration.
     
    
    Targeted Effects. 
    Spells and other magical effects, such as magic missle and
     charm person, that target a creature or an object in the sphere have no effect 
    on that target. 
    
    Areas of Magic. 
    The area of another spell or magical effect, 
    such as fireball, can’t extend into the sphere. If the sphere overlaps an area 
    of magic, the part of the area that is covered by the sphere is suppressed. For 
    example, the flames created by a wall of fire are suppressed within the sphere, 
    creating a gap in the wall if the overlap is large enough. 
    
    Spells. 
     Any 
    active spell or other magical effect on a creature or an object in the sphere is
     suppressed while the creature or object is in it. 
    
    Magic Items. 
    The 
    properties and powers of magic items are suppressed in the sphere. Forexample, a
     +1 longsword in the sphere functions as a nonmagical longsword. A magic 
    weapon’s properties and powers are suppressed if it is used against a target in 
    the sphere or wielded by an attacker in the sphere. If a magic weapon or piece 
    of magic ammunition fully leaves the sphere (For example, if you fire a magic 
    arrow or throw a magic spear at a target outside the sphere), the magic of the 
    item ceases to be supressed as soon as it exits. 
    
    Magical Travel. 
    
    Teleportation and planar travel fail to work in the sphere, whether the sphere 
    is the destination or the departure point for such magical travel. A portal to 
    another location, world, or plane of existence, as well as an opening to an 
    extradimensional space such as that created by the rope trick spells, 
    temporarily closes while in the sphere. 
    
    Creatures and Objects. 
    A creature or 
    object summoned or created by magic temporarily winks out of existence in the 
    sphere. Such a creature instantly reappears once the space the creature occupied
     is no longer withinthe sphere. 
    
    Dispel Magic. 
    Spells and magical effects such
     as dispel magic have no effect on the sphere. Likewise, the spheres created by 
    different antimagic field spells don’t nullify each other.
    """
    name = "Antimagic Field"
    level = 8
    casting_time = "1 action"
    casting_range = "Self (10-foot-radius sphere)"
    components = ('V', 'SM')
    materials = """A pinch of powdered iron or iron filings"""
    duration = "Concentration, up to 1 hour"
    ritual = False
    magic_school = "Abjuration"
    classes = ('Cleric', 'Wizard')


class Antipathysympathy(Spell):
    """This spell attracts or repels creatures of your choice. 
    You target something 
    within range, either a Huge or smaller object or creature or an area that is no 
    larger than a 200-foot cube. Then specify a kind of intelligent creature, such 
    as red dragons, goblins, or vampires. You invest the target with an aura that 
    either attracts or repels the specified creatures for the duration. Choose 
    antipathy or sympathy as the aura’s effect. 
    
    Antipathy. 
    The enchantment causes
     creatures of the kind you designated to feel an intense urge to leave the area 
    and avoid the target. When such a creature can see the target or comes within 60
     feet of it, the creature must succeed on a Wisdom saving throw or 
    become frightened. The creature remains frightened while it can see the target 
    or is within 60 feet of it. While frightened by the target, the creature must 
    use its movement to move to the nearest safe spot from which it can’t see the 
    target. If the creature moves more than 60 feet from the target and can’t see 
    it, the creature is no longer frightened, but the creature becomes frightened 
    again if it regains sight of the target or moves within 60 feet of it. 
    
    
    Sympathy. 
    The enchantment causes the specified creatures to feel an intense 
    urge to approach the target while within 60 feet of it or able to see it. When 
    such a creature can see the target or comes within 60 feet o fit, the creature 
    must succeed on a Wisdom saving throw or use its movement on each of its turns 
    to enter the area or move within reach of the target. When the creature has done
     so, it can’t willingly move away from the target. If the target damages or 
    otherwise harms an affected creature, the affected creature can make a 
    Wisdom saving throw to end the effect, as described below. 
    
    Ending the Effect.
     
    If an affected creature ends its turn while not within 60 feet of the target 
    or able to see it, the creature makes a Wisdom saving throw. On a successful 
    save, the creature is no longer affected by the target and recognizes the 
    feeling of repugnance or attraction as magical. In addition, a creature affected
     by the spell is allowed another Wisdom saving throw every 24 hours while the 
    spell persists. 
    A creature that successfully saves against this effect is 
    immune to it for 1 minute, after which time it can be affected again.
    """
    name = "Antipathysympathy"
    level = 8
    casting_time = "1 hour"
    casting_range = "60 feet"
    components = ('V', 'S', 'M')
    materials = """Either a lump of alum soaked in vinegar for the antipathy effect or a drop of honey for the sympathy effect"""
    duration = "10 days"
    ritual = False
    magic_school = "Enchantment"
    classes = ('Druid', 'Wizard')


class ArcaneEye(Spell):
    """You create an invisible, magical eye within range that hovers in the air for the
     duration. 
    You mentally receive visual information from the eye, which has 
    normal vision and darkvision out to 30 feet. The eye can look in every 
    direction. 
    As an action, you can move the eye up to 30 feet in any direction. 
    There is no limit to how far away from you the eye can move, but it can’t enter 
    another plane of existence. A solid barrier blocks the eye’s movement, but the 
    eye can pass through an opening as small as 1 inch in diameter.
    """
    name = "Arcane Eye"
    level = 4
    casting_time = "1 action"
    casting_range = "30 feet"
    components = ('V', 'S', 'M')
    materials = """A bit of bat fur"""
    duration = "Concentration, up to 1 hour"
    ritual = False
    magic_school = "Divination"
    classes = ('Wizard',)


class ArcaneGate(Spell):
    """You create linked teleportation portals that remain open for the duration. 
    
    Choose two points on the ground that you can see, one point within 10 feet of 
    you and one point within 500 feet of you. A circular portal, 10 feet in 
    diameter, opens over each point. If the portal would open in the space occupied 
    by a creature, the spell fails, and the casting is lost. 
    
     The portals are two-
    dimensional glowing rings filled with mist, hovering inches from the ground and 
    perpendicular to it at the points you choose. A ring is visible only from one 
    side (your choice), which is the side that functions as a portal. 
     
    Any 
    creature or object entering the portal exits from the other portal as if the two
     were adjacent to each other; passing through a portal from the nonportal side 
    has no effect. The mist that fills each portal is opaque and blocks vision 
    through it. On your turn, you can rotate the rings as a bonus action so that the
     active side faces in a different direction.
    """
    name = "Arcane Gate"
    level = 6
    casting_time = "1 action"
    casting_range = "500 feet"
    components = ('V', 'S')
    materials = """"""
    duration = "Concentration, up to 10 minutes"
    ritual = False
    magic_school = "Conjuration"
    classes = ('Sorcerer', 'Warlock', 'Wizard')


class ArcaneLock(Spell):
    """You touch a closed door, window, gate, chest, or other entryway, and 
    it becomes locked for the duration. You and the creatures you 
    designate when you cast this spell can open the object normally. You 
    can also set a password that, when spoken within 5 feet of the object,
     suppresses this spell for 1 minute. Otherwise, it is impassable until
     it is broken or the spell is dispelled or suppressed. Casting knock 
    on the object suppresses arcane lock for 10 minutes.
    
    While affected 
    by this spell, the object is more difficult to break or force open; 
    the DC to break it or pick any locks on it increases by 10.
    """
    name = "Arcane Lock"
    level = 2
    casting_time = "1 action"
    casting_range = "Touch"
    components = ('V', 'S', 'M')
    materials = """Gold dust worth at least 25 gp, which the spell consumes"""
    duration = "Until dispelled"
    ritual = False
    magic_school = "Abjuration"
    classes = ('Wizard',)


class ArmorOfAgathys(Spell):
    """A protective magical force surrounds you, manifesting as a spectral frost that 
    covers you and your gear. 
    You gain 5 temporary hit points for the duration. If 
    a creature hits you with a melee attack while you have these hit points, the 
    creature takes 5 cold damage.
    
    At Higher Levels: When you cast this spell using 
    a spell slot of 2nd level or higher, both the temporary hit points and the cold 
    damage increase by 5 for each slot
    """
    name = "Armor Of Agathys"
    level = 1
    casting_time = "1 action"
    casting_range = "Self"
    components = ('V', 'S', 'M')
    materials = """A cup of water"""
    duration = "1 hour"
    ritual = False
    magic_school = "Abjuration"
    classes = ('Warlock',)


class ArmsOfHadar(Spell):
    """You invoke the power of Hadar, the Dark Hunger. 
    Tendrils of dark energy erupt 
    from you and batter all creatures within 10 feet of you. Each creature in that 
    area must make a Strength saving throw. On a failed save, a target takes 2d6 
    necrotic damage and can’t take reactions until its next turn. On a successful 
    save, the creature takes half damage, but suffers no other effect.
    
    At Higher 
    Levels: When you cast this spell using a spell slot of 2nd level or higher, the 
    damage increases by 1d6 for each slot level above 1st.
    """
    name = "Arms Of Hadar"
    level = 1
    casting_time = "1 action"
    casting_range = "Self (10-foot radius)"
    components = ('V', 'S')
    materials = """"""
    duration = "Instantaneous"
    ritual = False
    magic_school = "Conjuration"
    classes = ('Warlock',)


class AstralProjection(Spell):
    """You and up to eight willing creatures within range project your astral bodies 
    into the Astral Plane (the spell fails and the casting is wasted if you are 
    already on that plane). 
    The material body you leave behind is unconscious and 
    in a state of suspended animation; it doesn’t need food or air and doesn’t age. 
    
    
    Your astral body resembles your mortal form in almost every way, replicating 
    your game statistics and possessions. The principal difference is the addition 
    of a silvery cord that extends from between your shoulder blades and trails 
    behind you, fading to invisibility after 1 foot. This cord is your tether to 
    your material body. As long as the tether remains intact, you can find your 
    way home. If the cord is cut something that can happen only when an effect 
    specifically states that it does your soul and body are separated, killing you 
    instantly. 
    
    Your astral form can freely travel through the Astral Plane and can
     pass through portals there leading to any other plane. If you enter a new plane
     or return to the plane you were on when casting this spell, your body 
    and possessions are transported along the silver cord, allowing you to re-enter 
    your body as you enter the new plane. Your astral form is a separate 
    incarnation. Any damage or other effects that apply to it have no effect on 
    your physical body, nor do they persist when you return to it. The spell ends 
    for you and your companions when you use your action to dismiss it. When the 
    spell ends, the affected creature returns to its physical body, and it awakens. 
    
    
    The spell might also end early for you or one of your companions. A successful
     dispel magic spell used against an astral or physical body ends the spell for 
    that creature. If a creature’s original body or its astral form drops to 0 hit 
    points, the spell ends for that creature. If the spell ends and the silver cord 
    is intact, the cord pulls the creature’s astral form back to its body, ending 
    its state of suspended animation. If you are returned to your body prematurely, 
    your companions remain in their astral forms and must find their own way back to
     their bodies, usually by dropping to 0 hit points.
    """
    name = "Astral Projection"
    level = 9
    casting_time = "1 hour"
    casting_range = "10 feet"
    components = ('V', 'S', 'M')
    materials = """For each creature you affect with this spell, you must provide one jacinth worth at least 1,000 gp and one ornately carved bar of silver worth at least 100 gp, all of which the spell consumes"""
    duration = "Special"
    ritual = False
    magic_school = "Necromancy"
    classes = ('Cleric', 'Warlock', 'Wizard')


class Augury(Spell):
    """By casting gem-inlaid sticks, rolling dragon bones, laying out ornate cards, or 
    employing some other divining tool, you receive an omen from an otherworldly 
    entity about the results of a specific course of action that you plan to take 
    within the next 30 minutes. The DM chooses from the following possible omens: 
    
    
    • Weal, for good results 
    • Woe, for bad results 
    • Weal and woe, for both good 
    and bad results 
    • Nothing, for results that aren’t especially good or bad 
    
    The
     spell doesn’t take into account any possible circumstances that might change 
    the outcome, such as the casting of additional spells or the loss or gain of a 
    companion.    If you cast the spell two or more times before completing your 
    next long rest, there is a cumulative 25 percent chance for each casting after 
    the first that you get a random reading. The DM makes this roll in secret.
    """
    name = "Augury"
    level = 2
    casting_time = "1 minute"
    casting_range = "Self"
    components = ('V', 'S', 'M')
    materials = """Specially marked sticks, bones, or similar tokens worth at least 25 gp"""
    duration = "Instantaneous"
    ritual = True
    magic_school = "Divination"
    classes = ('Cleric',)


class AuraOfLife(Spell):
    """Life-preserving energy radiates from you in an aura with a 30-foot radius. 
    
    Until the spll ends, the aura moves with you, centered on you. Each nonhostile 
    creature in the aura (including you) has resistance to necrotic damage, and its 
    hit point maximum can’t be reduced. In addition, a nonhostile, living creature 
    regains 1 hit point when it starts its turn in the arua with 0 hit points.
    """
    name = "Aura Of Life"
    level = 4
    casting_time = "1 action"
    casting_range = "Self (30-foot radius)"
    components = ('V',)
    materials = """"""
    duration = "Concentration, up to 10 minutes"
    ritual = False
    magic_school = "Abjuration"
    classes = ('Paladin',)


class AuraOfPurity(Spell):
    """Purifying energy radiates from you in an aura with a 30-foot radius. 
    Until the 
    spell ends, the aura moves with you, centered on you. Each nonhostile creature 
    in the aura (including you) can’t become diseased, has resistance to poison 
    damage, and has advantage on saving throws against effects that cause any of the
     following conditions: blnded, charmed, deafended, frightened, paralyzed, 
    poisoned, and stunned.
    """
    name = "Aura Of Purity"
    level = 4
    casting_time = "1 action"
    casting_range = "Self (30-foot radius)"
    components = ('V',)
    materials = """"""
    duration = "Concentration, up to 10 minutes"
    ritual = False
    magic_school = "Abjuration"
    classes = ('Paladin',)


class AuraOfVitality(Spell):
    """Healing energy radiates from you in an aura with a 30-foot radius. 
    Until the 
    spell ends, the aura moves with you, centered on you. You can use a bonus action
     to cause one creature in the aura (including you) to regain 2d6 hit points.
    """
    name = "Aura Of Vitality"
    level = 3
    casting_time = "1 action"
    casting_range = "Self (30-foot radius)"
    components = ('V',)
    materials = """"""
    duration = "Concentration, up to 1 minute"
    ritual = False
    magic_school = "Evocation"
    classes = ('Paladin',)


class Awaken(Spell):
    """After spending the casting time tracing magical pathways within a precious 
    gemstone, you touch a huge or smaller beast or plant. 
    The target must have 
    either no Intelligence score or an Intelligence of 3 or less. The target gains 
    an Intelligence of 10. The target also gains the ability to speak one language 
    you know. If the target is a plant, it gains the ability to move its limbs, 
    roots, vinces, creepers, and so forth, and it gains senses similar to a huamn’s.
     Your DM chooses statistics appropriate for the awakened plant, such as the 
    statistics for the awakened shrub or the awakened tree. 
    
    The awakened beast or 
    plant is charmed by you for 30 days or until you and your companions do anything
     harmful to it. When the charmed condition ends, the awakened creature chooses 
    whether to remain friendly to you, based on how you treated it while it was 
    charmed.
    """
    name = "Awaken"
    level = 5
    casting_time = "8 hours"
    casting_range = "Touch"
    components = ('V', 'S', 'M')
    materials = """An agate worth at least 1,000 gp, which the spell consumes"""
    duration = "Instantaneous"
    ritual = False
    magic_school = "Transmutation"
    classes = ('Bard', 'Druid')


