import unittest

import core.html.HTML


class TestHtml(unittest.TestCase):

    def setUp(self):
        self.url = 'http://www.google.es'

    def test_get_html(self):
        parser = core.html.HTML.HTML()
        self.assertIsNotNone(parser.get_html(self.url))

    def test_get_links(self):
        parser = core.html.HTML.HTML()
        html = parser.get_html(self.url)
        links = parser.get_links(html)
        self.assertIsNotNone(links)
        self.assertGreater(len(links), 5)

if __name__ == '__main__':
    unittest.main()
