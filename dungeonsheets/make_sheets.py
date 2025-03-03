#!/usr/bin/env python

"""Program to take character definitions and build a PDF of the
character sheet."""

import argparse
import logging
import os
import re
import subprocess
import warnings
from itertools import product
from multiprocessing import Pool, cpu_count
from pathlib import Path
from pypdf import PdfReader, PdfWriter
from typing import Union, Sequence, Optional, List

from dungeonsheets import (
    character as _char,
    exceptions,
    readers,
    latex,
    epub,
    monsters,
    forms,
    random_tables,
)
from dungeonsheets.character import Character
from dungeonsheets.content import Creature
from dungeonsheets.content_registry import find_content
from dungeonsheets.fill_pdf_template import (
    create_character_pdf_template,
    create_personality_pdf_template,
    create_spells_pdf_template,
)
from dungeonsheets.pdf_image_insert import insert_image_into_pdf

log = logging.getLogger(__name__)

ORDINALS = {
    1: "1st",
    2: "2nd",
    3: "3rd",
    4: "4th",
    5: "5th",
    6: "6th",
    7: "7th",
    8: "8th",
    9: "9th",
}

PDFTK_CMD = "pdftk"

jinja_env = forms.jinja_environment()
jinja_env.filters["rst_to_latex"] = latex.rst_to_latex
jinja_env.filters["rst_to_html"] = epub.rst_to_html
jinja_env.filters["to_heading_id"] = epub.to_heading_id
jinja_env.filters["boxed"] = latex.rst_to_boxlatex
jinja_env.filters["spellsheetparser"] = latex.msavage_spell_info
jinja_env.filters["monsterdoc"] = latex.RPGtex_monster_info

# Custom types
File = Union[Path, str]


class CharacterRenderer:
    def __init__(self, template_name: str):
        self.template_name = template_name

    def __call__(
        self,
        character: Character,
        content_suffix: str = "tex",
        use_dnd_decorations: bool = False,
        spell_order: bool = False,
        feat_order: bool = False,
    ):
        template = jinja_env.get_template(
            self.template_name.format(suffix=content_suffix)
        )
        return template.render(
            character=character,
            use_dnd_decorations=use_dnd_decorations,
            spell_order=spell_order,
            feat_order=feat_order,
            ordinals=ORDINALS,
        )


create_character_sheet_content = CharacterRenderer("character_sheet_template.{suffix}")
create_subclasses_content = CharacterRenderer("subclasses_template.{suffix}")
create_features_content = CharacterRenderer("features_template.{suffix}")
create_magic_items_content = CharacterRenderer("magic_items_template.{suffix}")
create_spellbook_content = CharacterRenderer("spellbook_template.{suffix}")
create_infusions_content = CharacterRenderer("infusions_template.{suffix}")
create_druid_shapes_content = CharacterRenderer("druid_shapes_template.{suffix}")


def create_monsters_content(
    monsters: Sequence[Union[monsters.Monster, str]],
    suffix: str,
    use_dnd_decorations: bool = False,
    base_template: str = "monsters_template",
) -> str:
    # Convert strings to Monster objects
    template = jinja_env.get_template(base_template + f".{suffix}")
    spell_list = [Spell() for monster in monsters for Spell in monster.spells]
    return template.render(
        monsters=monsters,
        use_dnd_decorations=use_dnd_decorations,
        spell_list=spell_list,
    )


def create_gm_spellbook(spell_list, suffix):
    template = jinja_env.get_template(f"gm_spellbook_template.{suffix}")
    return template.render(spells=spell_list)


def create_party_summary_content(
    party: Sequence[Creature],
    summary_rst: str,
    suffix: str,
    use_dnd_decorations: bool = False,
) -> str:
    log.debug("Preparing summary table for party: %s", party)
    template = jinja_env.get_template(f"party_summary_template.{suffix}")
    return template.render(
        party=party, summary=summary_rst, use_dnd_decorations=use_dnd_decorations
    )


def create_random_tables_content(
    tables: Sequence[random_tables.RandomTable],
    suffix: str,
    use_dnd_decorations: bool = False,
) -> str:
    template = jinja_env.get_template(f"random_tables_template.{suffix}")
    return template.render(
        tables=tables,
        use_dnd_decorations=use_dnd_decorations,
    )


