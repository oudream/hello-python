# -*- coding:utf-8 -*-
# file: PyQtRes.py
#
import sys
from PyQt4 import QtCore, QtGui, uic	
class MyDialog(QtGui.QDialog):							# 继承QtGui.QDialog
    	def __init__(self):
		QtGui.QWidget.__init__(self)
        	uic.loadUi("res.ui", self)	

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
			self.button.setText(dialog.lineEdit.text())
app = QtGui.QApplication(sys.argv)
mywindow = MyWindow()
mywindow.show()
app.exec_()
