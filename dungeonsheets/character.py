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
    level = 1
    alignment = 'true neutral'
    xp = 0
    armor_class = 10
    speed = 30 # In feet
    # Hit points
    hp_max = 10
    hit_dice_num = 1
    hit_dice_faces = 8
    # Base stats (ability scores
    strength = Stat()
    dexterity = Stat()
    constitution = Stat()
    intelligence = Stat()
    wisdom = Stat()
    charisma = Stat()

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
        return f"{self.hit_dice_num}d{self.hit_dice_faces}"
    
    @hit_dice.setter
    def hit_dice(self, val):
        dice = read_dice_str(val)
        self.hit_dice_faces = dice.faces
        self.hit_dice_num = dice.num
