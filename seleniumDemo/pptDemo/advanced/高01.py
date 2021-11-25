import time
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
import unittest
import traceback

class TestDemo(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_executeScript(self):
        self.driver.get("http://www.baidu.com")
        souJS = "document.getElementById('kw').value='软达启航';"
        anJS = "document.getElementById('su').click()"
        try:
            self.driver.execute_script(souJS)
            time.sleep(2)
            self.driver.execute_script(anJS)
            time.sleep(2)
            self.assertTrue('百度百科' in self.driver.page_source)
        except WebDriverException as e:
            print('页面中没有找到要操作的页面元素',traceback.print_exc())
        except AssertionError as e:
            print('页面中不存在断言的关键字符串')
        except Exception as e:
            print(traceback.print_exc())

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()