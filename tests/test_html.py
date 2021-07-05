import unittest

from dungeonsheets import spells, features, epub


class MarkdownTestCase(unittest.TestCase):
    """Check that conversion of markdown formats to LaTeX code works
    correctly."""

    def test_rst_bold(self):
        text = epub.rst_to_html("**hello**")
        self.assertEqual(text, "<p><strong>hello</strong></p>\n")

    def test_hit_dice(self):
        text = epub.rst_to_html("1d6+3")
        self.assertEqual(text.strip("\n"), '<p><span class="docutils literal">1d6+3</span></p>')

    def test_no_text(self):
        text = epub.rst_to_html(None)
        self.assertEqual(text, "")

    def test_verbatim(self):
        text = epub.rst_to_html("``hello, world``")
        self.assertIn('<p><span class="docutils literal">hello, world</span></p>', text)

    def test_literal_backslash(self):
        text = epub.rst_to_html(r"\\")
        self.assertEqual(r"<p>\</p>", text.strip("\n"))

    @unittest.skip(
        "Headings are all screwed up because it treats them as the document title"
    )
    def test_headings(self):
        # Simple heading by itself
        text = epub.rst_to_html("Hello, world\n------------\n\nGoodbye, world")
        self.assertEqual("\\section*{Hello, world}\n", text)
        # Simple heading with leading whitespace
        text = epub.rst_to_html("    Hello, world\n    ============\n")
        self.assertEqual("\\section*{Hello, world}\n", text)
        # Heading with text after it
        text = epub.rst_to_html("Hello, world\n============\n\nThis is some text")
        self.assertEqual("\\section*{Hello, world}\n\nThis is some text", text)
        # Heading with text before it
        text = epub.rst_to_html("This is a paragraph\n\nHello, world\n============\n")
        self.assertEqual("This is a paragraph\n\n\\section*{Hello, world}\n", text)
        # Check that levels of headings are parsed appropriately
        text = epub.rst_to_html("Hello, world\n^^^^^^^^^^^^\n")
        self.assertEqual("\\subsubsection*{Hello, world}\n", text)
        text = epub.rst_to_html("Hello, world\n^^^^^^^^^^^^\n", top_heading_level=3)
        self.assertEqual("\\subparagraph*{Hello, world}\n", text)
        # This is a bad heading missing with all the underline on one line
        text = epub.rst_to_html("Hello, world^^^^^^^^^^^^\n")
        self.assertEqual("Hello, world\\^\\^\\^\\^\\^\\^\\^\\^\\^\\^\\^\\^\n", text)

    def test_bullet_list(self):
        tex = epub.rst_to_html("\n- Hello\n- World\n\n")
        expected_tex = '<ul class="simple">\n<li><p>Hello</p></li>\n<li><p>World</p></li>\n</ul>'
        self.assertEqual(expected_tex, tex.strip("\n"))
        # Other bullet characters
        tex = epub.rst_to_html("\n* Hello\n* World\n\n")
        self.assertEqual(expected_tex, tex.strip("\n"))
        tex = epub.rst_to_html("\n+ Hello\n+ World\n\n")
        self.assertEqual(expected_tex, tex.strip("\n"))
        # A real list taken from a docstring
        real_list = """
        - Secondhand (you have heard of the target) - +5
        - Firsthand (you have met the target) - +0
        - Familiar (you know the target well) - -5
        
        """
        tex = epub.rst_to_html(real_list)
        self.assertIn('<ul class="simple">', tex)

    def test_multiline_bullet_list(self):
        md_list = """
        - Secondhand (you have heard
          of the target) - +5
        - Firsthand (you have met
          the target) - +0
        - Familiar (you know the target
          well) - -5
        
        """
        tex = epub.rst_to_html(md_list)
        self.assertIn('<ul class="simple">', tex)

    def test_simple_table(self):
        table_rst = """
            =====  =====  =======
            A      B      A and B
            =====  =====  =======
            False  False  False
            True   False  False
            False  True   False
            True   True   True
            =====  =====  =======
        """
        tex = epub.rst_to_html(table_rst)
        # Check begin/end environment is fixed
        self.assertIn("<table>", tex)

    def test_rst_all_spells(self):
        for spell in spells.all_spells():
            tex = epub.rst_to_html(spell.__doc__)
            self.assertNotIn(
                "DUadmonition", tex, f"spell {spell} is not valid reStructured text"
            )

    def test_rst_all_features(self):
        for feature in features.all_features():
            tex = epub.rst_to_html(feature.__doc__)
            self.assertNotIn(
                "DUadmonition", tex, f"feature {feature} is not valid reStructured text"
            )
