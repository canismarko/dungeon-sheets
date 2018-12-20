from .spells import Spell


class OttosIrresistibleDance(Spell):
    """Choose one creature that you can see within range. The target
    begins a comic dance in place: shuffling, tapping its feet, and
    capering for the duration. Creatures that can’t be charmed are
    immune to this spell. A dancing creature must use all its movement
    to dance without leaving its space and has disadvantage on
    Dexterity saving throws and attack rolls. While the target is
    affected by this spell, other creatures have advantage on attack
    rolls against it. As an action, a dancing creature makes a Wisdom
    saving throw to regain control of itself. On a successful save,
    the spell ends.
    
    """
    name = "Otto's Irresistible Dance"
    level = 6
    casting_time = "1 action"
    components = ('V',)
    materials = ""
    duration = "Concentration, up to 1 minute"
    magic_school = "Enchantment"
    classes = ('Bard', 'Wizard')


class Passwall(Spell):
    """A passage appears at a point of your choice that you can see on a
    wooden, plaster, or stone surface (such as a wall, a ceiling, or a
    floor) within range, and lasts for the duration. You choose the
    opening’s dimensions: up to 5 feet wide, 8 feet tall, and 20 feet
    deep. The passage creates no instability in a structure
    surrounding it. When the opening disappears, any creatures or
    objects still in the passage created by the spell are safely
    ejected to an unoccupied space nearest to the surface on which you
    cast the spell.
    
    """
    name = "Passwall"
    level = 5
    casting_time = "1 action"
    components = ('V', 'S', 'M')
    materials = "a pinch of sesame seeds"
    duration = "1 hour"
    magic_school = "Transmutation"
    classes = ('Wizard',)


class PhantasmalForce(Spell):
    """You craft an illusion that takes root in the mind of a creature
    that you can see within range. The target must make an
    Intelligence saving throw. On a failed save, you create a
    phantasmal object, creature or other visible phenomenon of your
    choice that is no larger than a 10-foot cube and that is
    perceivable only to the target for the duration. This spell has no
    effect on undead or constructs.
    
    The phantasm includes sound, temperature, and other stimuli, also
    evident only to the creature. The target can use its action to
    examine the phantasm with an Intelligence (Investigation) check
    against your spell save DC. If the check succeeds, the target
    realizes that the phantasm is an illusion, and the spell
    ends. While a target is affected by the spell, the target treats
    the phantasm as if it were real. The target rationalizes any
    illogical outcomes from interacting with the phantasm. For
    example, a target attempting to walk across a phantasmal bridge
    that spans a chasm falls once it steps onto the bridge. If the
    target survives the fall, it still believes that the bridge exists
    and comes up with some other explanation for its fall-it was
    pushed, it slipped, or a strong wind might have knocked it off.
    
    An affected target is so convinced of the phantasm's reality that
    it can even take damage from the illusion. A phantasm created to
    appear as a creature can attack the target. Similarly, a phantasm
    created to appear as fire, a pool of acid, or lava can burn the
    target. Each round on your turn, the phantasm can deal 1d6 psychic
    damage to the target if it is in the phantasm's area or within 5
    feet of the phantasm, provided that the illusion is of a creature
    or hazard that could logically deal damage, such as by
    attacking. The target perceives the damage as a type appropriate
    to the illusion.
    
    """
    name = "Phantasmal Force"
    level = 2
    casting_time = "1 action"
    casting_range = "60 feet"
    components = ('V', 'S', 'M')
    materials = "A bit of fleece"
    duration = "Concentration, up to 1 minute"
    magic_school = "Illusion"
    classes = ('Bard', 'Sorceror', 'Wizard')


class PoisonSpray(Spell):
    """You extend your hand toward a creature you can see within range and
    project a puff of noxious gas from your palm. The creature must
    succeed on a Constitution saving throw or take ``1d12`` poison
    damage. This spell’s damage increases by ``1d12`` when you reach
    5th level (``2d12``), 11th level (``3d12``), and 17th level
    (``4d12``).
    
    """
    name = "Poison Spray"
    level = 0
    casting_time = "1 action"
    components = ('V', 'S')
    materials = ""
    duration = "Instantaneous"
    magic_school = "Conjuration"
    classes = ()


class PowerWordKill(Spell):
    """You utter a word of power that can compel one creature you can see
    within range to die instantly. If the creature you choose has 100
    hit points or fewer, it dies. Otherwise, the spell has no
    effect.
    
    """
    name = "Power Word Kill"    
    level = 9
    casting_time = "1 action"
    components = ('V',)
    materials = ""
    duration = "Instantaneous"
    magic_school = "Enchantment"
    classes = ('Bard', 'Wizard', 'Sorceror', 'Warlock')


