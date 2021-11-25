#encoding=utf-8
from selenium import webdriver
from ReportTemplate import htmlTemplate
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

@ddt.ddt
class TestDemo(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        TestDemo.trStr=""
    def setUp(self):
        self.driver = webdriver.Chrome()
        status = None  #用于存放测试结果状态
        flag = 0 #数据驱动测试结果的标志，失败0 成功1
    
    @ddt.file_data("test_data_list.json")
    def test_dataDrivenByFile(self,value):
        flagDict = {0:'red',1:'00FF00'}
        self.driver.get("http://www.baidu.com/")
        testdata,expectdata = tuple(value.strip().split("||"))
        time.sleep(5)
        try:
            start = time.time()
            startTime = time.strftime(" %Y - %M - %d %H:%M:%S",time.localtime())
            self.driver.find_element_by_id("kw").send_keys(testdata)
            self.driver.find_element_by_id("su").click()
            time.sleep(3)
            self.assertTrue(expectdata in self.driver.page_source)
        except NoSuchElementException as e:
            logging.error("查找的页面元素不存在，异常信息："
                          +str(traceback.format_exc()))
            status = 'fail'
            flag = 0
        except AssertionError as e:
            logging.info('搜索 \' %r\',期望 \' %r\',失败' %(testdata,expectdata,))
            status = 'fail'
            flag = 0
        except Exception as e:
            logging.error('未知错误，信息：'+str(traceback.format_exc()))
            status = 'fail'
            flag = 0
        else:
            logging.info("搜索 ' %r',期望 ' %r',通过" %(testdata,expectdata,))
            status = 'pass'
            flag = 1
            
        wasteTime = time.time() - start - 3 
        TestDemo.trStr += '''
        <tr>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>%.2f</td>
            <td style="color:%s">%s</td>
        </tr><br />''' %(testdata,expectdata,startTime,
                         wasteTime,flagDict[flag],status)
        
    def tearDown(self):
        self.driver.quit()
    
    @classmethod
    def tearDownClass(cls):
        htmlTemplate(TestDemo.trStr)

if __name__ == '__main__':
    unittest.main()