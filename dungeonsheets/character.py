"""Tools for describing a player character."""
__all__ = ('Character',)

import re
import os
import warnings
from . import exceptions
import importlib.util
import jinja2
import subprocess

from .stats import Ability, Skill, findattr, ArmorClass, Speed, Initiative
from .dice import read_dice_str
from . import (weapons, race, background, spells, armor, monsters,
               exceptions, classes, features, magic_items)
from .weapons import Weapon
from .armor import Armor, NoArmor, Shield, NoShield


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


__version__ = read('../VERSION').strip()


dice_re = re.compile('(\d+)d(\d+)')

__all__ = ('Barbarian', 'Bard', 'Cleric', 'Druid', 'Fighter', 'Monk',
           'Paladin', 'Ranger', 'Rogue', 'Sorcerer', 'Warlock', 'Wizard', )

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
    player_name = ""
    alignment = "Neutral"
    dungeonsheets_version = __version__
    class_list = list()
    _race = None
    _background = None
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
    armor_class = ArmorClass()
    initiative = Initiative()
    speed = Speed()
    inspiration = 0
    _saving_throw_proficiencies = tuple()  # use to overwrite class proficiencies
    other_weapon_proficiencies = tuple()  # add to class/race proficiencies
    skill_proficiencies = list()
    skill_expertise = list()
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
    persuasion = Skill(ability='charisma')
    religion = Skill(ability='intelligence')
    sleight_of_hand = Skill(ability='dexterity')
    stealth = Skill(ability='dexterity')
    survival = Skill(ability='wisdom')
    # Characteristics
    attacks_and_spellcasting = ""
    personality_traits = "TODO: Describe how your character behaves, interacts with others"
    ideals = "TODO: Describe what values your character believes in."
    bonds = "TODO: Describe your character's commitments or ongoing quests."
    flaws = "TODO: Describe your character's interesting flaws."
    features_and_traits = "Describe any other features and abilities."
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
    _proficiencies_text = list()
    # Magic
    spellcasting_ability = None
    _spells = list()
    _spells_prepared = list()
    # Features IN MAJOR DEVELOPMENT
    custom_features = list()
    feature_choices = list()
    
    def __init__(self, **attrs):
        """Takes a bunch of attrs and passes them to ``set_attrs``"""
        self.clear()
        # make sure class, race, background are set first
        my_classes = attrs.pop('classes', [])
        my_levels = attrs.pop('levels', [])
        my_subclasses = attrs.pop('subclasses', [])
        # backwards compatability
        if (len(my_classes) == 0):
            if ('class' in attrs):
                my_classes = [attrs.pop('class')]
                my_levels = [attrs.pop('level', 1)]
                my_subclasses = [attrs.pop('subclass', None)]
            else:  # if no classes or levels given, default to Lvl 1 Fighter
                my_classes = ['Fighter']
                my_levels = [1]
                my_subclasses = [None]
        # Generate the list of class objects
        self.add_classes(
            my_classes, my_levels, my_subclasses,
            feature_choices=attrs.get('feature_choices', []))
        # parse race and background
        self.race = attrs.pop('race', None)
        self.background = attrs.pop('background', None)
        # parse all other attributes
        self.set_attrs(**attrs)

    def clear(self):
        # reset class-definied items
        self.class_list = list()
        self.weapons = list()
        self.magic_items = list()
        self._saving_throw_proficiencies = tuple()
        self.other_weapon_proficiencies = tuple()
        self.skill_proficiencies = list()
        self.skill_expertise = list()
        self._proficiencies_text = list()
        self._spells = list()
        self._spells_prepared = list()
        self.custom_features = list()
        self.feature_choices = list()
                
    def __str__(self):
        return self.name
    
    def __repr__(self):
        return f"<{self.class_name}: {self.name}>"

    def add_class(self, cls: (classes.CharClass, type, str), level: (int, str),
                  subclass=None, feature_choices=[]):
        if isinstance(cls, str):
            cls = cls.strip().title().replace(' ', '')
            try:
                cls = getattr(classes, cls)
            except AttributeError:
                raise AttributeError(
                    'class was not recognized from classes.py: {:s}'.format(cls))
        if isinstance(level, str):
            level = int(level)
        self.class_list.append(cls(level, owner=self,
                                   subclass=subclass,
                                   feature_choices=feature_choices))
            
    def add_classes(self, classes_list=[], levels=[], subclasses=[],
                    feature_choices=[]):
        if isinstance(classes_list, str):
            classes_list = [classes_list]
        if isinstance(levels, int) or isinstance(levels, float) or isinstance(levels, str):
            levels = [levels]
        if len(levels) == 0:
            levels = [1]*len(classes_list)
        if isinstance(subclasses, str):
            subclasses = [subclasses]
        if len(subclasses) == 0:
            subclasses = [None]*len(classes_list)
        assert len(classes_list) == len(levels), (
            'the length of classes {:d} does not match length of '
            'levels {:d}'.format(len(classes), len(levels)))
        assert len(classes_list) == len(subclasses), (
            'the length of classes {:d} does not match length of '
            'subclasses {:d}'.format(len(classes_list), len(subclasses)))
        class_list = []
        for cls, lvl, sub in zip(classes_list, levels, subclasses):
            params = {}
            params['feature_choices'] = feature_choices
            self.add_class(cls=cls, level=lvl, subclass=sub,
                           **params)
    
    @property
    def race(self):
        return self._race

    @race.setter
    def race(self, newrace):
        if isinstance(newrace, race.Race):
            self._race = newrace
            self._race.owner = self
        elif isinstance(newrace, type) and issubclass(newrace, race.Race):
            self._race = newrace(owner=self)
        elif isinstance(newrace, str):
            try:
                self._race = findattr(race, newrace)(owner=self)
            except AttributeError:
                msg = (f'Race "{newrace}" not defined. '
                       f'Please add it to ``race.py``')
                self._race = race.Race(owner=self)
                warnings.warn(msg)
        elif newrace is None:
            self._race = race.Race(owner=self)
        
    @property
    def background(self):
        return self._background

    @background.setter
    def background(self, bg):
        if isinstance(bg, background.Background):
            self._background = bg
            self._background.owner = self
        elif isinstance(bg, type) and issubclass(bg, background.Background):
            self._background = bg(owner=self)
        elif isinstance(bg, str):
            try:
                self._background = findattr(background, bg)(owner=self)
            except AttributeError:
                msg = (f'Background "{bg}" not defined. '
                       f'Please add it to ``background.py``')
                self._background = background.Background(owner=self)
                warnings.warn(msg)

    @property
    def class_name(self):
        if self.num_classes >= 1:
            return self.primary_class.name
        else:
            return ""

    @property
    def classes_and_levels(self):
        return ' / '.join([f'{c.name} {c.level}'
                           for c in self.class_list])

    @property
    def class_names(self):
        return [c.name for c in self.class_list]

    @property
    def levels(self):
        return [c.level for c in self.class_list]
    
    @property
    def subclasses(self):
        return list([c.subclass or '' for c in self.class_list])
    
    @property
    def level(self):
        return sum(c.level for c in self.class_list)

    @level.setter
    def level(self, new_level):
        self.primary_class.level = new_level
        if self.num_classes > 1:
            warnings.warn("Unable to tell which level to set. Updating "
                          "level of primary class {:s}".format(self.primary_class.name))
    
    @property
    def num_classes(self):
        return len(self.class_list)

    @property
    def has_class(self):
        return (self.num_classes > 0)

    @property
    def primary_class(self):
        # for now, assume first class given must be primary class
        if self.has_class:
            return self.class_list[0]
        else:
            return None

    @property
    def weapon_proficiencies(self):
        wp = set(self.other_weapon_proficiencies)
        if self.num_classes > 0:
            wp |= set(self.primary_class.weapon_proficiencies)
        if self.num_classes > 1:
            for c in self.class_list[1:]:
                wp |= set(c.multiclass_weapon_proficiencies)
        if self.race is not None:
            wp |= set(getattr(self.race, 'weapon_proficiencies', ()))
        if self.background is not None:
            wp |= set(getattr(self.background, 'weapon_proficiencies', ()))
        return tuple(wp)
    
    @weapon_proficiencies.setter
    def weapon_proficiencies(self, new_weapons):
        self.other_weapon_proficiencies = tuple(new_weapons)

    @property
    def other_weapon_proficiencies_text(self):
        return tuple(w.name for w in self.other_weapon_proficiencies)

    @property
    def features(self):
        fts = set(self.custom_features)
        if not self.has_class:
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
        return sorted(tuple(fts), key=(lambda x: x.name))

    @property
    def custom_features_text(self):
        return tuple([f.name for f in self.custom_features])

    def has_feature(self, feat):
        return any([isinstance(f, feat) for f in self.features])
    
    @property
    def saving_throw_proficiencies(self):
        if self.primary_class is None:
            return self._saving_throw_proficiencies
        else:
            return (self._saving_throw_proficiencies or
                    self.primary_class.saving_throw_proficiencies)

    @saving_throw_proficiencies.setter
    def saving_throw_proficiencies(self, vals):
        self._saving_throw_proficiencies = vals

    @property
    def spellcasting_classes(self):
        return [c for c in self.class_list if c.is_spellcaster]
    
    @property
    def is_spellcaster(self):
        return (len(self.spellcasting_classes) > 0)

    def spell_slots(self, spell_level):
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
                        eff_level += c.level
                    elif type(c) in [classes.Paladin, classes.Ranger]:
                        eff_level += c.level // 2
                    elif type(c) in [classes.Fighter, classes.Rogue]:
                        eff_level += c.level // 3
                if eff_level == 0:
                    return 0
                else:
                    return multiclass_spellslots_by_level[eff_level][spell_level]

    @property
    def spells(self):
        spells = set(self._spells) | set(self._spells_prepared)
        for f in self.features:
            spells |= set(f.spells_known) | set(f.spells_prepared)
        for c in self.spellcasting_classes:
            spells |= set(c.spells_known) | set(c.spells_prepared)
        if self.race is not None:
            spells |= set(self.race.spells_known) | set(self.race.spells_prepared)
        return sorted(tuple(spells), key=(lambda x: (x.name)))
            
    @property
    def spells_prepared(self):
        spells = set(self._spells_prepared)
        for f in self.features:
            spells |= set(f.spells_prepared)
        for c in self.spellcasting_classes:
            spells |= set(c.spells_prepared)
        if self.race is not None:
            spells |= set(self.race.spells_prepared)
        return sorted(tuple(spells), key=(lambda x: (x.name)))

    def set_attrs(self, **attrs):
        """Bulk setting of attributes. Useful for loading a character from a
        dictionary."""
        for attr, val in attrs.items():
            if attr == 'dungeonsheets_version':
                pass # Maybe we'll verify this later?
            elif attr == 'weapons':
                if isinstance(val, str):
                    val = [val]
                # Treat weapons specially
                for weap in val:
                    self.wield_weapon(weap)
            elif attr == 'magic_items':
                if isinstance(val, str):
                    val = [val]
                for mitem in val:
                    try:
                        self.magic_items.append(findattr(magic_items, mitem)(owner=self))
                    except (AttributeError):
                        msg = (f'Magic Item "{mitem}" not defined. '
                               f'Please add it to ``magic_items.py``')
                        warnings.warn(msg)
            elif attr == 'weapon_proficiencies':
                self.other_weapon_proficiencies = ()
                wps = set([findattr(weapons, w) for w in val])
                wps -= set(self.weapon_proficiencies)
                self.other_weapon_proficiencies = list(wps)
            elif attr == 'armor':
                self.wear_armor(val)
            elif attr == 'shield':
                self.wield_shield(val)
            elif attr == 'circle':
                if hasattr(self, 'Druid'):
                    self.Druid.circle = val
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
                self.custom_features += tuple(F(owner=self) for F in _features)
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
                    self._spells = tuple(S() for S in _spells)
                else:
                    # Instantiate them all for the spells list
                    self._spells_prepared = tuple(S() for S in _spells)
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
        all_proficiencies = tuple(self._proficiencies_text)
        if self.has_class:
            all_proficiencies += tuple(self.primary_class._proficiencies_text)
        if self.num_classes > 1:
            for c in self.class_list[1:]:
                all_proficiencies += tuple(c._multiclass_proficiencies_text)
        if self.race is not None:
            all_proficiencies += tuple(self.race.proficiencies_text)
        if self.background is not None:
            all_proficiencies += tuple(self.background.proficiencies_text)
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
            s = '(See Features Page)\n\n--' + s
            s += '\n\n=================\n\n'
        return s
    
    @property
    def magic_items_text(self):
        s = ', '.join([f.name + ("**" if f.needs_implementation else "")
                        for f in sorted(self.magic_items, key=(lambda x: x.name))])
        if s:
            s += ', '
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
        if isinstance(weapon, weapons.Weapon):
            weapon_ = type(weapon)(wielder=self)
        elif isinstance(weapon, str):
            try:
                NewWeapon = findattr(weapons, weapon)
            except AttributeError:
                raise AttributeError(f'Weapon "{weapon}" is not defined')
            weapon_ = NewWeapon(wielder=self)
        elif issubclass(weapon, weapons.Weapon):
            weapon_ = weapon(wielder=self)
        else:
            raise AttributeError(f'Weapon "{weapon}" is not defined')
        # Save it to the array
        self.weapons.append(weapon_)
    
    @property
    def hit_dice(self):
        """What type and how many dice to use for re-gaining hit points.
        
        To change, set hit_dice_num and hit_dice_faces."""
        return ' + '.join([f'{c.level}d{c.hit_dice_faces}'
                           for c in self.class_list])

    @property
    def hit_dice_faces(self):
        # Not a valid function if multiclass
        if self.num_classes > 1:
            warnings.warn("hit_dice_faces is not valid for multiclass characters")
        return self.primary_class.hit_dice_faces
    
    @hit_dice_faces.setter
    def hit_dice_faces(self, faces):
        self.primary_class.hit_dice_faces = faces
    
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
    
    def can_assume_shape(self, shape: monsters.Monster):
        return hasattr(self, 'Druid') and self.Druid.can_assume_shape(shape)

    @property
    def all_wild_shapes(self):
        if hasattr(self, 'Druid'):
            return self.Druid.all_wild_shapes
        else:
            return ()

    @property
    def wild_shapes(self):
        if hasattr(self, 'Druid'):
            return self.Druid.wild_shapes
        else:
            return ()

    @wild_shapes.setter
    def wild_shapes(self, new_shapes):
        if hasattr(self, 'Druid'):
            self.Druid.wild_shapes = new_shapes

    @classmethod
    def load(cls, character_file):
        # Create a character from the character definition
        char_props = read_character_file(character_file)
        classes = char_props.get('classes', [])
        # backwards compatability
        if (len(classes) == 0) and ('character_class' in char_props):
            char_props['classes'] = [char_props.pop('character_class').lower().capitalize()]
            char_props['levels'] = [str(char_props.pop('level'))]
        # Create the character with loaded properties
        char = Character(**char_props)
        return char

    def save(self, filename, template_file='character_template.txt'):
        # Create the template context
        context = dict(
            char=self,
        )
        # Render the template
        src_path = os.path.join(os.path.dirname(__file__), 'forms/')
        text = jinja2.Environment(
            loader=jinja2.FileSystemLoader(src_path or './')
        ).get_template(template_file).render(context)
        # Save the file
        with open(filename, mode='w') as f:
            f.write(text)

    def to_pdf(self, filename, **kwargs):
        from .make_sheets import make_sheet
        if filename.endswith('.pdf'):
            filename = filename.replace('pdf', 'py')
        make_sheet(filename, character=self,
                   flatten=kwargs.get('flatten', True))

        
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


