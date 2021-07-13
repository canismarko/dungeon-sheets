import importlib
import warnings
import json
import re
from functools import lru_cache
import logging
from typing import Union

from pathlib import Path

from dungeonsheets import exceptions

log = logging.getLogger(__file__)


def read_sheet_file(filename: Union[str, Path]) -> dict:
    """Create a character object from the given definition file.

    The definition file should be an importable python file or a JSON
    file following one of the supported formats, filled with variables
    describing the character.

    This function also resolves any *parent_sheets* attributes in the
    given sheet, loading parent sheets and updating those attributes.

    Parameters
    ----------
    filename
      The path to the file that will be imported.

    Returns
    -------
    char_props
      Dictionary with the import character properties.

    """
    filename = Path(filename).resolve()
    # Parse the file name
    ext = filename.suffix
    try:
        reader = readers_by_extension[ext](filename=filename)
    except KeyError:
        raise ValueError(f"Character definition {filename} is not a known file type.")
    else:
        these_props = reader()
    # Resolve parent_sheets
    char_props = {}
    parent_sheets = these_props.pop("parent_sheets", [])
    for parent_sheet in parent_sheets:
        parent_sheet = (filename.parent / parent_sheet).resolve()
        if parent_sheet != filename:
            parent_props = read_sheet_file(parent_sheet)
            char_props.update(parent_props)
    char_props.update(these_props)
    # Remove imported dungeonsheets modules
    char_props.pop("import_homebrew", None)
    char_props.pop("mechanics", None)
    # Remove private variables (start with a '_')
    for attr in list(char_props.keys()):
        if attr[0] == "_":
            char_props.pop(attr)
    return char_props


class BaseCharacterReader:
    """Callable to parse a generic character file. Meant to be subclassed."""

    def __init__(self, filename: str):
        """

        Parameters
        ----------
        filename
          The path to the file that will be imported.

        """
        self.filename = filename

    def __call__(self, filename):
        """
        Parameters
        ----------
        filename
          The path to the file that will be imported.
        """
        raise NotImplementedError()


def json_character_reader(filename: str):
    """Factory to create a JSON reader of the correct sub-type."""
    # Try and extract the schema version to see if it's valid
    json_reader = Roll20CharacterReader(filename)
    try:
        json_reader.schema_version
    except KeyError:
        # Assume it's a foundry file
        json_reader = FoundryCharacterReader(filename)
    return json_reader


class JSONCharacterReader(BaseCharacterReader):
    """Callable to parse a JSON character file from Roll20 VVTES.

    The definition file should be a JSON file following one of the
    supported formats, filled with variables describing the character.

    """

    @lru_cache()
    def json_data(self):
        # Load the JSON data from disk
        with open(self.filename, mode="r") as fp:
            data = json.load(fp)
        return data

    def as_int(self, val):
        try:
            val = int(val)
        except ValueError:
            val = 0
        return val


