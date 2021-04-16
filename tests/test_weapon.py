import unittest

from dungeonsheets.weapons import Weapon


class WeaponTestCase(unittest.TestCase):
    def test_weapon_damage(self):
        weapon = Weapon()
        weapon.base_damage = "1d6"
        self.assertEqual(weapon.damage, "1d6")
        # Now add some bonus damage
        weapon.damage_bonus = 2
        self.assertEqual(weapon.damage, "1d6+2")
