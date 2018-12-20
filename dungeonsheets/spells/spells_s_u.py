from .spells import Spell


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


class Shillelagh(Spell):
    """The wood of a club or quarterstaff you are holding is imbued with
    nature's power. For the duration, you can use your spellcasting
    ability instead of Strength for the attack and damage rolls of
    melee attacks using that weapon, and the weapon's damage die
    becomes a ``d8``. The weapon also becomes magical, if it isn't
    already. The spell ends if you cast it again or if you let go of
    the weapon.

    """
    level = 0
    name = "Shillelagh"
    casting_time = "1 bonus action"
    casting_range = "Touch"
    components = ("V", "S", "M")
    materials = "mistletoe, a shamrock leaf, and a club or quarterstaff"
    duration = "1 minute"
    ritual = False
    magic_school = "Transmutation"
    classes = ('Druid')


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


class SpeakWithAnimals(Spell):
    """You gain the ability to comprehend and verbally communicate with
    beasts for the duration. The knowledge and awareness of many
    beasts is limited by their intelligence, but at minimum, beasts
    can give you information about nearby locations and monsters,
    including whatever they can perceive or have perceived within the
    past day. You might be able to persuade a beast to perform a small
    favor for you, at the GM's discretion.
    
    """
    level = 1
    name = "Speak with Animals"
    casting_time = "1 action"
    casting_range = "Self"
    components = ("V", "S")
    duration = "10 minutes"
    ritual = True
    magic_school = "Divination"
    classes = ('Bard', 'Druid', 'Ranger')


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


class UnseenServant(Spell):
    """This spell creates an invisible, mindless, shapeless force that performs
    simple tasks at your command until the spell ends. The servant springs into
    existence in an unoccupied space on the ground within range. It has AC 10,
    1 hit point, and a Strength of 2, and it can’t attack. If it drops to 0 hit
    points, the spell ends.  Once on each of your turns as a bonus action, you
    can mentally command the servant to move up to 15 feet and inteact with an
    object. The servant can perform simple tasks that a human servant could do,
    such as fetching things, cleaning, mending, folding clothes, lighting
    fires, serving food, and pouring wine. Once you give the command, the
    servant performs the task to the best of its ability until it completes the
    task, then waits for your next command.  If you command the servant to
    perform a task that would move it more than 60 feet away from you, the
    spell ends.

    """
    name = "Unseen Servant"
    level = 1
    casting_time = '1 action'
    components = ('V', 'S', 'M')
    materials = 'a piece of string and a bit of wood'
    duration = '1 hour'
    casting_rage = '60 feet'
    magic_school = 'Conjuration'
    ritual = True
    classes = ('Bard', 'Warlock', 'Wizard')
    
