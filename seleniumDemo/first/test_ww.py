import unittest,time
from selenium import webdriver
from time import sleep
class Test_SoGou(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Firefox()

    @classmethod
    def tearDownClass(self):
        self.driver.quit()
    def setUp(self):
        self.driver.get("http://www.sogou.com/")

    def test_zhongwen(self):
        self.driver.find_element_by_id('query').send_keys('老胡')
        self.driver.find_element_by_id('stb').click()
        time.sleep(2)
        self.assertEqual(self.driver.title,'老胡 - 搜狗搜索')

    def test_english(self):
        self.driver.find_element_by_id('query').send_keys('Demon')
        self.driver.find_element_by_id('stb').click()
        time.sleep(2)
        self.assertEqual(self.driver.title,'Demon - 搜狗搜索')

    def test_pinyin(self):
        self.driver.find_element_by_id('query').send_keys('laohu')
        self.driver.find_element_by_id('stb').click()
        time.sleep(2)
        self.assertEqual(self.driver.title,'laohu - 搜狗搜索')


if __name__ == '__main__':
    unittest.main()
