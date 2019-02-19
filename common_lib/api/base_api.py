import os
import json
import requests
from config.config_parser import ConfigParser
from common_lib.base_logger import BaseLogger


class BaseAPI(BaseLogger):
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
        BaseLogger.get_info_log('Sending GET url: {}.'.format(url))
        response = requests.get(url)
        return response

    def post(self, url, body):
        BaseLogger.get_info_log('Sending POST url: {} body: {}.'.format(url, body))
        response = requests.post(url, data=body)
        parsed_response = self.parse_response_to_json(response)
        BaseLogger.get_info_log('Received "{}".'.format(response))
        BaseLogger.get_info_log('Response body "{}".'.format(parsed_response))
        return response

    @staticmethod
    def parse_response_to_json(response):
        return response.json()


