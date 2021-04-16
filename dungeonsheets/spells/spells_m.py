from dungeonsheets.spells.spells import Spell


class MaddeningDarkness(Spell):
    """Magical darkness spreads from a point you choose within range to fill a
    60-foot-radius sphere until the spell ends. The darkness spreads around corners.
    A creature with darkvision can't see through this darkness. Nonmagical light,
    as well as light created by spells of 8th level or lower, can't illuminate the
    area. Shrieks, gibbering, and mad laughter can be heard within the sphere.
    Whenever a creature starts its turn in the sphere, it must make a Wisdom saving
    throw, taking 8d8 psychic damage on a failed save, or half as much damage on a
    successful one.
    """

    name = "Maddening Darkness"
    level = 8
    casting_time = "1 action"
    casting_range = "150 feet"
    components = ("V", "M")
    materials = "A drop of pitch mixed with a drop of mercury"
    duration = "Concentration, up to 10 minutes"
    ritual = False
    magic_school = "Evocation"
    classes = ("Warlock", "Wizard")


class Maelstrom(Spell):
    """(paper or leaf in the shape of a funnel)
    A mass of 5-foot-deep water appears and
    swirls in a 30-foot radius centered on a point you can see within range. The
    point must be on ground or in a body of water. Until the spell ends, that area
    is difficult terrain, and any creature that starts its turn there must succeed
    on a Strength saving throw or take 6d6 bludgeoning damage and be pulled 10 feet
    toward the center.
    """

    name = "Maelstrom"
    level = 5
    casting_time = "1 action"
    casting_range = "120 feet"
    components = ("V", "S", "M")
    materials = ""
    duration = "Concentration, up to 1 minute"
    ritual = False
    magic_school = "Evocation"
    classes = ("Druid",)


class MageArmor(Spell):
    """You touch a willing creature who isn't wearing armor, and a protective magical
    force surrounds it until the spell ends. The target's base AC becomes 13 + its
    Dexterity modifier. The spell ends it if the target dons armor or if you dismiss
    the spell as an action.
    """

    name = "Mage Armor"
    level = 1
    casting_time = "1 action"
    casting_range = "Touch"
    components = ("V", "S", "M")
    materials = "A piece of cured leather"
    duration = "8 hours"
    ritual = False
    magic_school = "Abjuration"
    classes = ("Sorcerer", "Wizard")


class MageHand(Spell):
    """A spectral, floating hand appears at a point you choose within range.
    The hand
    lasts for the duration or until you dismiss it as an action. The hand vanishes
    if it is ever more than 30 feet away from you or if you cast this spell again.


    You can use your action to control the hand. You can use the hand to manipulate
    an object, open an unlocked door or container, stow or retrieve an item from an
    open container, or pour the contents out of a vial. You can move the hand up to
    30 feet each time you use it.

    The hand can't attack, activate magical items, or
    carry more than 10 pounds.
    """

    name = "Mage Hand"
    level = 0
    casting_time = "1 action"
    casting_range = "30 feet"
    components = ("V", "S")
    materials = ""
    duration = "1 minute"
    ritual = False
    magic_school = "Conjuration"
    classes = ("Bard", "Sorcerer", "Warlock", "Wizard")


class MagicCircle(Spell):
    """You create a 10-foot-radius, 20-foot-tall cylinder of magical energy centered on
    a point on the ground that you can see within range. Glowing runes appear
    wherever the cylinder intersects with the floor or other surface.

    Choose one or more of the following types of creatures:
    celestials, elementals, fey, fiends, or undead. The circle affects
    a creature of the chosen type in the following ways:

    - The creature can't willingly enter the cylinder by nonmagical
      means. If the creature tries to use teleportation or interplanar
      travel to do so, it must first succeed on a Charisma saving
      throw.
    - The creature has disadvantage on attack rolls against targets
      within the cylinder.
    - Targets within the cylinder can't be charmed, frightened, or
      possessed by the creature.

    When you cast this spell, you can elect to cause its magic to
    operate in the reverse direction, preventing a creature of the
    specified type from leaving the cylinder and protecting targets
    outside it.

    **At Higher Levels:** When you cast this spell using a spell slot
    of 4th level or higher, the duration increases by 1 hour for each
    slot level above 3rd.

    """

    name = "Magic Circle"
    level = 3
    casting_time = "1 minute"
    casting_range = "10 feet"
    components = ("V", "S", "M")
    materials = (
        "Holy water or powdered silver and iron worth at least 100 gp, which the spell"
        " consumes"
    )
    duration = "1 hour"
    ritual = False
    magic_school = "Abjuration"
    classes = ("Cleric", "Paladin", "Warlock", "Wizard")


class MagicJar(Spell):
    """Your body falls into a catatonic state as your soul leaves it and enters the
    container you used for the spell's material component. While your soul inhabits
    the container, you are aware of your surroundings as if you were in the
    container's space. You can't move or use reactions. The only action you can take
    is to project your soul up to 100 feet out of the container, either returning
    to your living body (and ending the spell) or attempting to possess a humanoids
    body.

    You can attempt to possess any humanoid within 100 feet of you that you
    can see (creatures warded by a protection from evil and good or magic circle
    spells can't be possessed). The target must make a Charisma saving throw. On a
    failure, your soul moves into the target's body, and the target's soul becomes
    trapped in the container. On a success, the target resists your efforts to
    possess it, and you can't attempt to possess it again for 24 hours.

    Once you
    possess a creature's body, you control it. Your game statistics are replaced by
    the statistics of the creature though you retain your alignment and your
    Intelligence, Wisom, and Charisma scores. You retain the benefit of your own
    class feature. If the target has any class levels, you can't use any of its
    class features.

    Meanwhile, the possessed creature's soul can perceive from the
    container using its own senses, but it can't move or take actions at all.

    While
    possessing a body, you can use your action to return from the host body to the
    container if it is within 100 feet of you, returning the host creature's soul to
    its body. If the host body dies while you're in it, the creature dies, and you
    must make a Charisma saving throw against your own spellcasting DC. On a
    success, you return to the container if it is within 100 feet of you. Otherwise,
    you die.

    If the container is destroyed or the spell ends, your soul
    immediately returns to your body. If your body is more than 100 feet away from
    you, or if your body is dead when you attempt to return to it, you die. If
    another creature's soul is in the container when it is destroyed, the creature's
    soul returns to its body if the body is alive and within 100 feet. Otherwise,
    that creature dies.

    When the spell ends, the container is destroyed.
    """

    name = "Magic Jar"
    level = 6
    casting_time = "1 minute"
    casting_range = "Self"
    components = ("V", "S", "M")
    materials = (
        "A gem, crystal, reliquary, or some other ornamental container worth at least"
        " 500 gp"
    )
    duration = "Until dispelled"
    ritual = False
    magic_school = "Necromancy"
    classes = ("Wizard",)


