import allure

from core.BaseTest import browser
from pages.BasePage import BasePageHelper
from pages.HelpPage import HelpPageHelperHelper, HelpPageLocators
from pages.ImportantInformationHelp import ImportantInformationHelpHelper

BASE_URL = 'https://ok.ru/help'


def test_help_test(browser):
    BasePageHelper(browser).get_url(BASE_URL)
    HelpPage = HelpPageHelperHelper(browser)
    HelpPage.scrollToitem(HelpPageLocators.IMPORTANT_INFORMATION)
    ImportantInformationHelpHelper(browser)