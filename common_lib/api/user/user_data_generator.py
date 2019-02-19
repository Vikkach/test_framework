import random
from allure import attach, attachment_type
from common_lib.api.base_data_generator import BaseDataGenerator


class UserDataGenerator:
    @staticmethod
    def generate_user_name():
        return f'Automation test user name {BaseDataGenerator.generate_random_string(8)}'

    @staticmethod
    def generate_job():
        return f'Automation test job {BaseDataGenerator.generate_random_string(8)}'

    def generate_user(self):
        test_user = {'name': self.generate_user_name(),
                     'job': self.generate_job()}
        attach(str(test_user), 'test_user', attachment_type=attachment_type.JSON)
        return test_user
