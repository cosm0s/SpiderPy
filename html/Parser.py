from html.parser import HTMLParser
import re

class Parser(HTMLParser):

    def __init__(self, links=None):
        HTMLParser.__init__(self)
        if links is None:
            self.links = []
        else:
            self.output_list = links

    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            self.links.append(dict(attrs).get('href'))
        for key, value in dict(attrs).items():
            if key != 'href' and not value is None:
                self.get_data_links(value)


    def handle_data(self, data):
        self.get_data_links(data)

    def get_data_links(self, value):
        if re.match('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', value) is not None:
            self.links = self.links + re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', value)


    def get_unique_url(self):
        return set(self.links)