import unittest

from dungeonsheets.magic_items import MagicItem
from dungeonsheets.weapons import Weapon


class WeaponTestCase(unittest.TestCase):
    def test_weapon_damage(self):
        weapon = Weapon()
        weapon.base_damage = "1d6"
        self.assertEqual(weapon.damage, "1d6")
        # Now add some bonus damage
        weapon.damage_bonus = 2
        self.assertEqual(weapon.damage, "1d6+2")


class MagicWeaponTestCase(unittest.TestCase):
    """Check that a magic weapon works as intended."""
    def test_class_inheritance_weapon_first(self):
        """Test that the class inheritance works correctly for multiclassing."""
        MagicWeapon = type("MagicWeapon", (Weapon, MagicItem),
                           dict(damage_bonus=2, attack_bonus=2,
                                st_bonus_all=3))
        weapon = MagicWeapon(wielder=None)
        # CHeck some weapon traits
        self.assertEqual(weapon.damage, "1d4+2")
        # Check some magic item traits
        self.assertEqual(weapon.st_bonus_all, 3)
    
    def test_class_inheritance_magic_item_first(self):
        """Test that the class inheritance works correctly for multiclassing."""
        MagicWeapon = type("MagicWeapon", (MagicItem, Weapon),
                           dict(damage_bonus=2, attack_bonus=2,
                                st_bonus_all=3))
        weapon = MagicWeapon(wielder=None)
        # CHeck some weapon traits
        self.assertEqual(weapon.damage, "1d4+2")
        # Check some magic item traits
        self.assertEqual(weapon.st_bonus_all, 3)
