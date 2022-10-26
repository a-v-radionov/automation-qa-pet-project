import pytest

from requests import get
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


# локальная функция для отправки запроса
def _get_data(api, name):
    response = get(api + name)
    return response


@pytest.fixture
def get_data():
    return _get_data

# scope="session"
@pytest.fixture
def browser():
    driver_service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=driver_service)
    driver.maximize_window()
    yield driver
    driver.quit()

