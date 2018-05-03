def create_spell(**params):
    """Create a new subclass of ``Spell`` with given default parameters.
    
    Useful for spells that haven't been entered into the ``spells.py``
    file yet.
    
    Parameters
    ----------
    params : optional
      Saved as attributes of the new class.
    
    Returns
    -------
    NewSpell
      New spell class, subclass of ``Spell``, with given params.
    """
    NewSpell = type('UnknownSpell', (Spell,), params)
    return NewSpell

class Spell():
    """A magical spell castable by a player character."""
    level = 0
    name = "Unknown spell"
    casting_time = "1 action"
    casting_range = "60 ft"
    components = ("V", "S")
    materials = ""
    duration = "instantaneous"
    concentration = False
    ritual = False
    magic_school = ""
    classes = ()
    
    def __str__(self):
        s = self.name
        # Indicate if this is a ritual or a concentration
        indicators = [('R', self.ritual), ('C', self.concentration)]
        indicators = tuple(letter for letter, is_active in indicators if is_active)
        if len(indicators):
            s += f' ({", ".join(indicators)})'
        return s
    
    def __repr__(self):
        return f'<{self.name}>'
    
    def component_string(self):
        s = f'{", ".join(self.components)}'
        if "M" in self.components:
            s += f' ({self.materials})'
        return s
    


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
    """As you hold your hands with lhumbs touching and fingers spread, a
    thin sheet of flames shoots forth from your outstretched
    fingertips. Each creature in a 15-foot cone must make a Dexterity
    saving throw. A creature takes 3d6 fire damage on a failed save,
    or half as much damage on a successful one.
    
    The fire ignites any flammable objecls in lhe area that aren't
    being worn or carried.
    
    **At Higher Levels.** When you cast lhis spell using a spell slot
    of 2nd level or higher, lhe damage increases by 1d6 for each slot
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
    """A creature you touch regains a number of hit points equal to 1d8 +
    your spellcasting ability modifier. This spell has no effect on
    undead or constructs. At Higher Levels. When you cast this spell
    using a spell slot of 2nd level or higher, the healing increases
    by 1d8 for each slot level above 1st.
    
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
    level = 3
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
    duration = "1 minutes"
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


class Knock(Spell):
    """Choose an object that you can see within range. The object can be a
    door, a box, a chest, a set of manacles, a padlock, or another
    object that contains a mundane or magical means that prevents
    access. A target that is held shut by a mundane lock or that is
    stuck or barred becomes unlocked, unstuck, or unbarred. If the
    object has multiple locks, only one of them is unlocked. If you
    choose a target that is held shut with arcane lock, that spell is
    suppressed for 10 minutes, during which time the target can be
    opened and shut normally. When you cast the spell, a loud knock,
    audible from as far away as 300 feet, emanates from the target
    object.
    
    """
    name = "Knock"
    level = 2
    casting_time = "1 action"
    components = ('V',)
    materials = ""
    duration = "Instantaneous"
    magic_school = "Transmutation"
    classes = ()


class LesserRestoration(Spell):
    """You touch a creature and can end either one disease or one
    condition afflicting it. The condition can be blinded, deafened,
    paralyzed, or poisoned.
    
    """
    name = "Lesser Restoration"
    level = 2
    casting_time = "1 action"
    components = ('V', 'S')
    materials = ""
    duration = "Instantaneous"
    magic_school = "Abjuration"
    classes = ()


class Levitate(Spell):
    """One creature or object of your choice that you can see within range
    rises vertically, up to 20 feet, and remains suspended there for
    the duration. The spell can levitate a target that weighs up to
    500 pounds. An unwilling creature that succeeds on a Constitution
    saving throw is unaffected. The target can move only by pushing or
    pulling against a fixed object or surface within reach (such as a
    wall or a ceiling), which allows it to move as if it were
    climbing. You can change the target’s altitude by up to 20 feet in
    either direction on your turn. If you are the target, you can move
    up or down as part of your move. Otherwise, you can use your
    action to move the target, which must remain within the spell’s
    range. When the spell ends, the target floats gently to the ground
    if it is still aloft.
    
    """
    name = "Levitate"
    level = 2
    casting_time = "1 action"
    components = ('V', 'S', 'M')
    materials = "either a small leather loop or a piece of golden wire bent into a cup shape with a long shank on one end"
    duration = "Concentration, up to 10 minutes"
    magic_school = "Transmutation"
    classes = ()


class Light(Spell):
    """You touch one object that is no larger than 10 feet in any
    dimension. Until the spell ends, the object sheds bright light in
    a 20-foot radius and dim light for an additional 20 feet. The
    light can be colored as you like. Completely covering the object
    with something opaque blocks the light. The spell ends if you cast
    it again or dismiss it as an action. If you target an object held
    or worn by a hostile creature, that creature must succeed on a
    Dexterity saving throw to avoid the spell.
    
    """
    name = "Light"
    level = 0
    casting_time = "1 action"
    components = ('V', 'M')
    materials = "a firefly or phosphorescent moss"
    duration = "1 hour"
    magic_school = "Evocation"
    classes = ()


class LightningBolt(Spell):
    """A stroke of lightning forming a line 100 feet long and 5 feet wide
    blasts out from you in a direction you choose. Each creature in
    the line must make a Dexterity saving throw. A creature takes 8d6
    lightning damage on a failed save, or half as much damage on a
    successful one. The lightning ignites flammable objects in the
    area that aren’t being worn or carried. At Higher Levels. When you
    cast this spell using a spell slot of 4th level or higher, the
    damage increases by 1d6 for each slot level above 3rd.
    
    """
    name = "Lightning Bolt"
    level = 3
    casting_time = "1 action"
    components = ('V', 'S', 'M')
    materials = "a bit of fur and a rod of amber, crystal, or glass"
    duration = "Instantaneous"
    magic_school = "Evocation"
    classes = ()


class LocateCreature(Spell):
    """Describe or name a creature that is familiar to you. You sense the
    direction to the creature’s location, as long as that creature is
    within 1,000 feet of you. If the creature is moving, you know the
    direction of its movement. The spell can locate a specific
    creature known to you, or the nearest creature of a specific kind
    (such as a human or a unicorn), so long as you have seen such a
    creature up close—within 30 feet—at least once. If the creature
    you described or named is in a different form, such as being under
    the effects of a polymorph spell, this spell doesn’t locate the
    creature. This spell can’t locate a creature if running water at
    least 10 feet wide blocks a direct path between you and the
    creature.
    
    """
    name = "Locate Creature"
    level = 4
    casting_time = "1 action"
    components = ('V', 'S', 'M')
    materials = "a bit of fur from a bloodhound"
    duration = "Concentration, up to 1 hour"
    magic_school = "Divination"
    classes = ()


