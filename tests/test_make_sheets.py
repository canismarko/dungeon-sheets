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


class PdfOutputTeestCase(unittest.TestCase):
    basename = 'clara'
    
    def tearDown(self):
        temp_files = [f'{self.basename}.pdf']
        for f in temp_files:
            if os.path.exists(f):
                os.remove(f)
        
    def test_file_created(self):
        # Check that a file is created once the function is run
        pdf_name = f'{self.basename}.pdf'
        # self.assertFalse(os.path.exists(pdf_name), f'{pdf_name} already exists.')
        char = character.Character(name='Clara')
        char.saving_throw_proficiencies = ['strength']
        make_sheets.create_character_pdf(character=char, basename=self.basename)
        self.assertTrue(os.path.exists(pdf_name), f'{pdf_name} not created.')


class MarkdownTestCase(unittest.TestCase):
    """Check that conversion of markdown formats to LaTeX code works
    correctly."""
    
    def test_rst_bold(self):
        text = make_sheets.rst_to_latex('**hello**')
        self.assertEqual(text, '\\textbf{hello}')
    
    def test_hit_dice(self):
        text = make_sheets.rst_to_latex('1d6+3')
        self.assertEqual(text, '\\texttt{1d6+3}')
    
    def test_no_text(self):
        text = make_sheets.rst_to_latex(None)
        self.assertEqual(text, '')
