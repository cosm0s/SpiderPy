import configparser
import os

class ConfigParser():

    def read_config(self):
        config = configparser.ConfigParser()
        config.read(os.path.join('conf', 'spider.properties'))

        return config