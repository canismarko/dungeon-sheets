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
):
    # Create tex document
    tex_file = f"{basename}.tex"
    with open(tex_file, mode="w", encoding="utf-8") as f:
        f.write(tex)

    # Compile the PDF
    pdf_file = Path(f"{basename}.pdf")
    output_dir = pdf_file.resolve().parent
    tex_command_line = [
        "pdflatex",
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
    environment['TEXINPUTS'] = f".:{':'.join(str(d) for d in module_dirs)}:" + tex_env
    passes = 2 if use_dnd_decorations else 1
    log.debug(tex_command_line)
    log.debug("LaTeX command: %s" % " ".join(tex_command_line))
    log.debug("LaTeX environ: %s" % environment)
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


def rst_to_latex(rst, top_heading_level=0):
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
        rst = dice_re.sub(r"``\1``", rst)
        tex_parts = latex_parts(rst)
        tex = tex_parts["body"]
    return tex