class MageArmor(Spell):
    """You touch a willing creature who isn't wearing armor, and a
    protective magical force surrounds it until the spell ends. The
    target's base AC becomes 13 + its Dexterity modifier. The spell
    ends it if the target dons armor or if you dismiss the spell as an
    action.
    
    """
    name = "Mage Armor"
    level = 1
    casting_time = "1 action"
    casting_range = "Touch"
    components = ("V", "S", "M")
    materials = "A piece of cured leather"
    duration = "8 hours"
    magic_school = "Abjuration"
    classes = ('Sorceror', 'Wizard', )


class MageHand(Spell):
    """A spectral, floating hand appears at a point you choose within
    range. The hand lasts for the duration or until you dismiss it as
    an action. The hand vanishes if it is ever more than 30 feet away
    from you or if you cast this spell again.
    
    You can use your action to control the hand. You can use the hand
    to manipulate an object, open an unlocked door or container, stow
    or retrieve an item from an open container, or pour the contents
    out of a vial. You can move the hand up to 30 feet each time you
    use it.
    
    The hand can't attack, activate magical items, or carry more than
    10 pounds.
    
    """
    name = "Mage Hand"
    level = 0
    casting_time = "1 action"
    casting_range = "30 feet"
    components = ("V", "S", )
    duration = "1 minute"
    magic_school = "Conjuration"
    classes = ('Bard', 'Sorceror', 'Warlock', 'Wizard', )


class MagicJar(Spell):
    """Your body falls into a catatonic state as your soul leaves it
    and enters the container you used for the spell's material
    component. While your soul inhabits the container, you are aware
    of your surroundings as if you were in the container's space. You
    can't move or use reactions. The only action you can take is to
    project your soul up to 100 feet out of the container, either
    returning to your living body (and ending the spell) or attempting to possess a humanoids body.
    
    You can attempt to possess any humanoid within 100 feet of you
    that you can see (creatures warded by a protection from evil and
    good or magic circle spell can't be possessed). The target must
    make a Charisma saving throw. On a failure, your soul moves into
    the target's body, and the target's soul becomes trapped in the
    container. On a success, the target resists your efforts to
    possess it, and you can't attempt to possess it again for 24
    hours.
    
    Once you possess a creature's body, you control it. Your game
    statistics are replaced by the statistics of the creature, though
    you retain your alignment and your Intelligence, Wisdom, and
    Charisma scores. You retain the benefit of your own class
    features. If the target has any class levels, you can't use any of
    its class features.
    
    Meanwhile, the possessed creature's soul can perceive from the
    container using its own senses, but it can't move or take actions
    at all.
    
    While possessing a body, you can use your action to return from
    the host body to the container if it is within 100 feet of you,
    returning the host creature's soul to its body. If the host body
    dies while you're in it, the creature dies, and you must make a
    Charisma saving throw against your own spellcasting DC. On a
    success, you return to the container if it is within 100 feet of
    you. Otherwise, you die.
    
    If the container is destroyed or the spell ends, your soul
    immediately returns to your body. If your body is more than 100
    feet away from you or if your body is dead when you attempt to
    return to it, you die. If another creature's soul is in the
    container when it is destroyed, the creature's soul returns to its
    body if the body is alive and within 100 feet. Otherwise, that
    creature dies.
    
    When the spell ends, the container is destroyed.
    
    """
    name = "Magic Jar"
    level = 6
    casting_time = "1 minute"
    casting_range = "Self"
    components = ("V", "S", "M", )
    materials = "a gem, crystal, reliquary, or some other ornamental container worth at least 500 gp)"
    duration = "Until dispelled"
    magic_school = "Necromancy"
    classes = ('Wizard', )


class MagicMissile(Spell):
    """You create three glowing darts of magical force. Each dart hits a
    creature of your choice that you can see within range. A dart
    deals 1d4+1 force damage to its target. The darts all strike
    simultaneously and you can direct them to hit one creature or
    several.
    
    At Higher Levels: When you cast this spell using a spell slot of
    2nd level or higher, the spell creates one more dart for each slot
    above 1st.
    
    """
    name = "Magic Missile"
    level = 1
    casting_time = "1 action"
    casting_range = "120 feet"
    components = ("V", "S", )
    duration = "Instantaneous"
    magic_school = "Evocation"
    classes = ('Sorceror', 'Wizard', )



class MagicWeapon(Spell):
    """You touch a nonmagical weapon. Until the spell ends, that weapon
    becomes a magic weapon with a +1 bonus to attack rolls and damage
    rolls. At Higher Levels. When you cast this spell using a spell
    slot of 4th level or higher, the bonus increases to +2. When you
    use a spell slot of 6th level or higher, the bonus increases to
    +3.
    
    """
    name = "Magic Weapon"
    level = 2
    casting_time = "1 bonus action"
    components = ('V', 'S')
    materials = ""
    duration = "Concentration, up to 1 hour"
    magic_school = "Transmutation"
    classes = ()



class MajorImage(Spell):
    """You create the image of an object, a creature, or some other
    visible phenomenon that is no larger than a 20-foot cube. The
    image appears at a spot that you can see within range and lasts
    for the duration. It seems completely real, including sounds,
    smells, and temperature appropriate to the thing depicted. You
    can’t create sufficient heat or cold to cause damage, a sound loud
    enough to deal thunder damage or deafen a creature, or a smell
    that might sicken a creature (like a troglodyte’s stench). As long
    as you are within range of the illusion, you can use your action
    to cause the image to move to any other spot within range. As the
    image changes location, you can alter its appearance so that its
    movements appear natural for the image. For example, if you create
    an image of a creature and move it, you can alter the image so
    that it appears to be walking. Similarly, you can cause the
    illusion to make different sounds at different times, even making
    it carry on a conversation, for example. Physical interaction with
    the image reveals it to be an illusion, because things can pass
    through it. A creature that uses its action to examine the image
    can determine that it is an illusion with a successful
    Intelligence (Investigation) check against your spell save DC. If
    a creature discerns the illusion for what it is, the creature can
    see through the image, and its other sensory qualities become
    faint to the creature. At Higher Levels. When you cast this spell
    using a spell slot of 6th level or higher, the spell lasts until
    dispelled, without requiring your concentration.
    
    """
    name = "Major Image"
    level = 3
    casting_time = "1 action"
    components = ('V', 'S', 'M')
    materials = "a bit of fleece"
    duration = "Concentration, up to 10 minutes"
    magic_school = "Illusion"
    classes = ()


class MassCureWounds(Spell):
    """A wave of healing energy washes out from a point of your choice
    within range. Choose up to six creatures in a 30-foot-radius
    sphere centered on that point. Each target regains hit points
    equal to 3d8 + your spellcasting ability modifier. This spell has
    no effect on undead or constructs. At Higher Levels. When you cast
    this spell using a spell slot of 6th level or higher, the healing
    increases by 1d8 for each slot level above 5th.
    
    """
    name = "Mass Cure Wounds"
    level = 5
    casting_time = "1 action"
    components = ('V', 'S')
    materials = ""
    duration = "Instantaneous"
    magic_school = "Conjuration"
    classes = ()


