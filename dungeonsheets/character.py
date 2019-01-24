"""Tools for describing a player character."""

import re
import warnings
import math

from .stats import Ability, Skill, findattr
from .dice import read_dice_str
from . import weapons, race, spells, armor, monsters, exceptions
from .weapons import Weapon
from .armor import Armor, NoArmor, Shield, NoShield

dice_re = re.compile('(\d+)d(\d+)')

__all__ = ('Barbarian', 'Bard', 'Cleric', 'Druid', 'Fighter', 'Monk',
           'Paladin', 'Ranger', 'Rogue', 'Sorcerer', 'Warlock', 'Wizard', )

class Character():
    """A generic player character. Intended to be subclasses by the
    various classes.
    
    """
    # General attirubtes
    name = ""
    class_name = ""
    player_name = ""
    background = ""
    level = 1
    alignment = "Neutral"
    race = None
    xp = 0
    # Hit points
    hp_max = 10
    hit_dice_faces = 2
    # Base stats (ability scores)
    strength = Ability()
    dexterity = Ability()
    constitution = Ability()
    intelligence = Ability()
    wisdom = Ability()
    charisma = Ability()
    saving_throw_proficiencies = []
    skill_proficiencies = tuple()
    class_skill_choices = tuple()
    num_skill_choices = 2
    weapon_proficiencies = tuple()
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
    weapons = [] # Replaced in __init__ constructor
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
        self.set_attrs(**attrs)
    
    def __str__(self):
        return self.name
    
    def __repr__(self):
        return f"<{self.class_name}: {self.name}>"
    
    @property
    def speed(self):
        return getattr(self.race, 'speed', 30)
    
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
    
    @property
    def is_spellcaster(self):
        result = (self.spellcasting_ability is not None)
        return result
    
    @property
    def spell_save_dc(self):
        ability_mod = getattr(self, self.spellcasting_ability).modifier
        return (8 + self.proficiency_bonus + ability_mod)
    
    @property
    def spell_attack_bonus(self):
        ability_mod = getattr(self, self.spellcasting_ability).modifier
        return (self.proficiency_bonus + ability_mod)
    
    def spell_slots(self, spell_level):
        """How many spells slots are available for this spell level."""
        return self.spell_slots_by_level[self.level][spell_level]
    
    def is_proficient(self, weapon: Weapon):
        """Is the character proficient with this item?
        
        Considers class proficiencies and race proficiencies.
        
        Parameters
        ----------
        weapon
          The weapon to be tested for proficiency.
        
        """
        all_proficiencies = tuple(self.weapon_proficiencies)
        all_proficiencies += tuple(getattr(self.race, 'weapon_proficiencies', tuple()))
        is_proficient = any((isinstance(weapon, W) for W in all_proficiencies))
        return is_proficient
    
    @property
    def proficiencies_text(self):
        final_text = ""
        all_proficiencies = self._proficiencies_text
        if self.race is not None:
            all_proficiencies += self.race.proficiencies_text
        all_proficiencies += self.proficiencies_extra
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
        return f"{self.level}d{self.hit_dice_faces}"
    
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


class Barbarian(Character):
    class_name = 'Barbarian'
    hit_dice_faces = 12
    saving_throw_proficiencies = ('strength', 'constitution')
    _proficiencies_text = ('light armor', 'medium armor', 'shields',
                           'simple weapons', 'martial weapons')
    weapon_proficiencies = (weapons.simple_weapons + weapons.martial_weapons)
    class_skill_choices = ('Animal Handling', 'Athletics',
                           'Intimidation', 'Nature', 'Perception', 'Survival')


class Bard(Character):
    class_name = 'Bard'
    hit_dice_faces = 8
    saving_throw_proficiencies = ('dexterity', 'charisma')
    _proficiencies_text = (
        'Light armor', 'simple weapons', 'hand crossbows', 'longswords',
        'rapiers', 'shortswords', 'three musical instruments of your choice')
    weapon_proficiencies = ((weapons.HandCrossbow, weapons.Longsword,
                            weapons.Rapier, weapons.Shortsword) +
                           weapons.simple_weapons)
    class_skill_choices = ('Acrobatics', 'Animal Handling', 'Arcana',
                           'Athletics', 'Deception', 'History', 'Insight',
                           'Intimidation', 'Investigation', 'Medicine', 'Nature',
                           'Perception', 'Performance', 'Persuasion', 'Religion',
                           'Sleight of Hand', 'Stealth', 'Survival')
    num_skill_choices = 3


