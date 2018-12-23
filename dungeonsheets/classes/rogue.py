from .. import (weapons, features)
from .classes import CharClass, SubClass
from collections import defaultdict


# PHB
class Thief(SubClass):
    """You hone your skills in the larcenous arts. Burglars, bandits, cutpurses,
    and other criminals typically follow this archetype, but so do rogues who
    prefer to think of themselves as professional treasure seekers, explorers,
    delvers, and investigators. In addition to improving your agility and
    stealth, you learn skills useful for delving into ancient ruins, reading
    unfamiliar languages, and using magic items you normally couldn’t employ

    """
    name = "Thief"
    features_by_level = defaultdict(list)


class Assassin(SubClass):
    """You focus your training on the grim art of death. Those who adhere to this
    archetype are diverse: hired killers, spies, bounty hunters, and even
    specially anointed priests trained to exterminate the enemies of their
    deity. Stealth, poison, and disguise help you eliminate your foes with
    deadly efficiency

    """
    name = "Assassin"
    features_by_level = defaultdict(list)


class ArcaneTrickster(SubClass):
    """Some rogues enhance their fine-honed skills of stealth and agility with
    magic, learning tricks of enchantment and illusion. These rogues include
    pickpockets and burglars, but also pranksters, mischief-makers, and a
    significant number of adventurers.

    """
    name = "Arcane Trickster"
    features_by_level = defaultdict(list)
    spellcasting_ability = 'intelligence'
    multiclass_spellslots_by_level = {
        # char_lvl: (cantrips, 1st, 2nd, 3rd, ...)
        1:  (0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
        2:  (0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
        3:  (3, 2, 0, 0, 0, 0, 0, 0, 0, 0),
        4:  (3, 3, 0, 0, 0, 0, 0, 0, 0, 0),
        5:  (3, 3, 0, 0, 0, 0, 0, 0, 0, 0),
        6:  (3, 3, 0, 0, 0, 0, 0, 0, 0, 0),
        7:  (3, 4, 2, 0, 0, 0, 0, 0, 0, 0),
        8:  (3, 4, 2, 0, 0, 0, 0, 0, 0, 0),
        9:  (3, 4, 2, 0, 0, 0, 0, 0, 0, 0),
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


class Mastermind(SubClass):
    """Your focus is on people and on the influence and secrets they have. Many
    spies, courtiers, and schemers follow this archetype, leading lives of
    intrigue. Words are your weapons as often as knives or poison, and secrets
    and favors are some of your favorite treasures.

    """
    name = "Mastermind"
    features_by_level = defaultdict(list)


class Scout(SubClass):
    """You are skilled in stealth and surviving far from the streets of a city,
    allowing you to scout ahead of your companions during expeditions. Rogues
    who embrace this archetype are at home in the wilderness and among
    barbarians and rangers, and many Scouts serve as the eyes and ears of war
    bands. Ambusher, spy, bounty hunter#these are just a few of the roles that
    Scouts as- sume as they range the world.

    """
    name = "Scout"
    features_by_level = defaultdict(list)


class Swashbuckler(SubClass):
    """You focus your training on the art of the blade, relying on speed,
    elegance, and charm in equal parts. While some warriors are brutes clad in
    heavy armor, your method of fighting looks almost like a performance. Du—
    elists and pirates typically belong to this archetype. A Swashbuckler
    excels in single combat, and can fight with two weapons while safely
    darting away from an opponent

    """
    name = "Swashbuckler"
    features_by_level = defaultdict(list)


class Rogue(CharClass):
    name = 'Rogue'
    hit_dice_faces = 8
    saving_throw_proficiencies = ('dexterity', 'intelligence')
    primary_abilities = ('dexterity',)
    _proficiencies_text = (
        'light armor', 'simple weapons', 'hand crossbows', 'longswords',
        'rapiers', 'shortswords', "thieves' tools")
    weapon_proficiencies = (weapons,SimpleWeapon, weapons.HandCrossbow,
                            weapons.Longsword, weapons.Rapier,
                            weapons.Shortsword)
    multiclass_weapon_proficiencies = ()
    _multiclass_proficiencies_text = ('light armor', "thieves' tools",
                                      '[choose one skill from Rogue list]')
    class_skill_choices = ('Acrobatics', 'Athletics', 'Deception',
                           'Insight', 'Intimidation', 'Investigation',
                           'Perception', 'Performance', 'Persuasion',
                           'Sleight of Hand', 'Stealth')
    features_by_level = defaultdict(list)
    subclasses_available = (Thief, Assassin, ArcaneTrickster,
                            Inquisitive, Mastermind, Scout, Swashbuckler)
