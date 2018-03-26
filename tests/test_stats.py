from unittest import TestCase

from dungeonsheets import stats

class TestStats(TestCase):

    def test_mod_str(self):
        self.assertEqual(stats.mod_str(-3), '-3')
        self.assertEqual(stats.mod_str(0), '0')
        self.assertEqual(stats.mod_str(2), '+2')
    
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
        stat = stats.Stat()
        for range_, target in ranges:
            for value in range_:
                stat.value = value
                msg = f"Stat {value} doesn't produce modifier {target} ({stat.modifier})"
                self.assertEqual(stat.modifier, target, msg)
    
    def test_setter(self):
        """Verify that this class works as a data descriptor."""
        # Set up a dummy class
        class MyCharacter():
            stat = stats.Stat()
        char = MyCharacter()
        # Check that the stat works as expected once set
        char.stat = 15
        self.assertEqual(char.stat.value, 15)
        self.assertEqual(char.stat.modifier, 2)
