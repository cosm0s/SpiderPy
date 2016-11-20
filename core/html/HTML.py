import urllib.request as request

import core.html.Parser as Data


class HTML:

    @staticmethod
    def get_html(url):
        url = request.urlopen(url)
        return url.read()

    @staticmethod
    def get_links(html):
        parser = Data.Parser()
        parser.feed(str(html))
        return parser.get_unique_url()
