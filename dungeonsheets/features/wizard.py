from dungeonsheets import spells
from dungeonsheets.features.features import Feature


# PHB
class ArcaneRecovery(Feature):
    """You have learned to regain some of your magical energy by studying
    your spellbook. Once per day when you finish a short rest, you can
    choose expended spell slots to recover. The spell slots can have a
    combined level that is equal to or less than half your wizard
    level (rounded up), and none of the slots can be 6th level or
    higher. For example, if you're a 4th-level wizard, you can recover
    up to two levels worth o f spell slots. You can recover either a
    2nd-level spell slot or two 1st-level spell slots

    """

    name = "Arcane Recovery"
    source = "Wizard"


class SpellMastery(Feature):
    """At 18th level, you have achieved such mastery over certain spells that you
    can cast them at will. Choose a 1st-level wizard spell and a 2nd-level
    wizard spell that are in your spellbook. You can cast those spells at their
    lowest level without expending a spell slot when you have them prepared. If
    you want to cast either spell at a higher level, you must expend a spell
    slot as normal. By spending 8 hours in study, you can exchange one or both
    o f the spells you chose for different spells of the same levels.

    """

    name = "Spell Mastery"
    source = "Wizard"


class SignatureSpells(Feature):
    """When you reach 20th level, you gain mastery over two powerful spells and
    can cast them with little effort. Choose two 3rd-level wizard spells in
    your spellbook as your signature spells. You always have these spells
    prepared, they don't count against the number of spells you have prepared,
    and you can cast each of them once at 3rd level without expending a spell
    slot. When you do so, you can't do so again until you finish a short or
    long rest. If you want to cast either spell at a higher level, you must
    expend a spell slot as normal.

    """

    name = "Signature Spells"
    source = "Wizard"


# Abjuration
class AbjurationSavant(Feature):
    """Beginning when you select this school at 2nd level, the gold and time you
    must spend to copy an abjuration spell into your spellbook is halved.

    """

    name = "Abjuration Savant"
    source = "Wizard (School of Abjuration)"


class ArcaneWard(Feature):
    """Starting at 2nd level, you can weave magic around yourself for
    protection. When you cast an abjuration spell of 1st level or higher, you
    can simultaneously use a strand of the spell's magic to create a magical
    ward on yourself that lasts until you finish a long rest. The ward has hit
    points equal to twice your wizard level + your Intelligence
    modifier. Whenever you take damage, the ward takes the damage instead. If
    this damage reduces the ward to 0 hit points, you take any remaining
    damage. While the ward has 0 hit points, it can't absorb damage, but its
    magic remains. Whenever you cast an abjuration spell of 1st level or
    higher, the ward regains a number of hit points equal to twice the level of
    the spell. Once you create the ward, you can't create it again until you
    finish a long rest

    """

    name = "Arcane Ward"
    source = "Wizard (School of Abjuration)"


class ProjectedWard(Feature):
    """Starting at 6th level, when a creature that you can see within 30 feet of
    you takes damage, you can use your reaction to cause your Arcane Ward to
    absorb that damage. If this damage reduces the ward to 0 hit points, the
    warded creature takes any remaining damage

    """

    name = "Projected Ward"
    source = "Wizard (School of Abjuration)"


class ImprovedAbjuration(Feature):
    """Beginning at 10th level, when you cast an abjuration spell that requires
    you to make an ability check as a part of casting that spell (as in
    counterspell and dispel magic), you add your proficiency bonus to that
    ability check.

    """

    name = "Improved Abjuration"
    source = "Wizard (School of Abjuration)"


class SpellResistance(Feature):
    """Starting at 14th level, you have advantage on saving throws against
    spells. Furthermore, you have resistance against the damage of spells

    """

    name = "Spell Resistance"
    source = "Wizard (School of Abjuration)"


# Conjuration
class ConjurationSavant(Feature):
    """Beginning when you select this school at 2nd level, the gold and time you
    must spend to copy a conjuration spell into your spellbook is halved.

    """

    name = "Conjuration Savant"
    source = "Wizard (School of Conjuration)"


