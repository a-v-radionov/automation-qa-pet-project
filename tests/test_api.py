from http import HTTPStatus
from src.schemas.address_info import Address
from src.baseclasses.response import Response
from configuration import BTC_ADDRESS, METHOD_ADDRESS_INFO, BTC_WRONG_ADDRESS, API_URL


def test_getting_wallet_data(get_data, api=API_URL, name=f'{METHOD_ADDRESS_INFO}/{BTC_ADDRESS}'):
    """
    Positive test.
    Valid BTC_ADDRESS. Check the status code. Validate the response using json schema.

    Позитивный кейс.
    Передаём в фикстуру корректный адрес, проверяем статус код, валидируем ответ на соответствие схемы
    """
    Response(get_data(api, name)).assert_status_code(HTTPStatus.OK.value).validate(Address)


# @pytest.mark.skip
def test_getting_wallet_data_negative(get_data, api=API_URL, name=f'{METHOD_ADDRESS_INFO}/{BTC_WRONG_ADDRESS}'):
    """
    Negative test.
    Invalid BTC_WRONG_ADDRESS. Check the status code
    """
    Response(get_data(api, name)).assert_status_code(HTTPStatus.BAD_REQUEST.value)
