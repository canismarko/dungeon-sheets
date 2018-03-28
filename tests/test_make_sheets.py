import unittest
import os

from dungeonsheets import make_sheets, character

EG_DIR = os.path.abspath(os.path.join(os.path.split(__file__)[0], '../examples/'))
CHARFILE = os.path.join(EG_DIR, 'rogue.py')

class CharacterFileTestCase(unittest.TestCase):
    def test_load_character_file(self):
        charfile = CHARFILE
        result = make_sheets.load_character_file(charfile)
        self.assertEqual(result['strength'], 8)

class FDFTestCase(unittest.TestCase):
    def tearDown(self):
        if os.path.exists('temp.fdf'):
            os.remove('temp.fdf')
    
    def test_create_fdf(self):
        fdfname = 'temp.fdf'
        char = character.Character()
        make_sheets.create_fdf(char, fdfname=fdfname)
        self.assertTrue(os.path.exists(fdfname))
