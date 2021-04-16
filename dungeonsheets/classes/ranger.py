__all__ = ("Ranger", "RevisedRanger")

from collections import defaultdict

from dungeonsheets import features, spells, weapons
from dungeonsheets.classes.classes import CharClass, SubClass


# PHB
class Hunter(SubClass):
    """Emulating the Hunter archetype means accepting your place as a bulwark
    between civilization and the terrors of the wilderness. As you walk the
    Hunter's path, you learn specialized techniques for fighting the threats
    you face, from rampaging ogres and hordes of orcs to towering giants and
    terrifying dragons.

    """

    name = "Hunter"
    features_by_level = defaultdict(list)
    features_by_level[3] = [features.HuntersPrey]
    features_by_level[7] = [features.DefensiveTactics]
    features_by_level[11] = [features.MultiattackRanger]
    features_by_level[15] = [features.SuperiorHuntersDefense]


class BeastMaster(SubClass):
    """The Beast Master archetype embodies a friendship between the civilized
    races and the beasts of the world. United in focus, beast and ranger work
    as one to fight the monstrous foes that threaten civilization and the
    wilderness alike. Emulating the Beast Master archetype means committing
    yourself to this ideal, working in partnership with an animal as its
    companion and friend.

    """

    name = "Beast Master"
    features_by_level = defaultdict(list)
    features_by_level[3] = [features.RangersCompanion]
    features_by_level[7] = [features.ExceptionalTraining]
    features_by_level[11] = [features.BestialFury]
    features_by_level[15] = [features.ShareSpells]


# XGTE
class GloomStalker(SubClass):
    """Gloom Stalkers are at home in the darkest places: deep under the earth, in
    gloomy alleyways, in primeval forests, and wherever else the light
    dims. Most folk enter such places with trepidation, but a Gloom Stalker
    ventures boldly into the darkness, seeking to ambush threats before they
    can reach the broader world. Such rangers are often found in the Underdark,
    but they will go any place Where evil lurks in the shadows

    """

    name = "Gloom Stalker"
    features_by_level = defaultdict(list)
    _spells = {
        3: [spells.DisguiseSelf],
        5: [spells.RopeTrick],
        9: [spells.Fear],
        13: [spells.GreaterInvisibility],
        17: [spells.Seeming],
    }
    features_by_level[3] = [
        features.DreadAmbusher,
        features.UmbralSight,
        features.Darkvision,
    ]
    features_by_level[7] = [features.IronMind]
    features_by_level[11] = [features.StalkersFlurry]
    features_by_level[15] = [features.ShadowyDodge]

    @property
    def level(self):
        return self.owner.Ranger.level

    @property
    def spells_known(self):
        spells = []
        for lvl, sps in self._spells.items():
            if self.level >= lvl:
                spells.extend(sps)
        return spells

    @property
    def spells_prepared(self):
        return self.spells_known


class HorizonWalker(SubClass):
    """Horizon Walkers guard the world against threats that originate from other
    planes or that seek to ravage the mortal realm with otherworldly
    magic. They seek out planar portals and keep watch over them, venturing to
    the Inner Planes and the Outer Planes as needed to pursue their foes. These
    rangers are also friends to any forces in the multiverse-especially
    benevolent dragons, fey, and elementals-that work to preserve life and the
    order of the planes

    """

    name = "Horizon Walker"
    _spells = {
        3: [spells.ProtectionFromEvilAndGood],
        5: [spells.MistyStep],
        9: [spells.Haste],
        13: [spells.Banishment],
        17: [spells.TeleportationCircle],
    }
    features_by_level = defaultdict(list)
    features_by_level[3] = [features.DetectPortal, features.PlanarWarrior]
    features_by_level[7] = [features.EtherealStep]
    features_by_level[11] = [features.DistantStrike]
    features_by_level[15] = [features.SpectralDefense]

    @property
    def level(self):
        return self.owner.Ranger.level

    @property
    def spells_known(self):
        spells = []
        for lvl, sps in self._spells.items():
            if self.level >= lvl:
                spells.extend(sps)
        return spells

    @property
    def spells_prepared(self):
        return self.spells_known


