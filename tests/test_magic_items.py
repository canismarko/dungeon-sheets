import unittest


from dungeonsheets.stats import Ability
from dungeonsheets import magic_items
from dungeonsheets.character import Character


class MyMagicItem(magic_items.MagicItem):
    ...


class MagicItemTests(unittest.TestCase):
    def test_st_bonus_all(self):
        char = Character()
        my_item = MyMagicItem(wielder=char)
        char.magic_items = [my_item]
        # Test an item that confers no saving throw bonus
        bonus = my_item.st_bonus()
        self.assertEqual(bonus, 0)
        # Now test with positive ST bonus
        my_item.st_bonus_all = 2
        bonus = my_item.st_bonus()
        self.assertEqual(bonus, 2)

    def test_st_bonus_by_ability(self):
        char = Character(strength=10)
        my_item = MyMagicItem(wielder=char)
        char.magic_items = [my_item]
        # Test an item with nonsense ability
        with self.assertRaises(AttributeError):
            my_item.st_bonus(ability="flight")
        # Test that the st_bonus_all is used if the specific ability is not listed
        my_item.st_bonus_all = 2
        bonus = my_item.st_bonus(ability="strength")
        self.assertEqual(bonus, 2)
        # Test a specific st_bonus
        my_item.st_bonus_strength = 3
        bonus = my_item.st_bonus(ability="strength")
        self.assertEqual(bonus, 3)
