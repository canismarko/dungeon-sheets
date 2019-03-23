from .spells import Spell


class DancingLights(Spell):
    """You create up to four torch-sized lights within range, making them appear as 
    torches, lanterns, or glowing orbs that hover in the air for the duration. 
    You 
    can also combine the four lights into one glowing vaguely humanoid form of 
    Medium size. Whichever form you choose, each light sheds dim light in a 10-foot 
    radius. 
    
    As a bonus action on your turn, you can move the lights up to 60 feet 
    to a new spot within range. A light must be within 20 feet of another light 
    created by this spell, and a light winks out if it exceeds the spell’s range.
    """
    name = "Dancing Lights"
    level = 0
    casting_time = "1 action"
    casting_range = "120 feet"
    components = ('V', 'S', 'M')
    materials = """A bit of phosphorus or wychwood, or a glowworm"""
    duration = "Concentration, up to 1 minute"
    ritual = False
    magic_school = "Evocation"
    classes = ('Bard', 'Sorcerer', 'Wizard')


class DanseMacabre(Spell):
    """Threads of dark power leap from your fingers to pierce up to five Small or 
    Medium corpses you can see within range. Each corpse immediately stands up and 
    becomes undead. You decide whether it is a zombie or a skeleton (the statistics 
    for zombies and skeletons are in the Monster Manual), and it gains a bonus to 
    its attack and damage rolls equal to your spellcasting ability modifier. You can
     use a bonus action to mentally command the creatures you make with this spell, 
    issuing the same command to all of them. To receive the command, a creature must
     be within 60 feet of you. You decide what action the creatures will take and 
    where they will move during their next turn, or you can issue a general command,
     such as to guard a chamber or passageway against your foes. lfyou issue no 
    commands, the creatures do nothing except defend themselves against hostile 
    creatures. Once given an order, the creatures continue to follow it until their 
    task is complete.
    The creatures are under your control until the spell ends, 
    after which they become inanimate once more.
    
    At Higher Levels: When you cast 
    this spell using a spell slot‘ of 6th level or higher, you animate up to two 
    additional corpses for each slot level above 5th.
    """
    name = "Danse Macabre"
    level = 5
    casting_time = "1 action"
    casting_range = "60 feet"
    components = ('V', 'S')
    materials = """"""
    duration = "Concentration, up to 1 hour"
    ritual = False
    magic_school = "Necromancy"
    classes = ('Warlock', 'Wizard')


class Darkness(Spell):
    """Magical darkness spreads from a point you choose within range to fill a 15-foot 
    radius sphere for the duration.
    The darkness spreads around corners. A creature 
    with darkvision can’t see through this darkness, and nonmagical light can’t 
    illuminate it. 
    
    If the point you choose is on an object you are holding or one 
    that isn’t being worn or carried, the darkness emanates from the object and 
    moves with it. Completely covering the source of the darkness with an opaque 
    object, such as a bowl or a helm, blocks the darkness.
    
    If any of this spell’s 
    area overlaps with an area of light created by a spell of 2nd level or lower, 
    the spell that created the light is dispelled.
    """
    name = "Darkness"
    level = 2
    casting_time = "1 action"
    casting_range = "60 feet"
    components = ('V', 'M')
    materials = """Bat fur and a drop of pitch or piece of coal"""
    duration = "Concentration, up to 10 minutes"
    ritual = False
    magic_school = "Evocation"
    classes = ('Sorcerer', 'Warlock', 'Wizard')


class Darkvision(Spell):
    """You touch a willing creature to grant it the ability to see in the dark.
    For the
     duration, that creature has darkvision out to a range of 60 feet.
    """
    name = "Darkvision"
    level = 2
    casting_time = "1 action"
    casting_range = "Touch"
    components = ('V', 'S', 'M')
    materials = """Either a pinch of dried carrot or an agate"""
    duration = "8 hours"
    ritual = False
    magic_school = "Transmutation"
    classes = ('Sorcerer', 'Wizard', 'Druid', 'Ranger')


class Dawn(Spell):
    """The light of dawn shines down on a location you specify within range. Until the 
    spell ends, a 30-foot-radius.40-foot-high cylinder of bright light glimmers 
    there. This light is sunlight. When the cylinder appears, each creature in it 
    must make a Constitution saving throw, taking 4d10 radiant damage on a failed 
    save, or half as much damage on a successful one. A creature must also make this
     saving throw whenever it ends its turn in the cylinder. If you’re within 60 
    feet of the cylinder, you can move it up to 60 feet as a bonus action on your 
    turn.
    """
    name = "Dawn"
    level = 5
    casting_time = "1 action"
    casting_range = "60 feet"
    components = ('V', 'S', 'M')
    materials = """A sunburst pendant worth at least 100 gp"""
    duration = "Concentration, up to 1 minute"
    ritual = False
    magic_school = "Evocation"
    classes = ('Cleric', 'Wizard')


