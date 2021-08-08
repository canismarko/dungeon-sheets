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


class EpubOutputTestCase(unittest.TestCase):
    gm_epub = Path(f"{GMFILE.stem}.epub").resolve()
    char_epub = Path(f"{CHARFILE.stem}.epub").resolve()

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

    def tearDown(self):
        for f in [self.gm_epub, self.char_epub]:
            if f.exists():
                f.unlink()

    def test_character_html_content(self):
        my_char = self.new_character()
        html = make_sheets.make_character_content(character=my_char,
                                                  content_format="html")
        html = "".join(html)
        # Make sure the various sections get rendered
        self.assertIn("Subclasses</h1>", html)
        self.assertIn("Features</h1>", html)
        self.assertIn("Magic Items</h1>", html)
        self.assertIn("Spells</h1>", html)
        self.assertIn("Infusions</h1>", html)
        self.assertIn("Known Beasts</h1>", html)
        # Check the character sheet
        self.assertIn("Character Sheet</h1>", html)
        self.assertIn("Dr. Who", html)

    def test_gm_file_created(self):
        # Check that a file is created once the function is run
        make_sheets.make_gm_sheet(gm_file=GMFILE, output_format="epub")
        self.assertTrue(self.gm_epub.exists(), f"{self.gm_epub} not created.")

    def test_character_file_created(self):
        # Check that a file is created once the function is run
        make_sheets.make_character_sheet(char_file=CHARFILE, output_format="epub")
        self.assertTrue(self.char_epub.exists(), f"{self.char_epub} not created.")        


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
    damage_vulnerabilities = "Wood-based"
    challenge_rating = 93
    spells = ["wish"]


class HtmlCreatorTestCase(unittest.TestCase):
    def test_create_monsters_html(self):
        monsters_ = [monsters.Priest()]
        html = make_sheets.create_monsters_content(monsters=monsters_, suffix="html")
        self.assertIn(r"Priest", html)
        # Check extended properties
        monsters_ = [VashtaNerada()]
        html = make_sheets.create_monsters_content(monsters=monsters_, suffix="html")
        self.assertIn(r"Vashta Nerada", html)
        self.assertIn(r"35", html)
        self.assertIn(r"45 fly", html)
        self.assertIn(r"55 swim", html)
        self.assertIn(r"65 burrow", html)
        self.assertIn(r"petrified", html)
        self.assertIn(r"Saving Throws", html)
        self.assertIn(r"Damage Immunities", html)
        self.assertIn(r"Damage Resistances", html)
        self.assertIn(r"Damage Vulnerabilities", html)
        self.assertIn(r"Senses", html)
        self.assertIn(r"Challenge", html)
        self.assertIn(r"Languages", html)
        self.assertIn(r"Skills", html)
        self.assertIn(r"petrified", html)
        self.assertIn(r"Dex +8", html)
        # Check spells and spell descriptions
        self.assertIn(r"<dt>Level 9</dt>", html)
        self.assertIn(r"Wish", html)        
        # Check fancy extended properties
        html = make_sheets.create_monsters_content(monsters=monsters_,
                                                   suffix="html",
                                                   use_dnd_decorations=True)

    def test_create_extra_gm_content(self):
        class MySection():
            name = "My D&D Homebrew Content"

        html = make_sheets.create_extra_gm_content(sections=[MySection], suffix="html")
        self.assertIn('<h1 id="extra-My-DD-Homebrew-Content">', html)
        tex = make_sheets.create_extra_gm_content(sections=[MySection], suffix="tex")
        self.assertIn(r'\section*{My D&D Homebrew Content', tex)


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
        tex = make_sheets.create_subclasses_content(character=char, content_suffix="tex")
        self.assertIn(r"\section*{Subclasses}", tex)
        self.assertIn(r"\subsection*{Way of the Open Hand}", tex)

    def test_create_features_tex(self):
        char = self.new_character()
        tex = make_sheets.create_features_content(character=char, content_suffix="tex")
        self.assertIn(r"\section*{Features}", tex)
        self.assertIn(r"\subsection*{Martial Arts}", tex)

    def test_create_magic_items_tex(self):
        char = self.new_character()
        tex = make_sheets.create_magic_items_content(character=char, content_suffix="tex")
        self.assertIn(r"\section*{Magic Items}", tex)
        self.assertIn(r"\subsection*{Cloak of Protection}", tex)

    def test_create_spellbook_tex(self):
        char = self.new_character()
        tex = make_sheets.create_spellbook_content(character=char, content_suffix="tex")
        self.assertIn(r"\section*{Spells}", tex)
        self.assertIn(r"\section*{Invisibility}", tex)

    def test_create_infusions_tex(self):
        char = self.new_character()
        tex = make_sheets.create_infusions_content(character=char, content_suffix="tex")
        self.assertIn(r"\section*{Infusions}", tex)
        self.assertIn(r"\subsection*{Boots of the Winding Path}", tex)

    def test_create_druid_shapes_tex(self):
        char = self.new_character()
        tex = make_sheets.create_druid_shapes_content(character=char, content_suffix="tex")
        self.assertIn(r"\section*{Known Beasts}", tex)
        self.assertIn(r"\section*{Crocodile}", tex)

    def test_create_monsters_tex(self):
        monsters_ = [monsters.GiantEagle()]
        tex = make_sheets.create_monsters_content(monsters=monsters_, suffix="tex")
        self.assertIn(r"Giant Eagle", tex)
        # Check extended properties
        monsters_ = [VashtaNerada()]
        tex = make_sheets.create_monsters_content(monsters=monsters_, suffix="tex")
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
        tex = make_sheets.create_monsters_content(monsters=monsters_,
                                                  suffix="tex",
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
        tex = make_sheets.create_party_summary_content(party=[char], suffix="tex", summary_rst="")
        self.assertIn(r"\section*{Party}", tex)
        self.assertIn(char.name, tex)
    
    def test_create_summary_tex(self):
        rst = "The party's create *adventure*."
        tex = make_sheets.create_party_summary_content(party=[], suffix="tex", summary_rst=rst)
        self.assertIn(r"\section*{Summary}", tex)
        # Check that the RST is parsed
        self.assertIn(r"\emph{adventure}", tex)

    def test_random_tables_tex(self):
        tex = make_sheets.create_random_tables_content(
            suffix="tex",
            conjure_animals=True,
        )
        self.assertIn(r"\subsection*{Conjure Animals}", tex)
