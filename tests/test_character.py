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
        char.hit_dice_faces = 10
        char.hit_dice_num = 2
        self.assertEqual(char.hit_dice, '2d10')
        # Test the setter
        char.hit_dice = '3d12'
        self.assertEqual(char.hit_dice_faces, 12)
        self.assertEqual(char.hit_dice_num, 3)
    
    def test_set_attrs(self):
        char = Character()
        char.set_attrs(name='Inara')
        self.assertEqual(char.name, 'Inara')
