import unittest

from dungeonsheets import spells, features, latex


class MarkdownTestCase(unittest.TestCase):
    """Check that conversion of markdown formats to LaTeX code works
    correctly."""

    def test_rst_bold(self):
        text = latex.rst_to_latex("**hello**")
        self.assertEqual(text, "\n\\textbf{hello}\n")

    def test_hit_dice(self):
        text = latex.rst_to_latex("1d6+3")
        self.assertEqual(text.strip("\n"), "\\texttt{1d6+3}")

    def test_no_text(self):
        text = latex.rst_to_latex(None)
        self.assertEqual(text, "")

    def test_verbatim(self):
        text = latex.rst_to_latex("``hello, world``")
        self.assertIn(r"\texttt{hello, world}", text)

    def test_literal_backslash(self):
        text = latex.rst_to_latex(r"\\")
        self.assertEqual(r"\textbackslash{}", text.strip("\n"))

    @unittest.skip(
        "Headings are all screwed up because it treats them as the document title"
    )
    def test_headings(self):
        # Simple heading by itself
        text = latex.rst_to_latex("Hello, world\n------------\n\nGoodbye, world")
        self.assertEqual("\\section*{Hello, world}\n", text)
        # Simple heading with leading whitespace
        text = latex.rst_to_latex("    Hello, world\n    ============\n")
        self.assertEqual("\\section*{Hello, world}\n", text)
        # Heading with text after it
        text = latex.rst_to_latex("Hello, world\n============\n\nThis is some text")
        self.assertEqual("\\section*{Hello, world}\n\nThis is some text", text)
        # Heading with text before it
        text = latex.rst_to_latex("This is a paragraph\n\nHello, world\n============\n")
        self.assertEqual("This is a paragraph\n\n\\section*{Hello, world}\n", text)
        # Check that levels of headings are parsed appropriately
        text = latex.rst_to_latex("Hello, world\n^^^^^^^^^^^^\n")
        self.assertEqual("\\subsubsection*{Hello, world}\n", text)
        text = latex.rst_to_latex("Hello, world\n^^^^^^^^^^^^\n", top_heading_level=3)
        self.assertEqual("\\subparagraph*{Hello, world}\n", text)
        # This is a bad heading missing with all the underline on one line
        text = latex.rst_to_latex("Hello, world^^^^^^^^^^^^\n")
        self.assertEqual("Hello, world\\^\\^\\^\\^\\^\\^\\^\\^\\^\\^\\^\\^\n", text)

    def test_bullet_list(self):
        tex = latex.rst_to_latex("\n- Hello\n- World\n\n")
        expected_tex = "\\begin{itemize}\n\\item Hello\n\n\\item World\n\\end{itemize}"
        self.assertEqual(expected_tex, tex.strip("\n"))
        # Other bullet characters
        tex = latex.rst_to_latex("\n* Hello\n* World\n\n")
        self.assertEqual(expected_tex, tex.strip("\n"))
        tex = latex.rst_to_latex("\n+ Hello\n+ World\n\n")
        self.assertEqual(expected_tex, tex.strip("\n"))
        # A real list taken from a docstring
        real_list = """
        - Secondhand (you have heard of the target) - +5
        - Firsthand (you have met the target) - +0
        - Familiar (you know the target well) - -5
        
        """
        tex = latex.rst_to_latex(real_list)
        self.assertIn("\\begin{itemize}", tex)

    def test_multiline_bullet_list(self):
        md_list = """
        - Secondhand (you have heard
          of the target) - +5
        - Firsthand (you have met
          the target) - +0
        - Familiar (you know the target
          well) - -5
        
        """
        tex = latex.rst_to_latex(md_list)
        self.assertIn("\\begin{itemize}", tex)

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
        tex = latex.rst_to_latex(table_rst)
        # Check begin/end environment is fixed
        self.assertNotIn("longtable", tex)
        self.assertIn("supertabular", tex)
        # Check headers and footers are fixed
        self.assertNotIn("endfoot", tex)
        self.assertNotIn("endhead", tex)
        self.assertNotIn("endfirsthead", tex)
        # Check that fancy decorations uses the DndTable environment
        tex = latex.rst_to_latex(table_rst, use_dnd_decorations=True)
        self.assertIn(r"\begin{DndTable}{l l l }", tex)

    def test_rst_all_spells(self):
        for spell in spells.all_spells():
            tex = latex.rst_to_latex(spell.__doc__)
            self.assertNotIn(
                "DUadmonition", tex, f"spell {spell} is not valid reStructured text"
            )

    def test_rst_all_features(self):
        for feature in features.all_features():
            tex = latex.rst_to_latex(feature.__doc__)
            self.assertNotIn(
                "DUadmonition", tex, f"feature {feature} is not valid reStructured text"
            )
