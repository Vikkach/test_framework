import configparser


class ConfigParser:
    def __init__(self, path):
        self.config = configparser.ConfigParser()
        self.config_path = path
        self.config.read(path)



