import urllib
import html.Parser as data

class HTML:

    def get_html(self, url):
        url = urllib.request.urlopen(url)
        return url.read()

    def get_links(self, html):
        parser = data.Parser()
        parser.feed(str(html))
        return parser.get_unique_url()