class Daylight(Spell):
    """A 60-foot-radius sphere of light spreads out from a point you choose within 
    range. 
    The sphere is bright light and sheds dim light for an additional 60 
    feet. 
    
    If you chose a point on an object you are holding or one that isn’t 
    being worn or carried, the light shines from the object with and moves with it. 
    Completely covering the affected object with an opaque object, such as a bowl or
     a helm, blocks the light. 
    
    If any of this spell’s area overlaps with an area 
    of darkness created by a spell of 3rd level or lower, the spell that created the
     darkness is dispelled.
    """
    name = "Daylight"
    level = 3
    casting_time = "1 action"
    casting_range = "60 feet"
    components = ('V', 'S')
    materials = """"""
    duration = "1 hour"
    ritual = False
    magic_school = "Evocation"
    classes = ('Cleric', 'Druid', 'Paladin', 'Ranger', 'Sorcerer')


class DeathWard(Spell):
    """You touch a creature and grant it a measure of protection from death. 
    The first
     time the target would drop to 0 hit points as a result of taking damage, the 
    target instead drops to 1 hit point, and the spell ends. If the spell is still 
    in effect when the target is subjected to an effect that would kill it 
    instantaneously without dealing damage, that effect is instead negated against 
    the target, and the spells ends.
    """
    name = "Death Ward"
    level = 4
    casting_time = "1 action"
    casting_range = "Touch"
    components = ('V', 'S')
    materials = """"""
    duration = "8 hours"
    ritual = False
    magic_school = "Abjuration"
    classes = ('Cleric', 'Paladin')


class DelayedBlastFireball(Spell):
    """A beam of yellow light flashes from your pointing finger, then condenses to 
    linger at a chosen point within range as a glowing bead for the duration. 
    When 
    the spell ends, either because your concentration is broken or because you 
    decide to end it, the bead blossoms with a low roar into an explosion of flame 
    that spreads around corners. Each creature in a 20-foot-radius sphere centered 
    on that point must make a Dexterity saving throw. A creature takes fire damage 
    equal to the total accumulated damage on a failed save, or half as much damage 
    on a successful one. 
    
    The spell’s base damage is 12d6. If at the end of your 
    turn the bead has not yet detonated, the damage increases by 1d6. 
    
    If the 
    glowing bead is touched before the interval has expired, the creature touching 
    it must make a Dexterity saving throw. On a failed save, the spell ends 
    immediately, causing the bead to erupt in flame. On a successful save, the 
    creature can throw the bead up to 40 feet. When it strikes a creature or a solid
     object, the spell ends, and the bead explodes. 
    The fire damages objects in the
     area and ignites flammable objects that aren’t being worn or carried.
    
    At 
    Higher Levels: When you cast this spell using a spell slot of 8th level or 
    higher, the base damage increases by 1d6 for each slot level above 7th.
    """
    name = "Delayed Blast Fireball"
    level = 7
    casting_time = "1 action"
    casting_range = "150 feet"
    components = ('V', 'S', 'M')
    materials = """A tiny ball of bat guano and sulfur"""
    duration = "Concentration, up to 1 minute"
    ritual = False
    magic_school = "Evocation"
    classes = ('Sorcerer', 'Wizard')


class Demiplane(Spell):
    """You create a shadowy door on a flat solid surface that you can see within range.
     
    The door is large enough to allow Medium creatures to pass through unhindered.
     When opened, the door leads to a demiplane that appears to be an empty room 30 
    feet in each dimension, made of wood or stone. When the spell ends, the door 
    disappears, and any creatures or objects inside the demiplane remain trapped 
    there, as the door also disappears from the other side. 
    
    Each time you cast 
    this spell, you can create a new demiplane, or have the shadowy door connect to 
    a demiplane you created with a previous casting of this spell. Additionally, if 
    you know the nature and contents of a demiplane created by a casting of  this 
    spell by another creature, you can have the shadowy door connect to its 
    demiplane instead.
    """
    name = "Demiplane"
    level = 8
    casting_time = "1 action"
    casting_range = "60 feet"
    components = ('S',)
    materials = """"""
    duration = "1 hour"
    ritual = False
    magic_school = "Conjuration"
    classes = ('Warlock', 'Wizard')


class DestructiveWave(Spell):
    """You strike the ground, creating a burst of divine energy that ripples outward 
    from you. Each creature you choose within 30 feet of you must succeed on a 
    Constitution saving throw or take 5d6 thunder damage, as well as 5d6 radiant or 
    necrotic damage (your choice), and be knocked prone. A creature that succeeds on
     its saving throw takes half as much damage and isn’t knocked prone.
    """
    name = "Destructive Wave"
    level = 5
    casting_time = "1 action"
    casting_range = "Self (30-foot radius)"
    components = ('V',)
    materials = """"""
    duration = "Instantaneous"
    ritual = False
    magic_school = "Evocation"
    classes = ('Paladin',)


