from . import (weapons, spells)
from . import features as feats
from collections import defaultdict


class Race():
    name = "Unknown"
    size = "medium"
    speed = 30
    owner = None
    languages = ('Common', )
    proficiencies_text = tuple()
    weapon_proficiences = tuple()
    skill_proficiencies = ()
    skill_choices = ()
    num_skill_choices = 0
    features = tuple()
    features_by_level = defaultdict(list)
    strength_bonus = 0
    dexterity_bonus = 0
    constitution_bonus = 0
    intelligence_bonus = 0
    wisdom_bonus = 0
    charisma_bonus = 0
    hit_point_bonus = 0
    spells_known = ()

    def __init__(self, owner=None):
        self.owner = owner
        cls = type(self)
        # Instantiate the features
        self.features = tuple([f(owner=self.owner) for f in cls.features])
        self.features_by_level = defaultdict(list)
        for i in range(1, 21):
            self.features_by_level[i] = [f(owner=self.owner)for f in
                                         cls.features_by_level[i]]
        self.spells_known = [S() for S in cls.spells_known]

    @property
    def spells_prepared(self):
        return self.spells_known

    def __str__(self):
        return self.name

    def __repr__(self):
        return "\"{:s}\"".format(self.name)


# Dwarves
class _Dwarf(Race):
    name = "Dwarf"
    size = "medium"
    speed = 25
    languages = ("Common", "Dwarvish")
    constitution_bonus = 2
    proficiencies_text = ('battleaxes', 'handaxes', 'throwing hammers',
                          'warhammers')
    weapon_proficiences = (weapons.Battleaxe, weapons.Handaxe,
                           weapons.ThrowingHammer, weapons.Warhammer)
    features = (feats.Darkvision, feats.DwarvenResilience, feats.Stonecunning)


class HillDwarf(_Dwarf):
    name = "Hill Dwarf"
    wisdom_bonus = 1
    hit_point_bonus = 1
    features = _Dwarf.features + (feats.DwarvenToughness,)


class MountainDwarf(_Dwarf):
    name = "Mountain Dwarf"
    strength_bonus = 2


# Elves
class _Elf(Race):
    name = "Elf"
    size = "medium"
    speed = 30
    dexterity_bonus = 2
    skill_proficiencies = ('perception',)
    languages = ('Common', 'Elvish')
    features = (feats.Darkvision, feats.FeyAncestry, feats.Trance)


class HighElf(_Elf):
    name = "High Elf"
    weapon_proficiencies = (weapons.Longsword, weapons.Shortsword,
                            weapons.Shortbow, weapons.Longbow)
    proficiencies_text = ('longswords', 'shortswords', 'shortbows', 'longbows')
    intelligence_bonus = 1
    languages = ('Common', 'Elvish', '[choose one]')
    features = _Elf.features + (feats.ElfCantrip,)


class WoodElf(_Elf):
    name = "Wood Elf"
    weapon_proficiencies = (weapons.Longsword, weapons.Shortsword,
                            weapons.Shortbow, weapons.Longbow)
    proficiencies_text = ('longswords', 'shortswords', 'shortbows', 'longbows')
    wisdom_bonus = 1
    speed = 35
    features = _Elf.features + (feats.MaskOfTheWild,)


class DarkElf(_Elf):
    name = "Dark Elf"
    weapon_proficiencies = (weapons.Rapier, weapons.Shortsword,
                            weapons.HandCrossbow)
    proficiencies_text = ('rapiers', 'shortswords', 'hand crossbows')
    charisma_bonus = 1
    features = (feats.SuperiorDarkvision, feats.FeyAncestry, feats.Trance,
                feats.SunlightSensitivity, feats.DrowMagic)
    spells_known = (spells.DancingLights,)


# Halflings
class _Halfling(Race):
    name = "Halfling"
    size = "small"
    speed = 25
    dexterity_bonus = 2
    languages = ('Common', 'Halfling')
    features = (feats.Lucky, feats.Brave, feats.HalflingNimbleness)


class LightfootHalfling(_Halfling):
    name = "Lightfoot Halfling"
    charisma_bonus = 1
    features = _Halfling.features + (feats.NaturallyStealthy,)


