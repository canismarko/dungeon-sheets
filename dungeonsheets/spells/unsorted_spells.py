from .spells import Spell

class ControlWater(Spell):
    """Until the spell ends, you control any freestanding water inside an area you 
    choose that is a cube up to 100 feet on a side. You can choose from any of the 
    following effects when you cast this spell. As an action on your turn, you can 
    repeat the same effect or choose a different one.
    
    Flood: You cause the water 
    level of all standing water in the area to rise by as much as 20 feet. If the 
    area includes a shore, the flooding water spills over onto dry land. If you 
    choose an area in a large body of water, you instead create a 20-foot tall wave 
    that travels from one side of the area to the other and then crashes down. Any 
    Huge or smaller vehicles in the wave's path are carried with it to the other 
    side. Any Huge or smaller vehicles struck by the wave have a 25 percent chance 
    of capsizing. The water level remains elevated until the spell ends or you 
    choose a different effect. If this effect produced a wave, the wave repeats on 
    the start of your next turn while the flood effect lasts.
    
    Part Water: You cause
     water in the area to move apart and create a trench. The trench extends across 
    the spell's area, and the separated water forms a wall to either side. The 
    trench remains until the spell ends or you choose a different effect. The water 
    then slowly fills in the trench over the course of the next round until the 
    normal water level is restored.
    
    Redirect Flow: You cause flowing water in the 
    area to move in a direction you choose, even if the water has to flow over 
    obstacles, up walls, or in other unlikely directions. The water in the area 
    moves as you direct it, but once it moves beyond the spell's area, it resumes 
    its flow based on the terrain conditions. The water continues to move in the 
    direction you chose until the spell ends or you choose a different effect.
    
    
    Whirlpool: This effect requires a body of water at least 50 feet square and 25 
    feet deep. You cause a whirlpool to form in the center of the area. The 
    whirlpool forms a vortex that is 5 feet wide at the base, up to 50 feet wide at 
    the top, and 25 feet tall. Any creature or object in the water and within 25 
    feet of the vortex is pulled 10 feet toward it. A creature can swim away from 
    the vortex by making a Strength (Athletics) check against your spell save DC. 
    When a creature enters the vortex for the first time on a turn or starts its 
    turn there, it must make a Strength saving throw. On a failed save, the creature
     takes 2d8 bludgeoning damage and is caught in the vortex until the spell ends. 
    On a successful save, the creature takes half damage, and isn't caught in the 
    vortex. A creature caught in the vortex can use its action to try to swim away 
    from the vortex as described above, but has disadvantage on the Strength 
    (Athletics) check to do so. The first time each turn that an object enters the 
    vortex, the object takes 2d8 bludgeoning damage, this damage occurs each round 
    it remains in the vortex.
    """
    name = "Control Water"
    level = 4
    casting_time = "1 action"
    casting_range = "300 feet"
    components = ('V', 'S', 'M')
    materials = "A drop of water and a pinch of dust"
    duration = "Concentration, up to 10 minutes"
    magic_school = "Transmutation"
    classes = ('Cleric', 'Druid', 'Wizard')

class SleetStorm(Spell):
    """Until the spell ends, freezing rain and sleet fall in a 20-foot-tall cylinder 
    with a 40-foot radius centered on a point you choose within range. The area is 
    heavily obscured, and exposed flames in the area are doused.
    
    The ground in the 
    area is covered with slick ice, making it difficult terrain. When a creature 
    enters the spell's area for the first time on a turn or starts its turn there, 
    it must make a Dexterity saving throw. On a failed save, it falls prone.
    
    If a 
    creature is concentrating in the spell's area, the creature must make a 
    successful Constitution saving throw against your spell save DC or lose 
    concentration.
    """
    name = "Sleet Storm"
    level = 3
    casting_time = "1 action"
    casting_range = "150 feet"
    components = ('V', 'S', 'M')
    materials = "A pinch of dust and a few drops of water"
    duration = "Concentration, up to 1 minute"
    magic_school = "Conjuration"
    classes = ('Druid', 'Sorcerer', 'Wizard')

    
