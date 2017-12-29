# -*- coding:utf-8 -*-
# file : GetFunction.py
# 
import re
import sys
def DealWithFunc(s):
	r = re.compile(r'''
		(?<=def\s)	# 前边必须含有def且def后跟一个空格
		\w+		# 匹配函数明
		\(.*?\)		# 匹配参数
		(?=:)		# 后边必须跟一个“:”
		''',re.X)	# 设置编译选项，忽略模式中的注释
	return r.findall(s)
def DealWithVar(s):
	vars = []		# 定义一个列表，因为这里分两种情况处理
	r = re.compile(r'''
		\b		# 匹配单词开始
		\w+		# 匹配变量名
		(?=\s=)		# 处理为为变量赋值的情况
		''',re.X)
	vars.extend(r.findall(s))
	r = re.compile(r'''
		(?<=for\s)	# 处理变量位于for语句中的情况
		\w+		# 匹配变量名
		\s		# 匹配空格
		(?=in)		# 匹配in
		''',re.X)	# 设置编译选项，忽略模式中的注释
	vars.extend(r.findall(s))
	return vars
# 判断命令行是否有输入，没有则要求输入要处理的文件
if len(sys.argv) == 1:
	sour = raw_input('请输入要处理的文件路径')
else:
	sour = sys.argv[1]
file = open(sour)		# 打开文件
s = file.readlines()		# 将文件内容以行读入的s中
file.close()			# 关闭文件
print '********************************'
print sour,'中的函数有：'
print '********************************'
i = 0				# i为函数所在的行号
# 循环处理每一行，匹配其中的函数并输出函数所在的行号，以及函数的原型
for line in s:
	i = i + 1
	function = DealWithFunc(line)
	if len(function) == 1:
		print 'Line: ',i,'\t',function[0]
print '********************************'
print sour,'中的变量有：'
print '********************************'
i = 0				# 此处i为变量所在的行号
# 循环处理每一行，匹配其中的变量，输出变量所在的行号，以及变量名
for line in s:
	i = i + 1
	var = DealWithVar(line)
	if len(var) == 1:
		print 'Line: ',i,'\t',var[0]
