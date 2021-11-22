import unittest,time
from selenium import webdriver

class Test_Baidu(unittest.TestCase):
    '''这是一个类注释'''
    @classmethod
    def setUpClass(self):
        '''这是一个方法注释'''
        self.driver = webdriver.Firefox()
        self.driver.get("http://www.baidu.com/")
    @classmethod
    def tearDownClass(self):
        self.driver.quit()

    def test_zhongwen(self):
        self.driver.find_element_by_id('kw').clear()
        self.driver.find_element_by_id('kw').send_keys('老胡')
        self.driver.find_element_by_id('su').click()
        time.sleep(2)
        self.assertEqual(self.driver.title,'老胡_百度搜索')

    def test_english(self):
        self.driver.find_element_by_id('kw').clear()
        self.driver.find_element_by_id('kw').send_keys('Demon')
        self.driver.find_element_by_id('su').click()
        time.sleep(2)
        self.assertEqual(self.driver.title,'Demon_百度搜索')

    def test_pinyin(self):
        self.driver.find_element_by_id('kw').send_keys('laohu')
        self.driver.find_element_by_id('su').click()
        time.sleep(2)
        self.assertEqual(self.driver.title,'laohu_百度搜索')


if __name__ == '__main__':
    unittest.main()
