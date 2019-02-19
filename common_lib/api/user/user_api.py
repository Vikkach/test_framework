from common_lib.api.base_api import BaseAPI
from common_lib.base_logger import BaseLogger


class UserAPI(BaseAPI):
    def __init__(self):
        BaseAPI.__init__(self)
        self.users_path = self.common_config.get('api', 'user')

    def get_users_list(self, page):
        BaseLogger.get_info_log(f'Get user from page {page}')
        url = f'{self.root_url}{self.users_path}?page={page}'
        response = self.get(url)
        response_json = self.parse_response_to_json(response)
        return response_json

    def create_user(self, user_data):
        BaseLogger.get_info_log('Creating user...')
        url = f'{self.root_url}{self.users_path}'
        response = self.post(url, user_data)
        response_json = self.parse_response_to_json(response)
        return response_json



