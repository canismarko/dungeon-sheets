import unittest
import os
from pathlib import Path

from dungeonsheets import make_sheets, character
from dungeonsheets.fill_pdf_template import create_character_pdf_template, create_spells_pdf_template


EG_DIR = os.path.abspath(os.path.join(os.path.split(__file__)[0], "../examples/"))
CHARFILE = os.path.join(EG_DIR, "rogue1.py")


class PdfOutputTestCase(unittest.TestCase):
    basename = "clara"

    def tearDown(self):
        temp_files = [f"{self.basename}.pdf"]
        for f in temp_files:
            if os.path.exists(f):
                os.remove(f)

    def test_file_created(self):
        # Check that a file is created once the function is run
        pdf_name = f"{self.basename}.pdf"
        # self.assertFalse(os.path.exists(pdf_name), f'{pdf_name} already exists.')
        char = character.Character(name="Clara")
        char.saving_throw_proficiencies = ["strength"]
        make_sheets.create_character_pdf_template(character=char, basename=self.basename)
        self.assertTrue(os.path.exists(pdf_name), f"{pdf_name} not created.")
