import thread

from selenium.common.exceptions import NoSuchElementException

from Onlineassessment.PageObject.Locators import locator
from selenium.webdriver.common.by import By
from Onlineassessment.TestBase import envsetup
from selenium import webdriver
from selenium.webdriver.common.by import By

class landingpage:
    def __init__(self, driver):
        self.driver = driver
        # Landing page locator defing
        try:
            self.alias = driver.find_element(By.XPATH, locator.tenantalias)
            self.okbutton = driver.find_element(By.XPATH, locator.okButton)
        except (NoSuchElementException) as e:
            print e
    def setAlias(self,alias):
        # self.alias.clear()
        self.alias.send_keys(alias)
        thread.sleep(5)
        print 'Alias entered successflly'
    def clickOk(self,okbutton ):
        self.okbutton.click( )
        thread.sleep(3)
        print 'Clicked  ok'