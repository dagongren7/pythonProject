import unittest
import logging
from time import sleep

from appiumDemo.unityDemo.kyb_testProject.common.desired_caps import appium_desired

'''
封装一个类，相当于dao层的一个对象实现，给他开始结束
'''
class StartEnd(unittest.TestCase):
    def setUp(self):
        logging.info('=====setUp====')
        self.driver=appium_desired()

    def tearDown(self):
        logging.info('====tearDown====')
        sleep(5)
        self.driver.close_app()