from unittest import TestCase

from ebooklib import epub


from dungeonsheets.epub import toc_from_headings


class TOCTestCase(TestCase):
    def test_toc_from_no_headings(self):
        html = '<p>Hello, world</p>'
        toc = toc_from_headings(html)
        self.assertIsInstance(toc, epub.Link)
    
    def test_toc_from_single_heading(self):
        html = '<h1 id="hello_world">Hello, world</h1>'
        toc = toc_from_headings(html)
        self.assertIsInstance(toc, tuple)
        self.assertIsInstance(toc[0], epub.Section)
        self.assertIsInstance(toc[1], list)

    def test_toc_from_heading_tree(self):
        html = ('<h1 id="other_world">Other, world</h1>'
                '<h2 id="other_country">Other, country</h2>'
                '<h1 id="hello_world">Hello, world</h1>'
                '<h2 id="hello_country">Hello, country</h2>'
                '<h2 id="goodbye_country">Goodbye, country</h2>'
                '<h3 id="hello_city">Hello, city</h3>'
                '<h1 id="whatever">Whatever</h1>'
                )
        toc = toc_from_headings(html)
        heading_toc = toc[1]
        self.assertIsInstance(heading_toc, list)
        self.assertIsInstance(heading_toc[0][0], epub.Section)
        self.assertEqual(heading_toc[0][0].title, "Other, world")
        self.assertIsInstance(heading_toc[2], epub.Link)
        self.assertEqual(heading_toc[2].title, "Whatever")
        self.assertIsInstance(heading_toc[2], epub.Link)
        self.assertIsInstance(heading_toc[1][1][0], epub.Link)
        self.assertEqual(heading_toc[1][1][0].title, "Hello, country")