class StoutHalfling(_Halfling):
    name = "Stout Halfling"
    constitution_bonus = 1
    features = _Halfling.features + (feats.StoutResilience,)


# Humans
class _Human(Race):
    name = "Human"
    size = "medium"
    speed = 30
    strength_bonus = 1
    dexterity_bonus = 1
    constitution_bonus = 1
    intelligence_bonus = 1
    wisdom_bonus = 1
    charisma_bonus = 1
    languages = ("Common", '[choose one]')


class Rashemi(_Human):
    name = 'Rashemi'


# Dragonborn
class Dragonborn(Race):
    name = "Dragonborn"
    size = "medium"
    speed = 30
    strength_bonus = 2
    charisma_bonus = 1
    languages = ("Common", "Draconic")
    features = (feats.DraconicAncestry, feats.BreathWeapon,
                feats.DraconicResistance)


# Gnomes
class _Gnome(Race):
    name = "Gnome"
    size = "small"
    speed = 25
    intelligence_bonus = 2
    languages = ("Common", "Gnomish")
    features = (feats.Darkvision, feats.GnomeCunning)


class ForestGnome(_Gnome):
    name = "Forest Gnome"
    dexterity_bonus = 1
    features = _Gnome.features + (feats.NaturalIllusionist,
                                  feats.SpeakWithSmallBeasts)
    spells_known = (spells.MinorIllusion,)


class RockGnome(_Gnome):
    name = "Rock Gnome"
    constitution_bonus = 1
    features = _Gnome.features + (feats.ArtificersLore,
                                  feats.Tinker)


class DeepGnome(_Gnome):
    name = "Deep Gnome"
    dexterity_bonus = 1
    languages = ("Common", "Gnomish", "Undercommon")
    features = (feats.SuperiorDarkvision, feats.GnomeCunning,
                feats.StoneCamouflage)


# Half-elves
class HalfElf(Race):
    name = "Half-Elf"
    size = "medium"
    speed = 30
    charisma_bonus = 2
    skill_choices = ('acrobatics', 'animal handling', 'arcana',
                     'athletics', 'deception', 'history', 'insight',
                     'intimidation', 'investigation', 'medicine', 'nature',
                     'perception', 'performance', 'persuasion', 'religion',
                     'sleight of hand', 'stealth', 'survival')
    num_skill_choices = 2
    languages = ("Common", "Elvish", "[choose one]")
    features = (feats.Darkvision, feats.FeyAncestry)


# Half-Orcs
class HalfOrc(Race):
    name = "Half-Orc"
    size = "medium"
    speed = 30
    strength_bonus = 2
    constitution_bonus = 1
    skill_proficiencies = ('intimidation',)
    languages = ("Common", "Orc")
    features = (feats.Darkvision, feats.RelentlessEndurance,
                feats.SavageAttacks)


# Tielflings
class Tiefling(Race):
    name = "Tiefling"
    size = "medium"
    speed = 30
    intelligence_bonus = 1
    charisma_bonus = 2
    languages = ("Common", "Infernal")
    features = (feats.Darkvision, feats.HellishResistance,
                feats.InfernalLegacy)


# Aassimar
class _Aasimar(Race):
    name = 'Aasimar'
    size = 'medium'
    speed = 30
    charisma_bonus = 2
    languages = ("Common", "Celestial")
    features = (feats.Darkvision, feats.CelestialResistance,
                feats.HealingHands, feats.LightBearer)
    spells_known = (spells.Light,)


# Protector Aasimar
class ProtectorAasimar(_Aasimar):
    name = "Protector Aasimar"
    wisdom_bonus = 1
    features_by_level = defaultdict(list)
    features_by_level[3] += [feats.RadiantSoul]


# Fallen Aasimar
class ScourgeAasimar(_Aasimar):
    name = "Scourge Aasimar"
    constitution_bonus = 1
    features_by_level = defaultdict(list)
    features_by_level[3] += [feats.RadiantConsumption]


# Fallen Aasimar
class FallenAasimar(_Aasimar):
    name = "Fallen Aasimar"
    strength_bonus = 1
    features_by_level = defaultdict(list)
    features_by_level[3] += [feats.NecroticShroud]


