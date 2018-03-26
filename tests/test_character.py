#!/usr/bin/env python

from unittest import TestCase

from dungeonsheets.character import Character

class TestCharacter(TestCase):
    """Tests for the generic character base class."""
    
    def test_constructor(self):
        char = Character(name="Inara")
    
    def test_hit_dice(self):
        # Test the getter
        char = Character()
        char.level = 2
        char.hit_dice_faces = 10
        self.assertEqual(char.hit_dice, '2d10')
    
    def test_set_attrs(self):
        char = Character()
        char.set_attrs(name='Inara')
        self.assertEqual(char.name, 'Inara')
    
    def test_proficiency_bonus(self):
        char = Character()
        char.level = 1
        self.assertEqual(char.proficiency_bonus, 2)
        char.level = 4
        self.assertEqual(char.proficiency_bonus, 2)
        char.level = 5
        self.assertEqual(char.proficiency_bonus, 3)
        char.level = 8
        self.assertEqual(char.proficiency_bonus, 3)
        char.level = 9
        self.assertEqual(char.proficiency_bonus, 4)
        char.level = 12
        self.assertEqual(char.proficiency_bonus, 4)
        char.level = 13
        self.assertEqual(char.proficiency_bonus, 5)
        char.level = 16
        self.assertEqual(char.proficiency_bonus, 5)
        char.level = 17
        self.assertEqual(char.proficiency_bonus, 6)
        char.level = 20
        self.assertEqual(char.proficiency_bonus, 6)
