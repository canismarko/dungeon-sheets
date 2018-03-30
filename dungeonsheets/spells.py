

class Spell():
    """A magical spell castable by a player character."""
    level = 0
    casting_time = "1 action"
    casting_range = "60 ft"
    components = ("V", "S")
    duration = "instantaneous"
    magic_school = ""
    classes = ()
    
    def __str__(self):
        return self.name
    
    def __repr__(self):
        return f'<{self.name}>'


class AcidSplash(Spell):
    """You hurl a bubble of acid. Choose one creature within range, or
    choose two crealures within range that are within 5 feet of each
    other. A target must succeed on a Dexterity saving throw or take
    1d6 acid damage.
    
    This spell's damage increases by 1d6 when you reach 5th level
    (2d6), 11th level (3d6), and 17th level (4d6).
    
    """
    name = "Acid Splash"
    classes = ('Sorceror', 'Wizard', )
    magic_school = "Conjuration"


class BlindnessDeafness(Spell):
    """Vou can blind or deafen a foe. Choose one creature that you can see
    within range to make a Constitution saving throw. If it fails, the
    target is either blinded or deafened (your choice) for the
    duration. At the end of each of its turns, the target can make a
    Constitution saving throw.  On a success, the spell ends.
    
    At Higher Levels. When you cast this spell using a spell slot of
    3rd level or higher, you can target one additional creature for
    each slot level above 2nd.
    
    """
    name = "Blindness/Deafness"
    magic_school = "Necromancy"
    level = 2
    casting_range = "30 feet"
    components = ("V", )
    duration = "1 minute"
    classes = ('Wizard', )


class BurningHands(Spell):
    """As you hold your hands with lhumbs touching and fingers spread, a
    thin sheet of flames shoots forth from your outstretched
    fingertips. Each creature in a 15-foot cone must make a Dexterity
    saving throw. A creature takes 3d6 fire damage on a failed save,
    or half as much damage on a successful one.
    
    The fire ignites any flammable objecls in lhe area that aren't
    being worn or carried.
    
    **At Higher Levels.** When you cast lhis spell using a spell slot
    of 2nd level or higher, lhe damage increases by 1d6 for each slot
    level above 1st.
    
    """
    name = "Burning Hands"
    level = 1
    casting_time = "1 action"
    casting_range = "Self (15 foot cone)"
    components = ("V", "S")
    duration = "Instantaneous"
    magic_school = "Evocation"
    classes = ('Wizard', )


class DetectMagic(Spell):
    """For the duration, you sense the presence of magic within 30 feet of
    you. If you sense magic in this way, you can use your action to
    see a faint aura around any visible creature or object in the area
    that bears magic, and you learn its school of magic, if any.
    
    The spell can penetrate most barriers, but is blocked by 1 foot of
    stone, 1 inch of common metal, a thin sheet of lead, or 3 feet of
    wood or dirt.
    
    """
    name = "Detect Magic"
    level = 1
    casting_time = "1 action"
    casting_range = "Self (30 feet)"
    components = ("V", "S")
    duration = "Concentration, Up to 10 minutes"
    magic_school = "Divination"
    classes = ('Bard', 'Cleric', 'Druid', 'Paladin', 'Ranger', 'Sorceror', 'Wizard', )


class FalseLife(Spell):
    """Bolstering yourself with a necromantic facsimile of life, you gain
    1d4+4 temporary hit points for the duration.
    
    At Higher Levels: When you cast this spell using a spell slot of
    2nd level or higher, you gain 5 additional temporary hit points
    for each slot level above 1st.
    
    """
    name = "False Life"
    level = 1
    casting_time = "1 action"
    casting_range = "Self (30 feet)"
    components = ("V", "S", "M")
    materials = "A small amount of alcohol or distilled spirits"
    duration = "1 hour"
    magic_school = "Necromancy"
    classes = ('Sorceror', 'Wizard', )


class MageArmor(Spell):
    """You touch a willing creature who isn't wearing armor, and a
    protective magical force surrounds it until the spell ends. The
    target's base AC becomes 13 + its Dexterity modifier. The spell
    ends it if the target dons armor or if you dismiss the spell as an
    action.
    
    """
    name = "Mage Armor"
    level = 1
    casting_time = "1 action"
    casting_range = "Touch"
    components = ("V", "S", "M")
    materials = "A piece of cured leather"
    duration = "8 hours"
    magic_school = "Abjuration"
    classes = ('Sorceror', 'Wizard', )