class DestructiveWave(Spell):
    """You strike the ground, creating a burst of divine energy that ripples
    outward from you. Each creature you choose within 30 feet of you must
    succeed on a Constitution saving throw or take 5d6 thunder damage, as well
    as 5d6 radiant or necrotic damage (your choice), and be knocked prone. A
    creature that succeeds on its saving throw takes half as much damage and
    isn’t knocked prone.

    """
    name = "Destructive Wave"
    level = 5
    casting_time = "1 action"
    casting_range = "Self (30 foot radius)"
    components = ("V",)
    magic_school = "Evocation"
    classes = ("Paladin",)

    
class InsectPlague(Spell):
    """Swarming, biting locusts fill a 20-foot-radius sphere centered on a point you 
    choose within range. The sphere spreads around corners. The sphere remains for 
    the duration, and its area is lightly obscured. The sphere's area is difficult 
    terrain.
    
    When the area appears, each creature in it must make a Constitution 
    saving throw. A creature takes 4d10 piercing damage on a failed save, or half as
     much damage on a successful one. A creature must also make this saving throw 
    when it enters the spell's area for the first time on a turn or ends its turn 
    there.
    
    At Higher Levels: When you cast this spell using a spell slot of 6th 
    level or higher, the damage increases by 1d10 for each slot level above 5th.
    """
    name = "Insect Plague"
    level = 5
    casting_time = "1 action"
    casting_range = "300 feet"
    components = ('V', 'S', 'M')
    materials = "A few grains of sugar, some kernels of grain, and a smear of fat"
    duration = "Concentration, Up to 10 minutes"
    magic_school = "Conjuration"
    classes = ('Cleric', 'Druid', 'Sorcerer')


class FindFamiliar(Spell):
    """You gain the service of a familiar, a spirit that takes an animal form you 
    choose: bat, cat, crab, frog (toad), hawk, lizard, octopus, owl, poisonous 
    snake, fish (quipper), rat, raven, sea horse, spider, or weasel. Appearing in an
     unoccupied space within range, the familiar has the statistics of the chosen 
    form, though it is a celestial, fey, or fiend (your choice) instead of a beast.
    
    
    Your familiar acts independently of you, but it always obeys your commands. In
     combat, it rolls its own initiative and acts on its own turn. A familiar can't 
    attack, but it can take other actions as normal.
    
    When the familiar drops to 0 
    hit points, it disappears, leaving behind no physical form. It reappears after 
    you cast this spell again.
    
    While your familiar is within 100 feet of you, you 
    can communicate with it telepathically. Additionally, as an action, you can see 
    through your familiar's eyes and hear what it hears until the start of your next
     turn, gaining the benefits of any special senses that the familiar has. During 
    this time, you are deaf and blind with regard to your own senses.
    
    As an action,
     you can temporarily dismiss your familiar. It disappears into a pocket 
    dimension where it awaits your summons. Alternatively, you can dismiss it 
    forever. As an action while it is temporarily dismissed, you can cause it to 
    reappear in any unoccupied space within 30 feet of you.
    
    You can't have more 
    than one familiar at a time. If you cast this spell while you already have a 
    familiar, you instead cause it to adopt a new form. Choose one of the forms from
     the above list. Your familiar transforms into the chosen creature.
    
    Finally, 
    when you cast a spell with a range of touch, your familiar can deliver the spell
     as if it had cast the spell. Your familiar must be within 100 feet of you, and 
    it must use its reaction to deliver the spell when you cast it. If the spell 
    requires an attack roll, you use your attack modifier for the roll.
    """
    name = "Find Familiar"
    level = 1
    casting_time = "1 hour"
    casting_range = "10 feet"
    components = ('V', 'S', 'M')
    materials = ("10 gp worth of charcoal, incense, and herbs that must be"
                 "consumed by fire in a brass brazier")
    duration = "Instantaneous"
    magic_school = "Conjuration"
    classes = ('Wizard',)

    
class ProtectionFromEvilAndGood(Spell):
    """Until the spell ends, one willing creature you touch is protected against 
    certain types of creatures - aberrations, celestials, elementals, fey, fiends, 
    and undead.
    
    The protection grants several benefits. Creatures of those types 
    have disadvantage on attack rolls against the target. The target also can't be 
    charmed, frightened, or possessed by them. If the target is already charmed, 
    frightened, or possessed by such a creature, the target has advantage on any new
     saving throw against the relevant effect.
    """
    name = "Protection From Evil And Good"
    level = 1
    casting_time = "1 action"
    casting_range = "Touch"
    components = ('V', 'S', 'M')
    materials = "Holy water or powdered silver and iron, which the spell consumes"
    duration = "Concentration, Up to 10 minutes"
    magic_school = "Abjuration"
    classes = ('Cleric', 'Paladin', 'Warlock', 'Wizard')


