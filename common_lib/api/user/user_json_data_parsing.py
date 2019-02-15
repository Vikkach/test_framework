from common_lib.api.base_api import BaseAPI


class UserJsonDataParsing(BaseAPI):
    @staticmethod
    def get_page_number(json):
        return json.get('page')
