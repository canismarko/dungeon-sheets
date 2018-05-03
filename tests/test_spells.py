#!/usr/bin/env python

from unittest import TestCase

from dungeonsheets.spells import create_spell, Spell


class TestSpells(TestCase):
    """Tests for spells and spell-related activities."""
    
    def test_create_spell(self):
        NewSpell = create_spell(name="Hello world")
        self.assertTrue(issubclass(NewSpell, Spell))
        self.assertEqual(NewSpell.name, 'Hello world')
        spell = NewSpell()
        print(spell, spell.__class__, type(spell))

    def test_spell_str(self):
        spell = Spell()
        spell.name = "My spell"
        self.assertEqual(str(spell), 'My spell')
        # Try with a ritual
        spell.ritual = True
        self.assertEqual(str(spell), 'My spell (R)')
        # Try with a ritual and a concentration
        spell.concentration = True
        self.assertEqual(str(spell), 'My spell (R, C)')
