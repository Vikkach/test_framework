import os
import configparser


class ConfigParser:
    def __init__(self, path):
        self.config_path = os.path.expanduser(f'{os.getcwd()}{path}')
        self.config = configparser.ConfigParser()
        self.config.sections()
        self.config.read(path)



