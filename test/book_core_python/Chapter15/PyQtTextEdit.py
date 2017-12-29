# -*- coding:utf-8 -*-
# file: PyQtTextEdit.py
#
import sys
from PyQt4 import QtCore, QtGui	
class MyWindow(QtGui.QWidget):							# 通过继承QtGui.QWidget创建类
	def __init__(self):							# 初始化方法
		QtGui.QWidget.__init__(self)					# 调用父类初始化方法
		self.setWindowTitle('PyQt')					# 设置窗口标题
		self.resize(300,200)						# 设置窗口大小
		gridlayout = QtGui.QGridLayout()				# 创建布局组件
		label = QtGui.QLabel('TextEdit')				# 创建标签
		label.setAlignment(QtCore.Qt.AlignCenter)
		gridlayout.addWidget(label, 0, 0 )
		edit = QtGui.QTextEdit()					# 创建多行文本框
		edit.setText('Python\nPyQt')					# 设置文本框中的文字
		gridlayout.addWidget(edit, 1, 0)
		self.setLayout(gridlayout)	
app = QtGui.QApplication(sys.argv)						# 创建QApplication对象
mywindow = MyWindow()								# 创建MyWindow对象
mywindow.show()									# 显示窗口
app.exec_()									# 进入消息循环

