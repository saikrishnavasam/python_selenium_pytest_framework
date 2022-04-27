import json

from requests import Response


class Asserts:
    """ These asserts are used in API tests """
    @staticmethod
    def assert_equals(val1, val2, error_message: str = ""):
        assert val1 == val2, f"Failed assert. {error_message}"

    @staticmethod
    def assert_code_status(response: Response, expected_code: int, error_message: str = ""):
        assert response.status_code == expected_code, f'Expected status code {expected_code}, not matching with actual {response.status_code}. {error_message}'

    @staticmethod
    def assert_response_text(response: Response, expected_text: str, error_message: str = ""):
        assert response.text == expected_text, f'Expected status code {expected_text}, not matching with actual {response.text}. {error_message}'

    @staticmethod
    def assert_json_value_by_key(response: Response, key: str, val: str):
        try:
            response_dict = response.json()
        except json.decoder.JSONDecodeError:
            assert False, f'Response not in JSON format. "{response.text}"'

        assert key in response_dict, f'Response json does not have key "{key}"'
        assert response_dict[key] == val, f'Response "{key}" has value {response_dict[key]} but expected is {val}'

    @staticmethod
    def assert_json_has_no_key(response: Response, key:str):
        try:
            response_dict = response.json()
        except json.decoder.JSONDecodeError:
            assert False, f'Response not in JSON format. "{response.text}"'

        assert key not in response_dict, f'Response json does not have key "{key}"'
