from configuration import WEB_URL, BTC_ADDRESS, SUCCESS_TEXT
from src.pages.explorer_page import ExplorerPage, Locators


def test_web_getting_wallet_data(driver):
    explorer_page = ExplorerPage(driver, WEB_URL)
    explorer_page.open()
    explorer_page.search_btc_address()
    assert BTC_ADDRESS == explorer_page.find_element_name(Locators.ADDRESS_ON_PAGE)
    assert SUCCESS_TEXT == explorer_page.find_element_name(Locators.TEXT)
