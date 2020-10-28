import unittest
import os

from dungeonsheets import make_sheets, character

EG_DIR = os.path.abspath(os.path.join(os.path.split(__file__)[0], '../examples/'))
CHARFILE = os.path.join(EG_DIR, 'rogue1.py')

class CharacterFileTestCase(unittest.TestCase):
    def test_load_character_file(self):
        charfile = CHARFILE
        result = make_sheets.load_character_file(charfile)
        self.assertEqual(result['strength'], 10)


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
    
    def test_verbatim(self):
        text = make_sheets.rst_to_latex('``hello, world``')
        self.assertIn(r'\begin{verbatim}', text)

    def test_literal_backslash(self):
        text = make_sheets.rst_to_latex('\\')
        self.assertEqual(r'\\', text)
    
    def test_headings(self):
        # Simple heading by itself
        text = make_sheets.rst_to_latex('Hello, world\n============\n')
        self.assertEqual('\\section*{Hello, world}\n', text)
        # Simple heading with leading whitespace
        text = make_sheets.rst_to_latex('    Hello, world\n    ============\n')
        self.assertEqual('\\section*{Hello, world}\n', text)
        # Heading with text after it
        text = make_sheets.rst_to_latex('Hello, world\n============\n\nThis is some text')
        self.assertEqual('\\section*{Hello, world}\n\nThis is some text', text)
        # Heading with text before it
        text = make_sheets.rst_to_latex('This is a paragraph\n\nHello, world\n============\n')
        self.assertEqual('This is a paragraph\n\n\\section*{Hello, world}\n', text)
        # Check that levels of headings are parsed appropriately
        text = make_sheets.rst_to_latex('Hello, world\n^^^^^^^^^^^^\n')
        self.assertEqual('\\subsubsection*{Hello, world}\n', text)
        text = make_sheets.rst_to_latex('Hello, world\n^^^^^^^^^^^^\n', top_heading_level=3)
        self.assertEqual('\\subparagraph*{Hello, world}\n', text)
        # This is a bad heading missing with all the underline on one line
        text = make_sheets.rst_to_latex('Hello, world^^^^^^^^^^^^\n')
        self.assertEqual('Hello, world\\^\\^\\^\\^\\^\\^\\^\\^\\^\\^\\^\\^\n', text)

    def test_bullet_list(self):
        tex = make_sheets.rst_to_latex("\n- Hello\n- World\n\n")
        expected_tex = "\n\\begin{itemize}\n\\item{Hello}\n\\item{World}\n\\end{itemize}\n\n"
        self.assertEqual(expected_tex, tex)
        # Other bullet characters
        tex = make_sheets.rst_to_latex("\n* Hello\n* World\n\n")
        self.assertEqual(expected_tex, tex)
        tex = make_sheets.rst_to_latex("\n+ Hello\n+ World\n\n")
        self.assertEqual(expected_tex, tex)
        # A real list taken from a docstring
        real_list = """
        - Secondhand (you have heard of the target) - +5
        - Firsthand (you have met the target) - +0
        - Familiar (you know the target well) - -5
        
        """
        tex = make_sheets.rst_to_latex(real_list)
        self.assertIn("\\begin{itemize}", tex)
    
    def test_multiline_bullet_list(self):
        md_list = """
        - Secondhand (you have heard
          of the target) - +5
        - Firsthand (you have met 
          the target) - +0
        - Familiar (you know the target 
          well) - -5
        
        """
        tex = make_sheets.rst_to_latex(md_list)
        print(tex)
        self.assertIn("\\begin{itemize}", tex)
