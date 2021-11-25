from selenium import webdriver
import unittest,time,traceback
from ObjectMap import ObjectMap

class Test(unittest.TestCase):
    def setUp(self):
        self.obj = ObjectMap()
        self.driver = webdriver.Chrome()
    def testSouSuo(self):
        self.driver.get("http://www.sogou.com")
        try:
            searchBox = self.obj.getElementObject(self.driver,"sogou","searchBox")
            searchButton = self.obj.getElementObject(self.driver,"sogou","searchButton")
            searchBox.send_keys('软达启航')
            searchButton.click()
            time.sleep(3)
            self.assertTrue("软达启航" in self.driver.page_source,'assertFalse')
        except Exception as e:
            print(traceback.print_exc())
    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()