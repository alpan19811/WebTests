import allure

from pages.BasePage import BasePage
from selenium.webdriver.common.by import By

class RegistrationPageLocators():
    PHONE_FIELD = (By.XPATH, '//div[@data-l="t,phone"]')
    COUNTRY_ITEM = (By.XPATH, '//div[@data-l="t,country"]')
    COUNTRY_ITEM = (By.XPATH, '//*[class="country-select_i __active"]')
