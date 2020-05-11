from collections import defaultdict

from dungeonsheets import exceptions, features, monsters, weapons
from dungeonsheets.classes.classes import CharClass, SubClass
from dungeonsheets.stats import findattr


class Alchemist(SubClass):
    """An Alchemist is an expert at combining reagents to pro­duce mystical
    effects. Alchemists use their creations to give life and to leech it away.
    Alchemy is the oldest of ar­tificer traditions, and its versatility has
    long been valued during times of war and peace.
    """

    name = "Alchemist"
    features_by_level = defaultdict(list)
    features_by_level[3] = [features.ToolProficiency]
    features_by_level[5] = [features.AlchemicalSavant]
    features_by_level[9] = [features.RestorativeReagents]
    features_by_level[15] = [features.ChemicalMastery]


class Artificer(CharClass):
    name = "Artificer"
    hit_dice_faces = 8
    subclass_select_level = 3
    saving_throw_proficiencies = ('intelligence', 'constitution')
    primary_abilities = ('intelligence',)
    _proficiencies_text = (
            'Light armor', 'Medium armor', 'Shields', 'Simple weapons',
            'Thieve\'s tools', 'Tinker\'s tools',
            'One type of artisan\'s tools of your choice')
    weapon_proficiencies = (weapon.SimpleWeapon)
    class_skill_choices = ('Arcana', 'History', 'Investigation', 'Medicine',
            'Nature', 'Perception', 'Sleight of Hand')
    features_by_level = defaultdict(list)
    features_by_level[1] = [features.MagicalTinkering]
    features_by_level[2] = [features.InfuseItem]
    features_by_level[3] = [features.TheRightToolForTheJob]
    features_by_level[6] = [features.ToolExpertise]
    features_by_level[7] = [features.FlashOfGenius]
    features_by_level[10] = [features.MagicItemAdept]
    features_by_level[11] = [features.SpellStoringItem]
    features_by_level[14] = [features.MagicItemSavant]
    features_by_level[18] = [features.MagicItemMaster]
    features_by_level[20] = [features.SoulOfArtifice]
    subclasses_available = (Alchemist, Artillerist, BattleSmith)
    spellcasting_ability = 'intelligence'
    spell_slots_by_level = {
            1:  (2, 2, 0, 0, 0, 0, 0, 0, 0, 0),
            2:  (2, 2, 0, 0, 0, 0, 0, 0, 0, 0),
            3:  (2, 3, 0, 0, 0, 0, 0, 0, 0, 0),
            4:  (2, 3, 0, 0, 0, 0, 0, 0, 0, 0),
            5:  (2, 4, 2, 0, 0, 0, 0, 0, 0, 0),
            6:  (2, 4, 2, 0, 0, 0, 0, 0, 0, 0),
            7:  (2, 4, 3, 0, 0, 0, 0, 0, 0, 0),
            8:  (2, 4, 3, 0, 0, 0, 0, 0, 0, 0),
            9:  (2, 4, 3, 2, 0, 0, 0, 0, 0, 0),
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