class ZoneOfTruth(Spell):
    """You create a magical zone that guards against deception in a 15-foot-radius 
    sphere centered on a point of your choice within range. Until the spell ends, a 
    creature that enters the spell's area for the first time on a turn or starts its
     turn there must make a Charisma saving throw. On a failed save, a creature 
    can't speak a deliberate lie while in the radius. You know whether each creature
     succeeds or fails on its saving throw.
    
    An affected creature is aware of the 
    spell and can thus avoid answering questions to which it would normally respond 
    with a lie. Such creatures can be evasive in its answers as long as it remains 
    within the boundaries of the truth.
    """
    name = "Zone Of Truth"
    level = 2
    casting_time = "1 action"
    casting_range = "60 feet"
    components = ('V', 'S')
    materials = ""
    duration = "10 minutes"
    magic_school = "Enchantment"
    classes = ('Bard', 'Cleric', 'Paladin')


class EnsnaringStrike(Spell):
    """The next time you hit a creature with a weapon attack before this spell
    ends, a writhing mass of thorny vines appears at the point of impact, and
    the target must succeed on a Strength saving throw or be restrained by the
    magical vines until the spell ends. A Large or larger creature has
    advantage on this saving throw. If the target succeeds on the save, the
    vines shrivel away.

    While restrained by this spell, the target takes 1d6 piercing damage at the
    start of each of its turns. A creature restrained by the vines or one that
    can touch the creature can use its action to make a Strength check against
    your spell save DC. On a success, the target is freed.

    At Higher Level:

    If you cast this spell using a spell slot of 2nd level or higher, the
    damage increases by 1d6 for each slot level above 1st.

    """
    name = "Ensnaring Strike"
    level = 1
    casting_time = '1 bonus action'
    casting_range = 'Self'
    components = ('V')
    duration = 'Concentration, up to 1 minute'
    magic_school = 'Conjuration'
    classes = ("Ranger",)


class Moonbeam(Spell):
    """A silvery beam of pale light shines down in a 5-foot radius, 40-foot-high 
    cylinder centered on a point within range. Until the spell ends, dim light fills
     the cylinder.
    
    When a creature enters the spell's area for the first time on a 
    turn or starts its turn there, it is engulfed in ghostly flames that cause 
    searing pain, and it must make a Constitution saving throw. It takes 2d10 
    radiant damage on a failed save, or half as much damage on a successful one.
    
    A 
    shapechanger makes its saving throw with disadvantage. If it fails, it also 
    instantly reverts to its original form and can't assume a different form until 
    it leaves the spell's light.
    
    On each of your turns after you cast this spell, 
    you can use an action to move the beam 60 feet in any direction.
    
    At Higher 
    Levels: When you cast this spell using a spell slot of 3rd level or higher, the 
    damage increases by 1d10 for each slot level above 2nd.
    """
    name = "Moonbeam"
    level = 2
    casting_time = "1 action"
    casting_range = "120 feet"
    components = ('V', 'S', 'M')
    materials = "Several seeds of any moonseed plant and a piece of opalescent feldspar"
    duration = "Concentration, Up to 1 minute"
    magic_school = "Evocation"
    classes = ('Druid',)


class PlantGrowth(Spell):
    """This spell channels vitality into plants within a specific area. There are two 
    possible uses for the spell, granting either immediate or long-term benefits.
    
    
    If you cast this spell using 1 action, choose a point within range. All normal 
    plants in a 100-foot radius centered on that point become thick and overgrown. A
     creature moving through the area must spend 4 feet of movement for every 1 foot
     it moves.
    
    You can exclude one or more areas of any size within the spell's 
    area from being affected.
    
    If you cast this spell over 8 hours, you enrich the 
    land. All plants in a half-mile radius centered on a point within range become 
    enriched for 1 year. The plants yield twice the normal amount of food when 
    harvested.
    """
    name = "Plant Growth"
    level = 3
    casting_time = "1 action or 8 hours"
    casting_range = "150 feet"
    components = ('V', 'S')
    materials = ""
    duration = "Instantaneous"
    magic_school = "Transmutation"
    classes = ('Bard', 'Druid', 'Ranger')


