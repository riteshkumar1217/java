import time
from Onlineassessment.TestBase.envsetup import envSetup
from Onlineassessment.PageObject.pages.starttest import startTestPage
from Onlineassessment.PageObject.pages.login import Login



class TestPreview(envSetup):
    def __init__(self):
        # type: # () -> object
        super(TestPreview, self).__init__()
        self.test_open_preview()

    def test_open_preview(self):
        driver = self.driver
        window_before = driver.window_handles[0]
        time.sleep(1)
        driver.get('https://amsin.hirepro.in/onlineassessment/#/assess/login/eyJhbGlhcyI6ImF0In0=')
        # time.sleep(5)
        try:
            window_after = driver.window_handles[1]
            driver.switch_to_window(window_after)
        except IndexError as e:
            print e

        time.sleep(5)
        # driver.switch_to_window(window_after)
        # time.sleep(3)
        login_obj = Login(driver)
        login_obj.setusername(self.Login_name)
        login_obj.setPasword(self.Password)
        login_obj.getCompanyinfo()
        # self.test_open_preview.getCompanyinfo()
        login_obj.clickLogin()
        print 'login button clicked successfully'
        login_obj.getInvalidsLogin()
        time.sleep(3)
        starttestobj = startTestPage(driver)
        time.sleep(3)
        starttestobj.checked_Tc()
        time.sleep(3)
        starttestobj.startTest()
        print 'Test started'

        # time.sleep(4)
        # testpageobj = testPage(driver)
        # # time.sleep(4)
        # # testpageobj.checkedAnswer()
        # time.sleep(3)
        # testpageobj.clickNext()