from common_lib.api.base_api import BaseAPI
from common_lib.api.general_data import STATUS_CODE


class BaseDataChecker:
    @staticmethod
    def check_status_code(response, **kwargs):
        actual_status_code = BaseAPI.ger_response_status_code(response)
        expected_status_code = STATUS_CODE.get(kwargs.get('status'))
        assert actual_status_code == expected_status_code, f'Status code is {actual_status_code} instead of {expected_status_code}'
