import os
import subprocess
import logging
import warnings
import io

import pdfrw
from fdfgen import forge_fdf
from reportlab.pdfgen import canvas

from dungeonsheets.forms import mod_str

CHECKBOX_ON = "Yes"
CHECKBOX_OFF = "Off"
PDFTK_CMD = "pdftk"

log = logging.getLogger(__name__)


def text_box(string):
    """Format a string for displaying in a text box."""
    # remove multiple whitespace without removing linebreaks
    new_string = " ".join(string.replace("\n", "\m").split())  # noqa: W605
    # Remove *single* line breaks, swap *multi* line breaks to single (fdf: \r)
    new_string = (
        new_string.replace("\m \m", "\r")  # noqa: W605
        .replace("\m\m", "\r")  # noqa: W605
        .replace("\m", " ")  # noqa: W605
    )
    return new_string


def create_character_pdf_template(character, basename, flatten=False):
    # Prepare the list of fields
    fields = {
        # Character description
        "CharacterName": character.name,
        "ClassLevel": character.classes_and_levels,
        "Background": str(character.background),
        "PlayerName": character.player_name,
        "Race ": str(character.race),
        "Alignment": character.alignment,
        "XP": str(character.xp),
        "Inspiration": str("Yes" if character.inspiration else ""),
        # Abilities
        "ProfBonus": mod_str(character.proficiency_bonus),
        "STRmod": str(character.strength.value),
        "STR": mod_str(character.strength.modifier),
        "DEXmod ": str(character.dexterity.value),
        "DEX": mod_str(character.dexterity.modifier),
        "CONmod": str(character.constitution.value),
        "CON": mod_str(character.constitution.modifier),
        "INTmod": str(character.intelligence.value),
        "INT": mod_str(character.intelligence.modifier),
        "WISmod": str(character.wisdom.value),
        "WIS": mod_str(character.wisdom.modifier),
        "CHamod": str(character.charisma.value),
        "CHA": mod_str(character.charisma.modifier),
        "AC": str(character.armor_class),
        "Initiative": str(character.initiative),
        "Speed": str(character.speed),
        "Passive": character.passive_wisdom,
        # Saving throws (proficiencies handled later)
        "ST Strength": mod_str(character.strength.saving_throw),
        "ST Dexterity": mod_str(character.dexterity.saving_throw),
        "ST Constitution": mod_str(character.constitution.saving_throw),
        "ST Intelligence": mod_str(character.intelligence.saving_throw),
        "ST Wisdom": mod_str(character.wisdom.saving_throw),
        "ST Charisma": mod_str(character.charisma.saving_throw),
        # Skills (proficiencies handled below)
        "Acrobatics": mod_str(character.acrobatics.modifier),
        "Animal": mod_str(character.animal_handling.modifier),
        "Arcana": mod_str(character.arcana.modifier),
        "Athletics": mod_str(character.athletics.modifier),
        "Deception ": mod_str(character.deception.modifier),
        "History ": mod_str(character.history.modifier),
        "Insight": mod_str(character.insight.modifier),
        "Intimidation": mod_str(character.intimidation.modifier),
        "Investigation ": mod_str(character.investigation.modifier),
        "Medicine": mod_str(character.medicine.modifier),
        "Nature": mod_str(character.nature.modifier),
        "Perception ": mod_str(character.perception.modifier),
        "Performance": mod_str(character.performance.modifier),
        "Persuasion": mod_str(character.persuasion.modifier),
        "Religion": mod_str(character.religion.modifier),
        "SleightofHand": mod_str(character.sleight_of_hand.modifier),
        "Stealth ": mod_str(character.stealth.modifier),
        "Survival": mod_str(character.survival.modifier),
        # Hit points
        "HDTotal": character.hit_dice,
        "HPMax": str(character.hp_max),
        "HPCurrent": str(character.hp_current)
        if character.hp_current is not None
        else "",
        "HPTemp": str(character.hp_temp) if character.hp_temp > 0 else "",
        # Personality traits and other features
        "PersonalityTraits ": text_box(character.personality_traits),
        "Ideals": text_box(character.ideals),
        "Bonds": text_box(character.bonds),
        "Flaws": text_box(character.flaws),
        "Features and Traits": text_box(
            character.features_text + character.features_and_traits
        ),
        # Inventory
        "CP": character.cp,
        "SP": character.sp,
        "EP": character.ep,
        "GP": character.gp,
        "PP": character.pp,
        "Equipment": text_box(character.magic_items_text + character.equipment),
    }
    # Check boxes for proficiencies
    ST_boxes = {
        "strength": "Check Box 11",
        "dexterity": "Check Box 18",
        "constitution": "Check Box 19",
        "intelligence": "Check Box 20",
        "wisdom": "Check Box 21",
        "charisma": "Check Box 22",
    }
    for ability in character.saving_throw_proficiencies:
        fields[ST_boxes[ability]] = CHECKBOX_ON
    # Add skill proficiencies
    skill_boxes = {
        "acrobatics": "Check Box 23",
        "animal_handling": "Check Box 24",
        "arcana": "Check Box 25",
        "athletics": "Check Box 26",
        "deception": "Check Box 27",
        "history": "Check Box 28",
        "insight": "Check Box 29",
        "intimidation": "Check Box 30",
        "investigation": "Check Box 31",
        "medicine": "Check Box 32",
        "nature": "Check Box 33",
        "perception": "Check Box 34",
        "performance": "Check Box 35",
        "persuasion": "Check Box 36",
        "religion": "Check Box 37",
        "sleight_of_hand": "Check Box 38",
        "stealth": "Check Box 39",
        "survival": "Check Box 40",
    }
    for skill in character.skill_proficiencies:
        try:
            fields[skill_boxes[skill.replace(" ", "_").lower()]] = CHECKBOX_ON
        except KeyError:
            raise KeyError(f"Unknown skill: '{skill}'")
    # Add weapons
    weapon_fields = [
        ("Wpn Name", "Wpn1 AtkBonus", "Wpn1 Damage"),
        ("Wpn Name 2", "Wpn2 AtkBonus ", "Wpn2 Damage "),
        ("Wpn Name 3", "Wpn3 AtkBonus  ", "Wpn3 Damage "),
    ]
    for _fields, weapon in zip(weapon_fields, character.weapons):
        name_field, atk_field, dmg_field = _fields
        fields[name_field] = weapon.name
        fields[atk_field] = "{:+d}".format(weapon.attack_modifier)
        fields[dmg_field] = f"{weapon.damage}/{weapon.damage_type}"
    # Additional attacks beyond 3
    attack = [
        f"{w.name}: Atk {w.attack_modifier:+d}, Dam {w.damage}/{w.damage_type}"
        for w in character.weapons[len(weapon_fields) :]
    ]
    # Other attack information
    if character.armor:
        attack.append(f"Armor: {character.armor}")
    if character.shield:
        attack.append(f"Shield: {character.shield}")
    attack.append(character.attacks_and_spellcasting)
    attack_str = "\n\n".join(attack)
    fields["AttacksSpellcasting"] = text_box(attack_str)
    # Other proficiencies and languages
    prof_text = "Proficiencies:\n" + text_box(character.proficiencies_text)
    prof_text += "\n\nLanguages:\n" + text_box(character.languages)
    fields["ProficienciesLang"] = prof_text
    # Prepare the actual PDF
    dirname = os.path.join(os.path.dirname(os.path.abspath(__file__)), "forms/")
    src_pdf = os.path.join(dirname, "blank-character-sheet-default.pdf")
    return make_pdf(fields, src_pdf=src_pdf, basename=basename, flatten=flatten, portrait="")


