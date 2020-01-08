from .spells import Spell


class GaseousForm(Spell):
    """You transform a willing creature you touch, along with everything it's wearing 
    and carrying, into a misty cloud for the duration. The spell ends if the 
    creature drops to 0 hit points. An incorporeal creature isn't affected.
    
    While 
    in this form, the target's only method of movement is a flying speed of 10 feet.
     The target can enter and occupy the space of another creature. The target has 
    resistance to nonmagical damage, and it has advantage on Strength, Dexterity, 
    and Constitution saving throws. The target can pass through small holes, narrow 
    openings, and even mere cracks, though it treats liquids as though they were 
    solid surfaces. The target can't fall and remains hovering in the air even when 
    stunned or otherwise incapacitated.
    
    While in the form of a misty cloud, the 
    target can't talk or manipulate objects, and any objects it was carrying or 
    holding can't be dropped, used, or otherwise interacted with. The target can't 
    attack or cast spells.
    """
    name = "Gaseous Form"
    level = 3
    casting_time = "1 action"
    casting_range = "Touch"
    components = ('V', 'S', 'M')
    materials = """A bit of gauze and a wisp of smoke"""
    duration = "Concentration, up to 1 hour"
    ritual = False
    magic_school = "Transmutation"
    classes = ('Sorcerer', 'Warlock', 'Wizard')


class Gate(Spell):
    """You conjure a portal linking an unoccupied space you can see within range to a 
    precise location on a different plane of existence. The portal is a circular 
    opening, which you can make 5 to 20 feet in diameter. You can orient the portal 
    in any direction you choose. The portal lasts for the duration.
    
    The portal has 
    a front and a back on each plane where it appears. Travel through the portal is 
    possible only by moving through its front. Anything that does so is instantly 
    transported to the other plane, appearing in the unoccupied space nearest to the
     portal.
    
    Deities and other planar rulers can prevent portals created by this 
    spell from opening in their presence or anywhere within their domains.
    
    When you
     cast this spell, you can speak the name of a specific creature (a pseudonym, 
    title, or nickname doesn't work). If that creature is on a plane other than the 
    one you are on, the portal opens in the named creature's immediate vicinity and 
    draws the creature through it to the nearest unoccupied space on your side of 
    the portal. You gain no special power over the creature, and it is free to act 
    as the Dm deems appropriate. It might leave, attack you, or help you.
    """
    name = "Gate"
    level = 9
    casting_time = "1 action"
    casting_range = "60 feet"
    components = ('V', 'S', 'M')
    materials = """A diamond worth at least 5,000 gp"""
    duration = "Concentration, up to 1 minute"
    ritual = False
    magic_school = "Conjuration"
    classes = ('Cleric', 'Sorcerer', 'Wizard')


class Geas(Spell):
    """You place a magical command on a creature that you can see within range, forcing
     it to carry out some service or refrain from some action or course of actiity 
    as you decide.
    If the creature can understand you, it must succeed on a Wisdom 
    saving throw or become charmed by you for the duration. While the creature is 
    charmed by you, it takes 5d10 psychic damage each time it acts in a manner 
    directly counter to your instructions, but no more than once each day. A 
    creature that can't understand you is unaffected by the spell.
    
    You can issue 
    any command you choose, short of an activity that would result in certain death.
     Should you issue a suicidal command, the spell ends. You can end the spell 
    early by using an action to dismiss it. A remove curse, greater restoration, or 
    wish spell also ends it.
    
    At Higher Levels: When you cast this spell usinga 
    spell slot of 7th or 8th level, the duration is 1 year.
    When you cast this 
    spell using a spell slot of 9th level, the spell lasts until it is ended by one 
    of the spells mentioned above.
    """
    name = "Geas"
    level = 5
    casting_time = "1 minute"
    casting_range = "60 feet"
    components = ('V',)
    materials = """"""
    duration = "30 days"
    ritual = False
    magic_school = "Enchantment"
    classes = ('Bard', 'Cleric', 'Druid', 'Paladin', 'Wizard')


