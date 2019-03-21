from .spells import Spell


class CallLightning(Spell):
    """A storm cloud appears in the shape of a cylinder that is 10 feet tall with a 
    60-foot radius, centered on a point you can see 100 feet directly above you. The
     spell fails if you can’t see a point in the air where the storm cloud could 
    appear (for example, if you are in a room that can’t accommodate the cloud). 
    
    
    When you cast the spell, choose a point you can see within range. A bolt of 
    lightning flashes down from the cloud to that point. Each creature within 5 feet
     of that point must make a Dexterity saving throw. A creature takes 3d10 
    lightning damage on a failed save, or half as much damage on a successful one. 
    On each of your turns until the spell ends, you can use your action to call down
     lightning in this way again, targeting the same point or a different one. 
    
    If 
    you are outdoors in stormy conditions when you cast this spell, the spell gives 
    you control over the existing storm instead of creating a new one. Under such 
    conditions, the spell’s damage increases by 1d10.
    
    At Higher Levels: When you 
    cast this spell using a spell slot of 4th or higher level, the damage increases 
    by 1d10 for each slot level above 3rd.
    """
    name = "Call Lightning"
    level = 3
    casting_time = "1 action"
    casting_range = "120 feet"
    components = ('V', 'S')
    materials = """"""
    duration = "Concentration, up to 10 minutes"
    ritual = False
    magic_school = "Conjuration"
    classes = ('Druid',)


class CalmEmotions(Spell):
    """You attempt to suppress strong emotions in a group of people. 
    Each humanoid in 
    a 20-foot-radius sphere centered on a point you choose within range must make a 
    Charisma saving throw; a creature can choose to fail this saving throw if it 
    wishes. If a creature fails its saving throw, choose one of the following two 
    effects. You can suppress any effect causing a target to be charmed or 
    frightened. When this spell ends, any suppressed effect resumes, provided that 
    its duration has not expired in the meantime. 
    
    Alternatively, you can make a 
    target indifferent about creatures of your choice that it is hostile toward. 
    This indifference ends if the target is attacked or harmed by a spell or if it 
    witnesses any of its friends being harmed. When the spell ends, the creature 
    becomes hostile again, unless the DM rules otherwise.
    """
    name = "Calm Emotions"
    level = 2
    casting_time = "1 action"
    casting_range = "60 feet"
    components = ('V', 'S')
    materials = """"""
    duration = "Concentration, up to 1 minute"
    ritual = False
    magic_school = "Enchantment"
    classes = ('Bard', 'Cleric')


class Catapult(Spell):
    """Choose one object weighing 1 to 5 pounds within range that isn’t being worn or 
    carried. The object flies in a straight line up to 90 feet in a direction you 
    choose before falling to the ground, stopping early if it impacts against a 
    solid surface. If the object would strike a creature, that creature must make a 
    Dexterity saving throw. On a failed save, the object strikes the target and 
    stops moving. In either case, both the object and the creature or solid surface 
    take 3d8 bludgeoning damage.
    At Higher Levels. When you cast this spell using a 
    spell slot of 2nd level or higher, the maximum weight of objects that you can 
    target with this spell increases by 5 pounds, and the damage increases by 1d8, 
    for each slot level above 1st.
    """
    name = "Catapult"
    level = 1
    casting_time = "1 action"
    casting_range = "150 feet"
    components = ('S',)
    materials = """"""
    duration = "Instantaneous"
    ritual = False
    magic_school = "Transmutation"
    classes = ('Sorcerer', 'Wizard')


class Catnap(Spell):
    """You make a calming gesture, and up to three willing creatures of your choice 
    that you can see within range fall unconscious for the spell’s duration. The 
    spell ends on a target early if it takes damage or someone uses an action to 
    shake or slap it awake. If a target remains unconscious for the full duration, 
    that target gains the benefit of a short rest, and it can’t be affected by this 
    spell again until it finishes a long rest.
    
    At Higher Levels: When you cast this
     spell using a spell slot of 4th level or higher, you can target one additional 
    willing creature for each slot level above 3rd.
    """
    name = "Catnap"
    level = 3
    casting_time = "1 action"
    casting_range = "30 feet"
    components = ('S', 'M')
    materials = """A pinch of sand"""
    duration = "10 minutes"
    ritual = False
    magic_school = "Enchantment"
    classes = ('Wizard', 'Bard', 'Sorcerer')


class CauseFear(Spell):
    """You awaken the sense of mortality in one creature you can see within range. A 
    construct or an undead is immune to this effect. The target must succeed on a 
    Wisdom saving throw or become frightened of you until the spell ends. The 
    frightened target can repeat the saving throw at the end of each of its turns, 
    ending the effect on itself on a success.
    
    At Higher Levels: When you cast this 
    spell using a spell slot of 2nd level or higher, you can target one additional 
    creature for each slot level above lst. The creatures must be within 30 feet of 
    each other when you target them.
    """
    name = "Cause Fear"
    level = 1
    casting_time = "1 action"
    casting_range = "60 feet"
    components = ('V',)
    materials = """"""
    duration = "Concentration, up to 1 minute"
    ritual = False
    magic_school = "Necromancy"
    classes = ('Warlock', 'Wizard')


class Ceremony(Spell):
    """You perform a special religious ceremony that is infused with magic. When you 
    cast the spell, choose one of the following rites, the target of which must be 
    within 10 feet of you throughout the casting.
    Atonement. You touch one willing 
    creature whose alignment has changed, and you make a DC 20 Wisdom (Insight) 
    check. On a successful check, you restore the target to its original alignment.
    
    Bless Water. You touch one vial of water and cause it to become holy water.
    
    Coming of Age. You touch one humanoid who is a young adult. For the next 24 
    hours, whenever the target makes an ability check, it can roll a d4 and add the 
    number rolled to the ability check. A creature can benefit from this rite only 
    once.
    Dedication. You touch one humanoid who wishes to be dedicated to your 
    god’s service. For the next 24 hours, whenever the target makes a saving throw, 
    it can roll a d4 and add the number rolled to the save. A creature can benefit 
    from this rite only once.
    Funeral Rite. You touch one corpse, and for the next 7
     days, the target can’t become undead by any means short of a wish spell.
    
    Wedding. You touch adult humanoids willing to be bonded together in marriage. 
    For the next 7 days, each target gains a +2 bonus to AC while they are within 30
     feet of each other. A creature can benefit from this rite again only if 
    widowed.
    """
    name = "Ceremony"
    level = 1
    casting_time = "1 hour"
    casting_range = "Touch"
    components = ('V', 'S', 'M')
    materials = """25 gp worth of powdered silver,which the spell consumes"""
    duration = "Instantaneous"
    ritual = True
    magic_school = "Abjuration"
    classes = ('Cleric', 'Paladin')


class ChainLightning(Spell):
    """You create a bolt of lightning that arcs toward a target of your choice that you
     can see within range. Three bolts then leap from that target to as many as 
    three other targets, each of which must be within 30 feet of the first target. A
     target can be a creature or an object and can be targeted by only one of the 
    bolts. 
    
    A target must make a Dexterity saving throw. The target takes 10d8 
    lightning damage on a failed save, or half as much on a successful one.
    
    At 
    Higher Levels: When you cast this spell using a spell slot of 7th level or 
    higher, one additional bolt leaps from the first target to another target for 
    each slot level above 6th.
    """
    name = "Chain Lightning"
    level = 6
    casting_time = "1 action"
    casting_range = "150 feet"
    components = ('V', 'S', 'M')
    materials = """A bit of fur; a piece of amber, glass, or a crystal rod; and three silver pins"""
    duration = "Instantaneous"
    ritual = False
    magic_school = "Evocation"
    classes = ('Sorcerer', 'Wizard')


