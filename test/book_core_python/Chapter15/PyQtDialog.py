# -*- coding:utf-8 -*-
# file: PyQtDialog.py
#
import sys
from PyQt4 import QtCore, QtGui	
class MyDialog(QtGui.QDialog):							# 继承QtGui.QDialog
    	def __init__(self):
        	QtGui.QDialog.__init__(self)
		self.gridlayout = QtGui.QGridLayout()				# 创建布局组件
		self.label = QtGui.QLabel('Input:')				# 创建标签
		self.gridlayout.addWidget(self.label, 0, 0)
		self.edit = QtGui.QLineEdit()					# 创建单行文本框
		self.gridlayout.addWidget(self.edit, 0, 1)
		self.ok = QtGui.QPushButton('Ok')				# 创建Ok按钮
		self.gridlayout.addWidget(self.ok, 1, 0)
		self.cancel = QtGui.QPushButton('Cancel')			# 创建Cancel按钮
		self.gridlayout.addWidget(self.cancel, 1, 1)
		self.setLayout(self.gridlayout)
		self.connect(self.ok, 						# Ok按钮事件
				QtCore.SIGNAL('clicked()'),
				self.OnOk)		
		self.connect(self.cancel, 					# Cancel按钮事件
				QtCore.SIGNAL('clicked()'),
				self.OnCancel)		
	def OnOk(self):								# 处理Ok按钮事件
		self.text = self.edit.text()					# 获取文本框中内容
		self.done(1)							# 结束对话框返回1
	def OnCancel(self):							# 处理Cancel按钮事件
		self.done(0)							# 结束对话框返回0
class MyWindow(QtGui.QWidget):
	def __init__(self):							# 初始化方法
		QtGui.QWidget.__init__(self)					# 调用父类初始化方法
		self.setWindowTitle('PyQt')					# 设置窗口标题
		self.resize(300,200)						# 设置窗口大小
		gridlayout = QtGui.QGridLayout()				# 创建布局组件
		self.button = QtGui.QPushButton('CreateDialog')			# 生成Button1
		gridlayout.addWidget(self.button, 1, 1)
		self.setLayout(gridlayout)					# 向窗口中添加布局组件
		self.connect(self.button, 					# Button事件
				QtCore.SIGNAL('clicked()'),
				self.OnButton)
	def OnButton(self):							# 处理按钮事件		
		dialog = MyDialog()						# 创建对话框对象
		r = dialog.exec_()						# 运行对话框
		if r:
			self.button.setText(dialog.text)
app = QtGui.QApplication(sys.argv)
mywindow = MyWindow()
mywindow.show()
app.exec_()

