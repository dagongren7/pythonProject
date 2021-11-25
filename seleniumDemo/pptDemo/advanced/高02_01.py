from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
import time

class TestDemo(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
    def test_AjaxDivOptionByKeys(self):
        self.driver.get("http://www.sogou.com/")
        searchBox = self.driver.find_element_by_id('query')
        searchBox.send_keys('wwe')
        time.sleep(2)
        for i in range(3):
            searchBox.send_keys(Keys.DOWN)
            time.sleep(1)
        searchBox.send_keys(Keys.ENTER)
        time.sleep(4)
    def tearDown(self):
        self.driver.quit()
if __name__ == '__main__':
    unittest.main()