class IceStorm(Spell):
    """A hail of rock-hard ice pounds to the ground in a 20-foot-radius, 40-foot-high 
    cylinder centered on a point within range. Each creature in the cylinder must 
    make a Dexterity saving throw. A creature takes 2d8 bludgeoning damage and 4d6 
    cold damage on a failed save, or half as much damage on a successful one.
    
    
    Hailstones turn the storm's area of effect into difficult terrain until the end 
    of your next turn.
    
    At Higher Levels: When you cast this spell using a spell 
    slot of 5th level or higher, the bludgeoning damage increases by 1d8 for each 
    slot level above 4th.
    """
    name = "Ice Storm"
    level = 4
    casting_time = "1 action"
    casting_range = "300 feet"
    components = ('V', 'S', 'M')
    materials = "A pinch of dust and a few drops of water"
    duration = "Instantaneous"
    magic_school = "Evocation"
    classes = ('Druid', 'Sorcerer', 'Wizard')


class CommuneWithNature(Spell):
    """You briefly become one with nature and gain knowledge of the surrounding 
    territory. In the outdoors, the spell gives you knowledge of the land within 3 
    miles of you. In caves and other natural underground settings, the radius is 
    limited to 300 feet. The spell doesn't function where nature has been replaced 
    by construction, such as in dungeons and towns.
    
    You instantly gain knowledge of
     up to three facts of your choice about any of the following subjects as they 
    relate to the area - terrain and bodies of water; prevalent plants, minerals, 
    animals, or peoples; powerful celestials, fey, fiends, elementals, or undead; 
    influence from other planes of existence; buildings.
    
    For example, you could 
    determine the location of powerful undead in the area, the location of major 
    sources of safe drinking water, and the location of any nearby towns.
    """
    name = "Commune With Nature"
    level = 5
    casting_time = "1 minute"
    casting_range = "Self"
    components = ('V', 'S')
    materials = ""
    duration = "Instantaneous"
    magic_school = "Divination"
    classes = ('Druid', 'Ranger')


class TreeStride(Spell):
    """You gain the ability to enter a tree and move from inside it to inside another 
    tree of the same kind within 500 feet. Both trees must be living and at least 
    the same size as you. You must use 5 feet of movement to enter a tree. You 
    instantly know the location of all other trees of the same kind within 500 feet 
    and, as part of the move used to enter the tree, can either pass into one of 
    those trees or step out of the tree you're in. You appear in a spot of your 
    choice within 5 feet of the destination tree, using another 5 feet of movement. 
    If you have no movement left, you appear within 5 feet of the tree you entered.
    
    
    You can use this transportation ability once per round for the duration. You 
    must end each turn outside a tree.
    """
    name = "Tree Stride"
    level = 5
    casting_time = "1 action"
    casting_range = "Self"
    components = ('V', 'S')
    materials = ""
    duration = "Concentration, Up to 1 minute"
    magic_school = "Conjuration"
    classes = ('Druid', 'Ranger')


class HoldMonster(Spell):
    """Choose a creature that you can see within range. The target must succeed on a 
    Wisdom saving throw or be paralyzed for the duration. This spell has no effect 
    on undead. At the end of each of its turns, the target can make another Wisdom 
    saving throw. On a success, the spell ends on the target.
    
    At Higher Levels: 
    When you cast this spell using a spell slot of 6th level or higher, you can 
    target on additional creature for each slot level above 5th. The creatures must 
    be within 30 feet of each other when you target them.
    """
    name = "Hold Monster"
    level = 5
    casting_time = "1 action"
    casting_range = "90 feet"
    components = ('V', 'S', 'M')
    materials = "A small, straight piece of iron"
    duration = "Concentration, Up to 1 minute"
    magic_school = "Enchantment"
    classes = ('Bard', 'Sorcerer', 'Warlock', 'Wizard')


