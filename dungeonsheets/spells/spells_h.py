from .spells import Spell


class HailOfThorns(Spell):
    """The next time you hit a creature with a ranged weapon attack before the spell 
    ends, this spell creates a rain of thorns that sprouts from your ranged weapon 
    or ammunition. In addition to the normal effect of the attack, the target of the
     attack and each creature within 5 feet of it must make a Dexterity saving 
    throw. A creature takes 1d10 piercing damage on a failed save, or half as much 
    damage on a successful one.
    
    At Higher Levels: If you cast this spell using a 
    spell slot of 2nd level or higher, the damage increases by 1d10 for each slot 
    level above 1st (to a maximum of 6d10).
    """
    name = "Hail Of Thorns"
    level = 1
    casting_time = "1 bonus action"
    casting_range = "Self"
    components = ('V',)
    materials = """"""
    duration = "Concentration, up to 1 minute"
    ritual = False
    magic_school = "Conjuration"
    classes = ('Ranger',)


class Hallow(Spell):
    """You touch a point and infuse an area around it with holy (or unholy) power. The 
    area can have a radius up to 60 feet, and the spell fails if the radius includes
     an area already under the effect a hallow spell. The affected area is subject 
    to the following effects.
    
    First, celestials, elementals, fey, fiends, and 
    undead can’t enter the area, nor can such creatures charm, frighten, or possess 
    creatures within it. Any creature charmed, frightened, or possessed by such a 
    creature is no longer charmed, frightened, or possessed upon entering the area. 
    You can exclude one or more of those types of creatures from this effect.
    
    
    Second, you can bind an extra effect to the area. Choose the effect from the 
    following list, or choose an effect offered by the DM. Som e of these effects 
    apply to creatures in the area; you can designate whether the effect applies to 
    all creatures, creatures that follow a specific deity or leader, or creatures of
     a specific sort, such as ores or trolls. When a creature that would be affected
     enters the spell’s area for the first time on a turn or starts its turn there, 
    it can make a Charisma saving throw. On a success, the creature ignores the 
    extra effect until it leaves the area.
    
    Courage
    Affected creatures can’t be 
    frightened while in the area. 
    
    Darkness
    Darkness fills the area. Normal light, 
    as well as magical light created by spells of a lower level than the slot you 
    used to cast this spell, can’t illuminate the area.
    
    Daylight
    Bright light fills
     the area. Magical darkness created by spells of a lower level than the slot you
     used to cast this spell can’t extinguish the light.
    
    Energy Protection
    Affected
     creatures in the area have resistance to one damage type of your choice, except
     for bludgeoning, piercing, or slashing.
    
    Energy Vulnerability
    Affected 
    creatures in the area have vulnerability to one damage type of your choice, 
    except for bludgeoning, piercing, or slashing.
    
    Everlasting Rest
    Dead bodies 
    interred in the area can’t be turned into undead.
    
    Extradimensional Interference
    
    Affected creatures can’t move or travel using teleportation or by 
    extradimensional or interplanar means.
    
    Fear
    Affected creatures are frightened 
    while in the area.
    
    Silence
    No sound can emanate from within the area, and no 
    sound can reach into it.
    
    Tongues
    Affected creatures can communicate with any 
    other creature in the area, even if they don’t share a common language.
    """
    name = "Hallow"
    level = 5
    casting_time = "24 hours"
    casting_range = "Touch"
    components = ('V', 'S', 'M')
    materials = """Herbs, oils, and incense worth at least 1,000 gp, which the spell consumes"""
    duration = "Until dispelled"
    ritual = False
    magic_school = "Evocation"
    classes = ('Cleric',)


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
    components = ('V', 'S', 'M')
    materials = """A stone, a twig, and a bit of green plant"""
    duration = "24 hours"
    ritual = False
    magic_school = "Illusion"
    classes = ('Bard', 'Druid', 'Warlock', 'Wizard')


class Harm(Spell):
    """You unleash a virulent disease on a creature that you can see within range.
    The 
    target must make a Constitution saving throw. On a failed save, it takes 14d6 
    necrotic damage, or half as much damage on a successful save. The damage can’t 
    reduce the target’s hit points below 1. If the target fails the saving throw, 
    its hit point maximum is reduced for 1 hour by an amount equal to the necrotic 
    damage it took. Any effect that removes a disease allows a creature’s hit point 
    maximum to return to normal before that time passes.
    """
    name = "Harm"
    level = 6
    casting_time = "1 action"
    casting_range = "60 feet"
    components = ('V', 'S')
    materials = """"""
    duration = "Instantaneous"
    ritual = False
    magic_school = "Necromancy"
    classes = ('Cleric',)


