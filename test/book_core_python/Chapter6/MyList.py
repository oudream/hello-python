# -*- coding:utf-8 -*-
# file: MyList.py
#
class MyList:									# 定义MyList类
	#__mylist = []									# 定义__mylist属性
	def __init__(self, *args):							# 重载__init__方法
		self.__mylist = []					# 此处相当于__mylist初始化，避免多个实例对象数据混合
		for arg in args:
			self.__mylist.append(arg)
	def __add__(self,n):								# 重载“+”运算符
		for i in range(0,len(self.__mylist)):
			self.__mylist[i] = self.__mylist[i] + n
	def __sub__(self,n):								# 重载“-”运算符
		for i in range(0,len(self.__mylist)):
			self.__mylist[i] = self.__mylist[i] - n
	def __mul__(self,n):								# 重载“*”运算符
		for i in range(0,len(self.__mylist)):
			self.__mylist[i] = self.__mylist[i] * n
	def __div__(self,n):								# 重载“/”运算符
		for i in range(0,len(self.__mylist)):
			self.__mylist[i] = self.__mylist[i] / n
	def __mod__(self,n):								# 重载“%”运算符
		for i in range(0,len(self.__mylist)):
			self.__mylist[i] = self.__mylist[i] % n
	def __pow__(self,n):								# 重载“**”运算符
		for i in range(0,len(self.__mylist)):
			self.__mylist[i] = self.__mylist[i] ** n
	def __len__(self):								# 重载len方法
		return len(self.__mylist)
	def show(self):									# 定义show方法
		print self.__mylist
		


