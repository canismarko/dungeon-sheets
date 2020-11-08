import warnings
from pathlib import Path
import unittest
import types

from dungeonsheets.readers import read_character_file

EG_DIR = (Path(__file__).parent.parent / "examples").resolve()
CHAR_PYTHON_FILE = EG_DIR / 'rogue1.py'
CHAR_JSON_FILE = EG_DIR / 'barbarian3.json'
SPELLCASTER_JSON_FILE = EG_DIR / 'artificer2.json'

class PythonReaderTests(unittest.TestCase):
    def test_load_python_file(self):
        charfile = CHAR_PYTHON_FILE
        result = read_character_file(charfile)
        self.assertEqual(result['strength'], 10)


class JSONReaderTests(unittest.TestCase):        
    def test_load_json_file(self):
        charfile = CHAR_JSON_FILE
        with warnings.catch_warnings(record=True) as w:
            result = read_character_file(charfile)
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
            skill_proficiencies=["athletics", "survival",],
            weapon_proficiencies=["simple weapons", "martial weapons",  "battleaxe", "handaxe", "light hammer", "warhammer", "unarmed strike",],
            _proficiencies_text=["Brewer's Supplies",],
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
            personality_traits="Can easily dismember a body\n\nKnow fight battle tactics",
            ideals="Vengence",
            bonds="friends and adventurers.",
            flaws="Bloodthirsty and wants to solve every problem by murder",
            equipment=("warhammer, handaxe, explorer's pack, javelin (4), backpack, "
                       "bedroll, mess kit, tinderbox, torch (10), rations (10), "
                       "waterskin, hempen rope"),
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
        with warnings.catch_warnings(record=True) as w:
            result = read_character_file(charfile)
        expected_data = dict(
            spells_prepared=["cure wounds",],
            spells=["spare the dying", "fire bolt", "absorb elements",
                    "alarm", "catapult", "cure wounds", "detect magic",
                    "disguise self", "expeditious retreat", "faerie fire",
                    "false life", "feather fall", "grease", "identify",
                    "jump", "longstrider", "purify food and drink",
                    "sanctuary", "snare",],
        )
        for key, val in expected_data.items():
            this_result = result[key]
            # Force evaluation of generators
            if isinstance(this_result, types.GeneratorType):
                this_result = list(this_result)
            self.assertEqual(this_result, val, key)