class MinorIllusion(Feature):
    """Starting at 2nd level when you select this school, you can use your action
    to conjure up an inanimate object in your hand or on the ground in an
    unoccupied space that you can see within 10 feet of you. This object can be
    no larger than 3 feet on a side and weigh no more than 10 pounds, and its
    form must be that of a nonmagical object that you have seen. The object is
    visibly magical, radiating dim light out to 5 feet. The object disappears
    after 1 hour, when you use this feature again, or if it takes any damage.

    """

    name = "Minor Illusion"
    source = "Wizard (School of Conjuration)"


class BenignTransposition(Feature):
    """Starting at 6th level, you can use your action to teleport up to 30 feet to
    an unoccupied space that you can see. Alternatively, you can choose a space
    within range that is occupied by a Small or Medium creature. If that
    creature is willing, you both teleport, swapping places. Once you use this
    feature, you can't use it again until you finish a long rest or you cast a
    conjuration spell of 1st level or higher.

    """

    name = "Benign Transposition"
    source = "Wizard (School of Conjuration)"


class FocusedConjuration(Feature):
    """Beginning at 10th level, while you are concentrating on a conjuration
    spell, your concentration can't be broken as a result of taking damage

    """

    name = "Focused Conjuration"
    source = "Wizard (School of Conjuration)"


class DurableSummons(Feature):
    """Starting at 14th level, any creature that you summon or create with a
    conjuration spell has 30 temporary hit points

    """

    name = "Durable Summons"
    source = "Wizard (School of Conjuration)"


# Divination
class DivinationSavant(Feature):
    """Beginning when you select this school at 2nd level, the gold and time you
    must spend to copy a divination spell into your spellbook is halved.  P

    """

    name = "Divination Savant"
    source = "Wizard (School of Divination)"


class Portent(Feature):
    """Starting at 2nd level when you choose this school, glimpses of the future
    begin to press in on your awareness. When you finish a long rest, roll two
    d20s and record the numbers rolled. You can replace any attack roll, saving
    throw, or ability check made by you or a creature that you can see with one
    of these foretelling rolls. You must choose to do so before the roll, and
    you can replace a roll in this way only once per turn. Each foretelling
    roll can be used only once. When you finish a long rest, you lose any
    unused foretelling rolls

    """

    name = "Portent"
    source = "Wizard (School of Divination)"


class ExpertDivination(Feature):
    """Beginning at 6th level, casting divination spells comes so easily to you
    that it expends only a fraction of your spellcasting efforts. When you cast
    a divination spell of 2nd level or higher using a spell slot, you regain
    one expended spell slot. The slot you regain must be of a level lower than
    the spell you cast and can't be higher than 5th level.

    """

    name = "Expert Divination"
    source = "Wizard (School of Divination)"


class TheThirdEye(Feature):
    """Starting at 10th level, you can use your action to increase your powers o f
    perception. When you do so, choose one of the following benefits, which
    lasts until you are incapacitated or you take a short or long rest. You
    can't use the feature again until you finish a rest.

    **Darkvision**: You gain darkvision out to a range of 60 feet, as described
    in chapter 8.

    **Ethereal Sight**: You can see into the Ethereal Plane within 60
    feet of you.

    **Greater Comprehension**: You can read any language.

    **See Invisibility**: You can see invisible creatures and objects within 10
    feet of you that are within line of sight

    """

    name = "The Third Eye"
    source = "Wizard (School of Divination)"


class GreaterPortent(Feature):
    """Starting at 14th level, the visions in your dreams intensify and paint a
    more accurate picture in your mind of what is to come. You roll three d20s
    for your Portent feature, rather than two

    """

    name = "Greater Portent"
    source = "Wizard (School of Divination)"


# Enchantment
class EnchantmentSavant(Feature):
    """Beginning when you select this school at 2nd level, the gold and time you
    must spend to copy an enchantment spell into your spellbook is halved

    """

    name = "Enchantment Savant"
    source = "Wizard (School of Enchantment)"


