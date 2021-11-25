#使用Chrome浏览器自动将文件下载到指定路径

from selenium import webdriver
import unittest,time

class TestDemo(unittest.TestCase):
    def setUp(self):
        chromeOptions = webdriver.ChromeOptions()
        prefs = {'download.default_directory':'e:\\download'}
        chromeOptions.add_experimental_option('prefs',prefs)
        self.driver = webdriver.Chrome()

    def test_downloadFileByChrome(self):
        url = 'https://pypi.org/project/selenium/#files'
        self.driver.get(url)
        self.driver.find_element_by_partial_link_text\
            ("selenium-3.11.0-py2.py3-none-any.whl").click()
        time.sleep(100)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()