# -*- coding:utf-8 -*-
# file: pythonasp.py
#
# -*- coding:utf-8 -*-
# file: pythonasp.py
#
import os														# 导入os模块
def HttpStatus():												# 定义函数输入HTTP状态
	print
	print 'Status: 200 OK'
	print 'Content-type: text/html'
	print
HttpStatus()													# 调用函数
print '''
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>Python</title>
</head>
<body>
'''
print '<h1>Python路径</h1>'
i = 1
for path in os.sys.path:											# 使用os模块
	print i, ' ', path
	print '<br>'
	i = i + 1
print '''
</body>
</html>
'''

