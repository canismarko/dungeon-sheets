from dungeonsheets.conditions.conditions import Blinded, Charmed
from dungeonsheets.stats import Ability, ArmorClass, Initiative, Speed, Skill, CurrentInitiative, CurrentHP
from abc import ABC


class Agent(ABC):
    """An actor in an encounter. Use Monster or Character, not this class directly!"""

    # General attributes
    name = ""
    alignment = "Neutral"

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

    # Conditions
    blinded = Blinded()
    charmed = Charmed()
    # TODO finish me!

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

    # Current Status:
    initiative_roll = CurrentInitiative()
    current_hp = CurrentHP()
    statuses = list()

    # TODO: Pull in the monster class-variables here too

    def __init__(self):
        pass

    # TODO: Perhaps these are better stored like the skills are as objects with a __get__?

    @property
    def actions(self):
        """All the things I can do in a turn"""
        return []
    
    @property
    def free_actions(self):
        """Stuff I can do as much as I want in a turn"""
        return []

    @property
    def movement(self):
        """Where I can go in a turn"""
        return []

    @property
    def bonus_actions(self):
        """Things I can do once in addition to an action"""
        return []

    @property
    def reactions(self):
        """Things I can do in response to an action"""
        return []

    @property
    def lair_actions(self):
        """Things I can do at initiative count 20"""
        return []

    @property
    def legendary_actions(self):
        """Things I can do so many times in a turn after another agent acts"""
        return []