class Roll20CharacterReader(JSONCharacterReader):
    @property
    def schema_version(self):
        return self.json_data()["schema_version"]

    def get_attrib(self, key, which="current", default=None):
        for obj in self.json_data()["attribs"]:
            if obj["name"] == key:
                val = obj[which]
                return val
        # No object was found
        if default is not None:
            return default
        else:
            raise KeyError(key)

    def has_skill_proficiency(self, key):
        false_profs = ["", "0"]
        return self.get_attrib(key=f"{key}_prof") not in false_profs

    def proficiencies(self, kind=None):
        """Iterator over the skills in which the character is proficient.

        *kind* can be one of "weapon", "language", or None (all
         proficiencies).

        """
        prof_re = re.compile("repeating_proficiencies_([-0-9a-zA-Z]+)_name")
        for obj in self.json_data()["attribs"]:
            match = prof_re.match(obj["name"])
            if match:
                prof_id = match.group(1)
                prof_type = self.get_attrib(
                    f"repeating_proficiencies_{prof_id}_prof_type"
                )
                if kind is None or prof_type == kind.upper():
                    yield self.get_attrib(
                        f"repeating_proficiencies_{prof_id}_name"
                    ).lower()

    def equipment(self, kind=None):
        """Iterator over items in the character's inventory."""
        prof_re = re.compile("repeating_inventory_([-0-9a-zA-Z]+)_itemname")
        for obj in self.json_data()["attribs"]:
            match = prof_re.match(obj["name"])
            if match:
                item_id = match.group(1)
                item_name = self.get_attrib(match.group(0))
                item_count = int(
                    self.get_attrib(
                        f"repeating_inventory_{item_id}_itemcount", default=1
                    )
                )
                # item_weight = self.get_attrib(
                #     f"repeating_inventory_{item_id}_itemweight", default=0
                # )
                item_str = item_name.lower().strip()
                if item_count > 1:
                    item_str += f" ({item_count})"
                yield item_str

    def weapons(self):
        """Iterator over the weapons the character is carrying in her inventory."""
        item_re = re.compile("repeating_attack_([-0-9a-zA-Z]+)_atkname")
        for obj in self.json_data()["attribs"]:
            match = item_re.match(obj["name"])
            if match:
                weapon_name = self.get_attrib(match.group()).lower()
                weapon_name = weapon_name.split("(")[0].strip()
                weapon_name = weapon_name.split(",")[0].strip()
                yield weapon_name

    def spells(self, prepared: bool = False):
        """Iterator over the spells the character knows.

        Parameters
        ==========
        prepared
          If true, only return prepared spells.

        """
        # "name": "repeating_spell-cantrip_-MEzYWPA5cUZYd4ZOvMS_spellname",
        prof_re = re.compile(
            "repeating_spell-(cantrip|[0-9]+)_([-0-9a-zA-Z]+)_spellname"
        )
        for obj in self.json_data()["attribs"]:
            match = prof_re.match(obj["name"])
            if match:
                level = match.group(1)
                spell_id = match.group(2)
                spell_name = self.get_attrib(
                    f"repeating_spell-{level}_{spell_id}_spellname"
                )
                is_prepared = self.as_int(
                    self.get_attrib(
                        f"repeating_spell-{level}_{spell_id}_spellprepared", default=0
                    )
                )
                if not prepared or is_prepared:
                    yield spell_name.lower()

    def __call__(self):
        """Create a character property dictionary from the JSON file."""
        # Verify the version compatibility
        if self.schema_version != 2:
            raise exceptions.JSONFormatError(
                "Cannot parse JSON schema version: %s" % self.schema_version
            )
        # Parse the json tree to get character properties
        char_props = {}
        char_props["name"] = self.json_data()["name"]
        char_props["level"] = self.as_int(self.get_attrib("base_level"))
        char_props["classes"] = [self.get_attrib("class")]
        char_props["background"] = self.get_attrib("background")
        char_props["race"] = self.get_attrib("subrace")
        char_props["alignment"] = self.get_attrib("alignment")
        char_props["xp"] = self.as_int(self.get_attrib("experience", default=0))
        # Attributes
        attribute_names = [
            "strength",
            "dexterity",
            "constitution",
            "intelligence",
            "wisdom",
            "charisma",
        ]
        for attr in attribute_names:
            char_props[attr] = self.as_int(self.get_attrib(f"{attr}_base"))
        # Skill proficiencies
        skill_names = [
            "acrobatics",
            "animal_handling",
            "arcana",
            "athletics",
            "deception",
            "history",
            "insight",
            "intimidation",
            "investigation",
            "medicine",
            "nature",
            "perception",
            "performance",
            "persuasion",
            "religion",
            "sleight_of_hand",
            "stealth",
            "survival",
        ]
        skill_profs = [
            skill for skill in skill_names if self.has_skill_proficiency(skill)
        ]
        char_props["skill_proficiencies"] = skill_profs
        # Other proficiencies
        char_props["weapon_proficiencies"] = self.proficiencies("weapon")
        char_props["languages"] = ", ".join(self.proficiencies("language"))
        # Tool proficiencies
        prof_re = re.compile("repeating_tool_([-0-9a-zA-Z]+)_toolname")
        tool_profs = []
        for obj in self.json_data()["attribs"]:
            match = prof_re.match(obj["name"])
            if match:
                tool_profs.append(self.get_attrib(match.group(0)))
        char_props["proficiencies_text"] = tool_profs
        # Combat stats
        char_props["hp_max"] = self.as_int(self.get_attrib("hp", which="max"))
        # Equipment
        char_props["cp"] = self.as_int(self.get_attrib("cp", default=0))
        char_props["sp"] = self.as_int(self.get_attrib("sp", default=0))
        char_props["ep"] = self.as_int(self.get_attrib("ep", default=0))
        char_props["gp"] = self.as_int(self.get_attrib("gp", default=0))
        char_props["pp"] = self.as_int(self.get_attrib("pp", default=0))
        char_props["weapons"] = self.weapons()
        char_props["equipment"] = ", ".join(self.equipment())
        # Personality, etc
        char_props["personality_traits"] = self.get_attrib("personality_traits").strip()
        char_props["flaws"] = self.get_attrib("flaws").strip()
        char_props["ideals"] = self.get_attrib("ideals").strip()
        char_props["bonds"] = self.get_attrib("bonds").strip()
        # Spells
        char_props["spells"] = self.spells()
        char_props["spells_prepared"] = self.spells(prepared=True)
        # Some unused values
        warn_msg = (
            "Importing the following traits from JSON is not yet supported: "
            "magic_items, armor, shield, attacks_and_spellcasting, "
            "infusions, wild_shapes"
        )
        warnings.warn(warn_msg)
        log.warning(warn_msg)
        char_props["magic_items"] = ()
        char_props["armor"] = ""
        char_props["shield"] = ""
        char_props["attacks_and_spellcasting"] = ""
        char_props["infusions"] = []
        char_props["wild_shapes"] = []
        return char_props