class MagicMissile(Spell):
    """You create three glowing darts of magical force. Each dart hits a
    creature of your choice that you can see within range. A dart
    deals 1d4 + 1 force damage to its target. The darts all strike
    simultaneously and you can direct them to hit one creature or
    several.

    **At Higher Levels:** When you cast this spell using a spell slot of
    2nd level or higher, the spell creates one more dart for each slot
    level above 1st.

    """

    name = "Magic Missile"
    level = 1
    casting_time = "1 action"
    casting_range = "120 feet"
    components = ("V", "S")
    materials = ""
    duration = "Instantaneous"
    ritual = False
    magic_school = "Evocation"
    classes = ("Sorcerer", "Wizard")


class MagicMouth(Spell):
    """You implant a message within an object in range, a message that is uttered when
    a trigger condition is met.
    Choose an object that you can see and that isn't
    being worn or carried by another creature. Then speak the message, which must be
    25 words or less, though it can be delivered over as long as 10 minutes.
    Finally, determine the circumstance that will trigger the spell to deliver your
    message.

    When that circumstance occurs, a magical mouth appears on the object
    and recites the message in your voice and at the same volume you spoke. If the
    object you chose has a mouth or something that looks like a mouth (for example,
    the mouth of a statue), the magical mouth appears there so that words appear to
    come from the object's mouth. When you cast this spell, you can have the spell
    end after it delivers its message, or it can remain and repeats its message
    whenever the trigger occurs.

    The triggering circumstance can be as general or
    as detailed as you like, though it must be based on visual or audible conditions
    that occur within 30 feet of the object. For example, you could instruct the
    mouth to speak when any creature moves within 30 feet of the object or when a
    silver bell rings within 30 feet of it.
    """

    name = "Magic Mouth"
    level = 2
    casting_time = "1 minute"
    casting_range = "30 feet"
    components = ("V", "S", "M")
    materials = (
        "A small bit of honeycomb and jade dust worth at least 10 gp, which the spell"
        " consumes"
    )
    duration = "Until dispelled"
    ritual = True
    magic_school = "Illusion"
    classes = ("Bard", "Wizard")


class MagicStone(Spell):
    """You touch one to three pebbles and imbue them with magic. You or someone else
    can make a ranged spell attack with one of the pebbles by throwing it or hurling
    it with a sling. If thrown, a pebble has a range of 60 feet. If someone else
    attacks with a pebble, that attacker adds your spellcasting ability modifier,
    not the attacker's, to the attack roll. On a hit, the target takes bludgeoning
    damage equal to 1d6 + your spellcasting ability modifier. Whether the attack
    hits or misses, the spell then ends on the stone.
    If you cast this spell again,
    the spell ends on any pebbles still affected by your previous casting.
    """

    name = "Magic Stone"
    level = 0
    casting_time = "1 bonus action"
    casting_range = "Touch"
    components = ("V", "S")
    materials = ""
    duration = "1 minute"
    ritual = False
    magic_school = "Transmutation"
    classes = ("Druid", "Warlock")


class MagicWeapon(Spell):
    """You touch a nonmagical weapon. Until the spell ends, that weapon becomes a magic
    weapon with a +1 bonus to attack rolls and damage rolls.

    At Higher Levels:
    When you cast this spell using a spell slot of 4th level or higher, the bonus
    increases to +2.
    When you use a spell slot of 6th level or higher, the bonus
    increases to +3.
    """

    name = "Magic Weapon"
    level = 2
    casting_time = "1 bonus action"
    casting_range = "Touch"
    components = ("V", "S")
    materials = ""
    duration = "Concentration, up to 1 hour"
    ritual = False
    magic_school = "Transmutation"
    classes = ("Paladin", "Wizard")


class MajorImage(Spell):
    """You create the image of an object, a creature, or some other visible phenomenon
    that is no larger than a 20-foot cube.
    The image appears at a spot that you can
    see within range and lasts for the duration. It seems completely real, including
    sounds, smells, and temperature appropriate to the thing depicted. You can't
    create sufficient heat or cold to cause damage, a sound loud enough to deal
    thunder damage or deafen a creature, or a smell that might sicken a creature
    (like a troglodyte's stench).

    As long as you are within range of the illusion,
    you can use your action to cause the image to move to any other spot within
    range. As the image changes location, you can alter its appearance so that its
    movements appear natural for the image. For example, if you create an image of a
    creature and move it, you can alter the image so that it appears to be walking.
    Similarly, you can cause the illusion to make different sounds at different
    times, even making it carry on a conversation, for example.

    Physical
    interaction with the image reveals it to be an illusion, because things can pass
    through it. A creature that uses its action to examine the image can determine
    that it is an illusion with a successful Intelligence (Investigation) check
    against your spell save DC. If a creature discerns the illusion for what it is,
    the creature can see through the image, and its other sensory qualities become
    faint to the creature.

    **At Higher Levels:** When you cast this spell using a spell
    slot of 6th level or higher, the spell lasts until dispelled, without requiring
    your concentration.
    """

    name = "Major Image"
    level = 3
    casting_time = "1 action"
    casting_range = "120 feet"
    components = ("V", "S", "M")
    materials = "A bit of fleece"
    duration = "Concentration, up to 10 minutes"
    ritual = False
    magic_school = "Illusion"
    classes = ("Bard", "Sorcerer", "Warlock", "Wizard")


