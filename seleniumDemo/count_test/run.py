# import unittest,HTMLTestRunner
#
# suite = unittest.defaultTestLoader.discover('./',pattern='num.py')
#
# if __name__=='__main__':
#     runner = HTMLTestRunner.HTMLTestRunner(open('./report.html','wb'),title='hehe',description='haha')
#     runner.run(suite)

import logging

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename='myapp.log',
                    filemode='a')

logging.debug('This is debug message')
logging.info('This is info message')
logging.warning('This is warning message')

