from .spells import Spell


class AcidArrow(Spell):
    """A shimmering green arrow streaks toward a target within range and
    bursts in a spray of acid. Make a ranged spell attack against the
    target. On a hit, the target takes 4d4 acid damage immediately and
    2d4 acid damage at the end of its next turn. On a miss, the arrow
    splashes the target with acid for half as much of the initial
    damage and no damage at the end of its next turn.
    
    At Higher Levels. When you cast this spell using a spell slot of
    3rd level or higher, the damage (both initial and later) increases
    by 1d4 for each slot level above 2nd.
    
    """
    level = 2
    name = "Acid Arrow"
    casting_time = "1 action"
    casting_range = "90 ft"
    components = ("V", "S", "M")
    duration = "instantaneous"
    magic_school = "Evocation"
    classes = ('Wizard',)


class AcidSplash(Spell):
    """You hurl a bubble of acid. Choose one creature within range, or
    choose two creatures within range that are within 5 feet of each
    other. A target must succeed on a Dexterity saving throw or take
    1d6 acid damage.
    
    This spell's damage increases by 1d6 when you reach 5th level
    (2d6), 11th level (3d6), and 17th level (4d6).
    
    """
    name = "Acid Splash"
    level = 0
    magic_school = "Conjuration"
    classes = ('Sorceror', 'Wizard', )


class Aid(Spell):
    """Your spell bolsters your allies with toughness and resolve. Choose
    up to three creatures within range. Each target’s hit point
    maximum and current hit points increase by 5 for the duration.
    
    At Higher Levels: When you cast this spell using a spell slot of
    3rd level or higher, a target’s hit points increase by an
    additional 5 for each slot level above 2nd.
    
    """
    name = "Aid"
    level = 2
    casting_time = "1 action"
    casting_range = "30 ft"
    components = ("V", "S", "M")
    materials = "A tiny strip of white cloth"
    duration = "8 hours"
    magic_school = "Abjuration"
    classes = ('Cleric', 'Paladin', )


class Alarm(Spell):
    """You set an alarm against unwanted intrusion. Choose a door, a
    window, or an area within range that is no larger than a 20-foot
    cube. Until the spell ends, an alarm alerts you whenever a Tiny or
    larger creature touches or enters the warded area. When you cast
    the spell, you can designate creatures that won’t set off the
    alarm. You also choose whether the alarm is mental or audible. A
    mental alarm alerts you with a ping in your mind if you are within
    1 mile of the warded area. This ping awakens you if you are
    sleeping. An audible alarm produces the sound of a hand bell for
    10 seconds within 60 feet.
    
    """
    name = "Alarm"
    level = 1
    casting_time = "1 minute"
    casting_range = "30 ft"
    components = ("V", "S", "M")
    materials = "A tiny bell and a piece of fine silver wire."
    duration = "8 hours"
    magic_school = "Abjuration"
    classes = ('Ranger', 'Wizard')


class AlterSelf(Spell):
    """You assume a different form. When you cast the spell, choose one of
    the following options, the effects of which last for the duration
    of the spell. While the spell lasts, you can end one option as an
    action to gain the benefits of a different one.
    
    *Aquatic Adaptation*: You adapt your body to an aquatic environment,
    sprouting gills and growing webbing between your fingers. You can
    breathe underwater and gain a swimming speed equal to your walking
    speed.
    
    *Change Appearance*: You transform your appearance. You decide
    what you look like, including your height, weight, facial
    features, sound of your voice, hair length, coloration, and
    distinguishing characteristics, if any. You can make yourself
    appear as a member of another race, though none of your statistics
    change. You also can't appear as a creature of a different size
    than you, and your basic shape stays the same; if you're bipedal,
    you can't use this spell to become quadrupedal, for instance. At
    any time for the duration of the spell, you can use your action to
    change your appearance in this way again.
    
    *Natural Weapons*: You grow claws, fangs, spines, horns, or a
    different natural weapon of your choice. Your unarmed strikes deal
    1d6 bludgeoning, piercing, or slashing damage, as appropriate to
    the natural weapon you chose, and you are proficient with your
    unarmed strikes. Finally, the natural weapon is magic and you have
    a +1 bonus to the attack and damage rolls you make using it.
    
    """
    name = "Alter Self"
    level = 2
    casting_time = "1 action"
    casting_range = "self"
    components = ("V", "S")
    duration = "Concentration, up to 1 hour"
    magic_school = "Transmutation"
    classes = ('Sorceror', 'Wizard', 'Warlock')


class AnimalFriendship(Spell):
    """This spell lets you convince a beast that you mean it no
    harm. Choose a beast that you can see within range. It must see
    and hear you. If the beast’s Intelligence is 4 or higher, the
    spell fails. Otherwise, the beast must succeed on a Wisdom saving
    throw or be charmed by you for the spell’s duration. If you or one
    of your companions harms the target, the spell ends.
    
    *At Higher Levels*: When you cast this spell using a spell slot of
    2nd level or higher, you can affect one additional beast for each
    slot level above 1st.
    
    """
    name = "Animal Friendship"
    level = 1
    casting_time = "1 action"
    casting_range = "30 ft"
    components = ("V", "S", "M")
    materials = "A morsel of food"
    duration = "24 hours"
    magic_school = "Enchantment"
    classes = ('Bard', 'Druid', 'Ranger')


class AnimalMessenger(Spell):
    """By means of this spell, you use an animal to deliver a
    message. Choose a Tiny beast you can see with in range, such as a
    squirrel, a blue jay, or a bat. You specify a location , which you
    must have visited, and a recipient who matches a general
    description , such as “a man or woman dressed in the uniform of
    the town guard” or “a red-haired dwarf wearing a pointed hat.” You
    also speak a message of up to twenty-five words. The target beast
    travels for the duration of the spell toward the specified
    location, covering about 50 miles per 24 hours for a flying
    messenger, or 25 miles for other animals.
    
    When the messenger arrives, it delivers your message to the
    creature that you described, replicating the sound of your
    voice. The messenger speaks only to a creature matching the
    description you gave. If the messenger doesn’t reach its
    destination before the spell ends, the message is lost, and the
    beast makes its way back to where you cast this spell.
    
    At Higher Levels: If you cast this spell using a spell slot of 3rd
    level or higher, the duration of the spell increases by 48 hours
    for each slot level above 2nd.
    
    """
    name = "Animal Messenger"
    level = 2
    casting_time = "1 action"
    casting_range = "30 ft"
    components = ("V", "S", "M")
    materials = "A morsel of food"
    duration = "24 hours"
    magic_school = "Enchantment"
    classes = ('Bard', 'Druid', 'Ranger')


class AnimalShapes(Spell):
    """Your magic turns others into beasts. Choose any number of willing
    creatures that you can see within range. You transform each target
    into the form of a Large or smaller beast with a challenge rating
    of 4 or lower. On subsequent turns, you can use your action to
    transform affected creatures into new forms.
    
    The transformation lasts for the duration for each target, or
    until the target drops to 0 hit points or dies. You can choose a
    different form for each target. A target’s game statistics are
    replaced by the statistics of the chosen beast, though the target
    retains its alignment and Intelligence, Wisdom and Charisma
    scores. The target assumes the hit points of its new form, and
    when it reverts to its normal form, it returns to the number of
    hit points it had before it transformed. If it reverts as a result
    of dropping to 0 hit points, any excess damage carries over to its
    normal form. As long as the excess damage doesn't reduce the
    creature’s normal form to 0 hit points, it isn't knocked
    unconscious. The creature is limited in the actions it can perform
    by the nature of its new form, and it can’t speak or cast spells.
    
    The target’s gear melds into the new form. The target can’t
    activate, wield, or otherwise benefit from any of its equipment.
    
    """
    name = "Animal Shapes"
    level = 8
    casting_time = "1 action"
    casting_range = "30 ft"
    components = ("V", "S")
    duration = "Concentration, up to 24 hours"
    magic_school = "Transmutation"
    classes = ('Druid',)


class AnimateDead(Spell):
    """This spell creates an undead servant. Choose a pile of bones or a
    corpse of a medium or small humanoid within range. Your spell
    imbues the target with a foul mimicry of life, raising it as an
    undead creature. The target becomes a skeleton if you chose bones
    or a zombie if you chose a corpse (the DM has the creature’s game
    statistics).
    
    On each of your turns, you can use a bonus action to mentally
    command any creature you made with this spell if the creature is
    within 60 feet of you (if you control multiple creatures, you can
    command any or all of them at the same time, issuing the same
    command to each one). You decide what action the creature will
    take and where it will move during its next turn, or you can issue
    a general command, such as to guard a particular chamber or
    corridor. If you issue no commands, the creature only defends
    itself against hostile creatures. Once given an order, the
    creature continues to follow it until its task is complete.
    
    The creature is under your control for 24 hours, after which it
    stops obeying any command you’ve given it. To maintain control of
    the creature for another 24 hours, you must cast this spell on the
    creature again before the current 24-hour period ends. This use of
    the spell reasserts your control over up to four creatures you
    have animated with this spell, rather than animating a new one.
    
    At Higher Levels. When you cast this spell using a spell slot of
    4th level or higher, you animate or reassert control over two
    additional undead creatures for each slot level above 3rd. Each of
    the creatures must come from a different corpse or pile of bones.
    
    """
    name = "Animate Dead"
    level = 3
    casting_time = "1 minute"
    casting_range = "10 ft"
    components = ("V", "S", "M")
    materials = "A drop of blood, a piece of flesh and a pinch of bone dust"
    duration = "instantaneous"
    magic_school = "Necromancy"
    classes = ('Cleric', 'Wizard', 'Paladin')


