"""Tools for describing a player character."""

import re

from .stats import Ability, Skill, findattr
from .dice import read_dice_str
from . import weapons

dice_re = re.compile('(\d+)d(\d+)')

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
    race = "Human"
    xp = 0
    speed = 30 # In feet
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
    weapon_proficienies = tuple()
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
    personality_traits = ""
    ideals = ""
    bonds = ""
    flaws = ""
    # Inventory
    cp = 0
    sp = 0
    ep = 0
    gp = 0
    pp = 0
    equipment = ""
    weapons = [] # Replaced in __init__ constructor
    _proficiencies_text = tuple()
    
    def __init__(self, **attrs):
        """Takes a bunch of attrs and passes them to ``set_attrs``"""
        self.weapons = []
        self.set_attrs(**attrs)
    
    def set_attrs(self, **attrs):
        """Bulk setting of attributes. Useful for loading a character from a
        dictionary."""
        for attr, val in attrs.items():
            if attr == 'weapons':
                # Treat weapons specially
                for weap in val:
                    self.wield_weapon(weap)
            else:
                if not hasattr(self, attr):
                    warnings.warn(f"Setting unknown character attribute {attr}",
                                  RuntimeWarning)
                # Lookup general attributes
                setattr(self, attr, val)
    
    @property
    def proficiencies_text(self):
        final_text = ""
        all_proficiencies = (self._proficiencies_text + self.proficiencies_extra)
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
            raise AttributeError(f'Weapon {weapon} is not defined')
        weapon_ = NewWeapon()
        # Set weapon attributes based on character
        if weapon_.is_finesse:
            ability_mod = max(self.strength.modifier, self.dexterity.modifier)
        else:
            ability_mod = getattr(self, weapon_.ability).modifier
        weapon_.attack_bonus += ability_mod
        weapon_.bonus_damage += ability_mod
        # Check for prifiency
        is_proficient = (weapon_.__class__ in self.weapon_proficienies)
        if is_proficient:
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
        """Armor class, without items."""
        return 10 + self.dexterity.modifier


class Barbarian(Character):
    class_name = 'Barbarian'
    hit_dice_faces = 12
    saving_throw_proficiencies = ('strength', 'constitution')
    _proficiencies_text = ('light armor', 'medium armor', 'shields',
                           'simple weapons', 'martial weapons')
    weapon_proficienies = (weapons.simple_weapons + weapons.martial_weapons)


class Bard(Character):
    class_name = 'Bard'
    hit_dice_faces = 8
    saving_throw_proficiencies = ('dexterity', 'charisma')
    _proficiencies_text = (
        'Light armor', 'simple weapons', 'hand crossbows', 'longswords',
        'rapiers', 'shortswords', 'three musical instruments of your choice')
    weapon_proficienies = ((weapons.HandCrossbow, weapons.Longsword,
                            weapons.Rapier, weapons.Shortsword) +
                           weapons.simple_weapons)


class Cleric(Character):
    class_name = 'Cleric'
    hit_dice_faces = 8
    saving_throw_proficiencies = ('wisdom', 'charisma')
    _proficiencies_text = ('light armor', 'medium armor', 'shields',
                          'all simple weapons')
    weapon_proficienies = weapons.simple_weapons


class Druid(Character):
    class_name = 'Druid'
    hit_dice_faces = 8
    saving_throw_proficiencies = ('intelligence', 'wisdom')
    _proficiencies_text = (
        'Light armor', 'medium armor',
        'shields (druids will not wear armor or use shields made of metal)',
        'clubs', 'daggers', 'darts', 'javelins', 'maces', 'quarterstaffs',
        'scimitars', 'sickles', 'slings', 'spears')
    weapon_proficienies = (weapons.Club, weapons.Dagger, weapons.Dart,
                           weapons.Javelin, weapons.Mace, weapons.Quarterstaff,
                           weapons.Scimitar, weapons.Sickle, weapons.Sling, weapons.Spear)


class Fighter(Character):
    class_name = 'Fighter'
    hit_dice_faces = 10
    saving_throw_proficiencies = ('strength', 'constitution')
    _proficiencies_text = ('All armar', 'shields', 'simple weapons', 'martial weapons')
    weapon_proficienies = weapons.simple_weapons + weapons.martial_weapons


class Monk(Character):
    class_name = 'Monk'
    hit_dice_faces = 8
    saving_throw_proficiencies = ('strength', 'dexterity')
    _proficiencies_text = (
        'simple weapons', 'shortswords',
        "one type of artisan's tools or one musical instrument")
    weapon_proficienies = (weapons.Shortsword,) + weapons.simple_weapons


class Paladin(Character):
    class_name = 'Paladin'
    hit_dice_faces = 10
    saving_throw_proficiencies = ('wisdom', 'charisma')
    _proficiencies_text = ('All armor', 'shields', 'simple weapons',
                          'martial weapons')
    weapon_proficienies = weapons.simple_weapons + weapons.martial_weapons


class Ranger(Character):
    class_name = 'Ranger'
    hit_dice_faces = 10
    saving_throw_proficiencies = ('strength', 'dexterity')
    _proficiencies_text = ("light armor", "medium armor", "shields",
                           "simple weapons", "martial weapons")
    weapon_proficienies = weapons.simple_weapons + weapons.martial_weapons


class Rogue(Character):
    class_name = 'Rogue'
    hit_dice_faces = 8
    saving_throw_proficiencies = ('dexterity', 'intelligence')
    _proficiencies_text = (
        'light armor', 'simple weapons', 'hand crossbows', 'longswords',
        'rapiers', 'shortswords', "thieves' tools")
    weapon_proficienies = (weapons.HandCrossbow, weapons.Longsword,
                           weapons.Rapier, weapons.Shortsword) + weapons.simple_weapons


class Sorceror(Character):
    class_name = 'Sorceror'
    hit_dice_faces = 6
    saving_throw_proficiencies = ('constitution', 'charisma')
    _proficiencies_text = ('daggers', 'darts', 'slings',
                           'quarterstaffs', 'light crossbows')
    weapon_proficienies = (weapons.Dagger, weapons.Dart,
                           weapons.Sling, weapons.Quarterstaff,
                           weapons.LightCrossbow)


class Warlock(Character):
    class_name = 'Warlock'
    hit_dice_faces = 8
    saving_throw_proficiencies = ('wisdom', 'charisma')
    _proficiencies_text = ("light Armor", "simple weapons")
    weapon_proficienies = weapons.simple_weapons


class Wizard(Character):
    class_name = 'Wizard'
    hit_dice_faces = 6
    saving_throw_proficiencies = ('intelligence', 'wisdom')
    _proficiencies_text = ('daggers', 'darts', 'slings',
                          'quarterstaffs', 'light crossbows')
    weapon_proficienies = (weapons.Dagger, weapons.Dart,
                           weapons.Sling, weapons.Quarterstaff,
                           weapons.LightCrossbow)