class GentleRepose(Spell):
    """You touch a corpse or other remains. For the duration, the target is protected 
    from decay and can't become undead.
    
    The spell also effectively extends the time
     limit on raising the target from the dead, since days spent under the influence
     of this spell don't count against the time limit of spells such as raise dead.
    """
    name = "Gentle Repose"
    level = 2
    casting_time = "1 action"
    casting_range = "Touch"
    components = ('V', 'S', 'M')
    materials = """A pinch of salt and one copper piece placed on each of the corpse's eyes, which must remain there for the duration"""
    duration = "10 days"
    ritual = True
    magic_school = "Necromancy"
    classes = ('Cleric', 'Wizard')


class GiantInsect(Spell):
    """You transform up to ten centipedes, three spiders, five wasps, or one scorpion 
    within range into giant versions of their natural forms for the duration. A 
    centipede becomes a giant centipede, a spider becaomes a giant spider, a wasp 
    becomes a giant wasp, and a scorpion becomes a giant scorpion.
    
    Each creature 
    obeys your verbal commands, and in combat, they act on your turn each round. The
     DM has the statistics for these creatures and resolves their actions and 
    movement.
    
    A creature remains in its giant size for the duration, until it drops
     to 0 hit points, or until you use an action to dismiss the effect on it.
    
    The 
    DM might allow you to choose different targets. For example, if you transform a 
    bee, its giant version might have the same statistics as a giant wasp.
    """
    name = "Giant Insect"
    level = 4
    casting_time = "1 action"
    casting_range = "30 feet"
    components = ('V', 'S')
    materials = """"""
    duration = "Concentration, up to 10 minutes"
    ritual = False
    magic_school = "Transmutation"
    classes = ('Druid',)


class Glibness(Spell):
    """Until the spell ends, when you make a Charisma check, you can replace the number
     you roll with a 15. Additionally, no matter what you say, magic that would 
    determine if you are telling the truth indicates that you are being truthful.
    """
    name = "Glibness"
    level = 8
    casting_time = "1 action"
    casting_range = "Self"
    components = ('V',)
    materials = """"""
    duration = "1 hour"
    ritual = False
    magic_school = "Transmutation"
    classes = ('Bard', 'Warlock')


class GlobeOfInvulnerability(Spell):
    """An immobile, faintly shimmering barrier springs into existence in a 10-foot 
    radius around you and remains for the duration.
    
    Any spell of 5th level or lower
     cast from outside the barrier can't affect creatures or objects within it, even
     if the spell is cast using a higher level spell slot. Such a spell can target 
    creatures and objects within the barrier, but the spell has no effect on them. 
    Similarly, the area within the barrier is excluded from the areas affected by 
    such spells.
    
    At Higher Levels: When you cast this spell using a spell slot of 
    7th level or higher, the barrier blocks spells of one level higher for each slot
     level above 6th.
    """
    name = "Globe Of Invulnerability"
    level = 6
    casting_time = "1 action"
    casting_range = "Self (10-foot radius)"
    components = ('V', 'S', 'M')
    materials = """A glass or crystal bead that shatters when the spell ends"""
    duration = "Concentration, up to 1 minute"
    ritual = False
    magic_school = "Abjuration"
    classes = ('Sorcerer', 'Wizard')