class HypnoticGaze(Feature):
    """Starting at 2nd level when you choose this school, your soft words and
    enchanting gaze can magically enthrall another creature. As an action,
    choose one creature that you can see within 5 feet of you. If the target
    can see or hear you, it must succeed on a Wisdom saving throw against your
    wizard spell save DC or be charmed by you until the end of your next
    turn. The charmed creature's speed drops to 0, and the creature is
    incapacitated and visibly dazed.

    On subsequent turns, you can use your action to maintain this effect,
    extending its duration until the end of your next turn. However, the effect
    ends if you move more than 5 feet away from the creature, if the creature
    can neither see nor hear you, or if the creature takes damage. Once the
    effect ends, or if the creature succeeds on its initial saving throw
    against this effect, you can't use this feature on that creature again
    until you finish a long rest

    """

    name = "Hypnotic Gaze"
    source = "Wizard (School of Enchantment)"


class InstinctiveGaze(Feature):
    """Beginning at 6th level, when a creature you can see within 30 feet of you
    makes an attack roll against you, you can use your reaction to divert the
    attack, provided that another creature is within the attack's range. The
    attacker must make a W isdom saving throw against your wizard spell save
    DC. On a failed save, the attacker must target the creature that is closest
    to it, not including you or itself. If multiple creatures are closest, the
    attacker chooses which one to target. On a successful save, you can't use
    this feature on the attacker again until you finish a long rest. You must
    choose to use this feature before knowing whether the attack hits or
    misses. Creatures that can't be charmed are immune to this effect.

    """

    name = "Instinctive Gaze"
    source = "Wizard (School of Enchanment)"


class SplitEnchantment(Feature):
    """Starting at 10th level, when you cast an enchantment spell of 1st level or
    higher that targets only one creature, you can have it target a second
    creature.

    """

    name = "Split Enchantment"
    source = "Wizard (School of Enchanment)"


class AlterMemories(Feature):
    """At 14th level, you gain the ability to make a creature unaware of your
    magical influence on it. When you cast an enchantment spell to charm one or
    more creatures, you can alter one creature's understanding so that it
    remains unaware of being charmed. Additionally, once before the spell
    expires, you can use your action to try to make the chosen creature forget
    some of the time it spent charmed. The creature must succeed on an
    Intelligence saving throw against your wizard spell save DC or lose a
    number of hours of its memories equal to 1 + your Charisma modifier
    (minimum 1). You can make the creature forget less time, and the amount of
    time can't exceed the duration of your enchantment spell.

    """

    _name = "Alter Memories"
    source = "Wizard (School of Enchanment)"

    @property
    def name(self):
        num = 1 + max(0, self.owner.charisma.modifier)
        return self._name + " ({:d} hours)".format(num)


# Evocation
class EvocationSavant(Feature):
    """Beginning when you select this school at 2nd level, the gold and time you
    must spend to copy an evocation spell into your spellbook is halved.

    """

    name = "Evocation Savant"
    source = "Wizard (School of Evocation)"


class SculptSpells(Feature):
    """Beginning at 2nd level, you can create pockets of relative safety within the
    effects of your evocation spells. When you cast an evocation spell that
    affects other creatures that you can see, you can choose a number of them
    equal to 1 + the spell's level. The chosen creatures automatically succeed
    on their saving throws against the spell, and they take no damage if they
    would normally take half damage on a successful save

    """

    name = "Sculpt Spells"
    source = "Wizard (School of Evocation)"


class PotentCantrip(Feature):
    """Starting at 6th level, your damaging cantrips affect even creatures that
    avoid the brunt of the effect. When a creature succeeds on a saving throw
    against your cantrip, the creature takes half the cantrip's damage (if any)
    but suffers no additional effect from the cantrip

    """

    name = "Potent Cantrip"
    source = "Wizard (School of Evocation)"


class EmpoweredEvocation(Feature):
    """Beginning at 10th level, you can add your Intelligence modifier to the
    damage roll of any wizard evocation spell you cast

    """

    name = "Empowered Evocation"
    source = "Wizard (School of Evocation)"


class Overchannel(Feature):
    """Starting at 14th level, you can increase the power of your simpler
    spells. When you cast a wizard spell of 5th level or lower that deals
    damage, you can deal maximum damage with that spell. The first time you do
    so, you suffer no adverse effect.  If you use this feature again before you
    finish a long rest, you take 2d12 necrotic damage for each level of the
    spell, immediately after you cast it. Each time you use this feature again
    before finishing a long rest, the necrotic damage per spell level increases
    by 1d12. This damage ignores resistance and immunity.

    """

    name = "Overchannel"
    source = "Wizard (School of Evocation)"


