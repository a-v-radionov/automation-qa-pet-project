import pytest

from requests import get
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


# the protected function for sending the request
def __get_data(api, name):
    response = get(api + name)
    return response


@pytest.fixture
def get_data():
    return __get_data


# scope="session"
@pytest.fixture(scope='function')
def driver():
    """
    - Download Chrome web driver.
    - Open browser
    - Close browser

    """
    driver_service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=driver_service)
    driver.maximize_window()
    yield driver
    driver.quit()