class MassCureWounds(Spell):
    """A wave of healing energy washes out from a point of your choice within range.

    Choose up to six creatures in a 30-foot-radius sphere centered on that point.
    Each target regains hit points equal to 3d8 + your spellcasting ability
    modifier. This spell has no effect on undead or constructs.

    At Higher Levels:
    When you cast this spell using a spell slot of 6th level or higher, the healing
    increases by 1d8 for each slot level above 5th.
    """

    name = "Mass Cure Wounds"
    level = 5
    casting_time = "1 action"
    casting_range = "60 feet"
    components = ("V", "S")
    materials = ""
    duration = "Instantaneous"
    ritual = False
    magic_school = "Evocation"
    classes = ("Bard", "Cleric", "Druid")


class MassHeal(Spell):
    """A flood of healing energy flows from you into injured creatures around you. You
    restore up to 700 hit points, divided as you choose among any number of
    creatures that you can see within range. Creatures healed by this spell are also
    cured of all diseases and any effect making them blinded or deafened. This
    spell has no effect on undead or constructs.
    """

    name = "Mass Heal"
    level = 9
    casting_time = "1 action"
    casting_range = "60 feet"
    components = ("V", "S")
    materials = ""
    duration = "Instantaneous"
    ritual = False
    magic_school = "Evocation"
    classes = ("Cleric",)


class MassHealingWord(Spell):
    """As you call out words of restoration, up to six creatures of your choice that
    you can see within range regain hit points equal to 1d4 + your spellcasting
    ability modifier. This spell has no effect on undead or constructs.

    At Higher
    Levels: When you cast this spell using a spell slot of 4th level or higher, the
    healing increases by 1d4 for each slot level above 3rd.
    """

    name = "Mass Healing Word"
    level = 3
    casting_time = "1 bonus action"
    casting_range = "60 feet"
    components = ("V",)
    materials = ""
    duration = "Instantaneous"
    ritual = False
    magic_school = "Evocation"
    classes = ("Cleric",)


class MassPolymorph(Spell):
    """You transform up to ten creatures of your choice that you can see within range.
    An unwilling target must succeed on a Wisdom saving throw to resist the
    transformation. An unwilling shapechanger automatically succeeds on the save.

    Each target assumes a beast form of your choice, and you can choose the same
    form or different ones for each target. The new form can be any beast you have
    seen whose challenge rating is equal to or less than the target's (or half the
    target's level, if the target doesn't have a challenge rating). The target's
    game statistics, including mental ability scores, are replaced by the statistics
    of the chosen beast, but the target retains its hit points, alignment, and
    personality.
    Each target gains a number of temporary hit points equal to the hit
    points of its new form. These temporary hit points can't be replaced by
    temporary hit points from another source. A target reverts to its normal form
    when it has no more temporary hit points or it dies. If the spell ends before
    then, the creature loses all its temporary hit points and reverts to its normal
    form.
    The creature is limited in the actions it can perform by the nature of its
    new form. It can't speak, cast spells, or do anything else that requires hands
    or speech. The target's gear melds into the new form.
    The target can't activate,
    use, wield, or otherwise benefit from any of its equipment.
    """

    name = "Mass Polymorph"
    level = 9
    casting_time = "1 action"
    casting_range = "120 feet"
    components = ("V.S", "M")
    materials = "A caterpillar cocoon"
    duration = "Concentration, up to 1 hour"
    ritual = False
    magic_school = "Transmutation"
    classes = ("Sorcerer", "Wizard", "Bard")


class MassSuggestion(Spell):
    """You suggest a course of activity (limited to a sentence or two) and magically
    influence up to twelve creatures of your choice that you can see within range
    and that can hear and understand you.
    Creatures that can't be charmed are immune
    to this effect. The suggestion must be worded in such a manner as to make the
    course of action sound reasonable. Asking the creature to stab itself, throw
    itself onto a spear, immolate itself, or do some other obviously harmful act
    automatically negates the effect of the spell.

    Each target must make a Wisdom
    saving throw. On a failed save, it pursues the course of action you described to
    the best of its ability. The suggested course of action can continue for the
    entire duration. If the suggested activity can be completed in a shorter time,
    the spell ends when the subject finishes what it was asked to do.

    You can also
    specify conditions that will trigger a special activity during the duration. For
    example, you might suggest that a group of soldiers give all their money to the
    first beggar they meet. If the condition isn't met before the spell ends, the
    activity isn't performed.

    If you or any of your companions damage a creature
    affected by this spell, the spell ends for that creature.

    At Higher Levels:
    When you cast this spell using a 7th-level spell slot, the duration is 10 days.

    When you use an 8th-level spell slot, the duration is 30 days.
    When you use a
    9th-level spell slot, the duration is a year and a day.
    """

    name = "Mass Suggestion"
    level = 6
    casting_time = "1 action"
    casting_range = "60 feet"
    components = ("V", "M")
    materials = (
        """A snake's tongue and either a bit of honeycomb or a drop of sweet oil"""
    )
    duration = "24 hours"
    ritual = False
    magic_school = "Enchantment"
    classes = ("Bard", "Sorcerer", "Warlock", "Wizard")