# Illusion
class IllusionSavant(Feature):
    """Beginning when you select this school at 2nd level, the gold and time you
    must spend to copy an illusion spell into your spellbook is halved.

    """

    name = "Illusion Savant"
    source = "Wizard (School of Illusion)"


class ImprovedMinorIllusion(Feature):
    """When you choose this school at 2nd level, you learn the minor illusion
    cantrip. If you already know this cantrip, you learn a different wizard
    cantrip of your choice. The cantrip doesn't count against your number of
    cantrips known. When you cast minor illusion, you can create both a sound
    and an image with a single casting o f the spell.

    """

    name = "Improved Minor Illusion"
    source = "Wizard (School of Illusion)"


class MalleableIllusions(Feature):
    """Starting at 6th level, when you cast an illusion spell that has a duration
    of 1 minute or longer, you can use your action to change the nature of that
    illusion (using the spell's normal parameters for the illusion), provided
    that you can see the illusion

    """

    name = "Malleable Illusions"
    source = "Wizard (School of Illusion)"


class IllusorySelf(Feature):
    """Beginning at 10th level, you can create an illusory duplicate of yourself
    as an instant, almost instinctual reaction to danger. When a creature makes
    an attack roll against you, you can use your reaction to interpose the
    illusory duplicate between the attacker and yourself. The attack
    automatically m isses you, then the illusion dissipates. Once you use this
    feature, you can't use it again until you finish a short or long rest.

    """

    name = "Illusory Self"
    source = "Wizard (School of Illusion)"


class IllusoryReality(Feature):
    """By 14th level, you have learned the secret of weaving shadow magic into
    your illusions to give them a semi- reality. When you cast an illusion
    spell of 1st level or higher, you can choose one inanimate, nonmagical
    object that is part of the illusion and make that object real. You can do
    this on your turn as a bonus action while the spell is ongoing. The object
    remains real for 1 minute. For example, you can create an illusion of a
    bridge over a chasm and then make it real long enough for your allies to
    cross. The object can't deal damage or otherwise directly harm anyone

    """

    name = "Illusory Reality"
    source = "Wizard (School of Illusion)"


# Necromancy
class NecromancySavant(Feature):
    """Beginning when you select this school at 2nd level, the gold and time you
    must spend to copy an Necromancy spell into your spellbook is halved.

    """

    name = "Necromancy Savant"
    source = "Wizard (School of Necromancy)"


class GrimHarvest(Feature):
    """At 2nd level, you gain the ability to reap life energy from creatures you
    kill with your spells. Once per turn when you kill one or more creatures
    with a spell of 1st level or higher, you regain hit points equal to twice
    the spell's level, or three times its level if the spell belongs to the
    School of Necromancy. You don't gain this benefit for killing constructs or
    undead"""

    name = "Grim Harvest"
    source = "Wizard (School of Necromancy)"


class UndeadThralls(Feature):
    """At 6th level, you add the animate dead spell to your spellbook if
    it is not there already. When you cast animate dead, you can
    target one additional corpse or pile of bones, creating another
    zombie or skeleton, as appropriate. Whenever you create an undead
    using a necromancy spell, it has additional benefits:

    - The creature's hit point maximum is increased by an amount equal
      to your wizard level.
    - The creature adds your proficiency bonus to its weapon damage
      rolls

    """

    name = "Undead Thralls"
    source = "Wizard (School of Necromancy)"
    spells_known = (spells.AnimateDead,)


class InuredToUndeath(Feature):
    """Beginning at 10th level, you have resistance to necrotic damage, and your
    hit point maximum can't be reduced. You have spent so much time dealing
    with undead and the forces that animate them that you have become inured to
    some of their worst effects

    """

    name = "Inured to Undeath"
    source = "Wizard (School of Necromancy)"