class ChaosBolt(Spell):
    """You hurl an undulating, warbling mass of chaotic energy at one creature in 
    range. Make a ranged spell attack against the target. On a hit, the target takes
     2d8 + 1d6 damage. Choose one of the dSs. The number rolled on that die 
    determines the attacks damage type, as shown below.
    d8 / Damage Type
    1 / Acid
    2 
    / Cold
    3 / Fire
    4 / Force
    5 / Lightning
    6 / Poison
    7 / Psychic
    8 / Thunder
    If 
    you roll the same number on both d8s, the chaotic energy leaps from the target 
    to a different creature of your choice within 30 feet of it. Make a new attack 
    roll against the new target, and make a new damage roll, which could cause the 
    chaotic energy to leap again. A creature can be targeted only once by each 
    casting of this spell.
    
    At Higher Levels: When you cast this spell using a spell
     slot of 2nd level or higher, each target takes 1d6 extra damage of the type 
    rolled for each slot level above 1st.
    """
    name = "Chaos Bolt"
    level = 1
    casting_time = "1 action"
    casting_range = "120 feet"
    components = ('V', 'S')
    materials = """"""
    duration = "Instantaneous"
    ritual = False
    magic_school = "Evocation"
    classes = ('Sorcerer',)


class CharmMonster(Spell):
    """You attempt to charm a creature you can see within range. It must make a Wisdom 
    saving throw, and it does so with advantage if you or your companions are 
    fighting it. If it fails the saving throw, it is charmed by you until the spell 
    ends or until you or your companions do anything harmful to it. The charmed 
    creature is friendly to you. When the spell ends, the creature knows it was 
    charmed by you.
    
    At Higher Levels: When you cast this spell using a spell slot 
    of 5th level or higher, you can target one additional creature for each slot 
    level above 4th. The creatures must be within 30 feet of each other when you 
    target them.
    """
    name = "Charm Monster"
    level = 4
    casting_time = "1 action"
    casting_range = "30 feet"
    components = ('V', 'S')
    materials = """"""
    duration = "1 hour"
    ritual = False
    magic_school = "Enchantment"
    classes = ('Bard', 'Druid', 'Sorcerer', 'Warlock', 'Wizard')


class CharmPerson(Spell):
    """You attempt to charm a humanoid you can see within range. 
    It must make a Wisdom
     saving throw, and does so with advantage if you or your companions are fighting
     it. If it fails the saving throw, it is charmed by you until the spell ends or 
    until you  or your companions do anything harmful to it.The charmed creature 
    regards you as a friendly acquaintance. When the spell ends, the creature knows 
    it was charmed by you.
    
    At Higher Levels: When you cast this spell using a spell
     slot of 2nd level or higher, you can target one additional creature for each 
    slot level above 1st. The creatures must be within 30 feet of each other when 
    you target them.
    """
    name = "Charm Person"
    level = 1
    casting_time = "1 action"
    casting_range = "30 feet"
    components = ('V', 'S')
    materials = """"""
    duration = "1 hour"
    ritual = False
    magic_school = "Enchantment"
    classes = ('Bard', 'Druid', 'Sorcerer', 'Warlock', 'Wizard')


class ChillTouch(Spell):
    """You create a ghostly, skeletal hand in the space of a creature within range. 
    
    Make a ranged spell attack against the creature to assail it with the chill of 
    the grave. On a hit, the target takes 1d8 necrotic damage, and it can’t regain 
    hit points until the start of your next turn. Until then, the hand clings to the
     target. If you hit an undead target, it also has disadvantage on attack rolls 
    against you until the end of your next turn.
    
    At Higher Levels: This spell’s 
    damage increases by 1d8 when you reach 5th level (2d8), 11th level (3d8), and 
    17th level (4d8).
    """
    name = "Chill Touch"
    level = 0
    casting_time = "1 action"
    casting_range = "120 feet"
    components = ('V', 'S')
    materials = """"""
    duration = "1 round"
    ritual = False
    magic_school = "Necromancy"
    classes = ('Sorcerer', 'Warlock', 'Wizard')


class ChromaticOrb(Spell):
    """You hurl a 4-inch-diameter sphere of energy at a creature that you can see 
    within range. You choose acid, cold, fire, lightning, poison, or thunder for the
     type of orb you create, and then make a ranged spell attack against the target.
     If the attack hits, the creature takes 3d8 damage of the type you chose.
    
    At 
    Higher Levels: When you cast this spell using a spell slot of 2nd level or 
    higher, the damage increases by 1d8 for each slot level above 1st.
    """
    name = "Chromatic Orb"
    level = 1
    casting_time = "1 action"
    casting_range = "90 feet"
    components = ('V', 'S', 'M')
    materials = """A diamond worth at least 50 gp"""
    duration = "Instantaneous"
    ritual = False
    magic_school = "Evocation"
    classes = ('Sorcerer', 'Wizard')


class CircleOfDeath(Spell):
    """A sphere of negative energy ripples out in a 60-foot-radius sphere from a point 
    within range. Each creature in that area must make a Constitution saving throw. 
    A target takes 8d6 necrotic damage on a failed save, or half as much damage on a
     successful one.
    
    At Higher Levels: W hen you cast this spell using a spell slot
     of 7th level or higher, the damage increases by 2d6 for each slot level above 
    6th.
    """
    name = "Circle Of Death"
    level = 6
    casting_time = "1 action"
    casting_range = "150 feet"
    components = ('V', 'S', 'M')
    materials = """The powder of a crushed black pearl worth at least 500 gp"""
    duration = "Instantaneous"
    ritual = False
    magic_school = "Necromancy"
    classes = ('Sorcerer', 'Warlock', 'Wizard')


class CircleOfPower(Spell):
    """Divine energy radiates from you, distorting and diffusing magical energy within 
    30 feet of you. 
    Until the spell ends, the sphere moves with you, centered on 
    you. For the duration, each friendly creature in the area (including you) has 
    advantage on saving throws against spells and other magical effects. 
    
    
    Additionally, when an affected creature succeeds on a saving throw made against 
    a spell or magical effect that allows it to make a saving throw to take only 
    half damage, it instead takes no damage if it succeeds on the saving throws.
    """
    name = "Circle Of Power"
    level = 5
    casting_time = "1 action"
    casting_range = "Self (30-foot radius)"
    components = ('V',)
    materials = """"""
    duration = "Concentration, up to 10 minutes"
    ritual = False
    magic_school = "Abjuration"
    classes = ('Paladin',)


class Clairvoyance(Spell):
    """You create an invisible sensor within range in a location familiar to you (a 
    place you have visited or seen before) or in an obvious location that is 
    unfamiliar to you (such as behind a door, around a corner, or in a grove of 
    trees). The sensor remains in place for the duration, and it can’t be attacked 
    or otherwise interacted with. 
    
    When you cast the spell, you choose seeing or 
    hearing. You can use the chosen sense through the sensor as if you were in its 
    space. As your action, you can switch between seeing and hearing. A creature 
    that can see the sensor (such as a creature benefitting from see invisibility or
     truesight) sees a luminous, intangible orb about the size of your fist.
    """
    name = "Clairvoyance"
    level = 3
    casting_time = "10 minutes"
    casting_range = "1 mile"
    components = ('V', 'S', 'M')
    materials = """A focus worth at least 100 gp, either a jeweled horn for hearing or a glass eye for seeing"""
    duration = "Concentration, up to 10 minutes"
    ritual = False
    magic_school = "Divination"
    classes = ('Bard', 'Cleric', 'Sorcerer', 'Wizard')


