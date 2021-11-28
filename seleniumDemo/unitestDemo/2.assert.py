import unittest

class Test(unittest.TestCase):
    def setUp(self):
        print('start')

    def tearDown(self):
        print('bye')

    def test_001(self):
        self.assertEqual('1','1')

    def test_002(self):
        self.assertEqual('1','0')

if __name__ == '__main__':
    unittest.main()