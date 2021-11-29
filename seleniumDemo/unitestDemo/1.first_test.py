# 导入unittest模块
import unittest

# 继承TestCase类，TestCase类是测试用例类
class Test1(unittest.TestCase):
    def setUp(self):
        print('hello')

    def tearDown(self):
        print('bye')

    def test_001(self):
        print('001')

    def test_002(self):
        print('002')

    def test_003(self):
        print('003')

# class Test2(unittest.TestCase):
#
#     def test_001(self):
#         print('201')
#
#     def test_002(self):
#         print('202')

if __name__ == '__main__':
    # unittest.main()

    # 创建测试套件
    suit = unittest.TestSuite()
    # 定义一个测试用例列表
    case_list= ['test_001','test_003']
    for case in case_list:
        suit.addTest(Test1(case))

    # 运行测试用例，verbosity=2为每一个测试用例输出报告,run的参数是测试套件
    unittest.TextTestRunner(verbosity=2).run(suit)


# 1.unittest.main()运行时，框架自动寻找TestCase子类，并且运行
# 2.在TestCase类中，只把以test开头的方法当做测试用例，然后执行
# 3.setUp()用于初始化一些参数，在测试用例执行前自动被调用，tearDown()用于清理，在测试用例执行后被调用