import time
from selenium import webdriver
import unittest,time
import win32api
class TestDemo(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
    def test_uploadFile(self):
        self.driver.get("http://sahitest.com/demo/php/fileUpload.htm")
        upload = self.driver.find_element_by_id('file')
        upload.send_keys('d:\\netcat-win32-1.12.zip')  # send_keys
        print(upload.get_attribute('value'))
    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