class MassHeal(Spell):
    """A flood of healing energy flows from you into injured creatures
    around you. You restore up to 700 hit points, divided as you
    choose among any number of creatures that you can see within
    range. Creatures healed by this spell are also cured of all
    diseases and any effect making them blinded or deafened. This
    spell has no effect on undead or constructs.
    
    """
    name = "Mass Heal"
    level = 9
    casting_time = "1 action"
    components = ('V', 'S')
    materials = ""
    duration = "Instantaneous"
    magic_school = "Conjuration"
    classes = ()


class MassHealingWord(Spell):
    """As you call out words of restoration, up to six creatures of your
    choice that you can see within range regain hit points equal to
    1d4 + your spellcasting ability modifier. This spell has no effect
    on undead or constructs. At Higher Levels. When you cast this
    spell using a spell slot of 4th level or higher, the healing
    increases by 1d4 for each slot level above 3rd.
    
    """
    name = "Mass Healing Word"
    level = 3
    casting_time = "1 bonus action"
    components = ('V',)
    materials = ""
    duration = "Instantaneous"
    magic_school = "Evocation"
    classes = ()


class MassSuggestion(Spell):
    """You suggest a course of activity (limited to a sentence or two) and
    magically influence up to twelve creatures of your choice that you
    can see within range and that can hear and understand
    you. Creatures that can’t be charmed are immune to this
    effect. The suggestion must be worded in such a manner as to make
    the course of action sound reasonable. Asking the creature to stab
    itself, throw itself onto a spear, immolate itself, or do some
    other obviously harmful act automatically negates the effect of
    the spell. Each target must make a Wisdom saving throw. On a
    failed save, it pursues the course of action you described to the
    best of its ability. The suggested course of action can continue
    for the entire duration. If the suggested activity can be
    completed in a shorter time, the spell ends when the subject
    finishes what it was asked to do. You can also specify conditions
    that will trigger a special activity during the duration. For
    example, you might suggest that a group of soldiers give all their
    money to the first beggar they meet. If the condition isn’t met
    before the spell ends, the activity isn’t performed. If you or any
    of your companions damage a creature affected by this spell, the
    spell ends for that creature. At Higher Levels. When you cast this
    spell using a 7th-level spell slot, the duration is 10 days. When
    you use an 8th-level spell slot, the duration is 30 days. When you
    use a 9th-level spell slot, the duration is a year and a day.
    
    """
    name = "Mass Suggestion"
    level = 6
    casting_time = "1 action"
    components = ('V', 'M')
    materials = "a snake’s tongue and either a bit of honeycomb or a drop of sweet oil"
    duration = "24 hours"
    magic_school = "Enchantment"
    classes = ()


class Maze(Spell):
    """You banish a creature that you can see within range into a
    labyrinthine demiplane. The target remains there for the duration
    or until it escapes the maze. The target can use its action to
    attempt to escape. When it does so, it makes a DC 20 Intelligence
    check. If it succeeds, it escapes, and the spell ends (a minotaur
    or goristro demon automatically succeeds). When the spell ends,
    the target reappears in the space it left or, if that space is
    occupied, in the nearest unoccupied space.
    
    """
    name = "Maze"
    level = 8
    casting_time = "1 action"
    components = ('V', 'S')
    materials = ""
    duration = "Concentration, up to 10 minutes"
    magic_school = "Conjuration"
    classes = ()


class MelfsAcidArrow(Spell):
    """A shimmering green arrow streaks toward a target within range and
    burst in a spray of acid. Make a ranged spell attack against the
    target. On a hit, the target takes 4d4 acid damage immediately and
    2d4 acid damage at the end of its next turn. On a miss, the arrow
    splashes the target for half as much of the initial damage and no
    damage at the end of its next turn.
    
    **At Higher Levels.** When you cast this spell using a spell slot
    of 3rd level or higher, the damage (both initial and later)
    increases by 1d4 for each slot level above 2nd.
    
    """
    name = "Melf's Acid Arrow"
    level = 2
    casting_time = "1 action"
    components = ('V', 'S', 'M', )
    materials = "powdered rhubarb leaf and an adder's stomach"
    duration = "Instantaneous"
    magic_school = "Evocation"
    classes = ('Wizard', )


class MeteorSwarm(Spell):
    """Blazing orbs of fire plummet to the ground at four different points
    you can see within range. Each creature in a 40-foot-radius sphere
    centered on each point you choose must make a Dexterity saving
    throw. The sphere spreads around corners. A creature takes 20d6
    fire damage and 20d6 bludgeoning damage on a failed save, or half
    as much damage on a successful one. A creature in the area of more
    than one fiery burst is affected only once. The spell damages
    objects in the area and ignites flammable objects that aren’t
    being worn or carried.
    
    """
    name = "Meteor Swarm"
    level = 9
    casting_time = "1 action"
    components = ('V', 'S')
    materials = ""
    duration = "Instantaneous"
    magic_school = "Evocation"
    classes = ()


class MinorIllusion(Spell):
    """You create a sound or an image of an object within range that lasts
    for the duration. The illusion also ends if you dismiss it as an
    action or cast this spell again. If you create a sound, its volume
    can range from a whisper to a scream. It can be your voice,
    someone else’s voice, a lion’s roar, a beating of drums, or any
    other sound you choose. The sound continues unabated throughout
    the duration, or you can make discrete sounds at different times
    before the spell ends. If you create an image of an object—such as
    a chair, muddy footprints, or a small chest—it must be no larger
    than a 5-foot cube. The image can’t create sound, light, smell, or
    any other sensory effect. Physical interaction with the image
    reveals it to be an illusion, because things can pass through
    it. If a creature uses its action to examine the sound or image,
    the creature can determine that it is an illusion with a
    successful Intelligence (Investigation) check against your spell
    save DC. If a creature discerns the illusion for what it is, the
    illusion becomes faint to the creature.
    
    """
    name = "Minor Illusion"
    level = 0
    casting_time = "1 action"
    components = ('S', 'M')
    materials = "a bit of fleece"
    duration = "1 minute"
    magic_school = "Illusion"
    classes = ()


class MistyStep(Spell):
    """Briefly surrounded by silvery mist, you teleport up to 30 feet to
    an unoccupied space that you can see.
    
    """
    name = "Misty Step"
    level = 2
    casting_time = "1 bonus action"
    components = ('V',)
    materials = ""
    duration = "Instantaneous"
    magic_school = "Conjuration"
    classes = ()


