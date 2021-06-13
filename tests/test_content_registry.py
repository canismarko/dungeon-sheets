from unittest import TestCase


from dungeonsheets.content_registry import ContentRegistry
from dungeonsheets import monsters


class TestContentRegistry(TestCase):
    def test_add_module(self):
        creg = ContentRegistry()
        creg.add_module(monsters)
        self.assertEqual(len(creg.modules), 1)
        # Check if is indempotent
        creg.add_module(monsters)
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
        
