# -*- coding:utf-8 -*-
# file: PyGTKRCbutton.py
#
import pygtk											# 导入pygtk模块
pygtk.require('2.0')										# 设置pygtk所需的gtk版本
import gtk											# 导入gtk模块
class MyWindow():										# 定义窗口类
	def __init__(self, title, width, height):						# 定义初始化方法
		self.window = gtk.Window()							# 生成窗口对象
		self.window.set_title(title)							# 设置窗口标题
		self.window.set_default_size(width, height)					# 设置窗口大小
		self.window.connect('destroy', lambda q: gtk.main_quit())
		self.fixed = gtk.Fixed()
		self.label1 = gtk.Label('PyGTK')						# 创建标签
		self.fixed.put(self.label1, 80, 20)						# 添加标签
		self.label2 = gtk.Label('PyGTK')
		self.fixed.put(self.label2, 160, 20)						# 添加单选框
		self.radio1 = gtk.RadioButton(None, 'Radio1')
		self.fixed.put(self.radio1, 50, 60)
		self.radio2 = gtk.RadioButton(self.radio1, 'Radio2')
		self.fixed.put(self.radio2, 50, 90)
		self.radio3 = gtk.RadioButton(self.radio1, 'Radio3')
		self.fixed.put(self.radio3, 50, 120)
		self.check = gtk.CheckButton('CheckButton')
		self.fixed.put(self.check, 150, 60)
		self.button = gtk.Button('Test')						# 创建按钮
		self.button.connect('clicked',self.OnButton, 'Test')				# 绑定按钮事件
		self.fixed.put(self.button, 120, 150)						# 添加按钮
		self.window.add(self.fixed)							# 向窗口中添加Fixed
		self.label1.show()								# 显示组件
		self.label2.show()
		self.radio1.show()
		self.radio2.show()
 		self.radio3.show()
		self.check.show()
		self.button.show()
		self.fixed.show()
		self.window.show()
	def OnButton(self, widget, data):
		if self.check.get_active():							# 判断复选框是否选中
			self.label2.set_text('checked')
		else:
			self.label2.set_text('uncheck')
		if self.radio1.get_active():							# 判断复选框选中状态
			self.label1.set_text('Radio1')
		elif self.radio2.get_active():
			self.label1.set_text('Radio2')
		else:
			self.label1.set_text('Radio3')
	def main(self):										# 定义main方法
		gtk.main()
window = MyWindow('PyGTK', 300, 200)								# 创建窗口对象
window.main()