class CommandUndead(Feature):
    """Starting at 14th level, you can use magic to bring undead under your
    control, even those created by other wizards. As an action, you can choose
    one undead that you can see within 60 feet of you. That creature must make
    a Charisma saving throw against your wizard spell save DC. If it succeeds,
    you can't use this feature on it again. If it fails, it becomes friendly to
    you and obeys your commands until you use this feature again. Intelligent
    undead are harder to control in this way.  If the target has an
    Intelligence of 8 or higher, it has advantage on the saving throw. If it
    fails the saving throw and has an Intelligence of 12 or higher, it can
    repeat the saving throw at the end of every hour until it succeeds and
    breaks free

    """

    name = "Command Undead"
    source = "Wizard (School of Necromancy)"


# Transmutation
class TransmutationSavant(Feature):
    """Beginning when you select this school at 2nd level, the gold and time you
    must spend to copy an Transmutation spell into your spellbook is halved.

    """

    name = "Transmutation Savant"
    source = "Wizard (School of Transmutation)"


class MinorAlchemy(Feature):
    """Starting at 2nd level when you select this school, you can temporarily alter
    the physical properties of one nonmagical object, changing it from one
    substance into another. You perform a special alchemical procedure on one
    object composed entirely of wood, stone (but not a gemstone), iron, copper,
    or silver, transforming it into a different one of those materials. For
    each 10 minutes you spend performing the procedure, you can transform up to
    1 cubic foot of material. After 1 hour, or until you lose your
    concentration (as if you were concentrating on a spell), the material
    reverts to its original substance

    """

    name = "Minor Alchemy"
    source = "Wizard (School of Transmutation)"


class TransmutersStone(Feature):
    """Starting at 6th level, you can spend 8 hours creating a
    transmuter's stone that stores transmutation magic. You can
    benefit from the stone yourself or give it to another creature. A
    creature gains a benefit of your choice as long as the stone is in
    the creature's possession. When you create the stone, choose the
    benefit from the following options:

    - Darkvision out to a range of 60 feet, as described in chapter 8
    - An increase to speed of 10 feet while the creature is
      unencumbered
    - Proficiency in Constitution saving throws
    - Resistance to acid, cold, fire, lightning, or thunder damage
      (your choice whenever you choose this benefit)

    Each time you cast a transmutation spell of 1st level or higher,
    you can change the effect of your stone if the stone is on your
    person. If you create a new transmuter's stone, the previous one
    ceases to function

    """

    name = "Transmuter's Stone"
    source = "Wizard (School of Transmutation)"


class Shapechanger(Feature):
    """At 10th level, you add the polymorph spell to your spellbook, if it
    is not there already. You can cast polymorph without expending a
    spell slot. When you do so, you can target only yourself and
    transform into a beast whose challenge rating is 1 or lower. Once
    you cast polymorph in this way, you can't do so again until you
    finish a short or long rest, though you can still cast it normally
    using an available spell slot

    """

    name = "Shapechanger"
    source = "Wizard (School of Transmutation)"
    spells_known = spells_prepared = (spells.Polymorph,)


class MasterTransmuter(Feature):
    """Starting at 14th level, you can use your action to consume the reserve of
    transmutation magic stored within your transmuter's stone in a single
    burst. When you do so, choose one of the following effects. Your
    transmuter's stone is destroyed and can't be remade until you finish a long
    rest.

    **Major Transformation**: You can transmute one nonmagical object-no
    larger than a 5-foot cube-into another nonmagical object of similar size
    and mass and of equal or lesser value. You must spend 10 minutes handling
    the object to transform it.

    **Panacea**: You remove all curses, diseases, and poisons affecting a creature
    that you touch with the transmuter's stone. The creature also regains all
    its hit points.

    **Restore Life**: You cast the raise dead spell on a creature you touch
    with the transmuter's stone, without expending a spell slot or needing to
    have the spell in your spellbook.

    **Restore Youth**: You touch the transmuter's stone to a willing creature,
    and that creature's apparent age is reduced by 3d10 years, to a minimum of
    13 years. This effect doesn't extend the creature's lifespan

    """

    name = "Master Transmuter"
    source = "Wizard (School of Transmutation)"