class Clone(Spell):
    """This spell grows an inert duplicate of a living creature as a safeguard against 
    death. 
    This clone forms inside a sealed vessel and grows to full size and 
    maturity after 120 days; you can also choose to have the clone be a younger 
    version of the same creature. It remains inert and endures indefinitely, as long
     as its vessel remains undisturbed.
    
    
     At any time after the clone matures, if 
    the original creature dies, its soul transfers to the clone, provided that the 
    soul is free and willing to return. The clone is physically identical to the 
    original and has the same personality, memories, and abilities, but none of the 
    original’s equipment. The original creature’s physical remains, if they still 
    exist, becom e inert and can’t thereafter be restored to life, since the 
    creature’s soul is elsewhere.
    """
    name = "Clone"
    level = 8
    casting_time = "1 hour"
    casting_range = "Touch"
    components = ('V', 'S', 'M')
    materials = """A diamond worth at least 1,000 gp and at least 1 cubic inch of flesh of the creature that is to be cloned, which the spell consum es, and a vessel worth at least 2,000 gp that has a sealable lid and is large enough to hold a medium creature, such"""
    duration = "Instantaneous"
    ritual = False
    magic_school = "Necromancy"
    classes = ('Wizard',)


class CloudOfDaggers(Spell):
    """You fill the air with spinning daggers in a cube 5 feet on each side, centered 
    on a point you choose within range. A creature takes 4d4 slashing damage when it
     enters the spell’s area for the first time on a turn or starts its turn there.
    
    
    At Higher Levels: When you cast this spell using a spell slot of 3rd level or 
    higher, the damage increases by 2d4 for each slot level above 2nd.
    """
    name = "Cloud Of Daggers"
    level = 2
    casting_time = "1 action"
    casting_range = "60 feet"
    components = ('V', 'S', 'M')
    materials = """A sliver of glass"""
    duration = "Concentration, up to 1 minute"
    ritual = False
    magic_school = "Conjuration"
    classes = ('Bard', 'Sorcerer', 'Warlock', 'Wizard')


class Cloudkill(Spell):
    """You create a 20-foot-radius sphere of poisonous, yellow-green fog centered on a 
    point you choose within range. The fog spreads around corners. It lasts for the 
    duration or until strong wind dispereses the fog, ending the spell. Its area is 
    heavily obscured. 
    
    When a creature enters the spell’s area for the first time 
    on a turn or starts its turn there, that creature must make a Constitution 
    saving throw. The creature takes 5d8 poison damageon a failed save, or half as 
    much damage on a successful one. Creatures are affected even if they hold their 
    breath or don’t need to breathe. 
    
    The fog moves 10 feet away from you at the 
    start of each of your turns, rolling along the surface of the ground. The 
    vapors, being heavier than air, sink to the lowest level of the land, even 
    pouring down openings.
    
    At Higher Levels: When you cast this spell using a spell
     slot of 6th level or higher, the damage increases by 1d8 for each slot level 
    above 5th.
    """
    name = "Cloudkill"
    level = 5
    casting_time = "1 action"
    casting_range = "120 feet"
    components = ('V', 'S')
    materials = """"""
    duration = "Concentration, up to 10 minutes"
    ritual = False
    magic_school = "Conjuration"
    classes = ('Sorcerer', 'Wizard')


class ColorSpray(Spell):
    """A dazzling array of flashing, colored light springs from your hand. 
    Roll 6d10, 
    the total is how many hit points of creatures this spell can effect. Creatures 
    in a 15-foot cone originating from you are affected in ascending order of their 
    current hit points (ignoring unconscious creatures and creatures that can’t 
    see). 
    
    Starting with the creature that has the lowest current hit points, each 
    creature affected by this spell is blinded until the spell ends. Subtract each 
    creature’s hit points from the total before moving on to the creature with the 
    next lowest hit points. A creature’s hit points must be equal to or less than 
    the remaining total for the creature to be affected.
    
    At Higher Levels: When you
     cast this spell using a spell slot of 2nd level or higher, roll an additional 
    2d10 for each slot level above 1st.
    """
    name = "Color Spray"
    level = 1
    casting_time = "1 action"
    casting_range = "Self (15-foot cone)"
    components = ('V', 'S', 'M')
    materials = """"""
    duration = "1 round"
    ritual = False
    magic_school = "Illusion"
    classes = ('Sorcerer', 'Wizard')


class Command(Spell):
    """You speak a one-word command to a creature you can see within range. 
    The target
     must succeed on a Wisdom saving throw or follow the command on its next turn. 
    The spell has no effect if the target is undead, if it doesn’t understand your 
    language, or if your command is directly harmful to it.  Some typical commands 
    and their effects follow. You might issue a command other than one described 
    here. If you do so, the DM determines how the target behaves. If the target 
    can’t follow your command, the spell ends.
    Approach The target moves toward you 
    by the shortest and most direct route, ending its turn if it moves within 5 feet
     of you.
    Drop The target drops whatever it is holding and then ends its turn.
    
    Flee The target spends its turn moving away from you by the fastest available 
    means.
    Grovel The target falls prone and then ends its turn.
    Halt The target 
    doesn’t move and takes no actions. A flying creature stays aloft, provided that 
    it is able to do so. If it must move to stay aloft, it flies the minimum 
    distance needed to remain in the air.
    
    At Higher Levels: When you cast this 
    spell using a spell slot of 2nd level or higher, you can affect one additional 
    creature for each slot level above 1st. The creatures must be within 30 feet of 
    each other when you target them
    """
    name = "Command"
    level = 1
    casting_time = "1 action"
    casting_range = "60 feet"
    components = ('V',)
    materials = """"""
    duration = "1 round"
    ritual = False
    magic_school = "Enchantment"
    classes = ('Cleric', 'Paladin')


class Commune(Spell):
    """You contact your deity or a divine proxy and ask up to three questions that can 
    be answered with a yes or no. You must ask your questions before the spell ends.
     You receive a correct answer for each question. 
    
    Divine beings aren’t 
    necessarily omniscient, so you might receive “unclear” as an answer if a 
    question pertains to information that lies beyond the deity’s knowledge. In a 
    case where a one-word answer could be misleading or contrary to the deity’s 
    interests, the DM might offer a short phrase as an answer instead. 
    
    If you cast
     the spell two or more times before finishing your next long rest, there is a 
    cumulative 25 percent chance for each casting after the first that you get no 
    answer. The DM makes this roll in secret.
    """
    name = "Commune"
    level = 5
    casting_time = "1 minute"
    casting_range = "Self"
    components = ('V', 'S', 'M')
    materials = """Incense and a vial of holy or unholy water"""
    duration = "1 minute"
    ritual = True
    magic_school = "Divination"
    classes = ('Cleric',)


class CommuneWithNature(Spell):
    """You briefly become one with nature and gain knowledge of the surrounding 
    territory. 
    In the outdoors, the spell gives you knowledge of the land within 3 
    miles of you. In caves and other natural underground settings, the radius is 
    limited to 300 feet. The spell doesn’t function where nature has been replaced 
    by construction, such as in dungeons and towns. 
    
    You instantly gain knowledge 
    of up to three facts of your choice about any of the following subjects as they 
    relate to the area: 
    
    •  terrain and bodies of water 
    •  prevalent plants, 
    minerals, animals, or peoples 
    •  powerful celestials, fey, fiends, elementals, 
    or undead 
    •  influence from other planes of existence 
    •  buildings 
    
    For 
    example, you could determine the location of powerful undead in the area, the 
    location of major sources of safe drinking water, and the location of any nearby
     towns.
    """
    name = "Commune With Nature"
    level = 5
    casting_time = "1 minute"
    casting_range = "Self"
    components = ('V', 'S')
    materials = """"""
    duration = "Instantaneous"
    ritual = True
    magic_school = "Divination"
    classes = ('Druid', 'Ranger')


class CompelledDuel(Spell):
    """You attempt to compel a creature into a duel. 
    One creature that you can see 
    within range must make a Wisdom saving throw. On a failed save, the creature is 
    drawn to you, compelled by your divine demand. For the duration, it has 
    disadvantage on attack rolls against creatures other than you, and must make a 
    Wisdom saving throw each time it attempts to move to a space that is more than 
    30 feet away from you; if it succeeds on this saving throw, this spell doesn’t 
    restrict the target’s movement for that turn. 
    
    The spell ends if you attack any
     other creature, if you cast a spell that targets a hostile creature other than 
    the target, if a creature friendly to you damages the target or casts a harmful 
    spell on it, or if you end your turn more than 30 feet away from the target.
    """
    name = "Compelled Duel"
    level = 1
    casting_time = "1 bonus action"
    casting_range = "30 feet"
    components = ('V',)
    materials = """"""
    duration = "Concentration, up to 1 minute"
    ritual = False
    magic_school = "Enchantment"
    classes = ('Paladin',)


