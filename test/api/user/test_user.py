import pytest
from allure import step, feature, title
from test.api.user import TestBaseUserAPI


@feature('User API')
class TestUser(TestBaseUserAPI):
    @pytest.mark.parametrize('page', [1])
    @title('Test GET list of users by page')
    def test_get_user_list_by_page(self, page, create_test_user):
        with step('Send request to get user by page'):
            response = self.user_api.get_users_list(page)
        with step('Get page number and check it'):
            page_number = self.user_data_parser.get_page_number(response)
            assert page_number == page
        with step('Get user list and check that it is not empty'):
            users_list = self.user_data_parser.get_user_list(response)
            assert len(users_list) >= 1

    @title('Test POST user')
    def test_create_user(self):
        with step('Generate test user'):
            user_data = self.user_data_generator.generate_user()
        with step('Send request to create user'):
            response = self.user_api.create_user(user_data)
        with step('Check response that user was created'):
            self.user_checker.check_created_user(user_data, response)


