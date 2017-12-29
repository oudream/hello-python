# -*- coding:utf-8 -*-
# file: HelloPyQt.py
#
import sys							# 导入sys模块
from PyQt4 import QtCore, QtGui					# 导入PyQt模块
class MyWindow(QtGui.QMainWindow):				# 通过继承QtGui.QMainWindow创建类
	def __init__(self):					# 初始化方法
		QtGui.QMainWindow.__init__(self)		# 调用父类初始化方法
		self.setWindowTitle('PyQt')			# 设置窗口标题
		self.resize(300,200)				# 设置窗口大小
app = QtGui.QApplication(sys.argv)				# 创建QApplication对象
mywindow = MyWindow()						# 创建MyWindow对象
mywindow.show()							# 显示窗口
app.exec_()							# 进入消息循环
