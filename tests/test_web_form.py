from configuration import WEB_URL, BTC_ADDRESS, SUCCESS_TEXT
from src.pages.explorer_page import ExplorerPage, Locators


def test_web_getting_wallet_data(browser):
    explorer_page = ExplorerPage(browser, WEB_URL)
    explorer_page.open()
    explorer_page.fill_fields_and_submit()
    assert BTC_ADDRESS == explorer_page.find_element_name(Locators.ADDRESS_ON_PAGE)
    assert SUCCESS_TEXT == explorer_page.find_element_name(Locators.TEXT)