class GlyphOfWarding(Spell):
    """When you cast this spell, you inscribe a glyph that harms other creatures, 
    either upon a surface (such as a table or a section of floor or wall) or within 
    an object that can be closed (such as a book, a scroll, or a treasure chest) to 
    conceal the glyph.
    If you choose a surface, the glyph can cover an area of the 
    surface no larger than 10 feet in diameter. If you choose an object, that object
     must remain in its place; if the object is moved more than 10 feet from where 
    you cast this spell, the glyph is broken, and the spell ends without being 
    triggered.
    
    The glyph is nearly invisible and requires a successful Intelligence
     (Investigation) check against your spell save DC to be found.
    
    You decide what 
    triggers the glyph when you cast the spell. For glyphs inscribed on a surface, 
    the most typical triggers include touching or standing on the glyph, removing 
    another object covering the glyph, approaching within a certain distance of the 
    glyph, or manipulating the object on which the glyph is inscribed. For glyphs 
    inscribed within an object, the most common triggers include opening that 
    object, approaching within a certain distance of the object, or seeing or 
    reading the glyph. Once a glyph is triggered, this spell ends.
    
    You can further 
    refine the trigger so the spell activates only under certain circumstances or 
    according to physical characteristics (such as height or weight), creature kind 
    (for example, the ward could be set to affect aberrations or drow), or 
    alignment. You can also set conditions for creatures that don't trigger the 
    glyph, such as those who say a certain password.
    
    When you inscribe the glyph, 
    choose explosive runes or a spell glyph.
    
    Explosive Runes
    When triggered, the 
    glyph erupts with magical energy in a 20-foot-radius sphere centered on the 
    glyph. The sphere spreads around corners. Each creature in the area must make a 
    Dexterity saving throw. A creature takes 5d8 acid, cold, fire, lightning, or 
    thunder damage on a failed saving throw (your choice when you create the glyph),
     or half as much damage on a successful one.
    
    Spell Glyph
    You can store a 
    prepared spell of 3rd level or lower in the glyph by casting it as part of 
    creating the glyph. The spell must target a single creature or an area. The 
    spell being stored has no immediate effect when cast in this way. When the glyph
     is triggered, the stored spell is cast. If the spell has a target, it targets 
    the creature that triggered the glyph. If the spell affects an area, the area is
     centered on that creature. If the spell summons hostile creatures or creates 
    harmful objects or traps, they appear as close as possible to the intruder and 
    attack it. If the spell requires concentration, it lasts until the end of its 
    full duration.
    
    At Higher Levels: 
    """
    name = "Glyph Of Warding"
    level = 3
    casting_time = "1 hour"
    casting_range = "Touch"
    components = ('V', 'S', 'M')
    materials = """Incense and powdered diamond worth at least 200 gp, which the spell consumes"""
    duration = "Until dispelled or triggered"
    ritual = False
    magic_school = "Abjuration"
    classes = ('you', 'cast', 'this', 'spell', 'using', 'a', 'spell', 'slot', 'of', '4th', 'level', 'or', 'higher', 'the', 'damage', 'of', 'an', 'explosive', 'runes', 'glyph', 'increases', 'by', '1d8', 'for', 'each', 'slot', 'level', 'above', '3rd.', 'If', 'you', 'create', 'a', 'spell', 'glyph', 'you', 'can', 'store', 'any', 'spell', 'of', 'up', 'to', 'the', 'same', 'level', 'as', 'the', 'slot', 'you', 'use', 'for', 'the', 'glyph', 'of')


class Goodberry(Spell):
    """Up to ten berries appear in your hand and are infused with magic for the 
    duration. A creature can use its action to eat one berry. Eating a berry 
    restores 1 hit point, and the berry provides enough nourishment to sustain a 
    creature for one day.
    The berries lose their potency if they have not been 
    consumed within 24 hours of the casting of this spell.
    """
    name = "Goodberry"
    level = 1
    casting_time = "1 action"
    casting_range = "Touch"
    components = ('V', 'S', 'M')
    materials = """A sprig of mistletoe"""
    duration = "Instantaneous"
    ritual = False
    magic_school = "Transmutation"
    classes = ('Druid', 'Ranger')


