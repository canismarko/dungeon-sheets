from collections import defaultdict


class CharClass():
    """
    A generic Character Class (not to be confused with builtin class)
    """
    class_name = ""
    class_level = 1
    hit_dice_faces = None
    weapon_proficiencies = ()
    _proficiencies_text = ()
    multiclass_weapon_proficiencies = ()
    _multiclass_proficiencies_text = ()
    languages = ()
    class_skill_choices = ()
    num_skill_choices = 2
    spellcasting_ability = None
    spell_slots_by_level = None
    subclass = None
    features_by_level = defaultdict(list)

    def __init__(self, level, subclass=None, **params):
        self.class_level = level
        self.subclass = subclass
        for k, v in params.items():
            setattr(self, k, v)
            
    @property
    def features(self):
        features = ()
        for lvl in range(1, self.class_level+1):
            features += tuple(self.features_by_level[lvl])
            if self.subclass is not None and not isinstance(self.subclass, str):
                features += tuple(self.subclass.features_by_level[lvl])
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
            return self.spell_slots_by_level[self.class_level][spell_level]