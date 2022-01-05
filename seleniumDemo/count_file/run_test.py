import ddt,time
import unittest
from selenium import webdriver
from seleniumDemo.count_file.ReportTemplate import htmlTemplate
from selenium.common.exceptions import NoSuchElementException
import logging,traceback
'''
=数据驱动：从json文件中读取数据
'''
@ddt.ddt
class DoubanTest(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        DoubanTest.TestDemo=''
        self.driver = webdriver.Chrome()
    @classmethod
    def tearDownClass(self):
        print(DoubanTest.TestDemo)
        self.driver.quit()
        htmlTemplate(DoubanTest.TestDemo)

    def setUp(self):
        self.driver.get('http://www.baidu.com/')
    def tearDown(self):
        pass
    @ddt.file_data('data.json')
    @ddt.unpack
    def test_baidu(self,value):
        #数据字典
        flagDict = {0:'red',1:'green'}
        can, yu = value.split('||')
        try:
            start = time.time()
            startTime = time.strftime(" %Y - %M - %d %H:%M:%S",time.localtime())
            time.sleep(2)
            self.driver.find_element_by_id('kw').send_keys(can)
            time.sleep(2)
            self.driver.find_element_by_id('su').click()
            time.sleep(2)
            self.assertIn(yu,self.driver.page_source)
        except NoSuchElementException as e:
            logging.error("查找的页面元素不存在，异常信息："
                          + str(traceback.format_exc()))
            status = 'fail'
            flag = 0
        except AssertionError as e:
            logging.info('搜索 \' %r\',期望 \' %r\',失败' % (can, yu,))
            status = 'fail'
            flag = 0
        except Exception as e:
            logging.error('未知错误，信息：' + str(traceback.format_exc()))
            status = 'fail'
            flag = 0
        else:
            logging.info("搜索 ' %r',期望 ' %r',通过" % (can, yu,))
            status = 'pass'
            flag = 1

        wasteTime = time.time() - start
        DoubanTest.TestDemo += '''
        <tr>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>%.2f</td>
            <td style="color:%s">%s</td>
        </tr><br />''' % (can, yu, startTime,
                          wasteTime, flagDict[flag], status)
if __name__ =='__main__':
    unittest.main()