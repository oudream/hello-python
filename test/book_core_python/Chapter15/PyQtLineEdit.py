# -*- coding:utf-8 -*-
# file: PyQtLineEdit.py
#
import sys
from PyQt4 import QtCore, QtGui	
class MyWindow(QtGui.QWidget):							# 通过继承QtGui.QWidget创建类
	def __init__(self):							# 初始化方法
		QtGui.QWidget.__init__(self)					# 调用父类初始化方法
		self.setWindowTitle('PyQt')					# 设置窗口标题
		self.resize(300,200)						# 设置窗口大小
		gridlayout = QtGui.QGridLayout()				# 创建布局组件
		label1 = QtGui.QLabel('Normal Lineedit')			# 创建标签
		label1.setAlignment(QtCore.Qt.AlignCenter)
		gridlayout.addWidget(label1, 0, 0 )
		edit1 = QtGui.QLineEdit()					# 创建单行文本框
		gridlayout.addWidget(edit1, 1, 0)
		label2 = QtGui.QLabel('Password')				# 创建标签
		label2.setAlignment(QtCore.Qt.AlignCenter)
		gridlayout.addWidget(label2, 2, 0)
		edit2 = QtGui.QLineEdit()					# 创建单行文本框
		edit2.setEchoMode(QtGui.QLineEdit.Password)			# 将其设置为密码框
		gridlayout.addWidget(edit2, 3, 0)
		self.setLayout(gridlayout)	
app = QtGui.QApplication(sys.argv)						# 创建QApplication对象
mywindow = MyWindow()								# 创建MyWindow对象
mywindow.show()									# 显示窗口
app.exec_()									# 进入消息循环
