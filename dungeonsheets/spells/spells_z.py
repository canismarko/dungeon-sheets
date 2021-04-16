from dungeonsheets.spells.spells import Spell


class ZephyrStrike(Spell):
    """You move like the wind. Until the spell ends, your movement doesn't provoke
    opportunity attacks.
    Once before the spell ends, you can give yourself advantage
    on one weapon attack roll on your turn. That attack deals an extra 1d8 force
    damage on a hit. Whether you hit or miss, your walking speed increases by 30
    feet until the end of that turn.
    """

    name = "Zephyr Strike"
    level = 1
    casting_time = "1 bonus action"
    casting_range = "Self"
    components = ("V",)
    materials = ""
    duration = "Concentration, up to 1 minute"
    ritual = False
    magic_school = "Transmutation"
    classes = ("Ranger",)


class ZoneOfTruth(Spell):
    """You create a magical zone that guards against deception in a 15-foot-radius
    sphere centered on a point of your choice within range.
    Until the spell ends, a
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
    components = ("V", "S")
    materials = ""
    duration = "10 minutes"
    ritual = False
    magic_school = "Enchantment"
    classes = ("Bard", "Cleric", "Paladin")
