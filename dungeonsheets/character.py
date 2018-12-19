"""Tools for describing a player character."""

import re
import os
import warnings
from . import exceptions
import importlib.util

from .stats import Ability, Skill, findattr
from .dice import read_dice_str
from . import (weapons, race, background, spells, armor, monsters,
               exceptions, classes)
from .weapons import Weapon
from .armor import Armor, NoArmor, Shield, NoShield

dice_re = re.compile('(\d+)d(\d+)')


class Character():
    """A generic player character.
    
    """
    # General attirubtes
    name = ""
    class_name = ""
    player_name = ""
    alignment = "Neutral"
    class_list = []
    race = None
    background = None
    xp = 0
    # Hit points
    hp_max = 10
    # Base stats (ability scores)
    strength = Ability()
    dexterity = Ability()
    constitution = Ability()
    intelligence = Ability()
    wisdom = Ability()
    charisma = Ability()
    skill_proficiencies = tuple()
    class_skill_choices = tuple()
    num_skill_choices = 2
    proficiencies_extra = tuple()
    languages = ""
    # Skills
    acrobatics = Skill(ability='dexterity')
    animal_handling = Skill(ability='wisdom')
    arcana = Skill(ability='intelligence')
    athletics = Skill(ability='strength')
    deception = Skill(ability='charisma')
    history = Skill(ability='intelligence')
    insight = Skill(ability='wisdom')
    intimidation = Skill(ability='charisma')
    investigation = Skill(ability='intelligence')
    medicine = Skill(ability='wisdom')
    nature = Skill(ability='intelligence')
    perception = Skill(ability='wisdom')
    performance = Skill(ability='charisma')
    persuasian = Skill(ability='charisma')
    religion = Skill(ability='intelligence')
    sleight_of_hand = Skill(ability='dexterity')
    stealth = Skill(ability='dexterity')
    survival = Skill(ability='wisdom')
    # Characteristics
    attacks_and_spellcasting = ""
    personality_traits = ""
    ideals = ""
    bonds = ""
    flaws = ""
    features_and_traits = ""
    # Inventory
    cp = 0
    sp = 0
    ep = 0
    gp = 0
    pp = 0
    equipment = ""
    weapons = []  # Replaced in __init__ constructor
    armor = None
    shield = None
    _proficiencies_text = tuple()
    # Magic
    spellcasting_ability = None
    spells = tuple()
    spells_prepared = tuple()
    
    def __init__(self, **attrs):
        """Takes a bunch of attrs and passes them to ``set_attrs``"""
        self.weapons = []
        # make sure class, race, background are set first
        class_list = attrs.pop('class_list', self.class_list)
        race = attrs.pop('race', self.race)
        background = attrs.pop('background', self.background)
        self.set_attrs(**{'class_list': class_list,
                          'race': race,
                          'background': background})
        self.set_attrs(**attrs)
        for c in self.class_list:
            if isinstance(c, classes.Druid):
                ws = self.wild_shapes
                c.wild_shapes = ws
                c.circle = self.circle
                self.all_wild_shapes = c.all_wild_shapes
                self.wild_shapes = c.wild_shapes
                self.can_assume_shape = c.can_assume_shape
                
    def __str__(self):
        return self.name
    
    def __repr__(self):
        return f"<{self.class_name}: {self.name}>"

    @property
    def speed(self):
        return getattr(self.race, 'speed', 30)

    @property
    def level(self):
        return sum(c.class_level for c in self.class_list)

    @property
    def num_classes(self):
        return len(self.class_list)

    @property
    def class_initialized(self):
        return (self.num_classes > 0)
    
    @property
    def primary_class(self):
        # for now, assume first class given must be primary class
        if self.class_initialized:
            return self.class_list[0]
        else:
            return None

    @property
    def weapon_proficiencies(self):
        if not self.class_initialized:
            return ()
        wp = set(self.primary_class.weapon_proficiencies)
        if self.num_classes > 1:
            for c in self.class_list[1:]:
                wp |= set(c.multiclass_weapon_proficiencies)
        if self.race is not None:
            wp |= set(getattr(self.race, 'weapon_proficiencies', ()))
        if self.background is not None:
            wp |= set(getattr(self.background, 'weapon_proficiencies', ()))
        return wp
            
    @property
    def saving_throw_proficiencies(self):
        if self.primary_class is not None:
            return self.primary_class.saving_throw_proficiencies
        else:
            return ()

    @property
    def spellcasting_classes(self):
        return [c for c in self.class_list if c.is_spellcaster]
    
    @property
    def is_spellcaster(self):
        return (len(self.spellcasting_classes) > 0)

    def spell_slots(self, spell_level):
        # TODO: Update this for Multiclassing
        return self.spellcasting_classes[0].spell_slots(spell_level)

    def set_attrs(self, **attrs):
        """Bulk setting of attributes. Useful for loading a character from a
        dictionary."""
        for attr, val in attrs.items():
            if attr == 'dungeonsheets_version':
                pass # Maybe we'll verify this later?
            elif attr == 'weapons':
                # Treat weapons specially
                for weap in val:
                    self.wield_weapon(weap)
            elif attr == 'race':
                MyRace = findattr(race, val)
                self.race = MyRace()
            elif attr == 'background':
                MyBackground = findattr(background, val)
                self.race = MyBackground()
            elif attr == 'armor':
                self.wear_armor(val)
            elif attr == 'shield':
                self.wield_shield(val)
            elif (attr == 'spells') or (attr == 'spells_prepared'):
                # Create a list of actual spell objects
                _spells = []
                for spell_name in val:
                    try:
                        _spells.append(findattr(spells, spell_name))
                    except AttributeError:
                        msg = (f'Spell "{spell_name}" not defined. '
                               f'Please add it to ``spells.py``')
                        warnings.warn(msg)
                        # Create temporary spell
                        _spells.append(spells.create_spell(name=spell_name, level=9))
                        # raise AttributeError(msg)
                # Sort by name
                _spells.sort(key=lambda spell: spell.name)
                # Save list of spells to character atribute
                if attr == 'spells':
                    # Instantiate them all for the spells list
                    self.spells = tuple(S() for S in _spells)
                else:
                    self.spells_prepared = tuple(_spells)
            else:
                if not hasattr(self, attr):
                    warnings.warn(f"Setting unknown character attribute {attr}",
                                  RuntimeWarning)
                # Lookup general attributes
                setattr(self, attr, val)

    def spell_save_dc(self, class_type):
        ability_mod = getattr(self, class_type.spellcasting_ability).modifier
        return (8 + self.proficiency_bonus + ability_mod)
    
    def spell_attack_bonus(self, class_type):
        ability_mod = getattr(self, class_type.spellcasting_ability).modifier
        return (self.proficiency_bonus + ability_mod)
    
    def is_proficient(self, weapon: Weapon):
        """Is the character proficient with this item?
        
        Considers class proficiencies and race proficiencies.
        
        Parameters
        ----------
        weapon
          The weapon to be tested for proficiency.
        
        """
        all_proficiencies = self.weapon_proficiencies
        is_proficient = any((isinstance(weapon, W) for W in all_proficiencies))
        return is_proficient
    
    @property
    def proficiencies_text(self):
        final_text = ""
        all_proficiencies = set(self._proficiencies_text)
        if self.class_initialized:
            all_proficiencies |= set(self.primary_class._proficiencies_text)
        if self.num_classes > 1:
            for c in self.class_list[1:]:
                all_proficiencies |= set(c._multiclass_proficiencies_text)
        if self.race is not None:
            all_proficiencies |= set(self.race.proficiencies_text)
        if self.background is not None:
            all_proficiencies |= set(self.background.proficiencies_text)
        all_proficiencies |= set(self.proficiencies_extra)
        # Create a single string out of all the proficiencies
        for txt in all_proficiencies:
            if not final_text:
                # Capitalize the first entry
                txt = txt.capitalize()
            else:
                # Put a comma first
                txt = ", " + txt
                # Add this item to the list text
            final_text += txt
        # Add a period at the end
        final_text += '.'
        return final_text
    
    def wear_armor(self, new_armor):
        """Accepts a string or Armor class and replaces the current armor.
        
        If a string is given, then a subclass of
        :py:class:`~dungeonsheets.armor.Armor` is retrived from the
        ``armor.py`` file. Otherwise, an subclass of
        :py:class:`~dungeonsheets.armor.Armor` can be provided
        directly.
        
        """
        if new_armor not in ('', None):
            if isinstance(new_armor, armor.Armor):
                new_armor = new_armor
            else:
                NewArmor = findattr(armor, new_armor)
                new_armor = NewArmor()
            self.armor = new_armor
    
    def wield_shield(self, shield):
        """Accepts a string or Shield class and replaces the current armor.
        
        If a string is given, then a subclass of
        :py:class:`~dungeonsheets.armor.Shield` is retrived from the
        ``armor.py`` file. Otherwise, an subclass of
        :py:class:`~dungeonsheets.armor.Shield` can be provided
        directly.
        
        """
        if shield not in ('', None):
            try:
                NewShield = findattr(armor, shield)
            except AttributeError:
                # Not a string, so just treat it as Armor
                NewShield = shield
            self.shield = NewShield()
    
    def wield_weapon(self, weapon):
        """Accepts a string and adds it to the list of wielded weapons.
        
        Parameters
        ----------
        weapon : str
          Case-insensitive string with a name of the weapon.
        
        """
        # Retrieve the weapon class from the weapons module
        try:
            NewWeapon = findattr(weapons, weapon)
        except AttributeError:
            raise AttributeError(f'Weapon "{weapon}" is not defined')
        weapon_ = NewWeapon()
        # Set weapon attributes based on character
        if weapon_.is_finesse:
            ability_mod = max(self.strength.modifier, self.dexterity.modifier)
        else:
            ability_mod = getattr(self, weapon_.ability).modifier
        weapon_.attack_bonus += ability_mod
        weapon_.bonus_damage += ability_mod
        # Check for prifiency
        if self.is_proficient(weapon_):
            weapon_.attack_bonus += self.proficiency_bonus
        # Save it to the array
        self.weapons.append(weapon_)
    
    @property
    def hit_dice(self):
        """What type and how many dice to use for re-gaining hit points.
        
        To change, set hit_dice_num and hit_dice_faces."""
        return ' + '.join([f'{c.class_level}d{c.hit_dice_faces}'
                           for c in self.class_list])
    
    @property
    def proficiency_bonus(self):
        if self.level < 5:
            prof = 2
        elif 5 <= self.level < 9:
            prof = 3
        elif 9 <= self.level < 13:
            prof = 4
        elif 13 <= self.level < 17:
            prof = 5
        elif 17 <= self.level:
            prof = 6
        return prof
    
    @property
    def armor_class(self):
        """Armor class, including contributions from worn armor and shield."""
        # ## TODO:
        # Implement AC functions by class
        # Retrieve current armor (or a generic armor substitute)
        armor = self.armor if self.armor is not None else NoArmor()
        shield = self.shield if self.shield is not None else NoShield()
        # Calculate and apply modifiers
        if armor.dexterity_mod_max is None:
            modifier = self.dexterity.modifier
        else:
            modifier = min(self.dexterity.modifier, armor.dexterity_mod_max)
        # Calculate final armor class
        ac = armor.base_armor_class + shield.base_armor_class + modifier
        return ac

    @classmethod
    def load(cls, character_file):
        # Create a character from the character definition
        char_props = read_character_file(character_file)
        classes_levels = char_props.pop('classes_levels', [])
        if isinstance(classes_levels, str):
            classes_levels = [classes_levels]
        subclasses = char_props.pop('subclasses', [])
        if isinstance(subclasses, str):
            subclasses = [subclasses]
        if len(subclasses) == 0:
            subclasses = [None]*len(classes_levels)
        assert len(classes_levels) == len(subclasses), (
            'the length of classes_levels {:d} does not match length of '
            'subclasses {:d}'.format(len(classes_levels), len(subclasses)))
        class_list = []
        for cl, sub in zip(classes_levels, subclasses):
            try:
                c, lvl = cl.strip().split(' ')  # " wizard 3 " => "wizard", "3"
            except ValueError:
                raise ValueError(
                    'classes_levels not properly formatted. Each entry should '
                    'be formatted \"class level\", but got {:s}'.format(cl))
            try:
                this_class = getattr(classes, c)
                this_level = int(lvl)
            except AttributeError:
                raise AttributeError(
                    'class was not recognized from classes.py: {:s}'.format(c))
            except ValueError:
                raise ValueError(
                    'level was not recognizable as an int: {:s}'.format(lvl))
            class_list += [this_class(this_level, subclass=sub)]
        # accept backwards compatability for single-class characters
        if len(class_list) == 0:
            class_name = char_props.pop('character_class').lower().capitalize()
            class_level = char_props.pop('level')
            CharClass = getattr(classes, class_name)
            class_list = [CharClass(class_level)]
        char_props['class_list'] = class_list
        # Create the character with loaded properties
        char = cls(**char_props)
        return char


def read_character_file(filename):
    """Create a character object from the given definition file.
    
    The definition file should be an importable python file, filled
    with variables describing the character.
    
    Parameters
    ----------
    filename : str
      The path to the file that will be imported.
    
    """
    # Parse the file name
    dir_, fname = os.path.split(os.path.abspath(filename))
    module_name, ext = os.path.splitext(fname)
    if ext != '.py':
        raise ValueError(f"Character definition {filename} is not a python file.")
    # Check if this file contains the version string
    version_re = re.compile('dungeonsheets_version\s*=\s*[\'"]([0-9.]+)[\'"]')
    with open(filename, mode='r') as f:
        version = None
        for line in f:
            match = version_re.match(line)
            if match:
                version = match.group(1)
                break
        if version is None:
            # Not a valid DND character file
            raise exceptions.CharacterFileFormatError(
                f"No ``dungeonsheets_version = `` entry in `{filename}`.")
    # Import the module to extract the information
    spec = importlib.util.spec_from_file_location('module', filename)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    # Prepare a list of properties for this character
    char_props = {}
    for prop_name in dir(module):
        if prop_name[0:2] != '__':
            char_props[prop_name] = getattr(module, prop_name)
    return char_props