class MonsterSlayer(SubClass):
    """You have dedicated yourself to hunting down creatures of the night and
    wielders of grim magic. A Monster Slayer seeks out vampires, dragons, evil
    fey, fiends, and other magical threats. Trained in supernatural techniques
    to overcome such monsters, Slayers are experts at unearthing and defeating
    mighty, mystical foes.

    """

    name = "Monster Slayer"
    features_by_level = defaultdict(list)
    features_by_level[3] = [features.HuntersSense, features.SlayersPrey]
    features_by_level[7] = [features.SupernaturalDefense]
    features_by_level[11] = [features.MagicUsersNemesis]
    features_by_level[15] = [features.SlayersCounter]
    _spells = {
        3: [spells.ProtectionFromEvilAndGood],
        5: [spells.ZoneOfTruth],
        9: [spells.MagicCircle],
        13: [spells.Banishment],
        17: [spells.HoldMonster],
    }

    @property
    def level(self):
        return self.owner.Ranger.level

    @property
    def spells_known(self):
        spells = []
        for lvl, sps in self._spells.items():
            if self.level >= lvl:
                spells.extend(sps)
        return spells

    @property
    def spells_prepared(self):
        return self.spells_known


class Ranger(CharClass):
    name = "Ranger"
    hit_dice_faces = 10
    saving_throw_proficiencies = ("strength", "dexterity")
    primary_abilities = ("dexterity", "wisdom")
    _proficiencies_text = (
        "light armor",
        "medium armor",
        "shields",
        "simple weapons",
        "martial weapons",
    )
    weapon_proficiencies = (weapons.SimpleWeapon, weapons.MartialWeapon)
    multiclass_weapon_proficiencies = weapon_proficiencies
    _multiclass_proficiencies_text = (
        "light armor",
        "medium armor",
        "shields",
        "simple weapons",
        "martial weapons",
        "[choose one skill from Ranger list]",
    )
    class_skill_choices = (
        "Animal Handling",
        "Athletics",
        "Insight",
        "Investigation",
        "Nature",
        "Perception",
        "Stealth",
        "Survival",
    )
    num_skill_choices = 3
    features_by_level = defaultdict(list)
    features_by_level[1] = [features.FavoredEnemy, features.NaturalExplorer]
    features_by_level[2] = [features.RangerFightingStyle]
    features_by_level[3] = [features.PrimevalAwareness]
    features_by_level[5] = [features.ExtraAttackRanger]
    features_by_level[8] = [features.LandsStride]
    features_by_level[10] = [features.HideInPlainSight]
    features_by_level[14] = [features.Vanish]
    features_by_level[18] = [features.FeralSenses]
    features_by_level[20] = [features.FoeSlayer]
    subclasses_available = (
        Hunter,
        BeastMaster,
        GloomStalker,
        HorizonWalker,
        MonsterSlayer,
    )
    spellcasting_ability = "wisdom"
    spell_slots_by_level = {
        # char_lvl: (cantrips, 1st, 2nd, 3rd, ...)
        1: (0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
        2: (0, 2, 0, 0, 0, 0, 0, 0, 0, 0),
        3: (0, 3, 0, 0, 0, 0, 0, 0, 0, 0),
        4: (0, 3, 0, 0, 0, 0, 0, 0, 0, 0),
        5: (0, 4, 2, 0, 0, 0, 0, 0, 0, 0),
        6: (0, 4, 2, 0, 0, 0, 0, 0, 0, 0),
        7: (0, 4, 3, 0, 0, 0, 0, 0, 0, 0),
        8: (0, 4, 3, 0, 0, 0, 0, 0, 0, 0),
        9: (0, 4, 3, 2, 0, 0, 0, 0, 0, 0),
        10: (0, 4, 3, 2, 0, 0, 0, 0, 0, 0),
        11: (0, 4, 3, 3, 0, 0, 0, 0, 0, 0),
        12: (0, 4, 3, 3, 0, 0, 0, 0, 0, 0),
        13: (0, 4, 3, 3, 1, 0, 0, 0, 0, 0),
        14: (0, 4, 3, 3, 1, 0, 0, 0, 0, 0),
        15: (0, 4, 3, 3, 2, 0, 0, 0, 0, 0),
        16: (0, 4, 3, 3, 2, 0, 0, 0, 0, 0),
        17: (0, 4, 3, 3, 3, 1, 0, 0, 0, 0),
        18: (0, 4, 3, 3, 3, 1, 0, 0, 0, 0),
        19: (0, 4, 3, 3, 3, 2, 0, 0, 0, 0),
        20: (0, 4, 3, 3, 3, 2, 0, 0, 0, 0),
    }


# Revised Ranger
class BeastConclave(SubClass):
    """Many rangers are more at home in the wilds than in civilization, to the
    point where animals consider them kin. Rangers of the Beast Conclave
    develop a close bond with a beast, then further strengthen that bond
    through the use of magic.

    """

    name = "Beast Conclave"
    features_by_level = defaultdict(list)
    features_by_level[3] = [features.AnimalCompanion, features.CompanionsBond]
    features_by_level[5] = [features.CoordinatedAttack]
    features_by_level[7] = [features.BeastsDefense]
    features_by_level[11] = [features.StormOfClawsAndFangs]
    features_by_level[15] = [features.SuperiorBeastsDefense]


class HunterConclave(SubClass):
    """Some rangers seek to master weapons to better protect civilization from the
    terrors of the wilderness. Members of the Hunter Conclave learn specialized
    fighting techniques for use against the most dire threats, from rampaging
    ogres and hordes of orcs to towering giants and terrifying dragons

    """

    name = "Hunter Conclave"
    features_by_level = defaultdict(list)
    features_by_level = defaultdict(list)
    features_by_level[3] = [features.HuntersPrey]
    features_by_level[5] = [features.ExtraAttackRanger]
    features_by_level[7] = [features.DefensiveTactics]
    features_by_level[11] = [features.MultiattackRanger]
    features_by_level[15] = [features.SuperiorHuntersDefense]


class DeepStalkerConclave(SubClass):
    """Most folk descend into the depths of the Underdark only under the most
    pressing conditions, undertaking some desperate quest or following the
    promise of vast riches. All too often, evil festers beneath the earth
    unnoticed, and rangers of the Deep Stalker Conclave strive to uncover and
    defeat such threats before they can reach the surface.

    """

    name = "Deep Stalker Conclave"
    features_by_level = defaultdict(list)
    features_by_level[3] = [features.UnderdarkScout]
    features_by_level[5] = [features.ExtraAttackRanger]
    features_by_level[7] = [features.IronMind]
    features_by_level[11] = [features.StalkersFlurry]
    features_by_level[15] = [features.StalkersDodge]
    _spells = {
        3: [spells.DisguiseSelf],
        5: [spells.RopeTrick],
        9: [spells.GlyphOfWarding],
        13: [spells.GreaterInvisibility],
        17: [spells.Seeming],
    }

    @property
    def spells_prepared(self):
        level = self.owner.Ranger.level
        my_spells = []
        for lvl, sps in self._spells.items():
            if level >= lvl:
                my_spells.extend(sps)
        return my_spells

    @property
    def spells_known(self):
        return self.spells_prepared


class RevisedRanger(Ranger):
    name = "Revised Ranger"
    features_by_level = defaultdict(list)
    features_by_level[1] = [
        features.FavoredEnemyRevised,
        features.NaturalExplorerRevised,
    ]
    features_by_level[2] = [features.RangerFightingStyle]
    features_by_level[3] = [features.PrimevalAwarenessRevised]
    features_by_level[6] = [features.GreaterFavoredEnemy]
    features_by_level[8] = [features.FleetOfFoot]
    features_by_level[10] = [features.HideInPlainSightRevised]
    features_by_level[14] = [features.Vanish]
    features_by_level[18] = [features.FeralSenses]
    features_by_level[20] = [features.FoeSlayer]
    subclasses_available = (BeastConclave, HunterConclave, DeepStalkerConclave)
