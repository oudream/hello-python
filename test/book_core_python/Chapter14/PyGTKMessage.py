# -*- coding:utf-8 -*-
# file: PyGTKMessage.py
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
		self.label = gtk.Label('MessageDialog Example')					# 创建标签
		self.fixed.put(self.label, 80, 20)						# 添加标签
		self.button = gtk.Button('Create')						# 创建按钮
		self.button.connect('clicked',self.OnButton, 'Create')				# 绑定按钮事件
		self.fixed.put(self.button, 120, 150)						# 添加按钮
		self.window.add(self.fixed)							# 向窗口中添加Fixed
		self.label.show()								# 显示组件
		self.button.show()
		self.fixed.show()
		self.window.show()
	def OnButton(self, widget, data):
		msg = gtk.MessageDialog(self.window, 						# 创建消息框
				gtk.DIALOG_MODAL, 						# 消息框标志
				gtk.MESSAGE_INFO, 						# 消息框类型
				gtk.BUTTONS_OK, 						# 消息框按钮
				'An example')							# 消息框中的内容
        	msg.run()									# 显示消息框
       		msg.destroy()									# 销毁消息框
	def main(self):										# 定义main方法
		gtk.main()
window = MyWindow('PyGTK', 300, 200)								# 创建窗口对象
window.main()
