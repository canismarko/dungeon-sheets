import unittest

from dungeonsheets import random_tables


class ChildTable(random_tables.RandomTable):
    """I'm a table too, but where is everyone else?"""
    name = "Child Table"


class ParentTable(random_tables.RandomTable):
    """Hello, world. I'm a table."""
    name = "Parent Table"
    subtables = [ChildTable]


class RandomTableTests(unittest.TestCase):
    def test_docstring(self):
        self.assertIn("Hello, world", ParentTable.__doc__)
        parent_table = ParentTable()
        self.assertIn("Hello, world", parent_table.__doc__)

    def test_subtables(self):
        # Check that docstrings are combined
        # parent_table = ParentTable()
        self.assertIn("**Child Table**", ParentTable.__doc__)
