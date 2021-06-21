import unittest
import os
from pathlib import Path

from dungeonsheets import make_sheets, character, monsters


EG_DIR = Path(__file__).parent.parent.resolve() / "examples"
CHARFILE = EG_DIR / "rogue1.py"
GMFILE = EG_DIR / "gm-session-notes.py"


class MakeSheetsTestCase(unittest.TestCase):
    char_pdf = Path(f"{CHARFILE.stem}.pdf")
    gm_pdf = Path(f"{GMFILE.stem}.pdf").resolve()

    def tearDown(self):
        if self.char_pdf.exists():
            self.char_pdf.unlink()
        if self.gm_pdf.exists():
            self.gm_pdf.unlink()

    def test_main(self):
        make_sheets.main(args=[str(CHARFILE), "--debug"])
    
    def test_make_sheets(self):
        # Character PDF
        make_sheets.make_sheet(sheet_file=CHARFILE)
        # Was the PDF created?
        self.assertTrue(self.char_pdf.exists(),
                        f"Character PDF ({self.char_pdf.resolve()}) not created.")
        # GM PDF
        make_sheets.make_sheet(sheet_file=GMFILE)
        self.assertTrue(self.gm_pdf.exists)
        # Was the PDF created?
        self.assertTrue(self.gm_pdf.exists(),
                        f"GM PDF ({self.gm_pdf.resolve()}) not created.")

    def test_make_fancy_sheets(self):
        # Character PDF
        make_sheets.make_sheet(sheet_file=CHARFILE,
                               fancy_decorations=True)
        # Was the PDF created?
        self.assertTrue(self.char_pdf.exists(),
                        f"Character PDF ({self.char_pdf.resolve()}) not created.")
        # GM PDF
        make_sheets.make_sheet(sheet_file=GMFILE,
                               fancy_decorations=True)
        self.assertTrue(self.gm_pdf.exists)
        # Was the PDF created?
        self.assertTrue(self.gm_pdf.exists(),
                        f"GM PDF ({self.gm_pdf.resolve()}) not created.")


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
        make_sheets.create_character_pdf_template(
            character=char, basename=self.basename
        )
        self.assertTrue(os.path.exists(pdf_name), f"{pdf_name} not created.")


class VashtaNerada(monsters.Monster):
    """Scariest monster ever, but luckily only for testing."""
    name = "Vashta Nerada"
    speed = 35
    fly_speed = 45
    swim_speed = 55
    burrow_speed = 65
    condition_immunities = "petrified"
    saving_throws = "Dex +8"
    damage_immunities = "Bludgeoning"
    damage_resistances = "Lightning"
    challenge_rating = 93
    


class TexCreatorTestCase(unittest.TestCase):
    """Test various helper functions for creating TeX from a character."""

    def new_character(self):
        char = character.Character(
            name="Dr. Who",
            classes=["Monk", "Druid", "Artificer"],
            levels=[1, 1, 1],
            subclasses=["way of the open hand", None, None],
            magic_items=["cloak of protection"],
            spells=["invisibility"],
            wild_shapes=["crocodile"],
            infusions=["boots of the winding path"]
        )
        return char

    def test_create_subclasses_tex(self):
        char = self.new_character()
        tex = make_sheets.create_subclasses_tex(character=char)
        self.assertIn(r"\section*{Subclasses}", tex)
        self.assertIn(r"\subsection*{Way of the Open Hand}", tex)

    def test_create_features_tex(self):
        char = self.new_character()
        tex = make_sheets.create_features_tex(character=char)
        self.assertIn(r"\section*{Features}", tex)
        self.assertIn(r"\subsection*{Martial Arts}", tex)

    def test_create_magic_items_tex(self):
        char = self.new_character()
        tex = make_sheets.create_magic_items_tex(character=char)
        self.assertIn(r"\section*{Magic Items}", tex)
        self.assertIn(r"\subsection*{Cloak of Protection}", tex)

    def test_create_spellbook_tex(self):
        char = self.new_character()
        tex = make_sheets.create_spellbook_tex(character=char)
        self.assertIn(r"\section*{Spells}", tex)
        self.assertIn(r"\section*{Invisibility}", tex)

    def test_create_infusions_tex(self):
        char = self.new_character()
        tex = make_sheets.create_infusions_tex(character=char)
        self.assertIn(r"\section*{Infusions}", tex)
        self.assertIn(r"\subsection*{Boots of the Winding Path}", tex)

    def test_create_druid_shapes_tex(self):
        char = self.new_character()
        tex = make_sheets.create_druid_shapes_tex(character=char)
        self.assertIn(r"\section*{Known Beasts}", tex)
        self.assertIn(r"\section*{Crocodile}", tex)

    def test_create_monsters_tex(self):
        monsters_ = [monsters.GiantEagle()]
        tex = make_sheets.create_monsters_tex(monsters=monsters_)
        self.assertIn(r"Giant Eagle", tex)
        # Check extended properties
        monsters_ = [VashtaNerada()]
        tex = make_sheets.create_monsters_tex(monsters=monsters_)
        self.assertIn(r"Vashta Nerada", tex)
        self.assertIn(r"35", tex)
        self.assertIn(r"45 fly", tex)
        self.assertIn(r"55 swim", tex)
        self.assertIn(r"65 burrow", tex)
        self.assertIn(r"petrified", tex)
        self.assertIn(r"Saving Throws:", tex)
        self.assertIn(r"Damage Immunities:", tex)
        self.assertIn(r"Damage Resistances:", tex)
        self.assertIn(r"Damage Vulnerabilities:", tex)
        self.assertIn(r"Senses:", tex)
        self.assertIn(r"Challenge:", tex)
        self.assertIn(r"Languages:", tex)
        self.assertIn(r"Skills:", tex)
        # Check fancy extended properties
        tex = make_sheets.create_monsters_tex(monsters=monsters_,
                                              use_dnd_decorations=True)
        self.assertIn(r"Vashta Nerada", tex)
        self.assertIn(r"35 ft.", tex)
        self.assertIn(r"45 ft. fly", tex)
        self.assertIn(r"55 ft. swim", tex)
        self.assertIn(r"65 ft. burrow", tex)
        self.assertIn(r"petrified", tex)
        self.assertIn(r"saving-throws = {Dex +8}", tex)

    def test_create_party_summary_tex(self):
        char = self.new_character()
        tex = make_sheets.create_party_summary_tex(party=[char], summary_rst="")
        self.assertIn(r"\section*{Party}", tex)
        self.assertIn(char.name, tex)
    
    def test_create_summary_tex(self):
        rst = "The party's create *adventure*."
        tex = make_sheets.create_party_summary_tex(party=[], summary_rst=rst)
        self.assertIn(r"\section*{Summary}", tex)
        # Check that the RST is parsed
        self.assertIn(r"\emph{adventure}", tex)

    def test_random_tables_tex(self):
        tex = make_sheets.create_random_tables_tex(
            conjure_animals=True,
        )
        self.assertIn(r"\subsection*{Conjure Animals}", tex)