def create_extra_gm_content(
    sections: Sequence, suffix: str, use_dnd_decorations: bool = False
):
    """Create content for arbitrary additional text provided in a GM sheet.

    Parameters
    ==========
    sections
      Subclasses of Content that will each be included as new sections
      in the output document.

    """
    template = jinja_env.get_template(f"extra_gm_content.{suffix}")
    return template.render(sections=sections, use_dnd_decorations=use_dnd_decorations)


def make_sheet(
    sheet_file: File,
    flatten: bool = False,
    output_format: str = "pdf",
    fancy_decorations: bool = False,
    debug: bool = False,
    use_tex_template: bool = False,
    spell_order: bool = False,
    feat_order: bool = False,
):
    """Make a character or GM sheet into a PDF.
    Parameters
    ----------
    sheet_file
      File (.py) to load character from. Will save PDF using same name
    flatten : bool, optional
      If true, the resulting PDF will look better and won't be
      fillable form.
    output_format
      Either "pdf" or "epub" to generate a PDF file or an EPUB file.
    fancy_decorations : bool, optional
      Use fancy page layout and decorations for extra sheets, namely
      the dnd style file: ://github.com/rpgtex/DND-5e-LaTeX-Template.
    debug : bool, optional
      Provide extra info and preserve temporary files.
    use_tex_template : bool, optional
      (experimental) Use the DnD LaTeX character sheet instead of the fillable PDF.

    """
    # Parse the file
    sheet_file = Path(sheet_file)
    sheet_props = readers.read_sheet_file(sheet_file)
    # Create the sheet
    if sheet_props.get("sheet_type", "") == "gm":
        ret = make_gm_sheet(
            gm_file=sheet_file,
            output_format=output_format,
            fancy_decorations=fancy_decorations,
            debug=debug,
        )
    else:
        ret = make_character_sheet(
            char_file=sheet_file,
            flatten=flatten,
            output_format=output_format,
            fancy_decorations=fancy_decorations,
            debug=debug,
            use_tex_template=use_tex_template,
            spell_order=spell_order,
            feat_order=feat_order,
        )
    return ret


format_suffixes = {
    "pdf": "tex",
    "epub": "html",
}


