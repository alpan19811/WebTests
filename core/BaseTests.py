import pytest
from selenium import webdriver

@pytest.fixture(scope='session')
def browser():
    driver = webdriver.Chrome()
    yield driver #в т.ч. для возможности добавления паузы
    driver.quit()