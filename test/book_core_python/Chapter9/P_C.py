# -*- coding:utf-8 -*-
# file: P_C.py
#
import threading							# 导入threading模块
class Producer(threading.Thread):					# 定义生产者类
	def __init__(self,threadname):
		threading.Thread.__init__(self,name = threadname)
	def run(self):
		global x
		con.acquire()						# 调用con的acquire方法				
		if x == 1000000:
			con.wait()					# 调用con的wait方法
			pass
		else:
			for i in range(1000000):
				x = x + 1
			con.notify()					# 调用con的notify方法
		print x
		con.release()						# 调用con的release方法
class Consumer(threading.Thread):					# 定义生产者类
	def __init__(self,threadname):
		threading.Thread.__init__(self,name = threadname)
	def run(self):
		global x
		con.acquire()
		if x == 0:
			con.wait()	
			pass
		else:
			for i in range(1000000):
				x = x - 1
			con.notify()
		print x
		con.release()
con = threading.Condition()						# 类实例化
x=0
p = Producer('Producer')						# 生成生产者对象
c = Consumer('Consumer')						# 生成消费者对象
p.start()								# 运行线程
c.start()
p.join()								# 等待线程结束
c.join()
print x