def create_personality_pdf_template(character, basename, portrait_file="", flatten=False):
    # Prepare the list of fields
    fields = {
        "CharacterName 2": character.name,
        "Age": str(character.age),
        "Height": character.height,
        "Weight": character.weight,
        "Eyes": character.eyes,
        "Skin": character.skin,
        "Hair": character.hair,
        # "CHARACTER IMAGE": None
        # "Faction Symbol Image": None
        "Allies": text_box(character.allies),
        "FactionName": character.faction_name,
        "Backstory": text_box(character.backstory),
        "Feat+Traits": text_box(character.other_feats_traits),
        "Treasure": text_box(character.treasure),
    }
    # Prepare the actual PDF
    dirname = os.path.join(os.path.dirname(os.path.abspath(__file__)), "forms/")
    src_pdf = os.path.join(dirname, "blank-personality-sheet-default.pdf")
    return make_pdf(fields, src_pdf=src_pdf, basename=basename, flatten=flatten, portrait=portrait_file)


def create_spells_pdf_template(character, basename, flatten=False):
    classes_and_levels = " / ".join(
        [c.name + " " + str(c.level) for c in character.spellcasting_classes]
    )
    abilities = " / ".join(
        [c.spellcasting_ability.upper()[:3] for c in character.spellcasting_classes]
    )
    DCs = " / ".join(
        [str(character.spell_save_dc(c)) for c in character.spellcasting_classes]
    )
    bonuses = " / ".join(
        [
            mod_str(character.spell_attack_bonus(c))
            for c in character.spellcasting_classes
        ]
    )

    def spell_level(x):
        return x or 0

    fields = {
        "Spellcasting Class 2": classes_and_levels,
        "SpellcastingAbility 2": abilities,
        "SpellSaveDC  2": DCs,
        "SpellAtkBonus 2": bonuses,
        # Number of spell slots
        "SlotsTotal 19": spell_level(character.spell_slots(1)),
        "SlotsTotal 20": spell_level(character.spell_slots(2)),
        "SlotsTotal 21": spell_level(character.spell_slots(3)),
        "SlotsTotal 22": spell_level(character.spell_slots(4)),
        "SlotsTotal 23": spell_level(character.spell_slots(5)),
        "SlotsTotal 24": spell_level(character.spell_slots(6)),
        "SlotsTotal 25": spell_level(character.spell_slots(7)),
        "SlotsTotal 26": spell_level(character.spell_slots(8)),
        "SlotsTotal 27": spell_level(character.spell_slots(9)),
    }
    # Cantrips
    cantrip_fields = (f"Spells 10{i}" for i in (14, 16, 17, 18, 19, 20, 21, 22))
    cantrips = (spl for spl in character.spells if spl.level == 0)
    for spell, field_name in zip(cantrips, cantrip_fields):
        fields[field_name] = str(spell)
    # Spells for each level
    field_numbers = {
        1: (
            1015,
            1023,
            1024,
            1025,
            1026,
            1027,
            1028,
            1029,
            1030,
            1031,
            1032,
            1033,
        ),
        2: (
            1046,
            1034,
            1035,
            1036,
            1037,
            1038,
            1039,
            1040,
            1041,
            1042,
            1043,
            1044,
            1045,
        ),
        3: (
            1048,
            1047,
            1049,
            1050,
            1051,
            1052,
            1053,
            1054,
            1055,
            1056,
            1057,
            1058,
            1059,
        ),
        4: (
            1061,
            1060,
            1062,
            1063,
            1064,
            1065,
            1066,
            1067,
            1068,
            1069,
            1070,
            1071,
            1072,
        ),
        5: (
            1074,
            1073,
            1075,
            1076,
            1077,
            1078,
            1079,
            1080,
            1081,
        ),
        6: (
            1083,
            1082,
            1084,
            1085,
            1086,
            1087,
            1088,
            1089,
            1090,
        ),
        7: (
            1092,
            1091,
            1093,
            1094,
            1095,
            1096,
            1097,
            1098,
            1099,
        ),
        8: (
            10101,
            10100,
            10102,
            10103,
            10104,
            10105,
            10106,
        ),
        9: (10108, 10107, 10109, 101010, 101011, 101012, 101013),
    }
    prep_numbers = {
        1: (
            251,
            309,
            3010,
            3011,
            3012,
            3013,
            3014,
            3015,
            3016,
            3017,
            3018,
            3019,
        ),
        2: (
            313,
            310,
            3020,
            3021,
            3022,
            3023,
            3024,
            3025,
            3026,
            3027,
            3028,
            3029,
            3030,
        ),
        3: (
            315,
            314,
            3031,
            3032,
            3033,
            3034,
            3035,
            3036,
            3037,
            3038,
            3039,
            3040,
            3041,
        ),
        4: (
            317,
            316,
            3042,
            3043,
            3044,
            3045,
            3046,
            3047,
            3048,
            3049,
            3050,
            3051,
            3052,
        ),
        5: (
            319,
            318,
            3053,
            3054,
            3055,
            3056,
            3057,
            3058,
            3059,
        ),
        6: (
            321,
            320,
            3060,
            3061,
            3062,
            3063,
            3064,
            3065,
            3066,
        ),
        7: (
            323,
            322,
            3067,
            3068,
            3069,
            3070,
            3071,
            3072,
            3073,
        ),
        8: (
            325,
            324,
            3074,
            3075,
            3076,
            3077,
            3078,
        ),
        9: (
            327,
            326,
            3079,
            3080,
            3081,
            3082,
            3083,
        ),
    }
    # Prepare the lists of spells for each level
    for level in field_numbers.keys():
        spells = [spl for spl in character.spells if spl.level == level]
        # Determine if we should omit un-prepared spells to save space
        if len(spells) > len(field_numbers[level]):
            spells = [s for s in spells if s in character.spells_prepared]
            warnings.warn(
                f"{character.name} knows more spells than the number of "
                "lines available in spell sheet. Limited to prepared "
                "spells only."
            )
        # Build the list of PDF controls to set/toggle
        field_names = [f"Spells {i}" for i in field_numbers[level]]
        prep_names = tuple(f"Check Box {i}" for i in prep_numbers[level])
        for spell, field, chk_field in zip(spells, field_names, prep_names):
            fields[field] = str(spell)
            is_prepared = any([spell == Spl for Spl in character.spells_prepared])
            fields[chk_field] = CHECKBOX_ON if is_prepared else CHECKBOX_OFF
        # # Uncomment to post field names instead:
        # for field in field_names:
        #     fields.append((field, field))
    # Make the actual pdf
    dirname = os.path.join(os.path.dirname(os.path.abspath(__file__)), "forms/")
    src_pdf = os.path.join(dirname, "blank-spell-sheet-default.pdf")
    make_pdf(fields, src_pdf=src_pdf, basename=basename, flatten=flatten, portrait="")