class Haste(Spell):
    """Choose a willing creature that you can see within range. Until the spell ends, 
    the target’s speed is doubled, it gains a +2 bonus to AC, it has advantage on 
    Dexterity saving throws, and it gains an additional action on each of its turns.
     That action can be used only to take the Attack (one weapon attack only), Dash,
     Disengage, Hide, or Use an Object action.
    
    When the spell ends, the target 
    can’t move or take actions until after its next turn, as a wave of lethargy 
    sweeps over it.
    """
    name = "Haste"
    level = 3
    casting_time = "1 action"
    casting_range = "30 feet"
    components = ('V', 'S', 'M')
    materials = """A shaving of licorice root"""
    duration = "Concentration, up to 1 minute"
    ritual = False
    magic_school = "Transmutation"
    classes = ('Sorcerer', 'Wizard')


class Heal(Spell):
    """Choose a creature that you can see within range. A surge of positive energy 
    washes through the creature, causing it to regain 70 hit points. The spell also 
    ends blindness, deafness, and any diseases affecting the target. This spell has 
    no effect on constructs or undead.
    
    At Higher Levels: When you cast this spell 
    using aspell slot of 7th level or higher, the amount of healing increases by 10 
    for each slot level above 6th.
    """
    name = "Heal"
    level = 6
    casting_time = "1 action"
    casting_range = "60 feet"
    components = ('V', 'S')
    materials = """"""
    duration = "Instantaneous"
    ritual = False
    magic_school = "Evocation"
    classes = ('Cleric', 'Druid')


class HealingSpirit(Spell):
    """You call forth a nature spirit to soothe the wounded. The intangible spirit 
    appears in a space that is a 5-foot cube you can see within range. The spirit 
    looks like a transparent beast or fey (your choice). Until the spell ends, 
    whenever you or a creature you can see moves into the spirits space for the 
    first time on a turn or starts its turn there, you can cause the spirit to 
    restore ld6 hit points to that creature (no action required). The spirit can’t 
    heal constructs or undead. As a bonus action on your turn, you can move the 
    Spirit up to 30 feet to a space you can see.
    
    At Higher Levels: When you cast 
    this spell using a spell slot of 3rd level or higher, the healing increases 1d6 
    for each slot level above 2nd.
    """
    name = "Healing Spirit"
    level = 2
    casting_time = "1 bonus action"
    casting_range = "60 feet"
    components = ('V', 'S')
    materials = """"""
    duration = "Concentration, up to 1 minute"
    ritual = False
    magic_school = "Conjuration"
    classes = ('Druid', 'Ranger')


class HealingWord(Spell):
    """A creature of your choice that you can see within range regains hit points equal
     to 1d4 + your spellcasting ability modifier.
    This spell has no effect on undead
     or constructs.
    
    At Higher Levels: When you cast this spell using a spell slot 
    of 2nd level or higher, the healing increases by 1d4 for each slot level above 
    1st.
    """
    name = "Healing Word"
    level = 1
    casting_time = "1 bonus action"
    casting_range = "60 feet"
    components = ('V',)
    materials = """"""
    duration = "Instantaneous"
    ritual = False
    magic_school = "Evocation"
    classes = ('Bard', 'Cleric', 'Druid')


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
    components = ('V', 'S', 'M')
    materials = """A piece of iron and a flame"""
    duration = "Concentration, up to 1 minute"
    ritual = False
    magic_school = "Transmutation"
    classes = ('Bard', 'Druid')


class HellishRebuke(Spell):
    """Reaction: you are being damaged by a creature within 60 feet of you that you can
     see.
    
    You point your finger, and the creature that damaged you is momentarily 
    surrounded by hellish flames. The creature must make a Dexterity saving throw. 
    It takes 2d10 fire damage on a failed save, or half as much damage on a 
    successful one.
    
    At Higher Levels: When you cast this spell using a spell slot 
    of 2nd level or higher, the damage increases by 1d10 for each slot level above 
    1st.
    """
    name = "Hellish Rebuke"
    level = 1
    casting_time = "Special"
    casting_range = "60 feet"
    components = ('V', 'S')
    materials = """"""
    duration = "Instantaneous"
    ritual = False
    magic_school = "Evocation"
    classes = ('Warlock',)


