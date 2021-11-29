import unittest,HTMLTestRunner_cn

suite = unittest.defaultTestLoader.discover('./',pattern='test_qq.py')

if __name__=='__main__':
    filename = 'result.html'
    runner = HTMLTestRunner_cn.HTMLTestRunner(open(filename,'wb') ,
                                           title='1129',
                                           description='''
                                           好的
                                                ''')
    runner.run(suite)
    # SendMailAttach(filename)