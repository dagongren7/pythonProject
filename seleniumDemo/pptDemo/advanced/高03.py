import traceback

from selenium import webdriver
import unittest
import os
from selenium.common.exceptions import NoSuchElementException

class TestDemo(unittest.TestCase):
    def test_killWindowsProcess(self):
        try:
            chromeDriver = webdriver.Chrome()
            returnCode = os.system("taskkill /f /t /im chrome.exe")
            if returnCode == 0:
                print("chrome进程结束成功")
        except Exception as e:
            print(traceback.print_exc())
if __name__ == '__main__':
    unittest.main()