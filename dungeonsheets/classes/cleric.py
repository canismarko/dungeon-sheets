from .. import (weapons, features, spells)
from .classes import CharClass, SubClass
from collections import defaultdict


class ClericDomain(SubClass):
    name = "Generic Cleric Domain"
    _domain_spells = {1: [], 3: [], 5: [], 7: [], 9: []}

    @property
    def level(self):
        return self.owner.Cleric.level

    @property
    def spells_known(self):
        spells = []
        for lvl, sps in self._domain_spells.items():
            if self.level >= lvl:
                spells.extend(sps)
        return spells
    
    # All Domain spells are both known and prepared
    @property
    def spells_prepared(self):
        return self.spells_known


class KnowledgeDomain(ClericDomain):
    """The gods of knowledge—including Oghma, Boccob, Gilean, Aureon, and
    Thoth—value learning and understanding above all. Some teach that knowledge
    is to be gathered and shared in libraries and universities, or promote the
    practical knowledge of craft and invention. Some deities hoard knowledge
    and keep its secrets to themselves. And some promise their followers that
    they will gain tremendous power if they unlock the secrets of the
    multiverse. Followers of these gods study esoteric lore, collect old tomes,
    delve into the secret places of the earth, and learn all they can. Some
    gods of knowledge promote the practical knowledge of craft and invention,
    including smith deities like Gond, Reorx, Onatar, Moradin, Hephaestus, and
    Goibhniu.

    """
    name = "Knowledge Domain"
    _domain_spells = {1: [spells.Command, spells.Identify],
                      3: [spells.Augury, spells.Suggestion],
                      5: [spells.Nondetection, spells.SpeakWithDead],
                      7: [spells.ArcaneEye, spells.Confusion],
                      9: [spells.LegendLore, spells.Scrying]}
    features_by_level = defaultdict(list)
    features_by_level[1] = [features.BlessingsOfKnowledge]
    features_by_level[2] = [features.KnowledgeOfTheAncients]
    features_by_level[6] = [features.ReadThoughts]
    features_by_level[8] = [features.PotentSpellcasting]
    features_by_level[17] = [features.VisionsOfThePast]


class LifeDomain(ClericDomain):
    """The Life domain focuses on the vibrant positive energy—one of the
    fundamental forces of the universe— that sustains all life. The gods of
    life promote vitality and health through healing the sick and wounded,
    caring for those in need, and driving away the forces of death and
    undeath. Almost any non-evil deity can claim influence over this domain,
    particularly agricultural deities (such as Chauntea, Arawai, and Demeter),
    sun gods (such as Lathander, Pelor, and Re-Horakhty), gods of healing or
    endurance (such as Ilmater, Mishakal, Apollo, and Diancecht), and gods of
    home and community (such as Hestia, Hathor, and Boldrei).

    """
    name = "Life Domain"
    _domain_spells = {1: [spells.Bless, spells.CureWounds],
                      3: [spells.LesserRestoration, spells.SpiritualWeapon],
                      5: [spells.BeaconOfHope, spells.Revivify],
                      7: [spells.DeathWard, spells.GuardianOfFaith],
                      9: [spells.MassCureWounds, spells.RaiseDead]}
    _proficiencies_text = ('heavy armor',)
    features_by_level = defaultdict(list)
    features_by_level[1] = [features.DiscipleOfLife]
    features_by_level[2] = [features.PreserveLife]
    features_by_level[6] = [features.BlessedHealer]
    features_by_level[8] = [features.DivineStrikeLife]
    features_by_level[17] = [features.SupremeHealing]


class LightDomain(ClericDomain):
    """Gods of light—including Helm, Lathander, Pholtus, Branchala, the Silver
    Flame, Belenus, Apollo, and Re-Horakhty—promote the ideals of rebirth and
    renewal, truth, vigilance, and beauty, often using the symbol of the
    sun. Some of these gods are portrayed as the sun itself or as a charioteer
    who guides the sun across the sky. Others are tireless sentinels whose eyes
    pierce every shadow and see through every deception. Some are deities of
    beauty and artistry, who teach that art is a vehicle for the soul's
    improvement. Clerics of a god of light are enlightened souls infused with
    radiance and the power of their gods’ discerning vision, charged with
    chasing away lies and burning away darkness.

    """
    name = "Light Domain"
    _domain_spells = {1: [spells.BurningHands, spells.FaerieFire],
                      3: [spells.FlamingSphere, spells.ScorchingRay],
                      5: [spells.Daylight, spells.Fireball],
                      7: [spells.GuardianOfFaith, spells.WallOfFire],
                      9: [spells.FlameStrike, spells.Scrying]}
    spells_known = (spells.Light,)
    spells_prepared = (spells.Light,)
    features_by_level = defaultdict(list)
    features_by_level[1] = [features.WardingFlare]
    features_by_level[2] = [features.RadianceOfTheDawn]
    features_by_level[6] = [features.ImprovedFlare]
    features_by_level[8] = [features.PotentSpellcasting]
    features_by_level[17] = [features.CoronaOfLight]


