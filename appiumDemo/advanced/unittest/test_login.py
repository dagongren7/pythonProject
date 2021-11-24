import unittest
from appiumDemo.advanced.page_object.loginView import LoginView
from appiumDemo.advanced.unittest.myunit import StartEnd


class TestLogin(StartEnd):

    def test_login_zxw2018(self):
        l=LoginView(self.driver)
        l.login_action('自学网2018','zxw2018')

    def test_login_zxw2017(self):
        l=LoginView(self.driver)
        l.login_action('自学网2017','zxw2017')

    def test_login_error(self):
        l = LoginView(self.driver)
        l.login_action('6666', '222')

if __name__ == '__main__':
    unittest.main()