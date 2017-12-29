# -*- coding:utf-8 -*-
# file: Chinese.py
#
chinese = '''
在Python中使用中文
需要注意字符编码的问题
可以使用的字符编码有如下几种：
utf-8、cp936、gb2312、iso-8859-1。
'''
print chinese.decode('utf-8').encode('cp936')
