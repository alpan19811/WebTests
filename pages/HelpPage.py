from selenium.webdriver import ActionChains

from pages.BasePage import BasePageHelper
from selenium.webdriver.common.by import By
import allure


class HelpPageLocators:
    SEARCH_FIELD = (By.XPATH, '//input[@type="search"]')
    ACTUAL_TODAY = (By.XPATH, '//*[@href="/help/segodnya-aktualno"]')
    REGISTRATION = (By.XPATH, '//*[@href="/help/registraciya"]')
    MY_PROFILE = (By.XPATH, '//*[@href="/help/moi-profil"]')
    COMMUNICATION = (By.XPATH, '//*[@href="/help/obshchenie"]')
    PROFILE_ACCESS = (By.XPATH, '//*[@href="/help/dostup-k-profilu"]')
    SECURITY = (By.XPATH, '//*[@href="/help/bezopasnost"]')
    GROUPS = (By.XPATH, '//*[@href="/help/gruppy"]')
    PAYED_FUNCTIONS = (By.XPATH, '//*[@href="/help/platnye-funkcii"]')
    SPAM = (By.XPATH, '//*[@href="/help/narusheniya-i-spam"]')
    GAMES_AND_APPS = (By.XPATH, '//*[@href="/help/igry-i-prilojeniya"]')
    OTHER_SERVICES = (By.XPATH, '//*[@href="/help/drugie-servisy"]')
    IMPORTANT_INFORMATION = (By.XPATH, '//*[@href="/help/poleznaya-informaciya"]')


class HelpPageHelperHelper(BasePageHelper):
    def __init__(self, driver):
        self.driver = driver
        self.check_page()

    def check_page(self):
        with allure.step('Проверяем корректность загрузки страницы'):
            self.attach_screenshot()
        self.find_element(HelpPageLocators.SEARCH_FIELD)
        self.find_element(HelpPageLocators.ACTUAL_TODAY)
        self.find_element(HelpPageLocators.REGISTRATION)
        self.find_element(HelpPageLocators.MY_PROFILE)
        self.find_element(HelpPageLocators.COMMUNICATION)
        self.find_element(HelpPageLocators.PROFILE_ACCESS)
        self.find_element(HelpPageLocators.SECURITY)
        self.find_element(HelpPageLocators.GROUPS)
        self.find_element(HelpPageLocators.PAYED_FUNCTIONS)
        self.find_element(HelpPageLocators.SPAM)
        self.find_element(HelpPageLocators.GAMES_AND_APPS)
        self.find_element(HelpPageLocators.OTHER_SERVICES)
        self.find_element(HelpPageLocators.IMPORTANT_INFORMATION)

    def scrollToitem(self, locator):
        scroll_item = self.find_element(locator)
        ActionChains(self.driver).scroll_to_element(scroll_item).click(scroll_item).perform()



