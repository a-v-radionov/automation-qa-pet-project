from enum import Enum


class GlobalErrorMessages(Enum):
    WRONG_STATUS_CODE = 'Received status code is not equal to expected.'
    WRONG_ADDRESS = 'Address on the page is not equal to expected.'
