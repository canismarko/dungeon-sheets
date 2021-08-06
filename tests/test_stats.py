from unittest import TestCase

from dungeonsheets import stats, character, magic_items


class TestStats(TestCase):
    def test_mod_str(self):
        self.assertEqual(stats.mod_str(-3), "-3")
        self.assertEqual(stats.mod_str(0), "+0")
        self.assertEqual(stats.mod_str(2), "+2")

    def test_saving_throw(self):
        # Try it with an ST proficiency
        class MyClass(character.Character):
            saving_throw_proficiencies = ["strength"]
            proficiency_bonus = 2
            strength = stats.Ability(14)

        my_class = MyClass()
        self.assertEqual(my_class.strength.saving_throw, 4)
        # Try it with a magic item
        my_class.magic_items.append(magic_items.RingOfProtection)
        self.assertEqual(my_class.strength.saving_throw, 5)

    def test_modifier(self):
        class MyCharacter(character.Character):
            saving_throw_proficiencies = ["strength"]
            proficiency_bonus = 2
            strength = stats.Ability(14)

        my_char = MyCharacter()
        ranges = [
            ((1,), -5),
            ((2, 3), -4),
            ((4, 5), -3),
            ((6, 7), -2),
            ((8, 9), -1),
            ((10, 11), 0),
            ((12, 13), 1),
            ((14, 15), 2),
            ((16, 17), 3),
            ((18, 19), 4),
            ((20, 21), 5),
            ((22, 23), 6),
            ((24, 25), 7),
            ((26, 27), 8),
            ((28, 29), 9),
            ((30,), 10),
        ]
        # Test the values for each modifier range
        for range_, target in ranges:
            for value in range_:
                my_char.strength = value
                stat = my_char.strength
                msg = (
                    f"Stat {value} doesn't produce modifier {target} ({stat.modifier})"
                )
                self.assertEqual(stat.modifier, target, msg)

    def test_setter(self):
        """Verify that this class works as a data descriptor."""
        # Set up a dummy class
        class MyCharacter(character.Character):
            stat = stats.Ability()

        char = MyCharacter()
        # Check that the stat works as expected once set
        char.stat = 15
        self.assertEqual(char.stat.value, 15)
        self.assertEqual(char.stat.modifier, 2)

    def test_skill(self):
        """Test for a skill, that depends on another ability."""

        class MyClass(character.Character):
            dexterity = stats.Ability(14)
            acrobatics = stats.Skill(ability="dexterity")
            sleight_of_hand = stats.Skill(ability="dexterity")
            skill_proficiencies = []
            proficiency_bonus = 2

        my_class = MyClass()
        self.assertEqual(str(my_class.acrobatics), "Acrobatics")
        self.assertEqual(my_class.acrobatics.modifier, 2)
        self.assertEqual(str(my_class.sleight_of_hand), "Sleight Of Hand")
        # Check for a proficiency
        my_class.skill_proficiencies = ["acrobatics"]
        self.assertTrue(my_class.acrobatics.is_proficient)
        self.assertEqual(my_class.acrobatics.proficiency_modifier, 2)
        self.assertEqual(my_class.acrobatics.modifier, 4)
        # Check for a proficiency with spaces in the name
        my_class.skill_proficiencies = ["sleight_of_hand"]
        self.assertEqual(my_class.sleight_of_hand.modifier, 4)