# Firbolg
class Firbolg(Race):
    name = "Firbolg"
    size = "medium"
    speed = 30
    wisdom_bonus = 2
    strength_bonus = 1
    features = (feats.FirbolgMagic, feats.HiddenStep,
                feats.PowerfulBuild, feats.SpeechOfBeastAndLeaf)
    languages = ("Common", "Elvish", "Giant")


# Goliath
class Goliath(Race):
    name = "Goliath"
    size = "Medium"
    speed = 30
    skill_proficiencies = ("athletics",)
    languages = ("Common", "Giant")
    features = (feats.StonesEndurance, feats.PowerfulBuild,
                feats.MountainBorn)


# Lizardfolk
class Lizardfolk(Race):
    name = 'Lizardfolk'
    size = 'medium'
    speed = """30 (30 swim)"""
    constitution_bonus = 2
    wisdom_bonus = 1
    languages = ('Common', 'Draconic')
    weapon_proficiencies = (weapons.Bite,)
    proficiencies_text = ('bite',)
    features = (feats.CunningArtisan, feats.HoldBreath,
                feats.NaturalArmor, feats.HungryJaws)
    skill_choices = ('animal handling', 'nature', 'perception',
                     'stealth', 'survival')

    def __init__(self, owner=None):
        super().__init__(owner=owner)
        self.owner.wield_weapon("bite")


# Kenku
class Kenku(Race):
    name = 'Kenku'
    size = 'medium'
    speed = 30
    dexterity_bonus = 2
    wisdom_bonus = 1
    languages = ('Common', 'Auran')
    skill_choices = ('acrobatics', 'deception', 'stealth',
                     'sleight of hand')
    num_skill_choices = 2
    features = (feats.ExpertForgery, feats.Mimicry,)


# Tabaxi
class Tabaxi(Race):
    name = 'Tabaxi'
    size = 'medium'
    dexterity_bonus = 2
    charisma_bonus = 1
    speed = "30 (20 climb)"
    languages = ("Common", "[Choose One]")
    weapon_proficiencies = (weapons.Claws,)
    proficiences_text = ('Claws',)
    skill_proficiencies = ('perception', 'stealth')
    features = (feats.Darkvision, feats.FelineAgility,)

    def __init__(self, owner=None):
        super().__init__(owner=owner)
        self.owner.wield_weapon("claws")


# Triton
class Triton(Race):
    name = "Triton"
    size = "medium"
    strength_bonus = 1
    constitution_bonus = 1
    charisma_bonus = 1
    speed = "30 (30 swim)"
    features = (feats.Amphibious, feats.ControlAirAndWater,
                feats.EmissaryOfTheSea, feats.GuardiansOfTheDepths)
    languages = ("Common", "Primordial")
    spells_known = (spells.FogCloud,)


# Aarakocra
class Aarakocra(Race):
    name = 'Aarakocra'
    size = 'medium'
    speed = "25 (50 fly)"
    dexterity_bonus = 2
    wisdom_bonus = 1
    languages = ('Common', 'Aarakocra', 'Auran')
    weapon_proficiencies = (weapons.Talons,)
    proficiences_text = ('Talons',)

    def __init__(self, owner=None):
        super().__init__(owner=owner)
        self.owner.wield_weapon("talons")


# Genasi
class _Genasi(Race):
    name = "Genasi"
    constitution_bonus = 2
    size = 'medium'
    speed = 30
    languages = ("Common", 'Primoridal')


class AirGenasi(_Genasi):
    name = "Air Genasi"
    dexterity_bonus = 1
    features = (feats.UnendingBreath,
                feats.MingleWithTheWind)


class EarthGenasi(_Genasi):
    name = "Earth Genasi"
    strength_bonus = 1
    features = (feats.EarthWalk, feats.MergeWithStone)


class FireGenasi(_Genasi):
    name = "Fire Genasi"
    intelligence_bonus = 1
    features = (feats.Darkvision, feats.FireResistance,
                feats.ReachToTheBlaze)


