import pytest
from selenium import webdriver


@pytest.fixture(scope="session")
def browser():
    driver = webdriver.Chrome(executable_path="C:/Users/Nikita/PycharmProjects/drivers/chromedriver.exe")
    yield driver
    driver.quit()
