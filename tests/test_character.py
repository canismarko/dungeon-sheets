#!/usr/bin/env python

from unittest import TestCase

from dungeonsheets import race
from dungeonsheets.character import Character, Wizard
from dungeonsheets.weapons import Weapon, Shortsword
from dungeonsheets.armor import Armor, LightLeatherArmor, Shield


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
        # Check that armor and shield gets set_attrs
        char.set_attrs(armor='light leather armor', shield='shield')
        self.assertFalse(isinstance(char.armor, str))
        self.assertFalse(isinstance(char.shield, str))
        # Check that race gets set to an object
        char.set_attrs(race='high elf')
        self.assertIsInstance(char.race, race.HighElf)
    
    def test_wield_weapon(self):
        char = Character()
        char.strength = 14
        char.weapon_proficiencies = [Shortsword]
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
        # Check if race weapon proficiencies are considered
        char.weapons = []
        char.weapon_proficiencies = []
        char.race = race.HighElf()
        char.wield_weapon('shortsword')
        sword = char.weapons[0]
        self.assertEqual(sword.attack_bonus, 5)
    
    def test_str(self):
        char = Wizard(name="Inara")
        self.assertEqual(str(char), 'Inara')
        self.assertEqual(repr(char), '<Wizard: Inara>')
    
    def test_is_proficient(self):
        char = Character()
        char.weapon_proficiencies
        sword = Shortsword()
        # Check for not-proficient weapon
        self.assertFalse(char.is_proficient(sword))
        # Check if we're proficient in the weapon
        char.weapon_proficiencies = [Shortsword]
        self.assertTrue(char.is_proficient(sword))
        # Now try it with a racial proficiency
        char.weapon_proficiencies = tuple()
        char.race = race.HighElf()
        self.assertTrue(char.is_proficient(sword))
    
    def test_proficiencies_text(self):
        char = Character()
        char._proficiencies_text = ('hello', 'world')
        self.assertEqual(char.proficiencies_text, 'Hello, world.')
        # Check for extra proficiencies
        char.proficiencies_extra = ("it's", "me")
        self.assertEqual(char.proficiencies_text, "Hello, world, it's, me.")
        # Check that race proficienceis are included
        elf = race.HighElf()
        char.race = elf
        expected = "Hello, world, longswords, shortswords, shortbows, longbows, it's, me."
        self.assertEqual(char.proficiencies_text, expected)
    
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
    
    def test_spell_slots(self):
        char = Wizard()
        # Wizard level 1
        char.level = 1
        self.assertEqual(char.spell_slots(spell_level=0), 3)
        self.assertEqual(char.spell_slots(spell_level=1), 2)
        self.assertEqual(char.spell_slots(spell_level=2), 0)
        # Wizard level 2
        char.level = 2
        self.assertEqual(char.spell_slots(spell_level=0), 3)
        self.assertEqual(char.spell_slots(spell_level=1), 3)
        self.assertEqual(char.spell_slots(spell_level=2), 0)
    
    def test_equip_armor(self):
        char = Character(dexterity=16)
        char.wear_armor('light leather armor')
        self.assertTrue(isinstance(char.armor, Armor))
        # Now make sure the armor class is correct
        self.assertEqual(char.armor_class, 14)
        # Try passing an Armor object directly
        char.wear_armor(LightLeatherArmor)
        self.assertEqual(char.armor_class, 14)
        # Test equipped armor with max dexterity mod_str
        char.armor.dexterity_mod_max = 1
        self.assertEqual(char.armor_class, 12)
    
    def test_wield_shield(self):
        char = Character(dexterity=16)
        char.wield_shield('shield')
        self.assertTrue(isinstance(char.shield, Shield), msg=char.shield)
        # Now make sure the armor class is correct
        self.assertEqual(char.armor_class, 15)
        # Try passing an Armor object directly
        char.wield_shield(Shield)
        self.assertEqual(char.armor_class, 15)
