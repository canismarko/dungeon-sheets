"""Tools for describing a player character."""

import re
import os
import warnings
from . import exceptions
import importlib.util
import jinja2
import subprocess

from .stats import Ability, Skill, findattr
from .dice import read_dice_str
from . import (weapons, race, background, spells, armor, monsters,
               exceptions, classes, features)
from .__init__ import __version__
from .weapons import Weapon
from .armor import Armor, NoArmor, Shield, NoShield

dice_re = re.compile('(\d+)d(\d+)')

multiclass_spellslots_by_level = {
        # char_lvl: (cantrips, 1st, 2nd, 3rd, ...)
        1:  (0, 2, 0, 0, 0, 0, 0, 0, 0, 0),
        2:  (0, 3, 0, 0, 0, 0, 0, 0, 0, 0),
        3:  (0, 4, 2, 0, 0, 0, 0, 0, 0, 0),
        4:  (0, 4, 3, 0, 0, 0, 0, 0, 0, 0),
        5:  (0, 4, 3, 2, 0, 0, 0, 0, 0, 0),
        6:  (0, 4, 3, 3, 0, 0, 0, 0, 0, 0),
        7:  (0, 4, 3, 3, 1, 0, 0, 0, 0, 0),
        8:  (0, 4, 3, 3, 2, 0, 0, 0, 0, 0),
        9:  (0, 4, 3, 3, 3, 1, 0, 0, 0, 0),
        10: (0, 4, 3, 3, 3, 2, 0, 0, 0, 0),
        11: (0, 4, 3, 3, 3, 2, 1, 0, 0, 0),
        12: (0, 4, 3, 3, 3, 2, 1, 0, 0, 0),
        13: (0, 4, 3, 3, 3, 2, 1, 1, 0, 0),
        14: (0, 4, 3, 3, 3, 2, 1, 1, 0, 0),
        15: (0, 4, 3, 3, 3, 2, 1, 1, 1, 0),
        16: (0, 4, 3, 3, 3, 2, 1, 1, 1, 0),
        17: (0, 4, 3, 3, 3, 2, 1, 1, 1, 1),
        18: (0, 4, 3, 3, 3, 3, 1, 1, 1, 1),
        19: (0, 4, 3, 3, 3, 3, 2, 1, 1, 1),
        20: (0, 4, 3, 3, 3, 3, 2, 2, 1, 1),
}


