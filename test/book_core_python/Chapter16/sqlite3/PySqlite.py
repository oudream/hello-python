# -*- coding:utf-8 -*-
# file: PySqlite.py
#
import sqlite3											# 导入sqlite3模块
con = sqlite3.connect('python')									# 连接到数据库
cur = con.cursor()										# 获得数据库游标
cur.execute('insert into people (name,age,sex) values (\'Jee\',21,\'F\')')			# 执行SQL语句
r = cur.execute('delete from people where age=20')						# 执行SQL语句
con.commit()											# 提交事务
cur.execute('select * from people')								# 执行SQL语句
s = cur.fetchall()										# 获得数据
print s												# 打印数据
cur.close()											# 关闭游标
con.close()											# 关闭数据库连接
