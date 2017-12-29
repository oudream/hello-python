<%@LANGUAGE=Python%>
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>use Python in ASP</title>
</head>
<body>
<h1>use Python in ASP</h1>
<%
import os								# 导入os模块
import string								# 导入string模块
class Info:								# 定义类
	def __init__(self):
		Response.Write('<h1>Python Class </h1>')
	def show(self):
		Response.Write('<h1>Class Info</h1>')
def print_br():								# 定义函数
	Response.Write('<br>')
def print_h1(s):
	Response.Write('<h1>')
	Response.Write(s)
	Response.Write('</h1>')
print_h1(u'使用os模块')							# 调用函数，使用u表示为unicode
for path in os.sys.path:						# 使用os模块
	Response.Write(path)
	print_br()
print_h1(u'使用string模块')
for s in string.split('Python is great'):				# 使用string模块
	Response.Write(s)
	print_br()
print_h1(u'使用类')
info = Info()								# 类实例化
info.show()								# 调用类方法
%>
</body>
</html>