class MaximiliansEarthenGrasp(Spell):
    """You choose a 5-foot-square unoccupied space on the ground that you can see
    within range. A Medium hand made from compacted soil rises there and reaches
    for
    one creature you can see within 5 feet of it. The target must make a Strength
    saving throw. On a failed save, the target takes 2d6 bludgeoning damage and is
    restrained for the spell's duration.
    As an action, you can cause the hand to
    crush the restrained target, who must make a Strength saving throw. It takes 2d6
    bludgeoning damage on a failed save, or half as much damage on a successful
    one.
    To break out, the restrained target can make a Strength check against your
    spell save DC. On a success, the target escapes and is no longer restrained by
    the hand.
    As an action, you can cause the hand to reach for a different creature
    or to move to a different unoccupied space within range. The hand releases a
    restrained target if you do either.
    """

    name = "Maximilians Earthen Grasp"
    level = 2
    casting_time = "1 action"
    casting_range = "30 feet"
    components = ("V", "S", "M")
    materials = "A miniature hand sculpted from clay"
    duration = "Concentration, up to 1 minute"
    ritual = False
    magic_school = "Transmutation"
    classes = ("Sorcerer", "Wizard")


class Maze(Spell):
    """You banish a creature that you can see within range into a labyrinthine
    demiplane. The target remains there for the duration or until it escapes the
    maze.

    The target can use its action to attempt to escape. When it does so, it
    makes a DC 20 Intelligence check. If it succeeds, it escapes, and the spell ends
    (a minotaur or goristro demon automatically succeeds).

    When the spell ends,
    the target reappears in the space it left or, if that space is occupied, in the
    nearest unoccupied space.
    """

    name = "Maze"
    level = 8
    casting_time = "1 action"
    casting_range = "60 feet"
    components = ("V", "S")
    materials = ""
    duration = "Concentration, up to 10 minutes"
    ritual = False
    magic_school = "Conjuration"
    classes = ("Wizard",)


class MeldIntoStone(Spell):
    """You step into a stone object or surface large enough to fully contain your body,
    melding yourself and all the equipment you carry with the stone for the
    duration.
    Using your movement, you step into the stone at a point you can touch.
    Nothing of your presence remains visible or otherwise detectable by nonmagical
    senses.

    While merged with the stone, you can't see what occurs outside it, and
    any Wisdom (Perception) checks you make to hear sounds outside it are made with
    disadvantage. You remain aware of the passage of time and can cast spells on
    yourself while merged in the stone. You can use your movement to leave the stone
    where you entered it, which ends the spell. You otherwise can't move.

    Minor
    physical damage to the stone doesn't harm you, but its partial destruction or a
    change in its shape (to the extent that you no longer fit within it) expels you
    and deals 6d6 bludgeoning damage to you. The stone's complete destruction (or
    transmutation into a different substance) expels you and deals 50 bludgeoning
    damage to you. If expelled, you fall prone in an unoccupied space closest to
    where you first entered.
    """

    name = "Meld Into Stone"
    level = 3
    casting_time = "1 action"
    casting_range = "Touch"
    components = ("V", "S")
    materials = ""
    duration = "8 hours"
    ritual = True
    magic_school = "Transmutation"
    classes = ("Cleric", "Druid")


class MelfsAcidArrow(Spell):
    """A shimmering green arrow streaks toward a target within range and bursts in a
    spray of acid.
    Make a ranged spell attack against the target. On a hit, the
    target takes 4d4 acid damage immediately and 2d4 acid damage at the end of its
    next turn. On a miss, the arrow splashes the target with acid for half as much
    of the initial damage and no damage at the end of its next turn.

    At Higher
    Levels: When you cast this spell using a spell slot of 3rd level or higher, the
    damage (both initial and later) increases by 1d4 for each slot level above 2nd.
    """

    name = "Melfs Acid Arrow"
    level = 2
    casting_time = "1 action"
    casting_range = "90 feet"
    components = ("V", "S", "M")
    materials = "Powdered rhubarb leaf and an adder's stomach"
    duration = "Instantaneous"
    ritual = False
    magic_school = "Evocation"
    classes = ("Wizard",)


class MelfsMinuteMeteors(Spell):
    """(niter, sulfur, and pine tar formed into a bead)
    You create six tiny meteors in
    your space. They float in the air and orbit you for the spell's duration. When
    you cast the spell-and as a bonus action on each of your turns thereafter-you
    can expend one or two of the meteors, sending them streaking toward a point or
    points you choose within 120 feet of you. Once a meteor reaches its destination
    or impacts against a solid surface, the meteor explodes. Each creature within 5
    feet of the point where the meteor explodes must make a Dexterity saving throw.
    A creature takes 2d6 fire damage on a failed save, or half as much damage on a
    successful one.
    At Higher Levels. When you cast this spell using a spell slot of
    4th level or higher, the number of meteors created increases by two for each
    slot level above 3rd.
    """

    name = "Melfs Minute Meteors"
    level = 3
    casting_time = "1 action"
    casting_range = "Self"
    components = ("V", "S", "M")
    materials = ""
    duration = "Concentration, up to 10 minutes"
    ritual = False
    magic_school = "Evocation"
    classes = ("Sorcerer", "Wizard")


class Mending(Spell):
    """This spell repairs a single break or tear in an object you touch, such as broken
    chain link, two halves of a broken key, a torn cloack, or a leaking wineskin.

    As long as the break or tear is no larger than 1 foot in any dimension, you mend
    it, leaving no trace of the former damage.

    This spell can physically repair a
    magic item or construct, but the spell can't restore magic to such an object.
    """

    name = "Mending"
    level = 0
    casting_time = "1 minute"
    casting_range = "Touch"
    components = ("V", "S", "M")
    materials = "Two lodestones"
    duration = "Instantaneous"
    ritual = False
    magic_school = "Transmutation"
    classes = ("Bard", "Cleric", "Druid", "Sorcerer", "Wizard")