class WaterGenasi(_Genasi):
    name = "Water Genasi"
    wisdom_bonus = 1
    speed = "30 (30 swim)"
    features = (feats.AcidResistance, feats.Amphibious,
                feats.CallToTheWave)

# Eberron Races
class Kalashtar(Race):
    name = "Kalashtar"
    wisdom_bonus = 2
    charisma_bonus = 1
    size = 'medium'
    speed = 30
    languages = ("Common", "Quori",) # Not sure how to have a "+1 language of your choice" - naviabbot
    features = (feats.DualMind, feats.MentalDiscipline, feats.MindLink, feats.SeveredFromDreams)

class BugBear(Race):
    name = "BugBear"
    strength_bonus = 2
    dexterity_bonus = 1
    size = 'medium'
    speed = 30
    features = (feats.Darkvision, feats.LongLimbed,
                feats.PowerfulBuild, feats.SupriseAttack)
    skill_proficiencies = ("stealth", )
    languages = ("Common", "Goblin")

class Goblin(Race):
    name = "Goblin"
    dexterity_bonus = 2
    constitution_bonus = 1
    size = 'small'
    speed = 30
    features = (feats.Darkvision, feats.FuryOfTheSmall,
                feats.NimbleEscape)
    languages = ("Common", "Goblin")

class HobGoblin(Race):
    name = "HobGoblin"
    constitution_bonus = 2
    intelligence_bonus = 1
    size = 'medium'
    speed = 30
    features = (feats.Darkvision, feats.SavingFace)
    proficiencies_text = ('light armor', '[Chose two martial melee weapons]')
    languages = ("Common", "Goblin")

class Kobold(Race):
    name = "Kobold"
    dexterity_bonus = 2
    strength_bonus = -2
    size = 'small'
    speed = 30
    features = (feats.Darkvision, feats.PackTactics,
                feats.GrovelCowerAndBeg, feats.SunlightSensitivity)
    languages = ("Common", "Draconic")

class Orc(Race):
    name = "Orc"
    strength_bonus = 2
    constitution_bonus = 1
    intelligence_bonus = -2
    size = 'medium'
    speed = 30
    skill_proficiencies = ('intimidation',)
    features = (feats.Darkvision, feats.Aggressive,
                feats.PowerfulBuild)
    languages = ("Common", "Orc")

class PureBlood(Race):
    name = "Yuan-Ti Pureblood"
    charisma_bonus = 2
    intelligence_bonus = 1
    size = 'medium'
    speed = 30
    features = (feats.Darkvision, feats.InnateSpellcasting,
                feats.MagicResistance, feats.PoisonImmunity)
    spells_known = (spells.PoisonSpray,)
    languages = ("Common", "Abyssal", "Draconic")


class Goblin(Race):
    name = "Goblin"
    size = "small"
    dexterity_bonus = 2
    constitution_bonus = 1
    speed = 30
    languages = ("Common", "Goblin")
    features = (feats.Darkvision, feats.FuryOfTheSmall, feats.NimbleEscape)


PHB_races = [HillDwarf, MountainDwarf, HighElf, WoodElf, DarkElf,
             LightfootHalfling, StoutHalfling, Rashemi, Dragonborn,
             ForestGnome, RockGnome, HalfElf, HalfOrc, Tiefling]

VOLO_races = [ProtectorAasimar, ScourgeAasimar, FallenAasimar,
              Firbolg, Goliath, Lizardfolk, Kenku, Tabaxi, Triton]

EE_races = [Aarakocra, DeepGnome, AirGenasi, FireGenasi, EarthGenasi,
            WaterGenasi]

MONSTER_races = [BugBear, Goblin, HobGoblin, Kobold, Orc, PureBlood]

RFTLW_races = [Kalashtar]

# Guildmaster's Guide to Ravnica
GGTR_races = [Goblin]

available_races = PHB_races + VOLO_races + EE_races + MONSTER_races + RFTLW_races + GGTR_races

__all__ = tuple([r.name for r in available_races]) + (
    'available_races', 'PHB_races', 'VOLO_races', 'EE_races', 'MONSTER_races', 'RFTLW_races', 'GGTR_races')
