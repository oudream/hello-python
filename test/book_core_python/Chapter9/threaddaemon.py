# -*- coding:utf-8 -*-
# file: threaddaemon.py
# 
import threading							# 导入threading模块
import time								# 导入time模块
class mythread(threading.Thread):					# 通过继承创建类
	def __init__(self,threadname):					# 初始化方法
		threading.Thread.__init__(self,name = threadname)	# 调用父类的初始化方法
	def run(self):							# 重载run方法
		time.sleep(5)						# 调用time模块中的sleep函数，让线程休眠5秒	
		print self.getName()
def func1():								# 定义函数func1
	t1.start()						
	print 'func1 done'
def func2():								# 定义函数func2
	t2.start()
	print 'func2 done'
t1 = mythread('t1')							# 类实例化
t2 = mythread('t2')							# 类实例化
t2.setDaemon(True)							# 设置t2的Daemon标志
func1()									# 调用函数func1
func2()									# 调用函数func2

