import time
import unittest
from selenium import webdriver

class Test_baidu_Sou(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome()


    @classmethod
    def tearDownClass(self):
        self.driver.quit()


    def setUp(self):
        self.driver.get('http://www.baidu.com')

    def tearDown(self):
        pass

    def test_sou(self):
        self.driver.find_element_by_id('kw').send_keys('华为')
        time.sleep(2)
        self.driver.find_element_by_id('su').click()
        time.sleep(2)
        self.assertEqual('华为_百度搜索',self.driver.title,'标题错误')

if __name__ == '__main__':
    unittest.main()