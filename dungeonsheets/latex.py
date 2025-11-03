import pathlib
from pathlib import Path
import os
import re
import subprocess
import logging

from docutils import core
from docutils.writers.latex2e import Writer, Table, LaTeXTranslator
from sphinx.util.docstrings import prepare_docstring

from dungeonsheets import exceptions
from dungeonsheets.forms import dice_re


log = logging.getLogger(__name__)


class LatexWriter(Writer):
    def __init__(self):
        super().__init__()
        self.translator_class = DNDTranslator


class DNDTable(Table):
    pass


class DNDTranslator(LaTeXTranslator):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.settings.table_style = ["borderless"]
        self.active_table = DNDTable(self, "supertabular")


def _remove_temp_files(basename_):
    # Convenience function for removing temporary files
    filenames = [
        Path(f"{basename_}.tex"),
        Path(f"{basename_}.aux"),
        Path(f"{basename_}.log"),
    ]
    for filename in filenames:
        if filename.exists():
            filename.unlink()


def create_latex_pdf(
    tex: str,
    basename: str,
    keep_temp_files: bool = False,
    use_dnd_decorations: bool = False,
    comm1: str = "pdflatex"
):
    # Create tex document
    tex_file = f"{basename}.tex"
    with open(tex_file, mode="w", encoding="utf-8") as f:
        f.write(tex)

    # Compile the PDF
    pdf_file = Path(f"{basename}.pdf")
    output_dir = pdf_file.resolve().parent
    tex_command_line = [
        comm1,
        "--output-directory",
        str(output_dir),
        "-halt-on-error",
        "-interaction=nonstopmode",
        str(tex_file),
    ]

    environment = os.environ
    tex_env = environment.get('TEXINPUTS', '')
    module_root = Path(__file__).parent / "modules/"
    module_dirs = [module_root / mdir for mdir in ["DND-5e-LaTeX-Template"]]
    log.debug(f"Loading additional modules from {module_dirs}.")
    texinputs = ['.', *module_dirs, module_root, tex_env]
    separator = ';' if isinstance(module_root, pathlib.WindowsPath) else ':'
    environment['TEXINPUTS'] = separator.join(str(path) for path in texinputs)
    passes = 2 if use_dnd_decorations else 1
    log.debug(tex_command_line)
    log.debug("LaTeX command: %s" % " ".join(tex_command_line))
    log.debug("LaTeX TEXINPUTS: %s" % texinputs)
    log.debug("LaTeX environ:")
    for key, val in environment.items():
        log.debug("    %s: %s" % (key, val))
    try:
        for i in range(passes):
            result = subprocess.run(
                tex_command_line, stdout=subprocess.DEVNULL, env=environment, timeout=30
            )
    except FileNotFoundError:
        # Remove temporary files
        _remove_temp_files(basename)
        raise exceptions.LatexNotFoundError()
    else:
        if result.returncode == 0 and not keep_temp_files:
            _remove_temp_files(basename)
        if result.returncode != 0:
            # Prepare to raise an exception
            logfile = Path(f"{basename}.log")
            err_msg = f"Processing of {basename}.tex failed. See {logfile} for details."
            # Load the log file for more details
            tex_error_msg = tex_error(logfile)
            if tex_error_msg:
                for line in tex_error_msg.split("\n"):
                    log.error(line)
            raise exceptions.LatexError(err_msg)
    finally:
        environment['TEXINPUTS'] = tex_env


def tex_error(logfile: Path) -> str:
    """Parse a LaTeX log file and look for errors."""
    has_error = False
    error_lines = []
    if logfile.exists():
        with open(logfile, mode="r") as fp:
            for line in fp.readlines():
                # Check for the start of an error message
                if "LaTeX Error" in line:
                    has_error = True
                # We've already found an error, so save this line for later
                if has_error:
                    error_lines.append(line)
    return "".join(error_lines)


