from .spells import Spell


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