class HeroesFeast(Spell):
    """You bring forth a great feast, including magnificent food and drink. The feast 
    takes 1 hour to consume and disappears at the end of that time, and the 
    beneficial effects don’t set in until this hour is over. Up to twelve other 
    creatures can partake of the feast.
    
    A creature that partakes of the feast gains
     several benefits. The creature is cured of all diseases and poison, becomes 
    immune to poison and being frightened, and makes all Wisdom saving throws with 
    advantage. Its hit point maximum also increases by 2d10, and it gains the same 
    number of hit points. These benefits last for 24 hours.
    """
    name = "Heroes Feast"
    level = 6
    casting_time = "10 minutes"
    casting_range = "30 feet"
    components = ('V', 'S', 'M')
    materials = """A gem-encrusted bowl worth at least 1,000 gp, which the spell consumes"""
    duration = "Instantaneous"
    ritual = False
    magic_school = "Conjuration"
    classes = ('Cleric', 'Druid')


class Heroism(Spell):
    """A willing creature you touch is imbued with bravery.
    Until the spell ends, the 
    creature is immune to being frightened and gains temporary hit points equal to 
    your spellcasting ability modifier at the start of each of its turns. When the 
    spell ends, the target loses any remaining temporary hit points from this spell.
    
    
    At Higher Levels: When you cast this spell using a spell slot of 2nd level or 
    higher, you can target one additional creature for each slot level above 1st.
    """
    name = "Heroism"
    level = 1
    casting_time = "1 action"
    casting_range = "Touch"
    components = ('V', 'S')
    materials = """"""
    duration = "Concentration, up to 1 minute"
    ritual = False
    magic_school = "Enchantment"
    classes = ('Bard', 'Paladin')


class Hex(Spell):
    """You place a curse on a creature that you can see within range. Until the spell 
    ends, you deal an extra 1d6 necrotic damage to the target whenever you hit it 
    with an attack. Also, choose one ability when you cast the spell. The target has
     disadvantage on ability checks made with the chosen ability.
    
    If the target 
    drops to 0 hit points before this spell ends, you can use a bonus action on a 
    subsequent turn of yours to curse a new creature.
    
    A remove curse cast on the 
    target ends this spell early.
    
    At Higher Levels: When you cast this spell using 
    a spell slot of 3rd or 4th level, you can maintain your concentration on the 
    spell for up to 8 hours.
    When you use a spell slot of 5th level or higher, you 
    can maintain your concentration on the spell for up to 24 hours.
    """
    name = "Hex"
    level = 1
    casting_time = "1 bonus action"
    casting_range = "90 feet"
    components = ('V', 'S', 'M')
    materials = """The petrified eye of a newt"""
    duration = "Concentration, up to 1 hour"
    ritual = False
    magic_school = "Enchantment"
    classes = ('Warlock',)


class HoldMonster(Spell):
    """Choose a creature that you can see within range. The target must succeed on a 
    Wisdom saving throw or be paralyzed for the duration. This spell has no effect 
    on undead. At the end of each of its turns, the target can make another Wisdom 
    saving throw. On a success, the spell ends on the target.
    
    At Higher Levels: 
    When you cast this spell using a spell slot of 6th level or higher, you can 
    target one additional creature for each slot level above 5th. The creatures must
     be within 30 feet of each other when you target them.
    """
    name = "Hold Monster"
    level = 5
    casting_time = "1 action"
    casting_range = "90 feet"
    components = ('V', 'S', 'M')
    materials = """A small, straight piece of iron"""
    duration = "Concentration, up to 1 minute"
    ritual = False
    magic_school = "Enchantment"
    classes = ('Bard', 'Sorcerer', 'Warlock', 'Wizard')


class HoldPerson(Spell):
    """Choose a humanoid that you can see within range. The target must succeed on a 
    Wisdom saving throw or be paralyzed for the duration. At the end of each of its 
    turns, the target can make another Wisdom saving throw. On a success, the spell 
    ends on the target.
    
    At Higher Levels: When you cast this spell using a spell 
    slot of 3rd level or higher, you can target one additional humanoid for each 
    slot level above 2nd. The humanoids must be within 30 feet of each other when 
    you target them.
    """
    name = "Hold Person"
    level = 2
    casting_time = "1 action"
    casting_range = "60 feet"
    components = ('V', 'S', 'M')
    materials = """A small, straight piece of iron"""
    duration = "Concentration, up to 1 minute"
    ritual = False
    magic_school = "Enchantment"
    classes = ('Bard', 'Cleric', 'Druid', 'Sorcerer', 'Warlock', 'Wizard')


