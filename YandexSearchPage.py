from Page import Page
from selenium.webdriver.common.by import By


class YandexSearchLocators:
    """Класс хранит некоторые локаторы к элементам на главной странице Яндекс"""
    LOCATOR_YANDEX_SEARCH_FIELD = (By.ID, "text")
    LOCATOR_YANDEX_SEARCH_BUTTON = (By.CLASS_NAME, "search2__button")
    LOCATOR_YANDEX_RESULT_TABLE = (By.CLASS_NAME, "content__left")
    LOCATOR_YANDEX_SUGGEST_TABLE = (By.CSS_SELECTOR, ".mini-suggest__overlay_visible")
    LOCATOR_YANDEX_FIRST_RESULT = (By.XPATH, '//*[@id="search-result"]/li[1]/div/div[1]/div[1]/a')
    LOCATOR_YANDEX_IMAGES_LINK = (By.XPATH, '/html/body/div[1]/div[2]/div[2]/div/div[1]/nav/div/ul/li[5]/a')


class SearchForm(Page):
    """Класс наследует Page и представляет главную страницу Яндекса"""
    def __init__(self, driver):
        super().__init__(driver)
        self.base_url = "https://yandex.ru/"

    def enter_word(self, word):
        """Метод принимает строку и вводит её в поле поиска на главной странице"""
        search_field = self.find_element(YandexSearchLocators.LOCATOR_YANDEX_SEARCH_FIELD)
        search_field.click()
        search_field.send_keys(word)
        return search_field

    def click_on_the_search_button(self):
        """Метод кликает на кнопку 'найти' на главной странице яндекса"""
        return self.find_element(YandexSearchLocators.LOCATOR_YANDEX_SEARCH_BUTTON).click()

    def press_enter_to_find_results(self):
        """Метод нажимает кнопку Enter для поискового поля. После этого открывается страница с результатами поиска"""
        return self.press_enter(YandexSearchLocators.LOCATOR_YANDEX_SEARCH_FIELD)

    def open_main_page(self):
        """Метод открывает главную страницу яндекса"""
        return self.driver.get(self.base_url)

    def switch_tab(self, tab_num):
        """Метод переключает драйвер на вкладку с номером tub_num"""
        return self.driver.switch_to_window(self.driver.window_handles[tab_num])

