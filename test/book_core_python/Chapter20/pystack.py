# -*- coding:utf-8 -*-
# file: pystack.py
#
class PyStack:									# 堆栈类
	def __init__(self, size = 20):
		self.stack = []							# 堆栈列表
		self.size = size						# 堆栈大小
		self.top = -1							# 栈顶位置
	def setSize(self, size):						# 设置堆栈大小
		self.size = size
	def push(self, element):						# 元素进栈
		if self.isFull():
			raise 'PyStackOverflow'					# 如果栈满则引发异常
		else:
			self.stack.append(element)
			self.top = self.top + 1
	def pop(self):								# 元素出栈
		if self.isEmpty():
			raise 'PyStackUnderflow'				# 如果栈为空则引发异常
		else:
			element = self.stack[-1]
			self.top = self.top - 1
			del self.stack[-1]
			return element
	def Top(self):								# 获取栈顶位置
		return self.top
	def empty(self):							# 清空栈
		self.stack = []
		self.top = -1
	def isEmpty(self):							# 是否为空栈
		if self.top == -1:
			return True
		else:
			return False
	def isFull(self):							# 是否为满栈
		if self.top == self.size - 1:
			return True
		else:
			return False
if __name__ == '__main__':
	stack = PyStack()							# 创建栈
	for i in range(10):
		stack.push(i)							# 元素进栈
	print stack.Top()							# 输出栈顶位置
	for i in range(10):
		print stack.pop()						# 元素出栈
	stack.empty()								# 清空栈
	for i in range(20):
		stack.push(i)							# 此处将引发异常
