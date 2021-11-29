import ddt
import unittest
@ddt.ddt
class DoubanTest(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass
    @ddt.data([1,2,3,6],[2,3,4,5],[1,2,2,5])
    @ddt.unpack
    def test_add(self,testdata1,testdata2,testdate3,exceptdata):
        sum=0
        sum=testdata1+testdata2+testdate3
        self.assertEqual(sum,exceptdata)
if __name__ =='__main__':
    unittest.main()
