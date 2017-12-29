# -*- coding:utf-8 -*-
# file: UseMenu.py
#
import win32ui
import win32api
from win32con import *
from pywin.mfc import window
# 定义窗口类
class MyWnd(window.Wnd):
	def __init__ (self):
		window.Wnd.__init__(self, win32ui.CreateWnd ())
	 	self._obj_.CreateWindowEx(WS_EX_CLIENTEDGE, \
           		win32ui.RegisterWndClass(0, 0, COLOR_WINDOW + 1), \
            		'MFC GUI', WS_OVERLAPPEDWINDOW, \
            		(10, 10, 800, 500), None, 0, None)
		# 创建菜单对象
		submenu = win32ui.CreateMenu()
		menu = win32ui.CreateMenu()
		# 向菜单中添加Open，其中&表示可以使用Alt+&后的字母访问该菜单命令
		submenu.AppendMenu(MF_STRING,1051,'&Open')	
		# 向菜单中添加Close
		submenu.AppendMenu(MF_STRING,1052,'&Close')	
		# 向菜单中添加Save
		submenu.AppendMenu(MF_STRING,1053,'&Save')
		# 将上面的菜单添加到File菜单中
		menu.AppendMenu(MF_STRING|MF_POPUP,submenu.GetHandle(),'&File')
		submenu = win32ui.CreateMenu()
		# 向菜单中添加Copy
		submenu.AppendMenu(MF_STRING,1054,'&Copy')
		# 向菜单中添加Paste
		submenu.AppendMenu(MF_STRING,1055,'&Paste')	
		# 向菜单中添加分隔符
		submenu.AppendMenu(MF_SEPARATOR,1056,None)
		# 向菜单中添加Cut
		submenu.AppendMenu(MF_STRING,1057,'C&ut')
		# 将上面的菜单添加到Edit菜单中
		menu.AppendMenu(MF_STRING|MF_POPUP,submenu.GetHandle(),'&Edit')
		submenu = win32ui.CreateMenu()
		# 向菜单中添加Tools
		submenu.AppendMenu(MF_STRING,1058,'Tools')
		# 向菜单中添加Settings
		submenu.AppendMenu(MF_STRING|MF_GRAYED,1059,'Setting')
		m = win32ui.CreateMenu()
		# 将上面的菜单添加到Option菜单中
		m.AppendMenu(MF_STRING|MF_POPUP|MF_CHECKED,submenu.GetHandle(),'Option')
		# 将Option菜单添加到Other菜单中
		menu.AppendMenu(MF_STRING|MF_POPUP,m.GetHandle(),'&Other')
		# 将菜单添加到窗口中
		self._obj_.SetMenu(menu)
	# 重载OnClose方法
	def OnClose(self):
		self.EndModalLoop(0)
w = MyWnd()											# 生成窗口对象
w.ShowWindow()											# 显示窗口
w.UpdateWindow()										# 刷新窗口
w.RunModalLoop(1)										# 进入消息循环

