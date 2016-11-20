import configparser
import os

class ConfigParser():

    def read_config(self, root_dir):
        config = configparser.ConfigParser()
        config.read(os.path.join( root_dir, 'conf', 'spiderpy.properties'))

        return config