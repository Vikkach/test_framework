from common_lib.api.user.user_api import UserAPI
from common_lib.api.user.user_json_data_parsing import UserJsonDataParsing
from common_lib.api.user.user_data_generator import UserDataGenerator
from common_lib.api.user.user_data_checker import UserDataChecker


class TestBaseAPI:

    def setup_class(self):
        self.user_api = UserAPI()
        self.user_data_parser = UserJsonDataParsing()
        self.user_data_generator = UserDataGenerator()
        self.user_checker = UserDataChecker()