class ComprehendLanguages(Spell):
    """For the duration, you understand the literal meaning of any spoken language that
     you hear. 
    You also understand any spoken language that you hear. You also 
    understand any written language that you see, but you must be touching the 
    surface of which the words are written. It takes about 1 minute to read one page
     of text. 
    
    This spell doesn’t decode secret messages in a text or glyph, such 
    as an arcane sigil, that isn’t part of a written language.
    """
    name = "Comprehend Languages"
    level = 1
    casting_time = "1 action"
    casting_range = "Self"
    components = ('V', 'S', 'M')
    materials = """A pinch of soot and salt"""
    duration = "1 hour"
    ritual = True
    magic_school = "Divination"
    classes = ('Bard', 'Sorcerer', 'Warlock', 'Wizard')


class Compulsion(Spell):
    """Creatures of your choice that you can see within range and that can hear you 
    must make a Wisdom saving throw. 
    A target automatically succeeds on this saving
     throw if it can’t be charmed. On a failed save, a target is affected by this 
    spell. Until the spell ends, you can use a bonus action on each of your turns to
     designate a direction that is horizontal to you. Each affected target must use 
    as much of its movement as possible to move in that direction on its next turn. 
    It can take its action before it moves. After moving in this way, it can make 
    another Wisdom saving throw to try to end the effect. 
    
    A target isn’t compelled
     to move into an obviously deadly hazard, such as a fire pit, but it will 
    provoke opportunity attacks to move in the designated direction.
    """
    name = "Compulsion"
    level = 4
    casting_time = "1 action"
    casting_range = "30 feet"
    components = ('V', 'S')
    materials = """"""
    duration = "Concentration, up to 1 minute"
    ritual = False
    magic_school = "Enchantment"
    classes = ('Bard',)


class ConeOfCold(Spell):
    """A blast of cold air erupts from your hands. 
    Each creature in a 60-foot cone 
    must make a Constitution saving throw. 
    
    A creature takes 8d8 cold damage on a 
    failed save, or half as much damage on a successful one. A creature killed by 
    this spell becomes a frozen statue until it thaws.
    
    At Higher Levels: When you 
    cast this spell using a spell slot of 6th level or higher, the damage increases 
    by 1d8 for each slot level above 5th.
    """
    name = "Cone Of Cold"
    level = 5
    casting_time = "1 action"
    casting_range = "Self (60-foot cone)"
    components = ('V', 'S', 'M')
    materials = """A small crystal or glass cone"""
    duration = "Instantaneous"
    ritual = False
    magic_school = "Evocation"
    classes = ('Sorcerer', 'Wizard')


class Confusion(Spell):
    """This spell assaults and twists creatures’ minds, spawning delusions and 
    provoking uncontrolled actions. Each creature in a 10-foot-radius sphere 
    centered on a point you choose within range must succeed on a Wisdom saving 
    throw when you cast this spell or be affected by it. 
    
    An affected target can’t 
    take reactions and must roll a d10 at the start of each of its turns to 
    determine its behavior for that turn. 
    
    d10   Behavior 
    
     1. The creature uses 
    all its movement to move in a random direction. To determine the direction, roll
     a d8 and assign a direction to each die face. The creature doesn’t take an 
    action this turn. 
     
    2-6. The creature doesn’t move or take actions this turn.
     
    
    7-8. The creature uses its action to make a melee attack against a randomly 
    determined creature within its reach. If there is no creature within its reach, 
    the creature does nothing this turn. 
    
     9-10. The creature can act and move 
    normally. 
    
    At the end of its turns, an affected target can make a Wisdom saving
     throw. It it succeeds, this effect ends for that target.
    
    At Higher Levels: 
    When you cast this spell using a spell slot of 5th level or higher, the radius 
    of the sphere increases by 5 feet for each slot level above 4th
    """
    name = "Confusion"
    level = 4
    casting_time = "1 action"
    casting_range = "90 feet"
    components = ('V', 'S', 'M')
    materials = """Three nut shells"""
    duration = "Concentration, up to 1 minute"
    ritual = False
    magic_school = "Enchantment"
    classes = ('Bard', 'Druid', 'Sorcerer', 'Wizard')


class ConjureAnimals(Spell):
    """You summon fey spirits that take the form of beasts and appear in unoccupied 
    spaces that you can see within range. 
    
    Choose one of the following options for 
    what appears: 
    
    •  One beast of challenge rating 2 or lower 
    •  Two beasts of 
    challenge rating 1  or lower 
    •  Four beasts of challenge rating 1/2 or lower 
    •
      Eight beasts of challenge rating 1/4 or lower 
    
    Each beast is also considered 
    fey, and it disappears when it drops to 0 hit points or when the spell ends. 
    
    
    The summoned creatures are friendly to you and your companions. Roll initiative 
    for the summoned creatures as a group, which has its own turns. They obey any 
    verbal commands that you issue to them (no action required by you). If you don’t
     issue any commands to them, they defend themselves from hostile creatures, but 
    otherwise take no actions. 
    The DM has the creatures’ statistics.
    
    At Higher 
    Levels: When you cast this spell using certain higher-level spell slots, you 
    choose one of the summoning options above, and more creatures appear: 
    
    twice 
    as many with a 5th-level slot
    three times as many with a 7th-level slot 
    four 
    times as many with a 9th-level slot.
    """
    name = "Conjure Animals"
    level = 3
    casting_time = "1 action"
    casting_range = "60 feet"
    components = ('V', 'S')
    materials = """"""
    duration = "Concentration, up to 1 hour"
    ritual = False
    magic_school = "Conjuration"
    classes = ('Druid', 'Ranger')


class ConjureBarrage(Spell):
    """You throw a nonmagical weapon or fire a piece of nonmagical ammunition into the 
    air to create a cone of identical weapons that shoot forward and then disappear.
     Each creature in a 60-foot cone must succeed on a Dexterity saving throw. A 
    creature takes 3d8 damage on a failed save, or half as much damage on a 
    successful one. The damage type is the same as that of the weapon or ammunition 
    used as a component.
    """
    name = "Conjure Barrage"
    level = 3
    casting_time = "1 action"
    casting_range = "Self (60-foot cone)"
    components = ('V', 'S', 'M')
    materials = """One piece of ammunition or a thrown weapon"""
    duration = "Instantaneous"
    ritual = False
    magic_school = "Conjuration"
    classes = ('Ranger',)


class ConjureCelestial(Spell):
    """You summon a celestial of challenge rating 4 or lower, which appears in an 
    unoccupied space that you can see within range. The celestial disappears when it
     drops to 0 hit points or when the spell ends. 
    
    The celestial is friendly to 
    you and your companions for the duration. Roll initiative for the celestial, 
    which has its own turns. It obeys any verbal commands that you issue to it (no 
    action required by you), as long as they don’t violate its alignment. If you 
    don’t issue any commands to the celestial, it defends itself from hostile 
    creatures but otherwise takes no actions 
    The DM has the celestial’s statistics.
    
    
    At Higher Levels: When you cast this spell using a 9th-level spell slot, you 
    summon a celestial of challenge rating 5 or lower.
    """
    name = "Conjure Celestial"
    level = 7
    casting_time = "1 minute"
    casting_range = "90 feet"
    components = ('V', 'S')
    materials = """"""
    duration = "Concentration, up to 1 hour"
    ritual = False
    magic_school = "Conjuration"
    classes = ('Cleric',)