class PowerWordStun(Spell):
    """You speak a word of power that can overwhelm the mind of one
    creature you can see within range, leaving it dumbfounded. If the
    target has 150 hit points or fewer, it is stunned. Otherwise, the
    spell has no effect. The stunned target must make a Constitution
    saving throw at the end of each of its turns. On a successful
    save, this stunning effect ends.
    
    """
    name = "Power Word Stun"
    level = 8
    casting_time = "1 action"
    components = ('V',)
    materials = ""
    duration = "Instantaneous"
    magic_school = "Enchantment"
    classes = ()


class PrayerOfHealing(Spell):
    """Up to six creatures of your choice that you can see within range
    each regain hit points equal to 2d8 + your spellcasting ability
    modifier. This spell has no effect on undead or constructs. At
    Higher Levels. When you cast this spell using a spell slot of 3rd
    level or higher, the healing increases by 1d8 for each slot level
    above 2nd.
    
    """
    name = "PrayerOfHealing"
    level = 2
    casting_time = "10 minutes"
    components = ('V',)
    materials = ""
    duration = "Instantaneous"
    magic_school = "Evocation"
    classes = ()


class Prestidigitation(Spell):
    """This spell is a minor magical trick that novice spellcasters use
    for practice. You create one of the following magical effects
    within range.
    
    - You create an instantaneous, harmless sensory effect, such as a
      shower of sparks, a puff of wind, faint musical notes, or an odd
      odor.
    - You instantaneously light or snuff out a candle, a torch, or a
      small campfire.
    - You instantaneously clean or soil an object no larger than 1
      cubic foot.
    - You chill, warm, or flavor up to 1 cubic foot of nonliving
      material for 1 hour.
    - You make a color, a small mark, or a symbol appear on an object
      or a surface for 1 hour.
    - You create a nonmagical trinket or an illusory image that can
      fit in your hand and that lasts until the end of your next turn.
    
    If you cast this spell multiple times, you can have up to three of
    its non-instantaneous effects active at a time, and you can
    dismiss such an effect as an action.
    
    """
    name = "Prestidigitation"
    level = 0
    casting_time = "1 action"
    casting_range = "10 feet"
    components = ("V", "S", )
    duration = "1 hour"
    magic_school = "Transmutation"
    classes = ('Bard', 'Sorceror', 'Warlock', 'Wizard', )


class ProtectionFromEnergy(Spell):
    """For the duration, the willing creature you touch has resistance to
    one damage type of your choice: acid, cold, fire, lightning, or
    thunder.
    
    """
    name = "Protection from Energy"
    level = 3
    casting_time = "1 action"
    components = ('V', 'S')
    materials = ""
    duration = "Concentration, up to 1 hour"
    magic_school = "Abjuration"
    classes = ()


class RaiseDead(Spell):
    """You return a dead creature you touch to life, provided that it has
    been dead no longer than 10 days. If the creature’s soul is both
    willing and at liberty to rejoin the body, the creature returns to
    life with 1 hit point.
    
    This spell also neutralizes any poisons and
    cures nonmagical diseases that affected the creature at the time
    it died. This spell doesn’t, however, remove magical diseases,
    curses, or similar effects; if these aren’t first removed prior to
    casting the spell, they take effect when the creature returns to
    life. The spell can’t return an undead creature to life.
    
    This spell closes all mortal wounds, but it doesn’t restore
    missing body parts. If the creature is lacking body parts or
    organs integral for its survival—its head, for instance—the spell
    automatically fails.
    
    Coming back from the dead is an ordeal. The target takes a −4
    penalty to all attack rolls, saving throws, and ability
    checks. Every time the target finishes a long rest, the penalty is
    reduced by 1 until it disappears.
    
    """
    name = "Raise Dead"
    level = 5
    casting_time = "1 hour"
    casting_range = "Touch"
    components = ('V', 'S', 'M')
    materials = "a diamond worth at least 500 gp, which the spell consumes"
    duration = "Instantaneous"
    magic_school = "Necromancy"
    classes = ('Bard', 'Cleric', 'Paladin', )


class RayOfEnfeeblement(Spell):
    """A black beam of enervating energy springs from your finger toward a
    creature within range. Make a ranged spell attack against the
    target. On a hit, the target deals only half damage with weapon
    attacks that use Strength until the spell ends.
    
    At the end of each of the target's turns, it can make a
    Constitution saving throw against the spell. On a success, the
    spell ends.
    
    """
    name = "Ray of Enfeeblement"
    level = 2
    casting_time = "1 action"
    casting_range = "60 feet"
    components = ('V', 'S', )
    materials = ""
    duration = "Concentration (1 minute)"
    magic_school = "Necromancy"
    classes = ('Warlock', 'Wizard', )