class NatureDomain(ClericDomain):
    """Gods of nature are as varied as the natural world itself, from inscrutable
    gods of the deep forests (such as Silvanus, Obad-Hai, Chislev, Balinor, and
    Pan) to friendly deities associated with particular springs and groves
    (such as Eldath). Druids revere nature as a whole and might serve one of
    these deities, practicing mysterious rites and reciting all-but-forgotten
    prayers in their own secret tongue. But many of these gods have clerics as
    well, champions who take a more active role in advancing the interests of
    a particular nature god. These clerics might hunt the evil monstrosities
    that despoil the woodlands, bless the harvest of the faithful, or wither
    the crops of those who anger their gods.

    """
    name = "Nature Domain"
    _domain_spells = {1: [spells.AnimalFriendship, spells.SpeakWithAnimals],
                      3: [spells.Barkskin, spells.SpikeGrowth],
                      5: [spells.PlantGrowth, spells.WindWall],
                      7: [spells.DominateBeast, spells.GraspingVine],
                      9: [spells.InsectPlague, spells.TreeStride]}
    _proficiencies_text = ('heavy armor',)
    features_by_level = defaultdict(list)
    features_by_level[1] = [features.AcolyteOfNature]
    features_by_level[2] = [features.CharmAnimalsAndPlants]
    features_by_level[6] = [features.DampenElements]
    features_by_level[8] = [features.DivineStrikeNature]
    features_by_level[17] = [features.MasterOfNature]


class TempestDomain(ClericDomain):
    """Gods whose portfolios include the Tempest domain - including Talos,
    Umberlee, Kord, Zeboim, the Devourer, Zeus, and Thor — govern storms, sea,
    and sky. They include gods of lightning and thunder, gods of earthquakes,
    some fire gods, and certain gods of violence, physical strength, and
    courage. In some pantheons, a god of this domain rules over other deities
    and is known for swift justice delivered by thunderbolts. In the pantheons
    of seafaring people, gods of this domain are ocean deities and the patrons
    of sailors. Tempest gods send their clerics to inspire fear in the common
    folk, either to keep those folk on the path of righteousness or to
    encourage them to offer sacrifices of propitiation to ward off divine
    wrath.

    """
    name = "Tempest Domain"
    _domain_spells = {1: [spells.FogCloud, spells.Thunderwave],
                      3: [spells.GustOfWind, spells.Shatter],
                      5: [spells.CallLightning, spells.SleetStorm],
                      7: [spells.ControlWater, spells.IceStorm],
                      9: [spells.DestructiveWave, spells.InsectPlague]}
    weapon_proficiencies = (weapons.MartialWeapon,)
    _proficiencies_text = ('martial weapons', 'heavy armor')
    features_by_level = defaultdict(list)
    features_by_level[1] = [features.WrathOfTheStorm]
    features_by_level[2] = [features.DestructiveWrath]
    features_by_level[6] = [features.ThunderboltStrike]
    features_by_level[8] = [features.DivineStrikeTempest]
    features_by_level[17] = [features.Stormborn]


class TrickeryDomain(ClericDomain):
    """Gods of trickery—such as Tymora, Beshaba, Olidammara, the Traveler, Garl
    Glittergold, and Loki—are mischief-makers and instigators who stand as a
    constant challenge to the accepted order among both gods and
    mortals. They’re patrons of thieves, scoundrels, gamblers, rebels, and
    liberators. Their clerics are a disruptive force in the world, puncturing
    pride, mocking tyrants, stealing from the rich, freeing captives, and
    flouting hollow traditions. They prefer subterfuge, pranks, deception, and
    theft rather than direct confrontation.

    """
    name = "Trickery Domain"
    _domain_spells = {1: [spells.CharmPerson, spells.DisguiseSelf],
                      3: [spells.MirrorImage, spells.PassWithoutTrace],
                      5: [spells.Blink, spells.DispelMagic],
                      7: [spells.DimensionDoor, spells.Polymorph],
                      9: [spells.DominatePerson, spells.ModifyMemory]}
    features_by_level = defaultdict(list)
    features_by_level[1] = [features.BlessingOfTheTrickster]
    features_by_level[2] = [features.InvokeDuplicity]
    features_by_level[6] = [features.CloakOfShadows]
    features_by_level[8] = [features.DivineStrikeTrickery]
    features_by_level[17] = [features.ImprovedDuplicity]


