from .features import Feature


# PHB
class GreatWeaponMaster(Feature):
    """You’ve learned to put the weight of a weapon to your advantage, letting its
    momentum empower your strikes. You gain the following benefits:

    -- On your turn, when you score a critical hit with a melee weapon or
    reduce a creature to 0 hit points with one, you can make one melee weapon
    attack as a bonus action.

    -- Before you make a melee attack with a heavy weapon that you are
    proficient with, you can choose to take a -5 penalty to the attack
    roll. If the attack hits, you add +10 to the attack’s damage

    """
    name = "Great Weapon Master"
    source = "Feats"


class Actor(Feature):
    """Skilled at mimicry and dramatics, you gain the following benefits:

    -- Increase your Charisma score by 1, to a maximum of 20.

    -- You have an advantage on Charisma (Deception) and Charisma (Performance) checks when trying to pass yourself off as a different person.

    --You can mimic the speech of another person or the sounds made by other
    creatures. You must have heard the person speaking, or heard the creature
    make the sound, for at least 1 minute. A successful Wisdom (Insight) check
    contested by your Charisma (Deception) check allows a listener to determine
    that the effect is faked.

    """
    name = "Actor"
    source = "Feats"
