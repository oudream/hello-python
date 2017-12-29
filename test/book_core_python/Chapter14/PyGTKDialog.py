# -*- coding:utf-8 -*-
# file: PyGTKDialog.py
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
		self.label = gtk.Label('Dialog Example')					# 创建标签
		self.fixed.put(self.label, 80, 40)						# 添加标签
		self.button = gtk.Button('CreateDialog')					# 创建按钮
		self.button.connect('clicked',self.OnButton, 'CreateDialog')			# 绑定按钮事件
		self.fixed.put(self.button, 80, 130)						# 添加按钮
		self.window.add(self.fixed)							# 向窗口中添加Fixed
		self.label.show()								# 显示组件
		self.button.show()
		self.fixed.show()
		self.window.show()
	def OnButton(self, widget, data):							# 按钮事件处理函数
		dialog = gtk.Dialog('PyGTK', 							# 创建对话框
				None,								# 对话框父窗口
				gtk.DIALOG_MODAL,						# 对话框标志
                     		(gtk.STOCK_CANCEL, 						# 向对话框中添加Cancel按钮
				gtk.RESPONSE_CANCEL,						# Cancel按钮的返回值
                      		gtk.STOCK_OK, 							# 向对话框中添加Ok按钮
				gtk.RESPONSE_OK))						# Ok按钮的返回值
		fixed = gtk.Fixed()								# 创建Fixed组件
		dialog.vbox.pack_start(fixed)							# 向对话框中的vbox添加Fixed组件
		label = gtk.Label('Input')							# 创建标签
		fixed.put(label,10,5)								# 向Fixed组件中添加标签
		entry = gtk.Entry()								# 创建文本框
		fixed.put(entry,50,5)								# 向Fixed组件中添加文本框
		fixed.show()									# 显示个组件
		label.show()
		entry.show()
		r = dialog.run()								# 显示对话框并获取其返回值
		if r == gtk.RESPONSE_OK:							# 如果点击Ok按钮则输出文本框中的内容
			print entry.get_text()
		dialog.destroy()
	def main(self):										# 定义main方法
		gtk.main()
window = MyWindow('PyGTK', 300, 200)								# 创建窗口对象
window.main()