class DetectEvilAndGood(Spell):
    """For the duration, you know if there is an aberration, celestial, elemental, fey,
     fiend, or undead within 30 feet of you, as well as where the creature is 
    located. Similarly, you know if there is a place or object within 30 feet of you
     that has been magically consecrated or desecrated. 
    
    The spell can penetrate 
    most barriers, but it is blocked by 1 foot of stone, 1 inch of common metal, a 
    thin sheet of lead, or 3 feet of wood or dirt.
    """
    name = "Detect Evil And Good"
    level = 1
    casting_time = "1 action"
    casting_range = "Self"
    components = ('V', 'S')
    materials = """"""
    duration = "Concentration, up to 10 minutes"
    ritual = False
    magic_school = "Divination"
    classes = ('Cleric', 'Paladin')


class DetectMagic(Spell):
    """For the duration, you sense the presence of magic within 30 feet of you. If you 
    sense magic in this way, you can use your action to see a faint aura around any 
    visible creature or object in the area that bears magic, and you learn its 
    school of magic, if any. 
    
    The spell can penetrate most barriers, but is blocked
     by 1 foot of stone, 1 inch of common metal, a thin sheet of lead, or 3 feet of 
    wood or dirt.
    """
    name = "Detect Magic"
    level = 1
    casting_time = "1 action"
    casting_range = "Self"
    components = ('V', 'S')
    materials = """"""
    duration = "Concentration, up to 10 minutes"
    ritual = True
    magic_school = "Divination"
    classes = ('Bard', 'Cleric', 'Druid', 'Paladin', 'Ranger', 'Sorcerer', 'Wizard')


class DetectPoisonAndDisease(Spell):
    """For the duration, you can sense the presence and location of poisons, poisonous 
    creatures, and diseases within 30 feet of you. You also identify the kind of 
    poison, poisonous creature, or disease in each case. 
    
    The spell can penetrate 
    most barriers, but is blocked by 1 foot of stone, 1 inch of common metal, a thin
     sheet of lead, or 3 feet of wood or dirt.
    """
    name = "Detect Poison And Disease"
    level = 1
    casting_time = "1 action"
    casting_range = "Self"
    components = ('V', 'S', 'M')
    materials = """A yew leaf"""
    duration = "Concentration, up to 10 minutes"
    ritual = False
    magic_school = "Divination"
    classes = ('Cleric', 'Druid', 'Paladin', 'Ranger')


class DetectThoughts(Spell):
    """For the duration, you can read the thoughts of certain creatures. 
    When you cast
     the spell and as your action on each turn until the spell ends, you can focus 
    your mind on any one creature that you can see within 30 feet of you. If the 
    creature you choose has an Intelligence of 3 or lower or doesn’t speak any 
    language, the creature is unaffected. 
    
    You initially learn the surface thoughts
     of the creature—what is most on its mind in that moment. As an action, you can 
    either shift your attention to another creature’s thoughts or attempt to probe 
    deeper into the same creature’s mind. If you probe deeper, the target must make 
    a W isdom saving throw. If it fails, you gain insight into its reasoning (if 
    any), its emotional state, and something that loom s large in its mind (such as 
    something it worries over, loves, or hates). If it succeeds, the spell ends. 
    Either way, the target knows that you are probing into its mind, and unless you 
    shift your attention to another creature’s thoughts, the creature can use its 
    action on its turn to make an Intelligence check contested by your Intelligence 
    check; if it succeeds, the spell ends. 
    
    Questions verbally directed at the 
    target creature naturally shape the course of its thoughts, so this spell is 
    particularly effective as part of an interrogation. 
    
    You can also use this 
    spell to detect the presence of thinking creatures you can’t see. When you cast 
    the spell or as your action during the duration, you can search for thoughts 
    within 30 feet of you. The spell can penetrate barriers, but 2 feet of rock, 2 
    inches of any metal other than lead, or a thin sheet of lead blocks you. You 
    can’t detect a creature with an Intelligence of 3 or lower or one that doesn’t 
    speak any language. 
    
    Once you detect the presence of a creature in this way, 
    you can read its thoughts for the rest of the duration as described above, even 
    if you can’t see it, but it must still be within range.
    """
    name = "Detect Thoughts"
    level = 2
    casting_time = "1 action"
    casting_range = "Self"
    components = ('V', 'S', 'M')
    materials = """A copper piece"""
    duration = "Concentration, up to 1 minute"
    ritual = False
    magic_school = "Divination"
    classes = ('Bard', 'Sorcerer', 'Wizard')


