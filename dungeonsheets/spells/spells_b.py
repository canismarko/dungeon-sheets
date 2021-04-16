from dungeonsheets.spells.spells import Spell


class Bane(Spell):
    """Up to three creatures of your choice that you can see within range must make
    Charisma saving throws. Whenever a target that fails this saving throw makes an
    attack roll or a saving throw before the spell ends, the target must roll a d4
    and subtract the number rolled from the attack roll or saving throw.

    At Higher
    Levels: When you cast this spell using a spelslot of 2nd level or higher, you
    can target one aditional creature for each slot level above 1st.
    """

    name = "Bane"
    level = 1
    casting_time = "1 action"
    casting_range = "30 feet"
    components = ("V", "S", "M")
    materials = "A drop of blood"
    duration = "Concentration, up to 1 minute"
    ritual = False
    magic_school = "Enchantment"
    classes = ("Bard", "Cleric")


class BanishingSmite(Spell):
    """The next time you hit a creature with a weapon attack before this spell ends,
    your weapon crackles with force, and the attack deals an extra 5d10 force damage
    to the target. Additionally, if this attack reduces the target to 50 hit points
    of fewer, you banish it. If the target is native to a different plane of
    existence than the on you're on, the target disappears, returning to its home
    plane. If the target is native to the plane you're on, the creature vanishes
    into a harmless demiplane. While there, the target is incapacitated. It remains
    there until the spell ends, at which point the target reappears in the space it
    left or in the nearest unoccupied space if that space is occupied.
    """

    name = "Banishing Smite"
    level = 5
    casting_time = "1 bonus action"
    casting_range = "Self"
    components = ("V",)
    materials = ""
    duration = "Concentration, up to 1 minute"
    ritual = False
    magic_school = "Abjuration"
    classes = ("Paladin",)


class Banishment(Spell):
    """You attempt to send one creature that you can see within range to another place
    of existence. The target must succeed on a Charisma saving throw or be banished.


    If the target is native to the plane of existence you're on, you banish the
    target to a harmless demiplane. While there, the target is incapacitated. The
    target remains there until the spell ends, at which point the target reappears
    in the space it left or in the nearest unoccupied space if that space is
    occupied.

    If the target is native to a different plane of existence that the
    one you're on, the target is banished with a faint popping noise, returning to
    its home plane.
    If the spell ends before 1 minute has passed, the target
    reappears in the space it left or in the nearest unoccupied space if that space
    is occupied. Otherwise, the target doesn't return.

    **At Higher Levels:** When you
    cast this spell using a spell slot of 5th level or higher, you can target one
    additional creature for each slot level above 4th.
    """

    name = "Banishment"
    level = 4
    casting_time = "1 action"
    casting_range = "60 feet"
    components = ("V", "S", "M")
    materials = "An item distasteful to the target"
    duration = "Concentration, up to 1 minute"
    ritual = False
    magic_school = "Abjuration"
    classes = ("Cleric", "Paladin", "Sorcerer", "Warlock", "Wizard")


class Barkskin(Spell):
    """You touch a willing creature. Until the spellends, the target's skin has a
    rough, bark-like appearance, and the target's AC can't be less than 16,
    regardless of what kind of armor it is wearing.
    """

    name = "Barkskin"
    level = 2
    casting_time = "1 action"
    casting_range = "Touch"
    components = ("V", "S", "M")
    materials = "A handful of oak bark"
    duration = "Concentration, up to 1 hour"
    ritual = False
    magic_school = "Transmutation"
    classes = ("Druid", "Ranger")


class BeaconOfHope(Spell):
    """This spell bestows hope and vitality. Choose any number of creatures within
    range. For the duration, each target has advantage on Wisdom saving throws and
    death saving throws, and regains the maximum number of hit points possible from
    any healing.
    """

    name = "Beacon Of Hope"
    level = 3
    casting_time = "1 action"
    casting_range = "30 feet"
    components = ("V", "S")
    materials = ""
    duration = "Concentration, up to 1 minute"
    ritual = False
    magic_school = "Abjuration"
    classes = ("Cleric",)


