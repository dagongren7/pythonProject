import time
from selenium import webdriver
import unittest, time


class TestDemo(unittest.TestCase):
    def setUp(self):
        profile = webdriver.FirefoxProfile()
        profile.set_preference('browser.download.dir', 'd:\\xiazai')
        profile.set_preference('browser.download.folderList', 2)
        profile.set_preference('browser.helperApps.alwaysAsk.force', False)
        profile.set_preference('browser.download.manager.showWhenStarting', False)
        profile.set_preference('browser.download.manager.useWindow', False)
        profile.set_preference('browser.download.manager.focusWhenStarting', False)
        profile.set_preference('browser.download.manager.alertOnEXEOpen', False)
        profile.set_preference('browser.helperApps.neverAsk.openFile', 'application/pdf')
        profile.set_preference('browser.helperApps.neverAsk.saveToDisk', 'application/zip,application/exe')
        profile.set_preference('browser.download.manager.showAlertOnComplete', False)
        profile.set_preference('browser.download.manager.closeWhenDone', False)
        self.driver = webdriver.Firefox(firefox_profile=profile)

    def test_dataPicker(self):
        self.driver.get("https://www.python.org/downloads/release/python-365/")
        self.driver.find_element_by_xpath('/html/body/div/div[3]/div/section/article/table/tbody/tr[9]/td[1]/a').click()
        time.sleep(10)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()