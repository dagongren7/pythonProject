from seleniumDemo.four.DatabaseInit import DataBaseInit
import MySQLdb

class MyMySQL():
    def __init__(self,host,dbName,username,password,charset):
        dbInit = DataBaseInit(host,dbName,username,password,charset)
        dbInit.create()
        dbInit.insertDatas()
        
        self.conn = MySQLdb.connect(
                host='localhost',
                user='root',
                passwd='123456',
                db='test',
                charset= 'utf8'
                    )
        self.cur = self.conn.cursor()
        
    def getDataFromDataBases(self):
        self.conn.select_db("test")
        self.cur.execute("select bookname,author from testdata;")
        
        datasTuple = self.cur.fetchall()
        return datasTuple
    
    def closeDataBase(self):
        self.cur.close()
        self.conn.commit()
        self.conn.close()

if __name__ == '__main__':
    db = MyMySQL(
        host='localhost',
        username='root',
        password='123456',
        dbName='test',
        charset='utf8'
        )
    qq = db.getDataFromDataBases()
    print(qq)
    db.closeDataBase()