class Cleric(Character):
    class_name = 'Cleric'
    hit_dice_faces = 8
    saving_throw_proficiencies = ('wisdom', 'charisma')
    _proficiencies_text = ('light armor', 'medium armor', 'shields',
                          'all simple weapons')
    weapon_proficiencies = weapons.simple_weapons
    class_skill_choices = ('History', 'Insight', 'Medicine',
                           'Persuasion', 'Religion')


class Druid(Character):
    class_name = 'Druid'
    circle = "" # Moon, land
    _wild_shapes = ()
    hit_dice_faces = 8
    saving_throw_proficiencies = ('intelligence', 'wisdom')
    spellcasting_ability = 'wisdom'
    languages = 'Druidic'
    _proficiencies_text = (
        'Light armor', 'medium armor',
        'shields (druids will not wear armor or use shields made of metal)',
        'clubs', 'daggers', 'darts', 'javelins', 'maces', 'quarterstaffs',
        'scimitars', 'sickles', 'slings', 'spears')
    weapon_proficiencies = (weapons.Club, weapons.Dagger, weapons.Dart,
                           weapons.Javelin, weapons.Mace, weapons.Quarterstaff,
                           weapons.Scimitar, weapons.Sickle, weapons.Sling, weapons.Spear)
    class_skill_choices = ('Arcana', 'Animal Handling', 'Insight',
                           'Medicine', 'Nature', 'Perception', 'Religion', 'Survival')
    spell_slots_by_level = {
        1:  (2, 2, 0, 0, 0, 0, 0, 0, 0, 0),
        2:  (2, 3, 0, 0, 0, 0, 0, 0, 0, 0),
        3:  (2, 4, 2, 0, 0, 0, 0, 0, 0, 0),
        4:  (3, 4, 3, 0, 0, 0, 0, 0, 0, 0),
        5:  (3, 4, 3, 2, 0, 0, 0, 0, 0, 0),
        6:  (3, 4, 3, 3, 0, 0, 0, 0, 0, 0),
        7:  (3, 4, 3, 3, 1, 0, 0, 0, 0, 0),
        8:  (3, 4, 3, 3, 2, 0, 0, 0, 0, 0),
        9:  (3, 4, 3, 3, 3, 1, 0, 0, 0, 0),
        10: (4, 4, 3, 3, 3, 2, 0, 0, 0, 0),
        11: (4, 4, 3, 3, 3, 2, 1, 0, 0, 0),
        12: (4, 4, 3, 3, 3, 2, 1, 0, 0, 0),
        13: (4, 4, 3, 3, 3, 2, 1, 1, 0, 0),
        14: (4, 4, 3, 3, 3, 2, 1, 1, 0, 0),
        15: (4, 4, 3, 3, 3, 2, 1, 1, 1, 0),
        16: (4, 4, 3, 3, 3, 2, 1, 1, 1, 0),
        17: (4, 4, 3, 3, 3, 2, 1, 1, 1, 1),
        18: (4, 4, 3, 3, 3, 3, 1, 1, 1, 1),
        19: (4, 4, 3, 3, 3, 3, 2, 1, 1, 1),
        20: (4, 4, 3, 3, 3, 3, 2, 2, 1, 1),
    }
    
    @property
    def all_wild_shapes(self):
        """Return all wild shapes, regardless of validity."""
        return self._wild_shapes
    
    @property
    def wild_shapes(self):
        """Return a list of valid wild shapes for this Druid."""
        valid_shapes = []
        for shape in self._wild_shapes:
            # Check if shape can be transformed into
            if self.can_assume_shape(shape):
                valid_shapes.append(shape)
        return valid_shapes
    
    @wild_shapes.setter
    def wild_shapes(self, new_shapes):
        actual_shapes = []
        # Retrieve the actual monster classes if possible
        for shape in new_shapes:
            if isinstance(shape, monsters.Monster):
                # Already a monster shape so just add it as is
                new_shape = shape
            else:
                # Not already a monster so see if we can find one
                try:
                    NewMonster = findattr(monsters, shape)
                    new_shape = NewMonster()
                except AttributeError:
                    msg = f'Wild shape "{shape}" not found. Please add it to ``monsters.py``'
                    raise exceptions.MonsterError(msg)
            actual_shapes.append(new_shape)
        # Save the updated list for later
        self._wild_shapes = actual_shapes
        
    def can_assume_shape(self, shape: monsters.Monster)-> bool:
        """Determine if a given shape meets the requirements for transforming.
        
        See Pg 66 of player's handbook.
        
        Parameters
        ==========
        shape
          A monster that the Druid wishes to transform into.
        
        Returns
        =======
        can_assume
          True if the monster meets the C/R, swim and flying speed
          restrictions.
        
        """
        # Determine acceptable states based on druid level
        if self.level < 2:
            max_cr = -1
            max_swim = 0
            max_fly = 0
        elif self.level < 4:
            max_cr = 1/4
            max_swim = 0
            max_fly = 0
        elif self.level < 8:
            max_cr = 1/2
            max_swim = None
            max_fly = 0
        else:
            max_cr = 1
            max_swim = None
            max_fly = None
        # Make adjustments for moon cirlce druids
        if self.circle.lower() == "moon":
            if 2 <= self.level < 6:
                max_cr = 1
            elif self.level >= 6:
                max_cr = math.floor(self.level / 3)
        # Check if the beast shape can be assumed
        valid_cr = (max_cr is None or shape.challenge_rating <= max_cr)
        valid_swim = (max_swim is None or shape.swim_speed <= max_swim)
        valid_fly = (max_fly is None or shape.fly_speed <= max_fly)
        can_assume = shape.is_beast and valid_cr and valid_swim and valid_fly
        return can_assume
    
    @property
    def spells(self):
        return tuple(S() for S in self.spells_prepared)
    
    @spells.setter
    def spells(self, val):
        if len(val) > 0:
            warnings.warn("Druids cannot learn spells, "
                          "use ``spells_prepared`` instead.",
                          RuntimeWarning)


