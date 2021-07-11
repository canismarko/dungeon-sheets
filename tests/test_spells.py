#!/usr/bin/env python

from unittest import TestCase

from dungeonsheets import spells
from dungeonsheets.spells import create_spell, Spell, all_spells


class TestSpells(TestCase):
    """Tests for spells and spell-related activities."""

    def test_all_spells(self):
        # Make sure only spells are returned
        for ThisSpell in all_spells():
            self.assertTrue(
                isinstance(ThisSpell, type),
                f"``all_spells`` returned {ThisSpell} (not a class)",
            )
            self.assertTrue(
                issubclass(ThisSpell, Spell),
                f"``all_spells`` returned {ThisSpell} (not a spell)",
            )
        # Pick a couple of known spells to spot-check for
        all_the_spells = list(all_spells())
        self.assertIn(spells.MagicMissile, all_the_spells)
        self.assertIn(spells.Thunderwave, all_the_spells)

    def test_create_spell(self):
        NewSpell = create_spell(name="Hello world")
        self.assertTrue(issubclass(NewSpell, Spell))
        self.assertEqual(NewSpell.name, "Hello world")
        spell = NewSpell()
        print(spell, spell.__class__, type(spell))

    def test_spell_str(self):
        spell = Spell()
        spell.name = "My spell"
        self.assertEqual(str(spell), "My spell")
        # Try with a ritual
        spell.ritual = True
        self.assertEqual(str(spell), "My spell (R)")
        # Try with a ritual and a concentration
        spell.concentration = True
        self.assertEqual(str(spell), "My spell (R/C)")
        # Try with ritual/concentration/verbal/somatic
        spell.components = ("V", "S")
        self.assertEqual(str(spell), "My spell (V/S/R/C)")
        # # Try with material components with a cost
        spell.components = ("V", "S", "M")
        spell.materials = "A stone worth 50 GP"
        self.assertEqual(str(spell), "My spell (V/S/M/R/C/$)")

    def test_special_material(self):
        spell = Spell()
        # From revivify
        spell.materials = "Diamonds worth 300 gp, which the spell consumes"
        self.assertTrue(spell.special_material)
