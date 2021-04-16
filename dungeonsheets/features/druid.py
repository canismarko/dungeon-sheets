from dungeonsheets import spells
from dungeonsheets.features.features import Feature, FeatureSelector


# PHB
class WildShape(Feature):
    """Starting at 2nd level, you can use your action to magically assume
    the shape of a beast that you have seen before. You can use this
    feature twice. You regain expended uses when you finish a short or
    long rest. Your druid level determines the beasts you can
    transform into, as shown in the Beast Shapes table. At 2nd level,
    for example, you can transform into any beast that has a challenge
    rating of 1/4 or lower that doesn't have a flying or swimming
    speed.

    ===== ====== ================== ===========
    Level Max CR Limitations        Example
    ===== ====== ================== ===========
    2nd   1/4    No Flying/Swimming Wolf
    4th   1/2    No flying          Crocodile
    8th   1      --                 Giant eagle
    ===== ====== ================== ===========

    You can stay in a beast shape for a number of hours equal to half
    your druid level (rounded down). You then revert to your normal
    form unless you expend another use of this feature. You can revert
    to your normal form earlier by using a bonus action on your
    turn. You automatically revert if you fall unconscious, drop to 0
    hit points, or die.

    While you are transformed, the following rules apply:

    - Your game statistics are replaced by the statistics of the
      beast, but you retain your alignment, personality, and
      Intelligence, Wisdom, and Charisma scores. You also retain all
      of your skill and saving throw proficiencies, in addition to
      gaining those of the creature. If the creature has the same
      proficiency as you and the bonus in its stat block is higher
      than yours, use the creature's bonus instead of yours. If the
      creature has any legendary or lair actions, you can't use them.
    - When you transform, you assume the beast's hit points and Hit
      Dice. When you revert to your normal form, you return to the
      number of hit points you had before you transformed. However, if
      you revert as a result of dropping to 0 hit points, any excess
      damage carries over to your normal form. For example, if you
      take 10 damage in animal form and have only 1 hit point left,
      you revert and take 9 damage. As long as the excess damage
      doesn't reduce your normal form to 0 hit points, you aren't
      knocked unconscious.
    - You can't cast spells, and your ability to speak or take any
      action that requires hands is limited to the capabilities of
      your beast form. Transforming doesn't break your concentration
      on a spell you've already cast, however, or prevent you from
      taking actions that are part of a spell, such as call lightning,
      that you've already cast.
    - You retain the benefit of any features from your class, race, or
      other source and can use them if the new form is physically
      capable of doing so. However, you can't use any of your special
      senses, such as darkvision, unless your new form also has that
      sense.
    - You choose whether your equipment falls to the ground in your
      space, merges into your new form, or is worn by it. Worn
      equipment functions as normal, but the DM decides whether it is
      practical for the new form to wear a piece of equipment, based
      on the creature's shape and size. Your equipment doesn't change
      size or shape to match the new form, and any equipment that the
      new form can't wear must either fall to the ground or merge with
      it. Equipment that merges with the form has no effect until you
      leave the form.

    """

    _name = "Wild Shape"
    source = "Druid"

    @property
    def name(self):
        num = 2
        time = self.owner.Druid.level // 2
        return self._name + " ({:d}x/SR, {:d} hours)".format(num, time)


class TimelessBody(Feature):
    """Starting at 18th level, the primal magic that you wield causes you to age
    more slowly. For every 10 years that pass, your body ages only 1 year.

    """

    name = "Timeless Body"
    source = "Druid"


class BeastSpells(Feature):
    """Beginning at 18th level, you can cast many of your druid spells in any
    shape you assume using Wild Shape. You can perform the somatic and verbal
    components of a druid spell while in a beast shape, but you aren't able to
    provide material components.

    """

    name = "Beast Spells"
    source = "Druid"


class Archdruid(Feature):
    """At 20th level, you can use your Wild Shape an unlimited number of times.

    Additionally, you can ignore the verbal and somatic components of your
    druid spells, as well as any material components that lack a cost and
    aren't consumed by a spell. You gain this benefit in both your normal shape
    and your beast shape from Wild Shape

    """

    name = "Archdruid"
    source = "Druid"


