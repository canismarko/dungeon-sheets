#!/usr/bin/env python

from unittest import TestCase

from dungeonsheets.character import Character
from dungeonsheets.weapons import Weapon, Shortsword


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
        # Check that the weapons get loaded as objects not string
        char.set_attrs(weapons=['shortsword'])
        self.assertEqual(len(char.weapons), 1)
        self.assertTrue(isinstance(char.weapons[0], Shortsword))
    
    def test_wield_weapon(self):
        char = Character()
        char.strength = 14
        char.weapon_proficienies = [Shortsword]
        # Add a weapon
        char.wield_weapon('shortsword')
        self.assertEqual(len(char.weapons), 1)
        sword = char.weapons[0]
        self.assertTrue(isinstance(sword, Weapon))
        self.assertTrue(isinstance(sword, Shortsword))
        self.assertEqual(sword.attack_bonus, 4) # str + prof
        self.assertEqual(sword.bonus_damage, 2) # str
        # Check if dexterity is used if it's higher (Finesse weapon)
        char.weapons = []
        char.dexterity = 16
        char.wield_weapon('shortsword')
        sword = char.weapons[0]
        self.assertEqual(sword.attack_bonus, 5) # dex + prof

    def test_proficiencies_text(self):
        char = Character()
        char._proficiencies_text = ('hello', 'world')
        self.assertEqual(char.proficiencies_text, 'Hello, world.')
        # Check for extra proficiencies
        char.proficiencies_extra = ("it's", "me")
        self.assertEqual(char.proficiencies_text, "Hello, world, it's, me.")
    
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