class AnimateObjects(Spell):
    """Objects come to life at your command. Choose up to ten nonmagical
    objects within range that are not being worn or carried. Medium
    targets count as two objects, Large targets count as four objects,
    Huge targets count as eight objects. You can’t animate any object
    larger than Huge. Each target animates and becomes a creature
    under your control until the spell ends or until reduced to 0 hit
    points.
    
    As a bonus action, you can mentally command any creature you made
    with this spell if the creature is within 500 feet of you (if you
    control multiple creatures, you can command any or all of them at
    the same time, issuing the same command to each one). You decide
    what action the creature will take and where it will move during
    its next turn, or you can issue a general command, such as to
    guard a particular chamber or corridor. If you issue no commands,
    the creature only defends itself against hostile creatures. Once
    given an order, the creature continues to follow it until its task
    is complete.
    
    **Animated Object Statistics**
    
    Size	HP	AC	Attack	                 Str	Dex
    ----        --      --      ------                   ---    ---
    Tiny	20	18	+8 to hit, 1D4+4 damage  4	18
    Small	25	16	+6 to hit, 1D8+2 damage	 6	14
    Medium	40	13	+5 to hit, 2D6+1 damage	 10	12
    Large	50	10	+6 to hit, 2D10+2 damage 14	10
    Huge	80	10	+8 to hit, 2D12+4 damage 18	6
    
    An animated object is a construct with AC, hit points, attacks,
    Strength, and Dexterity determined by its size. Its Constitution
    is 10 and its Intelligence and Wisdom are 3, and its Charisma is
    1. Its speed is 30 feet; if the object lacks legs or other
    appendages it can use for locomotion, it instead has a flying
    speed of 30 feet and can hover. If the object is securely attached
    to a surface or a larger object, such as a chain bolted to a wall,
    its speed is 0. It has blindsight with a radius of 30 feet and is
    blind beyond that distance. When the animated object drops to 0
    hit points, it reverts to its original object form, and any
    remaining damage carries over to its original object form.
    
    If you command an object to attack, it can make a single melee
    attack against a creature within 5 feet of it. It makes a slam
    attack with an attack bonus and bludgeoning damage determined by
    its size. The DM might rule that a specific object inflicts
    slashing or piercing damage based on its form.
    
    *At Higher Levels*: If you cast this spell using a spell slot of
    6th level or higher, you can animate two additional objects for
    each slot level above 5th.
    
    """
    name = "Animate Objects"
    level = 5
    casting_time = "1 action"
    casting_range = "120 ft"
    components = ("V", "S")
    duration = "Concentration, up to 1 minute."
    magic_school = "Transmutation"
    classes = ('Bard', 'Sorceror', 'Wizard')


class AntilifeShell(Spell):
    """A shimmering barrier extends out from you in a 10-foot radius and
    moves with you, remaining centered on you and hedging out
    creatures other than undead and constructs. The barrier lasts for
    the duration. The barrier prevents an affected creature from
    passing or reaching through. An affected creature can cast spells
    or make attacks with ranged or reach weapons through the
    barrier. If you move so that an affected creature is forced to
    pass through the barrier, the spell ends.
    
    """
    name = "Antilife Shell"
    level = 5
    casting_time = "1 action"
    casting_range = "Self (10-foot radius)"
    components = ("V", "S")
    duration = "Concentration, up to 1 hour"
    magic_school = "Abjuration"
    classes = ('Druid', )


class AntimagicField(Spell):
    """A 10-foot-radius invisible sphere of antimagic surrounds you. This
    area is divorced from the magical energy that suffuses the
    multiverse. Within the sphere, spells can’t be cast, summoned
    creatures disappear, and even magic items become mundane. Until
    the spell ends, the sphere moves with you, centered on you.
    
    Spells and other magical effects, except those created by an
    artifact or a deity, are suppressed in the sphere and can’t
    protrude into it. A slot expended to cast a suppressed spell is
    consumed. While an effect is suppressed, it doesn’t function, but
    the time it spends suppressed counts against its duration.
    
    **Targeted Effects** Spells and other magical effects, such as Magic
    Missile and Charm Person, that target a creature or an object in
    the sphere have no effect on that target.
    
    **Areas of Magic** The area of another spell or magical effect,
    such as Fireball, can’t extend into the sphere. If the sphere
    overlaps an area of magic, the part of the area that is covered by
    the sphere is suppressed. For example, the flames created by a
    Wall of Fire are suppressed within the sphere, creating a gap in
    the wall if the overlap is large enough.
    
    **Spells** Any active spell or other magical effect on a creature
    or an object in the sphere is suppressed while the creature or
    object is in it.
    
    **Magic Items** The properties and powers of magic items are
    suppressed in the sphere. For example, a + 1 longsword in the
    sphere functions as a nonmagical longsword.
    
    A magic weapon’s properties and powers are suppressed if it is
    used against a target in the sphere or wielded by an attacker in
    the sphere. If a magic weapon or a piece of magic ammunition fully
    leaves the sphere (for example, if you fire a magic arrow or throw
    a magic spear at a target outside the sphere), the magic of the
    item ceases to be suppressed as soon as it exits.
    
    **Magical Travel** Teleportation and planar travel fail to work in
    the sphere, whether the sphere is the destination or the departure
    point for such magical travel. A portal to another location,
    world, or plane of existence, as well as an opening to an
    extradimensional space such as that created by the Rope Trick
    spell, temporarily closes while in the sphere.
    
    **Creatures and Objects** A creature or object summoned or created
    by magic temporarily winks out of existence in the sphere. Such a
    creature instantly reappears once the space the creature occupied
    is no longer within the sphere.
    
    **Dispel Magic** Spells and magical effects such as Dispel Magic
    have no effect on the sphere. Likewise, the spheres created by
    different antimagic field spells don’t nullify each other.
    
    """
    name = "Antimagic Field"
    level = 8
    casting_time = "1 action"
    casting_range = "10-foot-radius sphere"
    components = ("V", "S", "M")
    materials = "A pinch of powdered iron or iron filings"
    duration = "Concentration, up to 1 hour"
    magic_school = "Abjuration"
    classes = ('Cleric', 'Wizard')


class AntipathySympathy(Spell):
    """This spell attracts or repels creatures of your choice. You target
    something within range, either a Huge or smaller object or
    creature or an area that is no larger than a 200-foot cube. Then
    specify a kind of intelligent creature, such as red dragons,
    goblins, or vampires. You invest the target with an aura that
    either attracts or repels the specified creatures for the
    duration. Choose antipathy or sympathy as the aura’s effect.
    
    **Antipathy** The enchantment causes creatures of the kind you
    designated to feel an intense urge to leave the area and avoid the
    target. When such a creature can see the target or comes within 60
    feet of it, the creature must succeed on a Wisdom saving throw or
    become frightened. The creature remains frightened while it can
    see the target or is within 60 feet of it. While frightened by the
    target, the creature must use its movement to move to the nearest
    safe spot from which it can’t see the target. If the creature
    moves more than 60 feet from the target and can’t see it, the
    creature is no longer frightened, but the creature becomes
    frightened again if it regains sight of the target or moves within
    60 feet of it.
    
    **Sympathy** The enchantment causes the specified creatures to
    feel an intense urge to approach the target while within 60 feet
    of it or able to see it. When such a creature can see the target
    or comes within 60 feet of it, the creature must succeed on a
    Wisdom saving throw or use its movement on each of its turns to
    enter the area or move within reach of the target. When the
    creature has done so, it can’t willingly move away from the
    target. If the target damages or otherwise harms an affected
    creature, the affected creature can make a Wisdom saving throw to
    end the effect, as described below.
    
    **Ending the Effect** If an affected creature ends its turn while
    not within 60 feet of the target or able to see it, the creature
    makes a Wisdom saving throw. On a successful save, the creature is
    no longer affected by the target and recognizes the feeling of
    repugnance or attraction as magical. In addition, a creature
    affected by the spell is allowed another Wisdom saving throw every
    24 hours while the spell persists. A creature that successfully
    saves against this effect is immune to it for 1 minute, after
    which time it can be affected again.
    
    """
    name = "Antipathy/Sympath"
    level = 8
    casting_time = "1 hour"
    casting_range = "60 ft"
    components = ("V", "S", "M")
    materials = "Either a lump of alum soaked in vinegar for the antipathy effect or a drop of honey for the sympathy effect"
    duration = "instantaneous"
    magic_school = "10 days"
    classes = ('Druid', 'Wizard')