class Character():
    """A generic player character.
    
    """
    # General attirubtes
    name = ""
    class_name = ""
    player_name = ""
    alignment = "Neutral"
    dungeonsheets_version = __version__
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
    other_weapon_proficiencies = tuple()
    skill_proficiencies = tuple()
    skill_expertise = tuple()
    class_skill_choices = tuple()
    num_skill_choices = 2
    proficiencies_extra = tuple()
    languages = ""
    # Skills
    acrobatics = Skill(ability='dexterity', name='acrobatics')
    animal_handling = Skill(ability='wisdom', name='animal handling')
    arcana = Skill(ability='intelligence', name='arcana')
    athletics = Skill(ability='strength', name='athletics')
    deception = Skill(ability='charisma', name='deception')
    history = Skill(ability='intelligence', name='history')
    insight = Skill(ability='wisdom', name='insight')
    intimidation = Skill(ability='charisma', name='intimidation')
    investigation = Skill(ability='intelligence', name='investigation')
    medicine = Skill(ability='wisdom', name='medicine')
    nature = Skill(ability='intelligence', name='nature')
    perception = Skill(ability='wisdom', name='perception')
    performance = Skill(ability='charisma', name='performance')
    persuasion = Skill(ability='charisma', name='persuasion')
    religion = Skill(ability='intelligence', name='religion')
    sleight_of_hand = Skill(ability='dexterity', name='sleight of hand')
    stealth = Skill(ability='dexterity', name='stealth')
    survival = Skill(ability='wisdom', name='survival')
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
    # Features IN MAJOR DEVELOPMENT
    custom_features = ()
    feature_choices = ()
    
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
        # instantiate any spells not listed properly
        for S in self.spells_prepared:
            if S not in [type(spl) for spl in self.spells]:
                self.spells += (S(),)
                
    def __str__(self):
        return self.name
    
    def __repr__(self):
        return f"<{self.class_name}: {self.name}>"

    @property
    def class_name(self):
        return ' / '.join([f'{c.class_name} {c.class_level}'
                           for c in self.class_list])
    
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
    def classes_levels(self):
        return [c.class_name.lower() + ' ' + str(c.class_level)
                for c in self.class_list]
    
    @property
    def primary_class(self):
        # for now, assume first class given must be primary class
        if self.class_initialized:
            return self.class_list[0]
        else:
            return None

    @property
    def weapon_proficiencies(self):
        wp = set(self.other_weapon_proficiencies)
        if not self.class_initialized:
            return wp
        wp |= set(self.primary_class.weapon_proficiencies)
        if self.num_classes > 1:
            for c in self.class_list[1:]:
                wp |= set(c.multiclass_weapon_proficiencies)
        if self.race is not None:
            wp |= set(getattr(self.race, 'weapon_proficiencies', ()))
        if self.background is not None:
            wp |= set(getattr(self.background, 'weapon_proficiencies', ()))
        return tuple(wp)

    @property
    def features(self):
        fts = set(self.custom_features)
        if not self.class_initialized:
            return fts
        for c in self.class_list:
            fts |= set(c.features)
        if self.race is not None:
            fts |= set(getattr(self.race, 'features', ()))
            # some races have level-based features (Ex: Aasimar)
            if hasattr(self.race, 'features_by_level'):
                for lvl in range(1, self.level+1):
                    fts |= set(self.race.features_by_level[lvl])
        if self.background is not None:
            fts |= set(getattr(self.background, 'features', ()))
        return tuple(fts)

    @property
    def custom_features_text(self):
        return tuple([f.name for f in self.custom_features])
    
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
        if len(self.spellcasting_classes) == 1:
            return self.spellcasting_classes[0].spell_slots(spell_level)
        else:
            if spell_level == 0:
                return sum([c.spell_slots(0)
                            for c in self.spellcasting_classes])
            else:
                # compute effective level from PHB pg 164
                eff_level = 0
                for c in self.spellcasting_classes:
                    if type(c) in [classes.Bard, classes.Cleric, classes.Druid,
                                   classes.Sorceror, classes.Wizard]:
                        eff_level += c.class_level
                    elif type(c) in [classes.Paladin, classes.Ranger]:
                        eff_level += c.class_level // 2
                    elif type(c) in [classes.Fighter, classes.Rogue]:
                        eff_level += c.class_level // 3
                if eff_level == 0:
                    return 0
                else:
                    return multiclass_spellslots_by_level[eff_level][spell_level]

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
            elif attr == 'weapon_proficiencies':
                self.other_weapon_proficiencies = tuple([findattr(weapons, w)
                                                         for w in val])
            elif attr == 'race':
                if val is not None:
                    MyRace = findattr(race, val)
                    self.race = MyRace()
            elif attr == 'background':
                if val is not None:
                    MyBackground = findattr(background, val)
                    self.background = MyBackground()
            elif attr == 'armor':
                self.wear_armor(val)
            elif attr == 'shield':
                self.wield_shield(val)
            elif attr == 'wild_shapes':
                for c in self.class_list:
                    if isinstance(c, classes.Druid):
                        c.wild_shapes = val
                        self.all_wild_shapes = c.all_wild_shapes
                        self.wild_shapes = c.wild_shapes
                        self.can_assume_shape = c.can_assume_shape
                        break
            elif attr == 'circle':
                for c in self.class_list:
                    if isinstance(c, classes.Druid) and (c.circle == ''):
                        c.circle = val
                        self.circle = val
                        break
            elif attr == 'features':
                if isinstance(val, str):
                    val = [val]
                _features = []
                for f in val:
                    try:
                        _features.append(findattr(features, f))
                    except AttributeError:
                        msg = (f'Feature "{f}" not defined. '
                               f'Please add it to ``features.py``')
                        # create temporary feature
                        _features.append(features.create_feature(
                            name=f, source='Unknown',
                            __doc__="""Unknown Feature. Add to features.py"""))
                        warnings.warn(msg)
                self.custom_features = tuple(F() for F in _features)
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
                    # Instantiate them all for the spells list
                    self.spells_prepared = tuple(S() for S in _spells)
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

        Returns
        -------
        Boolean: is this character proficient with this weapon?
        
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

    @property
    def features_text(self):
        s = '\n\n--'.join([f.name + ("**" if f.needs_implementation else "")
                           for f in self.features])
        if s != '':
            s = '(See Features and Traits Page)\n\n--' + s
            s += '\n\n=================\n\n'
        return s
    
    def wear_armor(self, new_armor):
        """Accepts a string or Armor class and replaces the current armor.
        
        If a string is given, then a subclass of
        :py:class:`~dungeonsheets.armor.Armor` is retrived from the
        ``armor.py`` file. Otherwise, an subclass of
        :py:class:`~dungeonsheets.armor.Armor` can be provided
        directly.
        
        """
        if new_armor not in ('', 'None', None):
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
        if shield not in ('', 'None', None):
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
        # check if features add any bonuses
        for f in self.features:
            weapon_ = f.weapon_func(weapon_, char=self)
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
    def default_AC(self):
        """Armor class, including contributions from worn armor and shield."""
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

    @property
    def armor_class(self):
        """Armor class, including any applicable features"""
        if hasattr(self, 'force_AC'):
            return self.force_AC
        ac = [self.default_AC]
        ac += [f.AC_func(self) for f in self.features]
        return max(ac)

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
                this_class = getattr(classes, c.capitalize())
                this_level = int(lvl)
            except AttributeError:
                raise AttributeError(
                    'class was not recognized from classes.py: {:s}'.format(c))
            except ValueError:
                raise ValueError(
                    'level was not recognizable as an int: {:s}'.format(lvl))
            params = {}
            params['feature_choices'] = char_props.get('feature_choices', [])
            class_list += [this_class(this_level, subclass=sub, **params)]
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

    def save(self, filename, template_file='character_template.txt'):
        # Create the template context
        context = dict(
            char=self,
        )
        # Render the template
        src_path = os.path.dirname(__file__)
        text = jinja2.Environment(
            loader=jinja2.FileSystemLoader(src_path or './')
        ).get_template(template_file).render(context)
        # Save the file
        with open(filename, mode='w') as f:
            f.write(text)

    def to_pdf(self, filename, **kwargs):
        char_file = filename.replace('pdf', 'py')
        self.save(char_file,
                  template_file=kwargs.get('template_file',
                                           'character_template.txt'))
        subprocess.call(['makesheets', char_file])

        
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
