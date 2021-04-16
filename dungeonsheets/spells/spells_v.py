from dungeonsheets.spells.spells import Spell


class VampiricTouch(Spell):
    """The touch of your shadow-wreathed hand can siphon force from others to heal your
    wounds. Make a melee spell attack against a creature within your reach. On a
    hit, the target takes 3d6 necrotic damage, and you regain hit points equal to
    half the amount of necrotic damage dealt. Until the spell ends, you can make the
    attack again on each of your turns as an action.

    **At Higher Levels:** When you
    cast this spell using a spell slot of 4th level or higher, the damage increases
    by 1d6 for each slot level above 3rd.
    """

    name = "Vampiric Touch"
    level = 3
    casting_time = "1 action"
    casting_range = "Self"
    components = ("V", "S")
    materials = ""
    duration = "Concentration, up to 1 minute"
    ritual = False
    magic_school = "Necromancy"
    classes = ("Warlock", "Wizard")


class ViciousMockery(Spell):
    """You unleash a string of insults laced with subtle enchantments at a creature you
    can see within range.
    If the target can hear you (thought it need not
    understand you), it must succeed on a Wisdom saving throw or take 1d4 psychic
    damage and have disadvantage on the next attack roll it makes before the end of
    its next turn.

    **At Higher Levels:** This spell's damage increases by 1d4 when you
    reach 5th level (2d4), 11th level (3d4), and 17th level (4d4).
    """

    name = "Vicious Mockery"
    level = 0
    casting_time = "1 action"
    casting_range = "60 feet"
    components = ("V",)
    materials = ""
    duration = "Instantaneous"
    ritual = False
    magic_school = "Enchantment"
    classes = ("Bard",)


class VitriolicSphere(Spell):
    """You point at a location within range, and a glowing, 1-foot-diameter ball of
    emerald acid streaks there and explodes in a 20-foot-radius sphere. Each
    creature in that area must make a Dexterity saving throw. On a failed save, a
    creature takes 10d4 acid damage and another 5d4 acid damage at the end of its
    next turn. On a successful save, a creature takes half the initial damage and no
    damage at the end of its next turn.

    **At Higher Levels:** When you cast this spell
    using a spell slot of 5th level or higher, the initial damage increases by 2d4
    for each slot level above 4th.
    """

    name = "Vitriolic Sphere"
    level = 4
    casting_time = "1 action"
    casting_range = "150 feet"
    components = ("V", "S", "M")
    materials = "A drop of giant slug bile"
    duration = "Instantaneous"
    ritual = False
    magic_school = "Evocation"
    classes = ("Sorcerer", "Wizard")
