#!/usr/bin/env python

import importlib.util
import os
import subprocess

from fdfgen import forge_fdf

from dungeonsheets.character import Character

"""Program to take character definitions and build a PDF of the
character sheet."""

def load_character_file(filename):
    """Create a character object from the given definition file.
    
    The definition file should be an importable python file, filled
    with variables describing the character.
    
    Parameters
    ----------
    filename : str
      The path to the file that will be imported.
    
    """
    # Parse the file name
    dir_, fname = os.path.split(os.path.abspath(filename))
    module_name, ext = os.path.splitext(fname)
    if ext != '.py':
        raise ValueError(f"Character definition {filename} is not a python file.")
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


def create_fdf(character, fdfname):
    # Prepare the list of fields
    class_level = (character.class_name + ' ' + str(character.level))
    fields = [
        # Character description
        ('CharacterName', character.name),
        ('ClassLevel', class_level),
        ('Background', character.background),
        ('PlayerName', character.player_name),
        ('Race ', character.race),
        ('Alignment', character.alignment),
        ('XP', character.xp),
        # Attributes
        ('STRmod', str(character.strength.value)),
        ('STR', character.strength.modifier_string),
        ('DEXmod ', character.dexterity.value),
        ('DEX', character.dexterity.modifier_string),
        ('CONmod', character.constitution.value),
        ('CON', character.constitution.modifier_string),
        ('INTmod', character.intelligence.value),
        ('INT', character.intelligence.modifier_string),
        ('WISmod', character.wisdom.value),
        ('WIS', character.wisdom.modifier_string),
        ('CHamod', character.charisma.value),
        ('CHA', character.charisma.modifier_string),
        # Hit points
        ('HDTotal', character.hit_dice),
        ('HPMax', character.hp_max),
        
    ]
    fdf = forge_fdf("", fields, [], [], [])
    fdf_file = open(fdfname, "wb")
    fdf_file.write(fdf)
    fdf_file.close()


def make_sheet(character_file, flatten=False):
    """Prepare a PDF character sheet from the given character file.
    
    Parameters
    ----------
    flatten : bool, optional
      If true, the resulting PDF will not be a fillable form.
    
    """
    # Create a character from the character definition
    char_props = load_character_file(character_file)
    char = Character(**char_props)
    # Set the fields in the FDF
    fdfname = os.path.splitext(character_file)[0] + '.fdf'
    create_fdf(character=char, fdfname=fdfname)
    # Build the final flattened PDF document
    dirname = os.path.dirname(os.path.abspath(__file__))
    src_pdf = os.path.join(dirname, 'blank-character-sheet-default.pdf')
    dest_pdf = os.path.splitext(character_file)[0] + '.pdf'
    popenargs = [
        'pdftk', src_pdf, 'fill_form', fdfname, 'output', dest_pdf,
    ]
    if flatten:
        popenargs.append('flatten')
    subprocess.call(popenargs)
    # Clean up temporary files
    os.remove(fdfname)


def main():
    make_sheet('examples/rogue.py')


if __name__ == '__main__':
    main()
