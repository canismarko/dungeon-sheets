from collections import defaultdict

from dungeonsheets import features, weapons
from dungeonsheets.classes.classes import CharClass, SubClass


# Eberron Rising from the Last War
class Alchemist(SubClass):
    """An Alchemist is an expert at combining reagents to produce mystical
    effects. Alchemists use their creations to give life and to leech it away.
    Alchemy is the oldest of artificer traditions, and its versatility has
    long been valued during times of war and peace.
    """

    name = "Alchemist"
    features_by_level = defaultdict(list)
    features_by_level[3] = [
        features.AlchemistToolProficiency,
        features.AlchemistSpells,
        features.ExperimentalElixir,
    ]
    features_by_level[5] = [features.AlchemicalSavant]
    features_by_level[9] = [features.RestorativeReagents]
    features_by_level[15] = [features.ChemicalMastery]


class Artillerist(SubClass):
    """An Artillerist specializes in using magic to hurl energy, projectiles,
    and explosions on a battlefield. This destructive power was valued by all
    the armies of the Last War. Now that the war is over, some members of this
    specialization have sought to build a more peaceful world by using their
    powers to fight the resurgence of strife in Khorvaire. The gnome artificer
    Vi, an unlikely yet key member of House Cannith's warforged project, has
    been especially vocal about making things right: "It's about time we fixed
    things instead of blowing them all to hell."
    """

    name = "Artillerist"
    features_by_level = defaultdict(list)
    features_by_level[3] = [
        features.ArtilleristSpells,
        features.ArtilleristToolProficiency,
        features.EldritchCannon,
    ]
    features_by_level[5] = [features.ArcaneFirearm]
    features_by_level[9] = [features.ExplosiveCannon]
    features_by_level[15] = [features.FortifiedPosition]


class BattleSmith(SubClass):
    """Armies require protection, and someone has to put things back together
    if defenses fail. A combination of protector and medic, a Battle Smith is
    an expert at defending others and repairing both material and personnel.
    To aid in their work, Battle Smiths are usually accompanied by a steel
    defender, a protective companion of their own creation. Many soldiers tell
    stories of nearly dying before being saved by a Battle Smith and a steel
    defender.

    Battle Smiths played a key role in House Cannith's work on battle
    constructs and the original warforged, and after the Last War, these
    artificers led efforts to aid those who were injured in the war's horrific
    battles.
    """

    name = "Battle Smith"
    features_by_level = defaultdict(list)
    features_by_level[3] = [
        features.BattleSmithSpells,
        features.BattleSmithToolProficiency,
        features.BattleReady,
        features.SteelDefender,
    ]
    features_by_level[5] = [features.ExtraAttackBattleSmith]
    features_by_level[9] = [features.ArcaneJolt]
    features_by_level[15] = [features.ImprovedDefender]


class Artificer(CharClass):
    name = "Artificer"
    hit_dice_faces = 8
    subclass_select_level = 3
    subclasses_available = (Alchemist, Artillerist, BattleSmith)
    saving_throw_proficiencies = ("intelligence", "constitution")
    primary_abilities = ("intelligence",)
    _proficiencies_text = (
        "Light armor",
        "Medium armor",
        "Shields",
        "Simple weapons",
        "Thieve's tools",
        "Tinker's tools",
        "One type of artisan's tools of your choice",
    )
    _multiclass_proficiencies_text = (
        "Light armor",
        "Medium armor",
        "Shields",
        "Thieve's tools",
        "Tinker's tools",
    )
    weapon_proficiencies = (weapons.SimpleWeapon,)
    infusions = []
    class_skill_choices = (
        "Arcana",
        "History",
        "Investigation",
        "Medicine",
        "Nature",
        "Perception",
        "Sleight of Hand",
    )
    features_by_level = defaultdict(list)
    features_by_level[1] = [
        features.MagicalTinkering,
        features.FirearmProficiency,
        features.ArtificerSpellcasting,
        features.ArtificerRitualCasting,
    ]
    features_by_level[2] = [features.InfuseItem]
    features_by_level[3] = [features.TheRightToolForTheJob]
    features_by_level[6] = [features.ToolExpertise]
    features_by_level[7] = [features.FlashOfGenius]
    features_by_level[10] = [features.MagicItemAdept]
    features_by_level[11] = [features.SpellStoringItem]
    features_by_level[14] = [features.MagicItemSavant]
    features_by_level[18] = [features.MagicItemMaster]
    features_by_level[20] = [features.SoulOfArtifice]
    spellcasting_ability = "intelligence"
    spell_slots_by_level = {
        1: (2, 2, 0, 0, 0, 0, 0, 0, 0, 0),
        2: (2, 2, 0, 0, 0, 0, 0, 0, 0, 0),
        3: (2, 3, 0, 0, 0, 0, 0, 0, 0, 0),
        4: (2, 3, 0, 0, 0, 0, 0, 0, 0, 0),
        5: (2, 4, 2, 0, 0, 0, 0, 0, 0, 0),
        6: (2, 4, 2, 0, 0, 0, 0, 0, 0, 0),
        7: (2, 4, 3, 0, 0, 0, 0, 0, 0, 0),
        8: (2, 4, 3, 0, 0, 0, 0, 0, 0, 0),
        9: (2, 4, 3, 2, 0, 0, 0, 0, 0, 0),
        10: (3, 4, 3, 2, 0, 0, 0, 0, 0, 0),
        11: (3, 4, 3, 3, 0, 0, 0, 0, 0, 0),
        12: (3, 4, 3, 3, 0, 0, 0, 0, 0, 0),
        13: (3, 4, 3, 3, 1, 0, 0, 0, 0, 0),
        14: (4, 4, 3, 3, 1, 0, 0, 0, 0, 0),
        15: (4, 4, 3, 3, 2, 0, 0, 0, 0, 0),
        16: (4, 4, 3, 3, 2, 0, 0, 0, 0, 0),
        17: (4, 4, 3, 3, 3, 1, 0, 0, 0, 0),
        18: (4, 4, 3, 3, 3, 1, 0, 0, 0, 0),
        19: (4, 4, 3, 3, 3, 2, 0, 0, 0, 0),
        20: (4, 4, 3, 3, 3, 2, 0, 0, 0, 0),
    }
