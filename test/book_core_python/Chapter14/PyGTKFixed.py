# -*- coding:utf-8 -*-
# file: PyGTKFixed.py
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
		self.label = gtk.Label('PyGTK')							# 创建标签
		self.fixed.put(self.label,10,5)							# 添加标签
		self.button = gtk.Button('Move')						# 创建按钮
		self.button.connect('clicked',self.OnButton, 'Move')				# 绑定按钮事件
		self.fixed.put(self.button, 120, 150)						# 添加按钮
		self.window.add(self.fixed)							# 向窗口中添加Fixed
		self.label.show()								# 显示标签
		self.button.show()								# 显示按钮
		self.fixed.show()								# 显示Fixed组件
		self.window.show()								# 显示窗口
	def OnButton(self, widget, data):
		self.fixed.move(self.label, 100,50)
	def main(self):										# 定义main方法
		gtk.main()
window = MyWindow('PyGTK', 300, 200)								# 创建窗口对象
window.main()

