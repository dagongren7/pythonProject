from selenium import webdriver
import unittest,time,traceback
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException,NoSuchElementException

class TestDemo(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
    def test_killWindowsProcess(self):
        self.driver.get("http://jqueryui.com/resources/demos/datepicker/other-months.html")
       #直到找到元素
        try:
            wait = WebDriverWait(self.driver,10,0.2)
            wait.until(EC.element_to_be_clickable((By.ID,'datepicker')))
        except TimeoutException as e:
            print(traceback.print_exc())
        except NoSuchElementException as e:
            print(traceback.print_exc())
        except Exception as e:
            print(traceback.print_exc())
        else:
            dateInputBox = self.driver.find_element_by_id('datepicker')
            dateInputBox.send_keys('11/24/2018')
            time.sleep(3)
if __name__ == '__main__':
    unittest.main()
