from collections import defaultdict

from dungeonsheets.features import Feature, FeatureSelector


class CharClass:
    """
    A generic Character Class (not to be confused with builtin class)
    """

    name = "Default"
    level = 1
    hit_dice_faces = 2
    subclass_select_level = 3
    weapon_proficiencies = ()
    _proficiencies_text = ()
    multiclass_weapon_proficiencies = ()
    _multiclass_proficiencies_text = ()
    saving_throw_proficiencies = ()
    primary_abilities = ()
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

    def __init__(self, level, owner=None, subclass=None, feature_choices=[], **params):
        self.level = level
        self.owner = owner
        # For ex: add "char.Monk" attribute
        setattr(self.owner, self.name, self)
        # Instantiate the features
        self.features_by_level = defaultdict(list)
        cls = type(self)
        for i in range(1, 21):
            fs = []
            for f in cls.features_by_level[i]:
                if issubclass(f, FeatureSelector):
                    fs.append(f(owner=self.owner, feature_choices=feature_choices))
                elif issubclass(f, Feature):
                    fs.append(f(owner=self.owner))
            self.features_by_level[i] = fs
        for k, v in params.items():
            setattr(self, k, v)
        self.spells_known = [S() for S in cls.spells_known]
        self.spells_prepared = [S() for S in cls.spells_prepared]

        # Apply subclass
        self.subclass = self.select_subclass(subclass)
        if isinstance(self.subclass, SubClass):
            self.apply_subclass(feature_choices=feature_choices)

    def select_subclass(self, subclass_str):
        """
        Return a SubClass object corresponding to given string.

        Intended to be replaced by classes so they can
        define their own methods of picking subclass by string.
        """
        if subclass_str in ["", "None", "none", None]:
            return None
        for sc in self.subclasses_available:
            if subclass_str.lower() in sc.name.lower():
                return sc(owner=self.owner)
        return None

    def apply_subclass(self, feature_choices=[]):
        if not isinstance(self.subclass, SubClass):
            return
        subcls = self.subclass
        for i in range(1, 21):
            fs = []
            for f in subcls.features_by_level[i]:
                if issubclass(f, FeatureSelector):
                    fs.append(f(owner=self.owner, feature_choices=feature_choices))
                elif issubclass(f, Feature):
                    fs.append(f(owner=self.owner))
            self.features_by_level[i].extend(fs)
        for attr in ("weapon_proficiencies", "_proficiencies_text"):
            new_list = tuple(getattr(self, attr, ())) + tuple(
                getattr(self.subclass, attr, ())
            )
            setattr(self, attr, new_list)
        # All subclass proficiencies transfer, regardless of if this is primary class
        self.multiclass_weapon_proficiencies += tuple(subcls.weapon_proficiencies)
        self._multiclass_proficiencies_text += tuple(subcls._proficiencies_text)
        self.spellcasting_ability = (
            self.spellcasting_ability or subcls.spellcasting_ability
        )
        self.spell_slots_by_level = (
            self.spell_slots_by_level or subcls.spell_slots_by_level
        )
        self.spells_known.extend([S() for S in subcls.spells_known])
        self.spells_prepared.extend([S() for S in subcls.spells_prepared])

    @property
    def features(self):
        features = ()
        for lvl in range(1, self.level + 1):
            features += tuple(self.features_by_level[lvl])
        return features

    @property
    def is_spellcaster(self):
        result = self.spellcasting_ability is not None
        return result

    def spell_slots(self, spell_level):
        """How many spells slots are available for this spell level."""
        if self.spell_slots_by_level is None:
            return 0
        else:
            return self.spell_slots_by_level[self.level][spell_level]

    def __str__(self):
        s = "Level {:d} {:s}".format(self.level, self.name)
        if isinstance(self.subclass, SubClass):
            s += " ({:s})".format(str(self.subclass))
        return s

    def __repr__(self):
        return '"{:s}"'.format(str(self))


class SubClass:
    """
    A generic subclass object. Add more detail in the __doc__ attribute.
    """

    name = ""
    features_by_level = defaultdict(list)
    weapon_proficiencies = ()
    _proficiencies_text = ()
    spellcasting_ability = None
    spell_slots_by_level = None
    spells_known = ()
    spells_prepared = ()

    def __init__(self, owner):
        self.owner = owner
        self.__doc__ = self.__doc__ or SubClass.__doc__

    def __str__(self):
        return self.name

    def __repr__(self):
        return '"{:s}"'.format(self.name)