def latex_parts(
    input_string,
    source_path=None,
    destination_path=None,
    input_encoding="unicode",
    doctitle=True,
    initial_header_level=1,
):
    """
    Given an input string, returns a dictionary of HTML document parts.

    Dictionary keys are the names of parts, and values are Unicode strings;
    encoding is up to the client.

    Parameters:

    - `input_string`: A multi-line text string; required.
    - `source_path`: Path to the source file or object.  Optional, but useful
      for diagnostic output (system messages).
    - `destination_path`: Path to the file or object which will receive the
      output; optional.  Used for determining relative paths (stylesheets,
      source links, etc.).
    - `input_encoding`: The encoding of `input_string`.  If it is an encoded
      8-bit string, provide the correct encoding.  If it is a Unicode string,
      use "unicode", the default.
    - `doctitle`: Disable the promotion of a lone top-level section title to
      document title (and subsequent section title to document subtitle
      promotion); enabled by default.
    - `initial_header_level`: The initial level for header elements (e.g. 1
      for "<h1>").
    """
    # Remove indentation, etc
    input_string = "\n".join(prepare_docstring(input_string))
    # Parse from rst to TeX
    overrides = {
        "input_encoding": input_encoding,
        "doctitle_xform": doctitle,
        "initial_header_level": initial_header_level,
        "use_latex_citations": True,
        "legacy_column_widths": False,
    }
    writer = LatexWriter()
    parts = core.publish_parts(
        source=input_string,
        source_path=source_path,
        destination_path=destination_path,
        writer=writer,
        settings_overrides=overrides,
    )
    return parts


def rst_to_latex(rst, top_heading_level: int=0, format_dice: bool = True, use_dnd_decorations=False):
    """Basic markup of reST to LaTeX code.

    The translation between reST headings and LaTeX headings is
    modified by the *top_heading_level* parameter. A value of 0
    (default) translates "# Heading" -> "\\section{Heading}". A value
    of 1 translates "# Heading" -> "\\subsection{Heading}", etc.

    Note: heading translation is currently broken.

    Parameters
    ==========
    rst
      reStructured text input to be parsed.
    top_heading_level : optional
      The highest level heading that will be added to the LaTeX as
      described above.
    format_dice
      If true, dice strings (e.g. "1d4") will be formatted in
      monospace font.

    Returns
    =======
    tex : str
      The reST text parsed into LaTeX markup.

    """
    if rst is None:
        # No reST, so return an empty string
        tex = ""
    else:
        # Mark hit dice in monospace font
        if format_dice:
            rst = dice_re.sub(r"``\1``", rst)
        tex_parts = latex_parts(rst)
        tex = tex_parts["body"]
    # Apply fancy D&D decorations
    if use_dnd_decorations:
        tex = tex.replace(r"\begin{supertabular}[c]", r"\begin{DndLongTable}[header=]")
        tex = tex.replace(r"\begin{supertabular}", r"\begin{DndLongTable}[header=]")
        tex = tex.replace(r"\end{supertabular}", r"\end{DndLongTable}")

        # Stretch table to the entire width of the text column.
        # First, get all table headers in tex and put them in a list. Each header
        # is a string.
        tableheader = re.findall(r"\\begin{DndLongTable}.*", tex)
        for header in tableheader:
            # Get all collumn widths, compute initial table width
            colwidths = [width for width in re.findall(r"0\.[0-9]+", str(header))]
            tablewidth = 0
            for width in colwidths:
                tablewidth += float(width)
            # Prepare the transformed header
            transformed_header = header
            for width in colwidths:
                # Transform the column width by dividing it by the initial table width
                transformed_width = str(round( float(width) / tablewidth, 3))
                # Replace the original width with the transformed width
                transformed_header = re.sub(width,
                                            transformed_width,
                                            transformed_header)
            # Replace the original table header with the transformed one
            tex = tex.replace(header, transformed_header)
        # Correct table header to the DndLongTable format.
        # First deal with the table caption, if present:
        tex = re.sub(r"(begin{DndLongTable}\[header=)\](.*?\n)\\multicolumn.*?\n(.*?)\n.*?\\\\\n",
                     r"\1\3]\2", tex, flags=re.M|re.DOTALL)
        # Next, take the first table row and define it as the first page table header:
        tex = re.sub(r"(begin{DndLongTable}\[header=.*?)\](.*?)\n(.*?\\\\)\n\n",
                     r"\1,firsthead={\3 }]\2\n", tex, flags=re.M|re.DOTALL)
    return tex


def rst_to_boxlatex(rst):
    """Adapted rst translation from dungeonsheets latex module, removing
    dice parsing and indentation."""

    if rst is None:
        return ""
    tex_parts = latex_parts(rst)
    tex = tex_parts["body"]
    tex = tex.replace('\n\n', ' \\\\\n')
    return tex


