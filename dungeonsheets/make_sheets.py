#!/usr/bin/env python

import argparse
import importlib.util
import os
import subprocess
import warnings

from fdfgen import forge_fdf

from dungeonsheets import character
from dungeonsheets.stats import mod_str

"""Program to take character definitions and build a PDF of the
character sheet."""

def text_box(string):
    """Format a string for displaying in a text box."""
    # Remove line breaks
    new_string = string.replace('\n', ' ').replace('\r', ' ')
    # Remove multiple whitespace
    new_string = ' '.join(new_string.split())
    return new_string


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


def create_spells_pdf(character, basename, flatten=False):
    class_level = (character.class_name + ' ' + str(character.level))
    spell_level = lambda x : (x or '')
    fields = [
        ('Spellcasting Class 2', class_level),
        ("SpellcastingAbility 2", character.spellcasting_ability.capitalize()),
        ('SpellSaveDC  2', character.spell_save_dc),
        ('SpellAtkBonus 2', mod_str(character.spell_attack_bonus)),
        # Number of spell slots
        ('SlotsTotal 19', spell_level(character.spell_slots(1))),
        ('SlotsTotal 20', spell_level(character.spell_slots(2))),
        ('SlotsTotal 21', spell_level(character.spell_slots(3))),
        ('SlotsTotal 22', spell_level(character.spell_slots(4))),
        ('SlotsTotal 23', spell_level(character.spell_slots(5))),
        ('SlotsTotal 24', spell_level(character.spell_slots(6))),
        ('SlotsTotal 25', spell_level(character.spell_slots(7))),
        ('SlotsTotal 26', spell_level(character.spell_slots(8))),
        ('SlotsTotal 27', spell_level(character.spell_slots(9))),
    ]
    # Cantrips
    cantrip_fields = (f'Spells 10{i}' for i in (14, 16, 17, 18, 19, 20, 21, 22))
    cantrips = (spl for spl in character.spells if spl.level == 0)
    for spell, field_name in zip(cantrips, cantrip_fields):
        fields.append((field_name, spell.name))
    # Spells for each level
    field_numbers = {
        1: (1015, 1023, 1024, 1025, 1026, 1027, 1028, 1029, 1030, 1031, 1032, 1033, ),
        2: (1046, 1034, 1035, 1036, 1037, 1038, 1039, 1040, 1041, 1042, 1043, 1044, 1045, ),
        3: (1048, 1047, 1049, 1050, 1051, 1052, 1053, 1054, 1055, 1056, 1057, 1058, 1059, ),
        4: (1061, 1060, 1062, 1063, 1064, 1065, 1066, 1067, 1068, 1069, 1070, 1071, 1072, ),
        5: (1074, 1073, 1075, 1076, 1077, 1078, 1079, 1080, 1081, ),
        6: (1083, 1082, 1084, 1085, 1086, 1087, 1088, 1089, 1090, ),
        7: (1092, 1091, 1093, 1094, 1095, 1096, 1097, 1098, 1099, ),
        8: (10101, 10100, 10102, 10103, 10104, 10105, 10106, ),
        9: (10108, 10107, 10109, 101010, 101011, 101012, 101013),
    }
    prep_numbers = {
        1: (251, 309, 3010, 3011, 3012, 3013, 3014, 3015, 3016, 3017, 3018, 3019, ),
        2: (313, 310, 3020, 3021, 3022, 3023, 3024, 3025, 3026, 3027, 3028, 3029, 3030, ),
        3: (315, 314, 3031, 3032, 3033, 3034, 3035, 3036, 3037, 3038, 3039, 3040, 3041, ),
        4: (317, 316, 3042, 3043, 3044, 3045, 3046, 3047, 3048, 3049, 3050, 3051, 3052, ),
        5: (319, 318, 3053, 3054, 3055, 3056, 3057, 3058, 3059, ),
        6: (321, 320, 3060, 3061, 3062, 3063, 3064, 3065, 3066, ),
        7: (323, 322, 3067, 3068, 3069, 3070, 3071, 3072, 3073, ),
        8: (325, 324, 3074, 3075, 3076, 3077, 3078, ),
        9: (327, 326, 3079, 3080, 3081, 3082, 3083, ),
    }
    for level in field_numbers.keys():
        spells = tuple(spl for spl in character.spells if spl.level == level)
        field_names = tuple(f'Spells {i}' for i in field_numbers[level])
        prep_names = tuple(f'Check Box {i}' for i in prep_numbers[level])
        for spell, field, chk_field in zip(spells, field_names, prep_names):
            fields.append((field, spell.name))
            is_prepared = any([isinstance(spell, Spl) for Spl in character.spells_prepared])
            fields.append((chk_field, is_prepared))
        # # Uncomment to post field names instead:
        # for field in field_names:
        #     fields.append((field, field))
    fields.append(('Check Box 3083', True))
    # Make the actual pdf
    dirname = os.path.dirname(os.path.abspath(__file__))
    src_pdf = os.path.join(dirname, 'blank-spell-sheet-default.pdf')
    make_pdf(fields, src_pdf=src_pdf, basename=basename, flatten=flatten)


