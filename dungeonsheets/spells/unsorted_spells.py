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


class Nondetection(Spell):
    """For the duration, you hide a target that you touch from divination magic. The 
    target can be a willing creature or a place or an object no larger than 10 feet 
    in any dimension. The target can't be targeted by any divination magic or 
    perceived through magical scrying sensors.
    """
    name = "Nondetection"
    level = 3
    casting_time = "1 action"
    casting_range = "Touch"
    components = ('V', 'S', 'M')
    materials = ("A pinch of diamond dust worth 25 gp sprinkled over the "
                 "target, which the spell consumes")
    duration = "8 hours"
    magic_school = "Abjuration"
    classes = ('Bard', 'Ranger', 'Wizard')


class Confusion(Spell):
    """This spell assaults and twists creatures' minds, spawning delusions and 
    provoking uncontrolled actions. Each creature in a 10-foot-radius sphere 
    centered on a point you choose within range must succeed on a Wisdom saving 
    throw when you cast this spell or be affected by it.
    
    An affected target can't 
    take reactions and must roll a d10 at the start of each of its turns to 
    determine its behavior for that turn.
    
    1: The creature uses all its movement to 
    move in a random direction. To determine the direction, roll a d8 and assign a 
    direction to each die face. The creature doesn't take an action this turn.
    
    2-6:
     The creature doesn't move or take actions this turn.
    
    7-8: The creature uses 
    its action to make a melee attack against a randomly determined creature within 
    its reach. If there is no creature within its reach, the creature does nothing 
    this turn.
    
    9-10: The creature can act and move normally.
    
    At the end of its 
    turns, an affected target can make a Wisdom saving throw. If it succeeds, this 
    effect ends for that target.
    
    At Higher Levels: When you cast this spell using a
     spell slot of 5th level or higher, the radius of the sphere increases by 5 feet
     for each slot above 4th.
    """
    name = "Confusion"
    level = 4
    casting_time = "1 action"
    casting_range = "90 feet"
    components = ('V', 'S', 'M')
    materials = "Three nut shells"
    duration = "Concentration, Up to 1 minute"
    magic_school = "Enchantment"
    classes = ('Bard', 'Druid', 'Sorcerer', 'Wizard')


class LegendLore(Spell):
    """Name or describe a person, place, or object. The spell brings to your mind a 
    brief summary of the significant lore about the thing you named. The lore might 
    consist of current tales, forgotten stories, or even secret lore that has never 
    been widely known. If the thing you named isn't of legendary importance, you 
    gain no information.
    
    The more information you already have about the thing, the
     more precise and detailed the information you receive is. The information you 
    learn is accurate but might be couched in figurative language. For example, if 
    you have a mysterious magic axe on hand, the spell might yield this information 
    - Woe to the evildoer whose hand touches the axe, for even the haft slices the 
    hand of the evil ones. Only a true Child of Stone, lover and beloved of Moradin,
     may awaken the true powers of the axe, and only with the sacred word Rudnogg on
     the lips.
    """
    name = "Legend Lore"
    level = 5
    casting_time = "10 minutes"
    casting_range = "Self"
    components = ('V', 'S', 'M')
    materials = ("Incense worth at least 250 gp, which the spell consumes, and"
                 "four ivory strips worth at least 50 gp each")
    duration = "Instantaneous"
    magic_school = "Divination"
    classes = ('Bard', 'Cleric', 'Wizard')


class FaerieFire(Spell):
    """Each object in a 20-foot cube within range is outlined in blue, green, or violet
     light (your choice). Any creature in the area when the spell is cast is also 
    outlined in light if it fails a Dexterity saving throw. For the duration, 
    objects and affected creatures shed dim light in a 10-foot radius.
    
    Any attack 
    roll against an affected creature or object has advantage if the attacker can 
    see it, and the affected creature or object can't benefit from being invisible.
    """
    name = "Faerie Fire"
    level = 1
    casting_time = "1 action"
    casting_range = "60 feet"
    components = ('V',)
    materials = ""
    duration = "Concentration, Up to 1 minute"
    magic_school = "Evocation"
    classes = ('Bard', 'Druid')


class ScorchingRay(Spell):
    """You create three rays of fire and hurl them at targets within range. You can 
    hurl them at one target or several.
    
    Make a ranged spell attack for each ray. On
     a hit, the target takes 2d6 fire damage.
    
    At Higher Levels: When you cast this 
    spell using a spell slot of 3rd level or higher, you create one additional ray 
    for each slot level above 2nd.
    """
    name = "Scorching Ray"
    level = 2
    casting_time = "1 action"
    casting_range = "120 feet"
    components = ('V', 'S')
    materials = ""
    duration = "Instantaneous"
    magic_school = "Evocation"
    classes = ('Sorcerer', 'Wizard')


class Daylight(Spell):
    """A 60-foot-radius sphere of light spreads out from a point you choose within 
    range. The sphere is bright light and sheds dim light for an additional 60 feet.
    
    
    If you chose a point on an object you are holding or one that isn't being worn
     or carried, the light shines from the object with and moves with it. Completely
     covering the affected object with an opaque object, such as a bowl or a helm, 
    blocks the light.
    
    If any of this spell's area overlaps with an area of darkness
     created by a spell of or lower, the spell that created the darkness is 
    dispelled.
    """
    name = "Daylight"
    level = 3
    casting_time = "1 action"
    casting_range = "60 feet"
    components = ('V', 'S')
    materials = ""
    duration = "1 hour"
    magic_school = "Evocation"
    classes = ('Cleric', 'Druid', 'Paladin', 'Ranger', 'Sorcerer')


