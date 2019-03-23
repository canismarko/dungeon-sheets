class Shield():
    """A shield that can be worn on one hand."""
    name = "Shield"
    cost = "10 gp"
    base_armor_class = 2
    
    def __str__(self):
        return self.name

    def __repr__(self):
        return "\"{:s}\"".format(self.name)

    @classmethod
    def improved_version(cls, bonus):
        bonus = int(bonus)
        
        class NewShield(cls):
            name = f'+{bonus} ' + cls.name
            base_armor_class = cls.base_armor_class + bonus
            
        return NewShield


class WoodenShield(Shield):
    name = 'Wooden shield'


class ShieldOfFaces(Shield):
    name = "Shield +1"
    base_armor_class = 3


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
    weight_class : str
      light, medium, or heavy
    weight : int
      In lbs.
    
    """
    name = "Unknown Armor"
    cost = "0 gp"
    base_armor_class = 10
    dexterity_mod_max = None
    strength_required = None
    stealth_disadvantage = False
    weight = 0  # In lbs
    
    def __str__(self):
        return self.name

    def __repr__(self):
        return "\"{:s}\"".format(self.name)

    @classmethod
    def improved_version(cls, bonus):
        bonus = int(bonus)
        
        class NewArmor(cls):
            name = f'+{bonus} ' + cls.name
            base_armor_class = cls.base_armor_class + bonus
            
        return NewArmor


class NoArmor(Armor):
    name = "No Armor"


class LightArmor(Armor):
    name = "Light Armor"


class MediumArmor(Armor):
    name = "Medium Armor"


class HeavyArmor(Armor):
    name = "Heavy Armor"


class PaddedArmor(LightArmor):
    name = "Padded Armor"
    cost = "5 gp"
    base_armor_class = 11
    weight = 8
    stealth_disadvantage = True


class LeatherArmor(LightArmor):
    name = "Leather Armor"
    cost = "10 gp"
    base_armor_class = 11
    weight = 10


class StuddedLeatherArmor(LightArmor):
    name = "Studded Leather Armor"
    cost = "45 gp"
    base_armor_class = 12
    weight = 13


class HideArmor(MediumArmor):
    name = "Hide Armor"
    cost = "10 gp"
    base_armor_class = 12
    dexterity_mod_max = 2
    weight = 12


class ChainShirt(MediumArmor):
    name = "Chain Shirt"
    cost = "50 gp"
    base_armor_class = 13
    dexterity_mod_max = 2
    weight = 20


class ScaleMail(MediumArmor):
    name = "Scale Mail"
    cost = "50 gp"
    base_armor_class = 14
    dexterity_mod_max = 2
    stealth_disadvantage = True
    weight = 45


class Breastplate(MediumArmor):
    name = "Breastplate"
    cost = "400 gp"
    base_armor_class = 14
    dexterity_mod_max = 2
    weight = 20


class HalfPlate(MediumArmor):
    name = "Half Plate"
    cost = "750 gp"
    base_armor_class = 15
    dexterity_mod_max = 2
    stealth_disadvantage = True
    weight = 40


class RingMail(HeavyArmor):
    name = "Ring Mail"
    cost = "30 gp"
    base_armor_class = 14
    dexterity_mod_max = 0
    stealth_disadvantage = True
    weight = 40


class ChainMail(HeavyArmor):
    name = "Chain Mail"
    cost = "75 gp"
    base_armor_class = 16
    dexterity_mod_max = 0
    strength_required = 13
    stealth_disadvantage = True
    weight = 55


class SplintArmor(HeavyArmor):
    name = "Splint Armor"
    cost = "200 gp"
    base_armor_class = 17
    dexterity_mod_max = 0
    strength_required = 15
    stealth_disadvantage = True
    weight = 60


class PlateMail(HeavyArmor):
    name = "Plate Mail"
    cost = "1,500 gp"
    base_armor_class = 18
    dexterity_mod_max = 0
    strength_required = 15
    stealth_disadvantage = True
    weight = 65


# Custom Armor
class ElvenChain(MediumArmor):
    name = 'Elven Chain'
    cost = '5,000 gp'
    base_armor_class = 14
    dexerity_mod_max = 2
    weight = 20
    

light_armors = [PaddedArmor, LeatherArmor, StuddedLeatherArmor]
medium_armors = [HideArmor, ChainShirt, ScaleMail, Breastplate, HalfPlate]
heavy_armors = [RingMail, ChainMail, SplintArmor, PlateMail]
all_armors = light_armors + medium_armors + heavy_armors