class FoundryCharacterReader(JSONCharacterReader):
    # List of weapons to ignore, only for class features that get added automatically
    _invalid_weapons = [
        "unarmed strike (monk)",
        "<no name>",
    ]

    def _skill_proficiency_value(self, key: str) -> float:
        proficiency_labels = {
            "acrobatics": "acr",
            "animal_handling": "ani",
            "arcana": "arc",
            "athletics": "ath",
            "deception": "dec",
            "history": "his",
            "insight": "ins",
            "intimidation": "itm",
            "investigation": "inv",
            "medicine": "med",
            "nature": "nat",
            "perception": "prc",
            "performance": "prf",
            "persuasion": "per",
            "religion": "rel",
            "sleight_of_hand": "slt",
            "stealth": "ste",
            "survival": "sur",
        }
        proficiency_value = float(
            self.json_data()["data"]["skills"][proficiency_labels[key]]["value"]
        )
        return proficiency_value

    def skill_proficiency(self, key: str) -> bool:
        return self._skill_proficiency_value(key) >= 1.0

    def skill_expertise(self, key: str) -> bool:
        return self._skill_proficiency_value(key) > 1.0

    def proficiencies(self, kind=None):
        """Iterator over the skills in which the character is proficient.

        *kind* can be one of "weapon", "language", or None (all
         proficiencies).

        """
        yield_weapons = kind is None or kind == "weapon"
        yield_languages = kind is None or kind == "language"
        # Weapon proficiencies
        if yield_weapons:
            weapon_prof = self.json_data()["data"]["traits"]["weaponProf"]
            # Simple and martial weapons
            if "sim" in weapon_prof["value"]:
                yield "simple weapons"
            if "mar" in weapon_prof["value"]:
                yield "martial weapons"
            # Extra weapons
            for weapon in weapon_prof["custom"].split(";"):
                yield weapon.strip()
        if yield_languages:
            # Languages
            lang_json = self.json_data()["data"]["traits"]["languages"]
            languages = lang_json["value"]
            languages.extend([s.strip() for s in lang_json["custom"].split(";")])
            yield from languages

    def weapons(self):
        """Iterator over the weapons the character is carrying in her inventory."""
        items = self.json_data()["items"]
        for item in items:
            is_valid_weapon = (
                item["type"] == "weapon"
                and item["name"].lower() not in self._invalid_weapons
            )
            if is_valid_weapon:
                yield item["name"].lower()

    def armor(self):
        items = self.json_data()["items"]
        armor_types = ["light", "medium", "heavy"]
        for item in items:
            if (
                item["type"] == "equipment"
                and item["data"]["armor"]["type"] in armor_types
            ):
                return item["name"].lower()

    def shield(self):
        items = self.json_data()["items"]
        for item in items:
            if (
                item["type"] == "equipment"
                and item["data"]["armor"]["type"] == "shield"
            ):
                return item["name"].lower()

    def equipment(self):
        """Iterator over the non-weapons the character is carrying in her
        inventory.

        """
        items = self.json_data()["items"]
        item_types = ["consumable", "equipment", "tool", "backpack", "loot"]
        for item in items:
            if item["type"] in item_types:
                item_name = item["name"]
                quantity = self.as_int(item["data"]["quantity"])
                if quantity != 1:
                    item_name += f"({quantity})"
                yield item_name.lower()

    def class_levels(self):
        for item in self.json_data()["items"]:
            if item["type"] == "class":
                yield (item["name"], item["data"]["levels"])

    def spells(self, prepared: bool = False):
        """Iterator over the spells the character knows.

        Parameters
        ==========
        prepared
          If true, only return prepared spells.

        """
        spells = (item for item in self.json_data()["items"] if item["type"] == "spell")
        if prepared:
            spells = (d for d in spells if d["data"]["preparation"]["prepared"])
        spell_names = (d["name"] for d in spells)
        yield from spell_names

    def __call__(self):
        """Create a character property dictionary from the JSON file."""
        # Parse the json tree to get character properties
        char_props = {}
        json_data = self.json_data()
        details = json_data["data"]["details"]
        char_props["name"] = json_data["name"]
        char_props["background"] = details["background"]
        char_props["race"] = details["race"]
        char_props["alignment"] = details["alignment"]
        char_props["xp"] = self.as_int(details["xp"]["value"])
        classes, levels = zip(*self.class_levels())
        char_props["levels"] = list(levels)
        char_props["classes"] = list(classes)
        # Attributes
        attribute_names = {
            "str": "strength",
            "dex": "dexterity",
            "con": "constitution",
            "int": "intelligence",
            "wis": "wisdom",
            "cha": "charisma",
        }
        abilities = self.json_data()["data"]["abilities"]
        save_proficiences = []
        for abbr, attr in attribute_names.items():
            char_props[attr] = self.as_int(abilities[abbr]["value"])
            # Check proficiency
            is_proficient = bool(abilities[abbr]["proficient"])
            if is_proficient:
                save_proficiences.append(attr)
        char_props["saving_throw_proficiencies"] = save_proficiences
        # Skill proficiencies
        skill_names = [
            "acrobatics",
            "animal_handling",
            "arcana",
            "athletics",
            "deception",
            "history",
            "insight",
            "intimidation",
            "investigation",
            "medicine",
            "nature",
            "perception",
            "performance",
            "persuasion",
            "religion",
            "sleight_of_hand",
            "stealth",
            "survival",
        ]
        skill_profs = [skill for skill in skill_names if self.skill_proficiency(skill)]
        char_props["skill_proficiencies"] = skill_profs
        skill_expertise = [
            skill for skill in skill_names if self.skill_expertise(skill)
        ]
        char_props["skill_expertise"] = skill_expertise
        # Other proficiencies
        char_props["weapon_proficiencies"] = self.proficiencies("weapon")
        char_props["languages"] = ", ".join(self.proficiencies("language"))
        # Tool proficiencies
        tool_labels = {
            "art": "artisan's tools",
            "disg": "disguise kit",
            "forg": "forger's kit",
            "game": "gaming set",
            "herb": "herbalism kit",
            "music": "musical instrument",
            "navg": "navigator's tools",
            "pois": "poisoner's kit",
            "thief": "thieves' tools",
            "vehicle": "vehicle (land or water)",
        }
        tool_profs = json_data["data"]["traits"]["toolProf"]["value"]
        tool_profs = [tool_labels[prof] for prof in tool_profs]
        custom_tool_profs = json_data["data"]["traits"]["toolProf"]["custom"]
        tool_profs.extend([s.strip() for s in custom_tool_profs.split(";")])
        char_props["proficiencies_text"] = tool_profs
        # Combat stats
        char_props["hp_max"] = self.as_int(json_data["data"]["attributes"]["hp"]["max"])
        # Equipment
        currency = json_data["data"]["currency"]
        char_props["cp"] = currency["cp"]
        char_props["sp"] = currency["sp"]
        char_props["ep"] = currency["ep"]
        char_props["gp"] = currency["gp"]
        char_props["pp"] = currency["pp"]
        char_props["weapons"] = list(self.weapons())
        char_props["equipment"] = ", ".join(self.equipment())
        char_props["armor"] = self.armor()
        char_props["shield"] = self.shield()
        # Personality, etc
        char_props["personality_traits"] = details["trait"].strip()
        char_props["flaws"] = details["flaw"].strip()
        char_props["ideals"] = details["ideal"].strip()
        char_props["bonds"] = details["bond"].strip()
        # Spells
        char_props["spells"] = self.spells()
        char_props["spells_prepared"] = self.spells(prepared=True)
        # Some unused values
        warn_msg = (
            "Importing the following traits from JSON is not yet supported: "
            "magic_items, attacks_and_spellcasting, "
            "infusions, wild_shapes."
        )
        warnings.warn(warn_msg)
        log.warning(warn_msg)
        char_props["magic_items"] = ()
        char_props["attacks_and_spellcasting"] = ""
        char_props["infusions"] = []
        char_props["wild_shapes"] = []
        return char_props


class PythonCharacterReader(BaseCharacterReader):
    def __call__(self):
        """Create a character object from the given definition file.

        The definition file should be an importable python file, filled
        with variables describing the character.

        Parameters
        ----------
        filename
          The path to the file that will be imported.

        """
        filename = self.filename
        # Check if this file contains the version string
        version_re = re.compile(r'dungeonsheets_version\s*=\s*[\'"]([0-9.]+)[\'"]')
        with open(filename, mode="r") as f:
            version = None
            for line in f:
                match = version_re.match(line)
                if match:
                    version = match.group(1)
                    break
            if version is None:
                # Not a valid DND character file
                raise exceptions.CharacterFileFormatError(
                    f"No ``dungeonsheets_version = `` entry in `{filename}`."
                )
        # Import the module to extract the information
        spec = importlib.util.spec_from_file_location("module", filename)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        # Prepare a list of properties for this character
        char_props = {}
        for prop_name in dir(module):
            if prop_name[0:2] != "__":
                char_props[prop_name] = getattr(module, prop_name)
        return char_props


readers_by_extension = {
    ".py": PythonCharacterReader,
    ".json": json_character_reader,
}