# Circle of the Land
class BonusCantrip(Feature):
    """When you choose this circle at 2nd level, you learn one additional druid
    cantrip of your choice

    """

    name = "Bonus Cantrip"
    source = "Druid (Circle of the Land)"


class NaturalRecovery(Feature):
    """Starting at 2nd level, you can regain some of your magical energy by
    sitting in meditation and communing with nature. During a short rest, you
    choose expended spell slots to recover. The spell slots can have a combined
    level that is equal to or less than half your druid level (rounded up), and
    none of the slots can be 6th level or higher. You can't use this feature
    again until you finish a long rest.

    For example, when you are a 4th-level druid, you can recover up to two
    levels worth of spell slots. You can recover either a 2nd-level slot or two
    1st-level slots.

    """

    name = "Natural Recovery"
    source = "Druid (Circle of the Land)"


class _CircleSpells(Feature):
    """Your mystical connection to the land infuses you with the ability to cast
    certain spells. At 3rd, 5th, 7th, and 9th level you gain access to circle
    spells connected to the land where you became a druid. Choose that
    land-arctic, coast, desert, forest, grassland, mountain, swamp, or
    Underdark-and consult the associated list of spells.

    Once you gain access to a circle spell, you always have it prepared, and it
    doesn't count against the number of spells you can prepare each day. If you
    gain access to a spell that doesn't appear on the druid spell list, the
    spell is nonetheless a druid spell for you.

    """

    _name = "Select One"
    source = "Druid (Circle of the Land)"
    _spells = {
        3: [spells.MirrorImage, spells.MistyStep],
        5: [spells.WaterBreathing, spells.WaterWalk],
        7: [spells.ControlWater, spells.FreedomOfMovement],
        9: [spells.ConjureElemental, spells.Scrying],
    }
    spells_known = []
    spells_prepared = []

    @property
    def name(self):
        return "Circle Spells ({:s})".format(self._name)

    def __init__(self, owner=None):
        if owner is not None:
            level = owner.Druid.level
            for lvl, sps in self._spells.items():
                if level >= lvl:
                    self.spells_known.extend(sps)
                    self.spells_prepared.extend(sps)
        super().__init__(owner=owner)


class ArcticSpells(_CircleSpells):
    """Your mystical connection to the land infuses you with the ability to cast
    certain spells.

    These spells are included in your Spell Sheet

    """

    _name = "Arctic"
    _spells = {
        3: [spells.HoldPerson, spells.SpikeGrowth],
        5: [spells.SleetStorm, spells.Slow],
        7: [spells.FreedomOfMovement, spells.IceStorm],
        9: [spells.CommuneWithNature, spells.ConeOfCold],
    }


class CoastSpells(_CircleSpells):
    """Your mystical connection to the land infuses you with the ability to cast
    certain spells.

    These spells are included in your Spell Sheet

    """

    _name = "Coast"
    _spells = {
        3: [spells.MirrorImage, spells.MistyStep],
        5: [spells.WaterBreathing, spells.WaterWalk],
        7: [spells.ControlWater, spells.FreedomOfMovement],
        9: [spells.ConjureElemental, spells.Scrying],
    }


class DesertSpells(_CircleSpells):
    """Your mystical connection to the land infuses you with the ability to cast
    certain spells.

    These spells are included in your Spell Sheet

    """

    _name = "Desert"
    _spells = {
        3: [spells.Blur, spells.Silence],
        5: [spells.CreateFoodAndWater, spells.ProtectionFromEnergy],
        7: [spells.Blight, spells.HallucinatoryTerrain],
        9: [spells.InsectPlague, spells.WallOfStone],
    }


class ForestSpells(_CircleSpells):
    """Your mystical connection to the land infuses you with the ability to cast
    certain spells.

    These spells are included in your Spell Sheet

    """

    _name = "Forest"
    _spells = {
        3: [spells.Barkskin, spells.SpiderClimb],
        5: [spells.CallLightning, spells.PlantGrowth],
        7: [spells.Divination, spells.FreedomOfMovement],
        9: [spells.CommuneWithNature, spells.TreeStride],
    }


