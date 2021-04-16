from dungeonsheets.spells.spells import Spell


class LegendLore(Spell):
    """Name or describe a person, place, or object. The spell brings to your mind a
    brief summary of the significant lore about the thing you named. The lore might
    consist of current tales, forgotten stories, or even secret lore that has never
    been widely known. If the thing you named isn't of legendary importance, you
    gain no information. The more information you already have about the thing, the
    more precise and detailed the information you receive is.

    The information you
    learn is accurate but might be couched in figurative language. For example, if
    you have a mysterious magic axe on hand, the spell might yield this information:
    Woe to the evildoer whose hand touches the axe, for even the haft slices the
    hand of the evil ones. Only a true Child of Stone, lover and beloved of Moradin,
    may awaken the true powers of the axe, and only with the sacred word Rudnogg on
    the lips.
    """

    name = "Legend Lore"
    level = 5
    casting_time = "10 minutes"
    casting_range = "Self"
    components = ("V", "S", "M")
    materials = (
        "Incense worth at least 250 gp, which the spell consumes, and four ivory strips"
        " worth at least 50 gp each"
    )
    duration = "Instantaneous"
    ritual = False
    magic_school = "Divination"
    classes = ("Bard", "Cleric", "Wizard")


class LeomundsSecretChest(Spell):
    """You hide a chest, and all its contents, on the Ethereal Plane.
    You must touch
    the chest and the miniature replica that serves as a material component for the
    spell. The chest can contain up to 12 cubic feet of nonliving material (3 feet
    by 2 feet by 2 feet).

    While the chest remains on the Ethereal Plane, you can
    use an action and touch the replica to recall the chest. It appears in an
    unoccupied space on the ground within 5 feet of you. You can send the chest back
    to the Ethereal Plane by using an action and touching both the chest and the
    replica.

    After 60 days, there is a cumulative 5 percent chance per day that the
    spell's effect ends. This effect ends if you cast this spell again, if the
    smaller replica chest is destroyed, or if you choose to end the spell as an
    action. If the spell ends and the larger chest is on the Ethereal Plane, it is
    irretrievably lost.
    """

    name = "Leomunds Secret Chest"
    level = 4
    casting_time = "1 action"
    casting_range = "Touch"
    components = ("V", "S", "M")
    materials = (
        "An exquisite chest, 3 feet by 2 feet by 2 feet, constructed from rare"
        " materials worth at least 5,000 gp, and a tiny replica made from the same"
        " materials worth at least 50 gp"
    )
    duration = "Instantaneous"
    ritual = False
    magic_school = "Conjuration"
    classes = ("Wizard",)


class LeomundsTinyHut(Spell):
    """A 10-foot-radius immobile dome of force springs into existence around and above
    you and remains stationary for the duration. The spell ends if you leave its
    area.

    Nine creatures of Medium size or smaller can fit inside the dome with
    you. The spell fails if its area includes a larger creature or more than nine
    creatures. Creatures and objects within the dome when you cast this spell can
    move through it freely. All other creatures and objects are barred from passing
    through it. Spells and other magical effects can't extend through the dome or be
    cast through it. The atmosphere inside the space is comfortable and dry,
    regardless of the weather outside.

    Until the spell ends, you can command the
    interior to become dimly lit or dark. The dome is opaque from the outside, of
    any color you choose, but it is transparent from the inside.
    """

    name = "Leomunds Tiny Hut"
    level = 3
    casting_time = "1 minute"
    casting_range = "Self (10-foot-radius hemisphere)"
    components = ("V", "S", "M")
    materials = "A small crystal bead"
    duration = "8 hours"
    ritual = True
    magic_school = "Evocation"
    classes = ("Bard", "Wizard")


class LesserRestoration(Spell):
    """You touch a creature and can end either one disease or one condition afflicting
    it. The condition can be blinded, deafened, paralyzed, or poisoned.
    """

    name = "Lesser Restoration"
    level = 2
    casting_time = "1 action"
    casting_range = "Touch"
    components = ("V", "S")
    materials = ""
    duration = "Instantaneous"
    ritual = False
    magic_school = "Abjuration"
    classes = ("Bard", "Cleric", "Druid", "Paladin", "Ranger")


