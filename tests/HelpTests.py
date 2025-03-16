import allure

from core.BaseTest import browser
from pages.BasePage import BasePage
from pages.HelpPage import HelpPageHelper, HelpPageLocators
from pages.ImportantInformationHelp import ImportantInformationHelpHelper

BASE_URL = 'https://ok.ru/help'


def test_help_test(browser):
    BasePage(browser).get_url(BASE_URL)
    HelpPage = HelpPageHelper(browser)
    HelpPage.scrollToitem(HelpPageLocators.IMPORTANT_INFORMATION)
    ImportantInformationHelpHelper(browser)