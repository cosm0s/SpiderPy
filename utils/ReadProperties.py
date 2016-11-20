import configparser
import os


class ConfigParser:

    @staticmethod
    def read_config(root_dir):
        config = configparser.ConfigParser()
        config.read(os.path.join(root_dir, 'conf', 'spiderpy.properties'))

        return config
