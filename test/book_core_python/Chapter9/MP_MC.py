# -*- coding:utf-8 -*-
# file: MP_MC.py
#
import threading		# 导入threading模块
import time			# 导入time模块
import Queue			# 导入Queue模块
class Producer(threading.Thread):# 定义生产者类
	def __init__(self,threadname):
		threading.Thread.__init__(self,name = threadname)
	def run(self):
		global queue	# 声明queue为全局变量
		queue.put(self.getName())	# 调用put方法将线程名添加到队列中
		print self.getName(),'put ',self.getName(),' to queue'
class Consumer(threading.Thread):# 定义消费者类
	def __init__(self,threadname):
		threading.Thread.__init__(self,name = threadname)
	def run(self):
		global queue
		print self.getName(),'get ',queue.get(),'from queue'#调用get方法获取队列中内容
queue = Queue.Queue()	# 生成队列对象
plist = []		# 生成者对象列表
clist = []		# 消费者对象列表
for i in range(10):
	p = Producer('Producer' + str(i))
	plist.append(p)		# 添加到生产者对象列表
for i in range(10):
	c = Consumer('Consumer' + str(i))
	clist.append(c)		# 添加到消费者对象列表
for i in plist:
	i.start()		# 运行生产者线程
	i.join()
for i in clist:
	i.start()		# 运行消费者线程
	i.join()

