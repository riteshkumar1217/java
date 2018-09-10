from Onlineassessment.PageObject.pages.landingpage import landingpage
from Onlineassessment.TestBase.envsetup import envSetup
from Onlineassessment.TestUtility.screenshot import SS


class Oa(envSetup):
    def test_landing(self):
        driver = self.driver
        self.driver.get('https://ams.hirepro.in/onlineassessment')
        print 'URL Entered'
        aliasobj = landingpage(driver)
        aliasobj.setAlias('at')
        aliasobj.okbutton

        ss=SS(driver)