class DimensionDoor(Spell):
    """You teleport yourself from your current location to any other spot within range.
     You arrive at exactly the spot desired. It can be a place you can see, one you 
    can visualize, or one you can describe by stating distance and direction, such 
    as "200 feet straight downward" or "upward to the northwest at a 45-degree 
    angle, 300 feet". 
    
    You can bring along objects as long as their weight doesn’t
     exceed what you can carry. You can also bring one willing creature of your size
     or smaller who is carrying gear up to its carrying capacity. The creature must 
    be within 5 feet of you when you cast this spell. 
    
    If you would arrive in a 
    place already occupied by an object or a creature, you and any creature 
    traveling with you each take 4d6 force damage, and the spell fails to teleport 
    you.
    """
    name = "Dimension Door"
    level = 4
    casting_time = "1 action"
    casting_range = "500 feet"
    components = ('V',)
    materials = """"""
    duration = "Instantaneous"
    ritual = False
    magic_school = "Conjuration"
    classes = ('Bard', 'Sorcerer', 'Warlock', 'Wizard')


class DisguiseSelf(Spell):
    """You make yourself – including your clothing, armor, weapons, and other 
    belongings on your person – look different until the spell ends or until you 
    use your action to dismiss it. 
    You can seem  1 foot shorter or taller and can 
    appear thin, fat, or in between. You can’t change your body type, so you must 
    adopt a form that has the same basic arrangement of limbs. Otherwise, the extent
     of the illusion is up to you. 
    
    The changes wrought by this spell fail to hold 
    up to physical inspection. For example, if you use this spell to add a hat to 
    your outfit, objects pass through the hat, and anyone who touches it would feel 
    nothing or would feel your head and hair. If you use this spell to appear 
    thinner than you are, the hand of som eone who reaches out to touch you would 
    bump into you while it was seemingly still in midair. To discern that you are 
    disguised, a creature can use its action to inspect your appearance and must 
    succeed on an Intelligence (Investigation) check against your spell save DC.
    """
    name = "Disguise Self"
    level = 1
    casting_time = "1 action"
    casting_range = "Self"
    components = ('V', 'S')
    materials = """"""
    duration = "1 hour"
    ritual = False
    magic_school = "Illusion"
    classes = ('Bard', 'Sorcerer', 'Wizard')


class Disintegrate(Spell):
    """A thin green ray springs from your pointing finger to a target that you can see 
    within range. 
    The target can be a creature, an object, or a creation of magical
     force, such as the wall created by wall of force. 
    
    A creature targeted by this
     spell must make a Dexterity saving throw. On a failed save, the target takes 
    10d6 + 40 force damage. If this damage reduces the target to 0 hit points, it is
     disintegrated. 
    
    A disintegrated creature and everything it is wearing and 
    carrying, except magic items, are reduced to a pile of fine gray dust. The 
    creature can be restored to life only by means of a true resurrection or a wish 
    spell. 
    
    This spell automatically disintegrates a Large or smaller nonmagical 
    object or a creation of magical force. If the target is a Huge or larger object 
    or creation of force, this spell disintegrates a 10-foot-cube portion of it. A 
    magic item is unaffected by this spell.
    
    At Higher Levels: When you cast this 
    spell using a spell slot of 7th level or higher, the damage increases by 3d6 for
     each slot level above 6th.
    """
    name = "Disintegrate"
    level = 6
    casting_time = "1 action"
    casting_range = "60 feet"
    components = ('V', 'S', 'M')
    materials = """A lodestone and a pinch of dust"""
    duration = "Instantaneous"
    ritual = False
    magic_school = "Transmutation"
    classes = ('Sorcerer', 'Wizard')


class DispelEvilAndGood(Spell):
    """Shimmering energy surrounds and protects you from fey, undead, and creatures 
    originating from beyond the Material Plane. For the duration, celestials, 
    elementals, fey, fiends, and undead have disadvantage on attack rolls against 
    you. 
    
    You can end the spell early by using either of the following special 
    functions. 
    
    Break  Enchantment 
    As your action, you touch a creature you can 
    reach that is charmed, frightened, or possessed by a celestial, an elemental, a 
    fey, a fiend, or an undead. The creature you touch is no longer charmed, 
    frightened, or possessed by such creatures. 
    
    Dismissal 
    As your action, make a 
    melee spell attack against a celestial, an elemental, a fey, a fiend, or an 
    undead you can reach. On a hit, you attempt to drive the creature back to its 
    home plane. The creature must succeed on a Charisma saving throw or be sent back
     to its home plane (if it isn’t there already). If they aren’t on their home 
    plane, undead are sent to the Shadowfell, and fey are sent to the Feywild.
    """
    name = "Dispel Evil And Good"
    level = 5
    casting_time = "1 action"
    casting_range = "Self"
    components = ('V', 'S', 'M')
    materials = """Holy water or powdered silver and iron"""
    duration = "Concentration, up to 1 minute"
    ritual = False
    magic_school = "Abjuration"
    classes = ('Cleric', 'Paladin')


