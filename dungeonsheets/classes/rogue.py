from collections import defaultdict

from dungeonsheets import features, weapons
from dungeonsheets.classes.classes import CharClass, SubClass


# PHB
class Thief(SubClass):
    """You hone your skills in the larcenous arts. Burglars, bandits, cutpurses,
    and other criminals typically follow this archetype, but so do rogues who
    prefer to think of themselves as professional treasure seekers, explorers,
    delvers, and investigators. In addition to improving your agility and
    stealth, you learn skills useful for delving into ancient ruins, reading
    unfamiliar languages, and using magic items you normally couldn't employ

    """

    name = "Thief"
    features_by_level = defaultdict(list)
    features_by_level[3] = [features.FastHands, features.SecondStoryWork]
    features_by_level[9] = [features.SupremeSneak]
    features_by_level[13] = [features.UseMagicDevice]
    features_by_level[17] = [features.ThiefsReflexes]


class Assassin(SubClass):
    """You focus your training on the grim art of death. Those who adhere to this
    archetype are diverse: hired killers, spies, bounty hunters, and even
    specially anointed priests trained to exterminate the enemies of their
    deity. Stealth, poison, and disguise help you eliminate your foes with
    deadly efficiency

    """

    name = "Assassin"
    _proficiencies_text = ("disguise kit", "poisoner's kit")
    features_by_level = defaultdict(list)
    features_by_level[3] = [features.Assassinate]
    features_by_level[9] = [features.InfiltrationExpertise]
    features_by_level[13] = [features.Imposter]
    features_by_level[17] = [features.DeathStrike]


