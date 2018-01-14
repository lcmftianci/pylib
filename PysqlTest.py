# This Python file uses the following encoding: utf-8
# python操作MySQL数据库测试代码
import time, MySQLdb, sys

print "HelloWorld"

# 连接
conn = MySQLdb.connect(host="localhost", user="root", passwd="123456", db="nbcast", charset="utf8")
cursor = conn.cursor()
print "连接成功"

# #增
sql = "insert into userinfo (username, pswd) values (%s, %s)"
param = ("哈哈", "ha11")
n = cursor.execute(sql, param)
print n
conn.commit()



# #更新
# sql = "update userinfo set pswd = %s where username = %s"
# param = ("999999999999", "张三")
# cursor.execute(sql, param)

# 删
# sql = "delete from userinfo where username = %s"
# param = ("张三")
# n = cursor.execute(sql, param)
# print n
# conn.commit()

# 查
sql = "select * from userinfo "
n = cursor.execute(sql)
for rows in cursor.fetchall():
    for cols in rows:
        print cols,
print ""

# 关闭指针对象和连接
cursor.close()
conn.close()