class ArcaneEye(Spell):
    """You create an invisible, magical eye within range that hovers in
    the air for the duration.
    
    You mentally receive visual information from the eye, which has
    normal vision and darkvision out to 30 feet. The eye can look in
    every direction.
    
    As an action, you can move the eye up to 30 feet in any
    direction. There is no limit to how far away from you the eye can
    move, but it can’t enter another plane of existence. A solid
    barrier blocks the eye’s movement, but the eye can pass through an
    opening as small as 1 inch in diameter.
    
    """
    name = "ArcaneEye"
    level = 4
    casting_time = "1 action"
    casting_range = "30 ft"
    components = ("V", "S", "M")
    materials = "A bit of bat fur"
    duration = "Concentration, up to 1 hour"
    magic_school = "Divination"
    classes = ('Wizard', )


class ArcaneGate(Spell):
    """You create linked teleportation portals that remain open for the
    duration. Choose two points on the ground that you can see, one
    point within 10 feet of you and one point within 500 feet of
    you. A circular portal, 10 feet in diameter, opens over each
    point. If the portal would open in the space occupied by a
    creature, the spell fails, and the casting is lost.
    
    The portals are two-dimensional glowing rings filled with mist,
    hovering inches from the ground and perpendicular to it at the
    points you choose. A ring is visible only from one side (your
    choice), which is the side that functions as a portal.
    
    Any creature or object entering the portal exits from the other
    portal as if the two were adjacent to each other; passing through
    a portal from the nonportal side has no effect. The mist that
    fills each portal is opaque and blocks vision through it. On your
    turn, you can rotate the rings as a bonus action so that the
    active side faces in a different direction.
    
    """
    name = "Arcane Gate"
    level = 6
    casting_time = "1 action"
    casting_range = "500 ft"
    components = ("V", "S")
    duration = "Concentration, up to 10 minutes"
    magic_school = "Conjuration"
    classes = ('Sorceror', 'Warlock', 'Wizard')


class ArcaneHand(Spell):
    """You create a Large hand of shimmering, translucent force in an
    unoccupied space that you can see within range. The hand lasts for
    the spell's duration, and it moves at your command, mimicking the
    movements of your own hand.
    
    The hand is an object that has AC 20 and hit points equal to your
    hit point maximum. If it drops to 0 hit points, the spell ends. It
    has a Strength of 26 (+8) and a Dexterity of 10 (+0). The hand
    doesn't fill its space.  When you cast the spell and as a bonus
    action on your subsequent turns, you can move the hand up to 60
    feet and then cause one of the following effects with it.
    
    **Clenched Fist** The hand strikes one creature or object within 5
    feet of it. Make a melee spell attack for the hand using your game
    statistics. On a hit, the target takes 4d8 force damage.
    
    **Forceful Hand** The hand attempts to push a creature within 5
    feet of it in a direction you choose. Make a check with the hand's
    Strength contested by the Strength (Athletics) check of the
    target. If the target is Medium or smaller, you have advantage on
    the check. If you succeed, the hand pushes the target up to 5 feet
    plus a number of feet equal to five times your spellcasting
    ability modifier. The hand moves with the target to remain within
    5 feet of it.
    
    **Grasping Hand** The hand attempts to grapple a Huge or smaller
    creature within 5 feet of it. You use the hand's Strength score to
    resolve the grapple. If the target is Medium or smaller, you have
    advantage on the check. While the hand is grappling the target,
    you can use a bonus action to have the hand crush it. When you do
    so, the target takes bludgeoning damage equal to 2d6 + your
    spellcasting ability modifier.
    
    **Interposing Hand** The hand interposes itself between you and a
    creature you choose until you give the hand a different
    command. The hand moves to stay between you and the target,
    providing you with half cover against the target. The target can't
    move through the hand's space if its Strength score is less than
    or equal to the hand's Strength score. If its Strength score is
    higher than the hand's Strength score, the target can move toward
    you through the hand's space, but that space is difficult terrain
    for the target.
    
    **At Higher Levels** When you cast this spell using a spell slot
    of 6th level or higher, the damage from the clenched fist option
    increases by 2d8 and the damage from the grasping hand increases
    by 2d6 for each slot level above 5th.
    
    """
    level = 5
    name = "Arcane Hand"
    casting_time = "1 action"
    casting_range = "120 ft"
    components = ("V", "S", "M")
    materials = "an eggshell and a snakeskin glove"
    duration = "1 minute"
    magic_school = "Evocation"
    classes = ('Wizard', )


class ArcaneLock(Spell):
    """You touch a closed door, window, gate, chest, or other entryway,
    and it becomes locked for the duration. You and the creatures you
    designate when you cast this spell can open the object
    normally. You can also set a password that, when spoken within 5
    feet of the object, suppresses this spell for 1 minute. Otherwise,
    it is impassable until it is broken or the spell is dispelled or
    suppressed. Casting knock on the object suppresses arcane lock for
    10 minutes.
    
    While affected by this spell, the object is more difficult to
    break or force open; the DC to break it or pick any locks on it
    increases by 10.
    
    """
    name = "Arcane Lock"
    level = 2
    casting_time = "1 action"
    casting_range = "Touch"
    components = ("V", "S", "M")
    materials = "Gold dust worth at least 25 gp, which the spell consumes"
    duration = "Until dispelled"
    magic_school = "Abjuration"
    classes = ('Wizard',)


class ArcanistsMagicAura(Spell):
    """You place an illusion on a creature or an object you touch so that divination spells reveal false information about it. The target can be a willing creature or an object that isn't being carried or worn by another creature. 
When you cast the spell, choose one or both of the following effects. The effect lasts for the duration. If you cast this spell on the same creature or object every day for 30 days, placing the same effect on it each time, the illusion lasts until it is dispelled.

False Aura. You change the way the target appears to spells and magical effects, such as detect magic, that detect magical auras. You can make a nonmagical object appear magical, a magical object appear nonmagical, or change the object's magical aura so that it appears to belong to a specific school of magic that you choose. When you use this effect on an object, you can make the false magic apparent to any creature that handles the item.

Mask. You change the way the target appears to spells and magical effects that detect creature types, such as a paladin's Divine Sense or the trigger of a symbol spell. You choose a creature type and other spells and magical effects treat the target as if it were a creature of that type or of that alignment.
    
    """
    level = 2
    name = "Arcanist's Magic Aura"
    casting_time = "1 action"
    casting_range = "Touch"
    components = ("V", "S", "M")
    materials = "a small square of silk"
    duration = "24 hours"
    magic_school = "Illusion"
    classes = ('Wizard', )


class ArmorOfAgathys(Spell):
    """A protective magical force surrounds you, manifesting as a spectral
    frost that covers you and your gear. You gain 5 temporary hit
    points for the duration. If a creature hits you with a melee
    attack while you have these hit points, the creature takes 5 cold
    damage.
    
    At Higher Levels: When you cast this spell using a spell slot of
    2nd level or higher, both the temporary hit points and the cold
    damage increase by 5 for each slot level above 1st.
    
    """
    name = "Armor of Agathys"
    level = 1
    casting_time = "1 action"
    casting_range = "Self"
    components = ("V", "S", "M")
    materials = "A cup of water"
    duration = "1 hour"
    magic_school = "Abjuration"
    classes = ('Warlock', )


class ArmsOfHadar(Spell):
    """You invoke the power of Hadar, the Dark Hunger.
    
    Tendrils of dark energy erupt from you and batter all creatures
    within 10 feet of you. Each creature in that area must make a
    Strength saving throw. On a failed save, a target takes 2d6
    necrotic damage and can’t take reactions until its next turn. On a
    successful save, the creature takes half damage, but suffers no
    other effect.
    
    **At Higher Levels**: When you cast this spell using a spell slot
    of 2nd level or higher, the damage increases by 1d6 for each slot
    level above 1st.
    
    """
    name = "Arms of Hadar"
    level = 1
    casting_time = "1 action"
    casting_range = "Self (10-foot radius)"
    components = ("V", "S")
    duration = "instantaneous"
    magic_school = "Conjuration"
    classes = ('Warlock',)


class AstralProjection(Spell):
    """You and up to eight willing creatures within range project your
    astral bodies into the Astral Plane (the spell fails and the
    casting is wasted if you are already on that plane). The material
    body you leave behind is unconscious and in a state of suspended
    animation; it doesn’t need food or air and doesn’t age.
    
    Your astral body resembles your mortal form in almost every way,
    replicating your game statistics and possessions. The principal
    difference is the addition of a silvery cord that extends from
    between your shoulder blades and trails behind you, fading to
    invisibility after 1 foot. This cord is your tether to your
    material body. As long as the tether remains intact, you can find
    your way home. If the cord is cut —something that can happen only
    when an effect specifically states that it does— your soul and
    body are separated, killing you instantly.
    
    Your astral form can freely travel through the Astral Plane and
    can pass through portals there leading to any other plane. If you
    enter a new plane or return to the plane you were on when casting
    this spell, your body and possessions are transported along the
    silver cord, allowing you to re-enter your body as you enter the
    new plane. Your astral form is a separate incarnation. Any damage
    or other effects that apply to it have no effect on your physical
    body, nor do they persist when you return to it.
    
    The spell ends for you and your companions when you use your
    action to dismiss it. When the spell ends, the affected creature
    returns to its physical body, and it awakens.
    
    The spell might also end early for you or one of your
    companions. A successful dispel magic spell used against an astral
    or physical body ends the spell for that creature. If a creature’s
    original body or its astral form drops to 0 hit points, the spell
    ends for that creature. If the spell ends and the silver cord is
    intact, the cord pulls the creature’s astral form back to its
    body, ending its state of suspended animation.
    
    If you are returned to your body prematurely, your companions
    remain in their astral forms and must find their own way back to
    their bodies, usually by dropping to 0 hit points.
    
    """
    name = "Astral Projection"
    level = 9
    casting_time = "1 hour"
    casting_range = "10 ft"
    components = ("V", "S", "M")
    materials = "For each creature you affect with this spell, you must provide one jacinth worth at least 1000 GP and one ornately carved bar of silver worth at least 100 GP, all of which the spell consumes."
    duration = "Special"
    magic_school = "Necromancy"
    classes = ('Necromancy', 'Cleric', 'Warlock', 'Wizard', 'Monk')


