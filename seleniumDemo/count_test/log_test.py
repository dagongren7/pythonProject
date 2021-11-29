from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import unittest,time,ddt,logging,traceback

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
        #打开日志文件的方式 w a 两种方式
        filemode ='a'
        )

@ddt.ddt
class TestDemo(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
    def tearDown(self):
        self.driver.quit()
    @ddt.data(['老胡','老胡_百度搜索'])#,['Demon','Demon_百度搜索'],['laohu','laohu_百度搜索']
    @ddt.unpack
    def test_dataDrivenByObj(self,testdata,exceptdata):
        self.driver.get('https://www.baidu.com/')
        try:
            self.driver.find_element_by_id('kwe').send_keys(testdata)
            self.driver.find_element_by_id('su').click()
            time.sleep(3)
            self.assertTrue(exceptdata in self.driver.page_source)
        except NoSuchElementException as e:
            logging.error("查找的页面元素不存在，异常堆栈信息："+str(traceback.format_exc()))
        except AssertionError as e:
            logging.info('搜索 \' %r\',期望 \' %r\',失败' %(testdata,exceptdata,))
        except Exception as e:
            logging.error('未知错误，信息：'+str(traceback.format_exc()))
        else:
            logging.info("搜索 ' %r',期望 ' %r',通过" %(testdata,exceptdata,))
if __name__ =='__main__':
    unittest.main()
