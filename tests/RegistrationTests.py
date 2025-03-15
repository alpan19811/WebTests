import allure

from core.BaseTest import browser
from pages.BasePage import BasePage
from pages.LoginPage import LoginPageHelper, LoginPageLocators
from pages.RegistrationPage import RegistrationPageHelper

BASE_URL = 'https://ok.ru/'

@allure.suite('Регистрация пользователя')
@allure.title('Проверка выбора случайной страны и кода страны')
def test_registration_random_country(browser):
    with allure.step('Открыть главную страницу'):
        BasePage(browser).get_url(BASE_URL)

    with allure.step("Перейти на страницу регистрации"):
        LoginPage = LoginPageHelper(browser)
        LoginPage.click_registration()

    with allure.step('Проверить корректность загрузки страницы регистрации'):
        RegistrationPage = RegistrationPageHelper(browser)

    with allure.step('Выбрать случайную страну и получить её код'):
        Selected_country_code = RegistrationPage.select_random_country()

    with allure.step('Получить код страны из поля ввода телефона'):
        Actual_country_code = RegistrationPage.get_phone_field_value()

    with allure.step('Проверка кода страны'):
        assert Selected_country_code == Actual_country_code