class GrasslandSpells(_CircleSpells):
    """Your mystical connection to the land infuses you with the ability to cast
    certain spells.

    These spells are included in your Spell Sheet

    """

    _name = "Grassland"
    _spells = {
        3: [spells.Invisibility, spells.PassWithoutTrace],
        5: [spells.Daylight, spells.Haste],
        7: [spells.Divination, spells.FreedomOfMovement],
        9: [spells.Dream, spells.InsectPlague],
    }


class MountainSpells(_CircleSpells):
    """Your mystical connection to the land infuses you with the ability to cast
    certain spells.

    These spells are included in your Spell Sheet

    """

    _name = "Mountain"
    _spells = {
        3: [spells.SpiderClimb, spells.SpikeGrowth],
        5: [spells.LightningBolt, spells.MeldIntoStone],
        7: [spells.StoneShape, spells.Stoneskin],
        9: [spells.Passwall, spells.WallOfStone],
    }


class SwampSpells(_CircleSpells):
    """Your mystical connection to the land infuses you with the ability to cast
    certain spells.

    These spells are included in your Spell Sheet

    """

    _name = "Swamp"
    _spells = {
        3: [spells.Darkness, spells.MelfsAcidArrow],
        5: [spells.WaterWalk, spells.StinkingCloud],
        7: [spells.FreedomOfMovement, spells.LocateCreature],
        9: [spells.InsectPlague, spells.Scrying],
    }


class UnderdarkSpells(_CircleSpells):
    """Your mystical connection to the land infuses you with the ability to cast
    certain spells.

    These spells are included in your Spell Sheet

    """

    _name = "Underdark"
    _spells = {
        3: [spells.SpiderClimb, spells.Web],
        5: [spells.GaseousForm, spells.StinkingCloud],
        7: [spells.GreaterInvisibility, spells.StoneShape],
        9: [spells.Cloudkill, spells.InsectPlague],
    }


class SporesSpells(_CircleSpells):
    """Your symbiotic link do fungus and your ability to tap into the cycle of
    life and death grants you access to certain spells.

    These spells are included in your Spell Sheet.

    """

    _name = "Spores"
    _spells = {
        2: [spells.ChillTouch],
        3: [spells.BlindnessDeafness, spells.GentleRepose],
        5: [spells.AnimateDead, spells.GaseousForm],
        7: [spells.Blight, spells.Confusion],
        9: [spells.Cloudkill, spells.Contagion],
    }


class CircleSpells(FeatureSelector, _CircleSpells):
    """
    Select a land where you became a druid in feature_choices in your .py file:

    arctic

    coast

    desert

    forest

    grassland

    mountain

    swamp

    underdark

    spores

    """

    options = {
        "arctic": ArcticSpells,
        "coast": CoastSpells,
        "desert": DesertSpells,
        "forest": ForestSpells,
        "grassland": GrasslandSpells,
        "mountain": MountainSpells,
        "swamp": SwampSpells,
        "underdark": UnderdarkSpells,
        "spores": SporesSpells,
    }
    name = "Circle Spells (Select One)"
    source = "Druid (Circle of the Land/Spores)"


class LandsStride(Feature):
    """Starting at 6th level, moving through nonmagical difficult terrain costs
    you no extra movement. You can also pass through nonmagical plants without
    being slowed by them and without taking damage from them if they have
    thorns, spines, or a similar hazard. In addition, you have advantage on
    saving throws against plants that are magically created or manipulated to
    impede movement, such those created by the entangle spell.

    """

    name = "Land's Stride"
    source = "Class (Many)"


class NaturesWard(Feature):
    """When you reach 10th level, you can't be charmed or frightened by elementals
    or fey, and you are immune to poison and disease

    """

    name = "Nature's Ward"
    source = "Druid (Circle of the Land)"


class NaturesSanctuary(Feature):
    """When you reach 14th level, creatures of the natural world sense your
    connection to nature and become hesitant to attack you. When a beast or
    plant creature attacks you, that creature must make a Wisdom saving throw
    against your druid spell save DC. On a failed save, the creature must
    choose a different target, or the attack automatically misses. On a
    successful save, the creature is immune to this effect for 24 hours. The
    creature is aware of this effect before it makes its attack against you

    """

    name = "Nature's Sanctuary"
    source = "Druid (Circle of the Land)"


