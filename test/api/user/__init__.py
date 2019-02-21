import pytest
from allure import step, title
from test.api.test_base_api import TestBaseAPI


class TestBaseUserAPI(TestBaseAPI):

    @pytest.fixture()
    @title('Create test user')
    def create_test_user(self):
        with step('Generate test user'):
            user_data = self.user_data_generator.generate_user()
        with step('Create user'):
            response = self.user_api.create_user(user_data)
            self.user_checker.check_status_code(response, status='created')


