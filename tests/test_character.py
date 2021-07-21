#!/usr/bin/env python

from unittest import TestCase, expectedFailure
import warnings

from dungeonsheets import race, monsters, exceptions, spells, infusions
from dungeonsheets.character import (
    Character,
    Wizard,
    Druid,
)
from dungeonsheets.weapons import Weapon, Shortsword
from dungeonsheets.armor import Armor, LeatherArmor, Shield


class TestCharacter(TestCase):
    """Tests for the generic character base class."""

    def test_constructor(self):
        char = Character(name="Inara")
        self.assertIsInstance(char, Character)

    def test_hit_dice(self):
        # Test the getter
        char = Character()
        char.level = 2
        char.hit_dice_faces = 10
        self.assertEqual(char.hit_dice, "2d10")

    def test_max_hp(self):
        char = Wizard(level=3, constitution=12)
        self.assertEqual(char.hp_max, 17)

    def test_set_attrs(self):
        char = Character()
        char.set_attrs(name="Inara")
        self.assertEqual(char.name, "Inara")
        # Check that the weapons get loaded as objects not string
        char.set_attrs(weapons=["shortsword"])
        self.assertEqual(len(char.weapons), 1)
        self.assertTrue(isinstance(char.weapons[0], Shortsword))
        # Check that armor and shield gets set_attrs
        char.set_attrs(armor="leather armor", shield="shield")
        self.assertFalse(isinstance(char.armor, str))
        self.assertFalse(isinstance(char.shield, str))
        # Check that race gets set to an object
        char.set_attrs(race="high elf")
        self.assertIsInstance(char.race, race.HighElf)
        # Check inspiration works
        char.set_attrs(inspiration=True)
        self.assertTrue(char.inspiration)
        char.set_attrs(inspiration=False)
        self.assertFalse(char.inspiration)

    def test_homebrew_spells(self):
        char = Character()

        class MySpell(spells.Spell):
            name = "my spell!"

        char.set_attrs(spells=(MySpell,))
        self.assertIsInstance(char.spells[0], spells.Spell)
        self.assertEqual(char.spells[0].name, "my spell!")

    def test_homebrew_infusions(self):
        char = Character(classes="artificer")

        class MyInfusion(infusions.Infusion):
            name = "my infusion!"

        # Pass an already created infusion class
        char.set_attrs(infusions=(MyInfusion,))
        self.assertIsInstance(char.infusions[0], infusions.Infusion)
        self.assertEqual(char.infusions[0].name, "my infusion!")
        # Pass a previously undefined infusion
        char = Character(classes="artificer")
        char.set_attrs(infusions=("spam_infusion",))
        self.assertIsInstance(char.infusions[0], infusions.Infusion)
        self.assertEqual(char.infusions[0].name, "Spam Infusion")

    def test_resolve_mechanic(self):
        # Test a well defined mechanic
        NewSpell = Character._resolve_mechanic("mage_hand", None)
        self.assertTrue(issubclass(NewSpell, spells.Spell))

        # Test an unknown mechanic
        def new_spell(**params):
            return spells.Spell

        NewSpell = Character._resolve_mechanic("hocus_pocus", spells.Spell)
        self.assertTrue(issubclass(NewSpell, spells.Spell))

        # Test direct resolution of a proper subclass
        class MySpell(spells.Spell):
            pass

        NewSpell = Character._resolve_mechanic(MySpell, spells.Spell)

    def test_wield_weapon(self):
        char = Character()
        char.strength = 14
        char.weapon_proficiencies = [Shortsword]
        # Add a weapon
        char.wield_weapon("shortsword")
        self.assertEqual(len(char.weapons), 1)
        sword = char.weapons[0]
        self.assertTrue(isinstance(sword, Weapon))
        self.assertTrue(isinstance(sword, Shortsword))
        self.assertEqual(sword.attack_modifier, 4)  # str + prof
        self.assertEqual(sword.damage, "1d6+2")  # str
        # Check if dexterity is used if it's higher (Finesse weapon)
        char._weapons = []
        char.dexterity = 16
        char.wield_weapon("shortsword")
        sword = char.weapons[0]
        self.assertEqual(sword.attack_modifier, 5)  # dex + prof
        # Check if race weapon proficiencies are considered
        char._weapons = []
        char.weapon_proficiencies = []
        char.race = race.HighElf()
        char.wield_weapon("shortsword")
        sword = char.weapons[0]
        self.assertEqual(sword.attack_modifier, 5)

    def test_str(self):
        char = Wizard(name="Inara")
        self.assertEqual(str(char), "Inara")
        self.assertEqual(repr(char), "<Wizard: Inara>")

    def test_is_proficient(self):
        char = Character(classes=["Wizard"])
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
        char._proficiencies_text = ("hello", "world")
        self.assertIn("hello", char.proficiencies_text.lower())
        self.assertIn("world", char.proficiencies_text.lower())
        # Check for extra proficiencies
        char._proficiencies_text += ("it's", "me")
        self.assertIn("it's", char.proficiencies_text.lower())
        self.assertIn("me", char.proficiencies_text.lower())
        # Check that race proficienceis are included
        elf = race.HighElf()
        char.race = elf
        expected = (
            "hello",
            "world",
            "longswords",
            "shortswords",
            "shortbows",
            "longbows",
            "it's",
            "me",
        )
        for e in expected:
            self.assertIn(e, char.proficiencies_text.lower())

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
        char.wear_armor("leather armor")
        self.assertTrue(isinstance(char.armor, Armor))
        # Now make sure the armor class is correct
        self.assertEqual(char.armor_class, 14)
        # Try passing an Armor object directly
        char.wear_armor(LeatherArmor())
        self.assertEqual(char.armor_class, 14)
        # Test equipped armor with max dexterity mod_str
        char.armor.dexterity_mod_max = 1
        self.assertEqual(char.armor_class, 12)

    def test_wield_shield(self):
        char = Character(dexterity=16)
        char.wield_shield("shield")
        self.assertTrue(isinstance(char.shield, Shield), msg=char.shield)
        # Now make sure the armor class is correct
        self.assertEqual(char.armor_class, 15)
        # Try passing an Armor object directly
        char.wield_shield(Shield)
        self.assertEqual(char.armor_class, 15)

    def test_speed(self):
        # Check that the speed pulls from the character's race
        char = Character(race="lightfoot halfling")
        self.assertEqual(char.speed, "25")
        # Check that a character with no race defaults to 30 feet
        char = Character()
        char.race = None
        self.assertEqual(char.speed, "30")

    def test_load_char(self):
        char = Character.load({"name": "Dave", "sheet_type": "character"})
        self.assertFalse(hasattr(char, "sheet_type"),
                         "'sheet_type' not stripped from char props")