class DispelMagic(Spell):
    """Choose any creature, object, or magical effect within range. Any spell of 3rd 
    level or lower on the target ends. For each spell of 4th level or higher on the 
    target, make an ability check using your spellcasting ability. The DC equals 10 
    + the spell’s level. On a successful check, the spell ends.
    
    At Higher Levels: 
    When you cast this spell using a spell slot of 4th level or higher, you 
    automatically end the effects of a spell on the target if the spell’s level is 
    equal to or less than the level of the spell slot you used.
    """
    name = "Dispel Magic"
    level = 3
    casting_time = "1 action"
    casting_range = "120 feet"
    components = ('V', 'S')
    materials = """"""
    duration = "Instantaneous"
    ritual = False
    magic_school = "Abjuration"
    classes = ('Bard', 'Cleric', 'Druid', 'Paladin', 'Sorcerer', 'Warlock', 'Wizard')


class DissonantWhispers(Spell):
    """You whisper a discordant melody that only one creature of your choice within 
    range can hear, wracking it with terrible pain. 
    The target must make a Wisdom 
    saving throw. On a failed save, it takes 3d6 psychic damage and must immediately
     use its reaction , if available, to move as far as its speed allows away from 
    you. The creature doesn’t move into obviously dangerous ground, such as a fire 
    or a pit. On a successful save, the target takes half as much damage and doesn’t
     have to move away. A deafened creature automatically succeeds on the save.
    
    At 
    Higher Levels: When you cast this spell using a spell slot of 2nd level or 
    higher, the damage increases by 1d6 for each slot level above 1st
    """
    name = "Dissonant Whispers"
    level = 1
    casting_time = "1 action"
    casting_range = "60 feet"
    components = ('V',)
    materials = """"""
    duration = "Instantaneous"
    ritual = False
    magic_school = "Enchantment"
    classes = ('Bard',)


class Divination(Spell):
    """Your magic and an offering put you in contact with a god or a god’s servants. 
    You ask a single question concerning a specific goal, event, or activity to 
    occur within 7 days. The DM offers a truthful reply. The reply might be a short 
    phrase, a cryptic rhyme, or an omen. 
    
    The spell doesn’t take into account any 
    possible circumstances that might change the outcome, such as the casting of 
    additional spells or the loss or gain of a companion. 
    
    If you cast this spell 
    two or more times before finishing your next long rest, there is a cumulative 25
     percent chance for each casting after the first that you get a random reading. 
    The DM makes this roll in secret.
    """
    name = "Divination"
    level = 4
    casting_time = "1 action"
    casting_range = "Self"
    components = ('V', 'S', 'M')
    materials = """Incense and a sacrificial offering appropriate to your religion, together worth at least 25 gp, which the spell consumes"""
    duration = "Instantaneous"
    ritual = True
    magic_school = "Divination"
    classes = ('Cleric',)


class DivineFavor(Spell):
    """Your prayer empowers you with divine radiance. Until the spell ends, your weapon
     attacks deal and extra 1d4 radiant damage on a hit.
    """
    name = "Divine Favor"
    level = 1
    casting_time = "1 bonus action"
    casting_range = "Self"
    components = ('V', 'S')
    materials = """"""
    duration = "Concentration, up to 1 minute"
    ritual = False
    magic_school = "Evocation"
    classes = ('Paladin',)


class DivineWord(Spell):
    """You utter a divine word, imbued with the power that shaped the world at the dawn
     of creation. 
    Choose any number of creatures you can see within range. Each 
    creature that can hear you must make a Charisma saving throw. On a failed save, 
    a creature suffers an effect based on its current hit points: 
    
     •  50 hit 
    points or fewer: deafened for 1 minute 
     •  40 hit points or fewer: deafened and
     blinded for 10 minutes 
     •  30 hit points or fewer: blinded, deafened, and 
    stunned for 1 hour 
     •  20 hit points or fewer: killed instantly 
    
    Regardless of
     its current hit points, a celestial, an elemental, a fey, or a fiend that fails
     its save is forced back to its plane of origin (if it isn’t there already) and 
    can’t return to your current plane for 24 hours by any means short of a wish 
    spell.
    """
    name = "Divine Word"
    level = 7
    casting_time = "1 bonus action"
    casting_range = "30 feet"
    components = ('V',)
    materials = """"""
    duration = "Instantaneous"
    ritual = False
    magic_school = "Evocation"
    classes = ('Cleric',)