def make_pdf(fields: dict, src_pdf: str, basename: str, flatten: bool = False, portrait = ""):
    """Create a new PDF by applying fields to a src PDF document.

    Parameters
    ==========
    fields :
      Data to fill into the form. The keys are field names in the PDF
      form, and the values will be entered as the value in the PDF.
    src_pdf :
      Path to the PDF that will serve as the template.
    basename :
      The path of the destination PDF without the file extensions. The
      resulting pdf will be {basename}.pdf
    flatten :
      If truthy, the PDF will be collapsed so it is no longer
      editable.

    """
    try:
        _make_pdf_pdftk(fields, src_pdf, basename, flatten, portrait)
    except FileNotFoundError:
        # pdftk could not run, so alert the user and use pdfrw
        warnings.warn(
            f"Could not run `{PDFTK_CMD}`, using fallback; forcing `--editable`.",
            RuntimeWarning,
        )
        _make_pdf_pdfrw(fields, src_pdf, basename, flatten, portrait)


def _make_pdf_pdfrw(fields: dict, src_pdf: str, basename: str, flatten: bool = False, portrait = ""):
    """Backup make_pdf function in case pdftk is not available."""
    template = pdfrw.PdfReader(src_pdf)
    # Different types of PDF fields
    BUTTON = "/Btn"
    # Names for entries in PDF annotation list
    # DEFAULT_VALUE = "/DV"
    # APPEARANCE = "/MK"
    FIELD = "/T"
    # PROPS = "/P"
    TYPE = "/FT"
    # FLAGS = "/Ff"
    # SUBTYPE = "/Subtype"
    # ALL_KEYS = [
    #     "/DV",
    #     "/F",
    #     "/FT",
    #     "/Ff",
    #     "/MK",
    #     "/P",
    #     "/Rect",
    #     "/Subtype",
    #     "/T",
    #     "/Type",
    # ]
    annots = template.pages[0]["/Annots"]
    # Update each annotation if it's in the requested dictionary
    for annot in annots:
        this_field = annot[FIELD][1:-1]
        # Check if the field has a new value passed
        if this_field in fields.keys():
            val = fields[this_field]
            # Convert integers to strings
            if isinstance(val, int):
                val = str(val)
            log.debug(
                f"Set field '{this_field}' "
                f"({annot[TYPE]}) "
                f"to `{val}` ({val.__class__}) "
                f"in file '{basename}.pdf'"
            )
            # Prepare a PDF dictionary based on the fields properties
            if annot[TYPE] == BUTTON:
                # Radio buttons require special appearance streams
                if val == CHECKBOX_ON:
                    val = bytes(val, "utf-8")
                    pdf_dict = pdfrw.PdfDict(V=val, AS=val)
                else:
                    continue
            else:
                # All other widget types
                pdf_dict = pdfrw.PdfDict(V=val)
            annot.update(pdf_dict)
        else:
            log.debug(f"Skipping unused field '{this_field}' in file '{basename}.pdf'")
    # Now write the PDF to the new pdf file
    pdfrw.PdfWriter().write(f"{basename}.pdf", template)


