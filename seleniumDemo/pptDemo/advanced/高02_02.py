from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import traceback
import unittest
import time

class TestDemo(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
    def test_AjaxDivOptionByKeys(self):
        self.driver.get("http://www.sogou.com/")
        try:
            searchBox = self.driver.find_element_by_id('query')
            searchBox.send_keys('软达启航')
            time.sleep(2)
            sugetion_option = self.driver.find_element_by_xpath("//ul/li[contains(.,'乔丹')]")
            sugetion_option.click()
            time.sleep(3)
        except NoSuchElementException as e:
            print("没有找到相关项")
        except Exception as e:
            print(traceback.print_exc())
    def tearDown(self):
        self.driver.quit()
if __name__ == '__main__':
    unittest.main()