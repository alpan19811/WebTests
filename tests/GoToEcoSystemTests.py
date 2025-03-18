import allure

from core.BaseTest import browser
from pages.BasePage import BasePageHelper
from pages.LoginPage import LoginPageHelper
from pages.VKEcosystemPage import VKEcosystemPageHelper

BASE_URL = 'https://ok.ru/'

@allure.suite('Проверка тулбара')
@allure.title('Переход к проектам экосистемы VK')
def test_open_vk_ecosystem(browser):
    BasePage = BasePageHelper(browser)
    BasePage.get_url(BASE_URL)
    BasePage.check_page()
    LoginPage = LoginPageHelper(browser)
    current_window_id = LoginPage.get_windows_id(0)

    with allure.step('Нажимаем кнопку экосистемы VK'):
        LoginPage.click_vk_ecosystem()
        LoginPage.attach_screenshot()


    with allure.step('Нажимаем кнопку "ещё"'):
        LoginPage.click_more_button()
        LoginPage.attach_screenshot()

    new_window_id = LoginPage.get_windows_id(1)

    with allure.step('Переключаемся на новое окно'):
        LoginPage.switch_window(new_window_id)
        LoginPage.attach_screenshot()

    VKEcosystemPage = VKEcosystemPageHelper(browser)

    with allure.step('Возвращаемся в исходное окно'):
        VKEcosystemPage.switch_window(current_window_id)
        VKEcosystemPage.attach_screenshot()

    with allure.step('Проверка возврата на исходную страницу'):
        LoginPageHelper(browser)
        LoginPage.attach_screenshot()