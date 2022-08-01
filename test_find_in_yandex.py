import pytest
from YandexSearchPage import SearchForm, YandexSearchLocators


def test_check_yandex_search(browser):
    """Открывает главную страницу yandex и проверяет наличие поля поиска"""
    yandex_page = SearchForm(browser)
    yandex_page.open_main_page()
    assert yandex_page.is_element_exist(YandexSearchLocators.LOCATOR_YANDEX_SEARCH_FIELD)


def test_check_suggest_table(browser):
    """Проверяет, что при вводе слова 'тензор' появляется таблица с подсказками запроса"""
    yandex_page = SearchForm(browser)
    yandex_page.open_main_page()
    yandex_page.enter_word("тензор")
    assert yandex_page.is_element_exist(YandexSearchLocators.LOCATOR_YANDEX_SUGGEST_TABLE)


def test_check_results_table(browser):
    """Проверяет, что при вводе слова 'тензор' в поисковик и нажатии Enter, появляется
        страница с таблицей результатов поиска"""
    yandex_page = SearchForm(browser)
    yandex_page.open_main_page()
    yandex_page.enter_word("тензор")
    yandex_page.press_enter_to_find_results()
    assert yandex_page.is_element_exist(YandexSearchLocators.LOCATOR_YANDEX_RESULT_TABLE)


def test_check_first_element_in_results(browser):
    """Проверяет, что в таблице результатов поиска по слову 'тензор' первой записью
        является ссылка на официальный сайт Тензора"""
    yandex_page = SearchForm(browser)
    yandex_page.open_main_page()
    yandex_page.enter_word("тензор")
    yandex_page.press_enter_to_find_results()
    link = yandex_page.find_element(YandexSearchLocators.LOCATOR_YANDEX_FIRST_RESULT)
    assert link.get_attribute('href') == "https://tensor.ru/"