class DominateBeast(Spell):
    """You attempt to beguile a beast that you can see within range. 
    It must succeed 
    on a W isdom saving throw or be charmed by you for the duration. If you or 
    creatures that are friendly to you are fighting it, it has advantage on the 
    saving throw. 
    
    While the beast is charmed, you have a telepathic link with it 
    as long as the two of you are on the same plane of existence. You can use this 
    telepathic link to issue commands to the creature while you are conscious (no 
    action required), which it does its best to obey. You can specify a simple and 
    general course of action, such as “Attack that creature,” “Run over there,” or 
    “Fetch that object.” If the creature completes the order and doesn’t receive 
    further direction from you, it defends and preserves itself to the best of its 
    ability. 
    
    You can use your action to take total and precise control of the 
    target. Until the end of your next turn, the creature takes only the actions you
     choose, and doesn’t do anything that you don’t allow it to do. During this 
    time, you can also cause the creature to use a reaction, but this requires you 
    to use your own reaction as well. 
    
    Each time the target takes damage, it makes 
    a new Wisdom saving throw against the spell. If the saving throw succeeds, the 
    spell ends.
    
    At Higher Levels: When you cast this spell with a 5th-level spell 
    slot, the duration is concentration, up to 10 minutes. 
    When you use a 6th-
    level spell slot, the duration is concentration, up to 1 hour. 
    When you use a 
    spell slot of 7th level or higher, the duration is concentration, up to 8 hours
    """
    name = "Dominate Beast"
    level = 4
    casting_time = "1 action"
    casting_range = "60 feet"
    components = ('V', 'S')
    materials = """"""
    duration = "Concentration, up to 1 minute"
    ritual = False
    magic_school = "Enchantment"
    classes = ('Druid', 'Sorcerer')


class DominateMonster(Spell):
    """You attempt to beguile a creature that you can see within range. 
    It must 
    succeed on a Wisdom saving throw or be charmed by you for the duration. If you 
    or creatures that are friendly to you are fighting it, it has advantage on the 
    saving throw. 
    
    While the creature is charmed, you have a telepathic link with 
    it as long as the two of you are on the same plane of existence. You can use 
    this telepathic link to issue commands to the creature while you are conscious 
    (no action required), which it does its best to obey. You can specify a simple 
    and general course of action, such as "Attack that creature", "Run over 
    there", or "Fetch that object". If the creature completes the order and 
    doesn’t receive further direction from you, it defends and preserves itself to 
    the best of its ability. 
    
    You can use your action to take total and precise 
    control of the target. Until the end of your next turn, the creature takes only 
    the actions you choose, and doesn’t do anything that you don’t allow it to do. 
    During this time, you can also cause the creature to use a reaction, but this 
    requires you to use your own reaction as well. 
    
    Each time the target takes 
    damage, it makes a new Wisdom saving throw against the spell. If the saving 
    throw succeeds, the spell ends.
    
    At Higher Levels: When you cast this spell with
     a 9th-level spell slot, the duration is concentration, up to 8 hours.
    """
    name = "Dominate Monster"
    level = 8
    casting_time = "1 action"
    casting_range = "60 feet"
    components = ('V', 'S')
    materials = """"""
    duration = "Concentration, up to 1 hour"
    ritual = False
    magic_school = "Enchantment"
    classes = ('Bard', 'Sorcerer', 'Warlock', 'Wizard')


class DominatePerson(Spell):
    """You attempt to beguile a humanoid that you can see within range. 
    It must 
    succeed on a Wisdom saving throw or be charmed by you for the duration. If you 
    or creatures that are friendly to you are fighting it, it has advantage on the 
    saving throw. 
    
    While the target is charmed, you have a telepathic link with it 
    as long as the two of you are on the same plane of existence. You can use this 
    telepathic link to issue commands to the creature while you are conscious (no 
    action required), which it does its best to obey. You can specify a simple and 
    general course of action, such as "Attack that creature", "Run over there", 
    or "Fetch that object". If the creature completes the order and doesn’t 
    receive further direction from you, it defends and preserves itself to the best 
    of its ability. 
    
    You can use your action to take total and precise control of 
    the target. Until the end of your next turn, the creature takes only the actions
     you choose, and doesn’t do anything that you don’t allow it to do. During this 
    time you can also cause the creature to use a reaction, but this requires you to
     use your own reaction as well. 
    
    Each time the target takes damage, it makes a 
    new Wisdom saving throw against the spell. If the saving throw succeeds, the 
    spell ends.
    
    At Higher Levels: When you cast this spell using a 6th-level spell 
    slot, the duration is concentration, up to 10 minutes. 
    When you use a 7th-
    level spell slot, the duration is concentration, up to 1 hour. 
    When you use a 
    spell slot of 8th level or higher, the duration is concentration, up to 8 hours.
    """
    name = "Dominate Person"
    level = 5
    casting_time = "1 action"
    casting_range = "60 feet"
    components = ('V', 'S')
    materials = """"""
    duration = "Concentration, up to 1 minute"
    ritual = False
    magic_school = "Enchantment"
    classes = ('Bard', 'Sorcerer', 'Wizard')