class MentalPrison(Spell):
    """You attempt to bind a creature within an illusory cell that only it perceives.
    One creature you can see within range must make an Intelligence saving throw.
    The target succeeds automatically if it is immune to being charmed. On a
    successful save, the target takes 5d10 psychic damage, and the spell ends. On a
    failed save, the target takes 5d10 psychic damage, and you make the area
    immediately around the target's space appear dangerous to it in some way. You
    might cause the target to perceive itself as being surrounded by fire, floating
    razors, or hideous maws filled with dripping teeth. Whatever form the illusion
    takes, the target can't see or hear anything beyond it and is restrained for the
    spell's duration. If the target is moved out of the illusion, makes a melee
    attack through it, or reaches any part of its body through it, the target takes
    10d10 psychic damage, and the spell ends.
    """

    name = "Mental Prison"
    level = 6
    casting_time = "1 action"
    casting_range = "60 feet"
    components = ("S",)
    materials = ""
    duration = "Concentration, up to 1 minute"
    ritual = False
    magic_school = "Illusion"
    classes = ("Sorcerer", "Warlock", "Wizard")


class Message(Spell):
    """You point your finger toward a creature within range and whisper a message.
    The
    target (and only the target) hears the message and can reply in a whisper that
    only you can hear.

    You can cast this spell through solid objects if you are
    familiar with the target and know it is beyond the barrier. Magical silence, 1
    foot of stone, 1 inch of common metal, a thin sheet of lead, or 3 feet of wood
    blocks the spell. The spell doesn't have to follow a straight line and can
    travel freely around corners or through openings.
    """

    name = "Message"
    level = 0
    casting_time = "1 action"
    casting_range = "120 feet"
    components = ("V", "S", "M")
    materials = "A short piece of copper wire"
    duration = "1 round"
    ritual = False
    magic_school = "Transmutation"
    classes = ("Bard", "Sorcerer", "Wizard")


class MeteorSwarm(Spell):
    """Blazing orbs of fire plummet to the ground at four different points you can see
    within range.
    Each creature in a 40-foot-radius sphere centered on each point
    you choose must make a Dexterity saving throw. The sphere spreads around
    corners. A creature takes 20d6 fire damage and 20d6 bludgeoning damage on a
    failed save, or half as much damage on a sucessful one. A creature in the area
    of more than one fiery burst is affected only once.

    The spell damages objects
    in the area and ignites flammable objects that aren't being worn or carried.
    """

    name = "Meteor Swarm"
    level = 9
    casting_time = "1 action"
    casting_range = "1 mile"
    components = ("V", "S")
    materials = ""
    duration = "Instantaneous"
    ritual = False
    magic_school = "Evocation"
    classes = ("Sorcerer", "Wizard")


class MightyFortress(Spell):
    """A fortress of stone erupts from a square area of ground of your choice that you
    can see within range. The area is 120 feet on each side, and it must not have
    any buildings or other structures on it. Any creatures in the area are
    harmlessly lifted up as the fortress rises.
    The fortress has four turrets with
    square bases, each one 20 feet on a side and 30 feet tall, with one turret on
    each corner. The turrets are connected to each other by stone walls that are
    each 80 feet long, creating an enclosed area. Each wall is 1 foot thick and is
    composed of panels that are 10 feet wide and 20 feet tall. Each panel is
    contiguous with two other panels or one other panel and a turret. You can place
    up to four stone doors in the fortress's outer wall.
    A small keep stands inside
    the enclosed area. The keep has a square base that is 50 feet on each side, and
    it has three floors with 10-foot-high ceilings. Each of the floors can be
    divided into as many rooms as you like, provided each room is at least 5 feet on
    each side. The floors of the keep are connected by stone staircases, its walls
    are 6 inches thick, and interior rooms can have stone doors or open archways as
    you choose. The keep is furnished and decorated however you like, and it
    contains sufficient food to serve a nine-course banquet for up to 100 people
    each day. Furnishings, food, and other objects created by this spell crumble to
    dust if removed from the fortress.
    A staff of one hundred invisible servants
    obeys anycommand given to them by creatures you designate when you cast the
    spell. Each servant functions as if created by the unseen servant spell.
    The
    walls, turrets, and keep are all made of stone that can be damaged. Each
    10-foot-bya10-foot section of stone has AC 15 and 30 hit points per inch of
    thickness. It is immune to poison and psychic damage. Reducing a section of
    stone to 0 hit points destroys it and might cause connected sections to buckle
    and collapse at the DM's discretion.
    After 7 days or when you cast this spell
    somewhere else, the fortress harmlessly crumbles and sinks back into the ground,
    leaving any creatures that were inside it safely on the ground.
    Casting this
    spell on the same spot once every 7 days for a year makes the fortress
    permanent.
    """

    name = "Mighty Fortress"
    level = 8
    casting_time = "1 minute"
    casting_range = "1 mile"
    components = ("V", "S", "M")
    materials = "A diamond worth at least 500 gp, which the spell consumes"
    duration = "Instantaneous"
    ritual = False
    magic_school = "Conjuration"
    classes = ("Wizard",)


class MindBlank(Spell):
    """Until the spell ends, one willing creature you touch is immune to psychic
    damage, any effect that would sense its emotions or read its thoughts,
    divination spells, and the charmed condition. The spell even foils wish spells
    and spells or effects of similar power used to affect the target's mind or to
    gain information about the target.
    """

    name = "Mind Blank"
    level = 8
    casting_time = "1 action"
    casting_range = "Touch"
    components = ("V", "S")
    materials = ""
    duration = "24 hours"
    ritual = False
    magic_school = "Abjuration"
    classes = ("Bard", "Wizard")


class MindSliver(Spell):
    """You drive a disorienting spike of psychic energy into the mind of one
    creature you can see within range. The target must succeed on
    an Intelligence saving throw or take 1d6 psychic damage and subtract 1d4
    from the next saving throw it makes before the end of your next turn.

    **At Higher Levels:** This spell’s damage increases by 1d6 when you reach
    certain levels: 5th level (2d6), 11th level (3d6), and 17th level (4d6).
    """

    name = "Mind Sliver"
    level = 0
    casting_time = "1 action"
    casting_range = "60 feet"
    components = ("V",)
    materials = ""
    duration = "1 round"
    ritual = False
    magic_school = "Enchantment"
    classes = ("Sorcerer", "Warlock", "Wizard")