class WarDomain(ClericDomain):
    """War has many manifestations. It can make heroes of ordinary people. It can
    be desperate and horrific, with acts of cruelty and cowardice eclipsing
    instances of excellence and courage. In either case, the gods of war watch
    over warriors and reward them for their great deeds. The clerics of such
    gods excel in battle, inspiring others to fight the good fight or offering
    acts of violence as prayers. Gods of war include champions of honor and
    chivalry (such as Torm, Heironeous, and KiriJolith) as well as gods of
    destruction and pillage (such as Erythnul, the Fury, Gruumsh, and Ares) and
    gods of conquest and domination (such as Bane, Hextor, and
    Maglubiyet). Other war gods (such as Tempus, Nike, and Nuada) take a more
    neutral stance, promoting war in all its manifestations and supporting
    warriors in any circumstance.

    """
    name = "War Domain"
    _domain_spells = {1: [spells.DivineFavor, spells.ShieldOfFaith],
                      3: [spells.MagicWeapon, spells.SpiritualWeapon],
                      5: [spells.CrusadersMantle, spells.SpiritGuardians],
                      7: [spells.FreedomOfMovement, spells.Stoneskin],
                      9: [spells.FlameStrike, spells.HoldMonster]}
    weapon_proficiencies = (weapons.MartialWeapon,)
    _proficiencies_text = ('martial weapons', 'heavy armor')
    features_by_level = defaultdict(list)
    features_by_level[1] = [features.WarPriest]
    features_by_level[2] = [features.GuidedStrike]
    features_by_level[6] = [features.WarGodsBlessing]
    features_by_level[8] = [features.DivineStrikeWar]
    features_by_level[17] = [features.AvatarOfBattle]


# SCAG
class ArcanaDomain(ClericDomain):
    """Magic is an energy that suffuses the multiverse and that fuels both
    destruction and creation. Gods of the Arcana domain know the secrets and
    potential of magic intimately. For some of these gods, magical knowledge
    is a great responsibility that comes with a special understanding of the
    nature of reality. Other gods of Arcana see magic as pure power, to be used
    as its wielder sees fit.

    The gods of this domain are often associated with knowledge, as learning
    and arcane power tend to go hand-in-hand. In the Realms, deities of this
    domain include Azuth and Mystra, as well as Corellon Larethian of the
    elven pantheon. In other worlds, this domain includes Hecate, Math
    Mathonwy, and Isis; the triple moon gods of Solinari , Lunitari, and
    Nuitari of Krynn; and Boccob, Vecna, and WeeJas of Greyhawk.

    """
    name = "Arcana Domain"
    _domain_spells = {1: [spells.DetectMagic, spells.MagicMissile],
                      3: [spells.MagicWeapon, spells.NystulsMagicAura],
                      5: [spells.DispelMagic, spells.MagicCircle],
                      7: [spells.ArcaneEye, spells.LeomundsSecretChest],
                      9: [spells.PlanarBinding, spells.TeleportationCircle]}
    features_by_level = defaultdict(list)
    features_by_level[1] = [features.ArcaneInitiate]
    features_by_level[2] = [features.ArcaneAbjuration]
    features_by_level[6] = [features.SpellBreaker]
    features_by_level[8] = [features.PotentSpellcasting]
    features_by_level[17] = [features.ArcaneMastery]


