# -*- coding:utf-8 -*-
# file: PyGTKTextView.py
#
import pygtk											# 导入pygtk模块
pygtk.require('2.0')										# 设置pygtk所需的gtk版本
import gtk											# 导入gtk模块
class MyWindow():										# 定义窗口类
	def __init__(self, title, width, height):						# 定义初始化方法
		self.window = gtk.Window()							# 生成窗口对象
		self.window.set_title(title)							# 设置窗口标题
		self.window.set_default_size(width, height)					# 设置窗口大小
		self.window.connect('destroy', lambda q: gtk.main_quit())			# 关闭窗口时退出程序
		vbox = gtk.VBox(False, 5)							# 生成竖向Box对象
		swindow = gtk.ScrolledWindow()
		text = gtk.TextView()								# 创建多行文本框
		textbuffer = text.get_buffer()							# 文本框缓冲区
		swindow.add(text)
	        swindow.show()
		vbox.pack_start(swindow)							# 向Box对象中添加文本框
		text.show()									# 显示文本框
		self.window.add(vbox)								# 向窗口添加Box对象
		vbox.show()
		self.window.show()								# 显示窗口
	def main(self):										# 定义main方法
		gtk.main()									# 调用gtk.main方法
window = MyWindow('PyGTK', 300, 200)								# 创建窗口对象
window.main()
