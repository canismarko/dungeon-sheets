import warnings
from pathlib import Path
import unittest
import types
from contextlib import contextmanager

from dungeonsheets import exceptions
from dungeonsheets.readers import read_sheet_file

EG_DIR = (Path(__file__).parent.parent / "examples").resolve()
CHAR_PYTHON_FILE = EG_DIR / "rogue1.py"
GM_PYTHON_FILE = EG_DIR / "gm-session-notes.py"
ROLL20_JSON_FILE = EG_DIR / "barbarian3.json"
FOUNDRY_JSON_FILE = EG_DIR / "bard3_foundry.json"
SPELLCASTER_JSON_FILE = EG_DIR / "artificer2.json"


class PythonReaderTests(unittest.TestCase):
    @contextmanager
    def inherited_sheets(self):
        """Create some cascading sheets to be inherited."""
        child = Path("child_sheet.py")
        parent = Path("parent_sheet.py")
        # Write inheritance files
        with open(parent, mode="w") as fp:
            fp.writelines("\n".join([
                "dungeonsheets_version = '0.15.0'",
                "background = 'entertainer'",
            ]) + "\n")
        with open(child, mode="w") as fp:
            fp.writelines("\n".join([
                "dungeonsheets_version = '0.15.0'",
                "name = 'Douglass Adams'",
                f"parent_sheets = ['{str(parent)}']",
            ]) + "\n")
        # Drop back into the calling code
        yield child, parent
        # Remove temporary files
        child.unlink()
        parent.unlink()

    def test_cascading_sheets(self):
        with self.inherited_sheets() as (child, parent):
            char_props = read_sheet_file(child)
        self.assertEqual(char_props["name"], "Douglass Adams")
        self.assertEqual(char_props["background"], "entertainer")
    
    def test_load_python_gm_sheet(self):
        gmfile = GM_PYTHON_FILE
        result = read_sheet_file(gmfile)
        self.assertEqual(result["sheet_type"], "gm")
    
    def test_load_python_character(self):
        charfile = CHAR_PYTHON_FILE
        result = read_sheet_file(charfile)
        self.assertEqual(result["strength"], 10)

    def test_load_bad_file(self):
        """This file is not a valid character, so should fail."""
        this_file = __file__
        with self.assertRaises(exceptions.CharacterFileFormatError):
            read_sheet_file(this_file)


class Roll20ReaderTests(unittest.TestCase):
    def test_load_json_file(self):
        charfile = ROLL20_JSON_FILE
        with warnings.catch_warnings(record=True):
            result = read_sheet_file(charfile)
        expected_data = dict(
            name="Ulthar Jenkins",
            classes=["Barbarian"],
            level=2,
            background="Soldier",
            alignment="Lawful Evil",
            race="Hill Dwarf",
            xp=557,
            strength=13,
            dexterity=12,
            constitution=19,
            intelligence=8,
            hp_max=32,
            skill_proficiencies=[
                "athletics",
                "survival",
            ],
            weapon_proficiencies=[
                "simple weapons",
                "martial weapons",
                "battleaxe",
                "handaxe",
                "light hammer",
                "warhammer",
                "unarmed strike",
            ],
            proficiencies_text=[
                "Brewer's Supplies",
            ],
            languages="common, dwarvish",
            cp=26,
            sp=55,
            ep=0,
            gp=207,
            pp=0,
            weapons=["handaxe", "javelin", "warhammer"],
            magic_items=(),
            armor="",
            shield="",
            personality_traits=(
                "Can easily dismember a body\n\nKnow fight battle tactics"
            ),
            ideals="Vengence",
            bonds="friends and adventurers.",
            flaws="Bloodthirsty and wants to solve every problem by murder",
            equipment=(
                "warhammer, handaxe, explorer's pack, javelin (4), backpack, "
                "bedroll, mess kit, tinderbox, torch (10), rations (10), "
                "waterskin, hempen rope"
            ),
            attacks_and_spellcasting="",
            spells_prepared=[],
            spells=[],
        )
        for key, val in expected_data.items():
            this_result = result[key]
            # Force evaluation of generators
            if isinstance(this_result, types.GeneratorType):
                this_result = list(this_result)
            self.assertEqual(this_result, val, key)

    def test_load_json_spells(self):
        charfile = SPELLCASTER_JSON_FILE
        with warnings.catch_warnings(record=True):
            result = read_sheet_file(charfile)
        expected_data = dict(
            spells_prepared=[
                "cure wounds",
            ],
            spells=[
                "spare the dying",
                "fire bolt",
                "absorb elements",
                "alarm",
                "catapult",
                "cure wounds",
                "detect magic",
                "disguise self",
                "expeditious retreat",
                "faerie fire",
                "false life",
                "feather fall",
                "grease",
                "identify",
                "jump",
                "longstrider",
                "purify food and drink",
                "sanctuary",
                "snare",
            ],
        )
        for key, val in expected_data.items():
            this_result = result[key]
            # Force evaluation of generators
            if isinstance(this_result, types.GeneratorType):
                this_result = list(this_result)
            self.assertEqual(this_result, val, key)


