from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys

from Onlineassessment.PageObject.Locators import locator
from selenium.webdriver.common.by import By


class Login(object):
    def __init__(self, driver):
        self.driver = driver
        try:
            self.login = driver.find_element(By.NAME, locator.loginname)
            self.password = driver.find_element(By.NAME, locator.password)
            self.companyinfos = driver.find_element(By.CSS_SELECTOR, locator.companyinfo)
            self.logintotests = driver.find_element(By.XPATH, locator.loginbutton)
        except (NoSuchElementException) as e:
            print e

    def setusername(self, loginname):
        self.login.send_keys(loginname)
        print 'login name entered'

    def setPasword(self, password):
        self.password.send_keys(password)
        print 'password entered'

    def getCompanyinfo(self):
        print self.companyinfos.text

    def clickLogin(self):
        print self.logintotests.is_displayed
        self.logintotests.send_keys(Keys.ENTER)

    def getInvalidsLogin(self):
        try:
            self.invalid_credentials = self.driver.find_element(By.CSS_SELECTOR, locator.invalidlogin)
            if hasattr(self, 'invalid_credentials'):
                print self.invalid_credentials.text
        except (NoSuchElementException) as e:
            print 'Login successfully'