class Levitate(Spell):
    """One creature or object of your choice that you can see within range rises
    vertically, up to 20 feet, and remains suspended there for the duration. The
    spell can levitate a target that weighs up to 500 pounds. An unwilling creature
    that succeeds on a Constitution saving throw is unaffected.

    The target can move
    only by pushing or pulling against a fixed object or surface within reach (such
    as a wall or a ceiling), which allows it to move as if it were climbing. You
    can change the target's altitude by up to 20 feet in either direction on your
    turn. If you are the target, you can move up or down as part of your move.
    Otherwise, you can use your action to move the target, which must remain within
    the spell's range.

    When the spell ends, the target floats gently to the ground
    if it is still aloft.
    """

    name = "Levitate"
    level = 2
    casting_time = "1 action"
    casting_range = "60 feet"
    components = ("V", "S", "M")
    materials = (
        "Either a small leather loop or a piece of golden wire bent into a cup shape"
        " with a long shank on one end"
    )
    duration = "Concentration, up to 10 minutes"
    ritual = False
    magic_school = "Transmutation"
    classes = ("Sorcerer", "Wizard")


class LifeTransference(Spell):
    """You sacrifice some of your health to mend another creature's injuries. You take
    4d8 necrotic damage, and one creature of your choice that you can see within
    range regains a number of hit points equal to twice the necrotic damage you
    take.

    **At Higher Levels:** When you cast this spell using a spell slot of 4th
    level or higher, the damage increases by 1d8 for each slot level above 3rd.
    """

    name = "Life Transference"
    level = 3
    casting_time = "1 action"
    casting_range = "30 feet"
    components = ("V", "S")
    materials = ""
    duration = "Instantaneous"
    ritual = False
    magic_school = "Necromancy"
    classes = ("Cleric", "Wizard")


class Light(Spell):
    """You touch one object that is no larger than 10 feet in any dimension. Until the
    spell ends, the object sheds bright light in a 20-foot radius and dim light for
    an additional 20 feet. The light can be colored as you like. Completely covering
    the object with something opaque blocks the light. The spell ends if you cast
    it again or dismiss it as an action.

    If you target an object held or worn by a
    hostile creature, that creature must succeed on a Dexterity saving throw to
    avoid the spell.
    """

    name = "Light"
    level = 0
    casting_time = "1 action"
    casting_range = "Touch"
    components = ("V", "M")
    materials = "A firefly or phosphorescent moss"
    duration = "1 hour"
    ritual = False
    magic_school = "Evocation"
    classes = ("Bard", "Cleric", "Sorcerer", "Wizard")


class LightningArrow(Spell):
    """The next time you make a ranged weapon attack during the spell's duration, the
    weapon's ammunition, or the weapon itself if it's a thrown weapon, transforms
    into a bolt of lightning. Make the attack roll as normal, The target takes 4d8
    lightning damage on a hit, or half as much damage on a miss, instead of the
    weapon's normal damage.

    Whether you hit or miss, each creature within 10 feet
    of the target must make a Dexterity saving throw. Each of these creatures takes
    2d8 lightning damage on a failed save, or half as much damage on a successful
    one.

    The piece of ammunition or weapon then returns to its normal form.

    At
    Higher Levels: When you cast this spell using a spell slot of 4th level or
    higher, the damage for both effects of the spell increases by 1d8 for each slot
    level above 3rd.
    """

    name = "Lightning Arrow"
    level = 3
    casting_time = "1 bonus action"
    casting_range = "Self"
    components = ("V", "S")
    materials = ""
    duration = "Concentration, up to 1 minute"
    ritual = False
    magic_school = "Transmutation"
    classes = ("Ranger",)


class LightningBolt(Spell):
    """A stroke of lightning forming a line of 100 feet long and 5 feet wide blasts out
    from you in a direction you choose. Each creature in the line must make a
    Dexterity saving throw. A creature takes 8d6 lightning damage on a failed save,
    or half as much damage on a successful one.

    The lightning ignites flammable
    objects in the area that aren't being worn or carried.

    **At Higher Levels:** When
    you cast this spell using a spell slot of 4th level or higher, the damage
    increases by 1d6 for each slot level above 3rd.
    """

    name = "Lightning Bolt"
    level = 3
    casting_time = "1 action"
    casting_range = "Self (100-foot line)"
    components = ("V", "S", "M")
    materials = "A bit of fur and a rod of amber, crystal, or glass"
    duration = "Instantaneous"
    ritual = False
    magic_school = "Evocation"
    classes = ("Sorcerer", "Wizard")