class ConjureElemental(Spell):
    """You call forth an elemental servant. 
    Choose an area of air, earth, fire, or 
    water that fills a 10-foot cube within range. An elemental of challenge rating 5
     or lower appropriate to the area you chose appears in an unoccupied space 
    within 10 feet of it. For example, a fire elemental emerges from a bonfire, and 
    an earth elemental rises up from the ground. The elemental disappears when it 
    drops to 0 hit points or when the spell ends. 
    
    The elemental is friendly to you
     and your companions for the duration. Roll initiative for the elemental, which 
    has its own turns. It obeys any verbal commands that you issue to it (no action 
    required by you). If you don’t issue any commands to the elemental, it defends 
    itself from hostile creatures but otherwise takes no actions. 
    
    If your 
    concentration is broken, the elemental doesn’t disappear. Instead, you lose 
    control of the elemental, it becom es hostile toward you and your companions, 
    and it might attack. An uncontrolled elemental can’t be dismissed by you, and it
     disappears 1 hour after you summoned it. The DM has the elemental’s statistics.
    
    
    At Higher Levels: When you cast this spell using a spell slot of 6th level or 
    higher, the challenge rating increases by 1 for each slot level above 5th.
    """
    name = "Conjure Elemental"
    level = 5
    casting_time = "1 minute"
    casting_range = "90 feet"
    components = ('V', 'S', 'M')
    materials = """Burning incense for air, soft clay for earth, sulfur and phosphorus for fire, or water and sand for water"""
    duration = "Concentration, up to 1 hour"
    ritual = False
    magic_school = "Conjuration"
    classes = ('Druid', 'Wizard')


class ConjureFey(Spell):
    """You summon a fey creature of challenge rating 6 or lower, or a fey spirit that 
    takes the form of a beast of challenge rating 6 or lower. 
    It appears in an 
    unoccupied space that you can see within range. The fey creature disappears when
     it drops to 0 hit points or when the spell ends. 
    
    The fey creature is friendly
     to you and your companions for the duration. Roll initiative for the creature, 
    which has its own turns. It obeys any verbal commands that you issue to it (no 
    action required by you), as long as they don’t violate its alignment. If you 
    don’t issue any commands to the fey creature, it defends itself from hostile 
    creatures but otherwise takes no actions. 
    
    If your concentration is broken, the
     fey creature doesn’t disappear. Instead, you lose control of the fey creature, 
    it becomes hostile toward you and your companions, and it might attack. An 
    uncontrolled fey creature can’t be dismissed by you, and it disappears 1 hour 
    after you summoned it. 
    The DM has the fey creature’s statistics.
    
    At Higher 
    Levels: When you cast this spell using a spell slot of 7th level or higher, the 
    challenge rating increases by 1 for each slot level above 6th
    """
    name = "Conjure Fey"
    level = 6
    casting_time = "1 minute"
    casting_range = "90 feet"
    components = ('V', 'S')
    materials = """"""
    duration = "Concentration, up to 1 hour"
    ritual = False
    magic_school = "Conjuration"
    classes = ('Druid', 'Warlock')


class ConjureMinorElementals(Spell):
    """You summon elementals that appear in unoccupied spaces that you can see within 
    range.
     You choose one the following options for what appears: 
    -One elemental 
    of challenge rating 2 or lower 
    -Two elementals of challenge rating 1 or lower 
    
    -Four elementals of challenge rating 1/2 or lower 
    -Eight elementals of 
    challenge rating 1/4 or lower. 
    
    An elemental summoned by this spell disappears 
    when it drops to 0 hit points or when the spell ends. 
    
    The summoned creatures 
    are friendly to you and your companions. Roll initiative for the summoned 
    creatures as a group, which has its own turns. They obey any verbal commands 
    that you issue to them (no action required by you). If you don’t issue any 
    commands to them, they defend themselves from hostile creatures, but otherwise 
    take no actions. 
    The DM has the creatures’ statistics.
    
    At Higher Levels: When 
    you cast this spell using certain higher-level spell slots, you choose one of 
    the summoning options above, and more creatures appear: twice as many with a 
    6th-level slot and three times as many with an 8th-level slot.
    """
    name = "Conjure Minor Elementals"
    level = 4
    casting_time = "1 minute"
    casting_range = "90 feet"
    components = ('V', 'S')
    materials = """"""
    duration = "Concentration, up to 1 hour"
    ritual = False
    magic_school = "Conjuration"
    classes = ('Druid', 'Wizard')


class ConjureVolley(Spell):
    """You fire a piece of nonmagical ammunition from a ranged weapon or throw a 
    nonmagical weapon into the air and choose a point within range. 
    Hundreds of 
    duplicates of the ammunition or weapon fall in a volley from above and then 
    disappear. Each creature in a 40-foot-radius. 20-foot-high cylinder centered on 
    that point must make a Dexterity saving throw. A creature takes 8d8 damage on a 
    failed save, or half as much damage on a successful one. The damage type is the 
    same as that of the ammunition or weapon.
    """
    name = "Conjure Volley"
    level = 5
    casting_time = "1 action"
    casting_range = "150 feet"
    components = ('V', 'S', 'M')
    materials = """One piece of ammunition or one thrown weapon"""
    duration = "Instantaneous"
    ritual = False
    magic_school = "Conjuration"
    classes = ('Ranger',)


class ConjureWoodlandBeings(Spell):
    """You summon fey creatures that appear in unoccupied spaces that you can see 
    within range. 
    
    Choose one of the following options for what appears: 
     •  One 
    fey creature of challenge rating 2 or lower 
     •  Two fey creatures of challenge 
    rating 1 or lower 
     •  Four fey creatures of challenge rating 1/2 or lower 
     •  
    Eight fey creatures of challenge rating 1/4 or lower 
    
    A summoned creature 
    disappears when it drops to 0 hit points or when the spell ends. 
    
    The summoned 
    creatures are friendly to you and your companions. Roll initiative for the 
    summoned creatures as a group, which have their own turns. They obey any verbal 
    commands that you issue to them (no action required by you). If you don’t issue 
    any commands to them, they defend themselves from hostile creatures, but 
    otherwise take no actions. 
    The DM has the creatures’ statistics.
    
    At Higher 
    Levels: When you cast this spell using certain higher-level spell slots, you 
    choose one of the summoning options above, and more creatures appear: 
    twice as
     many with a 6th-level slot
    three times as many with an 8th-level slot.
    """
    name = "Conjure Woodland Beings"
    level = 4
    casting_time = "1 action"
    casting_range = "60 feet"
    components = ('V', 'S', 'M')
    materials = """One holly berry per creature summoned"""
    duration = "Concentration, up to 1 hour"
    ritual = False
    magic_school = "Conjuration"
    classes = ('Druid', 'Ranger')


class ContactOtherPlane(Spell):
    """You mentally contact a demigod, the spirit of a long-dead sage, or some other 
    mysterious entity from another plane. 
    Contacting this extraplanar intelligence 
    can strain or even break your mind. When you cast this spell, make a DC 15 
    Intelligence saving throw. On a failure, you take 6d6 psychic damage and are 
    insane until you finish a long rest. While insane, you can’t take actions, can’t
     understand what other creatures say, can’t read, and speak only in gibberish. A
     greater restoration spell cast on you ends this effect. 
    
    On a successful save,
     you can ask the entity up to five questions. You must ask your questions before
     the spell ends. The DM answers each question with one word, such as yes, 
    no, maybe, never, irrelevant, or unclear (if the entity doesn’t know 
    the answer to the question). If a one-word answer would be misleading, the DM 
    might instead offer a short phrase as an answer.
    """
    name = "Contact Other Plane"
    level = 5
    casting_time = "1 minute"
    casting_range = "Self"
    components = ('V',)
    materials = """"""
    duration = "1 minute"
    ritual = True
    magic_school = "Divination"
    classes = ('Warlock', 'Wizard')