class Fighter(Character):
    class_name = 'Fighter'
    hit_dice_faces = 10
    saving_throw_proficiencies = ('strength', 'constitution')
    _proficiencies_text = ('All armar', 'shields', 'simple weapons', 'martial weapons')
    weapon_proficiencies = weapons.simple_weapons + weapons.martial_weapons
    class_skill_choices = ('Acrobatics', 'Animal Handling',
                           'Athletics', 'History', 'Insight', 'Intimidation', 'Perception',
                           'Survival')


class Monk(Character):
    class_name = 'Monk'
    hit_dice_faces = 8
    saving_throw_proficiencies = ('strength', 'dexterity')
    _proficiencies_text = (
        'simple weapons', 'shortswords',
        "one type of artisan's tools or one musical instrument")
    weapon_proficiencies = (weapons.Shortsword,) + weapons.simple_weapons
    class_skill_choices = ('Acrobatics', 'Athletics', 'History', 'Insight', 'Religion', 'Stealth')

class Paladin(Character):
    class_name = 'Paladin'
    hit_dice_faces = 10
    saving_throw_proficiencies = ('wisdom', 'charisma')
    _proficiencies_text = ('All armor', 'shields', 'simple weapons',
                          'martial weapons')
    weapon_proficiencies = weapons.simple_weapons + weapons.martial_weapons
    class_skill_choices = ("Athletics", 'Insight', 'Intimidation',
                           'Medicine', 'Persuasion', 'Religion')


class Ranger(Character):
    class_name = 'Ranger'
    hit_dice_faces = 10
    saving_throw_proficiencies = ('strength', 'dexterity')
    _proficiencies_text = ("light armor", "medium armor", "shields",
                           "simple weapons", "martial weapons")
    weapon_proficiencies = weapons.simple_weapons + weapons.martial_weapons
    class_skill_choices = ('Animal Handling', 'Athletics', 'Insight',
                           'Investigation', 'Nature', 'Perception', 'Stealth', 'Survival')
    num_skill_choices = 3


