from common_lib.api.user.user_api import UserAPI
from common_lib.api.user.user_json_data_parsing import UserJsonDataParsing


class TestBaseUserAPI:

    def setup_class(self):
        self.user_api = UserAPI()
        self.user_data_parser = UserJsonDataParsing()
