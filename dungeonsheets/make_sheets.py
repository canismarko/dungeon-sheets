#!/usr/bin/env python

import argparse
import importlib.util
import os
import subprocess

from fdfgen import forge_fdf

from dungeonsheets import character
from dungeonsheets.stats import mod_str

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
        ('ProfBonus', mod_str(character.proficiency_bonus)),
        ('STRmod', str(character.strength.value)),
        ('STR', mod_str(character.strength.modifier)),
        ('DEXmod ', character.dexterity.value),
        ('DEX', mod_str(character.dexterity.modifier)),
        ('CONmod', character.constitution.value),
        ('CON', mod_str(character.constitution.modifier)),
        ('INTmod', character.intelligence.value),
        ('INT', mod_str(character.intelligence.modifier)),
        ('WISmod', character.wisdom.value),
        ('WIS', mod_str(character.wisdom.modifier)),
        ('CHamod', character.charisma.value),
        ('CHA', mod_str(character.charisma.modifier)),
        ('AC', character.armor_class),
        ('Initiative', mod_str(character.dexterity.modifier)),
        ('Speed', character.speed),
        # Hit points
        ('HDTotal', character.hit_dice),
        ('HPMax', character.hp_max),
        # Inventory
        ('CP', character.cp),
        ('SP', character.sp),
        ('EP', character.ep),
        ('GP', character.gp),
        ('PP', character.pp),
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
    class_name = char_props.pop('character_class').lower().capitalize()
    CharClass = getattr(character, class_name)
    char = CharClass(**char_props)
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
    # Prepare an argument parser
    parser = argparse.ArgumentParser(
        description='Prepare Dungeons and Dragons character sheets as PDFs')
    parser.add_argument('filename', type=str, help="Python file with character definition")
    parser.add_argument('--flatten', '-F', action="store_true", help="Remove the PDF fields once processed.")
    args = parser.parse_args()
    # Process the requested file
    make_sheet(character_file=args.filename, flatten=args.flatten)


if __name__ == '__main__':
    main()
