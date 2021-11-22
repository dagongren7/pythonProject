import unittest,ddt
from count_db.TestData import Mysql_Data

def getTestData():
    db = Mysql_Data(
        host='localhost',
        dbName='qq123',
        username='root',
        passwd='1234',
        charset='utf8'
    )
    testdata = db.getData()
    return testdata

@ddt.ddt
class TestDemo(unittest.TestCase):
    @ddt.data( * getTestData())
    def test_one(self,data):
        print(data[0],data[1])

if __name__=='__main__':
    unittest.main()