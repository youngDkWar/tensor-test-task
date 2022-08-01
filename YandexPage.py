from Page import Page
from selenium.webdriver.common.by import By


class YandexLocators:
    LOCATOR_YANDEX_SEARCH_FIELD = (By.ID, "text")
    LOCATOR_YANDEX_SEARCH_BUTTON = (By.CLASS_NAME, "search2__button")
    LOCATOR_YANDEX_RESULT_TABLE = (By.CLASS_NAME, "content__left")
    LOCATOR_YANDEX_SUGGEST_TABLE = (By.CSS_SELECTOR, ".mini-suggest__overlay_visible")
    LOCATOR_YANDEX_FIRST_RESULT = (By.XPATH, '//*[@id="search-result"]/li[1]/div/div[1]/div[1]/a')


class SearchForm(Page):

    def enter_word(self, word):
        search_field = self.find_element(YandexLocators.LOCATOR_YANDEX_SEARCH_FIELD)
        search_field.click()
        search_field.send_keys(word)
        return search_field

    def click_on_the_search_button(self):
        return self.find_element(YandexLocators.LOCATOR_YANDEX_SEARCH_BUTTON).click()

    def press_enter_to_find_results(self):
        return self.press_enter(YandexLocators.LOCATOR_YANDEX_SEARCH_FIELD)
