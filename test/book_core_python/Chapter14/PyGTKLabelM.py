# -*- coding:utf-8 -*-
# file: PyGTKLabelM.py
#
import pygtk											# 导入pygtk模块
pygtk.require('2.0')										# 设置pygtk所需的gtk版本
import gtk											# 导入gtk模块
class MyWindow():										# 定义窗口类
	def __init__(self, title, width, height):						# 定义初始化方法
		self.window = gtk.Window()							# 生成窗口对象
		self.window.set_title(title)							# 设置窗口标题
		self.window.set_default_size(width, height)					# 设置窗口大小
		vbox = gtk.VBox(False, 5)							# 生成竖向Box对象
       		hbox1 = gtk.HBox(False, 5)							# 生成水平Box对象
		hbox2 = gtk.HBox(False, 5)
		label1 = gtk.Label('Label1')							# 创建标签
		label1.set_angle(90)								# 设置标签角度
		label2 = gtk.Label('Label2')
		label2.set_angle(270)
		label3 = gtk.Label('Label3')
		label4 = gtk.Label('Label4')
		label5 = gtk.Label('Label5')
		hbox1.pack_start(label1)							# 向Box对象中添加标签
		hbox1.pack_start(label2)
		hbox2.pack_start(label3)
		hbox2.pack_end(label4)
		hbox2.pack_end(label5)
		vbox.pack_start(hbox1)								# 向Box对象中添加其他Box对象
		vbox.pack_start(hbox2)
		self.window.add(vbox)								# 向窗口添加Box对象
		label1.show()									# 显示标签
		label2.show()
		label3.show()
		label4.show()
		label5.show()
		hbox1.show()									# 显示Box对象
		hbox2.show()
		vbox.show()
		self.window.show()								# 显示窗口
	def main(self):										# 定义main方法
		gtk.main()									# 调用gtk.main方法
window = MyWindow('PyGTK', 300, 200)								# 创建窗口对象
window.main()

