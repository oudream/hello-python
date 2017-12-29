# -*- coding:utf-8 -*-
# file: PyQtMenu.py
#
import sys
from PyQt4 import QtCore, QtGui	
class MyWindow(QtGui.QMainWindow):						# 通过继承QtGui.QMainWindow创建类
	def __init__(self):							# 初始化方法
		QtGui.QMainWindow.__init__(self)				# 调用父类初始化方法
		self.setWindowTitle('PyQt')					# 设置窗口标题
		self.resize(300,200)						# 设置窗口大小
		menubar = self.menuBar()					# 获得窗口的菜单条
		file = menubar.addMenu('&File')					# 添加File菜单
		file.addAction('Open')						# 添加Open命令
		file.addAction('Save')						# 添加Save命令
		file.addSeparator()						# 添加分隔符
		file.addAction('Close')						# 添加Close命令
		edit = menubar.addMenu('&Edit')					# 添加Edit菜单
		edit.addAction('Copy')						# 添加Copy命令
		edit.addAction('Paste')						# 添加Paste命令
		edit.addAction('Cut')						# 添加Cut命令
		edit.addAction('SelectAll')					# 添加SelectAll命令
		help = menubar.addMenu('&Help')					# 添加Help菜单
		help.addAction('About')						# 添加About命令
app = QtGui.QApplication(sys.argv)						# 创建QApplication对象
mywindow = MyWindow()								# 创建MyWindow对象
mywindow.show()									# 显示窗口
app.exec_()									# 进入消息循环