class MindSpike(Spell):
    """You reach into the mind of one creature you can see within range. The target
    must make a Wisdom saving throw, taking 3d8 psychic damage on a failed save, or
    half as much damage on a successful one. On a failed save, you also always know
    the target's location until the spell ends, but only while the two of you are on
    the same plane of existence. While you have this knowledge, the target can't
    become hidden from you, and if it's invisible, it gains no benefit from that
    condition against you.

    **At Higher Levels:** When you cast this spell using a spell
    slot of 3rd level or higher, the damage increases by 1d8 for each slot level
    above 2nd.
    """

    name = "Mind Spike"
    level = 2
    casting_time = "1 action"
    casting_range = "60 feet"
    components = ("S",)
    materials = ""
    duration = "Concentration, up to 1 hour"
    ritual = False
    magic_school = "Divination"
    classes = ("Sorcerer", "Warlock", "Wizard")


class MinorIllusion(Spell):
    """You create a sound or an image of an object within range that lasts for the
    duration. The illusion also ends if you dismiss it as an action or cast this
    spell again.

    If you create a sound, its volume can range from a whisper to a
    scream. It can be your voice, someone else's voice, a lion's roar, a beating of
    drums, or any other sound you choose. The sound continues unabated throughout
    the duration, or you can make discrete sounds at different times before the
    spell ends.

    If you create an image of an object such as a chair, muddy
    footprints, or a small chest it must be no larger than a 5-foot cube. The image
    can't create sound, light, smell, or any other sensory effect. Physical
    interaction with the image reveals it to be an illusion, because things can pass
    through it.

    If a creature uses its action to examine the sound or image, the
    creature can determine that it is an illusion with a successful Intelligence
    (Investigation) check against your spell save DC. If a creature discerns the
    illusion for what it is, the illusion becomes faint to the creature.
    """

    name = "Minor Illusion"
    level = 0
    casting_time = "1 action"
    casting_range = "30 feet"
    components = ("S", "M")
    materials = "A bit of fleece"
    duration = "1 minute"
    ritual = False
    magic_school = "Illusion"
    classes = ("Bard", "Sorcerer", "Warlock", "Wizard")


class MirageArcane(Spell):
    """You make terrain in an area up to 1 mile square look, sound, smell, and even
    feel like some other sort of terrain.
    The terrain's general shape remains the
    same, however. Open fields or a road could be made to resemble a swamp, hill,
    crevasse, or some other difficult or impassable terrain. A pond can be made to
    seem like a grassy meadow, a precipice like a gentle slope, or a rock-strewn
    gully like a wide and smooth road.

    Similarly, you can alter the appearance of
    structures, or add them where none are present. The spell doesn't disguise,
    conceal, or add creatures.

    The illusion includes audible, visual, tactile, and
    olfactory elements, so it can turn clear ground into difficult terrain (or vice
    versa) or otherwise impede movement through the area. Any piece of the illusory
    terrain (such as a rock or stick) that is removed from the spell's area
    disappears immediately.

    Creatures with truesight can see through the illusion
    to the terrain's true form however, all other elements of the illusion remain,
    so while the creature is aware of the illusion's presence, the creature can
    still physically interact with the illusion.
    """

    name = "Mirage Arcane"
    level = 7
    casting_time = "10 minutes"
    casting_range = "Sight"
    components = ("V", "S")
    materials = ""
    duration = "10 days"
    ritual = False
    magic_school = "Illusion"
    classes = ("Bard", "Druid", "Wizard")


class MirrorImage(Spell):
    """Three illusory duplicates of yourself appear in your space.
    Until the spell
    ends, the duplicates move with you and mimic your actions, shifting position so
    it's impossible to track which image is real. You can use your action to dismiss
    the illusory duplicates.

    Each time a creature targets you with an attack
    during the spell's duration, roll a d20 to determine whether the attack instead
    targets one of your duplicates.

    If you have three duplicates, you must roll a 6
    or higher to change the attack's target to a duplicate. With two duplicates,
    you must roll an 8 or higher. With one duplicate, you must roll an 11 or higher.


    A duplicate's AC equals 10 + your Dexterity modifier. If an attack hits a
    duplicate, the duplicate is destroyed. A duplicate can be destroyed only by an
    attack that hits it. It ignores all other damage and effects. The spell ends
    when all three duplicates are destroyed.

    A creature is unaffected by this spell
    if it can't see, if it relies on senses other than sight, such as blindsight,
    or if it can perceive illusions as false, as with truesight.
    """

    name = "Mirror Image"
    level = 2
    casting_time = "1 action"
    casting_range = "Self"
    components = ("V", "S")
    materials = ""
    duration = "1 minute"
    ritual = False
    magic_school = "Illusion"
    classes = ("Sorcerer", "Warlock", "Wizard")


class Mislead(Spell):
    """You become invisible at the same time that an illusory double of you appears
    where you are standing. The double lasts for the duration, but the invisibility
    ends if you attack or cast a spell.

    You can use your action to move your
    illusory double up to twice your speed and make it gesture, speak, and behave in
    whatever way you choose.

    You can see through its eyes and hear through its
    ears as if you were located where it is. On each of your turns as a bonus
    action, you can switch from using its senses to using your own, or back again.
    While you are using its senses, you are blinded and deafened in regard to your
    own surroundings.
    """

    name = "Mislead"
    level = 5
    casting_time = "1 action"
    casting_range = "Self"
    components = ("S",)
    materials = ""
    duration = "Concentration, up to 1 hour"
    ritual = False
    magic_school = "Illusion"
    classes = ("Bard", "Wizard")