class Augury(Spell):
    """By casting gem-inlaid sticks, rolling dragon bones, laying out
    ornate cards, or employing some other divining tool, you receive
    an omen from an otherworldly entity about the results of a
    specific course of action that you plan to take within the next 30
    minutes. The DM chooses from the following possible omens:
    
    - Weal, for good results
    - Woe, for bad results
    - Weal and woe, for both good and bad results
    - Nothing, for results that aren’t especially good or bad
    
    The spell doesn’t take into account any possible circumstances
    that might change the outcome, such as the casting of additional
    spells or the loss or gain of a companion. If you cast the spell
    two or more times before completing your next long rest, there is
    a cumulative 25 percent chance for each casting after the first
    that you get a random reading. The DM makes this roll in secret.
    
    """
    name = "Augury"
    level = 2
    casting_time = "1 minute"
    casting_range = "Self"
    components = ("V", "S", "M")
    materials = "specially marked sticks, bones, or similar tokens worth at least 25 gp"
    duration = "instantaneous"
    magic_school = "Divination"
    classes = ('Cleric', )


class AuraOfLife(Spell):
    """Life-preserving energy radiates from you in an aura with a 30-foot
    radius. Until the spell ends, the aura moves with you, centered on
    you. Each nonhostile creature in the aura (including you) has
    resistance to necrotic damage, and its hit point maximum can’t be
    reduced. In addition, a nonhostile, living creature regains 1 hit
    point when it starts its turn in the aura with 0 hit points.
    
    """
    name = "Aura of Life"
    level = 4
    casting_time = "1 action"
    casting_range = "Self (30 foot radius)"
    components = ("V",)
    duration = "Concentration, up to 10 minutes"
    magic_school = "Abjuration"
    classes = ('Paladin', )


class AuraOfPurity(Spell):
    """Until the spell ends, the aura moves with you, centered on
    you. Each nonhostile creature in the aura (including you) can’t
    become diseased, has resistance to poison damage, and has
    advantage on saving throws against effects that cause any of the
    following conditions: blinded, charmed, deafened, frightened,
    paralyzed, poisoned, and stunned.
    
    """
    name = "Aura of Purity"
    level = 4
    casting_time = "1 action"
    casting_range = "Self (30-foot radius)"
    components = ("V",)
    duration = "Concentration, up to 10 minutes."
    magic_school = "Abjuration"
    classes = ('Paladin', )


class AuraOfVitality(Spell):
    """Healing energy radiates from you in an aura with a 30-foot
    radius. Until the spell ends, the aura moves with you, centered on
    you. You can use a bonus action to cause one creature in the aura
    (including you) to regain 2d6 hit points.
    
    """
    name = "Aura of Vitality"
    level = 3
    casting_time = "1 action"
    casting_range = "Self (30-foot radius)"
    components = ("V", )
    duration = "Concentration, up to 1 minute"
    magic_school = "Evocation"
    classes = ('Paladin', )


class Awaken(Spell):
    """After spending the casting time tracing magical pathways within a
    precious gem stone, you touch a Huge or smaller beast or
    plant. The target must have either no Intelligence score or an
    Intelligence of 3 or less. The target gains an Intelligence of
    10. The target also gains the ability to speak one language you
    know. If the target is a plant, it gains the ability to move its
    limbs, roots, vines, creepers, and so forth, and it gains senses
    similar to a human’s. Your DM chooses statistics appropriate for
    the awakened plant, such as the statistics for the awakened shrub
    or the awakened tree.
    
    The awakened beast or plant is charmed by you for 30 days or until
    you or your companions do anything harmful to it. When the charmed
    condition ends, the awakened creature chooses whether to remain
    friendly to you, based on how you treated it while it was charmed.
    
    """
    name = "Awaken"
    level = 5
    casting_time = "8 hours"
    casting_range = "Touch"
    components = ("V", "S", "M")
    materials = "an agate worth at least 1,000 gp, which the spell consumes"
    duration = "instantaneous"
    magic_school = "Transmutation"
    classes = ('Bard', )


class Bane(Spell):
    """Up to three creatures of your choice that you can see within range
    must make Charisma saving throws. Whenever a target that fails
    this saving throw makes an attack roll or a saving throw before
    the spell ends, the target must roll a d4 and subtract the number
    rolled from the attack roll or saving throw.
    
    At Higher Levels. When you cast this spell using a spell slot of
    2nd level or higher, you can target one additional creature for
    each slot level above 1st.
    
    """
    name = "Bane"
    level = 1
    casting_time = "1 action"
    casting_range = "30 feet"
    components = ("V", "S", "M")
    materials = "a drop of blood"
    duration = "Concentration, up to 1 minute"
    magic_school = "Enchantment"
    classes = ('Bard', 'Cleric', )


class BanishingSmite(Spell):
    """The next time you hit a creature with a weapon attack before this
    spell ends, your weapon crackles with force, and the attack deals
    an extra 5d10 force damage to the target. Additionally, if this
    attack reduces the target to 50 hit points or fewer, you banish
    it. If the target is native to a different plane of existence than
    the one you’re on, the target disappears, returning to its home
    plane. If the target is native to the plane you’re on, the
    creature vanishes into a harmless demiplane. While there, the
    target is incapacitated. It remains there until the spell ends, at
    which point the target reappears in the space it left or in the
    nearest unoccupied space if that space is occupied.
    
    """
    name = "Banishing Smite"
    level = 5
    casting_time = "1 bonus action"
    casting_range = "Self"
    components = ("V", )
    duration = "Concentration, up to 1 minute"
    magic_school = "Abjuration"
    classes = ('Paladin', )


class Banishment(Spell):
    """You attempt to send one creature that you can see within range to
    another plane of existence. The target must succeed on a Charisma
    saving throw or be banished.
    
    If the target is native to the plane of existence you're on, you
    banish the target to a harmless demiplane. While there, the target
    is incapacitated. The target remains there until the spell ends,
    at which point the target reappears in the space it left or in the
    nearest unoccupied space if that space is occupied.
    
    If the target is native to a different plane of existence than the
    one you're on, the target is banished with a faint popping noise,
    returning to its home plane. If the spell ends before 1 minute has
    passed, the target reappears in the space it left or in the
    nearest unoccupied space if that space is occupied. Otherwise, the
    target doesn't return.
    
    At Higher Levels. When you cast this spell using a spell slot of
    5th level or higher, you can target one additional creature for
    each slot level above 4th.
    
    """
    level = 4
    name = "Banishment"
    casting_time = "1 action"
    casting_range = "60 ft"
    components = ("V", "S", "M")
    materials = "an item distasteful to the target"
    duration = "1 minutes"
    magic_school = "Abjuration"
    classes = ('Cleric', 'Paladin', 'Sorceror', 'Warlock', 'Wizard')


class Barkskin(Spell):
    """You touch a willing creature. Until the spell ends, the target's
    skin has a rough, bark-like appearance, and the target's AC can't
    be less than 16, regardless of what kind of armor it is wearing.
    
    """
    level = 2
    name = "Barkskin"
    casting_time = "1 action"
    casting_range = "Touch"
    components = ("V", "S", "M")
    materials = "a handful of oak bark"
    duration = "1 hour"
    magic_school = "Transmutation"
    classes = ('Druid', 'Ranger')


class BeaconOfHope(Spell):
    """This spell bestows hope and vitality. Choose any number of
    creatures within range. For the duration, each target has
    advantage on Wisdom saving throws and death saving throws, and
    regains the maximum number of hit points possible from any
    healing.
    
    """
    name = "Beacon of Hope"
    level = 3
    casting_time = "1 action"
    casting_range = "30 feet"
    components = ('V', 'S')
    duration = "Concentration, up to 1 minute"
    magic_school = "Abjuration"
    classes = ('Cleric', )