class HolyAura(Spell):
    """Divine light washes out from you and coalesces in a soft radiance in a 30-foot 
    radius around you.
    Creatures of your choice in that radius when you cast this 
    spell shed dim light in a 5-foot radius and have advantage on all saving throws,
     and other creatures have disadvantage on attack rolls against them until the 
    spell ends. In addition, when a fiend or an undead hits an affected creature 
    with a melee attack, the aura flashes with brilliant light. The attacker must 
    succeed on a Constitution saving throw or be blinded until the spell ends.
    """
    name = "Holy Aura"
    level = 8
    casting_time = "1 action"
    casting_range = "Self"
    components = ('V', 'S', 'M')
    materials = """A tiny reliquary worth at least 1,000 gp containing a sacred relic, such as a scrap of cloth from a saint’s robe or a piece of parchment from a religious text"""
    duration = "Concentration, up to 1 minute"
    ritual = False
    magic_school = "Abjuration"
    classes = ('Cleric',)


class HolyWeapon(Spell):
    """You imbue a weapon you touch with holy power. Until the spell ends, the weapon 
    emits bright light in a 30—foot radius and dim light for an additional 30 feet. 
    In addition, weapon attacks made with it deal an extra 2d8 radiant damage on a 
    hit. If the weapon isn’t already a magic weapon, it becomes one for the 
    duration. As a bonus action on your turn, you can dismiss this spell and cause 
    the weapon to emit a burst of radiance. Each creature of your choice that you 
    can see within 30 feet ofyou must make a Constitution saving throw. On a failed 
    save, a creature takes 4d8 radiant damage, and it is blinded for 1 minute. On a 
    successful save, a creature takes half as much damage and isn’t blinded. At the 
    end of each Ofits turns, a blinded creature can make a Constitution saving 
    throw, ending the effect on itselfon a success.
    """
    name = "Holy Weapon"
    level = 5
    casting_time = "1 bonus action"
    casting_range = "Touch"
    components = ('V', 'S')
    materials = """"""
    duration = "Concentration, up to 1 hour"
    ritual = False
    magic_school = "Evocation"
    classes = ('Cleric', 'Paladin')


class HungerOfHadar(Spell):
    """You open a gateway to the dark between the stars, a region infested with unknown
     horrors. A 20-foot-radius sphere of blackness and bitter cold appears, centered
     on a point with range and lasting for the duration. This void is filled with a 
    cacophony of soft whispers and slurping noises that can be heard up to 30 feet 
    away. No light, magical or otherwise, can illuminate the area, and creatures 
    fully within the area are blinded.
    
    The void creates a warp in the fabric of 
    space, and the area is difficult terrain. Any creature that starts its turn in 
    the area takes 2d6 cold damage. Any creature that ends its turn in the area must
     succeed on a Dexterity saving throw or take 2d6 acid damage as milky, 
    otherwordly tentacles rub against it.
    """
    name = "Hunger Of Hadar"
    level = 3
    casting_time = "1 action"
    casting_range = "150 feet"
    components = ('V', 'S', 'M')
    materials = """A pickled octopus tentacle"""
    duration = "Concentration, up to 1 minute"
    ritual = False
    magic_school = "Conjuration"
    classes = ('Warlock',)


class HuntersMark(Spell):
    """You choose a creature you can see within range and mystically mark it as your 
    quarry.
    Until the spell ends, you deal an extra 1d6 damage to the target 
    whenever you hit it with a weapon attack, and you have advantage on any Wisdom 
    (Perception) or Wisdom (Survival) check you make to find it. If the target drops
     to 0 hit points before this spell ends, you can use a bonus action on a 
    subsequent turn of yours to mark a new creature.
    
    At Higher Levels: When you 
    cast this spell using a spell slot of 3rd or 4th level, you can maintain your 
    concentration on the spell for up to 8 hours.
    When you use a spell slot of 5th 
    level or higher, you can maintain your concentration on the spell for up to 24 
    hours.
    """
    name = "Hunters Mark"
    level = 1
    casting_time = "1 bonus action"
    casting_range = "90 feet"
    components = ('V',)
    materials = """"""
    duration = "Concentration, up to 1 hour"
    ritual = False
    magic_school = "Divination"
    classes = ('Ranger',)


class HypnoticPattern(Spell):
    """You create a twisting pattern of colors that weaves through the air inside a 
    30-foot cube within range.
    The pattern appears for a moment and vanishes. Each 
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
    materials = """A glowing stick of incense or a crystal vial filled with phosphorescent material"""
    duration = "Concentration, up to 1 minute"
    ritual = False
    magic_school = "Illusion"
    classes = ('Bard', 'Sorcerer', 'Warlock', 'Wizard')


