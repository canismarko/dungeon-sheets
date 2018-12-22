from collections import defaultdict
from ..features import Feature, FeatureSelector


class CharClass():
    """
    A generic Character Class (not to be confused with builtin class)
    """
    name = "Default"
    level = 1
    hit_dice_faces = 2
    weapon_proficiencies = ()
    _proficiencies_text = ()
    multiclass_weapon_proficiencies = ()
    _multiclass_proficiencies_text = ()
    languages = ()
    class_skill_choices = ()
    num_skill_choices = 2
    spellcasting_ability = None
    spell_slots_by_level = None
    spells_known = ()
    spells_prepared = ()
    subclass = None
    subclasses_available = ()
    features_by_level = defaultdict(list)

    def __init__(self, level, subclass=None, feature_choices=[],
                 **params):
        self.level = level
        # Instantiate the features
        self.features_by_level = defaultdict(list)
        cls = type(self)
        for i in range(1, 21):
            fs = []
            for f in cls.features_by_level[i]:
                if issubclass(f, FeatureSelector):
                    fs.append(f(feature_choices=feature_choices))
                elif issubclass(f, Feature):
                    fs.append(f())
            fs = [f() for f in cls.features_by_level[i]]
            self.features_by_level[i] = fs
        for k, v in params.items():
            setattr(self, k, v)

        # Apply subclass
        self.subclass = self.select_subclass(subclass)
        if isinstance(self.subclass, SubClass):
            self.apply_subclass()

    def select_subclass(self, subclass_str):
        """
        Return a SubClass object corresponding to given string.
        
        Intended to be replaced by classes so they can 
        define their own methods of picking subclass by string.
        """
        if subclass_str in ['', 'None', 'none', None]:
            return None
        for sc in self.subclasses_available:
            if subclass_str.lower() in sc.name.lower():
                return sc(level=self.level)
        return None

    def apply_subclass(self):
        if self.subclass is None:
            return
        for i in range(1, 21):
            self.features_by_level[i] += ([f() for f in
                                           self.subclass.features_by_level[i]])
        for attr in ('weapon_proficiencies', '_proficiencies_text',
                     'spells_known', 'spells_prepared'):
            new_list = getattr(self, attr, ()) + getattr(self.subclass, attr, ())
            setattr(self, attr, new_list)
        # All subclass proficiencies transfer, regardless of if this is primary class
        self.multiclass_weapon_proficiencies += (self.subclass.weapon_proficiencies)
        self._multiclass_proficiencies_text += (self._proficiencies_text)
        self.spellcasting_ability = (self.spellcasting_ability or
                                     self.subclass.spellcasting_ability)
        self.spell_slots_by_level = (self.spell_slots_by_level or
                                     self.subclass.spell_slots_by_level)
    
    @property
    def features(self):
        features = ()
        for lvl in range(1, self.level+1):
            features += tuple(self.features_by_level[lvl])
        return features

    @property
    def is_spellcaster(self):
        result = (self.spellcasting_ability is not None)
        return result
    
    def spell_slots(self, spell_level):
        """How many spells slots are available for this spell level."""
        if self.spell_slots_by_level is None:
            return 0
        else:
            return self.spell_slots_by_level[self.level][spell_level]


class SubClass():
    """
    A generic subclass object. Add more detail in the __doc__ attribute.
    """
    name = ''
    features_by_level = defaultdict(list)
    weapon_proficiencies = ()
    _proficiencies_text = ()
    spellcasting_ability = None
    spell_slots_by_level = None
    spells_known = ()
    spells_prepared = ()

    def __init__(self, level):
        self.__doc__ = self.__doc__ or SubClass.__doc__
        self.level = level

    def __str__(self):
        return self.name

    def __repr__(self):
        return "\"{:s}\"".format(self.name)
