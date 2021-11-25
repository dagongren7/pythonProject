from selenium import webdriver
import unittest,time
import win32gui,win32con
class TestDemo(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
    def test_uploadFile(self):
        self.driver.get("http://sahitest.com/demo/php/fileUpload.htm")
        upload = self.driver.find_element_by_id('file')
        print(upload)
        upload.click()
        time.sleep(2)
        # win32gui
        dialog = win32gui.FindWindow('#32770', '文件上传')  # 对话框
        ComboBoxEx32 = win32gui.FindWindowEx(dialog, 0, 'ComboBoxEx32', None)
        ComboBox = win32gui.FindWindowEx(ComboBoxEx32, 0, 'ComboBox', None)
        Edit = win32gui.FindWindowEx(ComboBox, 0, 'Edit', None)  # 上面三句依次寻找对象，直到找到输入框Edit对象的句柄
        button = win32gui.FindWindowEx(dialog, 0, 'Button', None)  # 确定按钮Button

        win32gui.SendMessage(Edit, win32con.WM_SETTEXT, None, 'd:\\netcat-win32-1.12.zip')  # 往输入框输入绝对地址
        win32gui.SendMessage(dialog, win32con.WM_COMMAND, 1, button)  # 按button
        print(upload.get_attribute('value'))
    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()