class BeastBond(Spell):
    """You establish a telepathic link with one beast you touch that is
    friendly to you or charmed by you. The spell fails if the beast's
    Intelligence is 4 or higher.  Until the spell ends, the link is
    active while you and the beast are within line of sight of each
    other. Through the link, the beast can understand your telepathic
    messages to it, and it can telepathically communicate simple
    emotions and concepts back to you. While the link is active, the
    beast gains advantage on attack rolls against any creature within
    5 feet of you that you can see.

    """

    name = "Beast Bond"
    level = 1
    casting_time = "1 action"
    casting_range = "Touch"
    components = ("V", "S", "M")
    materials = "A bit of fur wrapped in a cloth"
    duration = "Instantaneous"
    ritual = False
    magic_school = "Divination"
    classes = ("Druid", "Ranger")


class BeastSense(Spell):
    """You touch a willing beast. For the duration of the spell, you can
    use your action to see through the beast's eyes and hear what it
    hears, and continue to do so until you use your action to return
    to your normal senses.

    """

    name = "Beast Sense"
    level = 2
    casting_time = "1 action"
    casting_range = "Touch"
    components = ("S",)
    materials = ""
    duration = "Concentration, up to 1 hour"
    ritual = True
    magic_school = "Divination"
    classes = ("Druid", "Ranger")


class BestowCurse(Spell):
    """You touch a creature, and that creature must succeed on a Wisdom saving throw or
    become cursed for the duration of the spell. When you cast this spell, choose
    the nature of the curse from the following options:* Choose one ability score.
    While cursed, the target has disadvantage on ability checks and saving throws
    made with that ability score.* While cursed, the target has disadvantage on
    attack rolls against you.* While cursed, the target must make a Wisdom saving
    throw at the start of each of its turns. If it fails, it wastes its action that
    turn doing nothing.* While the target is cursed, your attacks and spells deal an
    extra 1d8 necrotic damage to the target.

    A remove curse spell ends this
    effect. At the DM's option, you may choose an alternative curse effect, but it
    should be no more powerful than those described above.
    The DM has final say on
    such a curse's effect.

    **At Higher Levels:** If you cast this spell using a spell
    slot of 4th level or higher, the duration is concentration, up to 10 minutes.

    If you use a spell slot of 5th level or higher, the duration is 8 hours.
    If
    you use a spell slot of 7th level or higher, the duration is 24 hours.
    If you
    use a 9th level spell slot, the spell lasts until it is dispelled.
    Using a
    spell slot of 5th level or higher grants a duration that doesn't require
    concentration.
    """

    name = "Bestow Curse"
    level = 3
    casting_time = "1 action"
    casting_range = "Touch"
    components = ("V", "S")
    materials = ""
    duration = "Concentration, up to 1 minute"
    ritual = False
    magic_school = "Necromancy"
    classes = ("Bard", "Cleric", "Wizard")