def msavage_spell_info(char):
    """Generates the spellsheet for msavage template."""
    headinfo = char.spell_casting_info["head"]
    font_options = {1:"", 2:r"\Large ", 3:r"\large "}
    selector = min(len(char.spellcasting_classes), 3)
    fs_command = font_options[selector]
    sc_classes = r"\SpellcastingClass{" \
                + fs_command \
                + headinfo["classes_and_levels"].replace(" / ", ", ") \
                + "}"
    sc_abilities = r"\SpellcastingAbility{" \
                + fs_command \
                + headinfo["abilities"].replace(" ", "") \
                + "}"
    sc_savedc = r"\SpellSaveDC{" \
                + fs_command \
                + headinfo["DCs"].replace(" ", "") \
                + "}"
    sc_atk = r"\SpellAttackBonus{" \
                + fs_command \
                + headinfo["bonuses"].replace(" ", "") \
                + "}"
    tex1 = "\n".join([sc_classes, sc_abilities, sc_savedc, sc_atk]) + "\n"
    spellslots = char.spell_casting_info["slots"]
    texT = []
    for k, v in spellslots.items():
        texT.append("\\" + k + "SlotsTotal{" + str(v) + "}")
    tex2 = "\n".join(texT) + "\n"
    texT = []
    level_names = level_names = ["Cantrip", 
                       'FirstLevelSpell',
                       'SecondLevelSpell',
                       'ThirdLevelSpell',
                       'FourthLevelSpell',
                       'FifthLevelSpell',
                       'SixthLevelSpell',
                       'SeventhLevelSpell',
                       'EighthLevelSpell',
                       'NinthLevelSpell']

    fullcaster_sheet_spaces = dict(zip(level_names,
                    [8, 13, 13, 13, 13, 9, 9, 9, 7, 7]))
    halfcaster_sheet_spaces = dict(zip(level_names,
                    [11, 26, 19, 19, 19, 0, 0, 0, 0, 0]))
    comp_letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", 
                  "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", 
                  "W", "X", "Y", "Z"]

    # spellList is a dict.
    # The keys in spellList are the level names, the values are lists of tuples:
    # Each tuple consists of two elements: a spell name and a boolean for prepared.
    # So: spellList = {levelname : [(spellname, preparedbool), ]}
    spellList = char.spell_casting_info["list"]
    # Default, assume fullcaster character and associated spellsheet.
    fullcaster = True
    # Determine which sheet to use (fullcaster or halfcaster).
    # Only use halfcaster when we have no spells > 5th level and
    # would overflow the fullcaster sheet.
    # Keep the same sheet for overflow pages, if any.
    if (any(len(spellList[key]) > fullcaster_sheet_spaces[key] for key in spellList.keys())
            and not any(name in spellList.keys() for name in level_names[6:10])):
        fullcaster = False

    def AddSpellPage(fullcaster = True):
        texT = []
        for k, v in spellList.items():
            spells_this_level_and_page = len(v)
            if fullcaster:
                spellsheet_command = "\\renderspellsheet"
                slots_max = fullcaster_sheet_spaces[k]
            else:
                spellsheet_command = "\\renderhalfspellsheet"
                slots_max = halfcaster_sheet_spaces[k]
            for spinfo, slot in zip(v[:slots_max], comp_letters):
                spellList[k].remove(spinfo)
                slot_command = "\\"+k+'Slot'+slot
                slot_command_name = slot_command+"{"+spinfo[0]+"}"
                if k == "Cantrip":
                    texT = texT + [slot_command_name]
                    continue
                slot_command_prep = slot_command+"Prepared"+"{"+str(spinfo[1])+"}"
                texT = texT + [slot_command_name, slot_command_prep]
            # Set remaining slots empty
            for empty_slot in comp_letters[spells_this_level_and_page:slots_max]:
                slot_command = "\\"+k+'Slot'+empty_slot
                slot_command_name = slot_command+"{}"
                if k == "Cantrip":
                    texT = texT + [slot_command_name]
                    continue
                slot_command_prep = slot_command+"Prepared{False}"
                texT = texT + [slot_command_name, slot_command_prep]
            if (not len(spellList[k]) == 0
                    and not spellList[k][0][0] == "--- Overflow ---"):
                spellList[k].insert(0, ("--- Overflow ---", False))
        return "\n".join(texT) + '\n\n' + spellsheet_command + '\n\n'

    tex3 = ""
    while any(spellList.values()):
        tex3 = tex3 + AddSpellPage(fullcaster)
    return "\n".join([tex1, tex2, tex3])


