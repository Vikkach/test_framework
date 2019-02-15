import os
import json
import requests
from config.config_parser import ConfigParser


class BaseAPI:
    env_name = os.environ['ENVIRONMENT']

    def __init__(self):
        self.env_name = os.environ['ENVIRONMENT']
        self.env_config = ConfigParser(f'config/{self.env_name}_env.ini').config
        self.common_config = ConfigParser('config/common.ini').config
        self.root_url = self.common_config.get('main_url', 'main_url')
        self.user_email = self.env_config.get('user_config', 'user_email')
        self.user_password = self.env_config.get('user_config', 'user_password')

    @staticmethod
    def get(url):
        response = requests.get(url)
        return response

    @staticmethod
    def parse_response_to_json(response):
        return response.json()


