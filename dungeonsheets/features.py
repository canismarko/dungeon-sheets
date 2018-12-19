from . import weapons, armor


class Feature():
    """
    Provide full text of rules in documentation
    """
    name = "Generic Feature"
    source = ''  # race, class, background, etc.

    def weapon_func(self, weapon: weapons.Weapon, **kwargs):
        """
        Return the attack/damage bonus from having this feature

        Parameters
        ----------
        weapon
           The weapon to be tested for special bonuses
        kwargs
           Any other key-word arguments the function may require

        Returns
        -------
        attack bonus : integer attack bonus
        damage bonus : integer attack bonus

        """
        return (0, 0)

    def AC_func(self, char, **kwargs):
        """
        Return the alternative AC from having this feat

        The character will take max AC from all available feats / standard AC,
        so the default is to output very low AC

        Parameters
        ----------
        char
           Character object, to check for necessary abilities, etc.
        kwargs
           Any other key-word arguments the function may require

        Returns
        -------
        AC : integer armor class from this feature
        """
        return -100


class Archery(Feature):
    """
    You gain a +2 bonus to attack rolls you make
    with ranged weapons.
    """
    name = "Archery"
    source = 'Revised Ranger'

    def weapon_func(self, weapon: weapons.Weapon):
        """
        +2 attack roll bonus if weapon is ranged
        """
        return (2, 0) if weapon.is_ranged else (0, 0)


class UnarmoredDefense(Feature):
    """Beginning at 1st level, while you are wearing no armor and not wearing a
    shield, your AC equals 10 + your Dexterity modifier + your Wisdom modifier.

    """
    name = "Unarmored Defense"
    source = "Monk"

    def AC_func(self, char):
        no_armor = ((char.armor is None)
                    or (isinstance(char.armor, armor.NoAmor)))
        no_shield = ((char.shield is None)
                     or (isinstance(char.shield, armor.NoShield)))
        if no_armor and no_shield:
            return 10 + char.dexterity.modifier + char.wisdom.modifier
        else:
            return -100
