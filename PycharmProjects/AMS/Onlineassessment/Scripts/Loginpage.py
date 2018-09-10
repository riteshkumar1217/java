import time

from Onlineassessment.PageObject.pages.login import Login
from Onlineassessment.TestBase.envsetup import envSetup
from Onlineassessment.TestUtility.screenshot import SS


class Logins(envSetup):
    def test_login(self):
        driver = self.driver
        window_before = driver.window_handles[0]

        driver.get('https://ams.hirepro.in/onlineassessment/#/assess/login/eyJhbGlhcyI6ImF0In0=')
        window_after = driver.window_handles[1]

        driver.switch_to_window(window_after)
        print ('Switched to child window')
        time.sleep(3)
        loginobj = Login(driver)

        print ('window swtiched successfully')
        loginobj.setusername('admin')
        loginobj.setPasword('sajd')
        time.sleep(3)
        loginobj.getCompanyinfo()


        ss=SS(driver)