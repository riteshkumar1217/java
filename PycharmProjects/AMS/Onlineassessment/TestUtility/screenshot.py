from selenium import webdriver
class SS(object):
    def __init__(self, driver):
        self.driver = driver

    def screenshot(self, path):
        directory='C:\Users\training.HIREPRO\PycharmProjects\AMS\Onlineassessment\Screenshot'
        self.driver.driver.getscreenshot_as_file(directory+path)