def _make_pdf_pdftk(fields, src_pdf, basename, flatten=False, portrait=""):
    """More robust way to make a PDF, but has a hard dependency."""
    # Create the actual FDF file
    fdfname = basename + ".fdf"

    fdf = forge_fdf("", fields, [], [], [])
    fdf_file = open(fdfname, "wb")
    fdf_file.write(fdf)
    fdf_file.close()
    # Build the final flattened PDF documents
    if portrait != "":
        dest_pdf = basename + "-temp.pdf"
        image_pdf = basename + "_image_tmp.pdf"
        make_image_pdf(portrait, image_pdf)
    else:
        dest_pdf = basename + ".pdf"
    popenargs = [
        PDFTK_CMD,
        src_pdf,
        "fill_form",
        fdfname,
        "output",
        dest_pdf,
    ]
    if flatten:
        popenargs.append("flatten")
    subprocess.call(popenargs)
    # stamp with image
    if portrait != "":
        src_pdf = dest_pdf
        stamped_pdf = basename + ".pdf"
        popenargs = [
            PDFTK_CMD,
            src_pdf,
            "stamp",
            image_pdf,
            "output",
            stamped_pdf,
        ]
        popenargs.append("flatten")
        subprocess.call(popenargs)
        # Clean up
        os.remove(image_pdf)
        os.remove(dest_pdf)
    # Clean up temporary files
    os.remove(fdfname)

def make_image_pdf(src_img:str, dest_pdf:str):
    packet = io.BytesIO()
    can = canvas.Canvas(packet)
    x_start = 10
    y_start = 240
    can.drawImage(src_img, x_start, y_start, width=175, preserveAspectRatio=True, mask='auto')
    can.showPage()
    can.save()
 
    #move to the beginning of the StringIO buffer
    packet.seek(0)
 
    new_pdf = pdfrw.PdfReader(packet)
    pdfrw.PdfWriter().write(dest_pdf, new_pdf)