class ArcaneTrickster(SubClass):
    """Some rogues enhance their fine-honed skills of stealth and agility with
    magic, learning tricks of enchantment and illusion. These rogues include
    pickpockets and burglars, but also pranksters, mischief-makers, and a
    significant number of adventurers.

    """

    name = "Arcane Trickster"
    features_by_level = defaultdict(list)
    features_by_level[3] = [features.MageHandLegerdemain]
    features_by_level[9] = [features.MagicalAmbush]
    features_by_level[13] = [features.VersatileTrickster]
    features_by_level[17] = [features.SpellThief]
    spellcasting_ability = "intelligence"
    multiclass_spellslots_by_level = {
        # char_lvl: (cantrips, 1st, 2nd, 3rd, ...)
        1: (0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
        2: (0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
        3: (3, 2, 0, 0, 0, 0, 0, 0, 0, 0),
        4: (3, 3, 0, 0, 0, 0, 0, 0, 0, 0),
        5: (3, 3, 0, 0, 0, 0, 0, 0, 0, 0),
        6: (3, 3, 0, 0, 0, 0, 0, 0, 0, 0),
        7: (3, 4, 2, 0, 0, 0, 0, 0, 0, 0),
        8: (3, 4, 2, 0, 0, 0, 0, 0, 0, 0),
        9: (3, 4, 2, 0, 0, 0, 0, 0, 0, 0),
        10: (4, 4, 3, 0, 0, 0, 0, 0, 0, 0),
        11: (4, 4, 3, 0, 0, 0, 0, 0, 0, 0),
        12: (4, 4, 3, 0, 0, 0, 0, 0, 0, 0),
        13: (4, 4, 3, 2, 0, 0, 0, 0, 0, 0),
        14: (4, 4, 3, 2, 0, 0, 0, 0, 0, 0),
        15: (4, 4, 3, 2, 0, 0, 0, 0, 0, 0),
        16: (4, 4, 3, 3, 0, 0, 0, 0, 0, 0),
        17: (4, 4, 3, 3, 0, 0, 0, 0, 0, 0),
        18: (4, 4, 3, 3, 0, 0, 0, 0, 0, 0),
        19: (4, 4, 3, 3, 1, 0, 0, 0, 0, 0),
        20: (4, 4, 3, 3, 1, 0, 0, 0, 0, 0),
    }


# XGTE
class Inquisitive(SubClass):
    """As an archetypal Inquisitive, you excel at rooting out se- crets and
    unraveling mysteries. You rely on your sharp eye for detail, but also on
    your finely honed ability to read the words and deeds of other creatures to
    deter- mine their true intent. You excel at defeating creatures that hide
    among and prey upon ordinary folk, and your mastery of lore and your keen
    deductions make you well equipped to expose and end hidden evils

    """

    name = "Inquisitive"
    features_by_level = defaultdict(list)
    features_by_level[3] = [
        features.EarForDeceit,
        features.EyeForDetail,
        features.InsightfulFighting,
    ]
    features_by_level[9] = [features.SteadyEye]
    features_by_level[13] = [features.UnerringEye]
    features_by_level[17] = [features.EyeForWeakness]


class Mastermind(SubClass):
    """Your focus is on people and on the influence and secrets they have. Many
    spies, courtiers, and schemers follow this archetype, leading lives of
    intrigue. Words are your weapons as often as knives or poison, and secrets
    and favors are some of your favorite treasures.

    """

    name = "Mastermind"
    features_by_level = defaultdict(list)
    features_by_level[3] = [features.MasterOfIntrigue, features.MasterOfTactics]
    features_by_level[9] = [features.InsightfulManipulator]
    features_by_level[13] = [features.Misdirection]
    features_by_level[17] = [features.SoulOfDeceit]


class Scout(SubClass):
    """You are skilled in stealth and surviving far from the streets of a city,
    allowing you to scout ahead of your companions during expeditions. Rogues
    who embrace this archetype are at home in the wilderness and among
    barbarians and rangers, and many Scouts serve as the eyes and ears of war
    bands. Ambusher, spy, bounty hunter#these are just a few of the roles that
    Scouts as- sume as they range the world.

    """

    name = "Scout"
    skill_proficiencies = ("nature", "survival")
    features_by_level = defaultdict(list)
    features_by_level[3] = [features.Skirmisher, features.Survivalist]
    features_by_level[9] = [features.SuperiorMobility]
    features_by_level[13] = [features.AmbushMaster]
    features_by_level[17] = [features.SuddenStrike]


class Swashbuckler(SubClass):
    """You focus your training on the art of the blade, relying on speed,
    elegance, and charm in equal parts. While some warriors are brutes clad in
    heavy armor, your method of fighting looks almost like a performance.
    Duelists and pirates typically belong to this archetype. A Swashbuckler
    excels in single combat, and can fight with two weapons while safely
    darting away from an opponent

    """

    name = "Swashbuckler"
    features_by_level = defaultdict(list)
    features_by_level[3] = [features.FancyFootwork, features.RakishAudacity]
    features_by_level[9] = [features.Panache]
    features_by_level[13] = [features.ElegantManeuver]
    features_by_level[17] = [features.MasterDuelist]


class Rogue(CharClass):
    name = "Rogue"
    hit_dice_faces = 8
    subclass_select_level = 3
    saving_throw_proficiencies = ("dexterity", "intelligence")
    primary_abilities = ("dexterity",)
    _proficiencies_text = (
        "light armor",
        "simple weapons",
        "hand crossbows",
        "longswords",
        "rapiers",
        "shortswords",
        "thieves' tools",
    )
    weapon_proficiencies = (
        weapons.SimpleWeapon,
        weapons.HandCrossbow,
        weapons.Longsword,
        weapons.Rapier,
        weapons.Shortsword,
    )
    multiclass_weapon_proficiencies = ()
    _multiclass_proficiencies_text = (
        "light armor",
        "thieves' tools",
        "[choose one skill from Rogue list]",
    )
    class_skill_choices = (
        "Acrobatics",
        "Athletics",
        "Deception",
        "Insight",
        "Intimidation",
        "Investigation",
        "Perception",
        "Performance",
        "Persuasion",
        "Sleight of Hand",
        "Stealth",
    )
    num_skill_choices = 4
    features_by_level = defaultdict(list)
    features_by_level[1] = [features.RogueExpertise, features.SneakAttack]
    features_by_level[2] = [features.CunningAction]
    features_by_level[5] = [features.UncannyDodge]
    features_by_level[7] = [features.Evasion]
    features_by_level[11] = [features.ReliableTalent]
    features_by_level[14] = [features.BlindSense]
    features_by_level[15] = [features.SlipperyMind]
    features_by_level[18] = [features.Elusive]
    features_by_level[20] = [features.StrokeOfLuck]
    subclasses_available = (
        Thief,
        Assassin,
        ArcaneTrickster,
        Inquisitive,
        Mastermind,
        Scout,
        Swashbuckler,
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # slippery mind feature
        if self.owner.Rogue.level >= 15:
            self.saving_throw_proficiencies = ("dexterity", "intelligence", "wisdom")
