from selenium.common.exceptions import NoSuchElementException
from Onlineassessment.PageObject.Locators import locator
from selenium.webdriver.common.by import By

class startTestPage(object):
    def __init__(self, driver):
        self.driver = driver
        try:

            self.termcondition = driver.find_element(By.XPATH, locator.tc)
            self.start = driver.find_element(By.NAME, locator.starttestButton)
        except (NoSuchElementException) as e:
            print e

    def checked_Tc(self):

        self.termcondition.click()

    def startTest(self):
        self.start.click()