def create_character_pdf(character, basename, flatten=False):
    # Prepare the list of fields
    class_level = (character.class_name + ' ' + str(character.level))
    fields = [
        # Character description
        ('CharacterName', character.name),
        ('ClassLevel', class_level),
        ('Background', character.background),
        ('PlayerName', character.player_name),
        ('Race ', str(character.race)),
        ('Alignment', character.alignment),
        ('XP', character.xp),
        # Abilities
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
        ('Passive', 10 + character.perception),
        # Saving throws (proficiencies handled later)
        ('ST Strength', mod_str(character.strength.saving_throw)),
        ('ST Dexterity', mod_str(character.dexterity.saving_throw)),
        ('ST Constitution', mod_str(character.constitution.saving_throw)),
        ('ST Intelligence', mod_str(character.intelligence.saving_throw)),
        ('ST Wisdom', mod_str(character.wisdom.saving_throw)),
        ('ST Charisma', mod_str(character.charisma.saving_throw)),
        # Skills (proficiencies handled below)
        ('Acrobatics', mod_str(character.acrobatics)),
        ('Animal', mod_str(character.animal_handling)),
        ('Arcana', mod_str(character.arcana)),
        ('Athletics', mod_str(character.athletics)),
        ('Deception ', mod_str(character.deception)),
        ('History ', mod_str(character.history)),
        ('Insight', mod_str(character.insight)),
        ('Intimidation', mod_str(character.intimidation)),
        ('Investigation ', mod_str(character.investigation)),
        ('Medicine', mod_str(character.medicine)),
        ('Nature', mod_str(character.nature)),
        ('Perception ', mod_str(character.perception)),
        ('Performance', mod_str(character.performance)),
        ('Persuasion', mod_str(character.persuasian)),
        ('Religion', mod_str(character.religion)),
        ('SleightofHand', mod_str(character.sleight_of_hand)),
        ('Stealth ', mod_str(character.stealth)),
        ('Survival', mod_str(character.survival)),
        # Hit points
        ('HDTotal', character.hit_dice),
        ('HPMax', character.hp_max),
        # Personality traits and other features
        ('PersonalityTraits ', text_box(character.personality_traits)),
        ('Ideals', text_box(character.ideals)),
        ('Bonds', text_box(character.bonds)),
        ('Flaws', text_box(character.flaws)),
        ('AttacksSpellcasting', text_box(character.attacks_and_spellcasting)),
        ('Features and Traits', text_box(character.features_and_traits)),
        # Inventory
        ('CP', character.cp),
        ('SP', character.sp),
        ('EP', character.ep),
        ('GP', character.gp),
        ('PP', character.pp),
        ('Equipment', text_box(character.equipment)),
    ]
    # Check boxes for proficiencies
    ST_boxes = {
        'strength': 'Check Box 11',
        'dexterity': 'Check Box 18',
        'constitution': 'Check Box 19',
        'intelligence': 'Check Box 20',
        'wisdom': 'Check Box 21',
        'charisma': 'Check Box 22',
    }
    for ability in character.saving_throw_proficiencies:
        fields.append((ST_boxes[ability], 'Yes'))
    skill_boxes = {
        'acrobatics': 'Check Box 23',
        'animal_handling': 'Check Box 24',
        'arcana': 'Check Box 25',
        'athletics': 'Check Box 26',
        'deception': 'Check Box 27',
        'history': 'Check Box 28',
        'insight': 'Check Box 29',
        'intimidation': 'Check Box 30',
        'investigation': 'Check Box 31',
        'medicine': 'Check Box 32',
        'nature': 'Check Box 33',
        'perception': 'Check Box 34',
        'performance': 'Check Box 35',
        'persuasian': 'Check Box 36',
        'religion': 'Check Box 37',
        'sleight_of_hand': 'Check Box 38',
        'stealth': 'Check Box 39',
        'survival': 'Check Box 40',
    }
    # Add skill proficienies
    for skill in character.skill_proficiencies:
        fields.append((skill_boxes[skill], 'Yes'))
    # Add weapons
    weapon_fields = [('Wpn Name', 'Wpn1 AtkBonus', 'Wpn1 Damage'),
                     ('Wpn Name 2', 'Wpn2 AtkBonus ', 'Wpn2 Damage '),
                     ('Wpn Name 3', 'Wpn3 AtkBonus  ', 'Wpn3 Damage '),]
    for _fields, weapon in zip(weapon_fields, character.weapons):
        name_field, atk_field, dmg_field = _fields
        fields.append((name_field, weapon.name))
        fields.append((atk_field, mod_str(weapon.attack_bonus)))
        fields.append((dmg_field, f'{weapon.damage} {weapon.damage_type}'))
    # Other proficiencies and languages
    prof_text = "Proficiencies:\n" + text_box(character.proficiencies_text)
    prof_text += "\n\nLanguages:\n" + text_box(character.languages)
    fields.append(('ProficienciesLang', prof_text))
    # Prepare the actual PDF
    dirname = os.path.dirname(os.path.abspath(__file__))
    src_pdf = os.path.join(dirname, 'blank-character-sheet-default.pdf')
    return make_pdf(fields, src_pdf=src_pdf, basename=basename, flatten=flatten)