class BestowCurse(Spell):
    """You touch a creature, and that creature must succeed on a Wisdom
    saving throw or become cursed for the duration of the spell. When
    you cast this spell, choose the nature of the curse from the
    following options:
    
    - Choose one ability score. While cursed, the target has
      disadvantage on ability checks and saving throws made with that
      ability score.
    - While cursed, the target has disadvantage on attack rolls against
      you.
    - While cursed, the target must make a Wisdom saving throw at the
      start of each of its turns. If it fails, it wastes its action
      that turn doing nothing.
    -While the target is cursed, your attacks and spells deal an extra
     1d8 necrotic damage to the target.
    
    A remove curse spell ends this effect. At the GM's option, you may
    choose an alternative curse effect, but it should be no more
    powerful than those described above. The GM has final say on such
    a curse's effect.
    
    **At Higher Levels** If you cast this spell using a spell slot of
    4th level or higher, the duration is concentration, up to 10
    minutes. If you use a spell slot of 5th level or higher, the
    duration is 8 hours. If you use a spell slot of 7th level or
    higher, the duration is 24 hours. If you use a 9th level spell
    slot, the spell lasts until it is dispelled. Using a spell slot of
    5th level or higher grants a duration that doesn't require
    concentration.
    
    """
    level = 3
    name = "Bestow Curse"
    casting_time = "1 action"
    casting_range = "Touch"
    components = ("V", "S")
    duration = "1 minute"
    magic_school = "Necromancy"
    classes = ('Bard', 'Cleric', 'Wizard')


class BlackTentacles(Spell):
    """Squirming, ebony tentacles fill a 20-foot square on ground that you
    can see within range. For the duration, these tentacles turn the
    ground in the area into difficult terrain.
    
    When a creature enters the affected area for the first time on a
    turn or starts its turn there, the creature must succeed on a
    Dexterity saving throw or take 3d6 bludgeoning damage and be
    restrained by the tentacles until the spell ends. A creature that
    starts its turn in the area and is already restrained by the
    tentacles takes 3d6 bludgeoning damage.
    
    A creature restrained by the tentacles can use its action to make
    a Strength or Dexterity check (its choice) against your spell save
    DC. On a success, it frees itself.
    
    """
    level = 4
    name = "Black Tentacles"
    casting_time = "1 action"
    casting_range = "90 ft"
    components = ("V", "S", "M")
    duration = "1 minute"
    magic_school = "Conjuration"
    classes = ('Wizard', )


class BladeBarrier(Spell):
    """You create a vertical wall of whirling, razor-sharp blades made of
    magical energy. The wall appears within range and lasts for the
    duration. You can make a straight wall up to 100 feet long, 20
    feet high, and 5 feet thick, or a ringed wall up to 60 feet in
    diameter, 20 feet high, and 5 feet thick. The wall provides
    three-quarters cover to creatures behind it, and its space is
    difficult terrain. When a creature enters the wall’s area for the
    first time on a turn or starts its turn there, the creature must
    make a Dexterity saving throw. On a failed save, the creature
    takes 6d10 slashing damage. On a successful save, the creature
    takes half as much damage.
    
    """
    name = "Blade Barrier"
    level = 6
    casting_time = "1 action"
    components = ('V', 'S')
    materials = ""
    duration = "Concentration, up to 10 minutes"
    magic_school = "Evocation"
    classes = ()


class BladeWard(Spell):
    """You extend your hand and trace a sigil of warding in the air. Until
    the end of your next turn, you have resistance against
    bludgeoning, piercing, and slashing damage dealt by weapon
    attacks.
    
    """
    name = "Blade Ward"
    level = 0
    casting_time = "1 action"
    components = ('V', 'S')
    duration = "1 round"
    magic_school = "Evocation"
    classes = ('Bard', 'Sorceror', 'Warlock', 'Wizard')


class Bless(Spell):
    """You bless up to three creatures of your choice within
    range. Whenever a target makes an attack roll or a saving throw
    before the spell ends, the target can roll a d4 and add the number
    rolled to the attack roll or saving throw. At Higher Levels. When
    you cast this spell using a spell slot of 2nd level or higher, you
    can target one additional creature for each slot level above
    1st.
    
    """
    name = "Bless"
    level = 1
    casting_time = "1 action"
    casting_range = "30 feet"
    components = ('V', 'S', 'M')
    materials = "a sprinkling of holy water"
    duration = "Concentration, up to 1 minute"
    magic_school = "Enchantment"
    classes = ()


class Blight(Spell):
    """Necromantic energy washes over a creature of your choice that you
    can see within range, draining moisture and vitality from it. The
    target must make a Constitution saving throw. The target takes 8d8
    necrotic damage on a failed save, or half as much damage on a
    successful one. This spell has no effect on undead or constructs.
    
    If you target a plant creature or a magical plant, it makes the
    saving throw with disadvantage, and the spell deals maximum damage
    to it.
    
    If you target a nonmagical plant that isn't a creature, such as a
    tree or shrub, it doesn't make a saving throw; it simply withers
    and dies.
    
    **At Higher Levels** When you cast this spell using a spell slot
    of 5th level or higher, the damage increases by 1d8 for each slot
    level above 4th.
    
    """
    name = "Blight"
    level = 4
    casting_time = "1 action"
    casting_range = "30 feet"
    components = ('V', 'S')
    duration = "Instantaneous"
    magic_school = "Necromancy"
    classes = ('Druid', 'Sorcerer', 'Warlock', 'Wizard')


class BlindnessDeafness(Spell):
    """You can blind or deafen a foe. Choose one creature that you can see
    within range to make a Constitution saving throw. If it fails, the
    target is either blinded or deafened (your choice) for the
    duration. At the end of each of its turns, the target can make a
    Constitution saving throw.  On a success, the spell ends.
    
    At Higher Levels. When you cast this spell using a spell slot of
    3rd level or higher, you can target one additional creature for
    each slot level above 2nd.
    
    """
    name = "Blindness/Deafness"
    magic_school = "Necromancy"
    level = 2
    casting_range = "30 feet"
    components = ("V", )
    duration = "1 minute"
    classes = ('Wizard', )


class Blink(Spell):
    """Roll a d20 at the end of each of your turns for the duration of the
    spell. On a roll of 11 or higher, you vanish from your current
    plane of existence and appear in the Ethereal Plane (the spell
    fails and the casting is wasted if you were already on that
    plane). At the start of your next turn, and when the spell ends if
    you are on the Ethereal Plane, you return to an unoccupied space
    of your choice that you can see within 10 feet of the space you
    vanished from. If no unoccupied space is available within that
    range, you appear in the nearest unoccupied space (chosen at
    random if more than one space is equally near). You can dismiss
    this spell as an action.
    
    While on the Ethereal Plane, you can see and hear the plane you
    originated from, which is cast in shades of gray, and you can't
    see anything there more than 60 feet away. You can only affect and
    be affected by other creatures on the Ethereal Plane. Creatures
    that aren't there can't perceive you or interact with you, unless
    they have the ability to do so.
    
    """
    name = "Blink"
    level = 3
    casting_time = "1 action"
    casting_range = "Self"
    components = ('V', 'S')
    duration = "1 minute"
    magic_school = "Transmutation"
    classes = ('Sorceror', 'Wizard')


class Blur(Spell):
    """Your body becomes blurred, shifting and wavering to all who can see
    you. For the duration, any creature has disadvantage on attack
    rolls against you. An attacker is immune to this effect if it
    doesn’t rely on sight, as with blindsight, or can see through
    illusions, as with truesight.
    
    """
    name = "Blur"
    level = 2
    casting_time = "1 action"
    casting_range = 'Self'
    components = ('V',)
    materials = ""
    duration = "Concentration, up to 1 minute"
    magic_school = "Illusion"
    classes = ()


class BurningHands(Spell):
    """As you hold your hands with thumbs touching and fingers spread, a
    thin sheet of flames shoots forth from your outstretched
    fingertips. Each creature in a 15-foot cone must make a Dexterity
    saving throw. A creature takes 3d6 fire damage on a failed save,
    or half as much damage on a successful one.
    
    The fire ignites any flammable objects in the area that aren't
    being worn or carried.
    
    **At Higher Levels.** When you cast this spell using a spell slot
    of 2nd level or higher, the damage increases by 1d6 for each slot
    level above 1st.
    
    """
    name = "Burning Hands"
    level = 1
    casting_time = "1 action"
    casting_range = "Self (15 foot cone)"
    components = ("V", "S")
    duration = "Instantaneous"
    magic_school = "Evocation"
    classes = ('Wizard', )


class ChainLightning(Spell):
    """You create a bolt of lightning that arcs toward a target of your
    choice that you can see within range. Three bolts then leap from
    that target to as many as three other targets, each of which must
    be within 30 feet of the first target. A target can be a creature
    or an object and can be targeted by only one of the bolts. A
    target must make a Dexterity saving throw. The target takes 10d8
    lightning damage on a failed save, or half as much damage on a
    successful one. At Higher Levels. When you cast this spell using a
    spell slot of 7th level or higher, one additional bolt leaps from
    the first target to another target for each slot level above
    6th.
    
    """
    name = "Chain Lightning"
    level = 6
    casting_time = "1 action"
    components = ('V', 'S', 'M')
    materials = "a bit of fur; a piece of amber, glass, or a crystal rod; and three silver pins"
    duration = "Instantaneous"
    magic_school = "Evocation"
    classes = ()


