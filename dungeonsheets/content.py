"""Base classes for the various D&D 5e content types."""


import warnings
from abc import ABC
from pathlib import Path

from dungeonsheets.stats import Ability, ArmorClass, Initiative, Speed, Skill
from dungeonsheets.content_registry import find_content


def read(fname):
    return open((Path(__file__).parent / fname).resolve()).read()


__version__ = read("../VERSION").strip()


class Content(ABC):
    """A base class for all D&D 5e content types.

    Every piece of content (e.g. class feature, spell, monster) should
    have this base class in its inheritance tree.

    """
    dungeonsheets_version = __version__
    name = "Generic content"


class Creature(Content):
    """A thing with stats. Use Monster or Character, not this class
    directly!

    """
    # General attributes
    alignment = "Neutral"
    _race = None
    name = "Generic creature"
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
    _weapons = list()
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

    @property
    def weapons(self):
        return self._weapons.copy()

    @property
    def passive_wisdom(self):
        return self.perception.modifier + 10

    @property
    def abilities(self):
        return [self.strength, self.dexterity, self.constitution,
                self.intelligence, self.wisdom, self.charisma]

    @property
    def skills(self):
        return [self.acrobatics, self.animal_handling, self.arcana,
                self.athletics, self.deception, self.history,
                self.insight, self.intimidation, self.investigation,
                self.medicine, self.nature, self.perception,
                self.performance, self.persuasion, self.religion,
                self.sleight_of_hand, self.stealth, self.survival]

    @staticmethod
    def _resolve_mechanic(mechanic, SuperClass, warning_message=None):
        """Take a raw entry in a character sheet and turn it into a usable object.

        Eg: spells can be defined in many ways. This function accepts all
        of those options and returns an actual *Spell* class that can be
        used by a character::

            >>> _resolve_mechanic("mage_hand", SuperClass=spells.Spell)

            >>> _resolve_mechanic("mage_hand", SuperClass=None)

            >>> from dungeonsheets import spells
            >>> class MySpell(spells.Spell): pass
            >>> _resolve_mechanic(MySpell, SuperClass=spells.Spell)

            >>> _resolve_mechanic("hocus pocus", SuperClass=spells.Spell)

        The acceptable entries for *mechanic*, in priority order, are:
          1. A subclass of *SuperClass*
          2. A string with the name of defined content
          3. The name of an unknown spell (creates generic object using *factory*)

        *SuperClass* can be ``None`` to match any class, however this will
        raise an exception if more than one content type has this
        name. For example, "shield" can refer to both the armor or the
        spell, so ``_resolve_mechanic("shield")`` will raise an exception.

        Parameters
        ==========
        mechanic : str, type
          The thing to be resolved, either a string with the name of the
          mechanic, or a subclass of *ParentClass* describing the
          mechanic.
        SuperClass : type
          Class to determine whether *mechanic* should just be allowed
          through as is.
        error_message : str, optional
          A string whose ``str.format()`` method (receiving one positional
          argument *mechanic*) will be used for displaying a warning when an
          unknown mechanic is resolved. If omitted, no warning will be
          displayed.

        Returns
        =======
        Mechanic
          A class representing the resolved game mechanic. This will
          likely be a subclass of *SuperClass* if the other parameters are
          well behaved, but this is not enforced.

        """
        is_already_resolved = isinstance(mechanic, type) and issubclass(
            mechanic, SuperClass
        )
        if is_already_resolved:
            Mechanic = mechanic
        elif SuperClass is not None and isinstance(mechanic, SuperClass):
            # Has been instantiated for some reason
            Mechanic = type(Mechanic)
        else:
            try:
                # Retrieve pre-defined mechanic
                valid_classes = [SuperClass] if SuperClass is not None else []
                Mechanic = find_content(mechanic, valid_classes=valid_classes)
            except ValueError:
                # No pre-defined mechanic available
                if warning_message is not None:
                    # Emit the warning
                    msg = warning_message.format(mechanic)
                    warnings.warn(msg)
                else:
                    # Create a generic message so we can make a docstring later.
                    msg = f'Mechanic "{mechanic}" not defined. Please add it.'
                # Create generic mechanic from the factory
                class_name = "".join([s.title() for s in mechanic.split("_")])
                mechanic_name = mechanic.replace("_", " ").title()
                attrs = {"name": mechanic_name, "__doc__": msg, "source": "Unknown"}
                Mechanic = type(class_name, (SuperClass,), attrs)
        return Mechanic
