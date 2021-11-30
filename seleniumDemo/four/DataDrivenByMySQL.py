from selenium import webdriver
from seleniumDemo.four.MysqlUtil import MyMySQL
from selenium.common.exceptions import NoSuchElementException
import unittest,time,logging,traceback,ddt
#初始化日志对象
logging.basicConfig(
        #日志级别
        level = logging.INFO,
        #日志格式
        #时间、代码所在文件名、代码行号、日志级别名字、日志信息
        format = '%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
        #打印日志的时间
        datefmt = '%a, %d %b %Y %H:%M:%S',
        #日志文件存放的目录(目录必须存在)及日志文件名
        filename = './report.log',
        #打工日志文件的方式
        filemode ='w'
        )
def getTestDatas():
    
    db = MyMySQL(
        host = "localhost",
        dbName = "test",
        username = "root",
        password = "123456",
        charset = "utf8"       
        )
    
    testData = db.getDataFromDataBases()
    db.closeDataBase()
    return testData

@ddt.ddt
class Test(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
    def tearDown(self):
        self.driver.quit()
        
    @ddt.data( * getTestDatas())
    def test_dataDrivenByDatabase(self,data):
        testData,expectData = data
        self.driver.get("http://www.baidu.com/")
        time.sleep(3)
        
        try:
            self.driver.find_element_by_id("kw").send_keys(testData)
            self.driver.find_element_by_id("su").click()
            time.sleep(3)
            self.assertTrue(expectData in self.driver.page_source)
        except NoSuchElementException as e:
            logging.error("查找的页面元素不存在，异常信息："
                          +str(traceback.format_exc()))
        except AssertionError as e:
            logging.info('搜索 \' %r\',期望 \' %r\',失败' %(testData,expectData,))
        except Exception as e:
            logging.error('未知错误，信息：'+str(traceback.format_exc()))
        else:
            logging.info("搜索 ' %r',期望 ' %r',通过" %(testData,expectData,))



if __name__ == "__main__":
    unittest.main()