def make_gm_sheet(
    gm_file: Union[str, Path],
    output_format: str = "pdf",
    fancy_decorations: bool = False,
    debug: bool = False,
):
    """Prepare a PDF character sheet from the given character file.

    Parameters
    ----------
    gm_file
      The file with the gm_sheet definitions.
    output_format
      Either "pdf" or "epub" to generate a PDF file or an EPUB file.
    fancy_decorations
      Use fancy page layout and decorations for extra sheets, namely
      the dnd style file: https://github.com/rpgtex/DND-5e-LaTeX-Template.
    debug
      Provide extra info and preserve temporary files.

    """
    # Parse the GM file and filename
    gm_file = Path(gm_file)
    basename = gm_file.stem
    gm_props = readers.read_sheet_file(gm_file)
    session_title = gm_props.pop("session_title", f"GM Notes: {basename}")
    # Create the intro tex
    content_suffix = format_suffixes[output_format]
    content = [
        jinja_env.get_template(f"preamble.{content_suffix}").render(
            use_dnd_decorations=fancy_decorations,
            title=session_title,
        )
    ]
    # Add the party stats table and session summary
    party = []
    for char_file in gm_props.pop("party", []):
        # Check if it's already resolved
        if isinstance(char_file, Creature):
            member = char_file
        elif isinstance(char_file, type) and issubclass(char_file, Creature):
            # Needs to be instantiated
            member = char_file()
        else:
            # Resolve the file path
            char_file = Path(char_file)
            if not char_file.is_absolute():
                char_file = gm_file.parent / char_file
            char_file = char_file.resolve()
            # Load the character file
            log.debug(f"Loading party member: {char_file}")
            character_props = readers.read_sheet_file(char_file)
            member = _char.Character.load(character_props)
        party.append(member)
    summary = gm_props.pop("summary", "")
    content.append(
        create_party_summary_content(
            party,
            summary_rst=summary,
            suffix=content_suffix,
            use_dnd_decorations=fancy_decorations,
        )
    )
    # Parse any extra homebrew sections, etc.
    content.append(
        create_extra_gm_content(
            sections=gm_props.pop("extra_content", []),
            suffix=content_suffix,
            use_dnd_decorations=fancy_decorations,
        )
    )
    # Add the monsters
    monsters_ = []
    input_monsters = list(gm_props.pop("monsters", []))
    for monster in input_monsters:
        if isinstance(monster, monsters.Monster):
            # It's already a monster, so just add it
            new_monster = monster
        elif isinstance(monster, type) and issubclass(monster, monsters.Monster):
            # Needs to be instantiated
            new_monster = monster()
        else:
            try:
                MyMonster = find_content(monster, valid_classes=[monsters.Monster])
            except exceptions.ContentNotFound:
                msg = f"Monster '{monster}' not found. Please add it to ``monsters.py``"
                warnings.warn(msg)
                continue
            else:
                # Make sure it's not already on the list
                if MyMonster in [type(m) for m in monsters_]:
                    continue
                new_monster = MyMonster()
        monsters_.append(new_monster)
    if len(monsters_) > 0:
        content.append(
            create_monsters_content(
                set(monsters_),
                suffix=content_suffix,
                use_dnd_decorations=fancy_decorations,
            )
        )

    # Add the GM Spellbook
    spells = []
    for monster in monsters_:
        for Spell in monster.spells:
            # Make sure it's not already on the list
            if Spell not in [type(spl) for spl in spells]:
                spells.append(Spell())
    # Alphabetical order
    spells = sorted(spells, key=lambda x: x.name)
    # Generate the content
    content.append(create_gm_spellbook(spells, content_suffix))
    # Add the random tables
    tables = [
        find_content(s, valid_classes=[random_tables.RandomTable])
        for s in gm_props.pop("random_tables", [])
    ]
    content.append(
        create_random_tables_content(
            tables=tables,
            suffix=content_suffix,
            use_dnd_decorations=fancy_decorations,
        )
    )
    # Add the closing TeX
    content.append(
        jinja_env.get_template(f"postamble.{format_suffixes[output_format]}").render(
            use_dnd_decorations=fancy_decorations
        )
    )
    # Warn about any unhandled sheet properties
    gm_props.pop("dungeonsheets_version")
    gm_props.pop("sheet_type")
    gm_props.pop("source_file_location")
    if len(gm_props.keys()) > 0:
        msg = f"Unhandled attributes in '{str(gm_file)}': {','.join(gm_props.keys())}"
        log.warning(msg)
        warnings.warn(msg)
    # Produce the combined output depending on the format requested
    if output_format == "pdf":
        # Typeset combined LaTeX file
        try:
            if len(content) > 2:
                latex.create_latex_pdf(
                    tex="".join(content),
                    basename=basename,
                    keep_temp_files=debug,
                    use_dnd_decorations=fancy_decorations,
                )
        except exceptions.LatexNotFoundError:
            log.warning(f"``pdflatex`` not available. Skipping {basename}")
    elif output_format == "epub":
        chapters = {session_title: "".join(content)}
        # Make sheets in the epub for each party member
        for char in party:
            char_html = make_character_content(
                char, "html", fancy_decorations=fancy_decorations
            )
            chapters[char.name] = "".join(char_html)
        # Create the combined HTML file
        epub.create_epub(
            chapters=chapters,
            basename=basename,
            title=session_title,
            use_dnd_decorations=fancy_decorations,
        )
    else:
        raise exceptions.UnknownOutputFormat(
            f"Unknown output format requested: {output_format}. Valid options are:"
            " 'pdf', 'epub'"
        )


