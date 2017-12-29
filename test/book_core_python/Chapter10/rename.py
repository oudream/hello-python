# -*- coding:utf-8 -*-
# file: rename.py
#
import os
perfix = 'Python'						# perfix 为重命名后的文件起始字符
length = 2 							# length 为除去perfix后，文件名要达到的长度
base = 1								# 文件名的起始数
format = 'mdb'							# 文件的后缀名
# 函数PadLeft将文件名补全到指定长度
# str 为要补全的字符
# num 为要达到的长度
# padstr 未达到长度所添加的字符
def PadLeft(str , num , padstr):
	stringlength = len (str)
	n = num - stringlength
	if n >=0 :
		str=padstr * n + str
	return str
# 为了避免误操作，这里先提示用户
print 'the files in %s will be renamed' % os.getcwd()
input = raw_input('press y to continue\n')		# 获取用户输入
if input != 'y':							# 判断用户输入，以决定是否执行重命名操作
	exit()
filenames = os.listdir(os.curdir)				# 获得当前目录中的内容
# 从基数减1，为了是下边 i = i + 1在第一次执行时等于基数
i = base - 1
for filename in filenames:					# 遍历目录中内容，进行重命名操作
	i = i+1
	# 判断当前路径是否为文件，并且不是“rename.py”
	if filename != "rename.py" and os.path.isfile(filename):
		name = str(i)					# 将i转换成字符
		name = PadLeft(name,length,'0')	# 将name补全到指定长度
		t = filename.split('.')				# 分割文件名，以检查其是否是所要修改的类型
		m = len(t)
		if format == '':					# 如果未指定文件类型，则更改当前目录中所有文件
			os.rename(filename,perfix+name+'.'+t[m-1])
		else:							# 否则只修改指定类型
			if t[m-1] == format:
				os.rename(filename,perfix+name+'.'+t[m-1])
			else:
				i = i - 1				# 保证i连续
	else:
		i = i - 1						# 保证i连续

