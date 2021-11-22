from count_db.DBinit import DB_init
import MySQLdb

class Mysql_Data():
    def __init__(self,host,dbName,username,passwd,charset):
        self.host = host
        self.db = dbName
        self.user = username
        self.pw = passwd
        self.charset = charset
        dbinit = DB_init(host,dbName,username,passwd,charset)
        dbinit.create()
        dbinit.insertDB()
        print('数据库初始化完成')
        self.conn = MySQLdb.connect(host=self.host,
                               user=self.user,
                               passwd=self.pw,
                               db=self.db,
                               charset=self.charset)
        self.cur = self.conn.cursor()

    def getData(self):
        self.conn.select_db(self.db)
        self.cur.execute("select can,yu from stu")
        data = self.cur.fetchall()
        self.closeDB()
        return data

    def closeDB(self):
        self.cur.close()
        self.conn.commit()
        self.conn.close()

if __name__=='__main__':
    db = Mysql_Data(
        host='localhost',
        dbName='qq123',
        username='root',
        passwd='1234',
        charset='utf8'
    )
    print(db.getData())