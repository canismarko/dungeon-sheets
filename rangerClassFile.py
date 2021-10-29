__all__ = ("Ranger", "RevisedRanger", "BloodHunter")

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
    
    
#Blood Hunter
class OrderOfTheGhostslayer(SubClass):
    """The Order of the Ghostslayer is the oldest of the orders, having originally rediscovered the secrets of blood magic and refined them for combat against the scourge of undeath. Ghostslayers seek out and study the moment of death, obsessing over the mysteries of the transition and how it can become corrupted by unholy powers to rise once more. Tuning their abilities to annihilate such abominations, these zealous blood hunters seek out the sources of such necromantic energies, intent to destroy them wherever they arise.

    """

    name = "Order of the Ghostslayer"
    features_by_level = defaultdict(list)
    features_by_level[3] = [features.RiteOfTheDawn, features.CurseSpecialist]
    features_by_level[7] = [features.EtherealStep]
    features_by_level[11] = [features.BrandOfSundering]
    features_by_level[15] = [features.BloodCurseOfTheExorcist]
    features_by_level[18] = [features.RiteRevival]
    spellcasting_ability = "intelligence"
    spell_slots_by_level = {
        # char_lvl: (cantrips, 1st, 2nd, 3rd, ...)
        1: (0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
        2: (0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
        3: (0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
        4: (0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
        5: (0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
        6: (0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
        7: (0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
        8: (0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
        9: (0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
        10: (0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
        11: (0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
        12: (0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
        13: (0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
        14: (0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
        15: (0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
        16: (0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
        17: (0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
        18: (0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
        19: (0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
        20: (0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
    }

class OrderOfTheLycan(SubClass):
    """Of the many terrible curses that plague the realm, few are as ancient or as feared as Lycanthropy. Passed through blood, this affliction seeds a host with the savage strength and hunger for violence of a wicked beast. The Order of the Lycan is a proud order of blood hunters who undergo “The Taming,” a ceremonial inflicting of lycanthropy from a senior member. These hunters then use their abilities to harness the power of the monster they harbor without losing themselves to it. Through intense honing of one’s own willpower, combined with the secrets of the order’s blood magic rituals, members learn to control and unleash their hybrid form for short periods of time. Enhanced physical prowess, unnatural resilience, and razor sharp claws make these warriors a terrible foe to any evil that crosses their path. Yet, no training is perfect, and without care and complete focus, even the greatest of blood hunters can temporarily lose themselves to the bloodlust.

    """

    name = "Order of the Lycan"
    features_by_level = defaultdict(list)
    features_by_level[3] = [features.HeightenedSenses, features.HybridTransformation]
    features_by_level[7] = [features.StalkerProwess]
    features_by_level[11] = [features.AdvancedTrasformation]
    features_by_level[15] = [features.BrandOfTheVoracious]
    features_by_level[18] = [features.HybridTrasformationMastery]
    spellcasting_ability = "intelligence"
    spell_slots_by_level = {
        # char_lvl: (cantrips, 1st, 2nd, 3rd, ...)
        1: (0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
        2: (0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
        3: (0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
        4: (0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
        5: (0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
        6: (0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
        7: (0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
        8: (0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
        9: (0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
        10: (0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
        11: (0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
        12: (0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
        13: (0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
        14: (0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
        15: (0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
        16: (0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
        17: (0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
        18: (0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
        19: (0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
        20: (0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
    }    


class OrderOfTheMutant(SubClass):
    """The process of the Hunter’s Bane is a painful, scarring, and sometimes fatal experience. Those that survive find themselves irrevocably changed, enhanced. Some found this experience exalting, embracing the ability to alter one’s own physiology through a combination of hemocraft and corrupted alchemy. Over generations of experimentation, a splinter order of blood hunters began to emerge, one that focused on brewing toxic elixirs to modify their capabilities in battle, altering their blood and, over time, become something beyond what they once were. They called themselves the Order of the Mutant. Researching their targets to know their strengths and weaknesses, these blood hunters can alter their biology to be best prepared for the coming conflict.

    """

    name = "Order of the Mutant"
    features_by_level = defaultdict(list)
    features_by_level[3] = [features.Formulas, features.Mutagencraft]
    features_by_level[7] = [features.StrangeMetabolism]
    features_by_level[11] = [features.BrandOfAxiom]
    features_by_level[15] = [features.BloodCurseOfCorrosion]
    features_by_level[18] = [features.ExaltedMutation]
    spellcasting_ability = "intelligence"
    spell_slots_by_level = {
        # char_lvl: (cantrips, 1st, 2nd, 3rd, ...)
        1: (0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
        2: (0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
        3: (0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
        4: (0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
        5: (0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
        6: (0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
        7: (0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
        8: (0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
        9: (0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
        10: (0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
        11: (0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
        12: (0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
        13: (0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
        14: (0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
        15: (0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
        16: (0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
        17: (0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
        18: (0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
        19: (0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
        20: (0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
    }


class OrderOfTheProfaneSoul(SubClass):
    """Those who have taken to the Order of the Profane Soul have seen the limits of hemocraft against some of the most ancient and cruel fiends and terrors of the world. Unable to pursue beings of such power, creatures able to vanish amongst the nobles without a trace, or bend the mind of the most stalwart warrior with but a glance, this order trusted in their resilience and delved into this same well of corrupting arcane knowledge, making pacts with lesser evils to better combat the greater. While they may have traded a part of themselves, members of this order believe the power gained far outweighs the price, for even devils now quake when they know they’ve drawn the attention of the Order of the Profane Soul.

    """

    name = "Order of the Profane Soul"
    features_by_level = defaultdict(list)
    features_by_level[3] = [features.OtherworldlyPatron, features.PactMagic, features.RiteFocus]
    features_by_level[7] = [features.MysticFrenzy,
features.RevealedArcana]
    features_by_level[11] = [features.BrandOfTheSappingScar]
    features_by_level[15] = [features.UnsealedArcana]
    features_by_level[18] = [features.BloodCurseOfTheSouleater]
    spellcasting_ability = "intelligence"
    spell_slots_by_level = {
        # char_lvl: (cantrips, 1st, 2nd, 3rd, ...)
        1: (0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
        2: (0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
        3: (2, 1, 0, 0, 0, 0, 0, 0, 0, 0),
        4: (2, 1, 0, 0, 0, 0, 0, 0, 0, 0),
        5: (2, 1, 0, 0, 0, 0, 0, 0, 0, 0),
        6: (2, 2, 0, 0, 0, 0, 0, 0, 0, 0),
        7: (2, 0, 2, 0, 0, 0, 0, 0, 0, 0),
        8: (2, 0, 2, 0, 0, 0, 0, 0, 0, 0),
        9: (2, 0, 2, 0, 0, 0, 0, 0, 0, 0),
        10: (3, 0, 2, 0, 0, 0, 0, 0, 0, 0),
        11: (3, 0, 2, 0, 0, 0, 0, 0, 0, 0),
        12: (3, 0, 2, 0, 0, 0, 0, 0, 0, 0),
        13: (3, 0, 0, 2, 0, 0, 0, 0, 0, 0),
        14: (3, 0, 0, 2, 0, 0, 0, 0, 0, 0),
        15: (3, 0, 0, 2, 0, 0, 0, 0, 0, 0),
        16: (3, 0, 0, 2, 0, 0, 0, 0, 0, 0),
        17: (3, 0, 0, 2, 0, 0, 0, 0, 0, 0),
        18: (3, 0, 0, 2, 0, 0, 0, 0, 0, 0),
        19: (3, 0, 0, 0, 2, 0, 0, 0, 0, 0),
        20: (3, 0, 0, 0, 2, 0, 0, 0, 0, 0),
    }    


class BloodHunter(Ranger):
    name = "Blood Hunter"
    hit_dice_faces = 10
    subclass_select_level = 3
    subclasses_available = (OrderOfTheGhostslayer, OrderOfTheLycan, OrderOfTheMutant, OrderOfTheProfaneSoul)
    saving_throw_proficiencies = ("intelligence", "dexterity")
    primary_abilities = ("dexterity",)
    _proficiencies_text = (
        "Light armor",
        "Medium armor",
        "Shields",
	"Simple Weapons",
	"Martial Weapons",
    )
    weapon_proficiencies = (weapons.SimpleWeapon, weapons.MartialWeapon)
    multiclass_weapon_proficiencies = ()
    _multiclass_proficiencies_text = ()
    class_skill_choices = ("Athletics", "Acrobatics", "Arcana", "History", "insight", "Investigation", "Religion", "Survival",)
    features_by_level = defaultdict(list)
    features_by_level[1] = [
    	features.HunterBane,
    	features.BloodMaledict,
    	]
    
    features_by_level[2] = [
    	features.CrimsonRites,
    	features.BloodHunterFightingStyle,
    	]
    features_by_level[5] = [features.ExtraAttackBloodHunter]
    features_by_level[6] = [features.BrandOfCastigation]
    features_by_level[9] = [features.GrimPsychometry]
    features_by_level[10] = [features.DarkAugmentation]
    features_by_level[13] = [features.BrandOfTethering]
    features_by_level[14] = [features.HardenedSoul]
    features_by_level[20] = [features.SanguineMastery]
    subclasses_available = (
        OrderOfTheGhostslayer,
        OrderOfTheProfaneSoul,
        OrderOfTheMutant,
        OrderOfTheLycan,
    )
    spellcasting_ability = "intelligence"
    spell_slots_by_level = {
        # char_lvl: (cantrips, 1st, 2nd, 3rd, ...)
        1: (0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
        2: (0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
        3: (0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
        4: (0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
        5: (0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
        6: (0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
        7: (0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
        8: (0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
        9: (0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
        10: (0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
        11: (0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
        12: (0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
        13: (0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
        14: (0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
        15: (0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
        16: (0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
        17: (0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
        18: (0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
        19: (0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
        20: (0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
    }