class DruidTestCase(TestCase):
    def test_learned_spells(self):
        """For a druid, learning spells is not necessary and this field should
        be ignored."""
        char = Druid()
        with warnings.catch_warnings():
            warnings.filterwarnings("ignore", message="Druids cannot learn spells")
            char.set_attrs(spells=["invisibility"], spells_prepared=["druidcraft"])
        # self.assertEqual(len(char.spells), 1)
        self.assertEqual(len(char.spells), 2)
        self.assertIn(spells.Druidcraft(), char.spells)

    def test_wild_shapes(self):
        char = Druid()
        # Druid level 2
        char.level = 2
        # Set reasonable wild shapes
        char.wild_shapes = ["Wolf"]
        self.assertIsInstance(char.wild_shapes[0], monsters.Wolf)
        # Check what happens if a non-existent wild_shape is added
        with self.assertRaises(exceptions.MonsterError):
            char.wild_shapes = ["Wolf", "Hyperion Loader"]
        # Check what happens if a valid monster class is directly added
        char.wild_shapes = [
            monsters.Wolf(),
        ]
        self.assertIsInstance(char.wild_shapes[0], monsters.Wolf)
        # Check that invalid monsters aren't accepted
        char.wild_shapes = ["Wolf", "giant eagle"]
        self.assertEqual(len(char.wild_shapes), 1)
        self.assertIsInstance(char.wild_shapes[0], monsters.Wolf)

    def test_moon_druid_wild_shapes(self):
        # Moon druid level 2 gets beasts up to CR 1
        char = Druid(level=2, wild_shapes=["Ape"], circle="moon")
        self.assertEqual(len(char.wild_shapes), 1)
        self.assertIsInstance(char.wild_shapes[0], monsters.Ape)
        # Moon druid above level 6 gets beasts up to CR level / 3
        char = Druid(level=9, wild_shapes=["ankylosaurus"], circle="moon")
        self.assertEqual(len(char.wild_shapes), 1)
        self.assertIsInstance(char.wild_shapes[0], monsters.Ankylosaurus)

    def test_can_assume_shape(self):
        class Beast(monsters.Monster):
            description = "beast"

        new_druid = Druid(level=1)
        low_druid = Druid(level=2)
        mid_druid = Druid(level=4)
        high_druid = Druid(level=8)
        beast = Beast()
        # Check that level 1 druid automatically fails
        self.assertFalse(new_druid.can_assume_shape(beast))
        # Check if a basic beast can be transformed
        self.assertTrue(low_druid.can_assume_shape(beast))
        # Check that challenge rating is checked
        hard_beast = Beast()
        hard_beast.challenge_rating = 1 / 2
        really_hard_beast = Beast()
        really_hard_beast.challenge_rating = 1
        self.assertFalse(low_druid.can_assume_shape(hard_beast))
        self.assertFalse(low_druid.can_assume_shape(really_hard_beast))
        self.assertTrue(mid_druid.can_assume_shape(hard_beast))
        self.assertFalse(mid_druid.can_assume_shape(really_hard_beast))
        self.assertTrue(high_druid.can_assume_shape(hard_beast))
        self.assertTrue(high_druid.can_assume_shape(really_hard_beast))
        # Check that swim speed is enforced
        swim_beast = Beast()
        swim_beast.swim_speed = 15
        self.assertFalse(low_druid.can_assume_shape(swim_beast))
        self.assertTrue(mid_druid.can_assume_shape(swim_beast))
        self.assertTrue(high_druid.can_assume_shape(swim_beast))
        # Check that fly speed is enforced
        fly_beast = Beast()
        fly_beast.fly_speed = 15
        self.assertFalse(low_druid.can_assume_shape(fly_beast))
        self.assertFalse(mid_druid.can_assume_shape(fly_beast))
        self.assertTrue(high_druid.can_assume_shape(fly_beast))
        # Check that non-beasts are not allowed
        not_beast = monsters.Monster()
        not_beast.description = "monster"
        self.assertFalse(low_druid.can_assume_shape(not_beast))
