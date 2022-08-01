from Page import Page
from selenium.webdriver.common.by import By


class YandexImagesLocators:
    """Класс хранит основные локаторы для страницы с картинками в Яндекс"""
    LOCATOR_YANDEX_FIRST_IMAGE = (By.CLASS_NAME, 'serp-item_pos_0')
    LOCATOR_YANDEX_FIRST_IMAGE_MODAL_WINDOW = (By.CLASS_NAME, 'MMImage-Origin')
    LOCATOR_YANDEX_FIRST_IMAGE_CATEGORY = (By.CLASS_NAME, 'PopularRequestList-Item_pos_0')
    LOCATOR_YANDEX_FIRST_IMAGE_CATEGORY_NAME = (By.XPATH, '//*[@class="PopularRequestList-Item PopularRequestList-Item_pos_0"]/a/div[2]')
    LOCATOR_YANDEX_SEARCH_FIELD = (By.CLASS_NAME, 'mini-suggest__input')
    LOCATOR_YANDEX_MODAL_IMAGE_BTN_NEXT = (By.CLASS_NAME, 'CircleButton_type_next')
    LOCATOR_YANDEX_MODAL_IMAGE_BTN_PREV = (By.CLASS_NAME, 'CircleButton_type_prev')


class ImagesPage(Page):
    """Класс наследует Page и представляет страницу 'картинки' в Яндекс"""
    def __init__(self, driver):
        super().__init__(driver)
        self.base_url = "https://yandex.ru/images/"

    def open_page(self):
        """Метод открывает страницу 'картинки' в яндекс"""
        return self.driver.get(self.base_url)

    def get_current_image_src(self):
        """Метод возвращает в виде строки ссылку на текущее открытое изображение в модальном окне на странице
            с картинками"""
        image = self.find_element(YandexImagesLocators.LOCATOR_YANDEX_FIRST_IMAGE_MODAL_WINDOW)
        return image.get_attribute("src")
