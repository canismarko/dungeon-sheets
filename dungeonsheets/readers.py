import importlib
import warnings
import json
import re
from functools import lru_cache
import logging

from pathlib import Path


from dungeonsheets import exceptions
from dungeonsheets import spells

log = logging.getLogger(__file__)


def read_character_file(filename: str):
    """Create a character object from the given definition file.
    
    The definition file should be an importable python file or a JSON
    file following one of the supported formats, filled with variables
    describing the character.
    
    Parameters
    ----------
    filename
      The path to the file that will be imported.
    
    """
    filename = Path(filename)
    # Parse the file name
    dir_ = filename.parent
    fname = filename.name
    ext = filename.suffix
    try:
        reader = readers_by_extension[ext]()
    except KeyError:
        raise ValueError(f"Character definition {filename} is not a known file type.")
    else:
        new_char = reader(filename=filename)
    return new_char


class BaseCharacterReader():
    """Callable to parse a generic character file. Meant to be subclassed."""
    def __call__(self, filename):
        """
        Parameters
        ----------
        filename
          The path to the file that will be imported.
        """
        raise NotImplementedError()


class JSONCharacterReader(BaseCharacterReader):
    """Callable to parse a JSON character file from Roll20 VVTES.
    
    The definition file should be a JSON file following one of the
    supported formats, filled with variables describing the character.
        
    Parameters
    ----------
    filename
      The path to the file that will be imported.
    
    """
    @lru_cache()
    def json_data(self):
        # Load the JSON data from disk
        with open(self.filename, mode='r') as fp:
            data = json.load(fp)
        return data

    def as_int(self, val):
        try:
            val = int(val)
        except ValueError:
            val = 0
        return val
    
    def get_attrib(self, key, which="current", default=None):
        for obj in self.json_data()['attribs']:
            if obj['name'] == key:
                val = obj[which]
                return val
        # No object was found
        if default is not None:
            return default
        else:
            raise KeyError(key)
    
    def has_skill_proficiency(self, key):
        false_profs = ['', '0']
        return self.get_attrib(key=f"{key}_prof") not in false_profs
    
    def spells(self, prepared: bool=False):
        """Iterator over the spells the character knows.
        
        Parameters
        ==========
        prepared
          If true, only return prepared spells.
        
        """
        # "name": "repeating_spell-cantrip_-MEzYWPA5cUZYd4ZOvMS_spellname",
        prof_re = re.compile("repeating_spell-(cantrip|[0-9]+)_([-0-9a-zA-Z]+)_spellname")
        for obj in self.json_data()['attribs']:
            match = prof_re.match(obj['name'])
            if match:
                level = match.group(1)
                spell_id = match.group(2)
                spell_name = self.get_attrib(f"repeating_spell-{level}_{spell_id}_spellname")
                is_prepared = self.as_int(self.get_attrib(f"repeating_spell-{level}_{spell_id}_spellprepared", default=0))
                if not prepared or is_prepared:
                    yield spell_name.lower()
    
    def proficiencies(self, kind=None):
        """Iterator over the skills in which the character is proficient.
        
        *kind* can be one of "weapon", "language", or None (all
         proficiencies).
        
        """
        prof_re = re.compile("repeating_proficiencies_([-0-9a-zA-Z]+)_name")
        for obj in self.json_data()['attribs']:
            match = prof_re.match(obj['name'])
            if match:
                prof_id = match.group(1)
                prof_type = self.get_attrib(f"repeating_proficiencies_{prof_id}_prof_type")
                if kind is None or prof_type == kind.upper():
                    yield self.get_attrib(f"repeating_proficiencies_{prof_id}_name").lower()
    
    def equipment(self, kind=None):
        """Iterator over items in the character's inventory.
        
        """
        prof_re = re.compile("repeating_inventory_([-0-9a-zA-Z]+)_itemname")
        for obj in self.json_data()['attribs']:
            match = prof_re.match(obj['name'])
            if match:
                item_id = match.group(1)
                item_name = self.get_attrib(match.group(0))
                item_count = int(self.get_attrib(f"repeating_inventory_{item_id}_itemcount", default=1))
                item_weight = self.get_attrib(f"repeating_inventory_{item_id}_itemweight", default=0)
                item_str = item_name.lower().strip()
                if item_count > 1:
                    item_str += f" ({item_count})"
                yield item_str
                    
    def weapons(self):
        """Iterator over the weapons the character is carrying in her inventory."""
        item_re = re.compile("repeating_attack_([-0-9a-zA-Z]+)_atkname")
        for obj in self.json_data()['attribs']:
            match = item_re.match(obj['name'])
            if match:
                weapon_name = self.get_attrib(match.group()).lower()
                weapon_name = weapon_name.split('(')[0].strip()
                weapon_name = weapon_name.split(',')[0].strip()
                yield weapon_name
    
    def __call__(self, filename: str):
        """Create a character property dictionary from the JSON file."""
        # Verify the version compatibility
        self.filename = filename
        version = self.json_data()['schema_version']
        if version != 2:
            raise exceptions.JSONFormatError("Cannot parse JSON schema version: %s" % version)
        # Parse the json tree to get character properties
        char_props = {}
        char_props['name'] = self.json_data()['name']
        char_props['level'] = self.as_int(self.get_attrib('base_level'))
        char_props['classes'] = [self.get_attrib('class')]
        char_props['background'] = self.get_attrib('background')
        char_props['race'] = self.get_attrib('subrace')
        char_props['alignment'] = self.get_attrib('alignment')
        char_props['xp'] = self.as_int(self.get_attrib('experience', default=0))
        # Attributes
        attribute_names = ['strength', 'dexterity', 'constitution',
                           'intelligence', 'wisdom', 'charisma']
        for attr in attribute_names:
            char_props[attr] = self.as_int(self.get_attrib(f"{attr}_base"))
        # Skill proficiencies
        skill_names = ['acrobatics', 'animal_handling', 'arcana',
                       'athletics', 'deception', 'history', 'insight', 'intimidation',
                       'investigation', 'medicine', 'nature', 'perception',
                       'performance', 'persuasion', 'religion', 'sleight_of_hand',
                       'stealth', 'survival']
        skill_profs = [skill for skill in skill_names if self.has_skill_proficiency(skill)]
        char_props['skill_proficiencies'] = skill_profs
        # Other proficiencies
        char_props['weapon_proficiencies'] = self.proficiencies("weapon")
        char_props['languages'] = ", ".join(self.proficiencies("language"))
        # Tool proficiencies
        prof_re = re.compile("repeating_tool_([-0-9a-zA-Z]+)_toolname")
        tool_profs = []
        for obj in self.json_data()['attribs']:
            match = prof_re.match(obj['name'])
            if match:
                tool_profs.append(self.get_attrib(match.group(0)))
        char_props['_proficiencies_text'] = tool_profs
        # Combat stats
        char_props['hp_max'] = self.as_int(self.get_attrib('hp', which="max"))
        # Equipment
        char_props['cp'] = self.as_int(self.get_attrib('cp', default=0))
        char_props['sp'] = self.as_int(self.get_attrib('sp', default=0))
        char_props['ep'] = self.as_int(self.get_attrib('ep', default=0))
        char_props['gp'] = self.as_int(self.get_attrib('gp', default=0))
        char_props['pp'] = self.as_int(self.get_attrib('pp', default=0))
        char_props['weapons'] = self.weapons()
        char_props['equipment'] = ", ".join(self.equipment())
        # Personality, etc
        char_props['personality_traits'] = self.get_attrib('personality_traits').strip()
        char_props['flaws'] = self.get_attrib('flaws').strip()
        char_props['ideals'] = self.get_attrib('ideals').strip()
        char_props['bonds'] = self.get_attrib('bonds').strip()
        # Spells
        char_props["spells"] = self.spells()
        char_props["spells_prepared"] = self.spells(prepared=True)
        # Some unused values
        warn_msg = ("Importing the following traits from JSON is not yet supported: "
                    "magic_items, armor, shield, attacks_and_spellcasting, "
                    "infusions, wild_shapes")
        warnings.warn(warn_msg)
        log.warning(warn_msg)
        char_props['magic_items'] = ()
        char_props['armor'] = ""
        char_props["shield"] = ""
        char_props["attacks_and_spellcasting"] = ""
        char_props["infusions"] = []
        char_props["wild_shapes"] = []
        return char_props


class PythonCharacterReader(BaseCharacterReader):
    def __call__(self, filename: str):
        """Create a character object from the given definition file.
        
        The definition file should be an importable python file, filled
        with variables describing the character.
        
        Parameters
        ----------
        filename
          The path to the file that will be imported.
        
        """
        # Check if this file contains the version string
        version_re = re.compile(r'dungeonsheets_version\s*=\s*[\'"]([0-9.]+)[\'"]')
        with open(filename, mode='r') as f:
            version = None
            for line in f:
                match = version_re.match(line)
                if match:
                    version = match.group(1)
                    break
            if version is None:
                # Not a valid DND character file
                raise exceptions.CharacterFileFormatError(
                    f"No ``dungeonsheets_version = `` entry in `{filename}`.")
        # Import the module to extract the information
        spec = importlib.util.spec_from_file_location('module', filename)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        # Prepare a list of properties for this character
        char_props = {}
        for prop_name in dir(module):
            if prop_name[0:2] != '__':
                char_props[prop_name] = getattr(module, prop_name)
        return char_props


readers_by_extension = {
    '.py': PythonCharacterReader,
    '.json': JSONCharacterReader,
}