class BigbysHand(Spell):
    """You create a Large hand of shimmering, translucent force in an
    unoccupied space that you can see within range. The hand lasts for
    the spell's duration, and it moves at your command, mimicking the
    movements of your own hand.

    The hand is an object that has AC 20 and hit points equal to your
    hit point maximum. If it drops to 0 hit points, the spell ends. It
    has a Strength of 26 (+8) and a Dexterity of 10 (+0). The hand
    doesn't fill its space.

    When you cast the spell and as a bonus action on your subsequent
    turns, you can move the hand up to 60 feet and then cause one of
    the following effects with it.

    **Clenched Fist**
    The hand strikes one creature or object within 5 feet of it. Make
    a melee spell attack for the hand using your game statistics. On a
    hit, the target takes 4d8 force damage.

    **Forceful Hand**
    The hand attempts to push a creature within 5 feet of it in a
    direction you choose. Make a check with the hand's Strength
    contested by the Strength (Athletics) check of the target. If the
    target is Medium or smaller, you have advantage on the check. If
    you succeed, the hand pushes the target up to 5 feet plus a number
    of feet equal to five times your spellcasting ability
    modifier. The hand moves with the target to remain within 5 feet
    of it.

    **Grasping Hand**
    The hand attempts to grapple a Huge or smaller creature within 5
    feet of it. You use the hand's Strength score to resolve the
    grapple. If the target is Medium or smaller, you have advantage on
    the check.  While the hand is grappling the target, you can use a
    bonus action to have the hand crush it. When you do so, the target
    takes bludgeoning damage equal to 2d6 + your spellcasting ability
    modifier.

    **Interposing Hand**
    The hand interposes itself between you and a creature you choose
    until you give the hand a different command. The hand moves to
    stay between you and the target, providing you with half cover
    against the target. The target can't move through the hand's space
    if its Strength score is less than or equal to the hand's Strength
    score. If its Strength score is higher than the hand's Strength
    score, the target can move toward you through the hand's space,
    but that space is difficult terrain for the target.

    **At Higher Levels:** When you cast this spell using a spell slot
    of 6th level or higher, the damage from the clenched fist option
    increases by 2d8 and the damage from the grasping hand increases
    by 2d6 for each slot level above 5th.

    """

    name = "Bigbys Hand"
    level = 5
    casting_time = "1 action"
    casting_range = "120 feet"
    components = ("V", "S", "M")
    materials = "An eggshell and a snakeskin glove"
    duration = "Instantaneous"
    ritual = False
    magic_school = "Evocation"
    classes = ("Wizard",)


class BladeBarrier(Spell):
    """You create a vertical wall of whirling, razor-sharp blades made of magical
    energy. The wall appears within range and lasts for the duration. You can make a
    straight wall up to 100 feet long, 20 feet high, and 5 feet thick, or a ringed
    wall up to 60 feet in diameter, 20 feet high, and 5 feet thick. The wall
    provides three-quarters cover to creatures behind it, and its space is difficult
    terrain.

     When a creature enters the wall's area for the first time on a turn
    or starts its turn there, the creature must make a Dexterity saving throw. On a
    failed save, the creature takes 6 d10 slashing damage. On a successful save,
    the creature takes half as much damage.
    """

    name = "Blade Barrier"
    level = 6
    casting_time = "1 action"
    casting_range = "90 feet"
    components = ("V", "S")
    materials = ""
    duration = "Concentration, up to 10 minutes"
    ritual = False
    magic_school = "Evocation"
    classes = ("Cleric",)


class BladeWard(Spell):
    """You extend your hand and trace a sigil of warding in the air. Until the end of
    your next turn, you have resistance against bludgeoning, piercing, and slashing
    damage dealt by weapon attacks.
    """

    name = "Blade Ward"
    level = 0
    casting_time = "1 action"
    casting_range = "Self"
    components = ("V", "S")
    materials = ""
    duration = "1 round"
    ritual = False
    magic_school = "Abjuration"
    classes = ("Bard", "Sorcerer", "Warlock", "Wizard")


class Bless(Spell):
    """You bless up to three creatures of your choice within range. Whenever a target
    makes an attack roll or a saving throw before the spell ends, the target can
    roll a d4 and add the number rolled to the attack roll or saving throw.

    At
    Higher Levels: When you cast this spell using a spell slot of 2nd level or
    higher, you can target one additional creature for each slot level above 1st.
    """

    name = "Bless"
    level = 1
    casting_time = "1 action"
    casting_range = "30 feet"
    components = ("V", "S", "M")
    materials = "A sprinkling of holy water"
    duration = "Concentration, up to 1 minute"
    ritual = False
    magic_school = "Enchantment"
    classes = ("Cleric", "Paladin")


