import time

from Onlineassessment.Scripts.testpreview import TestPreview
from Onlineassessment.PageObject.pages.testpage import testPage
class Normaltest(TestPreview):

    def setUpClass(self):
        # type: # () -> object
        super(Normaltest, self).setUpClass()

    def test_normal(self):
        print 'Inherited successfully'
        driver = self.driver
        testPage_Obj = testPage(driver)
        try:
            # for i in range(0,24):
                # time.sleep(10)
                # testPage_Obj.checkedAnswer()
                # # time.sleep(10)
                # driver.implicitly_wait(10)
                # testPage_Obj.clickNext()
                # time.sleep(10)
                while (driver.find_element_by_name('btnNext').is_enabled()):
                    time.sleep(1)
                    driver.find_element_by_id('A').click()
                    time.sleep(1)
                    driver.find_element_by_name('btnNext').click()
                    time.sleep(1)

        except Exception as e:
            print str(e)
        driver.find_element_by_name('btnSubmit').click()


Normaltest_Obj = Normaltest()
Normaltest_Obj.test_normal()



