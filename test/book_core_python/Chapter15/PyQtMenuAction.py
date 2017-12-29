# -*- coding:utf-8 -*-
# self.file: PyQtMenuAction.py
#
import sys
from PyQt4 import QtCore, QtGui	
class MyWindow(QtGui.QMainWindow):							# 通过继承QtGui.QMainWindow创建类
	def __init__(self):								# 初始化方法
		QtGui.QMainWindow.__init__(self)					# 调用父类初始化方法
		self.setWindowTitle('PyQt')						# 设置窗口标题
		self.resize(300,200)							# 设置窗口大小
		self.label = QtGui.QLabel('Menu Action')				# 创建标签
		self.label.setAlignment(QtCore.Qt.AlignCenter)				# 设置标签文字对齐样式
		self.setCentralWidget(self.label)
		menubar = self.menuBar()						# 获得窗口的菜单条
		self.file = menubar.addMenu('&File')					# 添加File菜单
		open = self.file.addAction('Open')					# 添加Open命令
		self.connect(open, QtCore.SIGNAL('triggered()'), self.OnOpen)		# 菜单信号
		save = self.file.addAction('Save')					# 添加Save命令
		self.connect(save, QtCore.SIGNAL('triggered()'), self.OnSave)		# 菜单信号
		self.file.addSeparator()						# 添加分隔符
		close = self.file.addAction('Close')					# 添加Close命令
		self.connect(close, QtCore.SIGNAL('triggered()'), self.OnClose)		# 菜单信号
	def OnOpen(self):								# 处理Open命令
		self.label.setText('Menu Action: Open')
	def OnSave(self):								# 处理Save命令
		self.label.setText('Menu Action: Save')
	def OnClose(self):								# 处理Close命令
		self.close()
	def contextMenuEvent(self, event):						# 重载弹出式菜单事件
        	self.file.exec_(event.globalPos())
app = QtGui.QApplication(sys.argv)							# 创建QApplication对象
mywindow = MyWindow()									# 创建MyWindow对象
mywindow.show()										# 显示窗口
app.exec_()										# 进入消息循环