class MageHand(Spell):
    """A spectral, floating hand appears at a point you choose within
    range. The hand lasts for the duration or until you dismiss it as
    an action. The hand vanishes if it is ever more than 30 feet away
    from you or if you cast this spell again.
    
    You can use your action to control the hand. You can use the hand
    to manipulate an object, open an unlocked door or container, stow
    or retrieve an item from an open container, or pour the contents
    out of a vial. You can move the hand up to 30 feet each time you
    use it.
    
    The hand can't attack, activate magical items, or carry more than
    10 pounds.
    
    """
    name = "Mage Hand"
    level = 0
    casting_time = "1 action"
    casting_range = "30 feet"
    components = ("V", "S", )
    duration = "1 minute"
    magic_school = "Conjuration"
    classes = ('Bard', 'Sorceror', 'Warlock', 'Wizard', )


class MagicMissile(Spell):
    """You create three glowing darts of magical force. Each dart hits a
    creature of your choice that you can see within range. A dart
    deals 1d4+1 force damage to its target. The darts all strike
    simultaneously and you can direct them to hit one creature or
    several.
    
    At Higher Levels: When you cast this spell using a spell slot of
    2nd level or higher, the spell creates one more dart for each slot
    above 1st.
    
    """
    name = "Magic Missile"
    level = 1
    casting_time = "1 action"
    casting_range = "120 feet"
    components = ("V", "S", )
    duration = "Instantaneous"
    magic_school = "Evocation"
    classes = ('Sorceror', 'Wizard', )


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


class Shield(Spell):
    """An invisible barrier of magical force appears and protects
    you. Until the start of your next turn, you have a +5 bonus to AC,
    including against the triggering attack, and you take no damage
    from magic missile.
    
    """
    name = "Shield"
    level = 1
    casting_time = "1 reaction"
    casting_range = "Self"
    components = ("V", "S", )
    duration = "1 round"
    magic_school = "Abjuration"
    classes = ('Sorceror', 'Wizard', )


class ShockingGrasp(Spell):
    """Lightning springs from your hand to deliver a shock to a creature
    you try to touch. Make a melee spell attack against the
    target. You have advantage on the attack roll if the target is
    wearing armor made of metal. On a hit, the target takes 1d8
    lightning damage, and it can't take reactions until the start of
    its next turn.
    
    The spell's damage increases by 1d8 when you reach 5th level
    (2d8), 11th level (3d8), and 17th level (4d8).
    
    """
    name = "Shocking Grasp"
    level = 0
    casting_time = "1 action"
    casting_range = "Touch"
    components = ("V", "S", )
    duration = "Instantaneous"
    magic_school = "Evocation"
    classes = ('Sorceror', 'Wizard', )


class Sleep(Spell):
    """This spell sends creatures into a magical slumber. Roll 5d8, the
    total is how many hit points of creatures this spell can
    affect. Creatures within 20 feet of a point you choose within
    range are affected in ascending order of their current hit points
    (ignoring unconscious creatures).
    
    Starting with the creature that has the lowest current hit points,
    each creature affected by this spell falls unconscious until the
    spell ends, the sleeper takes damage, or someone uses an action to
    shake or slap the sleeper awake. Subtract each creature's hit
    points from the total before moving on to the creature with the
    next lowest hit points. A creature's hit points must be equal to
    or less than the remaining total for that creature to be affected.
    
    Undead and creatures immune to being charmed aren't affected by
    this spell.
    
    At Higher Levels: When you cast this spell using a spell slot of
    2nd level or higher, roll an additional 2d8 for each slot level
    above 1st.
    
    """
    name = "Sleep"
    level = 1
    casting_time = "1 action"
    casting_range = "90 feet"
    components = ("V", "S", "M", )
    materials = "A pinch of fine sand, rose petals, or a cricket"
    duration = "1 minutes"
    magic_school = "Enchantment"
    classes = ('Bard', 'Sorceror', 'Wizard', )
