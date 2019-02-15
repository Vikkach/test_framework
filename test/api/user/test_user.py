import pytest
from allure import step
from test.api.test_base_api import TestBaseUserAPI


class TestUser(TestBaseUserAPI):
    @pytest.mark.parametrize('page', range(1, 13))
    def test_get_user_list_by_page(self, page):
        with step('Send response to get user by page'):
            response = self.user_api.get_users_list(page)
        with step('Parse response to json and get page number'):
            json = self.user_api.parse_response_to_json(response)
            page_number = self.user_data_parser.get_page_number(json)
        with step('Check page number'):
            assert page_number == page