class Scrying(Spell):
    """You can see and hear a particular creature you choose that is on the same plane 
    of existence as you. The target must make a Wisdom saving throw, which is 
    modified by how well you know the target and the sort of physical connection you
     have to it. If a target knows you're casting this spell, it can fail the saving
     throw voluntarily if it wants to be observed.
    
    Knowledge - Save Modifier
    
    
    Secondhand (you have heard of the target) - +5
    
    Firsthand (you have met the 
    target) +0
    Familiar (you know the target well) - -5
    
    Connection - Save Modifier
    
    
    Likeness or picture - -2
    
    Possession or garment - -4
    
    Body part, lock of hair,
     bit of nail, or the like - -10
    
    On a successful save, the target isn't affected, and you can't use this
    spell against it again for 24 hours.
    
    On a failed save, the spell creates an invisible sensor within 10 feet of
    the target.  You can see and hear through the sensor as if you were
    there. The sensor moves with the target, remaining within 10 feet of it for
    the duration. A creature that can see invisible objects sees the sensor as
    a luminous orb about the size of your fist.
    
    Instead of targeting a creature, you can choose a location you 
    have seen before as the target of this spell. When you do, the sensor appears at
     that location and doesn't move.

    """
    name = "Scrying"
    level = 5
    casting_time = "10 minutes"
    casting_range = "Self"
    components = ('V', 'S', 'M')
    materials = ("A focus worth at least 1,000 gp, such as a crystal ball, "
                 "a silver mirror, or a font filled with holy water")
    duration = "Concentration, Up to 10 minutes"
    magic_school = "Divination"
    classes = ('Bard', 'Cleric', 'Druid', 'Warlock', 'Wizard')


class CompelledDuel(Spell):
    """You attempt to compel a creature into a duel.  One creature that you can
    see within range must make a Wisdom saving throw. On a failed save, the
    creature is drawn to you, compelled by your divine demand. For the
    duration, it has disadvantage on attack rolls against creatures other than
    you, and must make a Wisdom saving throw each time it attempts to move to a
    space that is more than 30 feet away from you; if it succeeds on this
    saving throw, this spell doesn’t restrict the target’s movement for that
    turn.

    The spell ends if you attack any other creature, if you cast a spell that
    targets a hostile creature other than the target, if a creature friendly to
    you damages the target or casts a harmful spell on it, or if you end your
    turn more than 30 feet away from the target.

    """
    name = "Compelled Duel"
    level = 1
    casting_time = "1 bonus action"
    casting_range = "30 feet"
    components = ("V",)
    duration = "Concentration, up to 10 minutes"
    magic_school = "Enchantment"
    classes = ('Paladin',)


class CircleOfPower(Spell):
    """Divine energy radiates from you, distorting and diffusing magical energy
    within 30 feet of you.  Until the spell ends, the sphere moves with you,
    centered on you. For the duration, each friendly creature in the area
    (including you) has advantage on saving throws against spells and other
    magical effects.

    Additionally, when an affected creature succeeds on a saving throw made
    against a spell or magical effect that allows it to make a saving throw to
    take only half damage, it instead takes no damage if it succeeds on the
    saving throws.  """
    name = "Circle of Power"
    level = 5
    casting_time = '1 action'
    casting_range = 'Self (30 foot radius)'
    components = ('V',)
    duration = "Concentration, up to 10 minutes"
    magic_school = "Abjuration"
    classes = ('Paladin',)


class Geas(Spell):
    """You place a magical command on a creature that you can see within range, forcing
     it to carry out some service or refrain from some action or course of activity 
    as you decide. If the creature can understand you, it must succeed on a Wisdom 
    saving throw or become charmed by you for the duration. While the creature is 
    charmed by you, it takes 5d10 psychic damage each time it acts in a manner 
    directly counter to your instructions, but no more than once each day. A 
    creature that can't understand you is unaffected by the spell.
    
    You can issue 
    any command you choose, short of an activity that would result in certain death.
     Should you issue a suicidal command, the spell ends.
    
    You can end the spell 
    early by using an action to dismiss it. A remove curse, greater restoration, or 
    wish spell also ends it.
    
    At Higher Levels: When you cast this spell using a 
    spell slot of 7th or 8th level, the duration is 1 year. When you cast this spell
     using a spell slot of 9th level, the spell lasts until it is ended by one of 
    the spells mentioned above.
    """
    name = "Geas"
    level = 5
    casting_time = "1 minute"
    casting_range = "60 feet"
    components = ('V',)
    materials = ""
    duration = "30 days"
    magic_school = "Enchantment"
    classes = ('Bard', 'Cleric', 'Druid', 'Paladin', 'Wizard')
