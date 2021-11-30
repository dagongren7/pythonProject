# 导入selenium封装类
from seleniumDemo.unitestDemo.Commonlib.Commonlib import Commonshare

class testDemo(Commonshare):
    def function1(self,data):
        self.open_url('http://www.baidu.com/')
        self.input_data('id','kw',data)
        self.click('id','su')

if __name__ == '__main__':
    log = testDemo()
    log.function1('海贼王')