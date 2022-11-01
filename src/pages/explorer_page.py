from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from configuration import BTC_ADDRESS
from src.baseclasses.base_page import BasePage


class Locators:
    INPUT = (By.CSS_SELECTOR, 'input[type="text"]')
    ADDRESS_ON_PAGE = (By.XPATH, r'//*[@id="__next"]/div[1]/div/div/div[1]/div/div[2]/div/div[2]/a')
    TEXT = (By.CLASS_NAME, 'search_overview__1Ef1E')


class ExplorerPage(BasePage):

    def fill_fields_and_submit(self):
        element = self.element_is_visible(Locators.INPUT)
        element.send_keys(BTC_ADDRESS)
        element.send_keys(Keys.ENTER)

    def find_element_name(self, locator):
        field = self.element_is_visible(locator)
        return field.text