class BestowCurse(Spell):
    """You touch a creature, and that creature must succeed on a Wisdom saving throw or
     become cursed for the duration of the spell. When you cast this spell, choose 
    the nature of the curse from the following options.
    
    • Choose one ability score.
     While cursed, the target has disadvantage on ability checks and saving throws 
    made with that ability score.
    
    • While cursed, the target has disadvantage on 
    attack rolls against you.
    
    • While cursed, the target must make a Wisdom saving 
    throw at the start of each of its turns. If it fails, it wastes its action that 
    turn doing nothing.
    
    • While the target is cursed, your attacks and spells deal 
    an extra 1d8 necrotic damage to the target.
    
    A remove curse spell ends this 
    effect. At the DM's option, you may choose an alternative curse effect, but it 
    should be no more powerful than those described above. The DM has final say on 
    such a curse's effect.
    
    At Higher Levels: If you cast this spell using a spell 
    slot of 4th level or higher, the duration is concentration, up to 10 minutes. If
     you use a spell slot of 5th level or higher, the duration is 8 hours. If you 
    use a spell slot of 7th level or higher, the duration is 24 hours. If you use a 
    9th level spell slot, the spell lasts until it is dispelled. Using a spell slot 
    of 5th level or higher grants a duration that doesn't require concentration.
    """
    name = "Bestow Curse"
    level = 3
    casting_time = "1 action"
    casting_range = "Touch"
    components = ('V', 'S')
    materials = ""
    duration = "Concentration, Up to 1 minute"
    magic_school = "Necromancy"
    classes = ('Bard', 'Cleric', 'Wizard')


class Fear(Spell):
    """You project a phantasmal image of a creature's worst fears. Each creature in a 
    30-foot cone must succeed on a Wisdom saving throw or drop whatever it is 
    holding and become frightened for the duration.
    
    While frightened by this spell,
     a creature must take the Dash action and move away from you by the safest 
    available route on each of its turns, unless there is nowhere to move. If the 
    creature ends its turn in a location where it doesn't have line of sight to you,
     the creature can make a Wisdom saving throw. On a successful save, the spell 
    ends for that creature.
    """
    name = "Fear"
    level = 3
    casting_time = "1 action"
    casting_range = "Self (30-foot radius)"
    components = ('V', 'S', 'M')
    materials = "A white feather or the heart of a hen"
    duration = "Concentration, Up to 1 minute"
    magic_school = "Illusion"
    classes = ('Bard', 'Sorcerer', 'Warlock', 'Wizard')


class DominateBeast(Spell):
    """You attempt to beguile a beast that you can see within range. It must succeed on
     a Wisdom saving throw or be charmed by you for the duration. If you or 
    creatures that are friendly to you are fighting it, it has advantage on the 
    saving throw.
    
    While the beast is charmed, you have a telepathic link with it as
     long as the two of you are on the same plane of existence. You can use this 
    telepathic link to issue commands to the creature while you are conscious (no 
    action required), which it does its best to obey. You can specify a simple and 
    general course of action, such as Attack that creature, Run over there, or Fetch
     that object. If the creature completes the order and doesn't receive further 
    direction from you, it defends and preserves itself to the best of its ability.
    
    
    You can use your action to take total and precise control of the target. Until
     the end of your next turn, the creature takes only the actions you choose, and 
    doesn't do anything that you don't allow it to do. During this time, you can 
    also cause the creature to use a reaction, but this requires you to use your own
     reaction as well.
    
    Each time the target takes damage, it makes a new Wisdom 
    saving throw against the spell. If the saving throw succeeds, the spell ends.
    
    
    At Higher Levels: When you cast this spell with a 5th-level spell slot, the 
    duration is concentration, up to 10 minutes. When you use a 6th-level spell 
    slot, the duration is concentration, up to 1 hour. When you use a spell slot of 
    7th level or higher, the duration is concentration, up to 8 hours.
    """
    name = "Dominate Beast"
    level = 4
    casting_time = "1 action"
    casting_range = "60 feet"
    components = ('V', 'S')
    materials = ""
    duration = "Concentration, Up to 1 minute"
    magic_school = "Enchantment"
    classes = ('Druid', 'Sorcerer')