def make_character_content(
    character: Character,
    content_format: str,
    fancy_decorations: bool = False,
    spell_order: bool = False,
    feat_order: bool = False,
) -> List[str]:
    """Prepare the inner content for a character sheet.

    This will produce a fully renderable document, suitable for
    passing to routines in either the ``epub`` or ``latex``
    modules. If *content_format* is ``"html"``, the returned content
    is just the portion that would be found inside the
    ``<body></body>`` tag.

    If *content_format* is ``"tex"``, the content returned will not
    include the character, spell list, or biography sheets, since
    these are currently processed through fillable PDFs.

    Parameters
    ----------
    character
      The character to render content for.
    content_format
      Which markup syntax to use, "tex" or "html".
    fancy_decorations
      Use fancy page layout and decorations for extra sheets, namely
      the dnd style file for *tex*, or extended CSS for *html*.

    Returns
    -------
    content
      The list of rendered character sheet contents for *character* in
      markup format *content_format*.

    """
    # Preamble, empty for HTML
    content = [
        jinja_env.get_template(f"preamble.{content_format}").render(
            use_dnd_decorations=fancy_decorations,
            title="Features, Magical Items and Spells",
        )
    ]
    # Make the character sheet, and background pages if producing HTML
    if content_format != "tex":
        content.append(
            create_character_sheet_content(
                character,
                content_suffix=content_format,
                use_dnd_decorations=fancy_decorations,
            )
        )
    # Create a list of subcasses, features, spells, etc
    if len(getattr(character, "subclasses", [])) > 0:
        content.append(
            create_subclasses_content(
                character,
                content_suffix=content_format,
                use_dnd_decorations=fancy_decorations,
            )
        )
    if len(getattr(character, "features", [])) > 0:
        content.append(
            create_features_content(
                character,
                content_suffix=content_format,
                use_dnd_decorations=fancy_decorations,
                feat_order=feat_order,
            )
        )
    if character.magic_items:
        content.append(
            create_magic_items_content(
                character,
                content_suffix=content_format,
                use_dnd_decorations=fancy_decorations,
            )
        )
    if len(getattr(character, "spells", [])) > 0:
        content.append(
            create_spellbook_content(
                character,
                content_suffix=content_format,
                use_dnd_decorations=fancy_decorations,
                spell_order=spell_order,
            )
        )
    if len(getattr(character, "infusions", [])) > 0:
        content.append(
            create_infusions_content(
                character,
                content_suffix=content_format,
                use_dnd_decorations=fancy_decorations,
            )
        )

    # Create a list of Druid wild_shapes
    if len(getattr(character, "all_wild_shapes", [])) > 0:
        content.append(
            create_druid_shapes_content(
                character,
                content_suffix=content_format,
                use_dnd_decorations=fancy_decorations,
            )
        )

    # Create a list of companions
    if len(getattr(character, "companions", [])) > 0:
        content.append(
            create_monsters_content(
                character.companions,
                suffix=content_format,
                use_dnd_decorations=fancy_decorations,
                base_template="companions_template",
            )
        )
    # Postamble, empty for HTML
    content.append(
        jinja_env.get_template(f"postamble.{content_format}").render(
            use_dnd_decorations=fancy_decorations
        )
    )
    return content


def msavage_sheet(character, basename, debug=False):
    """Another adaption. All changes can be easily included as options
    in the orignal functions, though."""

    # Load portrait image file if present
    portrait_command = ""
    if character.portrait:
        for image in character.images:
            if re.search(r"" + character.portrait, str(image[0])):
                character.images.remove(image)
                break
        portrait_command = r"\includegraphics[width=5.75cm]{" + character.portrait + "}"

    # Move symbol image a bit left, if applicable
    if character.symbol:
        for image in character.images:
            if re.search(r"" + character.symbol, str(image[0])):
                character.images.remove(image)
                character.images = [(character.symbol, 1, 488, 564, 145, 112)] + character.images
                break

    tex = jinja_env.get_template("MSavage_template.tex").render(
        char=character, portrait=portrait_command
    )
    latex.create_latex_pdf(
        tex,
        basename=basename,
        keep_temp_files=debug,
        use_dnd_decorations=True,
        comm1="xelatex",
    )


