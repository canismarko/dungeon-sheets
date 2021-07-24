from typing import Mapping
from html.parser import HTMLParser
import re
from pathlib import Path

from ebooklib import epub, ITEM_STYLE
from docutils import core
from sphinx.util.docstrings import prepare_docstring
from docutils.writers.html5_polyglot import Writer as HTMLWriter

from dungeonsheets.forms import dice_re, jinja_environment


def create_epub(
    chapters: Mapping, title: str, basename: str, use_dnd_decorations: bool = False
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
    book.set_identifier("id123456")
    book.set_title(title)
    book.set_language("en")
    # Add the css files
    css_template = jinja_env.get_template("dungeonsheets_epub.css")
    dl_widths = {  # Width for dl lists, in 'em' units
        "character-details": 11,
        "combat-stats": 15,
        "proficiencies": 8.5,
        "faction": 6,
        "spellcasting": 12.5,
        "spell-slots": 8,
        "spell-details": 10,
        "beast-stats": 9,
        "feature-details": 5.5,
        "infusion-details": 8.5,
        "magic-item-details": 13.5,
        "monster-details": 15,
    }
    style = css_template.render(use_dnd_decorations=use_dnd_decorations, dl_widths=dl_widths)
    css = epub.EpubItem(
        uid="style_default",
        file_name="style/gm_sheet.css",
        media_type="text/css",
        content=style,
    )
    book.add_item(css)
    # Add paper background
    with open(Path(__file__).parent / "forms/paper-low-res.jpg", mode="rb") as fp:
        bg_img = fp.read()
    paper = epub.EpubItem(
        file_name="images/paper.jpg",
        media_type="image/jpeg",
        content=bg_img,
    )
    book.add_item(paper)
    # Create the separate chapters
    toc = ["nav"]
    html_chapters = []
    for chap_title, content in chapters.items():
        chap_fname = chap_title.replace(" - ", "-").replace(" ", "_").lower()
        chap_fname = "{}.html".format(chap_fname)
        chapter = epub.EpubHtml(
            title=chap_title,
            file_name=chap_fname,
            lang="en",
            media_type="application/xhtml+xml",
        )
        chapter.set_content(content)
        chapter.add_item(css)
        book.add_item(chapter)
        html_chapters.append(chapter)
        # Add entries for the table of contents
        toc.append(
            toc_from_headings(
                html=content, filename=chap_fname, chapter_title=chap_title
            )
        )
    # Add the table of contents
    book.toc = toc
    book.spine = ("nav", *html_chapters)
    # add default NCX and Nav file
    book.add_item(epub.EpubNcx())
    book.add_item(epub.EpubNav())
    # Save the file
    epub_fname = f"{basename}.epub"
    epub.write_epub(epub_fname, book)


class HeadingParser(HTMLParser):
    tag_re = re.compile("h(\d+)")
    _curr_level = None
    _curr_id = None
    _curr_title = None

    def __init__(self, *args, **kwargs):
        self.headings = []
        super().__init__(*args, **kwargs)

    def heading_level(self, tag):
        match = self.tag_re.match(tag)
        if match:
            return int(match.group(1))
        else:
            return None

    def handle_starttag(self, tag, attrs):
        this_level = self.heading_level(tag)
        if this_level is not None:
            # Found a heading, so process the properties
            self._curr_level = this_level
            attrs = {k: v for k, v in attrs}
            self._curr_id = attrs.get("id")

    def handle_endtag(self, tag):
        this_level = self.heading_level(tag)
        if this_level is not None and this_level == self._curr_level and self._curr_id is not None:
            heading = {
                "level": this_level,
                "id": self._curr_id,
                "title": self._curr_title,
            }
            self.headings.append(heading)
            # Reset the current values
            self._curr_level = None
            self._curr_id = None
            self._curr_title = None

    def handle_data(self, data):
        # Save the title
        if self._curr_level is not None:
            self._curr_title = data


def toc_from_headings(
    html: str, filename: str = "", chapter_title: str = "Sheet"
) -> list:
    """Accept a chapter of HTML, and extract a table of contents segment.

    Parameters
    ----------
    html
      The HTML block to be parsed.
    filename
      The name of this file to be used for hrefs. E.g.
      "index.html#heading_1".

    Returns
    -------
    toc
      A sequence of table-of-contents links.

    """
    # Parse the HTML
    parser = HeadingParser()
    parser.feed(html)
    headings = parser.headings
    # Parse into a table of contents
    if len(headings) == 0:
        # No headings found, so just the chapter link
        toc = epub.Link(href=filename, title=chapter_title, uid=filename)
    else:
        # Add a section for the chapter as a whole
        toc = (epub.Section(href=filename, title=chapter_title), [])
        sections_stack = [toc]
        # Parse all the headings
        for idx, heading in enumerate(headings):
            # Determine where we are in the tree
            href = f"{filename}#{heading['id']}"
            parent_section = sections_stack[-1]
            is_last = idx == (len(headings) - 1)
            is_leaf = is_last or heading["level"] >= headings[idx + 1]["level"]
            # Add a leaf or branch depending on the heading structure
            if is_leaf:
                parent_section[1].append(
                    epub.Link(href=href, title=heading["title"], uid=href.replace("#", ":"))
                )
            else:
                new_section = (epub.Section(href=href, title=heading["title"]), [])
                parent_section[1].append(new_section)
                sections_stack.append(new_section)
            # Walk back up the stack
            if not is_last:
                for idx in range(max(0, heading["level"] - headings[idx + 1]["level"])):
                    sections_stack.pop()

    return toc


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
    bad_characters = ["'", "(", ")", "&", "/", "+", ",", "=", ]
    for c in bad_characters:
        inpt = inpt.replace(c, "")
    return inpt.replace(" ", "-")



# Prepare the jinja environment
jinja_env = jinja_environment()
jinja_env.filters["rst_to_html"] = rst_to_html
jinja_env.filters["to_heading_id"] = to_heading_id
