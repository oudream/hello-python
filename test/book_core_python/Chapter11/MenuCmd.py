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
		# 将菜单添加到窗口中
		self._obj_.SetMenu(menu)
		# 设置菜单处理消息
		self.HookCommand(self.MenuClick,1051)
		self.HookCommand(self.MenuClick,1052)
		self.HookCommand(self.MenuClick,1053)
		# 重载OnClose方法
	def OnClose(self):
		self.EndModalLoop(0)
	def MenuClick(self,lParam,wParam):
		# 根据lParam参数判断点击的菜单
		if lParam == 1051:
			self.MessageBox('Open','Python',MB_OK)
		elif lParam == 1053:
			self.MessageBox('Save','Python',MB_OK)
		else:
			self.OnClose()
w = MyWnd()											# 生成窗口对象
w.ShowWindow()											# 显示窗口
w.UpdateWindow()										# 刷新窗口
w.RunModalLoop(1)										# 进入消息循环


