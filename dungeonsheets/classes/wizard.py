from collections import defaultdict

from dungeonsheets import features, weapons
from dungeonsheets.classes.classes import CharClass, SubClass


# PHB
class Abjuration(SubClass):
    """The School of Abjuration emphasizes magic that blocks, banishes, or
    protects. Detractors of this school say that its tradition is about denial,
    negation rather than positive assertion. You understand, however, that
    ending harmful effects, protecting the weak, and banishing evil influences
    is anything but a philosophical void. It is a proud and respected vocation.

    Called abjurers, members of this school are sought when baleful spirits
    require exorcism, when important locations must be guarded against magical
    spying, and when portals to other planes of existence must be closed.

    """

    name = "School of Abjuration"
    features_by_level = defaultdict(list)
    features_by_level[2] = [features.AbjurationSavant, features.ArcaneWard]
    features_by_level[6] = [features.ProjectedWard]
    features_by_level[10] = [features.ImprovedAbjuration]
    features_by_level[14] = [features.SpellResistance]


class Conjuration(SubClass):
    """As a conjurer, you favor spells that produce objects and creatures out o f
    thin air. You can conjure billowing clouds of killing fog or summon
    creatures from elsewhere to fight on your behalf. As your mastery grows,
    you learn spells of transportation and can teleport yourself across vast
    distances, even to other planes of existence, in an instant

    """

    name = "School of Conjuration"
    features_by_level = defaultdict(list)
    features_by_level[2] = [features.ConjurationSavant, features.MinorIllusion]
    features_by_level[6] = [features.BenignTransposition]
    features_by_level[10] = [features.FocusedConjuration]
    features_by_level[14] = [features.DurableSummons]


class Divination(SubClass):
    """The counsel of a diviner is sought by royalty and commoners alike, for all
    seek a clearer understanding of the past, present, and future. As a
    diviner, you strive to part the veils of space, time, and consciousness so
    that you can see clearly. You work to master spells of discernment, remote
    viewing, supernatural knowledge, and foresight.

    """

    name = "School of Divination"
    features_by_level = defaultdict(list)
    features_by_level[2] = [features.DivinationSavant, features.Portent]
    features_by_level[6] = [features.ExpertDivination]
    features_by_level[10] = [features.TheThirdEye]
    features_by_level[14] = [features.GreaterPortent]


class Enchantment(SubClass):
    """As a member of the School of Enchantment, you have honed your ability to
    magically entrance and beguile other people and monsters. Some enchanters
    are peacemakers who bewitch the violent to lay down their arms and charm
    the cruel into showing mercy. Others are tyrants who magically bind the
    unwilling into their service. Most enchanters fall somewhere in between.

    """

    name = "School of Enchantment"
    features_by_level = defaultdict(list)
    features_by_level[2] = [features.EnchantmentSavant, features.HypnoticGaze]
    features_by_level[6] = [features.InstinctiveGaze]
    features_by_level[10] = [features.SplitEnchantment]
    features_by_level[14] = [features.AlterMemories]


class Evocation(SubClass):
    """You focus your study on magic that creates powerful elemental effects such
    as bitter cold, searing flame, rolling thunder, crackling lightning, and
    burning acid. Some evokers find employment in military forces, serving as
    artillery to blast enemy armies from afar. Others use their spectacular
    power to protect the weak, while some seek their own gain as bandits,
    adventurers, or aspiring tyrants.

    """

    name = "School of Evocation"
    features_by_level = defaultdict(list)
    features_by_level[2] = [features.EvocationSavant, features.SculptSpells]
    features_by_level[6] = [features.PotentCantrip]
    features_by_level[10] = [features.EmpoweredEvocation]
    features_by_level[14] = [features.Overchannel]


class Illusion(SubClass):
    """You focus your studies on magic that dazzles the senses, befuddles the
    mind, and tricks even the wisest folk. Your magic is subtle, but the
    illusions crafted by your keen mind make the impossible seem real. Some
    illusionists-including many gnome wizards-are benign tricksters who use
    their spells to entertain. Others are more sinister masters of deception,
    using their illusions to frighten and fool others for their personal gain.

    """

    name = "School of Illusion"
    features_by_level = defaultdict(list)
    features_by_level[2] = [features.IllusionSavant, features.ImprovedMinorIllusion]
    features_by_level[6] = [features.MalleableIllusions]
    features_by_level[10] = [features.IllusorySelf]
    features_by_level[14] = [features.IllusoryReality]


class Necromancy(SubClass):
    """The School of Necromancy explores the cosm ic forces of life, death, and
    undeath. As you focus your studies in this tradition, you learn to
    manipulate the energy that animates all living things. As you progress, you
    learn to sap the life force from a creature as your magic destroys its
    body, transforming that vital energy into magical power you can manipulate.

    Most people see necromancers as menacing, or even villainous, due to the
    close association with death. Not all necromancers are evil, but the forces
    they manipulate are considered taboo by many societies

    """

    name = "School of Necromancy"
    features_by_level = defaultdict(list)
    features_by_level[2] = [features.NecromancySavant, features.GrimHarvest]
    features_by_level[6] = [features.UndeadThralls]
    features_by_level[10] = [features.InuredToUndeath]
    features_by_level[14] = [features.CommandUndead]