class FoundryReaderTests(unittest.TestCase):
    def test_load_json_file(self):
        charfile = FOUNDRY_JSON_FILE
        with warnings.catch_warnings(record=True):
            result = read_sheet_file(charfile)
        expected_data = dict(
            name="Sam Lloyd",
            classes=["Bard"],
            levels=[6],
            background="Attorney",
            alignment="Lawful Neutral",
            race="Variant",
            xp=0,
            strength=6,
            dexterity=12,
            constitution=14,
            intelligence=10,
            wisdom=12,
            charisma=18,
            hp_max=47,
            skill_proficiencies=[
                "deception",
                "insight",
                "investigation",
                "perception",
                "persuasion",
                "sleight_of_hand",
            ],
            skill_expertise=[
                "insight",
                "persuasion",
            ],
            weapon_proficiencies=[
                "simple weapons",
                "martial weapons",
                "crossbow",
                "knives",
            ],
            proficiencies_text=[
                "artisan's tools",
                "disguise kit",
                "forger's kit",
                "gaming set",
                "herbalism kit",
                "musical instrument",
                "navigator's tools",
                "poisoner's kit",
                "thieves' tools",
                "vehicle (land or water)",
                "chopsticks",
                "juggling balls"
            ],
            saving_throw_proficiencies=["dexterity", "charisma"],
            languages="common, elvish, law jargon, spanish",
            cp=0,
            sp=0,
            ep=0,
            gp=162,
            pp=2,
            weapons=["rapier"],
            # magic_items=(),
            armor="padded armor",
            shield="shield",
            personality_traits="Loves a good lawyer joke.",
            ideals="Every form in triplicate.",
            bonds="Just show up to your court date and it won't be a problem.",
            flaws="Too many to list.",
            equipment=(
                "rations(7), ring of acid resistance, cartographer's tools, bag of holding, diamonds(20), padded armor, shield"
            ),
            attacks_and_spellcasting="",
            spells_prepared=["Bane", "Faerie Fire", "Thunderwave", "Detect Thoughts"],
            spells=["Vicious Mockery", "Message", "Prestidigitation", "Bane", "Faerie Fire", "Thunderwave", "Healing Word", "Blindness/Deafness", "Detect Thoughts", "Hold Person", "Fear", "Heat Metal"],
            features=["jack of all trades", "song of rest", "bard college", "expertise (bard)",  "font of inspiration", "bardic inspiration", "lucky", "jack of all trades", "countercharm"],
        )
        for key, val in expected_data.items():
            this_result = result[key]
            # Force evaluation of generators
            if isinstance(this_result, types.GeneratorType):
                this_result = list(this_result)
            self.assertEqual(this_result, val, key)
    
    def test_load_json_spells(self):
        charfile = SPELLCASTER_JSON_FILE
        with warnings.catch_warnings(record=True):
            result = read_sheet_file(charfile)
        expected_data = dict(
            spells_prepared=[
                "cure wounds",
            ],
            spells=[
                "spare the dying",
                "fire bolt",
                "absorb elements",
                "alarm",
                "catapult",
                "cure wounds",
                "detect magic",
                "disguise self",
                "expeditious retreat",
                "faerie fire",
                "false life",
                "feather fall",
                "grease",
                "identify",
                "jump",
                "longstrider",
                "purify food and drink",
                "sanctuary",
                "snare",
            ],
        )
        for key, val in expected_data.items():
            this_result = result[key]
            # Force evaluation of generators
            if isinstance(this_result, types.GeneratorType):
                this_result = list(this_result)
            self.assertEqual(this_result, val, key)
            
    def test_load_homebrew_weapon(self):
        """Check that the properties of a homebrew magic weapon get read
        properly.

        """
        charfile = FOUNDRY_JSON_FILE
        with warnings.catch_warnings(record=True):
            result = read_sheet_file(charfile)
        # Check that some magic items were set
        self.assertGreater(len(result['magic_items']), 0,
                           "No magic items imported")