class DragonsBreath(Spell):
    """You touch one willing creature and imbue it with the power to spew magical 
    energy from its mouth, provided it has one. Choose acid, cold, fire, lightning, 
    or poison. Until the spell ends, the creature can use an action to exhale energy
     of the chosen type in a 15-foot cone. Each creature in that area must make a 
    Dexterity saving throw, taking 3d6 damage of the chosen type on a failed save, 
    or half as much damage on a successful one.
    
    At Higher Levels: When you cast 
    this spell using a spell slot of 3rd level or higher, the damage increases by 
    1d6 for each slot level above 2nd.
    """
    name = "Dragons Breath"
    level = 2
    casting_time = "1 bonus action"
    casting_range = "Touch"
    components = ('V', 'S', 'M')
    materials = """A hot pepper"""
    duration = "Concentration, up to 1 minute"
    ritual = False
    magic_school = "Transmutation"
    classes = ('Sorcerer', 'Wizard')


class DrawmijsInstantSummons(Spell):
    """You touch an object weighing 10 pounds or less whose longest dimension is 6 feet
     or less. 
    The spell leaves an invisible mark on its surface and invisibly 
    inscribes the name of the item on the sapphire you use as the material 
    component. Each time you cast this spell, you must use a different sapphire. 
    
    
    At any time thereafter, you can use your action to speak the item’s name and 
    crush the sapphire. The item instantly appears in your hand regardless of 
    physical or planar distances, and the spell ends. If another creature is holding
     or carrying the item, crushing the sapphire doesn’t transport the item to you, 
    but instead you learn who the creature possessing the object is and roughly 
    where that creature is located at that moment. 
    
    Dispel magic or a similar 
    effect successfully applied to the sapphire ends this spell’s effect.
    """
    name = "Drawmijs Instant Summons"
    level = 6
    casting_time = "1 minute"
    casting_range = "Touch"
    components = ('V', 'S', 'M')
    materials = """A sapphire worth 1,000 gp"""
    duration = "Until dispelled"
    ritual = True
    magic_school = "Conjuration"
    classes = ('Wizard',)


class Dream(Spell):
    """This spell shapes a creature's dreams. Choose a creature known to you 
    as the target of this spell. The target must be on the same plane of 
    existence as you. Creatures that don't sleep, such as elves, can't be 
    contacted by this spell. You, or a willing creature you touch, enters 
    a trance state, acting as a messenger. While in the trance, the 
    messenger is aware of his or her surroundings, but can't take actions 
    or move.
    
    If the target is asleep, the messenger appears in the 
    target's dreams and can converse with the target as long as it remains
     asleep, through the duration of the spell. The messenger can also 
    shape the environment of the dream, creating landscapes, objects, and 
    other images. The messenger can emerge from the trance at any time, 
    ending the effect of the spell early. The target recalls the dream 
    perfectly upon waking. If the target is awake when you cast the spell,
     the messenger knows it, and can either end the trance (and the spell)
     or wait for the target to fall asleep, at which point the messenger 
    appears in the target's dreams.
    
    You can make the messenger appear 
    monstrous and terrifying to the target. If you do, the messenger can 
    deliver a message of no more than ten words and then the target must 
    make a Wisdom saving throw. On a failed save, echoes of the phantasmal
     monstrosity spawn a nightmare that lasts the duration of the target's
     sleep and prevents the target from gaining any benefit from that 
    rest. In addition, when the target wakes up, it takes 3d6 psychic 
    damage.
    
    If you have a body part, lock of hair, clipping from a nail, 
    or similar portion of the target's body, the target makes its saving 
    throw with disadvantage.
    """
    name = "Dream"
    level = 5
    casting_time = "1 minute"
    casting_range = "Special"
    components = ('V', 'S', 'M')
    materials = """A handful of sand, a dab of ink, and a writing quill plucked from a 
sleeping bird"""
    duration = "8 hours"
    ritual = False
    magic_school = "Illusion"
    classes = ('Bard', 'Druid', 'Warlock', 'Wizard')


