import unittest,HTMLTestRunner_cn
from first.tools import *

suite = unittest.defaultTestLoader.discover('./',pattern='test_qq.py')

if __name__=='__main__':
    filename = 'result.html'
    runner = HTMLTestRunner_cn.HTMLTestRunner(open(filename,'wb') ,
                                           title='5月19日Test',
                                           description='''
                                           a;lskfj;asdfj;afd
                                                ''')
    runner.run(suite)
    SendMailAttach(filename)