class LightningLure(Spell):
    """You create a lash of lightning energy that strikes at one creature of your
    choice that you can see within range.
    The target must succeed on a Strength
    saving throw or be pulled up to 10 feet in a straight line toward you and then
    take 1d8 lightning damage if it is within 5 feet of you.

    **At Higher Levels:** This
    spell's damage increases by 1d8 when you reach 5th level (2d8), 11th level
    (3d8), and 17th level (4d8).
    """

    name = "Lightning Lure"
    level = 0
    casting_time = "1 action"
    casting_range = "15 feet"
    components = ("V",)
    materials = ""
    duration = "Instantaneous"
    ritual = False
    magic_school = "Evocation"
    classes = ("Sorcerer", "Warlock", "Wizard")


class LocateAnimalsOrPlants(Spell):
    """Describe or name a specific kind of beast or plant. Concentrating on the voice
    of nature in your surroundings, you learn the direction and distance to the
    closest creature or plant of that kind within 5 miles, if any are present.
    """

    name = "Locate Animals Or Plants"
    level = 2
    casting_time = "1 action"
    casting_range = "Self"
    components = ("V", "S", "M")
    materials = "A bit of fur from a bloodhound"
    duration = "Instantaneous"
    ritual = True
    magic_school = "Divination"
    classes = ("Bard", "Druid", "Ranger")


class LocateCreature(Spell):
    """Describe or name a creature that is familiar to you. You sense the direction to
    the creature's location, as long as that creature is within 1,000 feet of you.
    If the creature is moving, you know the direction of its movement.

    The spell
    can locate a specific creature known to you, or the nearest creature of a
    specific kind (such as a human or a unicorn), so long as you have seen such a
    creature up close – within 30 feet – at least once. If the creature you
    described or named is in a different form, such as being under the effects of a
    polymorph spell, this spell doesn't locate the creature.

    This spell can't
    locate a creature if running water at least 10 feet wide blocks a direct path
    between you and the creature.
    """

    name = "Locate Creature"
    level = 4
    casting_time = "1 action"
    casting_range = "Self"
    components = ("V", "S", "M")
    materials = "A bit of fur from a bloodhound"
    duration = "Concentration, up to 1 hour"
    ritual = False
    magic_school = "Divination"
    classes = ("Bard", "Cleric", "Druid", "Paladin", "Ranger", "Wizard")


class LocateObject(Spell):
    """Describe or name an object that is familiar to you. You sense the direction to
    the object's location, as long as that object is within 1,000 feet of you. If
    the object is in motion, you know the direction of its movement.

    The spell can
    locate a specific object known to you, as long as you have seen it up close –
    within 30 feet – at least once. Alternatively, the spell can locate the nearest
    object of a particular kind, such as a certain kind of apparel, jewelry,
    furniture, tool, or weapon.

    This spell can't locate an object if any thickness
    of lead, even a thin sheet, blocks a direct path between you and the object.
    """

    name = "Locate Object"
    level = 2
    casting_time = "1 action"
    casting_range = "Self"
    components = ("V", "S", "M")
    materials = "A forked twig"
    duration = "Concentration, up to 10 minutes"
    ritual = False
    magic_school = "Divination"
    classes = ("Bard", "Cleric", "Druid", "Paladin", "Ranger", "Wizard")


class Longstrider(Spell):
    """You touch a creature. The target's speed increases by 10 feet until the spell
    ends.

    **At Higher Levels:** When you cast this spell using a spell slot of 2nd
    level or higher, you can target one additional creature for each slot level
    above 1st.
    """

    name = "Longstrider"
    level = 1
    casting_time = "1 action"
    casting_range = "Touch"
    components = ("V", "S", "M")
    materials = "A pinch of dirt"
    duration = "1 hour"
    ritual = False
    magic_school = "Transmutation"
    classes = ("Bard", "Druid", "Ranger", "Wizard")
