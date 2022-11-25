from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as Wait


class BasePage:
    def __init__(self, driver, url):
        """Init Class methods.

        Parameters
        ----------
        driver
            Web driver.
        url
            A URL website's.

        """
        self.driver = driver
        self.url = url

    def open(self):
        self.driver.get(self.url)

    def element_is_visible(self, locator, timeout=5):
        """Используем явное(до определенного условия) ожидание для поиска эл-та на странице.
            Driver wait(timeout) until element is not found
        Parameters
        ----------
        locator
            Locator of element.
        timeout
            The second parameter.

        Returns
        -------
        String
            a value of element located if successful, error message otherwise.

        """
        return Wait(self.driver, timeout).until(EC.visibility_of_element_located(locator),
                                                message=f'Cant find element by locator {locator}')

    def elements_is_visible(self, locator, timeout=5):
        return Wait(self.driver, timeout).until(EC.visibility_of_all_elements_located(locator),
                                                message=f"Can't find elements by locator {locator}")