class GraspingVine(Spell):
    """You conjure a vine that sprouts from the ground in an unoccupied space of your 
    choice that you can see within range. When you cast this spell, you can direct 
    the vine to lash out at a creature within 30 feet of it that you can see. That 
    creature must succeed on a Dexterity saving throw or be pulled 20 feet directly 
    toward the vine.
    
    Until the spell ends, you can direct the vine to lash out at 
    the same creature or another one as a bonus action on each of your turns.
    """
    name = "Grasping Vine"
    level = 4
    casting_time = "1 bonus action"
    casting_range = "30 feet"
    components = ('V', 'S')
    materials = """"""
    duration = "Concentration, up to 1 minute"
    ritual = False
    magic_school = "Conjuration"
    classes = ('Druid', 'Ranger')


class Grease(Spell):
    """Slick grease covers the ground in a 10-foot square centered on a point within 
    range and turns it into difficult terrain for the duration.
    
    When the grease 
    appears, each creature standing in its area must succeed on a Dexterity saving 
    throw or fall prone. A creature that enters the area or ends its turn there must
     also succeed on a Dexterity saving throw or fall prone.
    """
    name = "Grease"
    level = 1
    casting_time = "1 action"
    casting_range = "60 feet"
    components = ('V', 'S', 'M')
    materials = """A bit of pork rind or butter"""
    duration = "1 minute"
    ritual = False
    magic_school = "Conjuration"
    classes = ('Wizard',)


class GreaterInvisibility(Spell):
    """You or a creature you touch becomes invisible until the spell ends. Anything the
     target is wearing or carrying is invisible as long as it is on the target's 
    person.
    """
    name = "Greater Invisibility"
    level = 4
    casting_time = "1 action"
    casting_range = "Touch"
    components = ('V', 'S')
    materials = """"""
    duration = "Concentration, up to 1 minute"
    ritual = False
    magic_school = "Illusion"
    classes = ('Bard', 'Sorcerer', 'Wizard')


class GreaterRestoration(Spell):
    """You imbue a creature you touch with positive energy to undo a debilitating 
    effect. You can reduce the target's exhaustion level by one, or end one of the 
    following effects on the target: 
    * One effect that charmed or petrified the 
    target 
    * One curse, including the target's attunement to a cursed magic item 
    *
     Any reduction to one of the target's ability scores 
    * One effect reducing the 
    target's hit point maximum
    """
    name = "Greater Restoration"
    level = 5
    casting_time = "1 action"
    casting_range = "Touch"
    components = ('V', 'S', 'M')
    materials = """Diamond dust worth at least 100 gp, which the spell consumes"""
    duration = "Instantaneous"
    ritual = False
    magic_school = "Abjuration"
    classes = ('Bard', 'Cleric', 'Druid')


class GreenFlameBlade(Spell):
    """As part of the action used to cast this spell, you must make a melee attack with
     a weapon against one creature within the spell's range, otherwise the spell 
    fails. On a hit, the target suffers the attack's normal effects, and green fire 
    leaps from the target to a different creature of your choice that you can see 
    within 5 feet of it. The second creature takes fire damage equal to your 
    spellcasting ability modifier. This spell's damage increases when you reach 
    higher levels.
    
    At Higher Levels: At 5th level, the melee attack deals an extra 
    1d8 fire damage to the target, and the fire damage to the second creature 
    increases to 1d8 + your spellcasting ability modifier. Both damage rolls 
    increase by 1d8 at 11th level and 17th level.
    """
    name = "Green-Flame Blade"
    level = 0
    casting_time = "1 action"
    casting_range = "5 feet"
    components = ('V', 'M')
    materials = """A weapon"""
    duration = "Instantaneous"
    ritual = False
    magic_school = "Evocation"
    classes = ('Sorcerer', 'Warlock', 'Wizard')


