from unittest import TestCase


from dungeonsheets.content_registry import ContentRegistry
from dungeonsheets import monsters, weapons


class TestContentRegistry(TestCase):
    def test_add_module(self):
        creg = ContentRegistry()
        creg.add_module(monsters)
        self.assertEqual(len(creg.modules), 1)
        # Check if is indempotent
        creg.add_module(monsters)
        self.assertEqual(len(creg.modules), 1)

    def test_add_module_by_name(self):
        # Check that a module gets converted to a module instance
        creg = ContentRegistry()
        creg.add_module("dungeonsheets.monsters")
        self.assertEqual(len(creg.modules), 1)
        self.assertFalse(isinstance(creg.modules[0], str),
                         "String not converted to module.")
        # Check if is indempotent
        creg.add_module("dungeonsheets.monsters")
        self.assertEqual(len(creg.modules), 1)

    def test_findattr(self):
        """Check if the function can find attributes."""

        class TestClass:
            my_attr = 47
            YourAttr = 53

        test_module = TestClass()
        creg = ContentRegistry()
        creg.add_module(test_module)
        # Direct access
        self.assertEqual(creg.findattr("my_attr"), test_module.my_attr)
        self.assertEqual(creg.findattr("YourAttr"), test_module.YourAttr)
        # Swapping spaces for capitalization
        self.assertEqual(creg.findattr("my attr"), test_module.my_attr)
        self.assertEqual(creg.findattr("your attr"), test_module.YourAttr)
        # Check for extra functuation
        self.assertEqual(creg.findattr("my attr"), test_module.my_attr)
        self.assertEqual(creg.findattr("Your/Attr"), test_module.YourAttr)
        
    def test_findattr_valid_classes(self):
        """Check if the function can find attributes."""

        class TestClass:
            my_attr = 47
            YourAttr = 53

        class TestClassB:
            my_attr = 48.0

        test_module = TestClass()
        creg = ContentRegistry()
        creg.add_module(test_module)
        creg.add_module(TestClassB)
        # Direct access
        self.assertEqual(creg.findattr("my_attr", valid_classes=[int]), test_module.my_attr)
        
    def test_findattr_magic_weapon(self):
        creg = ContentRegistry()
        creg.add_module(weapons)
        # First test with a non-magical weapon
        shortsword = creg.findattr("shortsword")
        self.assertIs(shortsword, weapons.Shortsword)
        # Now test with a magical weapon
        magic_shortsword = creg.findattr("shortsword + 1")
        self.assertTrue(issubclass(magic_shortsword, weapons.Shortsword),
                        "Improved version is not subclass of base.")
        self.assertEqual(magic_shortsword.attack_bonus, 1)
        self.assertEqual(magic_shortsword.damage_bonus, 1)
        # Make sure some other item that can't be "improved" still works
        creg = ContentRegistry()
        creg.add_module(monsters)
        lich = creg.findattr("lich+1")
        self.assertIs(lich, monsters.Lich)