class Blight(Spell):
    """Necromantic energy washes over a creature of your choice that you can see within
    range, draining moisture and vitality from it. The target must make a
    Constitution saving throw. The target takes 8d8 necrotic damage on a failed
    save, or half as much damage on a successful one. This spell has no effect on
    undead or constructs.

    If you target a plant creature or a magical plant, it
    makes the saving throw with disadvantage, and the spell deals maximum damage to
    it.

    If you target a nonmagical plant that isn't a creature, such as a tree or
    shrub, it doesn't make a saving throw; it simply withers and dies.

    At Higher
    Levels: When you cast this spell using a spell slot of 5th level or higher, the
    damage increases by 1d8 for each slot level above 4th.
    """

    name = "Blight"
    level = 4
    casting_time = "1 action"
    casting_range = "30 feet"
    components = ("V", "S")
    materials = ""
    duration = "Instantaneous"
    ritual = False
    magic_school = "Necromancy"
    classes = ("Druid", "Sorcerer", "Warlock", "Wizard")


class BlindingSmite(Spell):
    """The next time you hit a creature with a melee weapon attack during
    this spell's duration, you weapon flares with a bright light, and
    the attack deals an extra 3d8 radiant damage to the
    target. Additionally, the target must succeed on a Constitution
    saving throw or be blinded until the spell ends.

    A creature blinded by this spell makes another Constitution saving
    throw at the end of each of its turns. On a successful save, it is
    no longer blinded.

    """

    name = "Blinding Smite"
    level = 3
    casting_time = "1 bonus action"
    casting_range = "Self"
    components = ("V",)
    materials = ""
    duration = "Concentration, up to 1 minute"
    ritual = False
    magic_school = "Evocation"
    classes = ("Paladin",)


class BlindnessDeafness(Spell):
    """You can blind or deafen a foe. Choose one creature that you can see
    within range to make a Constitution saving throw. If it fails, the
    target is either blinded or deafened (your choice) for the
    duration. At the end of each of its turns, the target can make a
    Constitution saving throw. On a success, the spell ends.

    **At Higher Levels:** When you cast this spell using a spell slot of
    3rd level or higher, you can target one additional creature for
    each slot level above 2nd.

    """

    name = "Blindness/Deafness"
    level = 2
    casting_time = "1 action"
    casting_range = "30 feet"
    components = ("V",)
    duration = "1 minute"
    ritual = False
    magic_school = "Necromancy"
    classes = ("Bard", "Cleric", "Sorcerer", "Wizard")


class Blink(Spell):
    """Roll a d20 at the end of each of your turns for the duration of the spell. On a
    roll of 11 or higher, you vanish from your current plane of existence and appear
    in the Etheral Plane (the spell fails and the casting is wasted if you were
    already on that plane).

    At the start of you next turn, and when the spell ends
    if you are on the Etheral Plane, you return to an unoccupied space of your
    choice that you can see within 10 feet of the space you vanished from. If no
    unoccupied space is available within that rang, you appear in the nearest
    unoccupied space (chosen at random if more that one space is equally near). You
    can dismiss this spell as an action.

    While on the Ethereal Plane, you can see
    and hear the plane you originated from, which is cast in shades of gray, and you
    can't see anything more than 60 feet away.You can only affect and be affected
    by other reatures on the Ethereal Plane. Creature that aren't there can't
    perceive you or interact with you, unless they have the ability to do so.
    """

    name = "Blink"
    level = 3
    casting_time = "1 action"
    casting_range = "Self"
    components = ("V", "S")
    materials = ""
    duration = "1 minute"
    ritual = False
    magic_school = "Transmutation"
    classes = ("Sorcerer", "Wizard")


class Blur(Spell):
    """Your body becomes blurred, shifting and wavering to all who can see you. For the
    duration, any creature has disadvantage on attack rolls against you. An
    attacker is immune to this effect if it doesnt rely on sight, as with
    blindsight, or can see through illusions, as with truesight.
    """

    name = "Blur"
    level = 2
    casting_time = "1 action"
    casting_range = "Self"
    components = ("V",)
    materials = ""
    duration = "Concentration, up to 1 minute"
    ritual = False
    magic_school = "Illusion"
    classes = ("Sorcerer", "Wizard")