class MordenkainensSword(Spell):
    """You create a sword-shaped plane of force that hovers within
    range. It lasts for the duration. When the sword appears, you make
    a melee spell attack against a target of your choice within 5 feet
    of the sword. On a hit, the target takes 3d10 force damage. Until
    the spell ends, you can use a bonus action on each of your turns
    to move the sword up to 20 feet to a spot you can see and repeat
    this attack against the same target or a different one.
    
    """
    name = "Mordenkainen's Sword"
    level = 7
    casting_time = "1 action"
    components = ('V', 'S', 'M')
    materials = "a miniature platinum sword with a grip and pommel of copper and zinc, worth 250 gp"
    duration = "Concentration, up to 1 minute"
    magic_school = "Evocation"
    classes = ()


class OttosIrresistibleDance(Spell):
    """Choose one creature that you can see within range. The target
    begins a comic dance in place: shuffling, tapping its feet, and
    capering for the duration. Creatures that can’t be charmed are
    immune to this spell. A dancing creature must use all its movement
    to dance without leaving its space and has disadvantage on
    Dexterity saving throws and attack rolls. While the target is
    affected by this spell, other creatures have advantage on attack
    rolls against it. As an action, a dancing creature makes a Wisdom
    saving throw to regain control of itself. On a successful save,
    the spell ends.
    
    """
    name = "Otto's Irresistible Dance"
    level = 6
    casting_time = "1 action"
    components = ('V',)
    materials = ""
    duration = "Concentration, up to 1 minute"
    magic_school = "Enchantment"
    classes = ('Bard', 'Wizard')


class Passwall(Spell):
    """A passage appears at a point of your choice that you can see on a
    wooden, plaster, or stone surface (such as a wall, a ceiling, or a
    floor) within range, and lasts for the duration. You choose the
    opening’s dimensions: up to 5 feet wide, 8 feet tall, and 20 feet
    deep. The passage creates no instability in a structure
    surrounding it. When the opening disappears, any creatures or
    objects still in the passage created by the spell are safely
    ejected to an unoccupied space nearest to the surface on which you
    cast the spell.
    
    """
    name = "Passwall"
    level = 5
    casting_time = "1 action"
    components = ('V', 'S', 'M')
    materials = "a pinch of sesame seeds"
    duration = "1 hour"
    magic_school = "Transmutation"
    classes = ('Wizard',)