class Cloudkill(Spell):
    """You create a 20-foot-radius sphere of poisonous, yellow-green fog centered on a 
    point you choose within range. The fog spreads around corners. It lasts for the 
    duration or until strong wind disperses the fog, ending the spell. Its area is 
    heavily obscured.
    
    When a creature enters the spell's area for the first time on
     a turn or starts its turn there, that creature must make a Constitution saving 
    throw. The creature takes 5d8 poison damage on a failed save, or half as much 
    damage on a successful one. Creatures are affected even if they hold their 
    breath or don't need to breathe.
    
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
    materials = ""
    duration = "Concentration, Up to 10 minutes"
    magic_school = "Conjuration"
    classes = ('Sorcerer', 'Wizard')


class CalmEmotions(Spell):
    """You attempt to suppress strong emotions in a group of people. Each humanoid in a
     20-foot-radius sphere centered on a point you choose within range must make a 
    Charisma saving throw a creature can choose to fail this saving throw if it 
    wishes. If a creature fails its saving throw, choose one of the following two 
    effects.
    
    You can suppress any effect causing a target to be charmed or 
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
    materials = ""
    duration = "Concentration, Up to 1 minute"
    magic_school = "Enchantment"
    classes = ('Bard', 'Cleric')


class HypnoticPattern(Spell):
    """You create a twisting pattern of colors that weaves through the air inside a 
    30-foot cube within range. The pattern appears for a moment and vanishes. Each 
    creature in the area who sees the pattern must make a Wisdom saving throw. On a 
    failed save, the creature becomes charmed for the duration. While charmed by 
    this spell, the creature is incapacitated and has a speed of 0.
    
    The spell ends 
    for an affected creature if it takes any damage or if someone else uses an 
    action to shake the creature out of its stupor.
    """
    name = "Hypnotic Pattern"
    level = 3
    casting_time = "1 action"
    casting_range = "120 feet"
    components = ('S', 'M')
    materials = "A glowing stick of incense or a crystal vial filled with phosphorescent material"
    duration = "Concentration, Up to 1 minute"
    magic_school = "Illusion"
    classes = ('Bard', 'Sorcerer', 'Warlock', 'Wizard')


class OtilukesResilientSphere(Spell):
    """A sphere of shimmering force encloses a creature or object of Large size or
     smaller within range. An unwilling creature must make a Dexterity saving
     throw. On a failed save, the creature is enclosed for the duration.
    
    Nothing---not physical objects, energy, or other spell effects---can pass
    through the barrier, in or out, though a creature in the sphere can breathe
    there. The sphere is immune to all damage, and a creature or object inside
    can’t be damaged by attacks or effects originating from outside, nor can a
    creature inside the sphere damage anything outside it.

    The sphere is weightless and just large enough to contain the creature or
    object inside. An enclosed creature can use its action to push against the
    sphere’s walls and thus roll the sphere at up to half the creature’s
    speed. Similarly, the globe can be picked up and moved by other creatures.

    A disintegrate spell targeting the globe destroys it without harming
    anything inside it.  """
    name = "Otiluke's Resilient Sphere"
    level = 4
    casting_time = "1 action"
    casting_range = "30 feet"
    components = ('V', 'S', 'M')
    materials = ("a hemispherical piece of clear crystal and a matching "
                 "hemispherical piece of gum arabic")
    duration = "Concentration, up to 1 minute"
    magic_school = "Evocation"
    classes = ('Wizard',)


class WallOfForce(Spell):
    """An invisible wall of force springs into existence at a point you choose within 
    range. The wall appears in any orientation you choose, as a horizontal or 
    vertical barrier or at an angle. It can be free floating or resting on a solid 
    surface. You can form it into a hemispherical dome or a sphere with a radius of 
    up to 10 feet, or you can shape a flat surface made up of ten 10-foot-by-10-foot
     panels. Each panel must be contiguous with another panel. In any form, the wall
     is 1/4 inch thick. It lasts for the duration. If the wall cuts through a 
    creature's space when it appears, the creature is pushed to one side of the wall
     (your choice which side).
    
    Nothing can physically pass through the wall. It is 
    immune to all damage and can't be dispelled by dispel magic. A disintegrate 
    spell destroys the wall instantly, however. The wall also extends into the 
    Ethereal Plane, blocking ethereal travel through the wall.
    """
    name = "Wall Of Force"
    level = 5
    casting_time = "1 action"
    casting_range = "120 feet"
    components = ('V', 'S', 'M')
    materials = "A pinch of powder made by crushing a clear gemstone"
    duration = "Concentration, Up to 10 minutes"
    magic_school = "Evocation"
    classes = ('Wizard',)


