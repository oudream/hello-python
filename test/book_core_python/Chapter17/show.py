# -*- coding:utf-8 -*-
# file: PySqlite.py
#
import sqlite3											# 导入sqlite3模块
con = sqlite3.connect('message')						# 连接到数据库
cur = con.cursor()										# 获得数据库游标, 'GBK')
cur.execute('select * from message')								# 执行SQL语句
results = cur.fetchall()										# 获得数据
print
print 'Status: 200 OK'
print 'Content-type: text/html'
print
print '''
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>use Python in ASP</title>
</head>
<body>
<center>
<h1>所有留言</h1>
</center>
<hr />
'''
for result in results:
	print '姓名:', result[0].encode('UTF-8')
	print '<br>'
	print '时间:', result[4].encode('UTF-8')
	print '<br>'
	print '邮箱:', result[1].encode('UTF-8')
	print '<br>'
	print '网站', result[2].encode('UTF-8')
	print '<br>'
	print '留言内容:'
	print '<br>'
	print result[3].encode('UTF-8')
	print '<hr />'
print '''
</body>
</html>
'''
cur.close()											# 关闭游标
con.close()											# 关闭数据库连接
