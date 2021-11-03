from collections import defaultdict

from dungeonsheets import features, weapons
from dungeonsheets.classes.classes import CharClass, SubClass


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


class BloodHunter(CharClass):
    name = "Blood Hunter"
    hit_dice_faces = 10
    subclass_select_level = 3
    subclasses_available = (OrderOfTheGhostslayer, OrderOfTheLycan, OrderOfTheMutant, OrderOfTheProfaneSoul)
    saving_throw_proficiencies = ("intelligence", "dexterity")
    primary_abilities = (
    	"dexterity",
    	"strenght",
    )
    _proficiencies_text = (
        "Light armor",
        "Medium armor",
        "Shields",
	"Simple Weapons",
	"Martial Weapons",
    )
    weapon_proficiencies = (weapons.SimpleWeapon, weapons.MartialWeapon)
    multiclass_weapon_proficiencies = (weapon_proficiencies)
    _multiclass_proficiencies_text = (
    	"light armor",
        "medium armor",
        "shields",
        "simple weapons",
        "martial weapons",
        )
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