class SpikeGrowth(Spell):
    """The ground in a 20-foot radius centered on a point within range twists and 
    sprouts hard spikes and thorns. The area becomes difficult terrain for the 
    duration. When a creature moves into or within the area, it takes 2d4 piercing 
    damage for every 5 feet it travels.
    
    The transformation of the ground is 
    camouflaged to look natural. Any creature that can't see the area at the time 
    the spell is cast must make a Wisdom (Perception) check against your spell save 
    DC to recognize the terrain as hazardous before entering it.
    """
    name = "Spike Growth"
    level = 2
    casting_time = "1 action"
    casting_range = "150 feet"
    components = ('V', 'S', 'M')
    materials = "Seven sharp thorns or seven small twigs, each sharpened to a point"
    duration = "Concentration, Up to 10 minutes"
    magic_school = "Transmutation"
    classes = ('Druid', 'Ranger')


class WindWall(Spell):
    """A wall of strong wind rises from the ground at a point you choose within range. 
    You can make the wall up to 50 feet long, 15 feet high, and 1 foot thick. You 
    can shape the wall in any way you choose so long as it makes one continuous path
     along the ground. The wall lasts for the duration.
    
    When the wall appears, each
     creature within its area must make a Strength saving throw. A creature takes 
    3d8 bludgeoning damage on a failed save, or half as much damage on a successful 
    one.
    
    The strong wind keeps fog, smoke, and other gases at bay. Small or smaller
     flying creatures or objects can't pass through the wall. Loose, lightweight 
    materials brought into the wall fly upward. Arrows, bolts, and other ordinary 
    projectiles launched at targets behind the wall are deflected upward and 
    automatically miss. (Boulders hurled by giants or siege engines, and similar 
    projectiles, are unaffected.) Creatures in gaseous form can't pass through it.
    """
    name = "Wind Wall"
    level = 3
    casting_time = "1 action"
    casting_range = "120 feet"
    components = ('V', 'S', 'M')
    materials = "A tiny fan and a feather of exotic origin"
    duration = "Concentration, Up to 1 minute"
    magic_school = "Evocation"
    classes = ('Druid', 'Ranger')


class GraspingVine(Spell):
    """You conjure a vine that sprouts from the ground in an unoccupied space of
    your choice that you can see within range. When you cast this spell, you
    can direct the vine to lash out at a creature within 30 feet of it that you
    can see. That creature must succeed on a Dexterity saving throw or be
    pulled 20 feet directly toward the vine.

    Until the spell ends, you can direct the vine to lash out at the same
    creature or another one as a bonus action on each of your turns. 
    
    """
    name = "Grasping Vine"
    level = 4
    casting_time = '1 bonus action'
    casting_range = '30 feet'
    components = ('V', 'S')
    duration = 'Concentration, up to 1 minute'
    magic_school = "Conjuration"
    classes = ("Druid", 'Ranger')



