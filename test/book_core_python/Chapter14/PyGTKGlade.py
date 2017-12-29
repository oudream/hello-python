# -*- coding:utf-8 -*-
# file: PyGTKGlade.py
#
import pygtk
pygtk.require('2.0')
import gtk
import gtk.glade
class MyWindow():							# 定义窗口类
	def __init__(self):						# 定义初始化方法
	        res = gtk.glade.XML('res.glade') 			# 载入资源文件，生成gtk.glade.XML实例对象
		window = res.get_widget('window')			# 载入window
		signal = { 'OnQuit' : self.OnQuit }			# 创建信号字典
		res.signal_autoconnect(signal)				# 绑定信号事件
		window.connect('destroy', lambda q:gtk.main_quit())	# 窗口关闭则退出程序
		window.show()
	def OnQuit(self, widget):					# Quit菜单命令处理事件
		gtk.main_quit()
	def main(self):							# 定义main方法
		gtk.main()						# 调用gtk.main方法
window = MyWindow()							# 创建窗口对象
window.main()			
