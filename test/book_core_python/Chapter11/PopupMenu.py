# -*- coding:utf-8 -*-
# file: PopupMenu.py
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
		self.HookMessage(self.OnRClick,WM_RBUTTONDOWN)
	# 重载OnClose方法
	def OnClose(self):
		self.EndModalLoop(0)
	# 处理点击鼠标右键消息
	def OnRClick(self, param):
		submenu = win32ui.CreatePopupMenu()
		submenu.AppendMenu(MF_STRING,1054,'Copy')				# 向菜单中添加Copy
		submenu.AppendMenu(MF_STRING,1055,'Paste')				# 向菜单中添加Paste
		submenu.AppendMenu(MF_SEPARATOR,1056,None)				# 向菜单中添加分隔符
		submenu.AppendMenu(MF_STRING,1057,'Cut')				# 向菜单中添加Cut
		flag = TPM_LEFTALIGN|TPM_LEFTBUTTON|TPM_RIGHTBUTTON 			# 弹出式菜单样式
		submenu.TrackPopupMenu(param[5],flag,self)				# param为系统向OnRClick函数传递的参数，其为一个元组，其第6项为鼠标x，y坐标组成的元组
w = MyWnd()				# 生成窗口对象			
w.ShowWindow()				# 显示窗口
w.UpdateWindow()			# 刷新窗口
w.RunModalLoop(1)			# 进入消息循环
