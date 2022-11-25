from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from configuration import WEB_URL_SIBAC
from src.baseclasses.base_page import BasePage


ARTICLES = (By.XPATH, '//*[@id="archive-wrapp"]/div/p/a')
TITLE_ARTICLE = (By.XPATH, '//*[@id="block-system-main"]/div/div/h1')


def test_web_page_title(driver):
    """Check each link text with the article title in a new tab"""
    browser = BasePage(driver, WEB_URL_SIBAC)
    browser.open()
    original_window = driver.current_window_handle
    list_of_links = browser.elements_is_visible(ARTICLES)
    for i, link in enumerate(list_of_links):
        driver.switch_to.window(original_window)
        text_first_page = list_of_links[i].text
        link.send_keys(Keys.CONTROL + Keys.SHIFT + Keys.RETURN)
        driver.switch_to.window(driver.window_handles[1])
        text_second_page = browser.element_is_visible(TITLE_ARTICLE).text
        assert text_first_page.lower() == text_second_page.lower()
        driver.close()
