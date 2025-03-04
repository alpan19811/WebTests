from pages.BasePage import BasePage
from selenium.webdriver.common.by import By

class LoginPageLocators:
    LOGIN_TAB = (By.XPATH, '// *[ @ id = "login-5522540423"]')
    QR_TAB = (By.XPATH, '// *[ @ id = "qrCode-5522540458"]')
    LOGIN_FIELD = (By.XPATH, '//*[@id="field_email"]') # если есть ID, то можно переписать код By.ID, "field_email"
    PASSWORD_FIELD = (By.XPATH, '//*[@id="field_password"]')
    LOG_IN_BUTTON = (By.XPATH, '//*[@id="tabpanel-login-5522540423"]/form/div[4]/input')
    LOG_IN_WITH_QR_BUTTON(By.XPATH, '//*[@id="qrCode-5522540458"]/span')
    CANT_LOG_IN_LINK(By.XPATH, '//*[@id="tabpanel-login-5522540423"]/form/div[4]/div[1]/a')
    NO_PROFILE_ON_OK_LINK(By.XPATH,'//*[@id="tabpanel-login-5522540423"]/form/div[4]/div[2]/div[1]/div')
    REGISTER_BUTTON(By.XPATH, '//*[@id="tabpanel-login-5522540423"]/form/div[4]/div[2]/a')
    LOG_IN_WITH_VK_ID_BUTTON(By.XPATH, '//*[@id="tabpanel-login-5522540423"]/form/div[4]/div[2]/div[2]/a[1]/i')
    LOG_IN_WITH_MAIL_BUTTON(By.XPATH, '//*[@id="tabpanel-login-5522540423"]/form/div[4]/div[2]/div[2]/a[2]/i')
    LOG_IN_WITH_YANDEX_BUTTON(By.XPATH, '//*[@id="tabpanel-login-5522540423"]/form/div[4]/div[2]/div[2]/a[3]/i')


class LoginPageHelper(BasePage):
    pass