class PhantasmalForce(Spell):
    """You craft an illusion that takes root in the mind of a creature
    that you can see within range. The target must make an
    Intelligence saving throw. On a failed save, you create a
    phantasmal object, creature or other visible phenomenon of your
    choice that is no larger than a 10-foot cube and that is
    perceivable only to the target for the duration. This spell has no
    effect on undead or constructs.
    
    The phantasm includes sound, temperature, and other stimuli, also
    evident only to the creature. The target can use its action to
    examine the phantasm with an Intelligence (Investigation) check
    against your spell save DC. If the check succeeds, the target
    realizes that the phantasm is an illusion, and the spell
    ends. While a target is affected by the spell, the target treats
    the phantasm as if it were real. The target rationalizes any
    illogical outcomes from interacting with the phantasm. For
    example, a target attempting to walk across a phantasmal bridge
    that spans a chasm falls once it steps onto the bridge. If the
    target survives the fall, it still believes that the bridge exists
    and comes up with some other explanation for its fall-it was
    pushed, it slipped, or a strong wind might have knocked it off.
    
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
    components = ('V', 'S', 'M')
    materials = "A bit of fleece"
    duration = "Concentration, up to 1 minute"
    magic_school = "Illusion"
    classes = ('Bard', 'Sorceror', 'Wizard')


class PoisonSpray(Spell):
    """You extend your hand toward a creature you can see within range and
    project a puff of noxious gas from your palm. The creature must
    succeed on a Constitution saving throw or take 1d12 poison
    damage. This spell’s damage increases by 1d12 when you reach 5th
    level (2d12), 11th level (3d12), and 17th level (4d12).
    
    """
    name = "Poison Spray"
    level = 0
    casting_time = "1 action"
    components = ('V', 'S')
    materials = ""
    duration = "Instantaneous"
    magic_school = "Conjuration"
    classes = ()


class PowerWordKill(Spell):
    """You utter a word of power that can compel one creature you can see
    within range to die instantly. If the creature you choose has 100
    hit points or fewer, it dies. Otherwise, the spell has no
    effect.
    
    """
    name = "Power Word Kill"    
    level = 9
    casting_time = "1 action"
    components = ('V',)
    materials = ""
    duration = "Instantaneous"
    magic_school = "Enchantment"
    classes = ('Bard', 'Wizard', 'Sorceror', 'Warlock')


class PowerWordStun(Spell):
    """You speak a word of power that can overwhelm the mind of one
    creature you can see within range, leaving it dumbfounded. If the
    target has 150 hit points or fewer, it is stunned. Otherwise, the
    spell has no effect. The stunned target must make a Constitution
    saving throw at the end of each of its turns. On a successful
    save, this stunning effect ends.
    
    """
    name = "Power Word Stun"
    level = 8
    casting_time = "1 action"
    components = ('V',)
    materials = ""
    duration = "Instantaneous"
    magic_school = "Enchantment"
    classes = ()


class PrayerOfHealing(Spell):
    """Up to six creatures of your choice that you can see within range
    each regain hit points equal to 2d8 + your spellcasting ability
    modifier. This spell has no effect on undead or constructs. At
    Higher Levels. When you cast this spell using a spell slot of 3rd
    level or higher, the healing increases by 1d8 for each slot level
    above 2nd.
    
    """
    name = "PrayerOfHealing"
    level = 2
    casting_time = "10 minutes"
    components = ('V',)
    materials = ""
    duration = "Instantaneous"
    magic_school = "Evocation"
    classes = ()


class Prestidigitation(Spell):
    """This spell is a minor magical trick that novice spellcasters use
    for practice. You create one of the following magical effects
    within range.
    
    - You create an instantaneous, harmless sensory effect, such as a
      shower of sparks, a puff of wind, faint musical notes, or an odd
      odor.
    - You instantaneously light or snuff out a candle, a torch, or a
      small campfire.
    - You instantaneously clean or soil an object no larger than 1
      cubic foot.
    - You chill, warm, or flavor up to 1 cubic foot of nonliving
      material for 1 hour.
    - You make a color, a small mark, or a symbol appear on an object
      or a surface for 1 hour.
    - You create a nonmagical trinket or an illusory image that can
      fit in your hand and that lasts until the end of your next turn.
    
    If you cast this spell multiple times, you can have up to three of
    its non-instantaneous effects active at a time, and you can
    dismiss such an effect as an action.
    
    """
    name = "Prestidigitation"
    level = 0
    casting_time = "1 action"
    casting_range = "10 feet"
    components = ("V", "S", )
    duration = "1 hour"
    magic_school = "Transmutation"
    classes = ('Bard', 'Sorceror', 'Warlock', 'Wizard', )


class ProtectionFromEnergy(Spell):
    """For the duration, the willing creature you touch has resistance to
    one damage type of your choice: acid, cold, fire, lightning, or
    thunder.
    
    """
    name = "Protection from Energy"
    level = 3
    casting_time = "1 action"
    components = ('V', 'S')
    materials = ""
    duration = "Concentration, up to 1 hour"
    magic_school = "Abjuration"
    classes = ()


class RaiseDead(Spell):
    """You return a dead creature you touch to life, provided that it has
    been dead no longer than 10 days. If the creature’s soul is both
    willing and at liberty to rejoin the body, the creature returns to
    life with 1 hit point.
    
    This spell also neutralizes any poisons and
    cures nonmagical diseases that affected the creature at the time
    it died. This spell doesn’t, however, remove magical diseases,
    curses, or similar effects; if these aren’t first removed prior to
    casting the spell, they take effect when the creature returns to
    life. The spell can’t return an undead creature to life.
    
    This spell closes all mortal wounds, but it doesn’t restore
    missing body parts. If the creature is lacking body parts or
    organs integral for its survival—its head, for instance—the spell
    automatically fails.
    
    Coming back from the dead is an ordeal. The target takes a −4
    penalty to all attack rolls, saving throws, and ability
    checks. Every time the target finishes a long rest, the penalty is
    reduced by 1 until it disappears.
    
    """
    name = "Raise Dead"
    level = 5
    casting_time = "1 hour"
    casting_range = "Touch"
    components = ('V', 'S', 'M')
    materials = "a diamond worth at least 500 gp, which the spell consumes"
    duration = "Instantaneous"
    magic_school = "Necromancy"
    classes = ('Bard', 'Cleric', 'Paladin', )


class RayOfEnfeeblement(Spell):
    """A black beam of enervating energy springs from your finger toward a
    creature within range. Make a ranged spell attack against the
    target. On a hit, the target deals only half damage with weapon
    attacks that use Strength until the spell ends.
    
    At the end of each of the target's turns, it can make a
    Constitution saving throw against the spell. On a success, the
    spell ends.
    
    """
    name = "Ray of Enfeeblement"
    level = 2
    casting_time = "1 action"
    casting_range = "60 feet"
    components = ('V', 'S', )
    materials = ""
    duration = "Concentration (1 minute)"
    magic_school = "Necromancy"
    classes = ('Warlock', 'Wizard', )


class RayOfFrost(Spell):
    """A frigid beam of blue-white light streaks toward a creature within
    range. Make a ranged spell attack against the target. On a hit, it
    takes 1d8 cold damage, and its speed is reduced by 10 feet until
    the start of your next turn.
    
    The spell's damage increases by 1d8 when you reach 5th level
    (2d8), 11th level (3d8), and 17th level (4d8).
    
    """
    name = "Ray of Frost"
    level = 0
    casting_time = "1 action"
    casting_range = "60 feet"
    components = ("V", "S", )
    duration = "Instantaneous"
    magic_school = "Evocation"
    classes = ('Sorceror', 'Wizard', )


class RayOfSickness(Spell):
    """A ray of sickening greenish energy lashes out toward a creature
    within range. Make a ranged spell attack against the target. On a
    hit, the target takes 2d8 poison damage and must make a
    Constitution saving throw. On a failed save, it is also poisoned
    until the end of your next turn.
    
    At Higher Levels. When you cast this spell using a spell slot of
    2nd level or higher, the damage increases by 1d8 for each slot
    level above 1st.
    
    """
    name = "Ray of Sickness"
    level = 1
    casting_time = "1 action"
    casting_range = "60 feet"
    components = ("V", "S", )
    duration = "Instantaneous"
    magic_school = "Necromancy"
    classes = ('Sorceror', 'Wizard', )


class Regenerate(Spell):
    """You touch a creature and stimulate its natural healing ability. The
    target regains 4d8 + 15 hit points. For the duration of the spell,
    the target regains 1 hit point at the start of each of its turns
    (10 hit points each minute). The target’s severed body members
    (fingers, legs, tails, and so on), if any, are restored after 2
    minutes. If you have the severed part and hold it to the stump,
    the spell instantaneously causes the limb to knit to the stump.
    
    """
    name = "Regenerate"
    level = 7
    casting_time = "1 minute"
    components = ('V', 'S', 'M')
    materials = "a prayer wheel and holy water"
    duration = "1 hour"
    magic_school = "Transmutation"
    classes = ()


class RemoveCurse(Spell):
    """At your touch, all curses affecting one creature or object end. If
    the object is a cursed magic item, its curse remains, but the
    spell breaks its owner’s attunement to the object so it can be
    removed or discarded.
    
    """
    name = "Remove Curse"
    level = 3
    casting_time = "1 action"
    components = ('V', 'S')
    materials = ""
    duration = "Instantaneous"
    magic_school = "Abjuration"
    classes = ()


class Resistance(Spell):
    """You touch one willing creature. Once before the spell ends, the
    target can roll a d4 and add the number rolled to one saving throw
    of its choice. It can roll the die before or after making the
    saving throw. The spell then ends.
    
    """
    name = "Resistance"
    level = 0
    casting_time = "1 action"
    components = ('V', 'S', 'M')
    materials = "a miniature cloak"
    duration = "Concentration, up to 1 minute"
    magic_school = "Abjuration"
    classes = ()


class Resurrection(Spell):
    """You touch a dead creature that has been dead for no more than a
    century, that didn’t die of old age, and that isn’t undead. If its
    soul is free and willing, the target returns to life with all its
    hit points. This spell neutralizes any poisons and cures normal
    diseases afflicting the creature when it died. It doesn’t,
    however, remove magical diseases, curses, and the like; if such
    effects aren’t removed prior to casting the spell, they afflict
    the target on its return to life. This spell closes all mortal
    wounds and restores any missing body parts. Coming back from the
    dead is an ordeal. The target takes a −4 penalty to all attack
    rolls, saving throws, and ability checks. Every time the target
    finishes a long rest, the penalty is reduced by 1 until it
    disappears. Casting this spell to restore life to a creature that
    has been dead for one year or longer taxes you greatly. Until you
    finish a long rest, you can’t cast spells again, and you have
    disadvantage on all attack rolls, ability checks, and saving
    throws.
    
    """
    name = "Resurrection"
    level = 7
    casting_time = "1 hour"
    components = ('V', 'S', 'M')
    materials = "a diamond worth at least 1,000 gp, which the spell consumes"
    duration = "Instantaneous"
    magic_school = "Necromancy"
    classes = ()


class Revivify(Spell):
    """You touch a creature that has died within the last minute. That
    creature returns to life with 1 hit point. This spell can’t return
    to life a creature that has died of old age, nor can it restore
    any missing body parts.
    
    """
    name = "Revivify"
    level = 3
    casting_time = "1 action"
    components = ('V', 'S', 'M')
    materials = "diamonds worth 300 gp, which the spell consumes"
    duration = "Instantaneous"
    magic_school = "Conjuration"
    classes = ()


class SacredFlame(Spell):
    """Flame-like radiance descends on a creature that you can see within
    range. The target must succeed on a Dexterity saving throw or take
    1d8 radiant damage. The target gains no benefit from cover for
    this saving throw. The spell’s damage increases by 1d8 when you
    reach 5th level (2d8), 11th level (3d8), and 17th level (4d8).
    
    """
    name = "Sacred Flame"
    level = 0
    casting_time = "1 action"
    components = ('V', 'S')
    materials = ""
    duration = "Instantaneous"
    magic_school = "Evocation"
    classes = ()


class Sanctuary(Spell):
    """You ward a creature within range against attack. Until the spell
    ends, any creature who targets the warded creature with an attack
    or a harmful spell must first make a Wisdom saving throw. On a
    failed save, the creature must choose a new target or lose the
    attack or spell. This spell doesn’t protect the warded creature
    from area effects, such as the explosion of a fireball. If the
    warded creature makes an attack or casts a spell that affects an
    enemy creature, this spell ends.
    
    """
    name = "Sanctuary"
    level = 1
    casting_time = "1 bonus action"
    components = ('V', 'S', 'M')
    materials = "a small silver mirror"
    duration = "1 minute"
    magic_school = "Abjuration"
    classes = ()


class Shatter(Spell):
    """A sudden loud ringing noise, painfully intense, erupts from a point
    of your choice within range. Each creature in a 10-foot-radius
    sphere centered on that point must make a Constitution saving
    throw. A creature takes 3d8 thunder damage on a failed save, or
    half as much damage on a successful one. A creature made of
    inorganic material such as stone, crystal, or metal has
    disadvantage on this saving throw. A nonmagical object that isn’t
    being worn or carried also takes the damage if it’s in the spell’s
    area. At Higher Levels. When you cast this spell using a spell
    slot of 3rd level or higher, the damage increases by 1d8 for each
    slot level above 2nd.
    
    """
    name = "Shatter"
    level = 2
    casting_time = "1 action"
    components = ('V', 'S', 'M')
    materials = "a chip of mica"
    duration = "Instantaneous"
    magic_school = "Evocation"
    classes = ()


class Shield(Spell):
    """An invisible barrier of magical force appears and protects
    you. Until the start of your next turn, you have a +5 bonus to AC,
    including against the triggering attack, and you take no damage
    from magic missile.
    
    """
    name = "Shield"
    level = 1
    casting_time = "1 reaction"
    casting_range = "Self"
    components = ("V", "S", )
    duration = "1 round"
    magic_school = "Abjuration"
    classes = ('Sorceror', 'Wizard', )


class ShieldOfFaith(Spell):
    """A shimmering field appears and surrounds a creature of your choice
    within range, granting it a +2 bonus to AC for the duration.
    
    """
    name = "Shield of Faith"
    level = 1
    casting_time = "1 bonus action"
    components = ('V', 'S', 'M')
    materials = "a small parchment with a bit of holy text written on it"
    duration = "Concentration, up to 10 minutes"
    magic_school = "Abjuration"
    classes = ()


class ShockingGrasp(Spell):
    """Lightning springs from your hand to deliver a shock to a creature
    you try to touch. Make a melee spell attack against the
    target. You have advantage on the attack roll if the target is
    wearing armor made of metal. On a hit, the target takes 1d8
    lightning damage, and it can't take reactions until the start of
    its next turn.
    
    The spell's damage increases by 1d8 when you reach 5th level
    (2d8), 11th level (3d8), and 17th level (4d8).
    
    """
    name = "Shocking Grasp"
    level = 0
    casting_time = "1 action"
    casting_range = "Touch"
    components = ("V", "S", )
    duration = "Instantaneous"
    magic_school = "Evocation"
    classes = ('Sorceror', 'Wizard', )


class Silence(Spell):
    """For the duration, no sound can be created within or pass through a
    20-foot-radius sphere centered on a point you choose within
    range. Any creature or object entirely inside the sphere is immune
    to thunder damage, and creatures are deafened while entirely
    inside it. Casting a spell that includes a verbal component is
    impossible there.
    
    """
    name = "Silence"
    level = 2
    casting_time = "1 action"
    components = ('V', 'S')
    materials = ""
    duration = "Concentration, up to 10 minutes"
    magic_school = "Illusion"
    classes = ()


class SilentImage(Spell):
    """You create the image of an object, a creature, or some other
    visible phenomenon that is no larger than a 15-foot cube. The
    image appears at a spot within range and lasts for the
    duration. The image is purely visual; it isn’t accompanied by
    sound, smell, or other sensory effects. You can use your action to
    cause the image to move to any spot within range. As the image
    changes location, you can alter its appearance so that its
    movements appear natural for the image. For example, if you create
    an image of a creature and move it, you can alter the image so
    that it appears to be walking. Physical interaction with the image
    reveals it to be an illusion, because things can pass through
    it. A creature that uses its action to examine the image can
    determine that it is an illusion with a successful Intelligence
    (Investigation) check against your spell save DC. If a creature
    discerns the illusion for what it is, the creature can see through
    the image.
    
    """
    name = "Silent Image"
    level = 1
    casting_time = "1 action"
    components = ('V', 'S', 'M')
    materials = "a bit of fleece"
    duration = "Concentration, up to 10 minutes"
    magic_school = "Illusion"
    classes = ()


class Sleep(Spell):
    """This spell sends creatures into a magical slumber. Roll 5d8, the
    total is how many hit points of creatures this spell can
    affect. Creatures within 20 feet of a point you choose within
    range are affected in ascending order of their current hit points
    (ignoring unconscious creatures).
    
    Starting with the creature that has the lowest current hit points,
    each creature affected by this spell falls unconscious until the
    spell ends, the sleeper takes damage, or someone uses an action to
    shake or slap the sleeper awake. Subtract each creature's hit
    points from the total before moving on to the creature with the
    next lowest hit points. A creature's hit points must be equal to
    or less than the remaining total for that creature to be affected.
    
    Undead and creatures immune to being charmed aren't affected by
    this spell.
    
    At Higher Levels: When you cast this spell using a spell slot of
    2nd level or higher, roll an additional 2d8 for each slot level
    above 1st.
    
    """
    name = "Sleep"
    level = 1
    casting_time = "1 action"
    casting_range = "90 feet"
    components = ("V", "S", "M", )
    materials = "A pinch of fine sand, rose petals, or a cricket"
    duration = "1 minutes"
    magic_school = "Enchantment"
    classes = ('Bard', 'Sorceror', 'Wizard', )


class SpareTheDying(Spell):
    """You touch a living creature that has 0 hit points. The creature
    becomes stable. This spell has no effect on undead or
    constructs.
    
    """
    name = "Spare the Dying"
    level = 0
    casting_time = "1 action"
    components = ('V', 'S')
    materials = ""
    duration = "Instantaneous"
    magic_school = "Necromancy"
    classes = ()


class SpeakWithDead(Spell):
    """You grant the semblance of life and intelligence to a corpse of
    your choice within range, allowing it to answer the questions you
    pose. The corpse must still have a mouth and can’t be undead. The
    spell fails if the corpse was the target of this spell within the
    last 10 days. Until the spell ends, you can ask the corpse up to
    five questions. The corpse knows only what it knew in life,
    including the languages it knew. Answers are usually brief,
    cryptic, or repetitive, and the corpse is under no compulsion to
    offer a truthful answer if you are hostile to it or it recognizes
    you as an enemy. This spell doesn’t return the creature’s soul to
    its body, only its animating spirit. Thus, the corpse can’t learn
    new information, doesn’t comprehend anything that has happened
    since it died, and can’t speculate about future events.
    
    """
    name = "Speak with Dead"
    level = 3
    casting_time = "1 action"
    components = ('V', 'S', 'M')
    materials = "burning incense"
    duration = "10 minutes"
    magic_school = "Necromancy"
    classes = ()


class SpiderClimb(Spell):
    """Until the spell ends, one willing creature you touch gains the
    ability to move up, down, and across vertical surfaces and upside
    down along ceilings, while leaving its hands free. The target also
    gains a climbing speed equal to its walking speed.
    
    """
    name = "Spider Climb"
    level = 2
    casting_time = "1 action"
    components = ('V', 'S', 'M')
    materials = "a drop of bitumen and a spider"
    duration = "Concentration, up to 1 hour"
    magic_school = "Transmutation"
    classes = ()


class SpiritGuardians(Spell):
    """You call forth spirits to protect you. They flit around you to a
    distance of 15 feet for the duration. If you are good or neutral,
    their spectral form appears angelic or fey (your choice). If you
    are evil, they appear fiendish. When you cast this spell, you can
    designate any number of creatures you can see to be unaffected by
    it. An affected creature’s speed is halved in the area, and when
    the creature enters the area for the first time on a turn or
    starts its turn there, it must make a Wisdom saving throw. On a
    failed save, the creature takes 3d8 radiant damage (if you are
    good or neutral) or 3d8 necrotic damage (if you are evil). On a
    successful save, the creature takes half as much damage. At Higher
    Levels. When you cast this spell using a spell slot of 4th level
    or higher, the damage increases by 1d8 for each slot level above
    3rd.
    
    """
    name = "Spirit Guardians"
    level = 3
    casting_time = "1 action"
    components = ('V', 'S', 'M')
    materials = "a holy symbol"
    duration = "Concentration, up to 10 minutes"
    magic_school = "Conjuration"
    classes = ()


class SpiritualWeapon(Spell):
    """You create a floating, spectral weapon within range that lasts for
    the duration or until you cast this spell again. When you cast the
    spell, you can make a melee spell attack against a creature within
    5 feet of the weapon. On a hit, the target takes force damage
    equal to 1d8 + your spellcasting ability modifier. As a bonus
    action on your turn, you can move the weapon up to 20 feet and
    repeat the attack against a creature within 5 feet of it. The
    weapon can take whatever form you choose. Clerics of deities who
    are associated with a particular weapon (as St. Cuthbert is known
    for his mace and Thor for his hammer) make this spell’s effect
    resemble that weapon. At Higher Levels. When you cast this spell
    using a spell slot of 3rd level or higher, the damage increases by
    1d8 for every two slot levels above the 2nd.
    
    """
    name = "Spiritual Weapon"
    level = 2
    casting_time = "1 bonus action"
    components = ('V', 'S')
    materials = ""
    duration = "1 minute"
    magic_school = "Evocation"
    classes = ()


class Stoneskin(Spell):
    """This spell turns the flesh of a willing creature you touch as hard
    as stone. Until the spell ends, the target has resistance to
    nonmagical bludgeoning, piercing, and slashing damage.
    
    """
    name = "Stoneskin"
    level = 4
    casting_time = "1 action"
    components = ('V', 'S', 'M')
    materials = "diamond dust worth 100 gp, which the spell consumes"
    duration = "Concentration, up to 1 hour"
    magic_school = "Abjuration"
    classes = ()


class Suggestion(Spell):
    """You suggest a course of activity (limited to a sentence or two) and
    magically influence a creature you can see within range that can
    hear and understand you. Creatures that can’t be charmed are
    immune to this effect. The suggestion must be worded in such a
    manner as to make the course of action sound reasonable. Asking
    the creature to stab itself, throw itself onto a spear, immolate
    itself, or do some other obviously harmful act ends the spell.
    
    The target must make a Wisdom saving throw. On a failed save, it
    pursues the course of action you described to the best of its
    ability. The suggested course of action can continue for the
    entire duration. If the suggested activity can be completed in a
    shorter time, the spell ends when the subject finishes what it was
    asked to do.
    
    You can also specify conditions that will trigger a special
    activity during the duration. For example, you might suggest that
    a knight give her warhorse to the first beggar she meets. If the
    condition isn’t met before the spell expires, the activity isn’t
    performed.
    
    If you or any of your companions damage the target, the spell
    ends.

    """
    name = "Suggestion"
    level = 2
    casting_time = "1 action"
    components = ('V', 'M')
    materials = "a snake’s tongue and either a bit of honeycomb or a drop of sweet oil"
    duration = "Concentration, up to 8 hours"
    magic_school = "Enchantment"
    classes = ()


class Sunburst(Spell):
    """Brilliant sunlight flashes in a 60-foot radius centered on a point
    you choose within range. Each creature in that light must make a
    Constitution saving throw. On a failed save, a creature takes 12d6
    radiant damage and is blinded for 1 minute. On a successful save,
    it takes half as much damage and isn’t blinded by this
    spell. Undead and oozes have disadvantage on this saving throw.
    
    A creature blinded by this spell makes another Constitution saving
    throw at the end of each of its turns. On a successful save, it is
    no longer blinded.
    
    This spell dispels any darkness in its area that was created by a
    spell.
    
    """
    name = "Sunburst"
    level = 8
    casting_time = "1 action"
    components = ('V', 'S', 'M')
    materials = "fire and a piece of sunstone"
    duration = "Instantaneous"
    magic_school = "Evocation"
    classes = ()


class Teleport(Spell):
    """This spell instantly transports you and up to eight willing
    creatures of your choice that you can see within range, or a
    single object that you can see within range, to a destination you
    select. If you target an object, it must be able to fit entirely
    inside a 10-foot cube, and it can’t be held or carried by an
    unwilling creature.
    
    The destination you choose must be known to you, and it must be on
    the same plane of existence as you. Your familiarity with the
    destination determines whether you arrive there successfully. The
    DM rolls d100 and consults the table.
    
    =================  ======  ============  ==========  =========
    Familiarity        Mishap  Similar Area  Off Target  On Target
    =================  ======  ============  ==========  =========
    Permanent circle   --      --            --          01-100
    Associated object  --      --            --          01-100
    Very familiar      01–05   06–13         14–24       25–100
    Seen casually      01–33   34–43         44–53       54–100
    Viewed once        01–43   44–53         54–73       74–100
    Description        01–43   44–53         54–73       74–100
    False destination  01–50   51–100        --          --
    =================  ======  ============  ==========  =========
    
    **Familiarity** “Permanent circle” means a permanent teleportation
    circle whose sigil sequence you know. “Associated object” means
    that you possess an object taken from the desired destination
    within the last six months, such as a book from a wizard’s
    library, bed linen from a royal suite, or a chunk of marble from a
    lich’s secret tomb.
    
    “Very familiar” is a place you have been very often, a place you
    have carefully studied, or a place you can see when you cast the
    spell. “Seen casually” is someplace you have seen more than once
    but with which you aren’t very familiar. “Viewed once” is a place
    you have seen once, possibly using magic. “Description” is a place
    whose location and appearance you know through someone else’s
    description, perhaps from a map.
    
    “False destination” is a place that doesn’t exist. Perhaps you
    tried to scry an enemy’s sanctum but instead viewed an illusion,
    or you are attempting to teleport to a familiar location that no
    longer exists.
    
    **On Target.** You and
    your group (or the target object) appear where you want to.
    
    **Off Target.** You and your group (or the target object) appear a
    random distance away from the destination in a random
    direction. Distance off target is 1d10 × 1d10 percent of the
    distance that was to be traveled. For example, if you tried to
    travel 120 miles, landed off target, and rolled a 5 and 3 on the
    two d10s, then you would be off target by 15 percent, or 18
    miles. The DM determines the direction off target randomly by
    rolling a d8 and designating 1 as north, 2 as northeast, 3 as
    east, and so on around the points of the compass. If you were
    teleporting to a coastal city and wound up 18 miles out at sea,
    you could be in trouble.
    
    **Similar Area.** You and your group (or the target object) wind
    up in a different area that’s visually or thematically similar to
    the target area. If you are heading for your home laboratory, for
    example, you might wind up in another wizard’s laboratory or in an
    alchemical supply shop that has many of the same tools and
    implements as your laboratory. Generally, you appear in the
    closest similar place, but since the spell has no range limit, you
    could conceivably wind up anywhere on the plane.
    
    **Mishap.** The spell’s unpredictable magic results in a difficult
    journey. Each teleporting creature (or the target object) takes
    3d10 force damage, and the DM rerolls on the table to see where
    you wind up (multiple mishaps can occur, dealing damage each
    time).
    
    """
    name = "Teleport"
    level = 7
    casting_time = "1 action"
    components = ('V',)
    materials = ""
    duration = "Instantaneous"
    magic_school = "Conjuration"
    classes = ()


class Thaumaturgy(Spell):
    """You manifest a minor wonder, a sign of supernatural power, within
    range. You create one of the following magical effects within
    range:
    
    - Your voice booms up to three times as loud as normal for 1 minute.
    - You cause flames to flicker, brighten, dim, or change color for 1 minute.
    - You cause harmless tremors in the ground for 1 minute.
    - You create an instantaneous sound that originates from a point
      of your choice within range, such as a rumble of thunder, the
      cry of a raven, or omi- nous whispers.
    - You instantaneously cause an unlocked door or win- dow to fly
      open or slam shut.
    - You alter the appearance of your eyes for 1 minute.
    
    If you cast this spell multiple times, you can have up to three of
    its 1-minute effects active at a time, and you can dismiss such an
    effect as an action.
    
    """
    name = "Thaumaturgy"
    level = 0
    casting_time = "1 action"
    components = ('V',)
    materials = ""
    duration = "Up to 1 minute"
    magic_school = "Transmutation"
    classes = ()


class Thunderwave(Spell):
    """A wave of thunderous force sweeps out from you. Each creature in a
    15-foot cube originating from you must make a Constitution saving
    throw. On a failed save, a creature takes 2d8 thunder damage and
    is pushed 10 feet away from you. On a successful save, the
    creature takes half as much damage and isn’t pushed. In addition,
    unsecured objects that are completely within the area of effect
    are automatically pushed 10 feet away from you by the spell’s
    effect, and the spell emits a thunderous boom audible out to 300
    feet. At Higher Levels. When you cast this spell using a spell
    slot of 2nd level or higher, the damage increases by 1d8 for each
    slot level above 1st.
    
    """
    name = "Thunderwave"
    level = 1
    casting_time = "1 action"
    components = ('V', 'S')
    materials = ""
    duration = "Instantaneous"
    magic_school = "Evocation"
    classes = ()


class TimeStop(Spell):
    """You briefly stop the flow of time for everyone but yourself. No
    time passes for other creatures, while you take 1d4 + 1 turns in a
    row, during which you can use actions and move as normal.
    
    This spell ends if one of the actions you use during this period,
    or any effects that you create during this period, affects a
    creature other than you or an object being worn or carried by
    someone other than you. In addition, the spell ends if you move to
    a place more than 1,000 feet from the location where you cast it.
    
    """
    name = "Time Stop"
    level = 9
    casting_time = "1 action"
    components = ('V',)
    materials = ""
    duration = "Instantaneous"
    magic_school = "Transmutation"
    classes = ()


class TrueResurrection(Spell):
    """You touch a creature that has been dead for no longer than 200
    years and that died for any reason except old age. If the
    creature’s soul is free and willing, the creature is restored to
    life with all its hit points. This spell closes all wounds,
    neutralizes any poison, cures all diseases, and lifts any curses
    affecting the creature when it died. The spell replaces damaged or
    missing organs and limbs. The spell can even provide a new body if
    the original no longer exists, in which case you must speak the
    creature’s name. The creature then appears in an unoccupied space
    you choose within 10 feet of you.
    
    """
    name = "True Resurrection"
    level = 9
    casting_time = "1 hour"
    components = ('V', 'S', 'M')
    materials = "a sprinkle of holy water and diamonds worth at least 25,000 gp, which the spell consumes"
    duration = "Instantaneous"
    magic_school = "Necromancy"
    classes = ()


class TrueSeeing(Spell):
    """This spell gives the willing creature you touch the ability to see
    things as they actually are. For the duration, the creature has
    truesight, notices secret doors hidden by magic, and can see into
    the Ethereal Plane, all out to a range of 120 feet.
    
    """
    name = "True Seeing"
    level = 6
    casting_time = "1 action"
    components = ('V', 'S', 'M')
    materials = "an ointment for the eyes that costs 25 gp; is made from mushroom powder, saffron, and fat; and is consumed by the spell"
    duration = "1 hour"
    magic_school = "Divination"
    classes = ()


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
