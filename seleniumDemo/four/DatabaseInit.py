import pymysql
pymysql.install_as_MySQLdb()
import MySQLdb
MySQLdb.__version__
from seleniumDemo.four.SqlInit import SqlYju
'''
pip install pymysql -i http://pypi.douban.com/simple/ --trusted-host pypi.douban.com
pip install wheel==0.34.1 -i http://pypi.douban.com/simple/ --trusted-host pypi.douban.com
回退wheel版本查看支持
>>> import wheel.pep425tags as w
>>> print(w.get_supported("amd64"))
pip install mysqlclient-1.4.6-cp39-cp39-win32.whl
'''
class DataBaseInit():
    def __init__(self,host,dbName,username,password,charset):
        self.host = host
        self.db = dbName
        self.user = username
        self.passwd = password
        self.charset = charset

    def test(self):
        conn = MySQLdb.connect(host=self.host, user=self.user, passwd=self.passwd, db=self.db, charset=self.charset)
        conn.select_db("test")
        cur = conn.cursor()
        test = cur.execute("select * from user ")
        print(test)

    def create(self):
        try:
            conn = MySQLdb.connect(
                host = self.host,
                user = self.user,
                passwd = self.passwd,
                db=self.db,
                charset=self.charset
            )
            #获取数据库游标
            cur = conn.cursor()
            #选择test数据库
            
            conn.select_db("test")
            cur.execute(SqlYju.create_table)
        except Exception as e:
            print("数据表创建错误！")
        else:
            cur.close()#关闭游标
            conn.commit()#关闭操作
            conn.close()#关闭连接
            print("创建数据表成功")
    
    def insertDatas(self):
        try:
            conn = MySQLdb.connect(
                host=self.host,
                user=self.user,
                passwd=self.passwd,
                db=self.db,
                charset=self.charset
            )
            cur = conn.cursor()
            conn.select_db("test")
            cur.execute(SqlYju.insert_table)
        except Exception as e:
            print("插入数据出错！")
        else:
            conn.commit()
            print("初始化数据成功")
            cur.execute("select * from testdata;")
            cur.close()
            conn.close()

if __name__ == '__main__':
    db = DataBaseInit(
        host = "localhost",
        dbName = "test",
        username = "root",
        password = "123456",
        charset = 'utf8'
        )
    db.test()

    # db.create()
    # db.insertDatas()
    # print("数据库初始化结束")
    pass