class Contagion(Spell):
    """Your touch inflicts disease. 
    Make a melee spell attack against a creature 
    within your reach. On a hit, you afflict the creature with a disease of your 
    choice from any of the ones described below. 
    
    At the end of each of the 
    target’s turns, it must make a Constitution saving throw. After failing three of
     these saving throws, the disease’s effects last for the duration, and the 
    creature stops making these saves. After succeeding on three of these saving 
    throws, the creature recovers from the disease, and the spell ends. 
    
    Since this
     spell induces a natural disease in its target, any effect that removes a 
    disease or otherwise ameliorates a disease’s effects apply to it. 
    
    Blinding 
    Sickness 
    Pain grips the creature’s mind, and its eyes turn milky white. The 
    creature has disadvantage on Wisdom checks and Wisdom saving throws and is 
    blinded. 
    
    Filth Fever 
    A raging fever sweeps through the creature’s body. The 
    creature has disadvantage on Strength checks, Strength saving throws, and attack
     rolls that use Strength. 
    
    Flesh Rot
    The creature’s flesh decays. The creature 
    has disadvantage on Charisma checks and vulnerability to all damage. 
    
    Mindfire
     
    The creature’s mind becomes feverish. The creature has disadvantage on 
    Intelligence checks and Intelligence saving throws, and the creature behaves as 
    if under the effects of the confusion spell during combat. 
    
    Seizure 
    The 
    creature is overcome with shaking. The creature has disadvantage on Dexterity 
    checks, Dexterity saving throws, and attack rolls that use Dexterity. 
    
    Slimy 
    Doom 
    The creature begins to bleed uncontrollably. The creature has disadvantage
     on Constitution checks and Constitution saving throws. In addition, whenever 
    the creature takes damage, it is stunned until the end of its next turn.
    """
    name = "Contagion"
    level = 5
    casting_time = "1 action"
    casting_range = "Touch"
    components = ('V', 'S')
    materials = """"""
    duration = "7 days"
    ritual = False
    magic_school = "Necromancy"
    classes = ('Cleric', 'Druid')


class Contingency(Spell):
    """Choose a spell of 5th level or lower that you can cast, that has a casting time 
    of 1 action, and that can target you. 
    You cast that spell called the 
    contingent spell as part of casting contingency, expending spell slots for 
    both, but the contingent spell doesn’t come into effect. Instead, it takes 
    effect when a certain circumstance occurs. You describe that circumstance when 
    you cast the two spells. For example, a contingency cast with water breathing 
    might stipulate that water breathing comes into effect when you are engulfed in 
    water or a similar liquid. 
    
    The contingent spell takes effect immediately after
     the circumstance is met for the first time, whether or not you want it to. and 
    then contingency ends. 
    
    The contingent spell takes effect only on you, even if 
    it can normally target others. You can use only one contingency spell at a time.
     If you cast this spell again, the effect of another contingency spell on you 
    ends. Also, contingency ends on you if its material component is ever not on 
    your person.
    """
    name = "Contingency"
    level = 6
    casting_time = "10 minutes"
    casting_range = "Self"
    components = ('V', 'S', 'M')
    materials = """A statuette of yourself carved from ivory and decorated with gems worth at least 1,500 gp"""
    duration = "10 days"
    ritual = False
    magic_school = "Evocation"
    classes = ('Wizard',)


class ContinualFlame(Spell):
    """A flame, equivalent in brightness to a torch, springs forth from an object that 
    you touch. 
    The effect looks like a regular flame, but it creates no heat and 
    doesn’t use oxygen. A continual flame can be covered or hidden but not smothered
     or quenched.
    """
    name = "Continual Flame"
    level = 2
    casting_time = "1 action"
    casting_range = "Touch"
    components = ('V', 'S', 'M')
    materials = """Ruby dust worth 50 gp, which the spell consumes"""
    duration = "Until dispelled"
    ritual = False
    magic_school = "Evocation"
    classes = ('Cleric', 'Wizard')


class ControlFlames(Spell):
    """You choose a nonmagical flame that you can see within range and that fits within
     a 5-foot cube. You affect it in one of the following ways:
    - You 
    instantaneously expand the flame 5 feet in one direction, provided that wood or 
    other fuel is present in the new location.
    - You instantaneously extinguish the 
    flames within the cube.
    - You double or halve the area of bright light and dim 
    light cast by the flame, change its color, or both. The change lasts for 1 hour.
    
    - You cause simple shapes — such as the vague form of a creature, an inanimate 
    object, or a location — to appear within the flames and animate as you like. The
     shapes last for 1 hour.
    If you cast this spell multiple times, you can have up 
    to three non-instantaneous
    """
    name = "Control Flames"
    level = 0
    casting_time = "1 action"
    casting_range = "60 feet"
    components = ('S',)
    materials = """"""
    duration = "Instantaneous or 1 hour"
    ritual = False
    magic_school = "Transmutation"
    classes = ('Druid', 'Sorcerer', 'Wizard')


class ControlWater(Spell):
    """Until the spell ends, you control any freestanding water inside an area you 
    choose that is a cube up to 100 feet on a side. 
    You can choose from any of the 
    following effects when you cast this spell. As an action on your turn, you can 
    repeat the same effect or choose a different one. 
    
    Flood 
    You cause the water 
    level of all standing water in the area to rise by as much as 20 feet. If the 
    area includes a shore, the flooding water spills over onto dry land. If you 
    choose an area in a large body of water, you instead create a 20-foot tall wave 
    that travels from one side of the area to the other and then crashes down. Any 
    Huge or smaller vehicles in the wave’s path are carried with it to the other 
    side. Any Huge or smaller vehicles struck by the wave have a 25 percent chance 
    of capsizing. The water level remains elevated until the spell ends or you 
    choose a different effect. If this effect produced a wave, the wave repeats on 
    the start of your next turn while the flood effect lasts. 
    
    Part Water 
    You 
    cause water in the area to move apart and create a trench. The trench extends 
    across the spell’s area, and the separated water forms a wall to either side. 
    The trench remains until the spell ends or you choose a different effect. The 
    water then slowly fills in the trench over the course of the next round until 
    the normal water level is restored. 
    
    Redirect Flow 
    You cause flowing water in 
    the area to move in a direction you choose, even if the water has to flow over 
    obstacles, up walls, or in other unlikely directions. The water in the area 
    moves as you direct it, but once it moves beyond the spell’s area, it resumes 
    its flow based on the terrain conditions. The water continues to move in the 
    direction you chose until the spell ends or you choose a different effect. 
    
    
    Whirlpool 
    This effect requires a body of water at least 50 feet square and 25 
    feet deep. You cause a whirlpool to form in the center of the area. The 
    whirlpool forms a vortex that is 5 feet wide at the base, up to 50 feet wide at 
    the top, and 25 feet tall. Any creature or object in the water and within 25 
    feet of the vortex is pulled 10 feet toward it. A creature can swim away from 
    the vortex by making a Strength (Athletics) check against your spell save DC. 
    
    When a creature enters the vortex for the first time on a turn or starts its 
    turn there, it must make a Strength saving throw. On a failed save, the creature
     takes 2d8 bludgeoning damage and is caught in the vortex until the spell ends. 
    On a successful save, the creature takes half damage, and isn’t caught in the 
    vortex. A creature caught in the vortex can use its action to try to swim away 
    from the vortex as described above, but has disadvantage on the Strength 
    (Athletics) check to do so. 
    The first time each turn that an object enters the 
    vortex, the object takes 2d8 bludgeoning damage, this damage occurs each round 
    it remains in the vortex.
    """
    name = "Control Water"
    level = 4
    casting_time = "1 action"
    casting_range = "300 feet"
    components = ('V', 'S', 'M')
    materials = """A drop of water and a pinch of dust"""
    duration = "Concentration, up to 10 minutes"
    ritual = False
    magic_school = "Transmutation"
    classes = ('Cleric', 'Druid', 'Wizard')