class MistyStep(Spell):
    """Briefly surrounded by silvery mist, you teleport up to 30 feet to an unoccupied
    space that you can see.
    """

    name = "Misty Step"
    level = 2
    casting_time = "1 bonus action"
    casting_range = "Self"
    components = ("V",)
    materials = ""
    duration = "Instantaneous"
    ritual = False
    magic_school = "Conjuration"
    classes = ("Sorcerer", "Warlock", "Wizard")


class ModifyMemory(Spell):
    """You attempt to reshape another creature's memories.
    One creature that you can
    see must make a Wisdom saving throw. If you are fighting the creature, it has
    advantage on the saving throw. On a failed save, the target becomes charmed by
    you for the duration. The charmed target is incapacitated and unaware of its
    surroundings, though it can still hear you. If it takes any damage or is
    targeted by another spell, this spell ends, and none of the target's memories
    are modified.

    While this charm lasts, you can affect the target's memory of an
    event that it experienced within the last 24 hours and that lasted no more than
    10 minutes. You can permanently eliminate all memory of the event, allow the
    target to recall the event with perfect clarity and exacting detail, change its
    memory of the details of the event, or create a memory of some other event.

    You
    must speak to the target to describe how its memories are affected, and it must
    be able to understand your language for the modified memories to take root. Its
    mind fills in any gaps in the details of your description. If the spell ends
    before you have finished describing the modified memories, the creature's memory
    isn't altered. Otherwise, the modified memories take hold when the spell ends.


    A modified memory doesn't necessarily affect how a creature behaves,
    particularly if the memory contradicts the creature's natural inclinations,
    alignment, or beliefs. An illogical modified memory, such as implanting a memory
    of how much the creature enjoyed dousing itself in acid, is dismissed, perhaps
    as a bad dream. The DM might deem a modified memory too nonsensical to affect a
    creature in a significant manner.

    A remove curse or greater restoration spell
    cast on the target restores the creature's true memory.

    **At Higher Levels:** If
    you cast this spell using a spell slot of 6th level or higher, you can alter the
    target's memories of an event that took place up to 7 days ago (6th level), 30
    days ago (7th level), 1 year ago (8th level), or any time in the creature's past
    (9th level).
    """

    name = "Modify Memory"
    level = 5
    casting_time = "1 action"
    casting_range = "30 feet"
    components = ("V", "S")
    materials = ""
    duration = "Concentration, up to 1 minute"
    ritual = False
    magic_school = "Enchantment"
    classes = ("Bard", "Wizard")


class MoldEarth(Spell):
    """You choose a portion of dirt or stone that you can see within range and that
    fits within a 5-foot cube. You manipulate it in one of the following ways:
    - If
    you target an area of loose earth, you can instantaneously excavate it, move it
    along the ground, and deposit it up to 5 feet away. This movement doesn't have
    enough force to cause damage.
    - You cause shapes, colors, or both to appear on
    the dirt or stone, spelling out words, creating images, or shaping patterns. The
    changes last for 1 hour.
    - If the dirt or stone you target is on the ground,
    you cause it to become difficult terrain. Alternatively, you can cause the
    ground to become normal terrain if it is already difficult terrain. This change
    lasts for 1 hour. If you cast this spell multiple times, you can have no more
    than two of its non-instantaneous effects active at a time, and you can dismiss
    such an effect as an action.
    """

    name = "Mold Earth"
    level = 0
    casting_time = "1 action"
    casting_range = "30 feet"
    components = ("S",)
    materials = ""
    duration = "Instantaneous or 1 hour"
    ritual = False
    magic_school = "Transmutation"
    classes = ("Druid", "Sorcerer", "Wizard")


class Moonbeam(Spell):
    """A silvery beam of pale light shines down in a 5-footradius,
    40-foot-high cylinder centered on a point within range. Until the
    spell ends, dim light fills the cylinder.

    When a creature enters the spell's area for the first time on a
    turn or starts its turn there, it is engulfed in ghostly flames
    that cause searing pain, and it must make a Constitution saving
    throw. It takes 2d10 radiant damage on a failed save, or half as
    much damage on a successful one.

    A shapechanger makes its saving throw with disadvantage. If it
    fails, it also instantly reverts to its original form and can't
    assume a different form until it leaves the spell's light.

    On each of your turns after you cast this spell, you can use an
    action to move the beam 60 feet in any direction.

    **At Higher Levels:** When you cast this spell using aspell slot
    of 3rd level or higher, the damage increases by 1d10 for each slot
    level above 2nd.

    """

    name = "Moonbeam"
    level = 2
    casting_time = "1 action"
    casting_range = "120 feet"
    components = ("V", "S", "M")
    materials = (
        """Several seeds of any moonseed plant and a piece of opalescent feldspar"""
    )
    duration = "Concentration, up to 1 minute"
    ritual = False
    magic_school = "Evocation"
    classes = ("Druid",)


class MordenkainensFaithfulHound(Spell):
    """You conjure a phantom watchdog in an unoccupied space that you can see within
    range, where it remains for the duration, until you dismiss it as an action, or
    until you move more than 100 feet away from it.

    The hound is invisible to all
    creatures except you and can't be harmed. When a Small or larger creature comes
    within 30 feet of it without first speaking the password that you specify when
    you cast this spell, the hound starts barking loudly. The hound sees invisible
    creatures and can see into the Ethereal Plane. It ignores illusions.

    At the
    start of each of your turns, the hound attempts to bite one creature within 5
    feet of it that is hostile to you. The hound's attack bonus is equal to your
    spellcasting ability modifier + your proficiency bonus. On a hit, it deals 4d8
    piercing damage.
    """

    name = "Mordenkainens Faithful Hound"
    level = 4
    casting_time = "1 action"
    casting_range = "30 feet"
    components = ("V", "S", "M")
    materials = "A tiny silver whistle, a piece of bone, and a thread"
    duration = "8 hours"
    ritual = False
    magic_school = "Conjuration"
    classes = ("Wizard",)


