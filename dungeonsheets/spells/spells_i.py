from .spells import Spell


class IceKnife(Spell):
    """(a drop of water or piece of ice)
    You create a shard of ice and fling it at one 
    creature within range. Make a ranged spell attack against the target. On a hit, 
    the target takes 1d10 piercing damage. Hit or miss, the shard then explodes. The
     target and each creature within 5 feet of the point where the ice exploded must
     succeed on a Dexterity saving throw or take 2d6 cold damage.
    At Higher Levels. 
    When you cast this spell using a spell slot of 2nd level or higher, the cold 
    damage increases by 1d6 for each slot level above 1st.
    """
    name = "Ice Knife"
    level = 1
    casting_time = "1 action"
    casting_range = "60 feet"
    components = ('S', 'M')
    materials = """"""
    duration = "Instantaneous"
    ritual = False
    magic_school = "Conjuration"
    classes = ('Druid', 'Sorcerer', 'Wizard')


class IceStorm(Spell):
    """A hail of rock-hard ice pounds to the ground in a 20-foot-radius, 40-foot-high 
    cylinder centered on a point within range. 
    Each creature in the cylinder must 
    make a Dexterity saving throw. A creature takes 2d8 bludgeoning damage and 4d6 
    cold damage on a failed save, or half as much damage on a successful one.
    
    
    Hailstones turn the storm’s area of effect into difficult terrain until the end 
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
    materials = """A pinch of dust and a few drops of water"""
    duration = "Instantaneous"
    ritual = False
    magic_school = "Evocation"
    classes = ('Druid', 'Sorcerer', 'Wizard')


class Identify(Spell):
    """You choose one object that you must touch throughout the casting of the spell. 
    If it is a magic item or some other magic-imbued object, you learn its 
    properties and how to use them, whether it requires attunement to use, and how 
    many charges it has, if any. You learn whether any spells are affecting the item
     and what they are. If the item was created by a spell, you learn which spell 
    created it.
    
    If you instead touch a creature throughout the casting, you learn 
    what spells, if any, are currently affecting it.
    """
    name = "Identify"
    level = 1
    casting_time = "1 minute"
    casting_range = "Touch"
    components = ('V', 'S', 'M')
    materials = """A pearl worth at least 100 gp and an owl feather"""
    duration = "Instantaneous"
    ritual = True
    magic_school = "Divination"
    classes = ('Bard', 'Wizard')


class IllusoryDragon(Spell):
    """By gathering threads of shadow material from the Shadowfell, you create a Huge 
    shadowy dragon in an unoccupied space that you can see within range. The 
    illusion lasts for the spell’s duration and occupies its space, as if it were a 
    creature.
    When the illusion appears, any of your enemies that can see it must 
    succeed on a Wisdom saving throw or become frightened of it for 1 minute. If a 
    frightened creature ends its turn in a location where it doesn’t have line of 
    sight to the illusion, it can repeat the saving throw, ending the effect on 
    itself on a success.
    As a bonus action on your turn, you can move the illusion 
    up to 60 feet. At any point during its movement, you can cause it to exhale a 
    blast of energy in a 60-foot cone originating from its space. When you create 
    the dragon, choose a damage type: acid, cold, fire, lightning, necrotic, or 
    poison. Each creature in the cone must make an Intelligence saving throw, taking
     '7d6 damage of the
    chosen damage type on a failed save, or half as much damage 
    on a successful one.
    The illusion is tangible because of the shadow stuff used 
    to create it, but attacks miss it automatically. it succeeds on all saving 
    throws, and it is immune to all damage and conditions. A creature that uses an 
    action to examine the dragon can determine that it is an illusion by succeeding 
    on an Intelligence (Investigation) check against your spell save DC. If a 
    creature discerns the illusion for what it is, the creature can see through it 
    and has advantage on saving throws against its breath.
    """
    name = "Illusory Dragon"
    level = 8
    casting_time = "1 action"
    casting_range = "120 feet"
    components = ('S',)
    materials = """"""
    duration = "Concentration, up to 1 minute"
    ritual = False
    magic_school = "Illusion"
    classes = ('Wizard',)


class IllusoryScript(Spell):
    """You write on parchment, paper, or some other suitable writing material and imbue
     it with a potent illusion that lasts for the duration.
    
    To you and any 
    creatures you designate when you cast the spell, the writing appears normal, 
    written in your hand, and conveys whatever meaning you intended when you wrote 
    the text. To all others, the writing appears as if it were written in an unknown
     or magical script that is unintelligible. Alternatively, you can cause the 
    writing to appear to be an entirely different message, written in a different 
    hand and language, though the language must be one you know.
    
    Should the spell 
    be dispelled, the original script and the illusion both disappear.
    A creature 
    with truesight can read the hidden message.
    """
    name = "Illusory Script"
    level = 1
    casting_time = "1 minute"
    casting_range = "Touch"
    components = ('S', 'M')
    materials = """A lead-based ink worth at least 10 gp, which the spell consumes"""
    duration = "10 days"
    ritual = True
    magic_school = "Illusion"
    classes = ('Bard', 'Warlock', 'Wizard')


class Immolation(Spell):
    """Flames wreathe one creature you can see within range. The target must make a 
    Dexterity saving throw. It takes 8d6 fire damage on a failed save, or half as 
    much damage on a successful one. On a failed save, the target also burns for the
     spell’s duration. The burning target sheds bright light in a 30-foot radius and
     dim light for an additional 30 feet. At the end of each of its turns, the 
    target repeats the saving throw. It takes 4d6 fire damage on a failed save, and 
    the spell ends on a successful one. These magical flames can’t be extinguished 
    by nonmagical means.
    If damage from this spell kills a target, the target is 
    turned to ash.
    """
    name = "Immolation"
    level = 5
    casting_time = "1 action"
    casting_range = "90 feet"
    components = ('V',)
    materials = """"""
    duration = "Concentration, up to 1 minute"
    ritual = False
    magic_school = "Evocation"
    classes = ('Sorcerer', 'Wizard')


class Imprisonment(Spell):
    """You create a magical restraint to hold a creature that you can see within range.
    
    The target must succeed on a Wisdom saving throw or be bound by the spell; if 
    it succeeds, it is immune to this spell if you cast it again. While affected by 
    this spell, the creature doesn't need to breathe, eat, or drink, and it doesn’t 
    age. Divination spells can’t locate or perceive the target.
    
    When you cast the 
    spell, you choose one of the following forms of imprisonment. 
    
    Burial
    The 
    target is entombed far beneath the earth in a sphere of magical force that is 
    just large enough to contain the target. Nothing can pass through the 
    sphere, nor can any creature teleport or use planar travel to get into or out of
     it.
    The special component for this version of the spell is a small mithral orb.
    
    
    Chaining
    Heavy chains, firmly rooted in the ground, hold the target in place. 
    The target is restrained until the spell ends, and it can’t move or be moved by 
    any means until then.
    The special component for this version of the spell is 
    a fine chain of precious metal.
    
    Hedged Prison
    The spell transports the target 
    into a tiny demiplane that is warded against teleportation and planar travel. 
    The demiplane can be a labyrinth, a cage, a tower, or any similar confined 
    structure or area of your choice.
    The special component for this version of the 
    spell is a miniature representation of the prison made from jade.
    
    Minimus 
    Containment
    The target shrinks to a height of 1 inch and is imprisoned inside a 
    gemstone or similarobject. Light can pass through the gemstone 
    normally (allowing the target to see out and other creatures to see in), but 
    nothing else can pass through, even by means of teleportation or planar travel. 
    The gemstone can’t be cut or broken while the spell remains in effect.
    The 
    special component for this version of the spell is a large, transparent 
    gemstone, such as a corundum, diamond, or ruby.
    
    Slumber
    The target falls asleep
     and can’t be awoken.
    The special component for this version of the 
    spell consists of rare soporific herbs. 
    
    Ending the Spell
    During the casting of
     the spell, in any of its versions, you can specify a condition that will cause 
    the spell to end and release the target. The condition can be as specific or as 
    elaborate as you choose, but the DM must agree that the condition is reasonable 
    and has a likelihood of coming to pass. The conditions can be based on a 
    creature’s name, identity, or deity but otherwise must be based on 
    observable actions or qualities and not based on intangibles such as level, 
    class, or hit points.
    
    A dispel magic spell can end the spell only if it is 
    cast as a 9th-level spell, targeting either the prison or the special component 
    used to create it.
    
    You can use a particular special component to create only 
    one prison at a time. If you cast the spell again using the same component, the 
    target of the first casting is immediately freed from its binding.
    """
    name = "Imprisonment"
    level = 9
    casting_time = "1 minute"
    casting_range = "30 feet"
    components = ('V', 'S', 'M')
    materials = """A vellum depiction or a carved statuette in the likeness of the target, and a special component that varies according to the version of the spell you choose, worth at least 500 gp per hit die of the target"""
    duration = "Until dispelled"
    ritual = False
    magic_school = "Abjuration"
    classes = ('Warlock', 'Wizard')


class IncendiaryCloud(Spell):
    """A swirling cloud of smoke shot through with white-hot embers appears in a 
    20-foot-radius sphere centered on a point within range.
    The cloud spreads around
     corners and is heavily obscured. It lasts for the duration or until a wind of 
    moderate or greater speed (at least 10 miles per hour) disperses it.
    
    When the 
    cloud appears, each creature in it must make a Dexterity saving throw. A 
    creature takes 10d8 fire damage on a failed save, or half as much damage on a 
    successful one. A creature must also make this saving throw when it enters the 
    spell’s area for the first time on a turn or ends its turn there.
    
    The cloud 
    moves 10 feet directly away from you in a direction that you choose at the start
     of each of your turns.
    """
    name = "Incendiary Cloud"
    level = 8
    casting_time = "1 action"
    casting_range = "150 feet"
    components = ('V', 'S')
    materials = """"""
    duration = "Concentration, up to 1 minute"
    ritual = False
    magic_school = "Conjuration"
    classes = ('Sorcerer', 'Wizard')


class InfernalCalling(Spell):
    """Uttering a dark incantation, you summon a devil from the Nine Hells. You choose 
    the devil’s type, which must be one of challenge rating 6 or lower, such as a 
    barbed devil or a bearded devil. The devil appears in an unoccupied space that 
    you can see within range. The devil disappears when it drops to 0 hit points or 
    when the spell ends.
    The devil is unfriendly toward you and your companions. 
    Roll initiative for the devil, which has its own turns. It is under the Dungeon 
    Master’s control and acts according to its nature on each of its turns, which 
    might result in its attacking you if it thinks it can prevail, or trying to 
    tempt you to undertake an evil act in exchange for limited service. The DM has 
    the creature’s statistics.
    On each of your turns, you can try to issue a verbal 
    command to the devil (no action required by you). It obeys the command if the 
    likely outcome is in accordance with its desires, especially if the result would
     draw you toward evil. Otherwise, you must make a Charisma (Deception, 
    Intimidation, or Persuasion) check contested by its Wisdom (Insight) check. You 
    make the check with advantage if you say the devil’s true name. Ifyour check 
    fails, the devil becomes immune to your verbal commands for the duration of the 
    spell, though it can still carry out your commands if it chooses. If your check 
    succeeds, the devil carries out your command— such as “attack my enemies,” 
    “explore the room ahead," or “bear this message to the queen"—until it completes
     the activity, at which point it returns to you to report having done so.
    If 
    your concentration ends before the spell reaches its full duration, the devil 
    doesn‘t disappear if it has become immune to your verbal commands. Instead, it 
    acts in whatever manner it chooses for 3d6 minutes, and then it disappears.
    If 
    you possess an individual devil’s talisman, you can summon that devil if it is 
    of the appropriate challenge
    rating plus 1, and it obeys all your commands, with
     no Charisma checks required.
    
    At Higher Levels: When you cast this spell using 
    a spell slot of 6th level or higher, the challenge rating increases by 1 for 
    each slot level above 5th.
    """
    name = "Infernal Calling"
    level = 5
    casting_time = "1 minute"
    casting_range = "90 feet"
    components = ('V', 'S', 'M')
    materials = """A ruby worth at least 999 gp"""
    duration = "Concentration, up to 1 hour"
    ritual = False
    magic_school = "Conjuration"
    classes = ('Warlock', 'Wizard')


class Infestation(Spell):
    """You cause a cloud of mites, fleas, and other parasites to appear momentarily on 
    one creature you can see within range. The target must succeed on a Constitution
     saving throw, or it takes 1d6 poison damage and moves 5 feet in a random 
    direction if it can move and its speed is at least 5 feet. Roll a d4 for the 
    direction: 1., north; 2, south; 3, east; or 4, west. This movement doesn’t 
    provoke opportunity attacks, and if the direction rolled is blocked, the target 
    doesn't move.
    The spell’s damage increases by 1d6 when you reach 5th level 
    (2d6), 11th level (3d6), and 17th level (4d6).
    """
    name = "Infestation"
    level = 0
    casting_time = "1 action"
    casting_range = "30 feet"
    components = ('V', 'S', 'M')
    materials = """A living flea"""
    duration = "Instantaneous"
    ritual = False
    magic_school = "Conjuration"
    classes = ('Druid', 'Sorcerer', 'Warlock', 'Wizard')


class InflictWounds(Spell):
    """Make a melee spell attack against a creature you can reach. On a hit, the target
     takes 3d10 necrotic damage.
    
    At Higher Levels: When you cast this spell using a
     spell slot of 2nd level or higher, the damage increases by 1d10 for each slot 
    level above 1st.
    """
    name = "Inflict Wounds"
    level = 1
    casting_time = "1 action"
    casting_range = "Touch"
    components = ('V', 'S')
    materials = """"""
    duration = "Instantaneous"
    ritual = False
    magic_school = "Necromancy"
    classes = ('Cleric',)


class InsectPlague(Spell):
    """Swarming, biting locusts fill a 20-foot-radius sphere centered on a point you 
    choose within range. The sphere spreads around corners. The sphere remains for 
    the duration, and its area is lightly obscured. The sphere’s area is difficult 
    terrain.
    
    When the area appears, each creature in it must make a Constitution 
    saving throw. A creature takes 4d10 piercing damage on a failed save, or half as
     much damage on a successful one. A creature must also make this saving throw 
    when it enters the spell’s area for the first time on a turn or ends its turn 
    there.
    
    At Higher Levels: When you cast this spell using a spell slot of 6th 
    level or higher, the damage increases by 1d10 for each slot level above 5th.
    """
    name = "Insect Plague"
    level = 5
    casting_time = "1 action"
    casting_range = "300 feet"
    components = ('V', 'S', 'M')
    materials = """A few grains of sugar, some kernels of grain, and a smear of fat"""
    duration = "Concentration, up to 10 minutes"
    ritual = False
    magic_school = "Conjuration"
    classes = ('Cleric', 'Druid', 'Sorcerer')


class InvestitureOfFlame(Spell):
    """Flames race across your body, shedding bright light in a 30-foot radius and dim 
    light for an additional 30 feet for the spell’s duration. The flames don’t harm 
    you. Until the spell ends, you gain the following benefits:
    • You are immune to 
    fire damage and have resistance to cold damage.
    • Any creature that moves within
     5 feet of you for the first time on a turn or ends its turn there takes 1d10 
    fire damage.
    • You can use your action to create a line of fire 15 feet long and
     5 feet wide extending from you in a direc- tion you choose. Each creature in 
    the line must make a Dexterity saving throw. A creature takes 4d8 fire damage on
     a failed save, or half as much damage on a successful one.
    """
    name = "Investiture Of Flame"
    level = 6
    casting_time = "1 action"
    casting_range = "Self"
    components = ('V', 'S')
    materials = """"""
    duration = "Concentration, up to 10 minutes"
    ritual = False
    magic_school = "Transmutation"
    classes = ('Druid', 'Sorcerer', 'Warlock', 'Wizard')


class InvestitureOfIce(Spell):
    """Until the spell ends, ice rimes your body, and you gain the following benefits:
    
    • You are immune to cold damage and have resistance to fire damage.
    • You can 
    move across difficult terrain created by ice or snow without spending extra 
    movement.
    • The ground in a 10-foot radius around you is icy and is difficult 
    terrain for creatures other than you. The radius moves with you.
    • You can use 
    your action to create a 15-foot cone of freezing wind extending from your 
    outstretched hand in a direction you choose. Each creature in the cone must make
     a Constitution saving throw. A creature takes 4d6 cold damage on a failed save,
     or half as much damage on a successful one. A creature that fails its save 
    against this effect has its speed halved until the start of your next turn.
    """
    name = "Investiture Of Ice"
    level = 6
    casting_time = "1 action"
    casting_range = "Self"
    components = ('V', 'S')
    materials = """"""
    duration = "Concentration, up to 10 minutes"
    ritual = False
    magic_school = "Transmutation"
    classes = ('Druid', 'Sorcerer', 'Warlock', 'Wizard')


class InvestitureOfStone(Spell):
    """Until the spell ends, bits of rock spread across your body, and you gain the 
    following benefits:
    • You have resistance to bludgeoning, piercing, and slashing
     damage from nonmagical weapons.
    • You can use your action to create a small 
    earthquake on the ground in a 15-foot radius centered on you. Other creatures on
     that ground must succeed on a Dexterity saving throw or be knocked prone.
    • You
     can move across difficult terrain made of earth or stone without spending extra
     movement. You can move through solid earth or stone as if it was air and 
    without destabilizing it, but you can’t end your movement there. If you do so, 
    you are ejected to the nearest unoccupied space, this spell ends, and you are 
    stunned until the end of your next turn.
    """
    name = "Investiture Of Stone"
    level = 6
    casting_time = "1 action"
    casting_range = "Self"
    components = ('V', 'S')
    materials = """"""
    duration = "Concentration, up to 10 minutes"
    ritual = False
    magic_school = "Transmutation"
    classes = ('Druid', 'Sorcerer', 'Warlock', 'Wizard')


class InvestitureOfWind(Spell):
    """Until the spell ends, wind whirls around you, and you gain the following 
    benefits:
    • Ranged weapon attacks made against you have disad- vantage on the 
    attack roll.
    • You gain a flying speed of 60 feet. If you are still flying when 
    the spell ends, you fall, unless you can some- how prevent it.
    • You can use 
    your action to create a 15-foot cube of swirling wind centered on a point you 
    can see within 60 feet of you. Each creature in that area must make a 
    Constitution saving throw. A creature takes 2d10 bludgeoning damage on a failed 
    save, or half as much damage on a successful one. If a Large or smaller creature
     fails the save, that creature is also pushed up to 10 feet away from the center
     of the cube.
    """
    name = "Investiture Of Wind"
    level = 6
    casting_time = "1 action"
    casting_range = "Self"
    components = ('V', 'S')
    materials = """"""
    duration = "Concentration, up to 10 minutes"
    ritual = False
    magic_school = "Transmutation"
    classes = ('Druid', 'Sorcerer', 'Warlock', 'Wizard')


class Invisibility(Spell):
    """A creature you touch becomes invisible until the spell ends. Anything the target
     is wearing or carrying is invisible as long as it is on the target’s person. 
    The spell ends for a target that attacks or casts a spell.
    
    At Higher Levels: 
    When you cast this spell using a spell slot of 3rd level or higher, you can 
    target one additional creature for each slot level above 2nd.
    """
    name = "Invisibility"
    level = 2
    casting_time = "1 action"
    casting_range = "Touch"
    components = ('V', 'S', 'M')
    materials = """An eyelash encased in gum arabic"""
    duration = "Concentration, up to 1 hour"
    ritual = False
    magic_school = "Illusion"
    classes = ('Bard', 'Sorcerer', 'Warlock', 'Wizard')


class Invulnerability(Spell):
    """You are immune to all damage until the spell ends.
    """
    name = "Invulnerability"
    level = 9
    casting_time = "1 action"
    casting_range = "Self"
    components = ('V', 'S', 'M')
    materials = """A small piece of adamantine worth at least 500 gp, which the spell consumes"""
    duration = "Concentration, up to 10 minutes"
    ritual = False
    magic_school = "Abjuration"
    classes = ('Wizard',)


