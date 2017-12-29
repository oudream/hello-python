# -*- coding:utf-8 -*-
# file: event.py
#
import threading			# 导入threading模块
class mythread(threading.Thread):
	def __init__(self,threadname):
		threading.Thread.__init__(self,name = threadname)
	def run(self):
		global event		# 使用全局Event对象
		if event.isSet():	# 判断Event对象内部信号标志
			event.clear()	# 若已设置标志则清除
			event.wait()	# 调用wait方法
			print self.getName()
		else:
			print self.getName()
			event.set()	# 设置Event对象内部信号标志
event = threading.Event()		# 生成Event对象
event.set()				# 设置Event对象内部信号标志
tl = []
for i in range(10):
	t = mythread(str(i))
	tl.append(t)			# 生成线程列表
	
for i in tl:
	i.start()			# 运行线程
