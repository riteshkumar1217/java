from selenium.common.exceptions import NoSuchElementException
import time
from Onlineassessment.PageObject.Locators import locator
from selenium.webdriver.common.by import By
class testPage(object):
    def __init__(self, driver):
        self.driver = driver
        try:
            self.ans = driver.find_element(By.ID, locator.answeroption)
            self.nextButton = driver.find_element(By.NAME, locator.nextbutton)
            self.submitBtn = driver.find_element(By.NAME, locator.submitbutton)
            self.confirmsubmit = driver.find_element(By.XPATH, locator.okconfirmationbutton)
            self.rusure = driver.find_element(By.XPATH, locator.confirmationmessage)
            self.submitmessage = driver.find_element(By.XPATH, locator.submitresponse)
        except (NoSuchElementException) as e:
            print e
    def clickNext(self):
        while (self.nextButton.is_enabled()):
            time.sleep(1)
            self.nextButton.click()

    def checkedAnswer(self):
        self.ans.click()
        time.sleep(2)

    def submit(self):
        self.submitBtn.click()

    def clickConfirmSubmit(self):
        self.confirmsubmit.click()

    def clcikRUSure(self):
        print self.rusure.text

    def readSumitResponse(self):
        print self.submitmessage.text

