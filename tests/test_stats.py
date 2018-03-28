from unittest import TestCase

from dungeonsheets import stats, character

class TestStats(TestCase):

    def test_mod_str(self):
        self.assertEqual(stats.mod_str(-3), '-3')
        self.assertEqual(stats.mod_str(0), '0')
        self.assertEqual(stats.mod_str(2), '+2')
    
    def test_saving_throw(self):
        stat = stats.Ability(14)
        self.assertEqual(stat.saving_throw, 2)
        # Now try it with an ST proficiency
        class MyClass():
            saving_throw_proficiencies = ['strength']
            proficiency_bonus = 2
            strength = stats.Ability(14)
        my_class = MyClass()
        self.assertEqual(my_class.strength.saving_throw, 4)
    
    def test_modifier(self):
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
        stat = stats.Ability()
        for range_, target in ranges:
            for value in range_:
                stat.value = value
                msg = f"Stat {value} doesn't produce modifier {target} ({stat.modifier})"
                self.assertEqual(stat.modifier, target, msg)
    
    def test_setter(self):
        """Verify that this class works as a data descriptor."""
        # Set up a dummy class
        class MyCharacter():
            stat = stats.Ability()
        char = MyCharacter()
        # Check that the stat works as expected once set
        char.stat = 15
        self.assertEqual(char.stat.value, 15)
        self.assertEqual(char.stat.modifier, 2)
    
    def test_skill(self):
        """Test for a skill, that depends on another ability."""
        class MyClass():
            dexterity = stats.Ability(14)
            acrobatics = stats.Skill(ability='dexterity')
            skill_proficiencies = []
            proficiency_bonus = 2
        my_class = MyClass()
        self.assertEqual(my_class.acrobatics, 2)
        # Check for a proficiency
        my_class.skill_proficiencies = ['acrobatics']
        self.assertEqual(my_class.acrobatics, 4)

    def test_findattr(self):
        """Check if the function can find attributes."""
        class TestClass():
            my_attr = 47
            YourAttr = 53
        test_class = TestClass()
        # Direct access
        self.assertEqual(stats.findattr(test_class, 'my_attr'),
                         test_class.my_attr)
        self.assertEqual(stats.findattr(test_class, 'YourAttr'),
                         test_class.YourAttr)
        # Swapping spaces for capitalization
        self.assertEqual(stats.findattr(test_class, 'my attr'),
                         test_class.my_attr)
        self.assertEqual(stats.findattr(test_class, 'your attr'),
                         test_class.YourAttr)
