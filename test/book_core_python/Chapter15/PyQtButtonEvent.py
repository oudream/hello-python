# -*- coding:utf-8 -*-
# file: PyQtButtonEvent.py
#
import sys
from PyQt4 import QtCore, QtGui	
class MyWindow(QtGui.QWidget):
	def __init__(self):							# 初始化方法
		QtGui.QWidget.__init__(self)					# 调用父类初始化方法
		self.setWindowTitle('PyQt')					# 设置窗口标题
		self.resize(300,200)						# 设置窗口大小
		gridlayout = QtGui.QGridLayout()				# 创建布局组件
		self.button1 = QtGui.QPushButton('Button1')			# 生成Button1
		gridlayout.addWidget(self.button1, 1, 1, 1 ,3)
		self.button2 = QtGui.QPushButton('Button2')			# 生成Button2
		gridlayout.addWidget(self.button2, 2, 2)
		self.setLayout(gridlayout)					# 向窗口中添加布局组件
		self.connect(self.button1, 					# Button1事件
				QtCore.SIGNAL('clicked()'), 			# clicked()信号
				self.OnButton1)					# 插槽函数
		self.connect(self.button2, 					# Button2事件
				QtCore.SIGNAL('clicked()'), 			# clicked()信号
				self.OnButton2)					# 插槽函数
	def OnButton1(self):							# Button1插槽函数
		self.button1.setText('clicked')
	def OnButton2(self):							# Button2插槽函数
		self.button2.setText('clicked')
app = QtGui.QApplication(sys.argv)
mywindow = MyWindow()		
mywindow.show()		
app.exec_()	