class GuardianOfFaith(Spell):
    """A Large spectral guardian appears and hovers for the duration in an unoccupied 
    space of your choice that you can see within range. The guardian occupies that 
    space and is indistinct except for a gleaming sword and shield emblazoned with 
    the symbol of your deity.
    
    Any creature hostile to you that moves to a space 
    within 10 feet of the guardian for the firs time on a turn must succeed on a 
    Dexterity saving throw. The creature takes 20 radiant damage on a failed save, 
    or half as much damage on a successful one. The guardian vanishes when it has 
    dealt a total of 60 damage.
    """
    name = "Guardian Of Faith"
    level = 4
    casting_time = "1 action"
    casting_range = "30 feet"
    components = ('V',)
    materials = """"""
    duration = "8 hours"
    ritual = False
    magic_school = "Conjuration"
    classes = ('Cleric',)


class GuardianOfNature(Spell):
    """A nature spirit answers your call and transforms you into a powerful guardian. 
    The transformation lasts until the spell ends. You choose one of the following 
    forms to assume: Primal Beast or Great Tree.
    Primal Beast. Bestial fur covers 
    your body, your facial features become feral, and you gain the following 
    benefits:
    - Your walking speed increases by 10 feet.
    - You gain darkvision with 
    a range of 120 feet.
    - You make Strength-based attack rolls with advantage.
    - 
    Your melee weapon attacks deal an extra 1d6 force damage on a hit.
    Great Tree. 
    Your skin appears barky, leaves sprout from your hair, and you gain the 
    following benefits:
    . You gain 10 temporary hit points.
    - You make Constitution 
    saving throws with advantage.
    - You make Dexterity- and Wisdom-based attack 
    rolls with advantage.
    - While you are on the ground, the ground within 15 feet 
    of you is difficult terrain for your enemies.
    """
    name = "Guardian Of Nature"
    level = 4
    casting_time = "1 bonus action"
    casting_range = "Self"
    components = ('V',)
    materials = """"""
    duration = "Concentration, up to 1 minute"
    ritual = False
    magic_school = "Transmutation"
    classes = ('Druid', 'Ranger')


class GuardsAndWards(Spell):
    """You create a ward that protects up to 2,500 square feet of floor space (an area 
    50 feet square, or one hundred 5-foot squares or twenty-five 10-foot squares). 
    The warded area can be up to 20 feet tall, and shaped as you desire. You can 
    ward several stories of a stronghold by dividing the area among them, as long as
     you can walk into each contiguous area while you are casting the spell.
    
    When 
    you cast this spell, you can specify individuals that are unaffected by any or 
    all of the effects that you choose. You can also specify a password that, when 
    spoken aloud, makes the speaker immune to these effects.
    
    Guards and wards 
    creates the following effects within the warded area.
    
    Corridors
    Fog fills all 
    the warded corridors, making them heavily obscured. In addition, at each 
    intersection or branching passage offering a choice of direction, there is a 50 
    percent chance that a creature other than you will believe it is going in the 
    opposite direction from the one it chooses.
    
    Doors
    All doors in the warded area 
    are magically locked, as if sealed by an arcane lock spell. In addition, you can
     cover up to ten doors with an illusion (equivalent to the illusory object 
    function of the m inor illusion spell) to make them appear as plain sections of 
    wall.
    
    Stairs
    Webs fill all stairs in the warded area from top to bottom, as the
     web spell. These strands regrow in 10 minutes if they are burned or torn away 
    while guards and wards lasts.
    
    Other Spell Effect
    You can place your choice of 
    one of the following magical effects within the warded area of the stronghold.
    -
     Place dancing lights in four corridors. You can designate a simple program that
     the lights repeat as long as
    guards and wards lasts.
    - Place magic mouth in two
     locations.
    - Place stinking cloud in two locations. The vapors appear in the 
    places you designate; they return within 10 minutes if dispersed by wind while 
    guards and wards lasts.
    - Place a constant gust of wind in one corridor or room.
    
    - Place a suggestion in one location. You select an area of up to 5 feet 
    square, and any creature that enters
    or passes through the area receives the 
    suggestion mentally.
    
    The whole warded area radiates magic. A dispel magic cast 
    on a specific effect, if successful, removes only that effect.
    You can create a 
    permanently guarded and warded structure by casting this spell there every 
    day for one year.
    """
    name = "Guards And Wards"
    level = 6
    casting_time = "10 minutes"
    casting_range = "Touch"
    components = ('V', 'S', 'M')
    materials = """Burning incense, a small measure of brimstone and oil, a knotted string, a small amount of umber hulk blood, and a small silver rod worth at least 10 gp"""
    duration = "24 hours"
    ritual = False
    magic_school = "Abjuration"
    classes = ('Bard', 'Wizard')


