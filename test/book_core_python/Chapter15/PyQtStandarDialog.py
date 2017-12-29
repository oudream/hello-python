# -*- coding:utf-8 -*-
# file: PyQtStandarDialog.py
#
import sys
from PyQt4 import QtCore, QtGui	
class MyWindow(QtGui.QWidget):
	def __init__(self):							# 初始化方法
		QtGui.QWidget.__init__(self)					# 调用父类初始化方法
		self.setWindowTitle('PyQt')					# 设置窗口标题
		self.resize(300,200)						# 设置窗口大小
		gridlayout = QtGui.QGridLayout()				# 创建布局组件
		self.label = QtGui.QLabel('StandarDialog example')
		gridlayout.addWidget(self.label, 1, 2)
		self.button1 = QtGui.QPushButton('File')			# 生成Button1
		gridlayout.addWidget(self.button1, 2, 1)
		self.button2 = QtGui.QPushButton('Font')			# 生成Button2
		gridlayout.addWidget(self.button2, 2, 2)
		self.button3 = QtGui.QPushButton('Color')			# 生成Button2
		gridlayout.addWidget(self.button3, 2, 3)
		spacer = QtGui.QSpacerItem(200, 80)
		gridlayout.addItem(spacer, 3, 1, 1, 3)
		self.setLayout(gridlayout)					# 向窗口中添加布局组件
		self.connect(self.button1, 					# Button1事件
				QtCore.SIGNAL('clicked()'),
				self.OnButton1)
		self.connect(self.button2, 					# Button2事件
				QtCore.SIGNAL('clicked()'),
				self.OnButton2)
		self.connect(self.button3, 					# Button3事件
				QtCore.SIGNAL('clicked()'),
				self.OnButton3)
	def OnButton1(self):			
		self.button1.setText('clicked')
		filename = QtGui.QFileDialog.getOpenFileName(self, 'Open')	# 创建文件打开对话框
        	if not filename.isEmpty():
            		self.label.setText(filename)
	def OnButton2(self):							# Button2插槽函数
		self.button2.setText('clicked')
		font, ok = QtGui.QFontDialog.getFont()				# 创建字体选中对话框
		if ok:
			self.label.setText(font.key())
	def OnButton3(self):							# Button3插槽函数
		self.button3.setText('clicked')
		color = QtGui.QColorDialog.getColor()				# 创建颜色选择对话框
		if color.isValid(): 
			self.label.setText(color.name())
app = QtGui.QApplication(sys.argv)
mywindow = MyWindow()
mywindow.show()
app.exec_()
