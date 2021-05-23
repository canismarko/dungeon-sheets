import warnings
from pathlib import Path
import unittest
import types

from dungeonsheets.readers import read_character_file

EG_DIR = (Path(__file__).parent.parent / "examples").resolve()
CHAR_PYTHON_FILE = EG_DIR / "rogue1.py"
ROLL20_JSON_FILE = EG_DIR / "barbarian3.json"
FOUNDRY_JSON_FILE = EG_DIR / "bard3_foundry.json"
SPELLCASTER_JSON_FILE = EG_DIR / "artificer2.json"


class PythonReaderTests(unittest.TestCase):
    def test_load_python_file(self):
        charfile = CHAR_PYTHON_FILE
        result = read_character_file(charfile)
        self.assertEqual(result["strength"], 10)


class Roll20ReaderTests(unittest.TestCase):
    def test_load_json_file(self):
        charfile = ROLL20_JSON_FILE
        with warnings.catch_warnings(record=True):
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
            _proficiencies_text=[
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
            result = read_character_file(charfile)
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
            result = read_character_file(charfile)
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
            _proficiencies_text=[
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
            magic_items=(),
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
            result = read_character_file(charfile)
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
            