class ControlWeather(Spell):
    """You take control of the weather within 5 miles of you for the duration. 
    You 
    must be outdoors to cast this spell. Moving to a place where you don’t have a 
    clear path to the sky ends the spell early. 
    
    When you cast the spell, you 
    change the current weather conditions, which are determined by the DM based on 
    the climate and season. You can change precipitation, temperature, and wind. It 
    takes 1d4 x 10 minutes for the new conditions to take effect. Once they do so, 
    you can change the conditions again. When the spell ends, the weather gradually 
    returns to normal. 
    
    When you change the weather conditions, find a current 
    condition on the following tables and change its stage by one, up or down. When 
    changing the wind, you can change its direction. 
    
    Precipitation 
    Stage 1 – 
    Clear, 
    Stage 2 – Light clouds, 
    Stage 3 – Overcast or ground fog, 
    Stage 4 – 
    Rain, hail or snow, 
    Stage 5 – Torrential rain, driving hail or blizzard 
    
    
    Temperature 
    Stage 1 – Unbearable heat, 
    Stage 2 – Hot, 
    Stage 3 – Warm, 
    Stage 
    4 – Cool, 
    Stage 5 – Cold, 
    Stage 6 – Arctic cold 
    
    Wind 
    Stage 1 – Calm, 
    Stage
     2 – Moderate wind, 
    Stage 3 – Strong wind, 
    Stage 4 – Gale, 
    Stage 5 – Storm
    """
    name = "Control Weather"
    level = 8
    casting_time = "10 minutes"
    casting_range = "Self (5-mile radius)"
    components = ('V', 'S', 'M')
    materials = """"""
    duration = "Concentration, up to 8 hours"
    ritual = False
    magic_school = "Transmutation"
    classes = ('Cleric', 'Druid', 'Wizard')


class ControlWinds(Spell):
    """You take control of the air in a 100-foot cube that you can see within range. 
    Choose one of the following effects when you cast the spell. The effect lasts 
    for the spell’s duration, unless you use your action on a later turn to switch 
    to a different effect. You can also use your action to temporarily halt the 
    effect or to restart one you’ve halted.
    Gusts. A wind picks up within the cube, 
    continually blowing in a horizontal direction that you choose. You choose the 
    intensity of the wind: calm, moderate, or strong. If the wind is moderate or 
    strong, ranged weapon attacks that pass through it or that are made against 
    targets within the cube have disadvantage on their attack rolls. If the wind is 
    strong, any creature moving against the wind must spend 1 extra foot of movement
     for each foot moved.
    
    Downdraft. You cause a sustained blast of strong wind to 
    blow downward from the top of the cube. Ranged weapon attacks that pass through 
    the cube
    or that are made against targets within it have disadvantage on their 
    attack rolls. A creature must make a Strength saving throw if it flies into the 
    cube for the first time on a turn or starts its turn there flying. On a failed 
    save, the creature is knocked prone.
    
    Updraft. You cause a sustained updraft 
    within the cube, rising upward from the cube’s bottom edge. Creatures that end a
     fall within the cube take only half damage from the fall. When a creature in 
    the cube makes a vertical jump, the creature can jump up to 10 feet higher than 
    normal.
    """
    name = "Control Winds"
    level = 5
    casting_time = "1 action"
    casting_range = "300 feet"
    components = ('V', 'S')
    materials = """"""
    duration = "Concentration, up to 1 hour"
    ritual = False
    magic_school = "Transmutation"
    classes = ('Druid', 'Sorcerer', 'Wizard')


class CordonOfArrows(Spell):
    """You plant four pieces of nonmagical ammunition – arrows or crossbow bolts – in 
    the ground within range and lay magic upon them to protect an area. 
    Until the 
    spell ends, whenever a creature other than you comes within 30 feet of the 
    ammunition for the first time on a turn or ends its turn there, one piece of 
    ammunition flies up to strike it. The creature must succeed on a Dexterity 
    saving throw or take 1d6 piercing damage. The piece of ammunition is then 
    destroyed. The spell ends when no ammunition remains. 
    
    When you cast this 
    spell, you can designate any creatures you choose, and the spell ignores them.
    
    
    At Higher Levels: When you cast this spell using a spell slot of 3rd level or 
    higher, the amount of ammunition that can be affected increases by two for each 
    slot level above 2nd.
    """
    name = "Cordon Of Arrows"
    level = 2
    casting_time = "1 action"
    casting_range = "5 feet"
    components = ('V', 'S', 'M')
    materials = """Four or more arrows or bolts"""
    duration = "8 hours"
    ritual = False
    magic_school = "Transmutation"
    classes = ('Ranger',)


class Counterspell(Spell):
    """1 reaction, which you take when you see a creature within 60 feet of you casting
     a spell
    
    You attempt to interrupt a creature in the process of casting a spell.
     If the creature is casting a spell of 3rd level or lower, its spell fails and 
    has no effect. If it is casting a spell of 4th level or higher, make an ability 
    check using your spellcasting ability.  The DC equals 10+ the spell’s level. On 
    a success, the creature’s spell fails and has no effect.
    
    At Higher Levels: When
     you cast this spell using a spell slot of 4th level or higher, the interrupted 
    spell has no effect if its level is less than or equal to the level of the spell
     slot you used.
    """
    name = "Counterspell"
    level = 3
    casting_time = "Special"
    casting_range = "60 feet"
    components = ('S',)
    materials = """"""
    duration = "Instantaneous"
    ritual = False
    magic_school = "Abjuration"
    classes = ('Sorcerer', 'Warlock', 'Wizard')


class CreateBonfire(Spell):
    """You create a bonfire on ground that you can see within range. Until the spell 
    ends, the magic bonfire fills a 5-foot cube. Any creature in the bonfire’s space
     when you cast the spell must succeed on a Dexterity saving throw or take 1d8 
    fire damage. A creature must also make the saving throw when it moves into the 
    bonfire’s space for the first time on a turn or ends its turn there.
    The bonfire
     ignites flammable objects in its area that aren’t being worn or carried.
    The 
    spell’s damage increases by 1d8 when you reach 5th level (2d8), 11th level 
    (3d8), and 17th level (4d8).
    """
    name = "Create Bonfire"
    level = 0
    casting_time = "1 action"
    casting_range = "60 feet"
    components = ('V', 'S')
    materials = """"""
    duration = "Concentration, up to 1 minute"
    ritual = False
    magic_school = "Conjuration"
    classes = ('Druid', 'Sorcerer', 'Warlock', 'Wizard')


class CreateFoodAndWater(Spell):
    """You create 45 pounds of food and 30 gallons of water on the ground or in 
    containers within range, enough to sustain up to fifteen humanoids or five 
    steeds for 24 hours. The food is bland but nourishing, and spoils if uneaten 
    after 24 hours. The water is clean and doesn’t go bad.
    """
    name = "Create Food And Water"
    level = 3
    casting_time = "1 action"
    casting_range = "30 feet"
    components = ('V', 'S')
    materials = """"""
    duration = "Instantaneous"
    ritual = False
    magic_school = "Conjuration"
    classes = ('Cleric', 'Paladin')


class CreateHomunculus(Spell):
    """While speaking an intricate incantation, you cut yourself with a jewel-encrusted
     dagger, taking 2d4 piercing damage that can’t be reduced in any way. You then 
    drip your blood on the spell’s other components and touch them, transforming 
    them into a special construct called a homunculus. The statistics of the 
    homunculus are in the Monster Manual. It is your faithful companion, and it dies
     if you die. Whenever you finish a long rest, you can spend up to half your Hit 
    Dice if the homunculus is on the same plane of existence as you. When you do so,
     roll each die and add your Constitution modifier to it. Your hit point maximum 
    is reduced by the total, and the homunculus’s hit point maximum and current hit 
    points are
    both increased by it. This process can reduce you to no lower than 1 
    hit point. and the change to your and the homunculus’s hit points ends when you 
    finish your next long rest. The reduction to your hit point maximum can’t be 
    removed by any means before then, except by the homunculus‘s death. You can have
     only one homunculus at a time. If you cast this spell while your homunculus 
    lives, the spell fails.
    """
    name = "Create Homunculus"
    level = 6
    casting_time = "1 hour"
    casting_range = "Touch"
    components = ('V', 'S', 'M')
    materials = """Clay, ash, and mandrake root, all of which the spell consumes, and a jewel-encrusted dagger worth at least 1,000 gp"""
    duration = "Instantaneous"
    ritual = False
    magic_school = "Transmutation"
    classes = ('Wizard',)