class CharmPerson(Spell):
    """You attempt to charm a humanoid you can see within range. It must
    make a Wisdom saving throw, and does so with advantage if you or
    your companions are fighting it. If it fails the saving throw, it
    is charmed by you until the spell ends or until you or your
    companions do anything harmful to it. The charmed creature regards
    you as a friendly acquaintance. When the spell ends, the creature
    knows it was charmed by you. At Higher Levels. When you cast this
    spell using a spell slot of 2nd level or higher, you can target
    one additional creature for each slot level above 1st. The
    creatures must be within 30 feet of each other when you target
    them.
    
    """
    name = "Charm Person"
    level = 1
    casting_time = "1 action"
    components = ('V', 'S')
    materials = ""
    duration = "1 hour"
    magic_school = "Enchantment"
    classes = ()


class ChillTouch(Spell):
    """You create a ghostly, skeletal hand in the space of a creature
    within range. Make a ranged spell attack including spell attack
    bonus, against the creature to assail it with the chill of the
    grave. On a hit, the target takes 1d8 necrotic damage, and it
    can't regain hit points until the start of your next turn. Until
    then, the hand clings to the target.
    
    If you hit an undead target, it also has disadvantage on attack
    rolls against you until the end of your next turn.
    
    This spell's damage increases by 1d8 when you reach 5th level
    (2d8), 11th level (3d8), and 17th level (4d8).
    
    """
    name = "Chill Touch"
    level = 0
    casting_time = "1 action"
    casting_range = "120 feet"
    components = ('V', 'S')
    materials = ""
    duration = "1 round"
    magic_school = "Necromancy"
    classes = ('Sorceror', 'Warlock', 'Wizard')


class ChromaticOrb(Spell):
    """You hurl a 4-inch-diameter sphere of energy at a creature that you
    can see within range. You choose acid, cold, fire, lightning,
    poison, or thunder for the type of orb you create, and then make a
    ranged spell attack against the target. If the attack hits, the
    creature takes 3d8 damage of the type you chose.
    
    **At Higher Levels.** When you cast this spell using a spell slot of
    2nd level or higher, the damage increases by 1d8 for each slot
    level above 1st.
    
    """
    name = "Chromatic Orb"
    level = 1
    casting_time = "1 action"
    casting_range = "90 feet"
    components = ('V', 'S', 'M')
    materials = "A diamond worth at least 50 gp"
    duration = "Instantaneous"
    magic_school = "Evocation"
    classes = ('Sorceror', 'Wizard')


class CircleOfDeath(Spell):
    """A sphere of negative energy ripples out in a 60-foot- radius sphere
    from a point within range. Each creature in that area must make a
    Constitution saving throw. A target takes 8d6 necrotic damage on a
    failed save, or half as much damage on a successful one.
    
    **At Higher Levels.** When you cast this spell using a spell slot of
    7th level or higher, the damage increases by 2d6 for each slot
    level above 6th.
    
    """
    name = "Circle of Death"
    level = 6
    casting_time = "1 action"
    casting_range = "150 feet"
    components = ('V', 'S', 'M')
    materials = "the powder of a crushed black pearl worth at least 500 gp"
    duration = "Instantaneous"
    magic_school = "Necromancy"
    classes = ('Sorceror', 'Warlock', 'Wizard')


class Clone(Spell):
    """This spell grows an inert duplicate of a living creature as a
    safeguard against death. This clone forms inside a sealed vessel
    and grows to full size and maturity after 120 days; you can also
    choose to have the clone be a younger version of the same
    creature. It remains inert and endures indefinitely, as long as
    its vessel remains undisturbed.
    
    At any time after the clone matures, if the original creature
    dies, its soul transfers to the clone, provided that the soul is
    free and willing to return. The clone is physically identical to
    the original and has the same personality, memories, and
    abilities, but none of the original's equipment. The original
    creature's physical remains, if they still exist, become inert and
    can't thereafter be restored to life, since the creature's soul is
    elsewhere.
    
    """
    name = "Clone"
    level = 8
    casting_time = "1 hour"
    casting_range = "Touch"
    components = ('V', 'S', "M")
    materials = "a diamond worth at least 1,000 gp and at least 1 cubic inch of flesh of the creature that is to be cloned, which the spell consumes, and a vessel worth at least 2,000 gp that has a sealable lid and is large enough to hold a Medium creature, such as a huge urn, coffin, mud- filled cyst in the ground, or crystal container filled with salt water"
    duration = "Instantaneous"
    magic_school = "Necromancy"
    classes = ('Wizard',)


class Command(Spell):
    """You speak a one-word command to a creature you can see within
    range. The target must succeed on a Wisdom saving throw or follow
    the command on its next turn. The spell has no effect if the
    target is undead, if it doesn’t understand your language, or if
    your command is directly harmful to it. Some typical commands and
    their effects follow. You might issue a command other than one
    described here. If you do so, the DM determines how the target
    behaves. If the target can’t follow your command, the spell
    ends. Approach. The target moves toward you by the shortest and
    most direct route, ending its turn if it moves within 5 feet of
    you. Drop. The target drops whatever it is holding and then ends
    its turn. Flee. The target spends its turn moving away from you by
    the fastest available means. Grovel. The target falls prone and
    then ends its turn. Halt. The target doesn’t move and takes no
    actions. A flying creature stays aloft, provided that it is able
    to do so. If it must move to stay aloft, it flies the minimum
    distance needed to remain in the air. At Higher Levels. When you
    cast this spell using a spell slot of 2nd level or higher, you can
    affect one additional creature for each slot level above 1st. The
    creatures must be within 30 feet of each other when you target
    them.
    
    """
    name = "Command"
    level = 1
    casting_time = "1 action"
    components = ('V',)
    materials = ""
    duration = "1 round"
    magic_school = "Enchantment"
    classes = ()


class Commune(Spell):
    """You contact your deity or a divine proxy and ask up to three
    questions that can be answered with a yes or no. You must ask your
    questions before the spell ends. You receive a correct answer for
    each question. Divine beings aren’t necessarily omniscient, so you
    might receive “unclear” as an answer if a question pertains to
    information that lies beyond the deity’s knowledge. In a case
    where a one-word answer could be misleading or contrary to the
    deity’s interests, the DM might offer a short phrase as an answer
    instead. If you cast the spell two or more times before finishing
    your next long rest, there is a cumulative 25 percent chance for
    each casting after the first that you get no answer. The DM makes
    this roll in secret.
    
    """
    name = "Commune"
    level = 5
    casting_time = "1 minute"
    components = ('V', 'S', 'M')
    materials = "incense and a vial of holy or unholy water"
    duration = "1 minute"
    magic_school = "Divination"
    classes = ()


class ComprehendLanguages(Spell):
    """For the duration, you understand the literal meaning of any spoken
    language that you hear. You also understand any written language
    that you see, but you must be touching the surface on which the
    words are written. It takes about 1 minute to read one page of
    text. This spell doesn’t decode secret messages in a text or a
    glyph, such as an arcane sigil, that isn’t part of a written
    language.
    
    """
    name = "Comprehend Languages"
    level = 1
    casting_time = "1 action"
    components = ('V', 'S', 'M')
    materials = "a pinch of soot and salt"
    duration = "1 hour"
    magic_school = "Divination"
    classes = ()


class ConeOfCold(Spell):
    """A blast of cold air erupts from your hands. Each creature in a
    60-foot cone must make a Constitution saving throw. A creature
    takes 8d8 cold damage on a failed save, or half as much damage on
    a successful one. A creature killed by this spell becomes a frozen
    statue until it thaws. At Higher Levels. When you cast this spell
    using a spell slot of 6th level or higher, the damage increases by
    1d8 for each slot level above 5th.
    
    """
    name = "Cone of Cold"
    level = 5
    casting_time = "1 action"
    components = ('V', 'S', 'M')
    materials = "a small crystal or glass cone"
    duration = "Instantaneous"
    magic_school = "Evocation"
    classes = ()


class Counterspell(Spell):
    """You attempt to interrupt a creature in the process of casting a
    spell. If the creature is casting a spell of 3rd level or lower,
    its spell fails and has no effect. If it is casting a spell of 4th
    level or higher, make an ability check using your spellcasting
    ability. The DC equals 10 + the spell’s level. On a success, the
    creature’s spell fails and has no effect. At Higher Levels. When
    you cast this spell using a spell slot of 4th level or higher, the
    interrupted spell has no effect if its level is less than or equal
    to the level of the spell slot you used.
    
    """
    name = "Counterspell"
    level = 3
    casting_time = "1 reaction, which you take when you see a creature within 60 feet of you casting a spell"
    components = ('S',)
    materials = ""
    duration = "Instantaneous"
    magic_school = "Abjuration"
    classes = ()


