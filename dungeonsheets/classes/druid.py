from ..stats import findattr
from .. import (weapons, monsters, exceptions, features)
from .classes import CharClass, SubClass
from collections import defaultdict
import warnings
import math


# PHB
class LandCircle(SubClass):
    """The Circle of the Land is made up of mystics and sages who safeguard
    ancient knowledge and rites through a vast oral tradition. These druids
    meet within sacred circles of trees or standing stones to whisper primal
    secrets in Druidic. The circle’s wisest members preside as the chief
    priests of communities that hold to the Old Faith and serve as advisors to
    the rulers of those folk. As a member of this circle, your magic is
    influenced by the land where you were initiated into the circle’s
    mysterious rites

    """
    name = "Circle of the Land"
    circle = "land"
    features_by_level = defaultdict(list)
    features_by_level[2] = [features.BonusCantrip, features.NaturalRecovery]
    features_by_level[3] = [features.CircleSpells]
    features_by_level[6] = [features.LandsStride]
    features_by_level[10] = [features.NaturesWard]
    features_by_level[14] = [features.NaturesSanctuary]


class MoonCircle(SubClass):
    """Druids of the Circle of the Moon are fierce guardians of the wilds. Their
    order gathers under the full moon to share news and trade warnings. They
    haunt the deepest parts of the wilderness, where they might go for weeks on
    end before crossing paths with another humanoid creature, let alone another
    druid.
    
    Changeable as the moon, a druid of this circle might prowl as a great cat
    one night, soar over the treetops as an eagle the next day, and crash
    through the undergrowth in bear form to drive off a trespassing
    monster. The wild is in the druid's blood.

    """
    name = "Circle of the Moon"
    circle = "moon"
    features_by_level = defaultdict(list)
    features_by_level[2] = [features.CombatWildShape, features.CircleForms]
    features_by_level[6] = [features.PrimalStrike]
    features_by_level[10] = [features.ElementalWildShape]
    features_by_level[14] = [features.ThousandForms]


# XGTE
class DreamsCircle(SubClass):
    """Druids who are members of the Circle of Dreams hail from regions that have
    strong ties to the Feywild and its dreamlike realms. The druids’
    guardianship of the natural world makes for a natural alliance between them
    and good-aligned fey. These druids seek to fill the world with dreamy
    wonder. Their magic mends wounds and brings joy to downcast hearts, and the
    realms they protect are gleaming, fruitful places, where dream and reality
    blur together and where the weary can find rest.

    """
    name = "Circle of Dreams"
    circle = "dreams"
    features_by_level = defaultdict(list)
    features_by_level[2] = [features.BalmOfTheSummerCourt]
    features_by_level[6] = [features.HearthOfMoonlightAndShadow]
    features_by_level[10] = [features.HiddenPaths]
    features_by_level[14] = [features.WalkerInDreams]


class ShepherdCircle(SubClass):
    """Druids of the Circle of the Shepherd commune with the spirits of nature,
    especially the spirits of beasts and the fey, and call to those spirits for
    aid. These druids recognize that all living things play a role in the
    natural world, yet they focus on protecting animals and fey creatures that
    have difficulty defending themselves. Shepherds, as they are known, see
    such creatures as their charges. They ward off monsters that threaten them,
    rebuke hunters who kill more prey than necessary, and prevent civilization
    from encroaching on rare animal habitats and on sites sacred to the
    fey. Many of these druids are happiest far from cities and towns, content
    to spend their days in the company of animals and the fey creatures of the
    wilds.

    Members of this circle become adventurers to oppose forces that threaten
    their charges or to seek knowledge and power that will help them safeguard
    their charges better. Wherever these druids go, the spirits of the wil—
    derness are with them

    """
    name = "Circle of the Shepherd"
    circle = "shepherd"
    languages = ('Sylvan',)
    features_by_level = defaultdict(list)
    features_by_level[2] = [features.SpeechOfTheWoods, features.SpiritTotem]
    features_by_level[6] = [features.MightySummoner]
    features_by_level[10] = [features.GuardianSpirit]
    features_by_level[14] = [features.FaithfulSummons]


class Druid(CharClass):
    name = 'Druid'
    _wild_shapes = ()
    _circle = ''
    hit_dice_faces = 8
    subclass_select_level = 2
    saving_throw_proficiencies = ('intelligence', 'wisdom')
    primary_abilities = ('wisdom',)
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
    multiclass_weapon_proficiencies = ()
    _multiclass_proficiencies_text = (
        'Light armor', 'medium armor',
        'shields (druids will not wear armor or use shields made of metal)')
    class_skill_choices = ('Arcana', 'Animal Handling', 'Insight',
                           'Medicine', 'Nature', 'Perception', 'Religion',
                           'Survival')
    features_by_level = defaultdict(list)
    features_by_level[2] = [features.WildShape]
    features_by_level[18] = [features.TimelessBody, features.BeastSpells]
    features_by_level[20] = [features.Archdruid]
    subclasses_available = (LandCircle, MoonCircle, DreamsCircle,
                            ShepherdCircle)
    spellcasting_ability = 'wisdom'
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

    def select_subclass(self, subclass_str):
        if subclass_str in ['', 'None', 'none', None]:
            return None
        for sc in self.subclasses_available:
            if ((subclass_str.lower() == sc.circle.lower())
                or (subclass_str.lower() in sc.name.lower())):
                return sc(owner=self.owner)
        return None

    @property
    def circle(self):
        if isinstance(self.subclass, SubClass):
            return self.subclass.circle.lower()
        else:
            return self._circle

    @circle.setter
    def circle(self, circle_str):
        if isinstance(self.subclass, SubClass):
            self.subclass = self.select_subclass(circle_str)
        else:
            self._circle = circle_str

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
        # Make adjustments for moon circle druids
        if self.circle == "moon":
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

