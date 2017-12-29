# -*- coding:utf-8 -*-
# file: PyGTKButtonEvent.py
#
import pygtk											# 导入pygtk模块
pygtk.require('2.0')										# 设置pygtk所需的gtk版本
import gtk											# 导入gtk模块
class MyWindow():										# 定义窗口类
	def __init__(self, title, width, height):						# 定义初始化方法
		self.window = gtk.Window()							# 生成窗口对象
		self.window.set_title(title)							# 设置窗口标题
		self.window.set_default_size(width, height)					# 设置窗口大小
		self.window.connect('destroy', lambda w: gtk.main_quit())			# 关闭窗口时退出程序
       		hbox = gtk.HBox(False, 20)							# 生成水平Box对象
		self.button1 = gtk.Button('Button1')						# 创建按钮
		self.button2 = gtk.Button('Button2')
		self.button1.connect('clicked', self.OnButton1, 'Button1')			# 绑定按钮事件
		self.button2.connect('clicked', self.OnButton2, 'Button2')
		hbox.pack_start(self.button1)							# 向Box对象中添加按钮
		hbox.pack_start(self.button2)
		self.window.add(hbox)								# 向窗口添加Box对象
		hbox.show()									# 显示Box对象
		self.button1.show()								# 显示按钮
		self.button2.show()
		self.window.show()								# 显示窗口
	def main(self):										# 定义main方法
		gtk.main()									# 调用gtk.main方法
	def OnButton1(self,widget, data):							# 处理按钮事件
		self.button2.set_label('Quit')							# 重新设置Button2文本
	def OnButton2(self, widgte, data):							# 处理按钮事件
		gtk.main_quit()									# 退出程序
window = MyWindow('PyGTK', 150, 30)								# 创建窗口对象
window.main()
