import allure

from pages.BasePage import BasePage
from selenium.webdriver.common.by import By
import random

class RegistrtionPaageLocators():
    PHONE_FIELD = (By.XPATH, '//div[@data-l="t,phone"]')
    COUNTRY_LIST = (By.XPATH, '//div[@data-l="t,country"]')
    COUNTRY_ITEM = (By.XPATH, '//div[@class="country-select_code"]')
    SUBMIT_BUTTON = (By.XPATH,'//input[@data-l="t,submit"]')
    SUPPORT_BUTTON = (By.XPATH, '//*[@data-l="t,support"]')

class RegistrationPageHelper(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.check_page()

    def check_page(self):
        with allure.step('Проверка корректности загрузки страницы'):
            self.attach_screenshot()
        self.find_element(RegistrtionPaageLocators.PHONE_FIELD)
        self.find_element(RegistrtionPaageLocators.COUNTRY_LIST)
        self.find_element(RegistrtionPaageLocators.SUBMIT_BUTTON)
        self.find_element(RegistrtionPaageLocators.SUPPORT_BUTTON)

    def select_random_country(self):
        with allure.step('Выбор случайной страны'):
            random_number = random.randint(0,212)
            self.find_element(RegistrtionPaageLocators.COUNTRY_LIST).click()
            country_items = self.find_elements(RegistrtionPaageLocators.COUNTRY_ITEM)
            country_code = country_items[random_number].get_attribute('text')
            country_items[random_number].click()
            return country_code

    def get_phone_field_value(self):
        with allure.step('Получение значения поля телефона'):
            return self.find_element(RegistrtionPaageLocators.PHONE_FIELD).get_attribute('value')