class CreateOrDestroyWater(Spell):
    """You either create or destroy water.
    
    **Create Water.** You create up to 10 gallons of clean water
    within range in an open container. Alternatively, the water falls
    as rain in a 30-foot cube within range, extinguishing exposed
    flames in the area.
    
    **Destroy Water.** You destroy up to 10 gallons of water in an open
    container within range. Alternatively, you destroy fog in a
    30-foot cube within range.
    
    **At Higher Levels.** When you cast this spell using a spell slot
    of 2nd level or higher, you create or destroy 10 additional
    gallons of water, or the size of the cube increases by 5 feet, for
    each slot level above 1st.

    """
    level = 1
    name = "Create or Destroy Water"
    casting_time = "1 action"
    casting_range = "30 ft (30 ft cube)"
    components = ("V", "S", "M")
    materials = "a drop of water if creating water or a few grains of sand if destroying it"
    duration = "instantaneous"
    magic_school = "Transmutation"
    classes = ('Cleric', 'Druid')


class CreateUndead(Spell):
    """You can cast this spell only at night. Choose up to three corpses
    of Medium or Small humanoids within range. Each corpse becomes a
    ghoul under your control. (The GM has game statistics for these
    creatures.)
    
    As a bonus action on each of your turns, you can mentally command
    any creature you animated with this spell if the creature is
    within 120 feet of you (if you control multiple creatures, you can
    command any or all of them at the same time, issuing the same
    command to each one). You decide what action the creature will
    take and where it will move during its next turn, or you can issue
    a general command, such as to guard a particular chamber or
    corridor. If you issue no commands, the creature only defends
    itself against hostile creatures. Once given an order, the
    creature continues to follow it until its task is complete.
    
    The creature is under your control for 24 hours, after which it
    stops obeying any command you have given it. To maintain control
    of the creature for another 24 hours, you must cast this spell on
    the creature before the current 24-hour period ends. This use of
    the spell reasserts your control over up to three creatures you
    have animated with this spell, rather than animating new ones.
    
    **At Higher Levels.** When you cast this spell using a 7th-level spell
    slot, you can animate or reassert control over four ghouls. When
    you cast this spell using an 8th-level spell slot, you can animate
    or reassert control over five ghouls or two ghasts or wights. When
    you cast this spell using a 9th-level spell slot, you can animate
    or reassert control over six ghouls, three ghasts or wights, or
    two mummy(ies).
    
    """
    name = "Create Undead"
    level = 6
    casting_time = "1 minute"
    casting_range = "10 feet"
    components = ('V', 'S', 'M')
    materials = "one clay pot filled with grave dirt, one clay pot filled with brackish water, and one 150 gp black onyx stone for each corpse"
    duration = "Instantaneous"
    magic_school = "Necromancy"
    classes = ('Cleric', 'Warlock', 'Wizard', )


class CureWounds(Spell):
    """A creature you touch regains a number of hit points equal to
    ``1d8`` + your spellcasting ability modifier. This spell has no
    effect on undead or constructs. At Higher Levels. When you cast
    this spell using a spell slot of 2nd level or higher, the healing
    increases by ``1d8`` for each slot level above 1st.
    
    """
    name = "Cure Wounds"
    level = 1
    casting_time = "1 action"
    components = ('V', 'S')
    materials = ""
    duration = "Instantaneous"
    magic_school = "Evocation"
    classes = ()


class DancingLights(Spell):
    """You create up to four torch-sized lights within range, making them
    appear as torches, lanterns, or glowing orbs that hover in the air
    for the duration. You can also combine the four lights into one
    glowing vaguely humanoid form of Medium size. Whichever form you
    choose, each light sheds dim light in a 10-foot radius. As a bonus
    action on your turn, you can move the lights up to 60 feet to a
    new spot within range. A light must be within 20 feet of another
    light created by this spell, and a light winks out if it exceeds
    the spell’s range.
    
    """
    name = "Dancing Lights"
    level = 0
    casting_time = "1 action"
    casting_range = "120 feet"
    components = ('V', 'S', 'M')
    materials = "a bit of phosphorus or wychwood, or a glowworm"
    duration = "Concentration, up to 1 minute"
    magic_school = "Evocation"
    classes = ('Bard', 'Sorceror', 'Wizard')


class Darkness(Spell):
    """Magical darkness spreads from a point you choose within range to
    fill a 15-foot-radius sphere for the duration. The darkness
    spreads around corners. A creature with darkvision can’t see
    through this darkness, and nonmagical light can’t illuminate
    it. If the point you choose is on an object you are holding or one
    that isn’t being worn or carried, the darkness emanates from the
    object and moves with it. Completely covering the source of the
    darkness with an opaque object, such as a bowl or a helm, blocks
    the darkness. If any of this spell’s area overlaps with an area of
    light created by a spell of 2nd level or lower, the spell that
    created the light is dispelled.
    
    """
    name = "Darkness"
    level = 2
    casting_time = "1 action"
    components = ('V', 'M')
    materials = "bat fur and a drop of pitch or piece of coal"
    duration = "Concentration, up to 10 minutes"
    magic_school = "Evocation"
    classes = ()


class DeathWard(Spell):
    """You touch a creature and grant it a measure of protection from
    death. The first time the target would drop to 0 hit points as a
    result of taking damage, the target instead drops to 1 hit point,
    and the spell ends. If the spell is still in effect when the
    target is subjected to an effect that would kill it
    instantaneously without dealing damage, that effect is instead
    negated against the target, and the spell ends.
    
    """
    name = "Death Ward"
    level = 4
    casting_time = "1 action"
    components = ('V', 'S')
    materials = ""
    duration = "8 hours"
    magic_school = "Abjuration"
    classes = ()


class DelayedBlastFireball(Spell):
    """A beam of yellow light flashes from your pointing finger, then
    condenses to linger at a chosen point within range as a glowing
    bead for the duration. When the spell ends, either because your
    concentration is broken or because you decide to end it, the bead
    blossoms with a low roar into an explosion of flame that spreads
    around corners. Each creature in a 20-foot-radius sphere centered
    on that point must make a Dexterity saving throw. A creature takes
    fire damage equal to the total accumulated damage on a failed
    save, or half as much damage on a successful one. The spell’s base
    damage is 12d6. If at the end of your turn the bead has not yet
    detonated, the damage increases by 1d6. If the glowing bead is
    touched before the interval has expired, the creature touching it
    must make a Dexterity saving throw. On a failed save, the spell
    ends immediately, causing the bead to erupt in flame. On a
    successful save, the creature can throw the bead up to 40
    feet. When it strikes a creature or a solid object, the spell
    ends, and the bead explodes. The fire damages objects in the area
    and ignites flammable objects that aren’t being worn or
    carried. At Higher Levels. When you cast this spell using a spell
    slot of 8th level or higher, the base damage increases by 1d6 for
    each slot level above 7th.
    
    """
    name = "Delayed Blast Fireball"
    level = 7
    casting_time = "1 action"
    components = ('V', 'S', 'M')
    materials = "a tiny ball of bat guano and sulfur"
    duration = "Concentration, up to 1 minute"
    magic_school = "Evocation"
    classes = ()


class DetectMagic(Spell):
    """For the duration, you sense the presence of magic within 30 feet of
    you. If you sense magic in this way, you can use your action to
    see a faint aura around any visible creature or object in the area
    that bears magic, and you learn its school of magic, if any.
    
    The spell can penetrate most barriers, but is blocked by 1 foot of
    stone, 1 inch of common metal, a thin sheet of lead, or 3 feet of
    wood or dirt.
    
    """
    name = "Detect Magic"
    level = 1
    casting_time = "1 action"
    casting_range = "Self (30 feet)"
    components = ("V", "S")
    duration = "Concentration, Up to 10 minutes"
    ritual = True
    magic_school = "Divination"
    classes = ('Bard', 'Cleric', 'Druid', 'Paladin', 'Ranger', 'Sorceror', 'Wizard', )


class DetectPoisonAndDisease(Spell):
    """For the duration, you can sense the presence and location of poisons,
    poisonous creatures, and diseases within 30 feet of you. You also identify
    the kind of poison, poisonous creature, or disease in each case.
    
    The spell can penetrate most barriers, but is blocked by 1 foot of stone, 1
    inch of common metal, a thin sheet of lead, or 3 feet of wood or dirt.

    """
    name = "Detect Poison and Disease"
    level = 1
    casting_time = '1 action'
    casting_range = "Self (30 feet)"
    components = ("V", "S", "M")
    materials = "a yew leaf"
    magic_school = "Divination"
    classes = ("Cleric", 'Druid', 'Paladin', 'Ranger')


class DimensionDoor(Spell):
    """You teleport yourself from your current location to any other spot
    within range. You arrive at exactly the spot desired. It can be a
    place you can see, one you can visualize, or one you can describe
    by stating distance and direction, such as “200 feet straight
    downward” or “upward to the northwest at a 45-degree angle, 300
    feet.” You can bring along objects as long as their weight doesn’t
    exceed what you can carry. You can also bring one willing creature
    of your size or smaller who is carrying gear up to its carrying
    capacity. The creature must be within 5 feet of you when you cast
    this spell. If you would arrive in a place already occupied by an
    object or a creature, you and any creature traveling with you each
    take 4d6 force damage, and the spell fails to teleport you.
    
    """
    name = "Dimension Door"
    level = 4
    casting_time = "1 action"
    components = ('V',)
    materials = ""
    duration = "Instantaneous"
    magic_school = "Conjuration"
    classes = ()