# Add backwards compatability for tests
class Barbarian(Character):
    def __init__(self, level=1, **attrs):
        attrs['classes'] = ['Barbarian']
        attrs['levels'] = [level]
        super().__init__(**attrs)
    

class Bard(Character):
    def __init__(self, level=1, **attrs):
        attrs['classes'] = ['Bard']
        attrs['levels'] = [level]
        super().__init__(**attrs)


class Cleric(Character):
    def __init__(self, level=1, **attrs):
        attrs['classes'] = ['Cleric']
        attrs['levels'] = [level]
        super().__init__(**attrs)


class Druid(Character):
    def __init__(self, level=1, **attrs):
        attrs['classes'] = ['Druid']
        attrs['levels'] = [level]
        super().__init__(**attrs)


class Fighter(Character):
    def __init__(self, level=1, **attrs):
        attrs['classes'] = ['Fighter']
        attrs['levels'] = [level]
        super().__init__(**attrs)


class Monk(Character):
    def __init__(self, level=1, **attrs):
        attrs['classes'] = ['Monk']
        attrs['levels'] = [level]
        super().__init__(**attrs)


class Paladin(Character):
    def __init__(self, level=1, **attrs):
        attrs['classes'] = ['Paladin']
        attrs['levels'] = [level]
        super().__init__(**attrs)


class Ranger(Character):
    def __init__(self, level=1, **attrs):
        attrs['classes'] = ['Ranger']
        attrs['levels'] = [level]
        super().__init__(**attrs)


class Rogue(Character):
    def __init__(self, level=1, **attrs):
        attrs['classes'] = ['Rogue']
        attrs['levels'] = [level]
        super().__init__(**attrs)


class Sorceror(Character):
    def __init__(self, level=1, **attrs):
        attrs['classes'] = ['Sorceror']
        attrs['levels'] = [level]
        super().__init__(**attrs)


class Warlock(Character):
    def __init__(self, level=1, **attrs):
        attrs['classes'] = ['Warlock']
        attrs['levels'] = [level]
        super().__init__(**attrs)


class Wizard(Character):
    def __init__(self, level=1, **attrs):
        attrs['classes'] = ['Wizard']
        attrs['levels'] = [level]
        super().__init__(**attrs)

