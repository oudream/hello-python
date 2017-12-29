# -*- coding:utf-8 -*-
# file: pyqueue.py
#
class PyQueue:									# 创建队
	def __init__(self, size = 20):
		self.queue = []							# 队
		self.size = size						# 队大小
		self.end = -1							# 队尾
	def setSize(self, size):						# 设置队大小
		self.size = size
	def In(self, element):							# 入队
		if self.end < self.size - 1:
			self.queue.append(element)
			self.end = self.end + 1
		else:
			raise 'PyQueueFull'					# 如果队满则引发异常
	def Out(self):								# 出队
		if self.end != -1:
			element = self.queue[0]
			self.queue = self.queue[1:]
			self.end = self.end - 1
			return element
		else:
			raise'PyQueueEmpty'					# 如果对为空则引发异常
	def End(self):								# 输出队尾
		return self.end
	def empty(self):							# 清楚队
		self.queue = []
		self.end = -1
if __name__ == '__main__':
	queue = PyQueue()
	for i in range(10):
		queue.In(i)							# 元素入队
	print queue.End()
	for i in range(10):
		print queue.Out()						# 元素出队
	for i in range(20):
		queue.In(i)							# 元素入队
	queue.empty()								# 清空队
	for i in range(20):
		print queue.Out()						# 此处将引发异常