class MirrorImage(Spell):
    """Three illusory duplicates of yourself appear in your space. Until the spell 
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
    components = ('V', 'S')
    materials = ""
    duration = "1 minute"
    magic_school = "Illusion"
    classes = ('Sorcerer', 'Warlock', 'Wizard')


class PassWithoutTrace(Spell):
    """A veil of shadows and silence radiates from you, masking you and your companions
     from detection. For the duration, each creature you choose within 30 feet of 
    you (including you) has a +10 bonus to Dexterity (Stealth) checks and can’t be 
    tracked except by magical means. A creature that receives this bonus leaves 
    behind no tracks or other traces of its passage.
    """
    name = "Pass Without Trace"
    level = 2
    casting_time = "1 action"
    casting_range = "Self"
    components = ('V', 'S', 'M')
    materials = "Ashes from a burned leaf of mistletoe and a sprig of spruce"
    duration = "Concentration, Up to 1 hour"
    magic_school = "Abjuration"
    classes = ('Druid', 'Ranger')


class Polymorph(Spell):
    """This spell transforms a creature with at least 1 hit point that you can see 
    within range into a new form. An unwilling creature must make a Wisdom saving 
    throw to avoid the effect. A shapechanger automatically succeeds on this saving 
    throw.
    
    The transformation lasts for the duration, or until the target drops to 
    0 hit points or dies. The new form can be any beast whose challenge rating is 
    equal to or less than the target's (or the target's level, if it doesn't have a 
    challenge rating). The target's game statistics, including mental ability 
    scores, are replaced by the statistics of the chosen beast. It retains its 
    alignment and personality.
    
    The target assumes the hit points of its new form. 
    When it reverts to its normal form, the creature returns to the number of hit 
    points it had before it transformed. If it reverts as a result of dropping to 0 
    hit points, any excess damage carries over to its normal form. As long as the 
    excess damage doesn't reduce the creature's normal form to 0 hit points, it 
    isn't knocked unconscious.
    
    The creature is limited in the actions it can 
    perform by the nature of its new form, and it can't speak, cast spells, or take 
    any other action that requires hands or speech.
    
    The target's gear melds into 
    the new form. The creature can't activate, use, wield, or otherwise benefit from
     any of its equipment.
    """
    name = "Polymorph"
    level = 4
    casting_time = "1 action"
    casting_range = "60 feet"
    components = ('V', 'S', 'M')
    materials = "A caterpillar cocoon"
    duration = "Concentration, Concentration, Up to 1 hour"
    magic_school = "Transmutation"
    classes = ('Bard', 'Druid', 'Sorcerer', 'Wizard')


class ModifyMemory(Spell):
    """You attempt to reshape another creature's memories. One creature that you can 
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
    
    At Higher Levels: If 
    you cast this spell using a spell slot of 6th level or higher, you can alter the
     target's memories of an event that took place up to 7 days ago (6th level), 30 
    days ago (7th level), 1 year ago (8th level), or any time in the creature's past
     (9th level).
    """
    name = "Modify Memory"
    level = 5
    casting_time = "1 action"
    casting_range = "30 feet"
    components = ('V', 'S')
    materials = ""
    duration = "Concentration, Up to 1 minute"
    magic_school = "Enchantment"
    classes = ('Bard', 'Wizard')


class DivineFavor(Spell):
    """Your prayer empowers you with divine radiance. Until the spell ends, your weapon
     attacks deal and extra 1d4 radiant damage on a hit.
    """
    name = "Divine Favor"
    level = 1
    casting_time = "1 bonus action"
    casting_range = "Self"
    components = ('V', 'S')
    materials = ""
    duration = "Concentration, Up to 1 minute"
    magic_school = "Evocation"
    classes = ('Paladin',)


class SpiritualWeapon(Spell):
    """You create a floating, spectral weapon within range that lasts for the duration 
    or until you cast this spell again. When you cast the spell, you can make a 
    melee spell attack against a creature within 5 feet of the weapon. On a hit, the
     target takes force damage equal to 1d8 + your spellcasting ability modifier.
    
    
    As a bonus action on your turn, you can move the weapon up to 20 feet and repeat
     the attack against a creature within 5 feet of it.
    
    The weapon can take 
    whatever form you choose. Clerics of deities who are associated with a 
    particular weapon (as St. Cuthbert is known for his mace and Thor for his 
    hammer) make this spell's effect resemble that weapon.
    
    At Higher Levels: When 
    you cast this spell using a spell slot 3rd level of or higher, the damage 
    increases by 1d8 for every two slot levels above the 2nd.
    """
    name = "Spiritual Weapon"
    level = 2
    casting_time = "1 bonus action"
    casting_range = "60 feet"
    components = ('V', 'S')
    materials = ""
    duration = "1 minute"
    magic_school = "Evocation"
    classes = ('Cleric',)


class CrusadersMantle(Spell):
    """Holy power radiates from you in an aura with a 30-foot radius, awakening
    boldness in friendly creatures. Until the spell ends, the aura moves with
    you, centered on you. While in the aura, each nonhostile creature in the
    aura (including you) deals an extra 1d4 radiant damage when it hits with a
    weapon attack.

    """
    name = "Crusader's Mantle"
    level = 3
    casting_time = "1 action"
    casting_range = "Self"
    components = ("V",)
    duration = "Concentration, up to 1 minute"
    magic_school = "Evocation"
    classes = ("Paladin",)


class NystulsMagicAura(Spell):
    """You place an illusion on a creature or an object you touch so that
    divination spells reveal false information about it.  The target can be a
    willing creature or an object that isn’t being carried or worn by another
    creature.

    When you cast the spell, choose one or both of the following effects. The
    effect lasts for the duration. If you cast this spell on the same creature
    or object every day for 30 days, placing the same effect on it each time,
    the illusion lasts until it is dispelled.

    **False Aura**: You change the way the target appears to spells and magical
    effects, such as detect magic, that detect magical auras. You can make a
    nonmagical object appear magical, a magical object appear nonmagical, or
    change the object’s magical aura so that it appears to belong to a specific
    school of magic that you choose. When you use this effect on an object, you
    can make the false magic apparent to any creature that handles the item.

    **Mask**: You change the way the target appears to spells and magical
    effects that detect creature types, such as a paladin’s Divine Sense or the
    trigger of a sym bol spell. You choose a creature type and other spells and
    magical effects treat the target as if it were a creature of that type or
    of that alignment.

    """
    name = "Nystul's Magic Aura"
    level = 2
    casting_time = "1 action"
    casting_range = "touch"
    components = ("V", "S", "M")
    materials = "a small square of silk"
    duration = "24 hours"
    magic_school = "Illusion"
    classes = ("Wizard",)


class MagicCircle(Spell):
    """You create a 10-foot-radius, 20-foot-tall cylinder of magical energy centered on
     a point on the ground that you can see within range. Glowing runes appear 
    wherever the cylinder intersects with the floor or other surface.
    
    Choose one or
     more of the following types of creatures - celestials, elementals, fey, fiends,
     or undead. The circle affects a creature of the chosen type in the following 
    ways.
    
    • The creature can't willingly enter the cylinder by nonmagical means. If
     the creature tries to use teleportation or interplanar travel to do so, it must
     first succeed on a Charisma saving throw.
    
    • The creature has disadvantage on 
    attack rolls against targets within the cylinder.
    
    • Targets within the cylinder
     can't be charmed, frightened, or possessed by the creature.
    
    When you cast this
     spell, you can elect to cause its magic to operate in the reverse direction, 
    preventing a creature of the specified type from leaving the cylinder and 
    protecting targets outside it.
    
    At Higher Levels: When you cast this spell using
     a spell slot of 4th level or higher, the duration increases by 1 hour for each 
    slot level above 3rd.
    """
    name = "Magic Circle"
    level = 3
    casting_time = "1 minute"
    casting_range = "10 feet"
    components = ('V', 'S', 'M')
    materials = ("Holy water or powdered silver and iron worth at least 100 "
                 "gp, which the spell consumes")
    duration = "1 hour"
    magic_school = "Abjuration"
    classes = ('Cleric', 'Paladin', 'Warlock', 'Wizard')
                 
                 
class LeomundsSecretChest(Spell):
    """You hide a chest, and all its contents, on the Ethereal Plane.  You must
    touch the chest and the miniature replica that serves as a material
    component for the spell. The chest can contain up to 12 cubic feet of
    nonliving material (3 feet by 2 feet by 2 feet).

    While the chest remains on the Ethereal Plane, you can use an action and
    touch the replica to recall the chest. It appears in an unoccupied space on
    the ground within 5 feet of you. You can send the chest back to the
    Ethereal Plane by using an action and touching both the chest and the
    replica.

    After 60 days, there is a cumulative 5 percent chance per day that the
    spell’s effect ends. This effect ends if you cast this spell again, if the
    smaller replica chest is destroyed, or if you choose to end the spell as an
    action. If the spell ends and the larger chest is on the Ethereal Plane, it
    is irretrievably lost.

    """
    name = "Leomund's Secret Chest"
    level = 4
    casting_time = '1 action'
    casting_range = 'Touch'
    components = ("V", "S", "M")
    materials = ("an exquisite chest, 3 feet by 2 feet by 2 feet, constructed "
                 "from rare materials worth at least 5,000 gp, and a Tiny "
                 "replica made from the same materials worth at least 50 gp")
    duration = "instantaneous"
    magic_school = "Conjuration"
    classes = ("Wizard",)



class PlanarBinding(Spell):
    """With this spell, you attempt to bind a celestial, an elemental, a fey, or a 
    fiend to your service. The creature must be within range for the entire casting 
    of the spell. (Typically, the creature is first summoned into the center of an 
    inverted magic circle in order to keep it trapped while this spell is cast.) At 
    the completion of the casting, the target must make a Charisma saving throw. On 
    a failed save, it is bound to serve you for the duration. If the creature was 
    summoned or created by another spell, that spell's duration is extended to match
     the duration of this spell.
    
    A bound creature must follow your instructions to 
    the best of its ability. You might command the creature to accompany you on an 
    adventure, to guard a location, or to deliver a message. The creature obeys the 
    letter of your instructions, but if the creature is hostile to you, it strives 
    to twist your words to achieve its own objectives. If the creature carries out 
    your instructions completely before the spell ends, it travels to you to report 
    this fact if you are on the same plane of existence. If you are on a different 
    plane of existence, it returns to the place where you bound it and remains there
     until the spell ends.
    
    At Higher Levels: When you cast this spell using a spell
     slot of a higher level, the duration increases to 10 days with a 6th-level 
    slot, to 30 days with a 7th-level slot, to 180 days with an 8th-level slot, and 
    to a year and a day with a 9th-level spell slot.
    """
    name = "Planar Binding"
    level = 5
    casting_time = "1 hour"
    casting_range = "60 feet"
    components = ('V', 'S', 'M')
    materials = "A jewel worth at least 1,000 gp, which the spell consumes"
    duration = "24 hours"
    magic_school = "Abjuration"
    classes = ('Bard', 'Cleric', 'Druid', 'Wizard')


class TeleportationCircle(Spell):
    """As you cast the spell, you draw a 10-foot-diameter circle on the ground 
    inscribed with sigils that link your location to a permanent teleportation 
    circle of your choice whose sigil sequence you know and that is on the same 
    plane of existence as you. A shimmering portal opens within the circle you drew 
    and remains open until the end of your next turn. Any creature that enters the 
    portal instantly appears within 5 feet of the destination circle or in the 
    nearest unoccupied space if that space is occupied.
    
    Many major temples, guilds,
     and other important places have permanent teleportation circles inscribed 
    somewhere within their confines. Each such circle includes a unique sigil 
    sequence - a string of magical runes arranged in a particular pattern. When you 
    first gain the ability to cast this spell, you learn the sigil sequences for two
     destinations on the Material Plane, determined by the DM. You can learn 
    additional sigil sequences during your adventures⁠. You can commit a new sigil 
    sequence to memory after studying it for 1 minute.
    
    You can create a permanent 
    teleportation circle by casting this spell in the same location every day for 
    one year. You need not use the circle to teleport⁠ when you cast the spell in 
    this way.
    """
    name = "Teleportation Circle"
    level = 5
    casting_time = "1 minute"
    casting_range = "10 ft"
    components = ('V', 'M')
    materials = ("Rare chalks and inks infused with precious gems with 50 gp, "
                 "which the spell consumes")
    duration = "1 round"
    magic_school = "Conjuration"
    classes = ('Bard', ' Sorcerer', ' Wizard')


class SearingSmite(Spell):
    """The next time you hit a creature with a melee weapon attack during the spell’s 
    duration, your weapon flares with white-hot intensitity, and the attack deals an
     extra 1d6 fire damage to the target and causes the target to ignite in flames.
    
    
    At the start of each of its turns until the spell ends, the target must make a
     Constitution saving throw. On a failed save, it takes 1d6 fire damage. On a 
    successful save, the spells ends. If the target or a creature within 5 feet of 
    it uses an action to put out the flames, or if some other effect douses the 
    flames (such as the target being submerged in water), the spell ends.
    
    At Higher
     Levels: When you cast this spell using a spell slot of 2nd level or higher, the
     initial extra damage dealt by the attack increases by 1d6 for each slot
    """
    name = "Searing Smite"
    level = 1
    casting_time = "1 bonus action"
    casting_range = "Self"
    components = ('V',)
    materials = """"""
    duration = "Concentration, up to 1 minute"
    magic_school = "Evocation"
    classes = ('Paladin',)


class HeatMetal(Spell):
    """Choose a manufactured metal object, such as a metal weapon or a suit of heavy or
     medium metal armor, that you can see within range. You cause the object to glow
     red-hot. Any creature in physical contact with the object takes 2d8 fire damage
     when you cast the spell. Until the spell ends, you can use a bonus action on 
    each of your subsequent turns to cause this damage again.
    
    If a creature is 
    holding or wearing the object and takes the damage from it, the creature must 
    succeed on a Constitution saving throw or drop the object if it can. If it 
    doesn’t drop the object, it has disadvantage on attack rolls and ability checks 
    until the start of your next turn.
    
    At Higher Levels: When you cast this spell 
    using a spell slot of 3rd level or higher, the damage increases by 1d8 for each 
    slot level above 2nd.
    """
    name = "Heat Metal"
    level = 2
    casting_time = "1 action"
    casting_range = "60 feet"
    components = ('V', 's', 'm')
    materials = """A piece of iron and a flame"""
    duration = "Concentration, up to 1 minute"
    magic_school = "Transmutation"
    classes = ('Bard', 'Druid')


class Fabricate(Spell):
    """You convert raw materials into products of the same material. 
    For example, you 
    can fabricate a wooden bridge from a clump of trees, a rope from a patch of 
    hemp, and clothes from flax or wool. 
    
    Choose raw materials that you can see 
    within range. You can fabricate a Large or smaller object (contained within a 
    10-foot cube, or eight connected 5-foot cubes), given a sufficient quantity of 
    raw material. If you are working with metal, stone, or another mineral 
    substance, however, the fabricated object can be no larger than Medium 
    (contained within a single 5-foot cube). The quality of objects made by the 
    spell is commensurate with the quality of the raw materials. 
    
    Creatures or 
    magic items can’t be created or transmuted by this spell. You also can’t use it 
    to create items that ordinarily require a high degree of craftsmanship, such as 
    jewelry, weapons, glass, or armor, unless you have proficiency with the type of 
    artisan’s tools used to craft such objects.
    """
    name = "Fabricate"
    level = 4
    casting_time = "10 minutes"
    casting_range = "120 feet"
    components = ('V', 's')
    materials = """"""
    duration = "Instantaneous"
    magic_school = "Transmutation"
    classes = ('Wizard',)


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
    components = ('V', 's', 'm')
    materials = """A tiny piece of matter of the same type of the item you plan to create"""
    duration = "Special"
    magic_school = "Illusion"
    classes = ('Sorcerer', 'Wizard')


class Slow(Spell):
    """You alter time around up to six creatures of your choice in a 40-foot cube 
    within range. Each target must succeed on a Wisdom saving throw or be affected 
    by this spell for the duration.
    
    An affected target’s speed is halved, it takes 
    a -2 penalty to AC and Dexterity saving throws, and it can’t use reactions. On 
    its turn, it can use either an action or a bonus action, not both. Regardless of
     the creature’s abilities or magic items, it can’t make more than one melee or 
    ranged attack during its turn.
    
    If the creature attempts to cast a spell with a 
    casting time of 1 action, roll a d20. On an 11 or higher, the spell doesn’t take
     effect until the creature’s next turn, and the creature must use its action on 
    that turn to complete the spell. If it can’t, the spell is wasted.
    
    A creature 
    affected by this spell makes another Wisdom saving throw at the end of its turn.
     On a successful save, the effect ends for it.
    """
    name = "Slow"
    level = 3
    casting_time = "1 action"
    casting_range = "120 feet"
    components = ('V', 's', 'm')
    materials = """A drop of molasses"""
    duration = "Concentration, up to 1 minute"
    magic_school = "Transmutation"
    classes = ('Sorcerer', 'Wizard')


class WaterBreathing(Spell):
    """This spell grants up to ten willing creatures you can see within range the 
    ability to breathe underwater until the spell ends. Affected creatures also 
    retain their normal mode of respiration.
    """
    name = "Water Breathing"
    level = 3
    casting_time = "1 action"
    casting_range = "30 feet"
    components = ('V', 's', 'm')
    materials = """A short reed or piece of straw"""
    duration = "24 hours"
    ritual = True
    magic_school = "Transmutation"
    classes = ('Druid', 'Ranger', 'Sorcerer', 'Wizard')


class WaterWalk(Spell):
    """This spell grants the ability to move across any liquid surface – such as water,
     acid, mud, snow, quicksand, or lava – as if it were harmless solid ground 
    (creatures crossing molten lava can still take damage from the heat).
    Up to ten 
    willing creatures you can see within range gain this ability for the duration.
    
    
    If you target a creature submerged in a liquid, the spell carries the target to 
    the surface of the liquid at a rate of 60 feet per round.
    """
    name = "Water Walk"
    level = 3
    casting_time = "1 action"
    casting_range = "30 feet"
    components = ('V', 's', 'm')
    materials = """A piece of cork"""
    duration = "1 hour"
    ritual = True
    magic_school = "Transmutation"
    classes = ('Cleric', 'Druid', 'Ranger', 'Sorcerer')


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
    components = ('V', 's', 'm')
    materials = """Burning incense for air, soft clay for earth, sulfur and phosphorus for fire, or water and sand for water"""
    duration = "Concentration, up to 1 hour"
    ritual = False
    magic_school = "Conjuration"
    classes = ('Druid', 'Wizard')


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
    components = ('V', 's')
    materials = """"""
    duration = "Instantaneous"
    ritual = False
    magic_school = "Conjuration"
    classes = ('Cleric', 'Paladin')


class HallucinatoryTerrain(Spell):
    """You make natural terrain in a 150-foot cube in range look, sound, and smell like
     some other sort of natural terrain. Thus, open fields or a road can be made to 
    resemble a swamp, hill, crevasse, or some other difficult or impassable terrain.
     A pond can be made to seem like a grassy meadow, a precipice like a gentle 
    slope, or a rock-strewn gully like a wide and smooth road. Manufactured 
    structures, equipment, and creatures within the area aren’t changed in 
    appearance.
    
    The tactile characteristics of the terrain are unchanged, so 
    creatures entering the area are likely to see through the illusion. If the 
    difference isn’t obvious by touch, a creature carefully examining the illusion 
    can attempt an Intelligence (Investigation) check against your spell save DC to 
    disbelieve it. A creature who discerns the illusion for what it is, sees it as a
     vague image superimposed on the terrain.
    """
    name = "Hallucinatory Terrain"
    level = 4
    casting_time = "10 minutes"
    casting_range = "300 feet"
    components = ('V', 's', 'm')
    materials = """A stone, a twig, and a bit of green plant"""
    duration = "24 hours"
    ritual = False
    magic_school = "Illusion"
    classes = ('Bard', 'Druid', 'Warlock', 'Wizard')


class MeldIntoStone(Spell):
    """You step into a stone object or surface large enough to fully contain your body,
     melding yourself and all the equipment you carry with the stone for the 
    duration.
    Using your movement, you step into the stone at a point you can touch.
     Nothing of your presence remains visible or otherwise detectable by nonmagical 
    senses.
    
    While merged with the stone, you can’t see what occurs outside it, and 
    any Wisdom (Perception) checks you make to hear sounds outside it are made with 
    disadvantage. You remain aware of the passage of time and can cast spells on 
    yourself while merged in the stone. You can use your movement to leave the stone
     where you entered it, which ends the spell. You otherwise can’t move.
    
    Minor 
    physical damage to the stone doesn’t harm you, but its partial destruction or a 
    change in its shape (to the extent that you no longer fit within it) expels you 
    and deals 6d6 bludgeoning damage to you. The stone’s complete destruction (or 
    transmutation into a different substance) expels you and deals 50 bludgeoning 
    damage to you. If expelled, you fall prone in an unoccupied space closest to 
    where you first entered.
    """
    name = "Meld Into Stone"
    level = 3
    casting_time = "1 action"
    casting_range = "Touch"
    components = ('V', 's')
    materials = """"""
    duration = "8 hours"
    ritual = True
    magic_school = "Transmutation"
    classes = ('Cleric', 'Druid')


class StoneShape(Spell):
    """You touch a stone object of Medium size or smaller or a section of stone no more
     than 5 feet in any dimension and form it into any shape that suits your 
    purpose. So, for example, you could shape a large rock into a weapon, idol, or 
    coffer, or make a small passage through a wall, as long as the wall is less than
     5 feet thick. You could also shape a stone door or its frame to seal the door 
    shut. The object you create can have up to two hinges and a latch, but finer 
    mechanical detail isn’t possible.
    """
    name = "Stone Shape"
    level = 4
    casting_time = "1 action"
    casting_range = "Touch"
    components = ('V', 's', 'm')
    materials = """Soft clay, which must be worked into roughly the desired shape of the stone object"""
    duration = "Instantaneous"
    ritual = False
    magic_school = "Transmutation"
    classes = ('Cleric', 'Druid', 'Wizard')


class Stoneskin(Spell):
    """This spell turns the flesh of a willing creature you touch as hard as stone. 
    Until the spell ends, the target has resistance to nonmagical bludgeoning, 
    piercing, and slashing damage.
    """
    name = "Stoneskin"
    level = 4
    casting_time = "1 action"
    casting_range = "Touch"
    components = ('V', 's', 'm')
    materials = """Diamond dust worth 100 gp, which the spell consumes"""
    duration = "Concentration, up to 1 hour"
    ritual = False
    magic_school = "Abjuration"
    classes = ('Druid', 'Ranger', 'Sorcerer', 'Wizard')


class StinkingCloud(Spell):
    """You create a 20-foot-radius sphere of yellow, nauseating gas centered on a point
     within range. The cloud spreads around corners, and its area is heavily 
    obscured. The cloud lingers in the air for the duration.
    
    Each creature that is 
    completely within the cloud at the start of its turn must make a Constitution 
    saving throw against poison. On a failed save, the creature spends its action 
    that turn retching and reeling. Creatures that don’t need to breathe or are 
    immune to poison automatically succeed on this saving throw.
    
    A moderate wind 
    (at least 10 miles per hour) disperses the cloud after 4 rounds. A strong wind 
    (at least 20 miles per hour) disperses it after 1 round.
    """
    name = "Stinking Cloud"
    level = 3
    casting_time = "1 action"
    casting_range = "90 feet"
    components = ('V', 's', 'm')
    materials = """A rotten egg or several skunk cabbage leaves"""
    duration = "Concentration, up to 1 minute"
    ritual = False
    magic_school = "Conjuration"
    classes = ('Bard', 'Sorcerer', 'Wizard')


class GaseousForm(Spell):
    """You transform a willing creature you touch, along with everything it’s wearing 
    and carrying, into a misty cloud for the duration. The spell ends if the 
    creature drops to 0 hit points. An incorporeal creature isn’t affected.
    
    While 
    in this form, the target’s only method of movement is a flying speed of 10 feet.
     The target can enter and occupy the space of another creature. The target has 
    resistance to nonmagical damage, and it has advantage on Strength, Dexterity, 
    and Constitution saving throws. The target can pass through small holes, narrow 
    openings, and even mere cracks, though it treats liquids as though they were 
    solid surfaces. The target can’t fall and remains hovering in the air even when 
    stunned or otherwise incapacitated.
    
    While in the form of a misty cloud, the 
    target can’t talk or manipulate objects, and any objects it was carrying or 
    holding can’t be dropped, used, or otherwise interacted with. The target can’t 
    attack or cast spells.
    """
    name = "Gaseous Form"
    level = 3
    casting_time = "1 action"
    casting_range = "Touch"
    components = ('V', 's', 'm')
    materials = """A bit of gauze and a wisp of smoke"""
    duration = "Concentration, up to 1 hour"
    ritual = False
    magic_school = "Transmutation"
    classes = ('Sorcerer', 'Warlock', 'Wizard')
class RopeTrick(Spell):
    """You touch a length of rope that is up to 60 feet long. One end of the rope then 
    rises into the air until the whole rope hangs perpendicular to the ground. At 
    the upper end of the rope, an invisible entrance opens to an extradimensional 
    space that lasts until the spell ends.
    
    The extradimensional space can be 
    reached by climbing to the top of the rope. The space can hold as many as eight 
    Medium or smaller creatures. The rope can be pulled into the space, making the 
    rope disappear from view outside the space.
    
    Attacks and spells can’t cross 
    through the entrance into or out of the extradimensional space, but those inside
     can see out of it as if through a 3-foot-by-5-foot window centered on the rope.
    
    
    Anything inside the extradimensional space drops out when the spell ends.
    """
    name = "Rope Trick"
    level = 2
    casting_time = "1 action"
    casting_range = "Touch"
    components = ('V', 's', 'm')
    materials = """Powdered corn extract and a twisted loop of parchment"""
    duration = "1 hour"
    ritual = False
    magic_school = "Transmutation"
    classes = ('Wizard',)


class Seeming(Spell):
    """This spell allows you to change the appearance of any number of creatures that 
    you can see within range.
    You give each target you choose a new, illusory 
    appearance. An unwilling target can make a Charisma saving throw, and if it 
    succeeds, it is unaffected by this spell.
    
    The spell disguises physicial 
    appearances as well as clothing, armor, weapons, and equipment. You can make 
    each creature seem 1 foot shorter or taller and appear thin, fat, or inbetween. 
    You can’t change a target’s body type, so you must choose a form that has the 
    same basic arrangement of limbs. Otherwise, the extent of the illusion is up to 
    you. The spell lasts for the duration, unless you use your action to dismiss it 
    sooner.
    
    The changes wrought by this spell fail to hold up to physical 
    inspections. For example, if you use this spell to add a hat to a creature’s 
    outfitm objects pass through the hat, and anyone who touches it would feel 
    nothing or would feel the creature’s head and hair. If you use this spell to 
    appear thinner then you are, the hand of someone who reaches out to touch you 
    would bump into you while it was seemingly still in midair.
    
    A creature can use 
    its action to inspect a target and make an Intelligence (Investigation) check 
    against your spell save DC. If it succeeds, it becomes aware that the target is 
    disguised.
    """
    name = "Seeming"
    level = 5
    casting_time = "1 action"
    casting_range = "30 feet"
    components = ('V', 's')
    materials = """"""
    duration = "8 hours"
    ritual = False
    magic_school = "Illusion"
    classes = ('Bard', 'Sorcerer', 'Wizard')


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
    alignment. You can also set conditions for creatures that don’t trigger the 
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
    components = ('V', 's', 'm')
    materials = """Incense and powdered diamond worth at least 200 gp, which the spell consumes"""
    duration = "Until dispelled or triggered"
    ritual = False
    magic_school = "Abjuration"
    classes = ('you', 'cast', 'this', 'spell', 'using', 'a', 'spell', 'slot', 'of', '4th', 'level', 'or', 'higher', 'the', 'damage', 'of', 'an', 'explosive', 'runes', 'glyph', 'increases', 'by', '1d8', 'for', 'each', 'slot', 'level', 'above', '3rd.', 'If', 'you', 'create', 'a', 'spell', 'glyph', 'you', 'can', 'store', 'any', 'spell', 'of', 'up', 'to', 'the', 'same', 'level', 'as', 'the', 'slot', 'you', 'use', 'for', 'the', 'glyph', 'of')

class Friends(Spell):
    """For the duration, you have advantage on all Charisma checks directed at one 
    creature of your choice that isn’t hostile toward you. When the spell ends, the 
    creature realizes that you used magic to influence its mood and becomes hostile 
    toward you. A creature prone to violence might attack you. Another creature 
    might seek retribution in other ways (at the DM’s discretion), depending on the 
    nature of your interaction with it.
    """
    name = "Friends"
    level = 0
    casting_time = "1 action"
    casting_range = "Self"
    components = ('S', 'm')
    materials = """A small amount of makeup applied to the face as this spell is cast"""
    duration = "Concentration, up to 1 minute"
    ritual = False
    magic_school = "Enchantment"
    classes = ('Bard', 'Sorcerer', 'Warlock', 'Wizard')


class Wish(Spell):
    """Wish is the mightiest spell a mortal creature can cast. By simply speaking 
    aloud, you can alter the very foundations of reality in accord with your 
    desires.
    
    The basic use of this spell is to duplicate any other spell of 8th 
    level or lower. You don’t need to meet any requirements in that spell, including
     costly components. The spell simply takes effect.
    Alternatively, you can create
     one of the following effects of your choice:
    
    • You create one object of up to 
    25,000 gp in value that isn’t a magic item. The object can be no more than 300 
    feet in any dimension, and it appears in an unoccupied space you can see on the 
    ground.
    
    • You allow up to twenty creatures that you can see to regain all hit 
    points, and you end all effects on them described in the greater restoration 
    spell.
    
    • You grant up to ten creatures that you can see resistance to a damage 
    type you choose.
    
    • You grant up to ten creatures you can see immunity to a 
    single spell or other magical effect for 8 hours. For instance, you could make 
    yourself and all your com panions immune to a lich’s life drain attack.
    
    • You 
    undo a single recent event by forcing a reroll of any roll made within the last 
    round (including your last turn). Reality reshapes itself to accommodate the new
     result. For example, a wish spell could undo an opponent’s successful save, a 
    foe’s critical hit, or a friend’s failed save. You can force the reroll to be 
    made with advantage or disadvantage, and you can choose whether to use the 
    reroll or the original roll.
    
    You might be able to achieve something beyond the 
    scope of the above examples. State your wish to the DM as precisely as possible.
     The DM has great latitude in ruling what occurs in such an instance; the 
    greater the wish, the greater the likelihood that something goes wrong. This 
    spell might simply fail, the effect you desire 
    mightonlybepartlyachieved,oryoumightsuffersome unforeseen consequence as a 
    result of how you worded the wish. For example, wishing that a villain were dead
     might propel you forward in time to a period when that villain is no longer 
    alive, effectively removing you from the game. Similarly, wishing for a 
    legendary magic item or artifact might instantly transport you to the presence 
    of the item’s current owner.
    
    The stress of casting this spell to produce any 
    effect other than duplicating another spell weakens you. After enduring that 
    stress, each time you cast a spell until you finish a long rest, you take 1d10 
    necrotic damage per level of that spell. This damage can’t be reduced or 
    prevented in any way. In addition, your Strength drops to 3, if it isn’t 3 or 
    lower already, for 2d4 days. For each of those days that you spend resting and 
    doing nothing more than light activity, your remaining recovery time decreases 
    by 2 days. Finally, there is a 33 percent chance that you are unable to cast 
    wish ever again if you suffer this stress.
    """
    name = "Wish"
    level = 9
    casting_time = "1 action"
    casting_range = "Self"
    components = ('V',)
    materials = """"""
    duration = "Instantaneous"
    ritual = False
    magic_school = "Conjuration"
    classes = ('Sorcerer', 'Wizard')


class WitchBolt(Spell):
    """A beam of crackling, blue energy lances out toward a creature within range, 
    forming a sustained arc of lightning between you and the target.
    Make a ranged 
    spell attack against that creature. On a hit, the target takes 1d12 lightning 
    damage, and on each of your turns for the duration, you can use your action to 
    deal 1d12 lightning damage to the target automatically. The spell ends if you 
    use your action to do anything else. The spell also ends if the target is ever 
    outside the spell’s range or if it has total cover from you.
    
    At Higher Levels: 
    When you cast this spell using a spell slot of 2nd level or higher, the initial 
    damage increases by 1d12 for each slot level above 1st.
    """
    name = "Witch Bolt"
    level = 1
    casting_time = "1 action"
    casting_range = "30 feet"
    components = ('V', 's', 'm')
    materials = """A twig from a tree that has been struck by lightning"""
    duration = "Concentration, up to 1 minute"
    ritual = False
    magic_school = "Evocation"
    classes = ('Sorcerer', 'Warlock', 'Wizard')