class Rogue(Character):
    class_name = 'Rogue'
    hit_dice_faces = 8
    saving_throw_proficiencies = ('dexterity', 'intelligence')
    _proficiencies_text = (
        'light armor', 'simple weapons', 'hand crossbows', 'longswords',
        'rapiers', 'shortswords', "thieves' tools")
    weapon_proficiencies = (weapons.HandCrossbow, weapons.Longsword,
                           weapons.Rapier, weapons.Shortsword) + weapons.simple_weapons
    class_skill_choices = ('Acrobatics', 'Athletics', 'Deception',
                           'Insight', 'Intimidation', 'Investigation', 'Perception',
                           'Performance', 'Persuasion', 'Sleight of Hand', 'Stealth')


class Sorcerer(Character):
    class_name = 'Sorcerer'
    hit_dice_faces = 6
    saving_throw_proficiencies = ('constitution', 'charisma')
    _proficiencies_text = ('daggers', 'darts', 'slings',
                           'quarterstaffs', 'light crossbows')
    weapon_proficiencies = (weapons.Dagger, weapons.Dart,
                           weapons.Sling, weapons.Quarterstaff,
                           weapons.LightCrossbow)
    class_skill_choices = ('Arcana', 'Deception', 'Insight',
                           'Intimidation' ,'Persuasion', 'Religion')


class Warlock(Character):
    class_name = 'Warlock'
    hit_dice_faces = 8
    saving_throw_proficiencies = ('wisdom', 'charisma')
    _proficiencies_text = ("light Armor", "simple weapons")
    class_skill_choices = ('Arcana', 'Deception', 'History',
                           'Intimidation', 'Investigation', 'Nature', 'Religion')
    weapon_proficiencies = weapons.simple_weapons
    spellcasting_ability = 'charisma'
    spell_slots_by_level = {
        1:  (2, 1, 0, 0, 0, 0, 0, 0, 0, 0),
        2:  (2, 2, 0, 0, 0, 0, 0, 0, 0, 0),
        3:  (2, 0, 2, 0, 0, 0, 0, 0, 0, 0),
        4:  (3, 0, 2, 0, 0, 0, 0, 0, 0, 0),
        5:  (3, 0, 0, 3, 0, 0, 0, 0, 0, 0),
        6:  (3, 0, 0, 3, 0, 0, 0, 0, 0, 0),
        7:  (3, 0, 0, 0, 2, 0, 0, 0, 0, 0),
        8:  (3, 0, 0, 0, 2, 0, 0, 0, 0, 0),
        9:  (3, 0, 0, 0, 0, 2, 0, 0, 0, 0),
        10: (4, 0, 0, 0, 0, 2, 0, 0, 0, 0),
        11: (4, 0, 0, 0, 0, 3, 0, 0, 0, 0),
        12: (4, 0, 0, 0, 0, 3, 0, 0, 0, 0),
        13: (4, 0, 0, 0, 0, 3, 0, 0, 0, 0),
        14: (4, 0, 0, 0, 0, 3, 0, 0, 0, 0),
        15: (4, 0, 0, 0, 0, 3, 0, 0, 0, 0),
        16: (4, 0, 0, 0, 0, 3, 0, 0, 0, 0),
        17: (4, 0, 0, 0, 0, 4, 0, 0, 0, 0),
        18: (4, 0, 0, 0, 0, 4, 0, 0, 0, 0),
        19: (4, 0, 0, 0, 0, 4, 0, 0, 0, 0),
        20: (4, 0, 0, 0, 0, 4, 0, 0, 0, 0),
    }


class Wizard(Character):
    class_name = 'Wizard'
    hit_dice_faces = 6
    saving_throw_proficiencies = ('intelligence', 'wisdom')
    _proficiencies_text = ('daggers', 'darts', 'slings',
                          'quarterstaffs', 'light crossbows')
    weapon_proficiencies = (weapons.Dagger, weapons.Dart,
                           weapons.Sling, weapons.Quarterstaff,
                           weapons.LightCrossbow)
    class_skill_choices = ('Arcana', 'History', 'Investigation',
                           'Medicine', 'Religion')
    spellcasting_ability = 'intelligence'
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