class DisguiseSelf(Spell):
    """You make yourself—including your clothing, armor, weapons, and
    other belongings on your person—look different until the spell
    ends or until you use your action to dismiss it. You can seem 1
    foot shorter or taller and can appear thin, fat, or in
    between. You can’t change your body type, so you must adopt a form
    that has the same basic arrangement of limbs. Otherwise, the
    extent of the illusion is up to you. The changes wrought by this
    spell fail to hold up to physical inspection. For example, if you
    use this spell to add a hat to your outfit, objects pass through
    the hat, and anyone who touches it would feel nothing or would
    feel your head and hair. If you use this spell to appear thinner
    than you are, the hand of someone who reaches out to touch you
    would bump into you while it was seemingly still in midair. To
    discern that you are disguised, a creature can use its action to
    inspect your appearance and must succeed on an Intelligence
    (Investigation) check against your spell save DC.
    
    """
    name = "Disguise Self"
    level = 1
    casting_time = "1 action"
    components = ('V', 'S')
    materials = ""
    duration = "1 hour"
    magic_school = "Illusion"
    classes = ()


class Disintegrate(Spell):
    """A thin green ray springs from your pointing finger to a target that
    you can see within range. The target can be a creature, an object,
    or a creation of magical force, such as the wall created by wall
    of force. A creature targeted by this spell must make a Dexterity
    saving throw. On a failed save, the target takes 10d6 + 40 force
    damage. If this damage reduces the target to 0 hit points, it is
    disintegrated. A disintegrated creature and everything it is
    wearing and carrying, except magic items, are reduced to a pile of
    fine gray dust. The creature can be restored to life only by means
    of a true resurrection or a wish spell. This spell automatically
    disintegrates a Large or smaller nonmagical object or a creation
    of magical force. If the target is a Huge or larger object or
    creation of force, this spell disintegrates a 10-foot-cube portion
    of it. A magic item is unaffected by this spell. At Higher
    Levels. When you cast this spell using a spell slot of 7th level
    or higher, the damage increases by 3d6 for each slot level above
    6th.
    
    """
    name = "Disintegrate"
    level = 6
    casting_time = "1 action"
    components = ('V', 'S', 'M')
    materials = "a lodestone and a pinch of dust"
    duration = "Instantaneous"
    magic_school = "Transmutation"
    classes = ()


class DispelMagic(Spell):
    """Choose one creature, object, or magical effect within range. Any
    spell of 3rd level or lower on the target ends. For each spell of
    4th level or higher on the target, make an ability check using
    your spellcasting ability. The DC equals 10 + the spell’s
    level. On a successful check, the spell ends. At Higher
    Levels. When you cast this spell using a spell slot of 4th level
    or higher, you automatically end the effects of a spell on the
    target if the spell’s level is equal to or less than the level of
    the spell slot you used.
    
    """
    name = "Dispel Magic"
    level = 3
    casting_time = "1 action"
    components = ('V', 'S')
    materials = ""
    duration = "Instantaneous"
    magic_school = "Abjuration"
    classes = ()


class Divination(Spell):
    """Your magic and an offering put you in contact with a god or a god’s
    servants. You ask a single question concerning a specific goal,
    event, or activity to occur within 7 days. The DM offers a
    truthful reply. The reply might be a short phrase, a cryptic
    rhyme, or an omen. The spell doesn’t take into account any
    possible circumstances that might change the outcome, such as the
    casting of additional spells or the loss or gain of a
    companion. If you cast the spell two or more times before
    finishing your next long rest, there is a cumulative 25 percent
    chance for each casting after the first that you get a random
    reading. The DM makes this roll in secret.
    
    """
    name = "Divination"
    level = 4
    casting_time = "1 action"
    components = ('V', 'S', 'M')
    materials = "incense and a sacrificial offering appropriate to your religion, together worth at least 25 gp, which the spell consumes"
    duration = "Instantaneous"
    magic_school = "Divination"
    classes = ()


class DominateMonster(Spell):
    """You attempt to beguile a creature that you can see within range. It
    must succeed on a Wisdom saving throw or be charmed by you for the
    duration. If you or creatures that are friendly to you are
    fighting it, it has advantage on the saving throw. While the
    creature is charmed, you have a telepathic link with it as long as
    the two of you are on the same plane of existence. You can use
    this telepathic link to issue commands to the creature while you
    are conscious (no action required), which it does its best to
    obey. You can specify a simple and general course of action, such
    as “Attack that creature,” “Run over there,” or “Fetch that
    object.” If the creature completes the order and doesn’t receive
    further direction from you, it defends and preserves itself to the
    best of its ability. You can use your action to take total and
    precise control of the target. Until the end of your next turn,
    the creature takes only the actions you choose, and doesn’t do
    anything that you don’t allow it to do. During this time, you can
    also cause the creature to use a reaction, but this requires you
    to use your own reaction as well. Each time the target takes
    damage, it makes a new Wisdom saving throw against the spell. If
    the saving throw succeeds, the spell ends. At Higher Levels. When
    you cast this spell with a 9th-level spell slot, the duration is
    concentration, up to 8 hours.
    
    """
    name = "Dominate Monster"
    level = 8
    casting_time = "1 action"
    components = ('V', 'S')
    materials = ""
    duration = "Concentration, up to 1 hour"
    magic_school = "Enchantment"
    classes = ()


class DominatePerson(Spell):
    """You attempt to beguile a humanoid that you can see within range. It
    must succeed on a Wisdom saving throw or be charmed by you for the
    duration. If you or creatures that are friendly to you are
    fighting it, it has advantage on the saving throw. While the
    target is charmed, you have a telepathic link with it as long as
    the two of you are on the same plane of existence. You can use
    this telepathic link to issue commands to the creature while you
    are conscious (no action required), which it does its best to
    obey. You can specify a simple and general course of action, such
    as “Attack that creature,” “Run over there,” or “Fetch that
    object.” If the creature completes the order and doesn’t receive
    further direction from you, it defends and preserves itself to the
    best of its ability. You can use your action to take total and
    precise control of the target. Until the end of your next turn,
    the creature takes only the actions you choose, and doesn’t do
    anything that you don’t allow it to do. During this time you can
    also cause the creature to use a reaction, but this requires you
    to use your own reaction as well. Each time the target takes
    damage, it makes a new Wisdom saving throw against the spell. If
    the saving throw succeeds, the spell ends. At Higher Levels. When
    you cast this spell using a 6th-level spell slot, the duration is
    concentration, up to 10 minutes. When you use a 7th-level spell
    slot, the duration is concentration, up to 1 hour. When you use a
    spell slot of 8th level or higher, the duration is concentration,
    up to 8 hours.
    
    """
    name = "Dominate Person"
    level = 5
    casting_time = "1 action"
    components = ('V', 'S')
    materials = ""
    duration = "Concentration, up to 1 minute"
    magic_school = "Enchantment"
    classes = ()


class Dream(Spell):
    """This spell shapes a creature’s dreams. Choose a creature known to
    you as the target of this spell. The target must be on the same
    plane of existence as you. Creatures that don’t sleep, such as
    elves, can’t be contacted by this spell. You, or a willing
    creature you touch, enters a trance state, acting as a
    messenger. While in the trance, the messenger is aware of his or
    her surroundings, but can’t take actions or move. If the target is
    asleep, the messenger appears in the target’s dreams and can
    converse with the target as long as it remains asleep, through the
    duration of the spell. The messenger can also shape the
    environment of the dream, creating landscapes, objects, and other
    images. The messenger can emerge from the trance at any time,
    ending the effect of the spell early. The target recalls the dream
    perfectly upon waking. If the target is awake when you cast the
    spell, the messenger knows it, and can either end the trance (and
    the spell) or wait for the target to fall asleep, at which point
    the messenger appears in the target’s dreams. You can make the
    messenger appear monstrous and terrifying to the target. If you
    do, the messenger can deliver a message of no more than ten words
    and then the target must make a Wisdom saving throw. On a failed
    save, echoes of the phantasmal monstrosity spawn a nightmare that
    lasts the duration of the target’s sleep and prevents the target
    from gaining any benefit from that rest. In addition, when the
    target wakes up, it takes 3d6 psychic damage. If you have a body
    part, lock of hair, clipping from a nail, or similar portion of
    the target’s body, the target makes its saving throw with
    disadvantage.
    
    """
    name = "Dream"
    level = 5
    casting_time = "1 minute"
    components = ('V', 'S', 'M')
    materials = "a handful of sand, a dab of ink, and a writing quill plucked from a sleeping bird"
    duration = "8 hours"
    magic_school = "Illusion"
    classes = ()


class Druidcraft(Spell):
    """You create one of the following effects within range:
    
    - You create a harmless sensory effect that predicts what the weather will be for the next 24 hours. This effect persists for 1 round.
    - You make a flower blossom, a seed pod open, or a leaf bud bloom.
    - You create a harmless nature-related sensory effect. The effect must fit in a 5-foot cube.
    - You light or put out a small flame.
    
    """
    level = 0
    name = "Druidcraft"
    casting_time = "1 action"
    casting_range = "30 ft"
    components = ("V", "S")
    materials = ""
    duration = "instantaneous"
    ritual = False
    magic_school = "Transmutation"
    classes = ('Druid')