class MordenkainensMagnificentMansion(Spell):
    """You conjure an extradimensional dwelling in range that lasts for the duration.

    You choose where its one entrance is located. The entrance shimmers faintly and
    is 5 feet w ide and 10 feet tall. You and any creature you designate when you
    cast the spell can enter the extradimensional dwelling as long as the portal
    remains open. You can open or close the portal if you are within 30 feet of it.
    While closed, the portal is invisible.

    Beyond the portal is a magnificent foyer
    with numerous chambers beyond. The atmosphere is clean, fresh, and warm.

    You
    can create any floor plan you like, but the space can't exceed 50 cubes, each
    cube being 10 feet on each side. The place is furnished and decorated as you
    choose. It contains sufficient food to serve a ninecourse banquet for up to 100
    people. A staff of 100 near-transparent servants attends all who enter. You
    decide the visual appearance of these servants and their attire. They are
    completely obedient to your orders. Each servant can perform any task a normal
    human servant could perform, but they can't attack or take any action that would
    directly harm another creature. Thus the servants can fetch things, clean,
    mend, fold clothes, light fires, serve food, pour wine, and so on. The servants
    can go anywhere in the mansion but can't leave it. Furnishings and other objects
    created by this spell dissipate into smoke if removed from the mansion. When
    the spell ends, any creatures inside the extradimensional space are expelled
    into the open spaces nearest to the entrance.
    """

    name = "Mordenkainens Magnificent Mansion"
    level = 7
    casting_time = "1 minute"
    casting_range = "300 feet"
    components = ("V", "S", "M")
    materials = (
        "A miniature portal carved from ivory, a small piece of polished marble, and a"
        " tiny silver spoon, each item worth at least 5 gp"
    )
    duration = "24 hours"
    ritual = False
    magic_school = "Conjuration"
    classes = ("Bard", "Wizard")


class MordenkainensPrivateSanctum(Spell):
    """You make an area within range magically secure.
    The area is a cube that can be
    as small as 5 feet to as large as 100 feet on each side. The spell lasts for the
    duration or until you use an action to dismiss it.

    When you cast the spell,
    you decide what sort of security the spell provides, choosing any or all of the
    following properties:
    * Sound can't pass through the barrier at the edge of the
    warded area.
    * The barrier of the warded area appears dark and foggy, preventing
    vision (including darkvision) through it.
    * Sensors created by divination
    spells can't appear inside the protected area or pass through the barrier at its
    perimeter.
    * Creatures in the area can't be targeted by divination spells.
    *
    Nothing can teleport into or out of the warded area.
    * Planar travel is blocked
    within the warded area.

    Casting this spell on the same spot every day for a
    year makes this effect permanent.

    **At Higher Levels:** When you cast this spell
    using a spell slot of 5th level or higher, you can increase the size of the cube
    by 100 feet for each slot level beyond 4th. Thus you could protect a cube that
    can be up to 200 feet on one side by using a spell slot o f 5th level.
    """

    name = "Mordenkainens Private Sanctum"
    level = 4
    casting_time = "10 minutes"
    casting_range = "120 feet"
    components = ("V", "S", "M")
    materials = (
        "A thin sheet of lead, a piece of opaque glass, a wad of cotton or cloth, and"
        " powdered chrysolite"
    )
    duration = "24 hours"
    ritual = False
    magic_school = "Abjuration"
    classes = ("Wizard",)


class MordenkainensSword(Spell):
    """You create a sword-shaped plane of force that hovers within range. It lasts for
    the duration.

    When the sword appears, you make a melee spell attack against a
    target of your choice within 5 feet of the sword. On a hit. the target takes
    3d10 force damage. Until the spell ends, you can use a bonus action on each of
    your turns to move the sword up to 20 feet to a spot you can see and repeat this
    attack against the same target or a different one.
    """

    name = "Mordenkainens Sword"
    level = 7
    casting_time = "1 action"
    casting_range = "60 feet"
    components = ("V", "S", "M")
    materials = (
        "A miniature platinum sword with a grip and pommel of copper and zinc, worth"
        " 250 gp"
    )
    duration = "Concentration, up to 1 minute"
    ritual = False
    magic_school = "Evocation"
    classes = ("Bard", "Wizard")


class MoveEarth(Spell):
    """Choose an area of terrain no larger than 40 feet on a side within range. You can
    reshape dirt, sand, or clay in the area in any manner you choose for the
    duration. You can raise or lower the area's elevation, create or fill in a
    trench, erect or flatten a wall, or form a pillar. The extent of any such
    changes can't exceed half the area's largest dimension. So, if you affect a
    40-foot square, you can create a pillar up to 20 feet high, raise or lower the
    square's elevation by up to 20 feet, dig a trench up to 20 feet deep, and so on.
    It takes 10 minutes for these changes to complete.

    At the end of every 10
    minutes you spend concentrating on the spell, you can choose a new area of
    terrain to affect.

    Because the terrain's transformation occurs slowly,
    creatures in the area can't usually be trapped or injured by the ground's
    movement.

    This spell can't manipulate natural stone or stone construction.
    Rocks and structures shift to accommodate the new terrain. If the way you shape
    the terrain would make a structure unstable, it might collapse.

    Similarly, this
    spell doesn't directly affect plant growth. The moved earth carries any plants
    along with it.
    """

    name = "Move Earth"
    level = 6
    casting_time = "1 action"
    casting_range = "120 feet"
    components = ("V", "S", "M")
    materials = (
        "An iron blade and a small bag containing a mixture of soils-clay, loam, and"
        " sand"
    )
    duration = "Concentration, up to 2 hours"
    ritual = False
    magic_school = "Transmutation"
    classes = ("Druid", "Sorcerer", "Wizard")
