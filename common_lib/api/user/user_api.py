from common_lib.api.base_api import BaseAPI


class UserAPI(BaseAPI):
    def __init__(self):
        BaseAPI.__init__(self)
        self.users_path = self.common_config.get('api', 'user')

    def get_users_list(self, page=2):
        url = f'{self.root_url}{self.users_path}?page={page}'
        response = self.get(url)
        return response



