from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


class Page:
    """Класс Page реализует общие функции, которые должны присутствовать на любой HTML странице"""
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator, time=10):
        """Находит по заданному локатору элемент на странице и возвращает его. Если элемента нет, возвращается
            ошибка с текстом message"""
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator), message="Not found")

    def press_enter(self, locator):
        """Нажимает кнопку Enter на элементе, путь к которому необходимо передать в аргументе locator"""
        self.find_element(locator).send_keys(Keys.ENTER)

    def find_elements(self, locator, time=10):
        """Находит по заданному локатору все элементы на странице и возвращает их список. Если элементов нет,
            возвращается ошибка с текстом message"""
        return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator), message="Not found")

    def is_element_exist(self, locator):
        """Проверяет, существует ли элемент на странице. В функцию необходимо передать путь к элементу.
            Возвращает bool"""
        element = self.find_elements(locator)
        return len(element) > 0
