from dungeonsheets.stats import Ability, ArmorClass, Initiative, Speed, Skill
from abc import ABC
import os


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


__version__ = read("../VERSION").strip()


class Entity(ABC):
    """A thing with stats. Use Monster or Character, not this class directly!"""

    # General attributes
    dungeonsheets_version = __version__
    name = ""
    alignment = "Neutral"
    _race = None

    # Hit points
    hp_max = None

    # Base stats (ability scores)
    strength = Ability()
    dexterity = Ability()
    constitution = Ability()
    intelligence = Ability()
    wisdom = Ability()
    charisma = Ability()

    # Numerical things
    armor_class = ArmorClass()
    initiative = Initiative()
    speed = Speed()

    # Proficiencies and Languages
    _saving_throw_proficiencies = tuple()  # use to overwrite class proficiencies
    other_weapon_proficiencies = tuple()  # add to class/race proficiencies
    skill_proficiencies = list()
    skill_expertise = list()
    languages = ""
    senses = ""

    # Skills
    acrobatics = Skill(ability="dexterity")
    animal_handling = Skill(ability="wisdom")
    arcana = Skill(ability="intelligence")
    athletics = Skill(ability="strength")
    deception = Skill(ability="charisma")
    history = Skill(ability="intelligence")
    insight = Skill(ability="wisdom")
    intimidation = Skill(ability="charisma")
    investigation = Skill(ability="intelligence")
    medicine = Skill(ability="wisdom")
    nature = Skill(ability="intelligence")
    perception = Skill(ability="wisdom")
    performance = Skill(ability="charisma")
    persuasion = Skill(ability="charisma")
    religion = Skill(ability="intelligence")
    sleight_of_hand = Skill(ability="dexterity")
    stealth = Skill(ability="dexterity")
    survival = Skill(ability="wisdom")

    # Inventory
    cp = 0
    sp = 0
    ep = 0
    gp = 0
    pp = 0
    equipment = ""
    weapons = list()
    magic_items = list()
    armor = None
    shield = None

    # Magic
    spellcasting_ability = None
    _spells = list()
    _spells_prepared = list()
    infusions = list()

    # Features IN MAJOR DEVELOPMENT
    custom_features = list()
    feature_choices = list()

    def __init__(self):
        pass