def make_character_sheet(
    char_file: Union[str, Path],
    character: Optional[Character] = None,
    flatten: bool = False,
    output_format: str = "pdf",
    fancy_decorations: bool = False,
    debug: bool = False,
    use_tex_template: bool = False,
    spell_order: bool = False,
    feat_order: bool = False,
):
    """Prepare a PDF character sheet from the given character file.

    Parameters
    ----------
    basename
      The basename for saving files (PDFs, etc).
    character
      If provided, will not load from the character file, just use
      file for PDF name
    flatten
      If true, the resulting PDF will look better and won't be
      fillable form.
    output_format
      Either "pdf" or "epub" to generate a PDF file or an EPUB file.
    fancy_decorations
      Use fancy page layout and decorations for extra sheets, namely
      the dnd style file: https://github.com/rpgtex/DND-5e-LaTeX-Template.
    debug
      Provide extra info and preserve temporary files.

    """
    # Load properties from file
    if character is None:
        character_props = readers.read_sheet_file(char_file)
        character = _char.Character.load(character_props)
    # Set the fields in the FDF
    basename = char_file.stem
    char_base = basename + "_char"
    person_base = basename + "_person"
    sheets = [char_base + ".pdf"]
    pages = []
    # Prepare the tex/html content
    content_suffix = format_suffixes[output_format]
    # Create a list of features and magic items
    content = make_character_content(
        character=character,
        content_format=content_suffix,
        fancy_decorations=fancy_decorations,
        spell_order=spell_order,
        feat_order=feat_order,
    )
    # Typeset combined LaTeX file
    if output_format == "pdf":
        if use_tex_template:
            msavage_sheet(
                character=character,
                basename=char_base,
                debug=debug,
            )
        # Fillable PDF forms
        else:
            sheets.append(person_base + ".pdf")
            char_pdf = create_character_pdf_template(
                character=character, basename=char_base, flatten=flatten
            )
            pages.append(char_pdf)
            person_pdf = create_personality_pdf_template(
                character=character,
                basename=person_base,
                flatten=flatten,
            )
            pages.append(person_pdf)
        if character.is_spellcaster and not (use_tex_template):
            # Create spell sheet
            spell_base = "{:s}_spells".format(basename)
            created_basenames = create_spells_pdf_template(
                character=character, basename=spell_base, flatten=flatten
            )
            for spell_base in created_basenames:
                sheets.append(spell_base + ".pdf")
        # Combined with additional LaTeX pages with detailed character info
        features_base = "{:s}_features".format(basename)
        try:
            if len(content) > 2:
                latex.create_latex_pdf(
                    tex="".join(content),
                    basename=features_base,
                    keep_temp_files=debug,
                    use_dnd_decorations=fancy_decorations,
                )
                sheets.append(features_base + ".pdf")
                final_pdf = f"{basename}.pdf"
                merge_pdfs(sheets, final_pdf, clean_up=not (debug))
                for image in character.images:
                    insert_image_into_pdf(final_pdf, *image)
        except exceptions.LatexNotFoundError:
            log.warning(
                f"``pdflatex`` not available. Skipping features for {character.name}"
            )
    elif output_format == "epub":
        epub.create_epub(
            chapters={character.name: "".join(content)},
            basename=basename,
            title=character.name,
            use_dnd_decorations=fancy_decorations,
        )
    else:
        raise exceptions.UnknownOutputFormat(
            f"Unknown output format requested: {output_format}. Valid options are:"
            " 'pdf', 'epub'"
        )


def merge_pdfs(src_filenames, dest_filename, clean_up=False):
    """Merge several PDF files into a single final file.

    src_filenames
      Iterable of source PDF file paths to use.
    dest_filename
      Path to requested PDF filename, will be overwritten if it
      exists.
    clean_up : optional
      If truthy, the ``src_filenames`` will be deleted once the
      ``dest_filename`` has been created.

    """
    popenargs = (PDFTK_CMD, *src_filenames, "cat", "output", dest_filename)
    try:
        subprocess.call(popenargs)
    except FileNotFoundError:
        warnings.warn(
            f"Could not run `{PDFTK_CMD}`, using fallback.", RuntimeWarning
        )

        merger = PdfWriter()
        for pdf in src_filenames:
            merger.append(pdf)
        merger.set_need_appearances_writer(True)
        merger.write(dest_filename)
        merger.close()
    finally:
        # Remove temporary files
        if clean_up:
            for sheet in src_filenames:
                os.remove(sheet)


