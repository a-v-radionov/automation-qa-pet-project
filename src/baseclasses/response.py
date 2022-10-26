from jsonschema import validate
from src.enums.global_enums import GlobalErrorMessages


class Response:

    def __init__(self, response):
        self.response = response
        self.response_json = response.json().get('data')
        self.response_status = response.status_code

    def assert_status_code(self, status_code):
        assert self.response_status == status_code, self
        return self

    def validate(self, schema):
        schema.parse_obj(self.response_json)

# create a magic method/ модифицирует наш ответ при ошибке
    def __str__(self):
        return \
            f'\nStatus code: {self.response_status} \n' \
            f'Request url: {self.response.url} \n' \
            f'Reason: {self.response.reason} \n' \
            f'Response body: {self.response_json}'

