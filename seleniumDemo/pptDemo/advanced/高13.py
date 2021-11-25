from selenium import webdriver
import unittest,time,requests
class TestDemo(unittest.TestCase):
    def __init__(self):
        self.i = 1
    def setUp(self):
        print("开始")
        self.text = ""
    def test_ipadChrome(self):
        self.text = "ipadChrome"
        requests.get("http://www.baidu.com", headers={"User-Agent":"Mozilla/5.0(Linux;U;Android 2.3.6;en-us;Nexus S Build/GRK39F)AppleWebKit/533.1(KHTML,like Gecko)Version/4.0 Mobile Safari/533.1"})
        driver = webdriver.Chrome()
        driver.get('http://www.baidu.com')
        time.sleep(3)
        driver.find_element_by_id('kw').send_keys('iPad')
        time.sleep(2)
        #查看伪装效果
        driver.get('about:version')
        time.sleep(10)
        driver.quit()

    def test_iPhoneChrome(self):
        self.text = "iPhoneChrome"
        options = webdriver.ChromeOptions()
        requests.get("http://m.baidu.com", headers={'User-Agent':'Mozilla/5.0(iPhone;CPU iPhone 5_0 like Mac OS X)AppleWebKit/534.46 (KHTML,like Gecko)Version/5.1 Mobile/9A334 Safari/7534.48.3'})
        driver = webdriver.Chrome(chrome_options=options)
        driver.get('http://m.baidu.com')
        time.sleep(2)
        driver.find_element_by_id('index-kw').send_keys('iPhone')
        time.sleep(2)
        driver.get('about:version')
        time.sleep(10)
        driver.quit()

    def test_Android236Chrome(self):
        self.text = "Android236Chrome"
        options = webdriver.ChromeOptions()
        mobileEmulation = {'deviceName': 'Apple iPhone 4'}
        options.add_experimental_option('mobileEmulation', mobileEmulation)
        options.add_argument('user-agent="Mozilla/5.0(Linux;U;Android 2.3.6;en-us;Nexus S Build/GRK39F)AppleWebKit/533.1(KHTML,like Gecko)Version/4.0 Mobile Safari/533.1"')
        driver = webdriver.Chrome(chrome_options=options)
        driver.get('http://m.baidu.com')
        time.sleep(2)
        driver.find_element_by_id('index-kw').send_keys('Android 2.3.6')
        time.sleep(2)
        driver.get('about:version')
        time.sleep(10)
        driver.quit()

    def test_Android402Chrome(self):
        self.text = "Android402Chrome"
        options = webdriver.ChromeOptions()
        options.add_argument('user-agent=Mozilla/5.0(Linux;U;Android 4.0.2;en-us;Galaxy Nexus Build/ICL53F)AppleWebKit/534.30(KHTML,like Gecko)Version/4.0 Mobile Safari/534.30')
        driver = webdriver.Chrome(chrome_options=options)
        driver.get('http://m.baidu.com')
        time.sleep(2)
        driver.find_element_by_id('index-kw').send_keys('Android 4.0.2')
        time.sleep(2)
        time.sleep(10)
    def tearDown(self):

        print(self.i)
        self.i = self.i + 1
        print("结束：",self.text)
if __name__ == '__main__':
    unittest.main()