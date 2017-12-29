# -*- coding:utf-8 -*-
# file: PyGTKMenu.py
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
		menu_items = (								# 菜单
       			     ( '/_File',      None,         None, 0, '<Branch>' ),
       			     ( '/File/Open',  '<control>O', None, 0, None ),
       			     ( '/File/Save',  '<control>S', None, 0, None ),
       			     ( '/File/s',  None,         None, 0, '<Separator>' ),
       			     ( '/File/Close', '<control>Q', None, 0, None ),
       			     ( '/_Edit',      None,         None, 0, '<Branch>' ),
       			     ( '/Edit/Copy',  None,         None, 0, None ),
			     ( '/Edit/Paste',  None,         None, 0, None ),
			     ( '/Edit/s',  None,         None, 0, '<Separator>' ),
			     ( '/Edit/Cut',  None,         None, 0, None ),
       			     ( '/_Help',      None,         None, 0, '<Branch>' ),
       			     ( '/Help/About', None,         None, 0, None ),
       			     )
		accel_group = gtk.AccelGroup()						# 创建快捷键对象
		itemfactory = gtk.ItemFactory(gtk.MenuBar, '<main>', accel_group)	# 创建ItemFactory对象
        	itemfactory.create_items(menu_items)					# 从菜单元组创建菜单
        	window.add_accel_group(accel_group)					# 向窗口中添加快捷键
        	menubar = gtk.MenuBar()							# 生成菜单条
		menubar = itemfactory.get_widget('<main>')				# 获得菜单菜单
		fixed.put(menubar, 0, 0)						# 向Fixed组件中添加菜单条
        	menubar.show()								# 显示个组件
		fixed.show()
		window.show()
	def main(self):									# 定义main方法
		gtk.main()
window = MyWindow('PyGTK', 300, 200)							# 创建窗口对象
window.main()
