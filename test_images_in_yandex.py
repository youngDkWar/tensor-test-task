from YandexSearchPage import SearchForm, YandexSearchLocators
from YandexImagesPage import ImagesPage, YandexImagesLocators
import pytest


def test_yandex_images_link(browser):
    """Проверяет, что на главной странице яндекса есть ссылка на картинки"""
    yandex_page = SearchForm(browser)
    yandex_page.open_main_page()
    assert yandex_page.is_element_exist(YandexSearchLocators.LOCATOR_YANDEX_IMAGES_LINK)


@pytest.mark.xfail
def test_yandex_images_link_click(browser):
    """Проверяет, что по клику на 'картинки' открывается страница images. Тест ожидаемо проваливается, так
        как яндекс открывает раздел картинок с параметром 'utm_source', и поэтому url не чистый 'yandex.ru/images/'."""
    yandex_page = SearchForm(browser)
    yandex_page.open_main_page()
    page_images_link = yandex_page.find_element(YandexSearchLocators.LOCATOR_YANDEX_IMAGES_LINK)
    page_images_link.click()
    yandex_page.switch_tab(1)
    assert yandex_page.driver.current_url == "https://yandex.ru/images/"


def test_category_name_in_search_field_after_click(browser):
    """Проверяет, что после клика по первой категории изображений, название категории вставляется
        в поле поиска"""
    yandex_page = ImagesPage(browser)
    yandex_page.open_page()
    first_image_category = yandex_page.find_element(YandexImagesLocators.LOCATOR_YANDEX_FIRST_IMAGE_CATEGORY)
    first_image_category_name = yandex_page.find_element(YandexImagesLocators.LOCATOR_YANDEX_FIRST_IMAGE_CATEGORY_NAME).text
    first_image_category.click()
    search_field_suggest_text = yandex_page.find_element(YandexImagesLocators.LOCATOR_YANDEX_SEARCH_FIELD).get_attribute("value")
    assert first_image_category_name == search_field_suggest_text


def test_open_first_image(browser):
    """Проверяет, что после клика по первой картинке, она открывается в модальном окне"""
    yandex_page = ImagesPage(browser)
    yandex_page.open_page()
    first_image_category = yandex_page.find_element(YandexImagesLocators.LOCATOR_YANDEX_FIRST_IMAGE_CATEGORY)
    first_image_category.click()
    first_image = yandex_page.find_element(YandexImagesLocators.LOCATOR_YANDEX_FIRST_IMAGE)
    first_image.click()
    assert yandex_page.is_element_exist(YandexImagesLocators.LOCATOR_YANDEX_FIRST_IMAGE_MODAL_WINDOW)


def test_open_first_image_and_swap(browser):
    """Проверяет, что после клика на кнопку 'следующая картинка' в модальном окне, происходит смена изображения на
        следующее. Проверка осуществляется при помощи поля src у изображения, так как оно уникального для всех
         изображений в яндекс"""
    yandex_page = ImagesPage(browser)
    yandex_page.open_page()
    yandex_page.find_element(YandexImagesLocators.LOCATOR_YANDEX_FIRST_IMAGE_CATEGORY).click()
    yandex_page.find_element(YandexImagesLocators.LOCATOR_YANDEX_FIRST_IMAGE).click()
    modal_image_src_origin = yandex_page.get_current_image_src()
    yandex_page.find_element(YandexImagesLocators.LOCATOR_YANDEX_MODAL_IMAGE_BTN_NEXT).click()
    modal_image_src_next = yandex_page.get_current_image_src()
    assert modal_image_src_origin != modal_image_src_next


def test_original_image_dont_changes(browser):
    """Проверяет, что после клика на кнопку 'следующая картинка' в модальном окне, происходит смена изображения на
        следующее, а после нажатия кнопки 'предыдущая картинка', изображение становится исходным. Проверка
        осуществляется при помощи поля src у изображения, так как оно уникального для всех изображений в яндекс"""
    yandex_page = ImagesPage(browser)
    yandex_page.open_page()
    yandex_page.find_element(YandexImagesLocators.LOCATOR_YANDEX_FIRST_IMAGE_CATEGORY).click()
    yandex_page.find_element(YandexImagesLocators.LOCATOR_YANDEX_FIRST_IMAGE).click()
    modal_image_src_origin = yandex_page.get_current_image_src()
    yandex_page.find_element(YandexImagesLocators.LOCATOR_YANDEX_MODAL_IMAGE_BTN_NEXT).click()
    yandex_page.find_element(YandexImagesLocators.LOCATOR_YANDEX_MODAL_IMAGE_BTN_PREV).click()
    modal_image_src_prev = yandex_page.get_current_image_src()
    assert modal_image_src_origin == modal_image_src_prev