# XGTE
class ForgeDomain(ClericDomain):
    """The gods of the forge are patrons of artisans who work with metal, from a
    humble blacksmith who keeps a village in horseshoes and plow blades to the
    mighty elf artisan whose diamond-tipped arrows of mithral have felled demon
    lords. The gods of the forge teach that, with patience and hard work, even
    the most intractable metal can be transformed from a lump of ore to a beau—
    tifully wrought object. Clerics of these deities search for objects lost to
    the forces of darkness, liberate mines overrun by ores, and uncover rare
    and wondrous materials necessary to create potent magic items. Followers
    of these gods take great pride in their work, and they are willing to craft
    and use heavy armor and powerful weapons to protect them. Deities of this
    domain include Gond, Reorx, Onatar, Moradin, Hephaestus, and Goibhniu.

    """
    name = "Forge Domain"
    _domain_spells = {1: [spells.Identify, spells.SearingSmite],
                      3: [spells.HeatMetal, spells.MagicWeapon],
                      5: [spells.ElementalWeapon, spells.ProtectionFromEnergy],
                      7: [spells.Fabricate, spells.WallOfFire],
                      9: [spells.AnimateObjects, spells.Creation]}
    _proficiencies_text = ('heavy armor', "smith's tools")
    features_by_level = defaultdict(list)
    features_by_level[1] = [features.BlessingOfTheForge]
    features_by_level[2] = [features.ArtisansBlessing]
    features_by_level[6] = [features.SoulOfTheForge]
    features_by_level[8] = [features.DivineStrikeForge]
    features_by_level[17] = [features.SaintOfForgeAndFire]


class GraveDomain(ClericDomain):
    """Gods of the grave watch over the line between life and death. To these
    deities, death and the afterlife are a foundational part of the
    multiverse. To desecrate the peace of the dead is an abomination. Deities
    of the grave include Kelemvor, Wee jas, the ancestral spirits of the
    Undying Court, Hades, Anubis, and Osiris. Followers of these deities seek
    to put wandering spirits to rest, destroy the undead, and ease the
    suffering of the dying. Their magic also allows them to stave off death for
    a time. particularly for a person who still has some great work to
    accomplish in the world. This is a delay of death, not a denial of it, for
    death will eventually get its due.

    """
    name = "Grave Domain"
    _domain_spells = {1: [spells.Bane, spells.FalseLife],
                      3: [spells.GentleRepose, spells.RayOfEnfeeblement],
                      5: [spells.Revivify, spells.VampiricTouch],
                      7: [spells.Blight, spells.DeathWard],
                      9: [spells.AntilifeShell, spells.RaiseDead]}
    features_by_level = defaultdict(list)
    features_by_level[1] = [features.CircleOfMortality,
                            features.EyesOfTheGrave]
    features_by_level[2] = [features.PathToTheGrave]
    features_by_level[6] = [features.SentinelAtDeathsDoor]
    features_by_level[8] = [features.PotentSpellcasting]
    features_by_level[17] = [features.KeeperOfSouls]


class Cleric(CharClass):
    name = 'Cleric'
    hit_dice_faces = 8
    subclass_select_level = 1
    saving_throw_proficiencies = ('wisdom', 'charisma')
    primary_abilities = ('wisdom',)
    _proficiencies_text = ('light armor', 'medium armor', 'shields',
                           'all simple weapons')
    weapon_proficiencies = (weapons.SimpleWeapon,)
    multiclass_weapon_proficiencies = ()
    _multiclass_proficiencies_text = ('light armor', 'medium armor', 'shields')
    class_skill_choices = ('History', 'Insight', 'Medicine',
                           'Persuasion', 'Religion')
    features_by_level = defaultdict(list)
    features_by_level[2] = (features.ChannelDivinity, features.TurnUndead,)
    features_by_level[5] = (features.DestroyUndead, )
    features_by_level[10] = (features.DivineIntervention,)
    subclasses_available = (KnowledgeDomain, LifeDomain, LightDomain,
                            NatureDomain, TempestDomain, TrickeryDomain,
                            WarDomain, ArcanaDomain, ForgeDomain,
                            GraveDomain)
    spellcasting_ability = 'wisdom'
    spell_slots_by_level = {
        # char_lvl: (cantrips, 1st, 2nd, 3rd, ...)
        1:  (3, 2, 0, 0, 0, 0, 0, 0, 0, 0),
        2:  (3, 3, 0, 0, 0, 0, 0, 0, 0, 0),
        3:  (3, 4, 2, 0, 0, 0, 0, 0, 0, 0),
        4:  (4, 4, 3, 0, 0, 0, 0, 0, 0, 0),
        5:  (4, 4, 3, 2, 0, 0, 0, 0, 0, 0),
        6:  (4, 4, 3, 3, 0, 0, 0, 0, 0, 0),
        7:  (4, 4, 3, 3, 1, 0, 0, 0, 0, 0),
        8:  (4, 4, 3, 3, 2, 0, 0, 0, 0, 0),
        9:  (4, 4, 3, 3, 3, 1, 0, 0, 0, 0),
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

