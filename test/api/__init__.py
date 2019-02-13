import os
from config.config_parser import ConfigParser


class BaseTest:
    env = os.environ['ENVIRONMENT']
    common_config_path = ConfigParser('common.ini').config
    dev_config_path = ConfigParser('dev_env.ini').config
    qa_config_path = ConfigParser('qa_env.ini').config