def make_pdf(fields, src_pdf, basename, flatten=False):
    # Create the actual FDF file
    fdfname = basename + '.fdf'
    fdf = forge_fdf("", fields, [], [], [])
    fdf_file = open(fdfname, "wb")
    fdf_file.write(fdf)
    fdf_file.close()
        # Build the final flattened PDF documents
    dest_pdf = basename + '.pdf'
    popenargs = [
        'pdftk', src_pdf, 'fill_form', fdfname, 'output', dest_pdf,
    ]
    if flatten:
        popenargs.append('flatten')
    subprocess.call(popenargs)
    # Clean up temporary files
    os.remove(fdfname)


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
    char_base = os.path.splitext(character_file)[0] + '_char'
    sheets = [char_base + '.pdf']
    create_character_pdf(character=char, basename=char_base, flatten=flatten)
    if char.is_spellcaster:
        spell_base = os.path.splitext(character_file)[0] + '_spells'
        create_spells_pdf(character=char, basename=spell_base, flatten=flatten)
        sheets.append(spell_base + '.pdf')
    # Combine sheets into final pdf
    final_pdf = os.path.splitext(character_file)[0] + '.pdf'
    popenargs = ('pdftk', *sheets, 'cat', 'output', final_pdf)
    subprocess.call(popenargs)
    # Remove temporary files
    for sheet in sheets:
        os.remove(sheet)


def main():
    # Prepare an argument parser
    parser = argparse.ArgumentParser(
        description='Prepare Dungeons and Dragons character sheets as PDFs')
    parser.add_argument('filename', type=str, nargs="?",
                        help="Python file with character definition")
    parser.add_argument('--flatten', '-F', action="store_true",
                        help="Remove the PDF fields once processed.")
    args = parser.parse_args()
    # Process the requested files
    if args.filename is None:
        filenames = [f for f in os.listdir('.') if os.path.splitext(f)[1] == '.py']
    else:
        filenames = [args.filename]
    for filename in filenames:
        print(f"Processing {os.path.splitext(filename)[0]}...", end='')
        try:
            make_sheet(character_file=filename, flatten=args.flatten)
        except Exception as e:
            print('failed')
            raise
        else:
            print("done")


if __name__ == '__main__':
    main()
