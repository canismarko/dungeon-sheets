from unittest import TestCase

from dungeonsheets import stats, character, encounter


class TestStats(TestCase):
    def new_character(self, level=1):
        return character.Character(classes=['cleric'], levels=[level])
    
    def test_xp_thresholds(self):
        # One level 1 character
        xp_th = encounter.xp_thresholds([self.new_character(1)])
        self.assertEqual(xp_th, (25, 50, 75, 100))
        # Three mixed-level characters
        party = [self.new_character(9), self.new_character(8), self.new_character(6)]
        xp_th = encounter.xp_thresholds(party)
        self.assertEqual(xp_th, (1300, 2600, 3900, 5900))


class TestEncounter(TestCase):
    def test_encounter_init(self):
        enc = encounter.Encounter()
