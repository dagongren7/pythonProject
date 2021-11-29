import pymysql
pymysql.install_as_MySQLdb()
import MySQLdb
MySQLdb.__version__
conn = MySQLdb.connect(host="localhost",user="root",passwd="123456",db="test",charset="utf8")
conn.select_db("test")
cur = conn.cursor()
test = cur.execute("select * from user ")
print(test)