class CreateOrDestroyWater(Spell):
    """You either create or destroy water. 
    
    Create Water 
    You create up to 10 gallons 
    of clean water within range in an open container. Alternatively, the water falls
     as rain in a 30-foot cube within range, extinguishing exposed flames in the 
    area. 
    
    Destroy Water 
    You destroy up to 10 gallons of water in an open 
    container within range. Alternatively, you destroy fog in a 30-foot cube within 
    range.
    
    At Higher Levels: When you cast this spell using a spell slot of 2nd 
    level or higher, you create or destroy 10 additional gallons of water, or the 
    size of the cube increases by 5 feet, for each slot level above 1st.
    """
    name = "Create Or Destroy Water"
    level = 1
    casting_time = "1 action"
    casting_range = "30 feet"
    components = ('V', 'S', 'M')
    materials = """A drop of water if creating water or a few grains of sand if destroying it"""
    duration = "Instantaneous"
    ritual = False
    magic_school = "Transmutation"
    classes = ('Cleric', 'Druid')


class CreateUndead(Spell):
    """You can cast this spell only at night. Choose up to three corpses of Medium or 
    Small humanoids within range. Each corpse becomes a ghoul under your control. 
    (The DM has game statistics for these creatures.) 
    
    As a bonus action on each of
     your turns, you can mentally command any creature you animated with this spell 
    if the creature is within 120 feet of you (if you control multiple creatures, 
    you can command any or all of them at the same time, issuing the same command to
     each one). You decide what action the creature will take and where it will move
     during its next turn, or you can issue a general command, such as to guard a 
    particular chamber or corridor. If you issue no commands, the creature only 
    defends itself against hostile creatures. Once given an order, the creature 
    continues to follow it until its task is complete. 
    
    The creature is under your 
    control for 24 hours, after which it stops obeying any command you have given 
    it. To maintain control of the creature for another 24 hours, you must cast this
     spell on the creature before the current 24-hour period ends. This use of the 
    spell reasserts your control over up to three creatures you have animated with 
    this spell, rather than animating new ones.
    
    At Higher Levels: When you cast 
    this spell using a 7th-level spell slot, you can animate or reassert control 
    over four ghouls. 
    When you cast this spell using an 8th-level spell slot, you 
    can animate or reassert control over five ghouls or two ghasts or wights. 
    When
     you cast this spell using a 9th-level spell slot, you can animate or reassert 
    control over six ghouls, three ghasts or wights, or two mummies.
    """
    name = "Create Undead"
    level = 6
    casting_time = "1 minute"
    casting_range = "10 feet"
    components = ('V', 'S', 'M')
    materials = """One clay pot filled with grave dirt, one clay pot filled with brackish water, and one 150 gp black onyx stone for each corpse"""
    duration = "Instantaneous"
    ritual = False
    magic_school = "Necromancy"
    classes = ('Cleric', 'Warlock', 'Wizard')


class Creation(Spell):
    """You pull wisps of shadow material from the Shadowfell to create a nonliving 
    object of vegetable matter within range: soft goods, rope, wood, or something 
    similar. You can also use this spell to create mineral objects such as stone, 
    crystal, or metal. The object created must be no larger than a 5-foot cube, and 
    the object must be of a form and material that you have seen before. 
    
    The 
    duration depends on the object’s material. If the object is composed of multiple
     materials, use the shortest duration. 
    
    Material — Duration 
    Vegetable matter —
     1 day 
    Stone/crystal — 12 hours 
    Precious metals — 1 hour 
    Gems — 10 minutes 
    
    Adamantine/Mithral — 1 minute 
    
    Using any material created by this spell as 
    another spell’s material component causes that spell to fail.
    
    At Higher Levels:
     When you cast this spell using a spell slot of 6th level or higher, the cube 
    increases by 5 feet for each slot level above 5th.
    """
    name = "Creation"
    level = 5
    casting_time = "1 minute"
    casting_range = "30 feet"
    components = ('V', 'S', 'M')
    materials = """A tiny piece of matter of the same type of the item you plan to create"""
    duration = "Special"
    ritual = False
    magic_school = "Illusion"
    classes = ('Sorcerer', 'Wizard')


class CrownOfMadness(Spell):
    """One humanoid of your choice that you can see within range must succeed on a 
    Wisdom saving throw or become charmed by you for the duration. 
    While the target
     is charmed in this way, a twisted crown of jagged iron appears on its head, and
     a madness glows in its eyes. 
    
    The charmed target must use its action before 
    moving on each of its turns to make a melee attack against a creature other than
     itself that you mentally choose. The target can act normally on its turn if you
     choose no creature or if none are within its reach. 
    
    On your subsequent turns,
     you must use your action to maintain control over the target, or the spell 
    ends. Also, the target can make a Wisdom saving throw at the end of each of its 
    turns. On a success, the spell ends.
    """
    name = "Crown Of Madness"
    level = 2
    casting_time = "1 action"
    casting_range = "120 feet"
    components = ('V', 'S')
    materials = """"""
    duration = "Concentration, up to 1 minute"
    ritual = False
    magic_school = "Enchantment"
    classes = ('Bard', 'Sorcerer', 'Warlock', 'Wizard')


class CrownOfStars(Spell):
    """Seven star-like motes of light appear and orbit your head until the spell ends. 
    You can use a bonus action to send one of the motes streaking toward one 
    creature or object within 120 feet of you. When you do so, make a ranged spell 
    attack. On a hit. the target takes 4d12 radiant damage. Whether you hit or miss,
     the mote is expended. The spell ends early if you expend the last mote. If you 
    have four or more motes remaining, they shed bright light in a 30-foot radius 
    and dim light for an additional 30 feet. Ifyou have one to three motes 
    remaining, they shed dim light in a 30—foot radius.
    
    At Higher Levels: When you 
    cast this spell using a spell slot of 8th level or higher, the number of motes 
    created increases by two for each slot level above 7th.
    """
    name = "Crown Of Stars"
    level = 7
    casting_time = "1 action"
    casting_range = "Self"
    components = ('V', 'S')
    materials = """"""
    duration = "1 hour"
    ritual = False
    magic_school = "Evocation"
    classes = ('Sorcerer', 'Warlock', 'Wizard')


class CrusadersMantle(Spell):
    """Holy power radiates from you in an aura with a 30-foot radius, awakening 
    boldness in friendly creatures. Until the spell ends, the aura moves with you, 
    centered on you. While in the aura, each nonhostile creature in the aura 
    (including you) deals an extra 1d4 radiant damage when it hits with a weapon 
    attack.
    """
    name = "Crusaders Mantle"
    level = 3
    casting_time = "1 action"
    casting_range = "Self"
    components = ('V',)
    materials = """"""
    duration = "Concentration, up to 1 minute"
    ritual = False
    magic_school = "Evocation"
    classes = ('Paladin',)


class CureWounds(Spell):
    """A creature you touch regains a number of hit points equal to 1d8 + your 
    spellcasting ability modifier. This spell has no effect on undead or constructs.
    
    
    At Higher Levels: When you cast this spell using a spell slot of 2nd level or 
    higher, the healing increases by 1d8 for each slot level above 1st.
    """
    name = "Cure Wounds"
    level = 1
    casting_time = "1 action"
    casting_range = "Touch"
    components = ('V', 'S')
    materials = """"""
    duration = "Instantaneous"
    ritual = False
    magic_school = "Evocation"
    classes = ('Bard', 'Cleric', 'Druid', 'Paladin', 'Ranger')


