from typing import Mapping

from ebooklib import epub, ITEM_STYLE
from docutils import core
from sphinx.util.docstrings import prepare_docstring
from docutils.writers.html5_polyglot import Writer as HTMLWriter

from dungeonsheets.forms import dice_re, jinja_environment


def create_epub(
        chapters: Mapping,
        title: str,
        basename: str,
        use_dnd_decorations: bool = False
):
    """Prepare an EPUB file from the list of chapters.

    Parameters
    ==========
    chapters
      A mapping where the keys are chapter names (spines) and the
      values are strings of HTML to be rendered as the chapter
      contents.
    basename
      The basename for saving files (PDFs, etc). The resulting epub
      file will be "{basename}.epub".
    use_dnd_decorations
      If true, style sheets will be included to produce D&D stylized
      stat blocks, etc.

    """
    # Create a new epub book
    book = epub.EpubBook()
    book.set_identifier('id123456')
    book.set_title(title)
    book.set_language('en')
    # Add the css files
    css_template = jinja_env.get_template("dungeonsheets_epub.css")
    style = css_template.render(use_dnd_decorations=use_dnd_decorations)
    css = epub.EpubItem(uid="style_default", file_name="style/gm_sheet.css",
                        media_type="text/css", content=style)
    book.add_item(css)    
    # Create the separate chapters
    html_chapters = []
    for chap_title, content in chapters.items():
        chap_fname = "{}.html".format(chap_title.replace(" ", "_").lower())
        chapter = epub.EpubHtml(title=chap_title,
                                file_name=chap_fname, lang="en",
                                media_type="application/xhtml+xml")
        chapter.set_content(content)
        chapter.add_item(css)
        book.add_item(chapter)
        html_chapters.append(chapter)
    # Add the table of contents
    book.toc = html_chapters
    book.spine = ("nav", *html_chapters)
    # add default NCX and Nav file
    book.add_item(epub.EpubNcx())
    book.add_item(epub.EpubNav())
    # Save the file
    epub_fname = f"{basename}.epub"
    epub.write_epub(epub_fname, book)


def html_parts(
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
    writer = HTMLWriter()
    parts = core.publish_parts(
        source=input_string,
        source_path=source_path,
        destination_path=destination_path,
        writer=writer,
        settings_overrides=overrides,
    )
    return parts


def rst_to_html(rst, top_heading_level=0):
    """Basic markup of reST to HTML code.

    The translation between reST headings and LaTeX headings is
    modified by the *top_heading_level* parameter. A value of 0
    (default) translates "# Heading" -> "<h1>{Heading}</h1>". A value
    of 1 translates "# Heading" -> "<h2>{Heading}</h2>", etc.

    Note: heading translation is currently broken.

    Parameters
    ==========
    rst
      reStructured text input to be parsed.
    top_heading_level : optional
      The highest level heading that will be added to the HTML as
      described above.

    Returns
    =======
    html : str
      The reST text parsed into HTML markup.

    """
    if rst is None:
        # No reST, so return an empty string
        html = ""
    else:
        # Mark hit dice in monospace font
        rst = dice_re.sub(r"``\1``", rst)
        _html_parts = html_parts(rst)
        html = _html_parts["body"]
    return html


def to_heading_id(inpt: str) -> str:
    """Take a string and make it suitable for use as an HTML header id."""
    return inpt.replace(" ", "-")


# Prepare the jinja environment
jinja_env = jinja_environment()
jinja_env.filters['rst_to_html'] = rst_to_html
jinja_env.filters['to_heading_id'] = to_heading_id