class Transmutation(SubClass):
    """You are a student of spells that modify energy and matter. To you, the
    world is not a fixed thing, but eminently mutable, and you delight in being
    an agent of change. You wield the raw stuff of creation and learn to alter
    both physical forms and mental qualities. Your magic gives you the tools to
    become a smith on reality's forge.

    Some transmuters are tinkerers and pranksters, turning people into toads
    and transforming copper into silver for fun and occasional profit. Others
    pursue their magical studies with deadly seriousness, seeking the power of
    the gods to make and destroy worlds

    """

    name = "School of Transmutation"
    features_by_level = defaultdict(list)
    features_by_level[2] = [features.TransmutationSavant, features.MinorAlchemy]
    features_by_level[6] = [features.TransmutersStone]
    features_by_level[10] = [features.Shapechanger]
    features_by_level[14] = [features.MasterTransmuter]


# SCAG
class Bladesinging(SubClass):
    """**Restriction: Elves Only**

    Bladesingers are elves who bravely defend their people and lands. They are
    elf wizards who master a school of sword fighting grounded in a tradition
    of arcane magic. In combat, a bladesinger uses a series of intricate,
    elegant maneuvers that fend off harm and allow the bladesinger to channel
    magic into devastating attacks and a cunning defense

    """

    name = "School of Bladesinging"
    _proficiencies_text = ("light armor",)
    skill_proficiencies = ("performance",)
    features_by_level = defaultdict(list)
    features_by_level[2] = [
        features.Bladesong,
    ]
    features_by_level[6] = [features.ExtraAttackBladesinging]
    features_by_level[10] = [features.SongOfDefense]
    features_by_level[14] = [features.SongOfVictory]


# XGTE
class WarMagic(SubClass):
    """A variety of arcane colleges specialize in training wiz- ards for war. The
    tradition of War Magic blends principles of evocation and abjuration,
    rather than specializing in either of those schools. It teaches
    techniques that empower a caster's spells, while also providing methods for
    wizards to bolster their own defenses.

    Followers of this tradition are known as war mages.  They see their magic
    as both a weapon and armor, a resource superior to any piece of steel. War
    mages act fast in battle, using their spells to seize tactical control of a
    situation. Their spells strike hard, while their defensive skills foil
    their opponents" attempts to counterattack. War mages are also adept at
    turning other spellcasters' magical energy against them.

    In great battles, a war mage often works with evokers, abjurers, and other
    types of wizards. Evokers, in particular, sometimes tease war mages for
    splitting their attention between offense and defense. A war mage's typical
    response: "What good is being able to throw a mighty fireball if I die
    before I can cast it?

    """

    name = "School of War Magic"
    features_by_level = defaultdict(list)
    features_by_level[2] = [features.ArcaneDeflection, features.TacticalWit]
    features_by_level[6] = [features.PowerSurge]
    features_by_level[10] = [features.DurableMagic]
    features_by_level[14] = [features.DeflectingShroud]


class Wizard(CharClass):
    name = "Wizard"
    hit_dice_faces = 6
    subclass_select_level = 2
    saving_throw_proficiencies = ("intelligence", "wisdom")
    primary_abilities = ("intelligence",)
    _proficiencies_text = (
        "daggers",
        "darts",
        "slings",
        "quarterstaffs",
        "light crossbows",
    )
    weapon_proficiencies = (
        weapons.Dagger,
        weapons.Dart,
        weapons.Sling,
        weapons.Quarterstaff,
        weapons.LightCrossbow,
    )
    multiclass_weapon_proficiencies = ()
    _multiclass_proficiencies_text = ()
    class_skill_choices = ("Arcana", "History", "Investigation", "Medicine", "Religion")
    features_by_level = defaultdict(list)
    features_by_level[1] = [features.ArcaneRecovery]
    features_by_level[18] = [features.SpellMastery]
    features_by_level[18] = [features.SignatureSpells]
    subclasses_available = (
        Abjuration,
        Conjuration,
        Divination,
        Enchantment,
        Evocation,
        Illusion,
        Necromancy,
        Transmutation,
        Bladesinging,
        WarMagic,
    )
    spellcasting_ability = "intelligence"
    spell_slots_by_level = {
        # char_lvl: (cantrips, 1st, 2nd, 3rd, ...)
        1: (3, 2, 0, 0, 0, 0, 0, 0, 0, 0),
        2: (3, 3, 0, 0, 0, 0, 0, 0, 0, 0),
        3: (3, 4, 2, 0, 0, 0, 0, 0, 0, 0),
        4: (4, 4, 3, 0, 0, 0, 0, 0, 0, 0),
        5: (4, 4, 3, 2, 0, 0, 0, 0, 0, 0),
        6: (4, 4, 3, 3, 0, 0, 0, 0, 0, 0),
        7: (4, 4, 3, 3, 1, 0, 0, 0, 0, 0),
        8: (4, 4, 3, 3, 2, 0, 0, 0, 0, 0),
        9: (4, 4, 3, 3, 3, 1, 0, 0, 0, 0),
        10: (5, 4, 3, 3, 3, 2, 0, 0, 0, 0),
        11: (5, 4, 3, 3, 3, 2, 1, 0, 0, 0),
        12: (5, 4, 3, 3, 3, 2, 1, 0, 0, 0),
        13: (5, 4, 3, 3, 3, 2, 1, 1, 0, 0),
        14: (5, 4, 3, 3, 3, 2, 1, 1, 0, 0),
        15: (5, 4, 3, 3, 3, 2, 1, 1, 1, 0),
        16: (5, 4, 3, 3, 3, 2, 1, 1, 1, 0),
        17: (5, 4, 3, 3, 3, 2, 1, 1, 1, 1),
        18: (5, 4, 3, 3, 3, 3, 1, 1, 1, 1),
        19: (5, 4, 3, 3, 3, 3, 2, 1, 1, 1),
        20: (5, 4, 3, 3, 3, 3, 2, 2, 1, 1),
    }