class DruidGrove(Spell):
    """You invoke the spirits of nature to protect an area outdoors or underground. The
     area can be as small as a 30—foot cube or as large as a 90-foot cube. Buildings
     and other structures are excluded from the affected area. If you cast this 
    spell in the same area every day for a year, the spell lasts until dispelled. 
    The spell creates the following effects within the area. When you cast this 
    spell, you can specify creatures as friends who are immune to the effects. You 
    can also specify a password that, when spoken aloud, makes the speaker immune to
     these effects. The entire warded area radiates magic. A dispel magic cast on 
    the area, if successful, removes only one of the following effects, not the 
    entire area. That spell’s caster chooses which effect to end. Only when all its 
    effects are gone is this spell dispelled.
    Solid Fog. You can fill any number of 
    5-foot squares on the ground with thick fog, making them heavily obscured. The 
    fog reaches 10 feet high. In addition, every foot of movement through the fog 
    costs 2 extra feet. To a creature immune to this effect, the fog obscures 
    nothing and looks like soft mist, with motes of green light floating in the air.
    
    Grasping Undergrowth. You can fill any number of 5-foot squares on the ground 
    that aren’t filled with fog with grasping weeds and vines, as if they were 
    affected by an entangle spell. To a creature immune to this effect, the weeds 
    and vines feel soft and reshape themselves to serve as temporary seats or beds.
    
    Grove Guardians. You can animate up to four trees in the area, causing them to 
    uproot themselves from the ground. These trees have the same statistics as an 
    awakened tree, which appears in the Monster Manual, except they can’t speak, and
     their bark is covered with druidic symbols. If any creature not immune to this 
    effect enters the warded area, the grove guardians fight until they have driven 
    off or slain the intruders. The grove guardians also obey your spoken commands 
    (no action required by you) that you issue while in the area. Ifyou don't give 
    them commands and no intruders are present, the grove guardians do nothing. The 
    grove guardians can‘t leave the warded area. When the spell ends, the magic 
    animating them disappears, and the trees take root again if possible.
    Additional
     Spell Effect. You can place your choice of one of the following magical effects
     within the warded area: 
    - A constant gust of Wind in two locations of your 
    choice
    - Spike growth in one location of your choice
    - Wind wall in two 
    locations of your choice
    To a creature immune to this effect, the winds are a 
    fragrant, gentle breeze, and the area of spike growth is harmless.
    """
    name = "Druid Grove"
    level = 6
    casting_time = "10 minutes"
    casting_range = "Touch"
    components = ('V', 'S', 'M')
    materials = """Mistletoe, which the spell consumes, that was harvested with a golden sickle under the light of a full moon"""
    duration = "24 hours"
    ritual = False
    magic_school = "Abjuration"
    classes = ('Druid',)


class Druidcraft(Spell):
    """Whispering to the spirits of nature, you create one of the following effects 
    within range: 
    
    • You create a tiny, harmless sensory effect that predicts what 
    the weather will be at your location for the next 24 hours. The effect might 
    manifest as a golden orb  for clear skies, a cloud for rain, falling snowflakes 
    for snow, and so on. This effect persists for 1 round. 
    • You instantly make a 
    flower blossom, a seed pod open, or a leaf bud bloom. 
    • You create an 
    instantaneous, harmless sensory effect, such as falling leaves, a puff of wind, 
    the sound of a small animal, or the faint odor of skunk. The effect  must fit in
     a 5-foot cube. 
    • You instantly light or snuff out a candle, a torch, or a 
    small campfire.
    """
    name = "Druidcraft"
    level = 0
    casting_time = "1 action"
    casting_range = "30 feet"
    components = ('V', 'S')
    materials = """"""
    duration = "Instantaneous"
    ritual = False
    magic_school = "Transmutation"
    classes = ('Druid',)


class DustDevil(Spell):
    """(a pinch of dust)
    Choose an unoccupied 5-foot cube of air that you can see 
    within range. An elemental force that resembles a dust devil appears in the cube
     and lasts for the spell’s duration.
    Any creature that ends its turn within 5 
    feet of the dust devil must make a Strength saving throw. On a failed save, the 
    creature takes 1d8 bludgeoning damage and is pushed 10 feet away. On a 
    successful save, the creature takes half as much damage and isn’t pushed.
    As a 
    bonus action, you can move the dust devil up to 30 feet in any direction. If the
     dust devil moves over sand, dust, loose dirt, or small gravel, it sucks up the 
    material and forms a 10-foot-radius cloud of debris around itself that lasts 
    until the start of your next turn. The cloud heavily obscures its area.
    At 
    Higher Levels. When you cast this spell using a spell slot of 3rd level or 
    higher, the damage increases by 1d8 for each slot level above 2nd.
    """
    name = "Dust Devil"
    level = 2
    casting_time = "1 action"
    casting_range = "60 feet"
    components = ('V', 'S', 'M')
    materials = """"""
    duration = "Instantaneous"
    ritual = False
    magic_school = "Conjuration"
    classes = ('Druid', 'Sorcerer', 'Wizard')


