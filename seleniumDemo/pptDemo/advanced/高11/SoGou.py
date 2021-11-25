#测试过程中发生异常或断言失败时进行屏幕截图

from selenium import webdriver
import unittest, time, os
from FileUtil import createDir
import traceback

#创建存放异常截图的目录，并得到本次实例中存放图片目录的绝对路径，并且作为全局变量，以共本次所有测试用例调用
picDir = createDir()

def takeScreenshot(driver, savePath, picName):
    # 封装截屏方法
    # 构造屏幕截图路径及图片名
    picPath = os.path.join(savePath + '.png')
    try:
        # 调用WebDriver提供的get_screenshot_as_file()方法
        # 将截取的屏幕图片保存为本地文件
        driver.get_screenshot_as_file(picPath)
    except Exception as e:
        print(traceback.print_exc())

class TestFailCaptureScreen(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def testSoGouSearch(self):
        self.driver.get('http://www.sogou.com')
        try:
            self.driver.find_element_by_id('query').send_keys('软达启航')
            self.driver.find_element_by_id('stb').click()
            time.sleep(3)
            self.assertTrue('事在人为' in self.driver.page_source,
                            "事在人为‘关键字串在页面源代码中未找到")
        except AssertionError as e:
            #调用封装好的截图方法，进行截图并保存在本地磁盘
            takeScreenshot(self.driver,picDir,e)
        except Exception as e:
            print(traceback.print_exc())
            takeScreenshot(self.driver,picDir,e)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()