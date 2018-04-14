class Shield():
    """A shield that can be worn on one hand."""
    name = "Shield"
    cost = "10 gp"
    base_armor_class = 2
    
    def __str__(self):
        return self.name


class NoShield(Shield):
    """If a character is carrying no shield."""
    name = "No shield"
    cost = "0"
    base_armor_class = 0
    
    def __str__(self):
        return self.name


class Armor():
    """A piece of armor that can be worn.
    
    Attributes
    ----------
    name : str
      Human-readable name for this armor.
    cost : str
      Cost and currency for this armor.
    base_armor_class : int
      Armor class granted before modifiers.
    dexterity_mod_max : int
      How much dexterity can the user contribute. ``0`` for no
      dexterity modifier, ``None`` for unlimited dexterity modifier.
    strength_required : int
      Minimum strength needed to use this armor properly.
    stealth_disadvantage : bool
      If true, the armor causes disadvantage on stealth rolls.
    weight : int
      In lbs.
    
    """
    name = "Unknown Armor"
    cost = "0 gp"
    base_armor_class = 10
    dexterity_mod_max = None
    strength_required = None
    stealth_disadvantage = False
    weight = 0 # In lbs
    
    def __str__(self):
        return self.name


class NoArmor(Armor):
    name = "No armor"


class LightPaddedArmor(Armor):
    name = "Light padded armor"
    cost = "5 gp"
    base_armor_class = 11
    weight = 8
    stealth_disadvantage = True


class LightLeatherArmor(Armor):
    name = "Light leather armor"
    cost = "10 gp"
    base_armor_class = 11
    weight = 10


class LightStuddedArmor(Armor):
    name = "Light studded armor"
    cost = "45 gp"
    base_armor_class = 12
    weight = 13


class MediumHideArmor(Armor):
    name = "Medium hide armor"
    cost = "10 gp"
    base_armor_class = 12
    dexterity_mod_max = 2
    weight = 12


class MediumChainShirtArmor(Armor):
    name = "Medium chain shirt armor"
    cost = "50 gp"
    base_armor_class = 13
    dexterity_mod_max = 2
    weight = 20


class MediumScaleMailArmor(Armor):
    name = "Medium scale mail armor"
    cost = "50 gp"
    base_armor_class = 14
    dexterity_mod_max = 2
    stealth_disadvantage = True
    weight = 45


class MediumBrassplateArmor(Armor):
    name = "Medium brassplate armor"
    cost = "400 gp"
    base_armor_class = 14
    dexterity_mod_max = 2
    weight = 20


class MediumHalfPlateArmor(Armor):
    name = "Medium half plate armor"
    cost = "750 gp"
    base_armor_class = 15
    dexterity_mod_max = 2
    stealth_disadvantage = True
    weight = 40


class HeavyRingMailArmor(Armor):
    name = "Heavy ring mail armor"
    cost = "30 gp"
    base_armor_class = 14
    dexterity_mod_max = 0
    stealth_disadvantage = True
    weight = 40


class HeavyChainMailArmor(Armor):
    name = "Heavy chain mail armor"
    cost = "75 gp"
    base_armor_class = 16
    dexterity_mod_max = 0
    strength_required = 13
    stealth_disadvantage = True
    weight = 55


class HeavySplintArmor(Armor):
    name = "Heavy splint armor"
    cost = "200 gp"
    base_armor_class = 17
    dexterity_mod_max = 0
    strength_required = 15
    stealth_disadvantage = True
    weight = 60


class HeavyPlateArmor(Armor):
    name = "Heavy splint armor"
    cost = "1,500 gp"
    base_armor_class = 18
    dexterity_mod_max = 0
    strength_required = 15
    stealth_disadvantage = True
    weight = 65