class RayOfFrost(Spell):
    """A frigid beam of blue-white light streaks toward a creature within
    range. Make a ranged spell attack against the target. On a hit, it
    takes 1d8 cold damage, and its speed is reduced by 10 feet until
    the start of your next turn.
    
    The spell's damage increases by 1d8 when you reach 5th level
    (2d8), 11th level (3d8), and 17th level (4d8).
    
    """
    name = "Ray of Frost"
    level = 0
    casting_time = "1 action"
    casting_range = "60 feet"
    components = ("V", "S", )
    duration = "Instantaneous"
    magic_school = "Evocation"
    classes = ('Sorceror', 'Wizard', )


class RayOfSickness(Spell):
    """A ray of sickening greenish energy lashes out toward a creature
    within range. Make a ranged spell attack against the target. On a
    hit, the target takes 2d8 poison damage and must make a
    Constitution saving throw. On a failed save, it is also poisoned
    until the end of your next turn.
    
    At Higher Levels. When you cast this spell using a spell slot of
    2nd level or higher, the damage increases by 1d8 for each slot
    level above 1st.
    
    """
    name = "Ray of Sickness"
    level = 1
    casting_time = "1 action"
    casting_range = "60 feet"
    components = ("V", "S", )
    duration = "Instantaneous"
    magic_school = "Necromancy"
    classes = ('Sorceror', 'Wizard', )


class Regenerate(Spell):
    """You touch a creature and stimulate its natural healing ability. The
    target regains 4d8 + 15 hit points. For the duration of the spell,
    the target regains 1 hit point at the start of each of its turns
    (10 hit points each minute). The target’s severed body members
    (fingers, legs, tails, and so on), if any, are restored after 2
    minutes. If you have the severed part and hold it to the stump,
    the spell instantaneously causes the limb to knit to the stump.
    
    """
    name = "Regenerate"
    level = 7
    casting_time = "1 minute"
    components = ('V', 'S', 'M')
    materials = "a prayer wheel and holy water"
    duration = "1 hour"
    magic_school = "Transmutation"
    classes = ()


class RemoveCurse(Spell):
    """At your touch, all curses affecting one creature or object end. If
    the object is a cursed magic item, its curse remains, but the
    spell breaks its owner’s attunement to the object so it can be
    removed or discarded.
    
    """
    name = "Remove Curse"
    level = 3
    casting_time = "1 action"
    components = ('V', 'S')
    materials = ""
    duration = "Instantaneous"
    magic_school = "Abjuration"
    classes = ()


class Resistance(Spell):
    """You touch one willing creature. Once before the spell ends, the
    target can roll a d4 and add the number rolled to one saving throw
    of its choice. It can roll the die before or after making the
    saving throw. The spell then ends.
    
    """
    name = "Resistance"
    level = 0
    casting_time = "1 action"
    components = ('V', 'S', 'M')
    materials = "a miniature cloak"
    duration = "Concentration, up to 1 minute"
    magic_school = "Abjuration"
    classes = ()


class Resurrection(Spell):
    """You touch a dead creature that has been dead for no more than a
    century, that didn’t die of old age, and that isn’t undead. If its
    soul is free and willing, the target returns to life with all its
    hit points. This spell neutralizes any poisons and cures normal
    diseases afflicting the creature when it died. It doesn’t,
    however, remove magical diseases, curses, and the like; if such
    effects aren’t removed prior to casting the spell, they afflict
    the target on its return to life. This spell closes all mortal
    wounds and restores any missing body parts. Coming back from the
    dead is an ordeal. The target takes a −4 penalty to all attack
    rolls, saving throws, and ability checks. Every time the target
    finishes a long rest, the penalty is reduced by 1 until it
    disappears. Casting this spell to restore life to a creature that
    has been dead for one year or longer taxes you greatly. Until you
    finish a long rest, you can’t cast spells again, and you have
    disadvantage on all attack rolls, ability checks, and saving
    throws.
    
    """
    name = "Resurrection"
    level = 7
    casting_time = "1 hour"
    components = ('V', 'S', 'M')
    materials = "a diamond worth at least 1,000 gp, which the spell consumes"
    duration = "Instantaneous"
    magic_school = "Necromancy"
    classes = ()


class Revivify(Spell):
    """You touch a creature that has died within the last minute. That
    creature returns to life with 1 hit point. This spell can’t return
    to life a creature that has died of old age, nor can it restore
    any missing body parts.
    
    """
    name = "Revivify"
    level = 3
    casting_time = "1 action"
    components = ('V', 'S', 'M')
    materials = "diamonds worth 300 gp, which the spell consumes"
    duration = "Instantaneous"
    magic_school = "Conjuration"
    classes = ()

