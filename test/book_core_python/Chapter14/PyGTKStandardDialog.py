# -*- coding:utf-8 -*-
# file: PyGTKStandardDialog.py
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
		self.label1 = gtk.Label('StandardDialog Example')				# 创建标签
		self.fixed.put(self.label1, 80, 40)						# 添加标签
		self.button1 = gtk.Button('FileChooser')						# 创建按钮
		self.button1.connect('clicked',self.OnButton1, 'FileChooser')			# 绑定按钮事件
		self.button2 = gtk.Button('FontChooser')						# 创建按钮
		self.button2.connect('clicked',self.OnButton2, 'FontChooser')			# 绑定按钮事件
		self.button3 = gtk.Button('ColorChooser')						# 创建按钮
		self.button3.connect('clicked',self.OnButton3, 'ColorChooser')			# 绑定按钮事件
		self.fixed.put(self.button1, 10, 130)						# 添加按钮
		self.fixed.put(self.button2, 95, 130)						# 添加按钮
		self.fixed.put(self.button3, 190, 130)						# 添加按钮
		self.window.add(self.fixed)							# 向窗口中添加Fixed
		self.label1.show()								# 显示组件
		self.button1.show()
		self.button2.show()
		self.button3.show()
		self.fixed.show()
		self.window.show()
	def OnButton1(self, widget, data):							# 按钮事件处理函数
		dialog = gtk.FileChooserDialog('Open',						# 创建文件打开对话框
                               None,								# 设置父窗口
                               gtk.FILE_CHOOSER_ACTION_OPEN,					# 设置对话框标志
                               (gtk.STOCK_CANCEL, 						# 添加Cancel按钮
				gtk.RESPONSE_CANCEL,						# Cancel按钮的返回值
                                gtk.STOCK_OPEN, 						# 添加Open按钮
				gtk.RESPONSE_OK))						# Open按钮的返回值
		filter = gtk.FileFilter()							# 生成gtk.FileFilter对象
		filter.set_name('All files')							# 添加文件类型名
		filter.add_pattern('*')								# 即所有文件
		dialog.add_filter(filter)							# 向对话框中添加gtk.FileFilter对象
		filter = gtk.FileFilter()							# 生成gtk.FileFilter对象
		filter.set_name('Python')							# 添加文件类型名
		filter.add_pattern('*.py')							# 添加文件后缀名
		filter.add_pattern('*.pyw')							# 添加文件后缀名
		dialog.add_filter(filter)							# 向窗口中添加gtk.FileFilter对象
		r = dialog.run()								# 显示对话框
		if r == gtk.RESPONSE_OK:
			print dialog.get_filename()
		dialog.destroy()								# 销毁对话框
	def OnButton2(self, widget, data):							# 按钮事件处理函数
		fontdlg = gtk.FontSelectionDialog('Choose Font')				# 创建字体选中对话框
		r = fontdlg.run()								# 显示对话框
		if r == gtk.RESPONSE_OK:
			print fontdlg.get_font_name()
		fontdlg.destroy()								# 销毁对话框
	def OnButton3(self, widget, data):							# 按钮事件处理函数
            	colordlg = gtk.ColorSelectionDialog('Choose Color')				# 创建颜色选择对话框
		colordlg.colorsel.set_has_palette(True)						# 显示调色板
            	response = colordlg.run()							# 显示对话框
            	if response == gtk.RESPONSE_OK:
            	    print colordlg.colorsel.get_current_color()
            	colordlg.destroy()								# 销毁对话框
	def main(self):										# 定义main方法
		gtk.main()
window = MyWindow('PyGTK', 300, 200)								# 创建窗口对象
window.main()

