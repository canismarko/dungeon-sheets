"""Tools for describing a player character."""

import re

from .stats import Stat
from .dice import read_dice_str

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
    # Base stats (ability scores
    strength = Stat()
    dexterity = Stat()
    constitution = Stat()
    intelligence = Stat()
    wisdom = Stat()
    charisma = Stat()
    # Inventory
    cp = 0
    sp = 0
    ep = 0
    gp = 0
    pp = 0
    
    def __init__(self, **attrs):
        """Takes a bunch of attrs and passes them to ``set_attrs``"""
        self.set_attrs(**attrs)
    
    def set_attrs(self, **attrs):
        """Bulk setting of attributes. Useful for loading a character from a
        dictionary."""
        for attr, val in attrs.items():
            setattr(self, attr, val)
                
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


class Bard(Character):
    class_name = 'Bard'
    hit_dice_faces = 8


class Cleric(Character):
    class_name = 'Cleric'
    hit_dice_faces = 8


class Druid(Character):
    class_name = 'Druid'
    hit_dice_faces = 8


class Fighter(Character):
    class_name = 'Fighter'
    hit_dice_faces = 10


class Monk(Character):
    class_name = 'Monk'
    hit_dice_faces = 8


class Paladin(Character):
    class_name = 'Paladin'
    hit_dice_faces = 10


class Ranger(Character):
    class_name = 'Ranger'
    hit_dice_faces = 10


class Rogue(Character):
    class_name = 'Rogue'
    hit_dice_faces = 8


class Sorceror(Character):
    class_name = 'Sorceror'
    hit_dice_faces = 6

class Warlock(Character):
    class_name = 'Warlock'
    hit_dice_faces = 8


class Wizard(Character):
    class_name = 'Wizard'
    hit_dice_faces = 6