def RPGtex_monster_info(char):
    """Generates the headings for the monster block info in the DND latex style"""
    tex = """\n""" # Clean start with a newline
    # Counting sections here:
    # 0: Feats
    # 1: Actions and reactions
    # 2: Legendary Actions
    # 3: Other types of actions.
    # Challenges: Some monsters only have feats, some only have actions.
    sectiontype = 0
    sectionlist = char.split("    # ") # Four spaces, a hash, and another space
    for section in sectionlist:
        # First find out what type of section we're dealing with, and
        # set sectiontype accordingly;
        # The first section is either feats or actions. Set sectiontype to
        # actions (and format accordingly) if the first line matches
        # actions or reactions
        if re.match (r"^[re]*actions\n", section, re.IGNORECASE):
            sectiontype = 1
        elif re.match (r"^legendary actions\n", section, re.IGNORECASE):
            sectiontype = 2
        elif sectionlist.index(section) > 0: # Not the first section, nor does
            sectiontype = 3                  # it have any header we recognize

        # Now we latex format each section according to type, applying
        # rst_to_latex where it's convenient, and resorting to our own
        # means where necessary. Goal is to make use of DND-5e-LaTeX-Template
        # style as much as possible.
        if sectiontype == 0 or sectiontype == 3:
            # Use rst_to_latex first, because of easy itemization
            section = rst_to_latex(section) # This somehow adds a newline at the start of the section
            # Snip away begin and end description:
            section = re.sub (r"\\[a-z]+{description}\n", "", section)
            # Sub \item[{}] with \DndMonsterAction{} headers:
            section = re.sub (r"\\item\[{(.+)\.}\]", r"\\DndMonsterAction{\1}", section)
            if sectiontype == 3: # Add section header
                section = re.sub(r"^\n(.*)\n", r"\\DndMonsterSection{\1}", section)
            # Remove spurious newlines from the start of the section:
            section = re.sub (r"^\n", r"", section)
            # Remove spurious newlines from the end of the section:
            section = re.sub (r"\n\n$", r"\n", section)
            tex += section

        if sectiontype == 1:
            # Process the section line by line.
            subsection = ""
            lines = section.splitlines()
            for line in lines:
                if re.match (r"^\S", line):
                    line = re.sub(r"(.+)$", r"\n\\DndMonsterSection{\1}\n", line)
                    subsection += line
                else:
                    # Italicize weapon type and hit, and remove six leading spaces
                    line = re.sub(r"^ {6}(.+)\:(.+)(Hit)\: (.+)", r"\\textit{\1:} \2\\textit{\3:} \4 ", line)
                    # Remove leading spaces from other lines
                    line = re.sub(r"^ {6}(.+)", r"\1\n", line)
                    # Add DndMonsterAction header for each action, and remove four leading spaces
                    line = re.sub(r"^ {4}(\S.+)\.$", r"\\DndMonsterAction{\1}\n", line)
                    subsection += line
                    subsection = re.sub(r" {6}", "\n", subsection)
            # Dice
            subsection = re.sub(r"\((\d+)d(\d+)\s*([+-]*)\s*(\d*)\)", r" (\\texttt{\1d\2\3\4}) ", subsection)
            tex += subsection

        if sectiontype == 2:
            # First process the section line by line to only get the legendary actions,
            # then add section start, end and header.
            subsection = ""
            lines = section.splitlines()
            for line in lines:
                if re.match(r"^ {4}\S", line):
                    # New legendary action, remove leading spaces
                    line = re.sub(r"^ {4}(.+)\.$", r"\\DndMonsterLegendaryAction{\1}{}", line)
                    subsection += line + "\n"
                elif re.match(r"^ {6}\S", line):
                    # Remove leading spaces from other lines
                    line = re.sub(r"^ {6}(.+)", r"\1", line)
                    subsection += line + "\n"
            # Add section header and DndMonsterLegendaryActions environment
            subsection = ("\n\\DndMonsterSection{Legendary Actions}\n\\begin{DndMonsterLegendaryActions}\n" + subsection + "\\end{DndMonsterLegendaryActions}\n")
            # Put the curly braces in place
            subsection = re.sub(r"}{}\n(.+?)\n\\", r"}\n{\1}\n\\", subsection, re.MULTILINE, re.DOTALL)
            # Dice
            subsection = re.sub(r"\((\d+)d(\d+)\s*([+-]*)\s*(\d*)\)", r" (\\texttt{\1d\2\3\4})", subsection)
            tex += subsection
    return tex