# Bladesinging
class Bladesong(Feature):
    """Starting at 2nd level, you can invoke a secret Elven magic called
    the Bladesong, provided that you aren't wearing medium or heavy
    armor or using a shield. It graces you with supernatural speed,
    agility, and focus. You can use a bonus action to start the
    Bladesong, which lasts for 1 minute. It ends early if you are
    incapac- itated, if you don medium or heavy armor or a shield, or
    if you use two hands to make an attack with a weapon. You can also
    dismiss the Bladesong at any time you choose (no action required).

    While your Bladesong is active, you gain the following benefits:

    - You gain a bonus to your AC equal to your Intelligence modifier
      (minimum of +1).
    - Your walking speed increases by 10 feet.
    - You have advantage on Dexterity (Acrobatics) checks.
    - You gain a bonus to any Constitution saving throw you make to
      maintain your concentration on a spell. The bonus equals your
      Intelligence modifier (minimum of +l).

    You can use this feature twice. You regain all expended uses of it
    when you finish a short or long rest.

    """

    name = "Bladesong (2x/SR)"
    source = "Wizard (School of Bladesinging)"


class ExtraAttackBladesinging(Feature):
    """Starting at 6th level, you can attack twice, instead of once, whenever you
    take the Attack action on your turn.

    """

    name = "Extra Attack (2x)"
    source = "Wizard (School of Bladesinging)"


class SongOfDefense(Feature):
    """Beginning at 10th level, you can direct your magic to ab- sorb damage
    while your Bladesong is active. When you take damage, you can use your
    reaction to expend one spell slot and reduce that damage to you by an
    amount equal to five times the spell slot's level.

    """

    name = "Song of Defense"
    source = "Wizard (School of Bladesinging)"


class SongOfVictory(Feature):
    """Starting at 14th level, you add your Intelligence modifier (minimum of +1)
    to the damage of your melee weapon attacks while you r Bladesong is active

    """

    name = "Song of Victory"
    source = "Wizard (School of Bladesinging)"


# War Magic
class ArcaneDeflection(Feature):
    """At 2nd level, you have learned to weave your magic to fortify yourself
    against harm. When you are hit by an at- tack or you fail a saving throw,
    you can use your reaction to gain a +2 bonus to your AC against that attack
    or a +4 bonus to that saving throw. When you use this feature, you can't
    cast spells other than cantrips until the end of your next turn.

    """

    name = "Arcane Deflection"
    source = "Wizard (School of War Magic)"


class TacticalWit(Feature):
    """Starting at 2nd level, your keen ability to assess tactical situations
    allows you to act quickly in battle. You can give yourself a bonus to your
    initiative rolls equal to your Intelligence modifier (included in stats on
    character sheet).

    """

    name = "Tactical Wit"
    source = "Wizard (School of War Magic)"


class PowerSurge(Feature):
    """Starting at 6th level, you can store magical energy within yourself to
    later empower your damaging spells. In its stored form, this energy is
    called a power surge. You can store a maximum number of power surges equal
    to your Intelligence modifier (minimum of one). Whenever you finish a long
    rest, your number of power surges reset-s to one. Whenever you successfully
    end a spell with dispel magic or counterspel], you gain one power surge, as
    you steal magic from the spell you foiled. If you end a short rest with no
    power surges, you gain one power surge

    Once per turn when you deal damage to a creature or object with a wizard
    spell, you can spend one power surge to deal extra force damage to that
    target. The ex- tra damage equals half your wizard level.

    """

    name = "Power Surge"
    source = "Wizard (School of War Magic)"


class DurableMagic(Feature):
    """Beginning at 10th level, the magic you channel helps ward off harm. While
    you maintain concentration on a spell, you have a +2 bonus to AC and all
    saving throws.

    """

    name = "Durable Magic"
    source = "Wizard (School of War Magic)"


class DeflectingShroud(Feature):
    """At 14th level, your Arcane Deflection becomes infused with deadly
    magic. When you use your Arcane Deflec- tion feature, you can cause magical
    energy to are from you. Up to three creatures ofyour choice that you can
    see within 60 feet of you each take force damage equal to half your wizard
    level.

    """

    name = "Deflecting Shroud"
    source = "Wizard (School of War Magic)"
