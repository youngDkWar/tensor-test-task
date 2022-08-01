from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


class Page:

    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://yandex.ru/"

    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator), message="Not found")

    def press_enter(self, locator):
        self.find_element(locator).send_keys(Keys.ENTER)

    def open_main_page(self):
        return self.driver.get(self.base_url)

    def find_elements(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator), message="Not found")

    def is_element_exist(self, locator):
        element = self.find_elements(locator)
        return len(element) > 0