# Circle of the Moon
class CombatWildShape(Feature):
    """When you choose this circle at 2nd level, you gain the ability to use Wild
    Shape on your turn as a bonus action, rather than as an
    action. Additionally, while you are transformed by Wild Shape, you can use
    a bonus action to expend one spell slot to regain 1d8 hit points per level
    of the spell slot expended.

    """

    name = "Combat Wild Shape"
    source = "Druid (Circle of the Moon)"


class CircleForms(Feature):
    """The rites of your circle grant you the ability to transform into more
    dangerous animal forms. Starting at 2nd level, you can use your Wild Shape
    to transform into a beast with a challenge rating as high as 1 (you ignore
    the Max. CR column of the Beast Shapes table, but must abide by the other
    limitations there). Starting at 6th level, you can transform into a beast
    with a challenge rating as high as your druid level divided by 3, rounded
    down

    """

    _name = "Circle Forms"
    source = "Druid (Circle of the Moon)"

    @property
    def name(self):
        level = self.owner.Druid.level
        return self._name + " (CR {:d})".format(max(1, level // 3))


class PrimalStrike(Feature):
    """Starting at 6th level, your attacks in beast form count as magical for the
    purpose of overcoming resistance and immunity to nonmagical attacks and
    damage.

    """

    name = "Primal Strike"
    source = "Druid (Circle of the Moon)"


class ElementalWildShape(Feature):
    """At 10th level, you can expend two uses of Wild Shape at the same time to
    transform into an air elemental, an earth elemental, a fire elemental, or a
    water elemental.

    """

    name = "Elemental Wild Shape"
    source = "Druid (Circle of the Moon)"


class ThousandForms(Feature):
    """By 14th level, you have learned to use magic to alter your physical form in
    more subtle ways. You can cast the alter self spell at will.

    """

    name = "Thousand Forms"
    source = "Druid (Circle of the Moon)"
    spells_known = (spells.AlterSelf,)
    spells_prepared = (spells.AlterSelf,)


# Circle of Dreams
class BalmOfTheSummerCourt(Feature):
    """At 2nd level, you become imbued with the blessings of the Summer Court. You
    are a font of energy that offers respite from injuries. You have a pool of
    fey energy represented by a number of C168 equal to your druid level. As
    a bonus action, you can choose one creature you can see within 120 feet
    ofyou and spend a number of those dice equal to halfyour druid level or
    less. Roll the spent dice and add them together. The target regains a
    number of hit points equal to the total. The target also gains 1 temporary
    hit point per die spent. You regain all expended dice when you finish a
    long rest.

    """

    _name = "Balm Of The Summer Court"
    source = "Druid (Circle of Dreams)"

    @property
    def name(self):
        return self._name + " ({:d}x d6)".format(self.owner.Druid.level)


class HearthOfMoonlightAndShadow(Feature):
    """At 6th level, home can be wherever you are. During a short or long rest,
    you can invoke the shadowy power of the Gleaming Court to help guard your
    respite. At the start of the rest, you touch a point in space, and an
    invisible, 30-foot-radius sphere of magic appears, centered on that
    point. Total cover blocks the sphere.

    While within the sphere, you and your allies gain a +5 bonus to Dexterity
    (Stealth) and Wisdom (Perception) checks, and any light from open flames in
    the sphere (a campfire, torches, or the like) isn't visible outside it. The
    sphere vanishes at the end of the rest or when you leave the sphere

    """

    name = "Hearth of Moonlight and Shadow"
    source = "Druid (Circle of the Moon)"


class HiddenPaths(Feature):
    """Starting at 10th level, you can use the hidden, magical pathways that some
    fey use to traverse space in the blink of an eye. As a bonus action on your
    turn, you can teleport up to 60 feet to an unoccupied space you can
    see.

    Alternatively, you can use your action to teleport one willing creature you
    touch up to 30 feet to an unoccupied space you can see. You can use this
    feature a number of times equal to your Wisdom modifier (minimum of once),
    and you regain all expended uses of it when you finish a long rest

    """

    name = "Hidden Paths"
    source = "Druid (Circle of the Moon)"


class WalkerInDreams(Feature):
    """At 14th level, the magic of the Feywild grants you the ability to travel
    mentally or physically through dreamlands. When you finish a short rest,
    you can cast one of the following spells, without expending a spell slot or
    requiring material components: dream (with you as the messenger),
    scrying, or teleportation circle.

    This use of teleportation circle is special. Rather than opening a portal
    to a permanent teleportation circle, it opens a portal to the last location
    where you finished a long rest on your current plane of existence. If you
    haven*t taken a long rest on your current plane, the spell fails but isn't
    wasted. Once you use this feature, you can't use it again until you finish
    a long rest.

    """

    name = "Walker in Dreams"
    source = "Druid (Circle of the Moon)"


# Circle of the Shepherd
class SpeechOfTheWoods(Feature):
    """At 2nd level, you gain the ability to converse with beasts and many fey. You
    learn to speak, read, and write Sylvan. In addition, beasts can
    understand your speech, and you gain the ability to decipher their noises
    and motions. Most beasts lack the intelligence to convey or understand
    sophisticated concepts, but a friendly beast could relay what it has seen
    or heard in the recent past. This ability doesn't grant you friendship with
    beasts, though you can combine this ability with gifts to curry favor with
    them as you would with any nonplayer character.

    """

    name = "Speech of the Woods"
    source = "Druid (Circle of the Shepherd)"


class SpiritTotem(Feature):
    """Starting at 2nd level, you can call forth nature spirits to
    influence the world around you. As a bonus action, you can
    magically summon an incorporeal spirit to a point you can see
    within 60 feet of you. The spirit creates an aura in a 30-foot
    radius around that point. It counts as neither a creature nor an
    object, though it has the spectral appearance of the creature
    it. represents.

    As a bonus action, you can move the spirit up to 60 feet to a
    point you can see. The spirit persists for 1 minute or until
    you're incapacitated. Once you use this feature, you can't use it
    again until you finish a short or long rest. The effect of the
    spirit's aura depends on the type of spirit you summon from the
    options below.

    **Bear Spirit**: The bear spirit grants you and your allies its
    might and endurance. Each creature ofyour choice in the aura when
    the spirit appears gains temporary hit points equal to 5 + your
    druid level. In addition, you and your allies gain advantage on
    Strength checks and Strength saving throws while in the aura.

    **Hawk Spirit**: The hawk spirit is a consummate hunter, aiding
    you and your allies with its keen sight. When a creature makes an
    attack roll against a target in the spirit's aura, you can use
    your reaction to grant advantage to that attack roll. In addition,
    you and your allies have advantage on Wisdom (Perception) checks
    while in the aura

    **Unicorn Spirit**: The unicorn spirit lends its protection to
    those nearby. You and your allies gain advantage on all ability
    checks made to detect creatures in the spirit's aura. In
    addition. if you cast a spell using a spell slot that restores hit
    points to any creature inside or outside the aura, each creature
    of your choice in the aura also regains hit points equal to your
    druid level.

    """

    name = "Spirit Totem"
    source = "Druid (Circle of the Shepherd)"


class MightySummoner(Feature):
    """Starting at 6th level, beasts and fey that you conjure are more
    resilient than normal. Any beast or fey summoned or created by a
    spell that you cast gains the. following benefits:

    - The creature appears with more hit points than normal: 2 extra
      hit
    - The creature appears with more hit points than normal: 2 extra
      hit points per Hit Die it has.
    - The damage from its natural weapons is considered magical for
      the purpose of overcoming immunity and resistance to nonmagical
      attacks and damage.

    """

    name = "Mighty Summoner"
    source = "Druid (Circle of the Shepherd)"


class GuardianSpirit(Feature):
    """Beginning at 10th level, your Spirit Totem safeguards the beasts
    and fey that you call forth with your magic. When a beast or fey
    that you summoned or created with a spell ends its turn in your
    Spirit Totem aura, that creature regains a number of hit points
    equal to half your druid level.

    """

    name = "Guardian Spirit"
    source = "Druid (Circle of the Shepherd)"


class FaithfulSummons(Feature):
    """Starting at 14th level, the nature spirits you commune with protect
    you when you are the most defenseless. Ifyou are reduced to 0 hit
    points or are incapacitated against your will, you can immediately
    gain the benefits of conjure animals as if it were cast using a
    9th-level spell slot. It summons four beasts of your choice that
    are challenge rating 2 or lower. The conjured beasts appear within
    20 feet of you. If they receive no commands from you, they protect
    you from harm and attack your foes. The spell lasts for 1 hour,
    requiring no concentration, or until you dismiss it (no action
    required). Once you use this feature, you can't use it again until
    you finish a long rest

    """

    name = "Faithful Summons"
    source = "Druid (Circle of the Shepherd)"


# Circle of Spores
class HaloOfSpores(Feature):
    """Starting at 2nd level, you are surrounded by invisible, necrotic spores
    that are harmless until you unleash them on a creature nearby. When a
    creature you can see moves into a space within 10 feet of you or starts its
    turn there, you can use your reaction to deal 1d4 necrotic damage to that
    creature unless it succeeds on a Constitution saving throw against your
    spell save DC. The necrotic damage increases to 1d6 at 6th level, 1d8 at
    10th level, and 1d10 at 14th level

    """

    name = "Halo of Spores"
    source = "Druid (Cirlce of Spores)"


class SymbioticEntity(Feature):
    """At 2nd level, you gain the ability to channel magic into your spores. As
    an action, you can expend a use of your Wild Shape feature to awaken those
    spores, rather than transforming into a beast form, and you gain 4
    temporary hit points for each level you have in this class. While this
    feature is active, you gain the following benefits:

    -- When you deal your Halo of Spores damage, roll the damage die a second
    time and add it to the total.

    -- Your melee weapon attacks deal an extra 1d6 poison damage to any target
    they hit.

    These benefits last for 10 minutes, until you lose all these temporary hit
    points, or until you use your Wild Shape again.

    """

    name = "Symbiotic Entity"
    source = "Druid (Circle of Spores)"


class FungalInfestation(Feature):
    """At 6th level, your spores gain the ability to infest a corpse and
    animate it. If a beast or a humanoid that is Small or Medium dies
    within 10 feet of you, you can use your reaction to animate it,
    causing it to stand up immediately with 1 hit point. The creature
    uses the zombie stat block in the Monster Manual. It remains
    animated for 1 hour, after which time it collapses and dies.

    In combat, the zombie's turn comes immediately after yours. It
    obeys your mental commands, and the only action it can take is the
    Attack action, making one melee attack.

    You can use this feature a number of times equal to your Wisdom
    modifier (minimum of once), and you regain all expended uses of it
    when you finish a long rest.

    """

    name = "Fungal Infestation"
    source = "Druid (Circle of Spores)"


class SpreadingSpores(Feature):
    """At 10th level, you gain the ability to seed an area with deadly spores.
    As a bonus action while your Symbiotic Entity feature is active, you can
    hurl spores up to 30 feet away, where they swirl in a 10-foot cube for 1
    minute. The spores disappear early if you use this feature again, if you
    dismiss them as a bonus action, or if your Symbiotic Entity feature is no
    longer active.

    Whenever a creature moves into the cube or starts its turn there, that
    creature takes your Halo of Spores damage, unless the creature succeeds on
    a Constitution saving throw against your spell save DC. A creature can take
    this damage nbo mre than once per turn.

    While the cube of spores persists, you can't use your Halo of Spores
    reaction.

    """

    name = "Spreading Spores"
    source = "Druid (Circle of Spores)"


class FungalBody(Feature):
    """At 14th level, the fungal spores in your body alter you: you can't be
    blinded, deafened, frightened, or poisoned, and any critical hit against
    you counts as a normal hit instead, unless you're incapacitated.

    """

    name = "Fungal Body"
    source = "Druid (Circle of Spores)"
