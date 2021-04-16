#!/usr/bin/env python

from unittest import TestCase

from dungeonsheets.character import Character
from dungeonsheets.weapons import Shortsword


class TestMulticlass(TestCase):
    """
    Tests for Multiclass character.
    """

    def test_constructor(self):
        char = Character(
            name="Multiclass", classes=["wizard", "fighter"], levels=[5, 4]
        )
        self.assertIsInstance(char, Character)

    def test_level(self):
        char = Character(
            name="Multiclass", classes=["wizard", "fighter"], levels=[5, 4]
        )
        self.assertEqual(char.level, 9)

    def test_spellcasting(self):
        char = Character(
            name="Multiclass", classes=["wizard", "fighter"], levels=[5, 4]
        )
        self.assertEqual(len(char.spellcasting_classes), 1)
        char = Character(
            name="Multiclass",
            classes=["wizard", "fighter"],
            subclasses=[None, "Eldritch Knight"],
            levels=[5, 4],
        )
        self.assertEqual(len(char.spellcasting_classes), 2)
        # equivalent spellcasting level: 6
        self.assertEqual(char.spell_slots(spell_level=1), 4)
        self.assertEqual(char.spell_slots(spell_level=2), 3)
        self.assertEqual(char.spell_slots(spell_level=3), 3)
        self.assertEqual(char.spell_slots(spell_level=4), 0)

    def test_proficiencies(self):
        char1 = Character(
            name="Multiclass", classes=["wizard", "fighter"], levels=[5, 4]
        )
        for svt in ("intelligence", "wisdom"):
            self.assertIn(svt, char1.saving_throw_proficiencies)
        char2 = Character(name="Multiclass", classes=["wizard", "rogue"], levels=[5, 4])
        char3 = Character(name="Multiclass", classes=["rogue", "wizard"], levels=[4, 5])
        sword = Shortsword()
        self.assertTrue(char1.is_proficient(sword))
        # multiclassing into Rogue doesn't give simple weapon proficiency
        self.assertFalse(char2.is_proficient(sword))
        self.assertTrue(char3.is_proficient(sword))
