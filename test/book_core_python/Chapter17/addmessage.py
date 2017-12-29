# -*- coding:utf-8 -*-
# file: addmessage.py
#
import cgi
import sqlite3											# 导入sqlite3模块
import datetime
print
print 'Status: 200 OK'
print 'Content-type: text/html'
print
form = cgi.FieldStorage()
name = unicode(form["name"].value, 'GBK')
mail = unicode(form["email"].value, 'GBK')
site = unicode( form["site"].value, 'GBK')
content = unicode(form["content"].value, 'GBK')
now = datetime.datetime.now()
time = now.strftime('%Y-%m-%d %H:%M:%S')
con = sqlite3.connect('message')									# 连接到数据库
cur = con.cursor()										# 获得数据库游标
cur.execute("INSERT INTO message VALUES(?,?,?,?,?)", (name, mail, site, content, time))
con.commit()
# 执行SQL语句
cur.close()											# 关闭游标
con.close()
print '''
<html>
<head>
<title>添加成功</title>
</head>
<body>
<h1>添加成功</h1>
<br>
<a href=show.py>点击查看留言</a>
</body>
</html>
'''