class BonesOfTheEarth(Spell):
    """You cause up to six pillars of stone to burst from places on the
    ground that you can see within range. Each pillar is a cylinder
    that has a diameter of 5 feet and a height of up to 30 feet. The
    ground where a pillar appears must be wide enough for its
    diameter, and you can target ground under a creature if that
    creature is Medium or smaller. Each pillar has AC 5 and 30 hit
    points. When reduced to 0 hit points, a pillar crumbles into
    rubble, which creates an area of difficult terrain with a 10-foot
    radius. The rubble lasts until cleared.

    If a pillar is created under a creature, that creature must
    succeed on a Dexterity saving throw or be lifted by the pillar. A
    creature can choose to fail the save.

    If a pillar is prevented from reaching its full height because of
    a ceiling or other obstacle, a creature on the pillar takes 6d6
    bludgeoning damage and is restrained, pinched between the pillar
    and the obstacle. The restrained creature can use an action to
    make a Strength or Dexterity check (the creature's choice) against
    the spell's saving throw DC. On a success, the creature is no
    longer restrained and must either move off the pillar or fall off
    it.

    **At Higher Levels.** When you cast this spell using a spell slot
    of 7th level or higher, you can create two additional pillars for
    each slot level above 6th.

    """

    name = "Bones Of The Earth"
    level = 6
    casting_time = "1 action"
    casting_range = "120 feet"
    components = ("V", "S")
    duration = "Instantaneous"
    ritual = False
    magic_school = "Transmutation"
    classes = ("Druid",)


class BoomingBlade(Spell):
    """As part of the action used to cast this spell, you must make a melee attack with
    a weapon against one creature within the spell's range, otherwise the spell
    fails.
    On a hit, the target suffers the attack's normal effects, and it becomes
    sheathed in booming energy until the start of your next turn. If the target
    willingly moves be- fore then, it immediately takes 1d8 thunder damage, and the
    spell ends.
    This spell's damage increases when you reach higher levels.

    At
    Higher Levels: At 5th level, the melee attack deals an extra 1d8 thunder damage
    to the target, and the damage the target takes for moving increases to 2d8. Both
    damage rolls increase by 1d8 at 11th level and 17th level.
    """

    name = "Booming Blade"
    level = 0
    casting_time = "1 action"
    casting_range = "5 feet"
    components = ("V", "M")
    materials = "A weapon"
    duration = "Instantaneous"
    ritual = False
    magic_school = "Evocation"
    classes = ("Sorcerer", "Warlock", "Wizard")


class BrandingSmite(Spell):
    """The next time you hit a creature with a weapon attack before this spell ends,
    the weapon glemas with astral radiance as you strike. The attack deals an extra
    2d6 radiant damage to the target, which becomes visible if it is invisible, and
    the target sheds dim light in a 5-foot radius and can't become invisible until
    the spell ends.

    **At Higher Levels:** When you cast this spell using a spell slot
    of 3rd level or higher, the extra damage increases by 1d6 for each slot level
    above 2nd.
    """

    name = "Branding Smite"
    level = 2
    casting_time = "1 bonus action"
    casting_range = "Self"
    components = ("V",)
    materials = ""
    duration = "Concentration, up to 1 minute"
    ritual = False
    magic_school = "Evocation"
    classes = ("Paladin",)


class BurningHands(Spell):
    """As you hold your hands with thumbs touching and fingers spread, a thin sheet of
    flames shoots forth from your outstretched fingertips. Each creature in a
    15-foot cone must make a Dexterity saving throw. A creature takes 3d6 fire
    damage on a failed save, or half as much damage on a successful one.

    The fire
    ignites any flammable objects in the area that aren't being worn or carried.

    At
    Higher Levels: When you cast this spell using a spell slot of 2nd level or
    higher, the damage increases by 1d6 for each slot level above 1st.
    """

    name = "Burning Hands"
    level = 1
    casting_time = "1 action"
    casting_range = "Self (15-foot cone)"
    components = ("V", "S")
    materials = ""
    duration = "Instantaneous"
    ritual = False
    magic_school = "Evocation"
    classes = ("Sorcerer", "Wizard")
