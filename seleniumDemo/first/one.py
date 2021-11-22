from selenium import webdriver
from time import sleep
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import unittest
import os
class DoubanTest(unittest.TestCase):1
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("http://www.baidu.com")
        sleep(2)
    def tearDown(self):
        # self.driver.quit()
        self.driver.quit()
    def test_add(self):
        element = self.driver.find_element_by_xpath(".//*[@id='lg']/img")
        self.driver.find_element_by_id("kw").send_keys("hehe")
        sleep(3)
        self.driver.find_element_by_id("su").click()
        sleep(2)
if __name__ =='__main__':
    unittest.main()