def _build(filename, args) -> int:
    basename = filename.stem
    print(f"Processing {basename}...")
    try:
        make_sheet(
            sheet_file=filename,
            flatten=(not args.editable),
            output_format=args.output_format,
            debug=args.debug,
            fancy_decorations=args.fancy_decorations,
            use_tex_template=args.use_tex_template,
            spell_order=args.spell_order,
            feat_order=args.feat_order,
        )
    except exceptions.CharacterFileFormatError:
        # Only raise the failed exception if this file is explicitly given
        print(f"invalid {basename}")
        if args.filename:
            raise
    except Exception:
        print(f"{basename} failed")
        raise
    else:
        print(f"{basename} done")
    return 1


def main(args=None):
    # Prepare an argument parser
    parser = argparse.ArgumentParser(
        description="Prepare Dungeons and Dragons character sheets as PDFs"
    )
    parser.add_argument(
        "filename",
        type=str,
        nargs="*",
        help="File with character definition, or directory containing such files",
    )
    parser.add_argument(
        "--editable",
        "-e",
        action="store_true",
        help="Keep the PDF fields in place once processed",
    )
    parser.add_argument(
        "--recursive",
        "-r",
        action="store_true",
        help="Descend into subfolders looking for character files",
    )
    parser.add_argument(
        "--spells-by-level",
        "-S",
        default=False,
        action="store_true",
        help="Order spells by level in the feature pages.",
        dest="spell_order",
    )
    parser.add_argument(
        "--feats-by-type",
        "-N",
        default=False,
        action="store_true",
        help="Order feats by type in the feature pages.",
        dest="feat_order",
    )
    parser.add_argument(
        "--fancy-decorations",
        "--fancy",
        "-F",
        action="store_true",
        help=(
            "Render extra pages using fancy decorations "
            "(experimental, requires https://github.com/rpgtex/DND-5e-LaTeX-Template)"
        ),
    )
    parser.add_argument(
        "--tex-template",
        "-T",
        action="store_true",
        help="(experimental) Build character sheets using the LaTeX template instead of the fillable PDF.",
        dest="use_tex_template",
    )
    parser.add_argument(
        "--output-format",
        "-o",
        help="Specify the output format for the sheets.",
        choices=["pdf", "epub"],
        default="pdf",
    )
    parser.add_argument(
        "--debug",
        "-d",
        action="store_true",
        help="Provide verbose logging for debugging purposes.",
    )
    args = parser.parse_args(args)
    # Prepare logging if necessary
    if args.debug:
        logging.basicConfig(level=logging.DEBUG)
    # Build the true list of filenames
    input_filenames = args.filename
    known_extensions = readers.readers_by_extension.keys()
    if input_filenames == []:
        input_filenames = [Path()]
    else:
        input_filenames = [Path(f) for f in input_filenames]

    def get_char_files(fpath, parse_dirs=False):
        valid_files = []
        if fpath.is_dir() and parse_dirs:
            for f in fpath.iterdir():
                valid_files.extend(get_char_files(f, parse_dirs=args.recursive))
        elif fpath.suffix in known_extensions:
            valid_files.append(fpath)
        else:
            log.info(f"Unhandled file: {str(fpath)}")
        return valid_files

    temp_filenames = []
    for fpath in input_filenames:
        temp_filenames.extend(get_char_files(fpath, parse_dirs=True))
    # IMPORTANT:
    # Check that the files are valid dungeonsheets files without importing them
    filenames = []
    version_re = re.compile(
        r"^dungeonsheets_version = [\'\"](?P<version>[0-9.]+)[\'\"]\s*$", re.MULTILINE
    )
    for fpath in temp_filenames:
        with open(fpath, mode="r") as fp:
            if version_re.search(fp.read()) or fpath.suffix != ".py":
                filenames.append(fpath)
    # Process the requested files
    if args.debug:
        for filename in filenames:
            log.debug("building")
            _build(filename, args)
    else:
        with Pool(cpu_count()) as p:
            p.starmap(_build, product(filenames, [args]))


if __name__ == "__main__":
    main()
