# -*- coding:utf-8 -*-
# file: PyQtLayout.py
#
import sys							# 导入sys模块
from PyQt4 import QtCore, QtGui					# 导入PyQt模块
class MyWindow(QtGui.QWidget):					# 通过继承QtGui.QWidget创建类
	def __init__(self):					# 初始化方法
		QtGui.QWidget.__init__(self)			# 调用父类初始化方法
		self.setWindowTitle('PyQt')			# 设置窗口标题
		self.resize(300,200)				# 设置窗口大小
		gridlayout = QtGui.QGridLayout()		# 创建布局组件
		hboxlayout1 = QtGui.QHBoxLayout()
		hboxlayout2 = QtGui.QHBoxLayout()
		vboxlayout1 = QtGui.QVBoxLayout()
		vboxlayout2 = QtGui.QVBoxLayout()
		label1 = QtGui.QLabel('Label1',self)		# 创建标签
		label1.setAlignment(QtCore.Qt.AlignCenter)
		label2 = QtGui.QLabel('Label2')
		label3 = QtGui.QLabel('Label3')
		label4 = QtGui.QLabel('Label4')
		label5 = QtGui.QLabel('Label5')
		hboxlayout1.addWidget(label1)			# 向布局组件中添加标签
		vboxlayout1.addWidget(label2)
		vboxlayout1.addWidget(label3)
		vboxlayout2.addWidget(label4)
		vboxlayout2.addWidget(label5)
		hboxlayout2.addLayout(vboxlayout1)		# 向hboxlayout2添加vboxlayout1
		hboxlayout2.addLayout(vboxlayout2)		# 向hboxlayout2添加vboxlayout2
		gridlayout.addLayout(hboxlayout1, 0 ,0)		# 向第一行第一列添加hboxlayout1
		gridlayout.addLayout(hboxlayout2, 1, 0)		# 向第二行第一列添加hboxlayout2
		gridlayout.setRowMinimumHeight (1, 180)		# 设置第二行的最小高度为108
		self.setLayout(gridlayout)
app = QtGui.QApplication(sys.argv)				# 创建QApplication对象
mywindow = MyWindow()						# 创建MyWindow对象
mywindow.show()							# 显示窗口
app.exec_()							# 进入消息循环
