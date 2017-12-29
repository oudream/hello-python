# -*- coding:utf-8 -*-
# file: PyQtMessageBox.py
#
import sys
from PyQt4 import QtCore, QtGui	
class MyWindow(QtGui.QWidget):
	def __init__(self):							# 初始化方法
		QtGui.QWidget.__init__(self)					# 调用父类初始化方法
		self.setWindowTitle('PyQt')					# 设置窗口标题
		self.resize(300,200)						# 设置窗口大小
		gridlayout = QtGui.QGridLayout()				# 创建布局组件
		self.label = QtGui.QLabel('MessBox example')
		gridlayout.addWidget(self.label, 1, 3, 1, 3)
		self.button1 = QtGui.QPushButton('About')			# 生成Button1
		gridlayout.addWidget(self.button1, 2, 1)
		self.button2 = QtGui.QPushButton('AboutQt')			# 生成Button2
		gridlayout.addWidget(self.button2, 2, 2)
		self.button3 = QtGui.QPushButton('Critical')			# 生成Button2
		gridlayout.addWidget(self.button3, 2, 3)
		self.button4 = QtGui.QPushButton('Info')			# 生成Button2
		gridlayout.addWidget(self.button4, 2, 4)
		self.button5 = QtGui.QPushButton('Qusetion')			# 生成Button2
		gridlayout.addWidget(self.button5, 2, 5)
		self.button6 = QtGui.QPushButton('Warning')			# 生成Button2
		gridlayout.addWidget(self.button6, 2, 6)
		spacer = QtGui.QSpacerItem(200, 80)
		gridlayout.addItem(spacer, 3, 1, 1, 5)
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
		self.connect(self.button4, 					# Button4事件
				QtCore.SIGNAL('clicked()'), 
				self.OnButton4)
		self.connect(self.button5, 					# Button5事件
				QtCore.SIGNAL('clicked()'), 
				self.OnButton5)
		self.connect(self.button6, 					# Button6事件
				QtCore.SIGNAL('clicked()'),
				self.OnButton6)	
	def OnButton1(self):							# Button1插槽函数
		self.button1.setText('clicked')
		QtGui.QMessageBox.about(self, 'PyQt', 'About')			# 创建About消息框
	def OnButton2(self):							# Button2插槽函数
		self.button2.setText('clicked')
		QtGui.QMessageBox.aboutQt(self, 'PyQt')				# 创建AboutQt消息框
	def OnButton3(self):							# Button3插槽函数
		self.button3.setText('clicked')
        	r = QtGui.QMessageBox.critical(self, 'PyQt',			# 创建Ctitical消息框
				'Critical', 
				QtGui.QMessageBox.Abort,
				QtGui.QMessageBox.Retry,
				QtGui.QMessageBox.Ignore)
        	if r == QtGui.QMessageBox.Abort:
            		self.label.setText('Abort')
        	elif r == QtGui.QMessageBox.Retry:
           		self.label.setText('Retry')
        	else:
            		self.label.setText('Ignore')
	def OnButton4(self):							# Button4插槽函数
		self.button4.setText('clicked')
		QtGui.QMessageBox.information(self, 'PyQt', 'Information')	# 创建Information消息框
	def OnButton5(self):							# Button5插槽函数
		self.button5.setText('clicked')
        	r = QtGui.QMessageBox.question(self, 'PyQt',			# 创建Question消息框
				'Question', 
				QtGui.QMessageBox.Yes,
				QtGui.QMessageBox.No,
				QtGui.QMessageBox.Cancel)
	def OnButton6(self):							# Button6插槽函数
		self.button6.setText('clicked')
       		r = QtGui.QMessageBox.warning(self, 'PyQt',			# 创建Warning消息框
				'Warning', 
				QtGui.QMessageBox.Yes,
				QtGui.QMessageBox.No)
app = QtGui.QApplication(sys.argv)
mywindow = MyWindow()
mywindow.show()
app.exec_()

