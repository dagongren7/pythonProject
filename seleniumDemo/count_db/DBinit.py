import MySQLdb
from count_db.Sql import Sqlyu

class DB_init():
    def __init__(self,host,dbName,username,passwd,charset):
        self.host = host
        self.db = dbName
        self.user = username
        self.pw = passwd
        self.charset = charset

    def create(self):
        try:
            conn = MySQLdb.connect(host=self.host,
                                   user=self.user,
                                   passwd=self.pw,
                                   db=self.db,
                                   charset=self.charset)
            conn.select_db("qq123")
            cur = conn.cursor()
            cur.execute(Sqlyu.create_table)
        except Exception as e:
            print('数据表创建失败')
        else:
            cur.close()
            conn.commit()
            conn.close()
            print('数据表创建成功')

    def insertDB(self):
        try:
            conn = MySQLdb.connect(host=self.host,
                                   user=self.user,
                                   passwd=self.pw,
                                   db=self.db,
                                   charset=self.charset)
            conn.select_db("qq123")
            cur = conn.cursor()
            cur.execute(Sqlyu.insert_table)
        except Exception as e:
            print('数据插入失败')
        else:
            cur.close()
            conn.commit()
            conn.close()
            print('数据插入成功')


if __name__=='__main__':
    db = DB_init(
        host='localhost',
        dbName='qq123',
        username='root',
        passwd='1234',
        charset='utf8'
    )
    db.create()
    db.insertDB()
    print('数据库初始化完成')