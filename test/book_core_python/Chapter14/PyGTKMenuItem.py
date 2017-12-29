# -*- coding:utf-8 -*-
# file: PyGTKMenuItem.py
#
import pygtk										# 导入pygtk模块
pygtk.require('2.0')									# 设置pygtk所需的gtk版本
import gtk										# 导入gtk模块
class MyWindow():									# 定义窗口类
	def __init__(self, title, width, height):					# 定义初始化方法
		window = gtk.Window()							# 生成窗口对象
		window.set_title(title)							# 设置窗口标题
		window.set_default_size(width, height)					# 设置窗口大小
		window.connect('destroy', lambda q: gtk.main_quit())			# 关闭窗口退出程序
		fixed = gtk.Fixed()							# 创建Fixed组件
		window.add(fixed)
		filemenu = gtk.Menu()							# 创建菜单
		open = gtk.MenuItem('Open')						# 创建Open菜单命令
		open.show()								# 显示Open
		close = gtk.MenuItem('Close')						# 创建Close菜单命令
		close.show()								# 显示Close
		filemenu.append(open)							# 向菜单中添加Open
		filemenu.append(close)							# 向菜单中添加Close
        	file = gtk.MenuItem('_File')						# 生成File菜单，下划线表示快捷键
		file.set_submenu(filemenu)						# 向File菜单添加项
        	file.show()								# 显示File菜单
		editmenu = gtk.Menu()							# 创建菜单
		copy = gtk.MenuItem('Copy')						# 创建Copy菜单命令
		copy.show()								# 显示Copy
		paste = gtk.MenuItem('Paste')						# 创建Paste菜单命令
		paste.show()								# 显示Paste
		editmenu.append(copy)							# 向菜单中添加Copy
		editmenu.append(paste)							# 向菜单中添加Paste
		edit = gtk.MenuItem('_Edit')						# 生成Edit菜单
		edit.set_submenu(editmenu)						# 向Edit菜单中添加项
		edit.show()								# 显示Edit菜单
        	menubar = gtk.MenuBar()							# 生成菜单条
		menubar.append(file)							# 向菜单条中添加File菜单
        	menubar.append(edit)							# 向菜单条中添加Edit菜单
		fixed.put(menubar, 0, 0)						# 向Fixed组件中添加菜单条
        	menubar.show()								# 显示个组件
		fixed.show()
		window.show()
	def main(self):									# 定义main方法
		gtk.main()
window = MyWindow('PyGTK', 300, 200)							# 创建窗口对象
window.main()
