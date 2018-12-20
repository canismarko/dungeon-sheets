from ..stats import findattr
from .. import (weapons, monsters, exceptions)
from .. import features as feats
from .classes import CharClass
import warnings
import math


class Druid(CharClass):
    class_name = 'Druid'
    circle = ""  # moon, land
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
                            weapons.Javelin, weapons.Mace,
                            weapons.Quarterstaff, weapons.Scimitar,
                            weapons.Sickle, weapons.Sling, weapons.Spear)
    class_skill_choices = ('Arcana', 'Animal Handling', 'Insight',
                           'Medicine', 'Nature', 'Perception', 'Religion',
                           'Survival')
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

    def __init__(self, level, subclass=None, **params):
        if subclass is not None:
            sc = str(subclass).lower()
            if 'moon' in sc:
                self.circle = 'moon'
                params.pop('circle', '')
            elif 'land' in sc:
                self.circle = 'land'
                params.pop('circle', '')
        super().__init__(level, **params)
        
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
        if self.class_level < 2:
            max_cr = -1
            max_swim = 0
            max_fly = 0
        elif self.class_level < 4:
            max_cr = 1/4
            max_swim = 0
            max_fly = 0
        elif self.class_level < 8:
            max_cr = 1/2
            max_swim = None
            max_fly = 0
        else:
            max_cr = 1
            max_swim = None
            max_fly = None
        # Make adjustments for moon circle druids
        if self.circle.lower() == "moon":
            if 2 <= self.class_level < 6:
                max_cr = 1
            elif self.class_level >= 6:
                max_cr = math.floor(self.class_level / 3)
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

