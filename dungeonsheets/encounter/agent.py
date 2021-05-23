from dungeonsheets.conditions.conditions import Blinded, Charmed
from dungeonsheets.encounter.actions import Attack
from dungeonsheets.stats import Ability, ArmorClass, Initiative, Speed, Skill, \
    NumericalInitiative
from abc import ABC
from dungeonsheets.dice import roll


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
    numerical_initiative = NumericalInitiative()
    _initiative_roll = False
    _current_hp = None
    statuses = list()

    # TODO: Pull in the monster class-variables here too

    def __init__(self):
        self.default_actions = list()
        self.default_bonus_actions = list()
        self.default_reactions = list()
        self.default_legendary_actions = list()
        self.default_lair_actions = list()
        self.long_rest()

    def roll_initiative(self):
        init_mod, adv = self.numerical_initiative
        val = roll(20)
        if adv:
            val = max(val, roll(20))
        self._initiative_roll = val + init_mod

    @property
    def current_hp(self):
        if self._current_hp is None:
            self._current_hp = self.hp_max
        return self._current_hp

    @current_hp.setter
    def current_hp(self, val):
        if val < 0:
            self._current_hp = 0
        else:
            self._current_hp = val

    @property
    def initiative_roll(self):
        if self._initiative_roll is False:
            self.roll_initiative()
        return self._initiative_roll

    def make_actions(self, encounter):
        """Return a series of actions"""

        # TODO: Dramatically improve logic, consider healing,
        #  consider encounter state, consider strategy etc.
        best_opponent = encounter.opponents(self)[0]  # TODO: Choose opponent cleverly
        action = self.actions[0](self, best_opponent)
        event = action.execute()
        encounter.events.append(event)
        return [event]  # TODO: Also allow bonus actions, etc.

    def long_rest(self):
        self.current_hp = self.hp_max
        # TODO: Support spell slots
        self.new_turn()

    def new_turn(self):
        self._actions = self.default_actions
        self._bonus_actions = self.default_bonus_actions
        self._reactions = self.default_reactions
        self._legendary_actions = self.default_legendary_actions
        self._lair_actions = self.default_lair_actions

    def has_feature(self, *args, **kwargs):
        return False  # TODO: Save list of monster features as a list to check

    # TODO: Consider having a single list of actions and gain or lose them each
    #  turn based on interrogating their sub-type instead, using isinstance or
    #  another method.

    @property
    def actions(self):
        """All the remaining things I can do in a turn"""
        return self._actions

    @property
    def movement(self):
        """The rest of where I can go in a turn"""
        return self._movement

    @property
    def bonus_actions(self):
        """The rest of the things I can do once in addition to an action"""
        return self._bonus_actions

    @property
    def reactions(self):
        """The remaining things I can do in response to an action"""
        return self._reactions

    @property
    def lair_actions(self):
        """Remaining things I can do at initiative count 20"""
        return self._lair_actions

    @property
    def legendary_actions(self):
        """Remaining things I can do only so many times in a turn after another agent acts"""
        return self._legendary_actions