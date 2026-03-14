import unittest


from dungeonsheets.stats import Ability
from dungeonsheets import magic_items
from dungeonsheets.character import Character
from dungeonsheets.content_registry import find_content


class MyMagicItem(magic_items.MagicItem): ...


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

    def test_staff_of_the_adder_registration_and_attributes(self):
        item_cls = find_content("staff of the adder")
        self.assertIs(item_cls, magic_items.StaffOfTheAdder)

        item = item_cls()
        self.assertEqual(item.name, "Staff of the Adder")
        self.assertEqual(item.rarity, "Uncommon")
        self.assertTrue(item.requires_attunement)
        self.assertEqual(item.item_type, "Staff")
