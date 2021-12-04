import unittest

suite = unittest.defaultTestLoader.discover('./../case_manage',pattern='test_baidu_*.py')


if __name__ == '__main__':
   unittest.TextTestRunner(verbosity=2).run(suite)