class Guidance(Spell):
    """You touch one willing creature. Once before the spell ends, the target can roll 
    a d4 and add the number rolled to one ability check of its choice. It can roll 
    the die before or after making the ability check. The spell then ends.
    """
    name = "Guidance"
    level = 0
    casting_time = "1 action"
    casting_range = "Touch"
    components = ('V', 'S')
    materials = """"""
    duration = "Concentration, up to 1 minute"
    ritual = False
    magic_school = "Divination"
    classes = ('Cleric', 'Druid')


class GuidingBolt(Spell):
    """A flash of light streaks toward a creature of your choice within range.
    Make a 
    ranged spell attack against the target. On a hit, the target takes 4d6 radiant 
    damage, and the next attack roll made against this target before the end of your
     next turn has advantage, thanks to the mystical dim light glittering on the 
    target until then.
    
    At Higher Levels: When you cast this spell using a spell 
    slot of 2nd level or higher, the damage increases by 1d6 for each slot level 
    above 1st.
    """
    name = "Guiding Bolt"
    level = 1
    casting_time = "1 action"
    casting_range = "120 feet"
    components = ('V', 'S')
    materials = """"""
    duration = "1 round"
    ritual = False
    magic_school = "Evocation"
    classes = ('Cleric',)


class Gust(Spell):
    """You seize the air and compel it to create one of the following effects at a 
    point you can see within range:
    - One Medium or smaller creature that you choose
     must succeed on a Strength saving throw or be pushed up to 5 feet away from 
    you.
    - You create a small blast of air capable of moving one object that is 
    neither held nor carried and that weighs no more than 5 pounds. The object is 
    pushed up to 10 feet away from you. It isn't pushed with enough force to cause 
    damage.
    - You create a harmless sensory affect using air, such as causing leaves
     to rustle, wind to slam shutters shut, or your clothing to ripple in a breeze.
    """
    name = "Gust"
    level = 0
    casting_time = "1 action"
    casting_range = "30 feet"
    components = ('V', 'S')
    materials = """"""
    duration = "Instantaneous"
    ritual = False
    magic_school = "Transmutation"
    classes = ('Druid', 'Sorcerer', 'Wizard')


class GustOfWind(Spell):
    """A line of strong wind 60 feet long and 10 feet wide blasts from you in a 
    direction you choose for the spell's duration. Each creature that starts its 
    turn in the line must succeed on a Strength saving throw or be pushed 15 feet 
    away from you in a direction following the line.
    
    Any creature in the line must 
    spend 2 feet of movement for every 1 foot it moves when moving closer to you.
    
    
    The gust disperses gas or vapor, and it extinguishes candles, torches, and 
    similar unprotected flames in the area. It causes protected flames, such as 
    those of lanterns, to dance wildly and has a 50 percent chance to extinguish 
    them.
    
    As a bonus action on each of your turns before the spell ends, you can 
    change the direction in which the line blasts from you.
    """
    name = "Gust Of Wind"
    level = 2
    casting_time = "1 action"
    casting_range = "Self (60-foot line)"
    components = ('V', 'S', 'M')
    materials = """A legume seed"""
    duration = "Concentration, up to 1 minute"
    ritual = False
    magic_school = "Evocation"
    classes = ('Druid', 'Sorcerer', 'Wizard')


