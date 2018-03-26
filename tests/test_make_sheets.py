import unittest
import os

from dungeonsheets import make_sheets, character


class CharacterFileTestCase(unittest.TestCase):
    def test_load_character_file(self):
        charfile = 'examples/rogue.py'
        result = make_sheets.load_character_file(charfile)
        self.assertEqual(result['strength'], 10)

class FDFTestCase(unittest.TestCase):
    def test_create_fdf(self):
        fdfname = 'temp.fdf'
        char = character.Character()
        make_sheets.create_fdf(char, fdfname=fdfname)
        self.assertTrue(os.path.exists(fdfname))
        
