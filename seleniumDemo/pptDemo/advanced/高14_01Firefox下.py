from selenium import webdriver
import unittest,time
class TestDemo(unittest.TestCase):
    def setUp(self):
        firefox_profile = webdriver.FirefoxProfile()
        firefox_profile.set_preference('permissions.default.stylesheet',2)
        firefox_profile.set_preference('permissions.default.image',2)
        firefox_profile.set_preference('dom.ipc.plugins.enabled.libflashplayer.so','false')
        self.driver = webdriver.Firefox(firefox_profile = firefox_profile)
    def test_jinImg(self):
        self.driver.get("http://www.kongfz.com")
        time.sleep(20)
    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()