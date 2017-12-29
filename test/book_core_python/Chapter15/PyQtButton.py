# -*- coding:utf-8 -*-
# file: PyQtButton.py
#
import sys									# 导入sys模块
from PyQt4 import QtCore, QtGui							# 导入PyQt模块
class MyWindow(QtGui.QWidget):							# 通过继承QtGui.QWidget创建类
	def __init__(self):							# 初始化方法
		QtGui.QWidget.__init__(self)					# 调用父类初始化方法
		self.setWindowTitle('PyQt')					# 设置窗口标题
		self.resize(300,200)						# 设置窗口大小
		gridlayout = QtGui.QGridLayout()				# 创建布局组件
		button1 = QtGui.QPushButton('Button1')				# 生成Button1
		gridlayout.addWidget(button1, 1, 1, 1 ,3)			# 添加Button1
		button2 = QtGui.QPushButton('Button2')				# 生成Button2
		button2.setFlat(True)
		gridlayout.addWidget(button2, 2, 2)				# 添加Button2
		self.setLayout(gridlayout)					# 向窗口中添加布局组件
app = QtGui.QApplication(sys.argv)						# 创建QApplication对象
mywindow = MyWindow()								# 创建MyWindow对象
mywindow.show()									# 显示窗口
app.exec_()									# 进入消息循环
